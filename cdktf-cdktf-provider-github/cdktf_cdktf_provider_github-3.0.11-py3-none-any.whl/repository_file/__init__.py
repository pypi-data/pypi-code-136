'''
# `github_repository_file`

Refer to the Terraform Registory for docs: [`github_repository_file`](https://www.terraform.io/docs/providers/github/r/repository_file).
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
    jsii_type="@cdktf/provider-github.repositoryFile.RepositoryFile",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/repository_file github_repository_file}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        content: builtins.str,
        file: builtins.str,
        repository: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        commit_author: typing.Optional[builtins.str] = None,
        commit_email: typing.Optional[builtins.str] = None,
        commit_message: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        overwrite_on_create: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/repository_file github_repository_file} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param content: The file's content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#content RepositoryFile#content}
        :param file: The file path to manage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#file RepositoryFile#file}
        :param repository: The repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#repository RepositoryFile#repository}
        :param branch: The branch name, defaults to "main". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#branch RepositoryFile#branch}
        :param commit_author: The commit author name, defaults to the authenticated user's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_author RepositoryFile#commit_author}
        :param commit_email: The commit author email address, defaults to the authenticated user's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_email RepositoryFile#commit_email}
        :param commit_message: The commit message when creating or updating the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_message RepositoryFile#commit_message}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#id RepositoryFile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param overwrite_on_create: Enable overwriting existing files, defaults to "false". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#overwrite_on_create RepositoryFile#overwrite_on_create}
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
            content=content,
            file=file,
            repository=repository,
            branch=branch,
            commit_author=commit_author,
            commit_email=commit_email,
            commit_message=commit_message,
            id=id,
            overwrite_on_create=overwrite_on_create,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetCommitAuthor")
    def reset_commit_author(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitAuthor", []))

    @jsii.member(jsii_name="resetCommitEmail")
    def reset_commit_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitEmail", []))

    @jsii.member(jsii_name="resetCommitMessage")
    def reset_commit_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitMessage", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOverwriteOnCreate")
    def reset_overwrite_on_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwriteOnCreate", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="commitSha")
    def commit_sha(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitSha"))

    @builtins.property
    @jsii.member(jsii_name="sha")
    def sha(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha"))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="commitAuthorInput")
    def commit_author_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitAuthorInput"))

    @builtins.property
    @jsii.member(jsii_name="commitEmailInput")
    def commit_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="commitMessageInput")
    def commit_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteOnCreateInput")
    def overwrite_on_create_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overwriteOnCreateInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

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
    @jsii.member(jsii_name="commitAuthor")
    def commit_author(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitAuthor"))

    @commit_author.setter
    def commit_author(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "commit_author").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitAuthor", value)

    @builtins.property
    @jsii.member(jsii_name="commitEmail")
    def commit_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitEmail"))

    @commit_email.setter
    def commit_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "commit_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitEmail", value)

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
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

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
    @jsii.member(jsii_name="overwriteOnCreate")
    def overwrite_on_create(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overwriteOnCreate"))

    @overwrite_on_create.setter
    def overwrite_on_create(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "overwrite_on_create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwriteOnCreate", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryFile, "repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repositoryFile.RepositoryFileConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "content": "content",
        "file": "file",
        "repository": "repository",
        "branch": "branch",
        "commit_author": "commitAuthor",
        "commit_email": "commitEmail",
        "commit_message": "commitMessage",
        "id": "id",
        "overwrite_on_create": "overwriteOnCreate",
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
        content: builtins.str,
        file: builtins.str,
        repository: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        commit_author: typing.Optional[builtins.str] = None,
        commit_email: typing.Optional[builtins.str] = None,
        commit_message: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        overwrite_on_create: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param content: The file's content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#content RepositoryFile#content}
        :param file: The file path to manage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#file RepositoryFile#file}
        :param repository: The repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#repository RepositoryFile#repository}
        :param branch: The branch name, defaults to "main". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#branch RepositoryFile#branch}
        :param commit_author: The commit author name, defaults to the authenticated user's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_author RepositoryFile#commit_author}
        :param commit_email: The commit author email address, defaults to the authenticated user's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_email RepositoryFile#commit_email}
        :param commit_message: The commit message when creating or updating the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_message RepositoryFile#commit_message}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#id RepositoryFile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param overwrite_on_create: Enable overwriting existing files, defaults to "false". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#overwrite_on_create RepositoryFile#overwrite_on_create}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryFileConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument commit_author", value=commit_author, expected_type=type_hints["commit_author"])
            check_type(argname="argument commit_email", value=commit_email, expected_type=type_hints["commit_email"])
            check_type(argname="argument commit_message", value=commit_message, expected_type=type_hints["commit_message"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument overwrite_on_create", value=overwrite_on_create, expected_type=type_hints["overwrite_on_create"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "file": file,
            "repository": repository,
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
        if branch is not None:
            self._values["branch"] = branch
        if commit_author is not None:
            self._values["commit_author"] = commit_author
        if commit_email is not None:
            self._values["commit_email"] = commit_email
        if commit_message is not None:
            self._values["commit_message"] = commit_message
        if id is not None:
            self._values["id"] = id
        if overwrite_on_create is not None:
            self._values["overwrite_on_create"] = overwrite_on_create

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
    def content(self) -> builtins.str:
        '''The file's content.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#content RepositoryFile#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file(self) -> builtins.str:
        '''The file path to manage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#file RepositoryFile#file}
        '''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''The repository name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#repository RepositoryFile#repository}
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The branch name, defaults to "main".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#branch RepositoryFile#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit_author(self) -> typing.Optional[builtins.str]:
        '''The commit author name, defaults to the authenticated user's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_author RepositoryFile#commit_author}
        '''
        result = self._values.get("commit_author")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit_email(self) -> typing.Optional[builtins.str]:
        '''The commit author email address, defaults to the authenticated user's email address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_email RepositoryFile#commit_email}
        '''
        result = self._values.get("commit_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit_message(self) -> typing.Optional[builtins.str]:
        '''The commit message when creating or updating the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#commit_message RepositoryFile#commit_message}
        '''
        result = self._values.get("commit_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#id RepositoryFile#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_on_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable overwriting existing files, defaults to "false".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_file#overwrite_on_create RepositoryFile#overwrite_on_create}
        '''
        result = self._values.get("overwrite_on_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryFileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RepositoryFile",
    "RepositoryFileConfig",
]

publication.publish()
