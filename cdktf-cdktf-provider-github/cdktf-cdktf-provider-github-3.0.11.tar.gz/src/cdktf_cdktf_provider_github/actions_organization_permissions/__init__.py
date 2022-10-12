'''
# `github_actions_organization_permissions`

Refer to the Terraform Registory for docs: [`github_actions_organization_permissions`](https://www.terraform.io/docs/providers/github/r/actions_organization_permissions).
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


class ActionsOrganizationPermissions(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.actionsOrganizationPermissions.ActionsOrganizationPermissions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions github_actions_organization_permissions}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        enabled_repositories: builtins.str,
        allowed_actions: typing.Optional[builtins.str] = None,
        allowed_actions_config: typing.Optional[typing.Union["ActionsOrganizationPermissionsAllowedActionsConfig", typing.Dict[str, typing.Any]]] = None,
        enabled_repositories_config: typing.Optional[typing.Union["ActionsOrganizationPermissionsEnabledRepositoriesConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions github_actions_organization_permissions} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param enabled_repositories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#enabled_repositories ActionsOrganizationPermissions#enabled_repositories}.
        :param allowed_actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#allowed_actions ActionsOrganizationPermissions#allowed_actions}.
        :param allowed_actions_config: allowed_actions_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#allowed_actions_config ActionsOrganizationPermissions#allowed_actions_config}
        :param enabled_repositories_config: enabled_repositories_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#enabled_repositories_config ActionsOrganizationPermissions#enabled_repositories_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#id ActionsOrganizationPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ActionsOrganizationPermissions.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ActionsOrganizationPermissionsConfig(
            enabled_repositories=enabled_repositories,
            allowed_actions=allowed_actions,
            allowed_actions_config=allowed_actions_config,
            enabled_repositories_config=enabled_repositories_config,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAllowedActionsConfig")
    def put_allowed_actions_config(
        self,
        *,
        github_owned_allowed: typing.Union[builtins.bool, cdktf.IResolvable],
        patterns_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        verified_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param github_owned_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#github_owned_allowed ActionsOrganizationPermissions#github_owned_allowed}.
        :param patterns_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#patterns_allowed ActionsOrganizationPermissions#patterns_allowed}.
        :param verified_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#verified_allowed ActionsOrganizationPermissions#verified_allowed}.
        '''
        value = ActionsOrganizationPermissionsAllowedActionsConfig(
            github_owned_allowed=github_owned_allowed,
            patterns_allowed=patterns_allowed,
            verified_allowed=verified_allowed,
        )

        return typing.cast(None, jsii.invoke(self, "putAllowedActionsConfig", [value]))

    @jsii.member(jsii_name="putEnabledRepositoriesConfig")
    def put_enabled_repositories_config(
        self,
        *,
        repository_ids: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param repository_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#repository_ids ActionsOrganizationPermissions#repository_ids}.
        '''
        value = ActionsOrganizationPermissionsEnabledRepositoriesConfig(
            repository_ids=repository_ids
        )

        return typing.cast(None, jsii.invoke(self, "putEnabledRepositoriesConfig", [value]))

    @jsii.member(jsii_name="resetAllowedActions")
    def reset_allowed_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedActions", []))

    @jsii.member(jsii_name="resetAllowedActionsConfig")
    def reset_allowed_actions_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedActionsConfig", []))

    @jsii.member(jsii_name="resetEnabledRepositoriesConfig")
    def reset_enabled_repositories_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledRepositoriesConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowedActionsConfig")
    def allowed_actions_config(
        self,
    ) -> "ActionsOrganizationPermissionsAllowedActionsConfigOutputReference":
        return typing.cast("ActionsOrganizationPermissionsAllowedActionsConfigOutputReference", jsii.get(self, "allowedActionsConfig"))

    @builtins.property
    @jsii.member(jsii_name="enabledRepositoriesConfig")
    def enabled_repositories_config(
        self,
    ) -> "ActionsOrganizationPermissionsEnabledRepositoriesConfigOutputReference":
        return typing.cast("ActionsOrganizationPermissionsEnabledRepositoriesConfigOutputReference", jsii.get(self, "enabledRepositoriesConfig"))

    @builtins.property
    @jsii.member(jsii_name="allowedActionsConfigInput")
    def allowed_actions_config_input(
        self,
    ) -> typing.Optional["ActionsOrganizationPermissionsAllowedActionsConfig"]:
        return typing.cast(typing.Optional["ActionsOrganizationPermissionsAllowedActionsConfig"], jsii.get(self, "allowedActionsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedActionsInput")
    def allowed_actions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedActionsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledRepositoriesConfigInput")
    def enabled_repositories_config_input(
        self,
    ) -> typing.Optional["ActionsOrganizationPermissionsEnabledRepositoriesConfig"]:
        return typing.cast(typing.Optional["ActionsOrganizationPermissionsEnabledRepositoriesConfig"], jsii.get(self, "enabledRepositoriesConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledRepositoriesInput")
    def enabled_repositories_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledRepositoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedActions")
    def allowed_actions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowedActions"))

    @allowed_actions.setter
    def allowed_actions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissions, "allowed_actions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedActions", value)

    @builtins.property
    @jsii.member(jsii_name="enabledRepositories")
    def enabled_repositories(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabledRepositories"))

    @enabled_repositories.setter
    def enabled_repositories(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissions, "enabled_repositories").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledRepositories", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissions, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.actionsOrganizationPermissions.ActionsOrganizationPermissionsAllowedActionsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "github_owned_allowed": "githubOwnedAllowed",
        "patterns_allowed": "patternsAllowed",
        "verified_allowed": "verifiedAllowed",
    },
)
class ActionsOrganizationPermissionsAllowedActionsConfig:
    def __init__(
        self,
        *,
        github_owned_allowed: typing.Union[builtins.bool, cdktf.IResolvable],
        patterns_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        verified_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param github_owned_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#github_owned_allowed ActionsOrganizationPermissions#github_owned_allowed}.
        :param patterns_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#patterns_allowed ActionsOrganizationPermissions#patterns_allowed}.
        :param verified_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#verified_allowed ActionsOrganizationPermissions#verified_allowed}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ActionsOrganizationPermissionsAllowedActionsConfig.__init__)
            check_type(argname="argument github_owned_allowed", value=github_owned_allowed, expected_type=type_hints["github_owned_allowed"])
            check_type(argname="argument patterns_allowed", value=patterns_allowed, expected_type=type_hints["patterns_allowed"])
            check_type(argname="argument verified_allowed", value=verified_allowed, expected_type=type_hints["verified_allowed"])
        self._values: typing.Dict[str, typing.Any] = {
            "github_owned_allowed": github_owned_allowed,
        }
        if patterns_allowed is not None:
            self._values["patterns_allowed"] = patterns_allowed
        if verified_allowed is not None:
            self._values["verified_allowed"] = verified_allowed

    @builtins.property
    def github_owned_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#github_owned_allowed ActionsOrganizationPermissions#github_owned_allowed}.'''
        result = self._values.get("github_owned_allowed")
        assert result is not None, "Required property 'github_owned_allowed' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def patterns_allowed(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#patterns_allowed ActionsOrganizationPermissions#patterns_allowed}.'''
        result = self._values.get("patterns_allowed")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def verified_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#verified_allowed ActionsOrganizationPermissions#verified_allowed}.'''
        result = self._values.get("verified_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionsOrganizationPermissionsAllowedActionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ActionsOrganizationPermissionsAllowedActionsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.actionsOrganizationPermissions.ActionsOrganizationPermissionsAllowedActionsConfigOutputReference",
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
            type_hints = typing.get_type_hints(ActionsOrganizationPermissionsAllowedActionsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPatternsAllowed")
    def reset_patterns_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPatternsAllowed", []))

    @jsii.member(jsii_name="resetVerifiedAllowed")
    def reset_verified_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifiedAllowed", []))

    @builtins.property
    @jsii.member(jsii_name="githubOwnedAllowedInput")
    def github_owned_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "githubOwnedAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="patternsAllowedInput")
    def patterns_allowed_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patternsAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="verifiedAllowedInput")
    def verified_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifiedAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="githubOwnedAllowed")
    def github_owned_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "githubOwnedAllowed"))

    @github_owned_allowed.setter
    def github_owned_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissionsAllowedActionsConfigOutputReference, "github_owned_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubOwnedAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="patternsAllowed")
    def patterns_allowed(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "patternsAllowed"))

    @patterns_allowed.setter
    def patterns_allowed(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissionsAllowedActionsConfigOutputReference, "patterns_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patternsAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="verifiedAllowed")
    def verified_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifiedAllowed"))

    @verified_allowed.setter
    def verified_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissionsAllowedActionsConfigOutputReference, "verified_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifiedAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ActionsOrganizationPermissionsAllowedActionsConfig]:
        return typing.cast(typing.Optional[ActionsOrganizationPermissionsAllowedActionsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ActionsOrganizationPermissionsAllowedActionsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissionsAllowedActionsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.actionsOrganizationPermissions.ActionsOrganizationPermissionsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "enabled_repositories": "enabledRepositories",
        "allowed_actions": "allowedActions",
        "allowed_actions_config": "allowedActionsConfig",
        "enabled_repositories_config": "enabledRepositoriesConfig",
        "id": "id",
    },
)
class ActionsOrganizationPermissionsConfig(cdktf.TerraformMetaArguments):
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
        enabled_repositories: builtins.str,
        allowed_actions: typing.Optional[builtins.str] = None,
        allowed_actions_config: typing.Optional[typing.Union[ActionsOrganizationPermissionsAllowedActionsConfig, typing.Dict[str, typing.Any]]] = None,
        enabled_repositories_config: typing.Optional[typing.Union["ActionsOrganizationPermissionsEnabledRepositoriesConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param enabled_repositories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#enabled_repositories ActionsOrganizationPermissions#enabled_repositories}.
        :param allowed_actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#allowed_actions ActionsOrganizationPermissions#allowed_actions}.
        :param allowed_actions_config: allowed_actions_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#allowed_actions_config ActionsOrganizationPermissions#allowed_actions_config}
        :param enabled_repositories_config: enabled_repositories_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#enabled_repositories_config ActionsOrganizationPermissions#enabled_repositories_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#id ActionsOrganizationPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(allowed_actions_config, dict):
            allowed_actions_config = ActionsOrganizationPermissionsAllowedActionsConfig(**allowed_actions_config)
        if isinstance(enabled_repositories_config, dict):
            enabled_repositories_config = ActionsOrganizationPermissionsEnabledRepositoriesConfig(**enabled_repositories_config)
        if __debug__:
            type_hints = typing.get_type_hints(ActionsOrganizationPermissionsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument enabled_repositories", value=enabled_repositories, expected_type=type_hints["enabled_repositories"])
            check_type(argname="argument allowed_actions", value=allowed_actions, expected_type=type_hints["allowed_actions"])
            check_type(argname="argument allowed_actions_config", value=allowed_actions_config, expected_type=type_hints["allowed_actions_config"])
            check_type(argname="argument enabled_repositories_config", value=enabled_repositories_config, expected_type=type_hints["enabled_repositories_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled_repositories": enabled_repositories,
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
        if allowed_actions is not None:
            self._values["allowed_actions"] = allowed_actions
        if allowed_actions_config is not None:
            self._values["allowed_actions_config"] = allowed_actions_config
        if enabled_repositories_config is not None:
            self._values["enabled_repositories_config"] = enabled_repositories_config
        if id is not None:
            self._values["id"] = id

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
    def enabled_repositories(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#enabled_repositories ActionsOrganizationPermissions#enabled_repositories}.'''
        result = self._values.get("enabled_repositories")
        assert result is not None, "Required property 'enabled_repositories' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_actions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#allowed_actions ActionsOrganizationPermissions#allowed_actions}.'''
        result = self._values.get("allowed_actions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_actions_config(
        self,
    ) -> typing.Optional[ActionsOrganizationPermissionsAllowedActionsConfig]:
        '''allowed_actions_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#allowed_actions_config ActionsOrganizationPermissions#allowed_actions_config}
        '''
        result = self._values.get("allowed_actions_config")
        return typing.cast(typing.Optional[ActionsOrganizationPermissionsAllowedActionsConfig], result)

    @builtins.property
    def enabled_repositories_config(
        self,
    ) -> typing.Optional["ActionsOrganizationPermissionsEnabledRepositoriesConfig"]:
        '''enabled_repositories_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#enabled_repositories_config ActionsOrganizationPermissions#enabled_repositories_config}
        '''
        result = self._values.get("enabled_repositories_config")
        return typing.cast(typing.Optional["ActionsOrganizationPermissionsEnabledRepositoriesConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#id ActionsOrganizationPermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionsOrganizationPermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-github.actionsOrganizationPermissions.ActionsOrganizationPermissionsEnabledRepositoriesConfig",
    jsii_struct_bases=[],
    name_mapping={"repository_ids": "repositoryIds"},
)
class ActionsOrganizationPermissionsEnabledRepositoriesConfig:
    def __init__(self, *, repository_ids: typing.Sequence[jsii.Number]) -> None:
        '''
        :param repository_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#repository_ids ActionsOrganizationPermissions#repository_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ActionsOrganizationPermissionsEnabledRepositoriesConfig.__init__)
            check_type(argname="argument repository_ids", value=repository_ids, expected_type=type_hints["repository_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "repository_ids": repository_ids,
        }

    @builtins.property
    def repository_ids(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_permissions#repository_ids ActionsOrganizationPermissions#repository_ids}.'''
        result = self._values.get("repository_ids")
        assert result is not None, "Required property 'repository_ids' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionsOrganizationPermissionsEnabledRepositoriesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ActionsOrganizationPermissionsEnabledRepositoriesConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.actionsOrganizationPermissions.ActionsOrganizationPermissionsEnabledRepositoriesConfigOutputReference",
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
            type_hints = typing.get_type_hints(ActionsOrganizationPermissionsEnabledRepositoriesConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="repositoryIdsInput")
    def repository_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "repositoryIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryIds")
    def repository_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "repositoryIds"))

    @repository_ids.setter
    def repository_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissionsEnabledRepositoriesConfigOutputReference, "repository_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ActionsOrganizationPermissionsEnabledRepositoriesConfig]:
        return typing.cast(typing.Optional[ActionsOrganizationPermissionsEnabledRepositoriesConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ActionsOrganizationPermissionsEnabledRepositoriesConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationPermissionsEnabledRepositoriesConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ActionsOrganizationPermissions",
    "ActionsOrganizationPermissionsAllowedActionsConfig",
    "ActionsOrganizationPermissionsAllowedActionsConfigOutputReference",
    "ActionsOrganizationPermissionsConfig",
    "ActionsOrganizationPermissionsEnabledRepositoriesConfig",
    "ActionsOrganizationPermissionsEnabledRepositoriesConfigOutputReference",
]

publication.publish()
