'''
# `tfe_organization`

Refer to the Terraform Registory for docs: [`tfe_organization`](https://www.terraform.io/docs/providers/tfe/r/organization).
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


class Organization(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.organization.Organization",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tfe/r/organization tfe_organization}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        email: builtins.str,
        name: builtins.str,
        assessments_enforced: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        collaborator_auth_policy: typing.Optional[builtins.str] = None,
        cost_estimation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        owners_team_saml_role_id: typing.Optional[builtins.str] = None,
        send_passing_statuses_for_untriggered_speculative_plans: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        session_remember_minutes: typing.Optional[jsii.Number] = None,
        session_timeout_minutes: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tfe/r/organization tfe_organization} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#email Organization#email}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#name Organization#name}.
        :param assessments_enforced: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#assessments_enforced Organization#assessments_enforced}.
        :param collaborator_auth_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#collaborator_auth_policy Organization#collaborator_auth_policy}.
        :param cost_estimation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#cost_estimation_enabled Organization#cost_estimation_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#id Organization#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owners_team_saml_role_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#owners_team_saml_role_id Organization#owners_team_saml_role_id}.
        :param send_passing_statuses_for_untriggered_speculative_plans: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#send_passing_statuses_for_untriggered_speculative_plans Organization#send_passing_statuses_for_untriggered_speculative_plans}.
        :param session_remember_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#session_remember_minutes Organization#session_remember_minutes}.
        :param session_timeout_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#session_timeout_minutes Organization#session_timeout_minutes}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Organization.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OrganizationConfig(
            email=email,
            name=name,
            assessments_enforced=assessments_enforced,
            collaborator_auth_policy=collaborator_auth_policy,
            cost_estimation_enabled=cost_estimation_enabled,
            id=id,
            owners_team_saml_role_id=owners_team_saml_role_id,
            send_passing_statuses_for_untriggered_speculative_plans=send_passing_statuses_for_untriggered_speculative_plans,
            session_remember_minutes=session_remember_minutes,
            session_timeout_minutes=session_timeout_minutes,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAssessmentsEnforced")
    def reset_assessments_enforced(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssessmentsEnforced", []))

    @jsii.member(jsii_name="resetCollaboratorAuthPolicy")
    def reset_collaborator_auth_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollaboratorAuthPolicy", []))

    @jsii.member(jsii_name="resetCostEstimationEnabled")
    def reset_cost_estimation_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostEstimationEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOwnersTeamSamlRoleId")
    def reset_owners_team_saml_role_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwnersTeamSamlRoleId", []))

    @jsii.member(jsii_name="resetSendPassingStatusesForUntriggeredSpeculativePlans")
    def reset_send_passing_statuses_for_untriggered_speculative_plans(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendPassingStatusesForUntriggeredSpeculativePlans", []))

    @jsii.member(jsii_name="resetSessionRememberMinutes")
    def reset_session_remember_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionRememberMinutes", []))

    @jsii.member(jsii_name="resetSessionTimeoutMinutes")
    def reset_session_timeout_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionTimeoutMinutes", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="assessmentsEnforcedInput")
    def assessments_enforced_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "assessmentsEnforcedInput"))

    @builtins.property
    @jsii.member(jsii_name="collaboratorAuthPolicyInput")
    def collaborator_auth_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collaboratorAuthPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="costEstimationEnabledInput")
    def cost_estimation_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "costEstimationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownersTeamSamlRoleIdInput")
    def owners_team_saml_role_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownersTeamSamlRoleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sendPassingStatusesForUntriggeredSpeculativePlansInput")
    def send_passing_statuses_for_untriggered_speculative_plans_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sendPassingStatusesForUntriggeredSpeculativePlansInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionRememberMinutesInput")
    def session_remember_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionRememberMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutMinutesInput")
    def session_timeout_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionTimeoutMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="assessmentsEnforced")
    def assessments_enforced(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "assessmentsEnforced"))

    @assessments_enforced.setter
    def assessments_enforced(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "assessments_enforced").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assessmentsEnforced", value)

    @builtins.property
    @jsii.member(jsii_name="collaboratorAuthPolicy")
    def collaborator_auth_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collaboratorAuthPolicy"))

    @collaborator_auth_policy.setter
    def collaborator_auth_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "collaborator_auth_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collaboratorAuthPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="costEstimationEnabled")
    def cost_estimation_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "costEstimationEnabled"))

    @cost_estimation_enabled.setter
    def cost_estimation_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "cost_estimation_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "costEstimationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ownersTeamSamlRoleId")
    def owners_team_saml_role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownersTeamSamlRoleId"))

    @owners_team_saml_role_id.setter
    def owners_team_saml_role_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "owners_team_saml_role_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownersTeamSamlRoleId", value)

    @builtins.property
    @jsii.member(jsii_name="sendPassingStatusesForUntriggeredSpeculativePlans")
    def send_passing_statuses_for_untriggered_speculative_plans(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sendPassingStatusesForUntriggeredSpeculativePlans"))

    @send_passing_statuses_for_untriggered_speculative_plans.setter
    def send_passing_statuses_for_untriggered_speculative_plans(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "send_passing_statuses_for_untriggered_speculative_plans").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendPassingStatusesForUntriggeredSpeculativePlans", value)

    @builtins.property
    @jsii.member(jsii_name="sessionRememberMinutes")
    def session_remember_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionRememberMinutes"))

    @session_remember_minutes.setter
    def session_remember_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "session_remember_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionRememberMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutMinutes")
    def session_timeout_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionTimeoutMinutes"))

    @session_timeout_minutes.setter
    def session_timeout_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Organization, "session_timeout_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionTimeoutMinutes", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.organization.OrganizationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "email": "email",
        "name": "name",
        "assessments_enforced": "assessmentsEnforced",
        "collaborator_auth_policy": "collaboratorAuthPolicy",
        "cost_estimation_enabled": "costEstimationEnabled",
        "id": "id",
        "owners_team_saml_role_id": "ownersTeamSamlRoleId",
        "send_passing_statuses_for_untriggered_speculative_plans": "sendPassingStatusesForUntriggeredSpeculativePlans",
        "session_remember_minutes": "sessionRememberMinutes",
        "session_timeout_minutes": "sessionTimeoutMinutes",
    },
)
class OrganizationConfig(cdktf.TerraformMetaArguments):
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
        email: builtins.str,
        name: builtins.str,
        assessments_enforced: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        collaborator_auth_policy: typing.Optional[builtins.str] = None,
        cost_estimation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        owners_team_saml_role_id: typing.Optional[builtins.str] = None,
        send_passing_statuses_for_untriggered_speculative_plans: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        session_remember_minutes: typing.Optional[jsii.Number] = None,
        session_timeout_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#email Organization#email}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#name Organization#name}.
        :param assessments_enforced: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#assessments_enforced Organization#assessments_enforced}.
        :param collaborator_auth_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#collaborator_auth_policy Organization#collaborator_auth_policy}.
        :param cost_estimation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#cost_estimation_enabled Organization#cost_estimation_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#id Organization#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owners_team_saml_role_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#owners_team_saml_role_id Organization#owners_team_saml_role_id}.
        :param send_passing_statuses_for_untriggered_speculative_plans: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#send_passing_statuses_for_untriggered_speculative_plans Organization#send_passing_statuses_for_untriggered_speculative_plans}.
        :param session_remember_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#session_remember_minutes Organization#session_remember_minutes}.
        :param session_timeout_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#session_timeout_minutes Organization#session_timeout_minutes}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(OrganizationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument assessments_enforced", value=assessments_enforced, expected_type=type_hints["assessments_enforced"])
            check_type(argname="argument collaborator_auth_policy", value=collaborator_auth_policy, expected_type=type_hints["collaborator_auth_policy"])
            check_type(argname="argument cost_estimation_enabled", value=cost_estimation_enabled, expected_type=type_hints["cost_estimation_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument owners_team_saml_role_id", value=owners_team_saml_role_id, expected_type=type_hints["owners_team_saml_role_id"])
            check_type(argname="argument send_passing_statuses_for_untriggered_speculative_plans", value=send_passing_statuses_for_untriggered_speculative_plans, expected_type=type_hints["send_passing_statuses_for_untriggered_speculative_plans"])
            check_type(argname="argument session_remember_minutes", value=session_remember_minutes, expected_type=type_hints["session_remember_minutes"])
            check_type(argname="argument session_timeout_minutes", value=session_timeout_minutes, expected_type=type_hints["session_timeout_minutes"])
        self._values: typing.Dict[str, typing.Any] = {
            "email": email,
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
        if assessments_enforced is not None:
            self._values["assessments_enforced"] = assessments_enforced
        if collaborator_auth_policy is not None:
            self._values["collaborator_auth_policy"] = collaborator_auth_policy
        if cost_estimation_enabled is not None:
            self._values["cost_estimation_enabled"] = cost_estimation_enabled
        if id is not None:
            self._values["id"] = id
        if owners_team_saml_role_id is not None:
            self._values["owners_team_saml_role_id"] = owners_team_saml_role_id
        if send_passing_statuses_for_untriggered_speculative_plans is not None:
            self._values["send_passing_statuses_for_untriggered_speculative_plans"] = send_passing_statuses_for_untriggered_speculative_plans
        if session_remember_minutes is not None:
            self._values["session_remember_minutes"] = session_remember_minutes
        if session_timeout_minutes is not None:
            self._values["session_timeout_minutes"] = session_timeout_minutes

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
    def email(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#email Organization#email}.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#name Organization#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assessments_enforced(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#assessments_enforced Organization#assessments_enforced}.'''
        result = self._values.get("assessments_enforced")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def collaborator_auth_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#collaborator_auth_policy Organization#collaborator_auth_policy}.'''
        result = self._values.get("collaborator_auth_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cost_estimation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#cost_estimation_enabled Organization#cost_estimation_enabled}.'''
        result = self._values.get("cost_estimation_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#id Organization#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owners_team_saml_role_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#owners_team_saml_role_id Organization#owners_team_saml_role_id}.'''
        result = self._values.get("owners_team_saml_role_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def send_passing_statuses_for_untriggered_speculative_plans(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#send_passing_statuses_for_untriggered_speculative_plans Organization#send_passing_statuses_for_untriggered_speculative_plans}.'''
        result = self._values.get("send_passing_statuses_for_untriggered_speculative_plans")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def session_remember_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#session_remember_minutes Organization#session_remember_minutes}.'''
        result = self._values.get("session_remember_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def session_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/organization#session_timeout_minutes Organization#session_timeout_minutes}.'''
        result = self._values.get("session_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Organization",
    "OrganizationConfig",
]

publication.publish()
