'''
# `tfe_team`

Refer to the Terraform Registory for docs: [`tfe_team`](https://www.terraform.io/docs/providers/tfe/r/team).
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


class Team(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.team.Team",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tfe/r/team tfe_team}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        organization: builtins.str,
        id: typing.Optional[builtins.str] = None,
        organization_access: typing.Optional[typing.Union["TeamOrganizationAccess", typing.Dict[str, typing.Any]]] = None,
        sso_team_id: typing.Optional[builtins.str] = None,
        visibility: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tfe/r/team tfe_team} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#name Team#name}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#organization Team#organization}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#id Team#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param organization_access: organization_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#organization_access Team#organization_access}
        :param sso_team_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#sso_team_id Team#sso_team_id}.
        :param visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#visibility Team#visibility}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Team.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TeamConfig(
            name=name,
            organization=organization,
            id=id,
            organization_access=organization_access,
            sso_team_id=sso_team_id,
            visibility=visibility,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putOrganizationAccess")
    def put_organization_access(
        self,
        *,
        manage_modules: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_policies: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_policy_overrides: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_providers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_run_tasks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_vcs_settings: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_workspaces: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param manage_modules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_modules Team#manage_modules}.
        :param manage_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_policies Team#manage_policies}.
        :param manage_policy_overrides: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_policy_overrides Team#manage_policy_overrides}.
        :param manage_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_providers Team#manage_providers}.
        :param manage_run_tasks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_run_tasks Team#manage_run_tasks}.
        :param manage_vcs_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_vcs_settings Team#manage_vcs_settings}.
        :param manage_workspaces: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_workspaces Team#manage_workspaces}.
        '''
        value = TeamOrganizationAccess(
            manage_modules=manage_modules,
            manage_policies=manage_policies,
            manage_policy_overrides=manage_policy_overrides,
            manage_providers=manage_providers,
            manage_run_tasks=manage_run_tasks,
            manage_vcs_settings=manage_vcs_settings,
            manage_workspaces=manage_workspaces,
        )

        return typing.cast(None, jsii.invoke(self, "putOrganizationAccess", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOrganizationAccess")
    def reset_organization_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationAccess", []))

    @jsii.member(jsii_name="resetSsoTeamId")
    def reset_sso_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsoTeamId", []))

    @jsii.member(jsii_name="resetVisibility")
    def reset_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibility", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="organizationAccess")
    def organization_access(self) -> "TeamOrganizationAccessOutputReference":
        return typing.cast("TeamOrganizationAccessOutputReference", jsii.get(self, "organizationAccess"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationAccessInput")
    def organization_access_input(self) -> typing.Optional["TeamOrganizationAccess"]:
        return typing.cast(typing.Optional["TeamOrganizationAccess"], jsii.get(self, "organizationAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="ssoTeamIdInput")
    def sso_team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ssoTeamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityInput")
    def visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Team, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Team, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Team, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="ssoTeamId")
    def sso_team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssoTeamId"))

    @sso_team_id.setter
    def sso_team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Team, "sso_team_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssoTeamId", value)

    @builtins.property
    @jsii.member(jsii_name="visibility")
    def visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibility"))

    @visibility.setter
    def visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Team, "visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibility", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.team.TeamConfig",
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
        "id": "id",
        "organization_access": "organizationAccess",
        "sso_team_id": "ssoTeamId",
        "visibility": "visibility",
    },
)
class TeamConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        organization_access: typing.Optional[typing.Union["TeamOrganizationAccess", typing.Dict[str, typing.Any]]] = None,
        sso_team_id: typing.Optional[builtins.str] = None,
        visibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#name Team#name}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#organization Team#organization}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#id Team#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param organization_access: organization_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#organization_access Team#organization_access}
        :param sso_team_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#sso_team_id Team#sso_team_id}.
        :param visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#visibility Team#visibility}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(organization_access, dict):
            organization_access = TeamOrganizationAccess(**organization_access)
        if __debug__:
            type_hints = typing.get_type_hints(TeamConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument organization_access", value=organization_access, expected_type=type_hints["organization_access"])
            check_type(argname="argument sso_team_id", value=sso_team_id, expected_type=type_hints["sso_team_id"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
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
        if id is not None:
            self._values["id"] = id
        if organization_access is not None:
            self._values["organization_access"] = organization_access
        if sso_team_id is not None:
            self._values["sso_team_id"] = sso_team_id
        if visibility is not None:
            self._values["visibility"] = visibility

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#name Team#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#organization Team#organization}.'''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#id Team#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_access(self) -> typing.Optional["TeamOrganizationAccess"]:
        '''organization_access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#organization_access Team#organization_access}
        '''
        result = self._values.get("organization_access")
        return typing.cast(typing.Optional["TeamOrganizationAccess"], result)

    @builtins.property
    def sso_team_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#sso_team_id Team#sso_team_id}.'''
        result = self._values.get("sso_team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visibility(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#visibility Team#visibility}.'''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.team.TeamOrganizationAccess",
    jsii_struct_bases=[],
    name_mapping={
        "manage_modules": "manageModules",
        "manage_policies": "managePolicies",
        "manage_policy_overrides": "managePolicyOverrides",
        "manage_providers": "manageProviders",
        "manage_run_tasks": "manageRunTasks",
        "manage_vcs_settings": "manageVcsSettings",
        "manage_workspaces": "manageWorkspaces",
    },
)
class TeamOrganizationAccess:
    def __init__(
        self,
        *,
        manage_modules: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_policies: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_policy_overrides: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_providers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_run_tasks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_vcs_settings: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        manage_workspaces: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param manage_modules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_modules Team#manage_modules}.
        :param manage_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_policies Team#manage_policies}.
        :param manage_policy_overrides: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_policy_overrides Team#manage_policy_overrides}.
        :param manage_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_providers Team#manage_providers}.
        :param manage_run_tasks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_run_tasks Team#manage_run_tasks}.
        :param manage_vcs_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_vcs_settings Team#manage_vcs_settings}.
        :param manage_workspaces: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_workspaces Team#manage_workspaces}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamOrganizationAccess.__init__)
            check_type(argname="argument manage_modules", value=manage_modules, expected_type=type_hints["manage_modules"])
            check_type(argname="argument manage_policies", value=manage_policies, expected_type=type_hints["manage_policies"])
            check_type(argname="argument manage_policy_overrides", value=manage_policy_overrides, expected_type=type_hints["manage_policy_overrides"])
            check_type(argname="argument manage_providers", value=manage_providers, expected_type=type_hints["manage_providers"])
            check_type(argname="argument manage_run_tasks", value=manage_run_tasks, expected_type=type_hints["manage_run_tasks"])
            check_type(argname="argument manage_vcs_settings", value=manage_vcs_settings, expected_type=type_hints["manage_vcs_settings"])
            check_type(argname="argument manage_workspaces", value=manage_workspaces, expected_type=type_hints["manage_workspaces"])
        self._values: typing.Dict[str, typing.Any] = {}
        if manage_modules is not None:
            self._values["manage_modules"] = manage_modules
        if manage_policies is not None:
            self._values["manage_policies"] = manage_policies
        if manage_policy_overrides is not None:
            self._values["manage_policy_overrides"] = manage_policy_overrides
        if manage_providers is not None:
            self._values["manage_providers"] = manage_providers
        if manage_run_tasks is not None:
            self._values["manage_run_tasks"] = manage_run_tasks
        if manage_vcs_settings is not None:
            self._values["manage_vcs_settings"] = manage_vcs_settings
        if manage_workspaces is not None:
            self._values["manage_workspaces"] = manage_workspaces

    @builtins.property
    def manage_modules(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_modules Team#manage_modules}.'''
        result = self._values.get("manage_modules")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def manage_policies(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_policies Team#manage_policies}.'''
        result = self._values.get("manage_policies")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def manage_policy_overrides(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_policy_overrides Team#manage_policy_overrides}.'''
        result = self._values.get("manage_policy_overrides")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def manage_providers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_providers Team#manage_providers}.'''
        result = self._values.get("manage_providers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def manage_run_tasks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_run_tasks Team#manage_run_tasks}.'''
        result = self._values.get("manage_run_tasks")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def manage_vcs_settings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_vcs_settings Team#manage_vcs_settings}.'''
        result = self._values.get("manage_vcs_settings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def manage_workspaces(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/team#manage_workspaces Team#manage_workspaces}.'''
        result = self._values.get("manage_workspaces")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamOrganizationAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamOrganizationAccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.team.TeamOrganizationAccessOutputReference",
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
            type_hints = typing.get_type_hints(TeamOrganizationAccessOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetManageModules")
    def reset_manage_modules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageModules", []))

    @jsii.member(jsii_name="resetManagePolicies")
    def reset_manage_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagePolicies", []))

    @jsii.member(jsii_name="resetManagePolicyOverrides")
    def reset_manage_policy_overrides(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagePolicyOverrides", []))

    @jsii.member(jsii_name="resetManageProviders")
    def reset_manage_providers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageProviders", []))

    @jsii.member(jsii_name="resetManageRunTasks")
    def reset_manage_run_tasks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageRunTasks", []))

    @jsii.member(jsii_name="resetManageVcsSettings")
    def reset_manage_vcs_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageVcsSettings", []))

    @jsii.member(jsii_name="resetManageWorkspaces")
    def reset_manage_workspaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageWorkspaces", []))

    @builtins.property
    @jsii.member(jsii_name="manageModulesInput")
    def manage_modules_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "manageModulesInput"))

    @builtins.property
    @jsii.member(jsii_name="managePoliciesInput")
    def manage_policies_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "managePoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="managePolicyOverridesInput")
    def manage_policy_overrides_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "managePolicyOverridesInput"))

    @builtins.property
    @jsii.member(jsii_name="manageProvidersInput")
    def manage_providers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "manageProvidersInput"))

    @builtins.property
    @jsii.member(jsii_name="manageRunTasksInput")
    def manage_run_tasks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "manageRunTasksInput"))

    @builtins.property
    @jsii.member(jsii_name="manageVcsSettingsInput")
    def manage_vcs_settings_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "manageVcsSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="manageWorkspacesInput")
    def manage_workspaces_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "manageWorkspacesInput"))

    @builtins.property
    @jsii.member(jsii_name="manageModules")
    def manage_modules(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "manageModules"))

    @manage_modules.setter
    def manage_modules(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamOrganizationAccessOutputReference, "manage_modules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageModules", value)

    @builtins.property
    @jsii.member(jsii_name="managePolicies")
    def manage_policies(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "managePolicies"))

    @manage_policies.setter
    def manage_policies(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamOrganizationAccessOutputReference, "manage_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managePolicies", value)

    @builtins.property
    @jsii.member(jsii_name="managePolicyOverrides")
    def manage_policy_overrides(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "managePolicyOverrides"))

    @manage_policy_overrides.setter
    def manage_policy_overrides(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamOrganizationAccessOutputReference, "manage_policy_overrides").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managePolicyOverrides", value)

    @builtins.property
    @jsii.member(jsii_name="manageProviders")
    def manage_providers(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "manageProviders"))

    @manage_providers.setter
    def manage_providers(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamOrganizationAccessOutputReference, "manage_providers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageProviders", value)

    @builtins.property
    @jsii.member(jsii_name="manageRunTasks")
    def manage_run_tasks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "manageRunTasks"))

    @manage_run_tasks.setter
    def manage_run_tasks(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamOrganizationAccessOutputReference, "manage_run_tasks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageRunTasks", value)

    @builtins.property
    @jsii.member(jsii_name="manageVcsSettings")
    def manage_vcs_settings(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "manageVcsSettings"))

    @manage_vcs_settings.setter
    def manage_vcs_settings(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamOrganizationAccessOutputReference, "manage_vcs_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageVcsSettings", value)

    @builtins.property
    @jsii.member(jsii_name="manageWorkspaces")
    def manage_workspaces(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "manageWorkspaces"))

    @manage_workspaces.setter
    def manage_workspaces(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamOrganizationAccessOutputReference, "manage_workspaces").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageWorkspaces", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TeamOrganizationAccess]:
        return typing.cast(typing.Optional[TeamOrganizationAccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TeamOrganizationAccess]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamOrganizationAccessOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Team",
    "TeamConfig",
    "TeamOrganizationAccess",
    "TeamOrganizationAccessOutputReference",
]

publication.publish()
