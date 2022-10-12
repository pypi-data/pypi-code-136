'''
# `gitlab_repository_file`

Refer to the Terraform Registory for docs: [`gitlab_repository_file`](https://www.terraform.io/docs/providers/gitlab/r/repository_file).
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


class RepositoryFile(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.repositoryFile.RepositoryFile",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file gitlab_repository_file}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        branch: builtins.str,
        commit_message: builtins.str,
        content: builtins.str,
        file_path: builtins.str,
        project: builtins.str,
        author_email: typing.Optional[builtins.str] = None,
        author_name: typing.Optional[builtins.str] = None,
        execute_filemode: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        start_branch: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["RepositoryFileTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file gitlab_repository_file} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param branch: Name of the branch to which to commit to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#branch RepositoryFile#branch}
        :param commit_message: Commit message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#commit_message RepositoryFile#commit_message}
        :param content: File content. If the content is not yet base64 encoded, it will be encoded automatically. No other encoding is currently supported, because of a `GitLab API bug <https://gitlab.com/gitlab-org/gitlab/-/issues/342430>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#content RepositoryFile#content}
        :param file_path: The full path of the file. It must be relative to the root of the project without a leading slash ``/``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#file_path RepositoryFile#file_path}
        :param project: The name or ID of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#project RepositoryFile#project}
        :param author_email: Email of the commit author. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#author_email RepositoryFile#author_email}
        :param author_name: Name of the commit author. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#author_name RepositoryFile#author_name}
        :param execute_filemode: Enables or disables the execute flag on the file. **Note**: requires GitLab 14.10 or newer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#execute_filemode RepositoryFile#execute_filemode}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#id RepositoryFile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param start_branch: Name of the branch to start the new commit from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#start_branch RepositoryFile#start_branch}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#timeouts RepositoryFile#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryFile.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RepositoryFileConfig(
            branch=branch,
            commit_message=commit_message,
            content=content,
            file_path=file_path,
            project=project,
            author_email=author_email,
            author_name=author_name,
            execute_filemode=execute_filemode,
            id=id,
            start_branch=start_branch,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#create RepositoryFile#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#delete RepositoryFile#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#update RepositoryFile#update}.
        '''
        value = RepositoryFileTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuthorEmail")
    def reset_author_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorEmail", []))

    @jsii.member(jsii_name="resetAuthorName")
    def reset_author_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorName", []))

    @jsii.member(jsii_name="resetExecuteFilemode")
    def reset_execute_filemode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecuteFilemode", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetStartBranch")
    def reset_start_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartBranch", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="blobId")
    def blob_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobId"))

    @builtins.property
    @jsii.member(jsii_name="commitId")
    def commit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitId"))

    @builtins.property
    @jsii.member(jsii_name="contentSha256")
    def content_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentSha256"))

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @builtins.property
    @jsii.member(jsii_name="fileName")
    def file_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileName"))

    @builtins.property
    @jsii.member(jsii_name="lastCommitId")
    def last_commit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastCommitId"))

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "RepositoryFileTimeoutsOutputReference":
        return typing.cast("RepositoryFileTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authorEmailInput")
    def author_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="authorNameInput")
    def author_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorNameInput"))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="commitMessageInput")
    def commit_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="executeFilemodeInput")
    def execute_filemode_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "executeFilemodeInput"))

    @builtins.property
    @jsii.member(jsii_name="filePathInput")
    def file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filePathInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="startBranchInput")
    def start_branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startBranchInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["RepositoryFileTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["RepositoryFileTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorEmail")
    def author_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorEmail"))

    @author_email.setter
    def author_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "author_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorEmail", value)

    @builtins.property
    @jsii.member(jsii_name="authorName")
    def author_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorName"))

    @author_name.setter
    def author_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "author_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorName", value)

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="commitMessage")
    def commit_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitMessage"))

    @commit_message.setter
    def commit_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "commit_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitMessage", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="executeFilemode")
    def execute_filemode(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "executeFilemode"))

    @execute_filemode.setter
    def execute_filemode(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "execute_filemode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executeFilemode", value)

    @builtins.property
    @jsii.member(jsii_name="filePath")
    def file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filePath"))

    @file_path.setter
    def file_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "file_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filePath", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="startBranch")
    def start_branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startBranch"))

    @start_branch.setter
    def start_branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "start_branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startBranch", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.repositoryFile.RepositoryFileConfig",
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
        "commit_message": "commitMessage",
        "content": "content",
        "file_path": "filePath",
        "project": "project",
        "author_email": "authorEmail",
        "author_name": "authorName",
        "execute_filemode": "executeFilemode",
        "id": "id",
        "start_branch": "startBranch",
        "timeouts": "timeouts",
    },
)
class RepositoryFileConfig(cdktf.TerraformMetaArguments):
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
        commit_message: builtins.str,
        content: builtins.str,
        file_path: builtins.str,
        project: builtins.str,
        author_email: typing.Optional[builtins.str] = None,
        author_name: typing.Optional[builtins.str] = None,
        execute_filemode: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        start_branch: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["RepositoryFileTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param branch: Name of the branch to which to commit to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#branch RepositoryFile#branch}
        :param commit_message: Commit message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#commit_message RepositoryFile#commit_message}
        :param content: File content. If the content is not yet base64 encoded, it will be encoded automatically. No other encoding is currently supported, because of a `GitLab API bug <https://gitlab.com/gitlab-org/gitlab/-/issues/342430>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#content RepositoryFile#content}
        :param file_path: The full path of the file. It must be relative to the root of the project without a leading slash ``/``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#file_path RepositoryFile#file_path}
        :param project: The name or ID of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#project RepositoryFile#project}
        :param author_email: Email of the commit author. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#author_email RepositoryFile#author_email}
        :param author_name: Name of the commit author. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#author_name RepositoryFile#author_name}
        :param execute_filemode: Enables or disables the execute flag on the file. **Note**: requires GitLab 14.10 or newer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#execute_filemode RepositoryFile#execute_filemode}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#id RepositoryFile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param start_branch: Name of the branch to start the new commit from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#start_branch RepositoryFile#start_branch}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#timeouts RepositoryFile#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = RepositoryFileTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryFileConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument commit_message", value=commit_message, expected_type=type_hints["commit_message"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument author_email", value=author_email, expected_type=type_hints["author_email"])
            check_type(argname="argument author_name", value=author_name, expected_type=type_hints["author_name"])
            check_type(argname="argument execute_filemode", value=execute_filemode, expected_type=type_hints["execute_filemode"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument start_branch", value=start_branch, expected_type=type_hints["start_branch"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "branch": branch,
            "commit_message": commit_message,
            "content": content,
            "file_path": file_path,
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
        if author_email is not None:
            self._values["author_email"] = author_email
        if author_name is not None:
            self._values["author_name"] = author_name
        if execute_filemode is not None:
            self._values["execute_filemode"] = execute_filemode
        if id is not None:
            self._values["id"] = id
        if start_branch is not None:
            self._values["start_branch"] = start_branch
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
        '''Name of the branch to which to commit to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#branch RepositoryFile#branch}
        '''
        result = self._values.get("branch")
        assert result is not None, "Required property 'branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_message(self) -> builtins.str:
        '''Commit message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#commit_message RepositoryFile#commit_message}
        '''
        result = self._values.get("commit_message")
        assert result is not None, "Required property 'commit_message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> builtins.str:
        '''File content.

        If the content is not yet base64 encoded, it will be encoded automatically. No other encoding is currently supported, because of a `GitLab API bug <https://gitlab.com/gitlab-org/gitlab/-/issues/342430>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#content RepositoryFile#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_path(self) -> builtins.str:
        '''The full path of the file.

        It must be relative to the root of the project without a leading slash ``/``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#file_path RepositoryFile#file_path}
        '''
        result = self._values.get("file_path")
        assert result is not None, "Required property 'file_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or ID of the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#project RepositoryFile#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def author_email(self) -> typing.Optional[builtins.str]:
        '''Email of the commit author.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#author_email RepositoryFile#author_email}
        '''
        result = self._values.get("author_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def author_name(self) -> typing.Optional[builtins.str]:
        '''Name of the commit author.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#author_name RepositoryFile#author_name}
        '''
        result = self._values.get("author_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execute_filemode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables or disables the execute flag on the file. **Note**: requires GitLab 14.10 or newer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#execute_filemode RepositoryFile#execute_filemode}
        '''
        result = self._values.get("execute_filemode")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#id RepositoryFile#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_branch(self) -> typing.Optional[builtins.str]:
        '''Name of the branch to start the new commit from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#start_branch RepositoryFile#start_branch}
        '''
        result = self._values.get("start_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["RepositoryFileTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#timeouts RepositoryFile#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["RepositoryFileTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryFileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.repositoryFile.RepositoryFileTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class RepositoryFileTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#create RepositoryFile#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#delete RepositoryFile#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#update RepositoryFile#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryFileTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#create RepositoryFile#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#delete RepositoryFile#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/repository_file#update RepositoryFile#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryFileTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryFileTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.repositoryFile.RepositoryFileTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(RepositoryFileTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(RepositoryFileTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFileTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFileTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RepositoryFileTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RepositoryFileTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RepositoryFileTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFileTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RepositoryFile",
    "RepositoryFileConfig",
    "RepositoryFileTimeouts",
    "RepositoryFileTimeoutsOutputReference",
]

publication.publish()
