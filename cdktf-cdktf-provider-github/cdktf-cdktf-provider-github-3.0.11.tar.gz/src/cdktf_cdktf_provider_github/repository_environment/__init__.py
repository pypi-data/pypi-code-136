'''
# `github_repository_environment`

Refer to the Terraform Registory for docs: [`github_repository_environment`](https://www.terraform.io/docs/providers/github/r/repository_environment).
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


class RepositoryEnvironment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repositoryEnvironment.RepositoryEnvironment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/repository_environment github_repository_environment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        environment: builtins.str,
        repository: builtins.str,
        deployment_branch_policy: typing.Optional[typing.Union["RepositoryEnvironmentDeploymentBranchPolicy", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        reviewers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RepositoryEnvironmentReviewers", typing.Dict[str, typing.Any]]]]] = None,
        wait_timer: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/repository_environment github_repository_environment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#environment RepositoryEnvironment#environment}.
        :param repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#repository RepositoryEnvironment#repository}.
        :param deployment_branch_policy: deployment_branch_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#deployment_branch_policy RepositoryEnvironment#deployment_branch_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#id RepositoryEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param reviewers: reviewers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#reviewers RepositoryEnvironment#reviewers}
        :param wait_timer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#wait_timer RepositoryEnvironment#wait_timer}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryEnvironment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RepositoryEnvironmentConfig(
            environment=environment,
            repository=repository,
            deployment_branch_policy=deployment_branch_policy,
            id=id,
            reviewers=reviewers,
            wait_timer=wait_timer,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDeploymentBranchPolicy")
    def put_deployment_branch_policy(
        self,
        *,
        custom_branch_policies: typing.Union[builtins.bool, cdktf.IResolvable],
        protected_branches: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param custom_branch_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#custom_branch_policies RepositoryEnvironment#custom_branch_policies}.
        :param protected_branches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#protected_branches RepositoryEnvironment#protected_branches}.
        '''
        value = RepositoryEnvironmentDeploymentBranchPolicy(
            custom_branch_policies=custom_branch_policies,
            protected_branches=protected_branches,
        )

        return typing.cast(None, jsii.invoke(self, "putDeploymentBranchPolicy", [value]))

    @jsii.member(jsii_name="putReviewers")
    def put_reviewers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RepositoryEnvironmentReviewers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryEnvironment.put_reviewers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putReviewers", [value]))

    @jsii.member(jsii_name="resetDeploymentBranchPolicy")
    def reset_deployment_branch_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentBranchPolicy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetReviewers")
    def reset_reviewers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReviewers", []))

    @jsii.member(jsii_name="resetWaitTimer")
    def reset_wait_timer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitTimer", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="deploymentBranchPolicy")
    def deployment_branch_policy(
        self,
    ) -> "RepositoryEnvironmentDeploymentBranchPolicyOutputReference":
        return typing.cast("RepositoryEnvironmentDeploymentBranchPolicyOutputReference", jsii.get(self, "deploymentBranchPolicy"))

    @builtins.property
    @jsii.member(jsii_name="reviewers")
    def reviewers(self) -> "RepositoryEnvironmentReviewersList":
        return typing.cast("RepositoryEnvironmentReviewersList", jsii.get(self, "reviewers"))

    @builtins.property
    @jsii.member(jsii_name="deploymentBranchPolicyInput")
    def deployment_branch_policy_input(
        self,
    ) -> typing.Optional["RepositoryEnvironmentDeploymentBranchPolicy"]:
        return typing.cast(typing.Optional["RepositoryEnvironmentDeploymentBranchPolicy"], jsii.get(self, "deploymentBranchPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="reviewersInput")
    def reviewers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RepositoryEnvironmentReviewers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RepositoryEnvironmentReviewers"]]], jsii.get(self, "reviewersInput"))

    @builtins.property
    @jsii.member(jsii_name="waitTimerInput")
    def wait_timer_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitTimerInput"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironment, "environment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironment, "repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="waitTimer")
    def wait_timer(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitTimer"))

    @wait_timer.setter
    def wait_timer(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironment, "wait_timer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitTimer", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repositoryEnvironment.RepositoryEnvironmentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "environment": "environment",
        "repository": "repository",
        "deployment_branch_policy": "deploymentBranchPolicy",
        "id": "id",
        "reviewers": "reviewers",
        "wait_timer": "waitTimer",
    },
)
class RepositoryEnvironmentConfig(cdktf.TerraformMetaArguments):
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
        environment: builtins.str,
        repository: builtins.str,
        deployment_branch_policy: typing.Optional[typing.Union["RepositoryEnvironmentDeploymentBranchPolicy", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        reviewers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RepositoryEnvironmentReviewers", typing.Dict[str, typing.Any]]]]] = None,
        wait_timer: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#environment RepositoryEnvironment#environment}.
        :param repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#repository RepositoryEnvironment#repository}.
        :param deployment_branch_policy: deployment_branch_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#deployment_branch_policy RepositoryEnvironment#deployment_branch_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#id RepositoryEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param reviewers: reviewers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#reviewers RepositoryEnvironment#reviewers}
        :param wait_timer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#wait_timer RepositoryEnvironment#wait_timer}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(deployment_branch_policy, dict):
            deployment_branch_policy = RepositoryEnvironmentDeploymentBranchPolicy(**deployment_branch_policy)
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryEnvironmentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument deployment_branch_policy", value=deployment_branch_policy, expected_type=type_hints["deployment_branch_policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument reviewers", value=reviewers, expected_type=type_hints["reviewers"])
            check_type(argname="argument wait_timer", value=wait_timer, expected_type=type_hints["wait_timer"])
        self._values: typing.Dict[str, typing.Any] = {
            "environment": environment,
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
        if deployment_branch_policy is not None:
            self._values["deployment_branch_policy"] = deployment_branch_policy
        if id is not None:
            self._values["id"] = id
        if reviewers is not None:
            self._values["reviewers"] = reviewers
        if wait_timer is not None:
            self._values["wait_timer"] = wait_timer

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
    def environment(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#environment RepositoryEnvironment#environment}.'''
        result = self._values.get("environment")
        assert result is not None, "Required property 'environment' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#repository RepositoryEnvironment#repository}.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_branch_policy(
        self,
    ) -> typing.Optional["RepositoryEnvironmentDeploymentBranchPolicy"]:
        '''deployment_branch_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#deployment_branch_policy RepositoryEnvironment#deployment_branch_policy}
        '''
        result = self._values.get("deployment_branch_policy")
        return typing.cast(typing.Optional["RepositoryEnvironmentDeploymentBranchPolicy"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#id RepositoryEnvironment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reviewers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RepositoryEnvironmentReviewers"]]]:
        '''reviewers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#reviewers RepositoryEnvironment#reviewers}
        '''
        result = self._values.get("reviewers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RepositoryEnvironmentReviewers"]]], result)

    @builtins.property
    def wait_timer(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#wait_timer RepositoryEnvironment#wait_timer}.'''
        result = self._values.get("wait_timer")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryEnvironmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repositoryEnvironment.RepositoryEnvironmentDeploymentBranchPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "custom_branch_policies": "customBranchPolicies",
        "protected_branches": "protectedBranches",
    },
)
class RepositoryEnvironmentDeploymentBranchPolicy:
    def __init__(
        self,
        *,
        custom_branch_policies: typing.Union[builtins.bool, cdktf.IResolvable],
        protected_branches: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param custom_branch_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#custom_branch_policies RepositoryEnvironment#custom_branch_policies}.
        :param protected_branches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#protected_branches RepositoryEnvironment#protected_branches}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryEnvironmentDeploymentBranchPolicy.__init__)
            check_type(argname="argument custom_branch_policies", value=custom_branch_policies, expected_type=type_hints["custom_branch_policies"])
            check_type(argname="argument protected_branches", value=protected_branches, expected_type=type_hints["protected_branches"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_branch_policies": custom_branch_policies,
            "protected_branches": protected_branches,
        }

    @builtins.property
    def custom_branch_policies(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#custom_branch_policies RepositoryEnvironment#custom_branch_policies}.'''
        result = self._values.get("custom_branch_policies")
        assert result is not None, "Required property 'custom_branch_policies' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def protected_branches(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#protected_branches RepositoryEnvironment#protected_branches}.'''
        result = self._values.get("protected_branches")
        assert result is not None, "Required property 'protected_branches' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryEnvironmentDeploymentBranchPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryEnvironmentDeploymentBranchPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repositoryEnvironment.RepositoryEnvironmentDeploymentBranchPolicyOutputReference",
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
            type_hints = typing.get_type_hints(RepositoryEnvironmentDeploymentBranchPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="customBranchPoliciesInput")
    def custom_branch_policies_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "customBranchPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="protectedBranchesInput")
    def protected_branches_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "protectedBranchesInput"))

    @builtins.property
    @jsii.member(jsii_name="customBranchPolicies")
    def custom_branch_policies(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "customBranchPolicies"))

    @custom_branch_policies.setter
    def custom_branch_policies(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentDeploymentBranchPolicyOutputReference, "custom_branch_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customBranchPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="protectedBranches")
    def protected_branches(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "protectedBranches"))

    @protected_branches.setter
    def protected_branches(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentDeploymentBranchPolicyOutputReference, "protected_branches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedBranches", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RepositoryEnvironmentDeploymentBranchPolicy]:
        return typing.cast(typing.Optional[RepositoryEnvironmentDeploymentBranchPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RepositoryEnvironmentDeploymentBranchPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentDeploymentBranchPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repositoryEnvironment.RepositoryEnvironmentReviewers",
    jsii_struct_bases=[],
    name_mapping={"teams": "teams", "users": "users"},
)
class RepositoryEnvironmentReviewers:
    def __init__(
        self,
        *,
        teams: typing.Optional[typing.Sequence[jsii.Number]] = None,
        users: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param teams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#teams RepositoryEnvironment#teams}.
        :param users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#users RepositoryEnvironment#users}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryEnvironmentReviewers.__init__)
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[str, typing.Any] = {}
        if teams is not None:
            self._values["teams"] = teams
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def teams(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#teams RepositoryEnvironment#teams}.'''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository_environment#users RepositoryEnvironment#users}.'''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryEnvironmentReviewers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryEnvironmentReviewersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repositoryEnvironment.RepositoryEnvironmentReviewersList",
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
            type_hints = typing.get_type_hints(RepositoryEnvironmentReviewersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RepositoryEnvironmentReviewersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryEnvironmentReviewersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RepositoryEnvironmentReviewersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentReviewersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentReviewersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentReviewersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RepositoryEnvironmentReviewers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RepositoryEnvironmentReviewers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RepositoryEnvironmentReviewers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentReviewersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RepositoryEnvironmentReviewersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repositoryEnvironment.RepositoryEnvironmentReviewersOutputReference",
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
            type_hints = typing.get_type_hints(RepositoryEnvironmentReviewersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @jsii.member(jsii_name="resetUsers")
    def reset_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsers", []))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="usersInput")
    def users_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "usersInput"))

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "teams"))

    @teams.setter
    def teams(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentReviewersOutputReference, "teams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teams", value)

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "users"))

    @users.setter
    def users(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentReviewersOutputReference, "users").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RepositoryEnvironmentReviewers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RepositoryEnvironmentReviewers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RepositoryEnvironmentReviewers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryEnvironmentReviewersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RepositoryEnvironment",
    "RepositoryEnvironmentConfig",
    "RepositoryEnvironmentDeploymentBranchPolicy",
    "RepositoryEnvironmentDeploymentBranchPolicyOutputReference",
    "RepositoryEnvironmentReviewers",
    "RepositoryEnvironmentReviewersList",
    "RepositoryEnvironmentReviewersOutputReference",
]

publication.publish()
