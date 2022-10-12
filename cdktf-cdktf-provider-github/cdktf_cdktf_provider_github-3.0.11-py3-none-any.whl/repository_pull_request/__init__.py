'''
# `github_repository_pull_request`

Refer to the Terraform Registory for docs: [`github_repository_pull_request`](https://www.terraform.io/docs/providers/github/r/repository_pull_request).
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


class RepositoryPullRequest(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repositoryPullRequest.RepositoryPullRequest",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request github_repository_pull_request}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        base_ref: builtins.str,
        base_repository: builtins.str,
        head_ref: builtins.str,
        title: builtins.str,
        body: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        maintainer_can_modify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        owner: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request github_repository_pull_request} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param base_ref: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#base_ref RepositoryPullRequest#base_ref}.
        :param base_repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#base_repository RepositoryPullRequest#base_repository}.
        :param head_ref: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#head_ref RepositoryPullRequest#head_ref}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#title RepositoryPullRequest#title}.
        :param body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#body RepositoryPullRequest#body}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#id RepositoryPullRequest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintainer_can_modify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#maintainer_can_modify RepositoryPullRequest#maintainer_can_modify}.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#owner RepositoryPullRequest#owner}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryPullRequest.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RepositoryPullRequestConfig(
            base_ref=base_ref,
            base_repository=base_repository,
            head_ref=head_ref,
            title=title,
            body=body,
            id=id,
            maintainer_can_modify=maintainer_can_modify,
            owner=owner,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintainerCanModify")
    def reset_maintainer_can_modify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintainerCanModify", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="baseSha")
    def base_sha(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseSha"))

    @builtins.property
    @jsii.member(jsii_name="draft")
    def draft(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "draft"))

    @builtins.property
    @jsii.member(jsii_name="headSha")
    def head_sha(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headSha"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "number"))

    @builtins.property
    @jsii.member(jsii_name="openedAt")
    def opened_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "openedAt"))

    @builtins.property
    @jsii.member(jsii_name="openedBy")
    def opened_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "openedBy"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="baseRefInput")
    def base_ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseRefInput"))

    @builtins.property
    @jsii.member(jsii_name="baseRepositoryInput")
    def base_repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="headRefInput")
    def head_ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headRefInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maintainerCanModifyInput")
    def maintainer_can_modify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "maintainerCanModifyInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="baseRef")
    def base_ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseRef"))

    @base_ref.setter
    def base_ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPullRequest, "base_ref").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseRef", value)

    @builtins.property
    @jsii.member(jsii_name="baseRepository")
    def base_repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseRepository"))

    @base_repository.setter
    def base_repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPullRequest, "base_repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseRepository", value)

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPullRequest, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="headRef")
    def head_ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headRef"))

    @head_ref.setter
    def head_ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPullRequest, "head_ref").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headRef", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPullRequest, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maintainerCanModify")
    def maintainer_can_modify(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "maintainerCanModify"))

    @maintainer_can_modify.setter
    def maintainer_can_modify(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPullRequest, "maintainer_can_modify").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintainerCanModify", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPullRequest, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPullRequest, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repositoryPullRequest.RepositoryPullRequestConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "base_ref": "baseRef",
        "base_repository": "baseRepository",
        "head_ref": "headRef",
        "title": "title",
        "body": "body",
        "id": "id",
        "maintainer_can_modify": "maintainerCanModify",
        "owner": "owner",
    },
)
class RepositoryPullRequestConfig(cdktf.TerraformMetaArguments):
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
        base_ref: builtins.str,
        base_repository: builtins.str,
        head_ref: builtins.str,
        title: builtins.str,
        body: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        maintainer_can_modify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        owner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param base_ref: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#base_ref RepositoryPullRequest#base_ref}.
        :param base_repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#base_repository RepositoryPullRequest#base_repository}.
        :param head_ref: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#head_ref RepositoryPullRequest#head_ref}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#title RepositoryPullRequest#title}.
        :param body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#body RepositoryPullRequest#body}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#id RepositoryPullRequest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintainer_can_modify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#maintainer_can_modify RepositoryPullRequest#maintainer_can_modify}.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#owner RepositoryPullRequest#owner}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryPullRequestConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument base_ref", value=base_ref, expected_type=type_hints["base_ref"])
            check_type(argname="argument base_repository", value=base_repository, expected_type=type_hints["base_repository"])
            check_type(argname="argument head_ref", value=head_ref, expected_type=type_hints["head_ref"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintainer_can_modify", value=maintainer_can_modify, expected_type=type_hints["maintainer_can_modify"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_ref": base_ref,
            "base_repository": base_repository,
            "head_ref": head_ref,
            "title": title,
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
        if body is not None:
            self._values["body"] = body
        if id is not None:
            self._values["id"] = id
        if maintainer_can_modify is not None:
            self._values["maintainer_can_modify"] = maintainer_can_modify
        if owner is not None:
            self._values["owner"] = owner

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
    def base_ref(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#base_ref RepositoryPullRequest#base_ref}.'''
        result = self._values.get("base_ref")
        assert result is not None, "Required property 'base_ref' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_repository(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#base_repository RepositoryPullRequest#base_repository}.'''
        result = self._values.get("base_repository")
        assert result is not None, "Required property 'base_repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def head_ref(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#head_ref RepositoryPullRequest#head_ref}.'''
        result = self._values.get("head_ref")
        assert result is not None, "Required property 'head_ref' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#title RepositoryPullRequest#title}.'''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#body RepositoryPullRequest#body}.'''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#id RepositoryPullRequest#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintainer_can_modify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#maintainer_can_modify RepositoryPullRequest#maintainer_can_modify}.'''
        result = self._values.get("maintainer_can_modify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_pull_request#owner RepositoryPullRequest#owner}.'''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryPullRequestConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RepositoryPullRequest",
    "RepositoryPullRequestConfig",
]

publication.publish()
