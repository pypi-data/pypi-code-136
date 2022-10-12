'''
# `tfe_policy_set`

Refer to the Terraform Registory for docs: [`tfe_policy_set`](https://www.terraform.io/docs/providers/tfe/r/policy_set).
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


class PolicySet(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.policySet.PolicySet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tfe/r/policy_set tfe_policy_set}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        organization: builtins.str,
        description: typing.Optional[builtins.str] = None,
        global_: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        policies_path: typing.Optional[builtins.str] = None,
        policy_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        slug: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vcs_repo: typing.Optional[typing.Union["PolicySetVcsRepo", typing.Dict[str, typing.Any]]] = None,
        workspace_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tfe/r/policy_set tfe_policy_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#name PolicySet#name}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#organization PolicySet#organization}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#description PolicySet#description}.
        :param global_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#global PolicySet#global}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#id PolicySet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policies_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#policies_path PolicySet#policies_path}.
        :param policy_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#policy_ids PolicySet#policy_ids}.
        :param slug: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#slug PolicySet#slug}.
        :param vcs_repo: vcs_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#vcs_repo PolicySet#vcs_repo}
        :param workspace_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#workspace_ids PolicySet#workspace_ids}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PolicySet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PolicySetConfig(
            name=name,
            organization=organization,
            description=description,
            global_=global_,
            id=id,
            policies_path=policies_path,
            policy_ids=policy_ids,
            slug=slug,
            vcs_repo=vcs_repo,
            workspace_ids=workspace_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putVcsRepo")
    def put_vcs_repo(
        self,
        *,
        identifier: builtins.str,
        oauth_token_id: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        ingress_submodules: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#identifier PolicySet#identifier}.
        :param oauth_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#oauth_token_id PolicySet#oauth_token_id}.
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#branch PolicySet#branch}.
        :param ingress_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#ingress_submodules PolicySet#ingress_submodules}.
        '''
        value = PolicySetVcsRepo(
            identifier=identifier,
            oauth_token_id=oauth_token_id,
            branch=branch,
            ingress_submodules=ingress_submodules,
        )

        return typing.cast(None, jsii.invoke(self, "putVcsRepo", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetGlobal")
    def reset_global(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobal", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPoliciesPath")
    def reset_policies_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoliciesPath", []))

    @jsii.member(jsii_name="resetPolicyIds")
    def reset_policy_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyIds", []))

    @jsii.member(jsii_name="resetSlug")
    def reset_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlug", []))

    @jsii.member(jsii_name="resetVcsRepo")
    def reset_vcs_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVcsRepo", []))

    @jsii.member(jsii_name="resetWorkspaceIds")
    def reset_workspace_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceIds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="vcsRepo")
    def vcs_repo(self) -> "PolicySetVcsRepoOutputReference":
        return typing.cast("PolicySetVcsRepoOutputReference", jsii.get(self, "vcsRepo"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="globalInput")
    def global_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "globalInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="policiesPathInput")
    def policies_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policiesPathInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdsInput")
    def policy_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policyIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="slugInput")
    def slug_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "slugInput"))

    @builtins.property
    @jsii.member(jsii_name="vcsRepoInput")
    def vcs_repo_input(self) -> typing.Optional["PolicySetVcsRepo"]:
        return typing.cast(typing.Optional["PolicySetVcsRepo"], jsii.get(self, "vcsRepoInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdsInput")
    def workspace_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "workspaceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="global")
    def global_(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "global"))

    @global_.setter
    def global_(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "global_").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "global", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="policiesPath")
    def policies_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policiesPath"))

    @policies_path.setter
    def policies_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "policies_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policiesPath", value)

    @builtins.property
    @jsii.member(jsii_name="policyIds")
    def policy_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policyIds"))

    @policy_ids.setter
    def policy_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "policy_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyIds", value)

    @builtins.property
    @jsii.member(jsii_name="slug")
    def slug(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "slug"))

    @slug.setter
    def slug(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "slug").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slug", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceIds")
    def workspace_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "workspaceIds"))

    @workspace_ids.setter
    def workspace_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySet, "workspace_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.policySet.PolicySetConfig",
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
        "organization": "organization",
        "description": "description",
        "global_": "global",
        "id": "id",
        "policies_path": "policiesPath",
        "policy_ids": "policyIds",
        "slug": "slug",
        "vcs_repo": "vcsRepo",
        "workspace_ids": "workspaceIds",
    },
)
class PolicySetConfig(cdktf.TerraformMetaArguments):
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
        organization: builtins.str,
        description: typing.Optional[builtins.str] = None,
        global_: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        policies_path: typing.Optional[builtins.str] = None,
        policy_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        slug: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vcs_repo: typing.Optional[typing.Union["PolicySetVcsRepo", typing.Dict[str, typing.Any]]] = None,
        workspace_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#name PolicySet#name}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#organization PolicySet#organization}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#description PolicySet#description}.
        :param global_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#global PolicySet#global}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#id PolicySet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policies_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#policies_path PolicySet#policies_path}.
        :param policy_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#policy_ids PolicySet#policy_ids}.
        :param slug: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#slug PolicySet#slug}.
        :param vcs_repo: vcs_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#vcs_repo PolicySet#vcs_repo}
        :param workspace_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#workspace_ids PolicySet#workspace_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(vcs_repo, dict):
            vcs_repo = PolicySetVcsRepo(**vcs_repo)
        if __debug__:
            type_hints = typing.get_type_hints(PolicySetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument policies_path", value=policies_path, expected_type=type_hints["policies_path"])
            check_type(argname="argument policy_ids", value=policy_ids, expected_type=type_hints["policy_ids"])
            check_type(argname="argument slug", value=slug, expected_type=type_hints["slug"])
            check_type(argname="argument vcs_repo", value=vcs_repo, expected_type=type_hints["vcs_repo"])
            check_type(argname="argument workspace_ids", value=workspace_ids, expected_type=type_hints["workspace_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "organization": organization,
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
        if description is not None:
            self._values["description"] = description
        if global_ is not None:
            self._values["global_"] = global_
        if id is not None:
            self._values["id"] = id
        if policies_path is not None:
            self._values["policies_path"] = policies_path
        if policy_ids is not None:
            self._values["policy_ids"] = policy_ids
        if slug is not None:
            self._values["slug"] = slug
        if vcs_repo is not None:
            self._values["vcs_repo"] = vcs_repo
        if workspace_ids is not None:
            self._values["workspace_ids"] = workspace_ids

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#name PolicySet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#organization PolicySet#organization}.'''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#description PolicySet#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#global PolicySet#global}.'''
        result = self._values.get("global_")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#id PolicySet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#policies_path PolicySet#policies_path}.'''
        result = self._values.get("policies_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#policy_ids PolicySet#policy_ids}.'''
        result = self._values.get("policy_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slug(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#slug PolicySet#slug}.'''
        result = self._values.get("slug")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vcs_repo(self) -> typing.Optional["PolicySetVcsRepo"]:
        '''vcs_repo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#vcs_repo PolicySet#vcs_repo}
        '''
        result = self._values.get("vcs_repo")
        return typing.cast(typing.Optional["PolicySetVcsRepo"], result)

    @builtins.property
    def workspace_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#workspace_ids PolicySet#workspace_ids}.'''
        result = self._values.get("workspace_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicySetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.policySet.PolicySetVcsRepo",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "oauth_token_id": "oauthTokenId",
        "branch": "branch",
        "ingress_submodules": "ingressSubmodules",
    },
)
class PolicySetVcsRepo:
    def __init__(
        self,
        *,
        identifier: builtins.str,
        oauth_token_id: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        ingress_submodules: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#identifier PolicySet#identifier}.
        :param oauth_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#oauth_token_id PolicySet#oauth_token_id}.
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#branch PolicySet#branch}.
        :param ingress_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#ingress_submodules PolicySet#ingress_submodules}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PolicySetVcsRepo.__init__)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument oauth_token_id", value=oauth_token_id, expected_type=type_hints["oauth_token_id"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument ingress_submodules", value=ingress_submodules, expected_type=type_hints["ingress_submodules"])
        self._values: typing.Dict[str, typing.Any] = {
            "identifier": identifier,
            "oauth_token_id": oauth_token_id,
        }
        if branch is not None:
            self._values["branch"] = branch
        if ingress_submodules is not None:
            self._values["ingress_submodules"] = ingress_submodules

    @builtins.property
    def identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#identifier PolicySet#identifier}.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth_token_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#oauth_token_id PolicySet#oauth_token_id}.'''
        result = self._values.get("oauth_token_id")
        assert result is not None, "Required property 'oauth_token_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#branch PolicySet#branch}.'''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_submodules(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/policy_set#ingress_submodules PolicySet#ingress_submodules}.'''
        result = self._values.get("ingress_submodules")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicySetVcsRepo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PolicySetVcsRepoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.policySet.PolicySetVcsRepoOutputReference",
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
            type_hints = typing.get_type_hints(PolicySetVcsRepoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetIngressSubmodules")
    def reset_ingress_submodules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressSubmodules", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressSubmodulesInput")
    def ingress_submodules_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ingressSubmodulesInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthTokenIdInput")
    def oauth_token_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthTokenIdInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySetVcsRepoOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySetVcsRepoOutputReference, "identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="ingressSubmodules")
    def ingress_submodules(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ingressSubmodules"))

    @ingress_submodules.setter
    def ingress_submodules(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySetVcsRepoOutputReference, "ingress_submodules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressSubmodules", value)

    @builtins.property
    @jsii.member(jsii_name="oauthTokenId")
    def oauth_token_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauthTokenId"))

    @oauth_token_id.setter
    def oauth_token_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySetVcsRepoOutputReference, "oauth_token_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthTokenId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PolicySetVcsRepo]:
        return typing.cast(typing.Optional[PolicySetVcsRepo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PolicySetVcsRepo]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PolicySetVcsRepoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PolicySet",
    "PolicySetConfig",
    "PolicySetVcsRepo",
    "PolicySetVcsRepoOutputReference",
]

publication.publish()
