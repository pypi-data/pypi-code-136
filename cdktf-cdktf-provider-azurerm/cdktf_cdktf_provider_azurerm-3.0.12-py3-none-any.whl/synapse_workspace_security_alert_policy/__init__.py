'''
# `azurerm_synapse_workspace_security_alert_policy`

Refer to the Terraform Registory for docs: [`azurerm_synapse_workspace_security_alert_policy`](https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy).
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


class SynapseWorkspaceSecurityAlertPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspaceSecurityAlertPolicy.SynapseWorkspaceSecurityAlertPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy azurerm_synapse_workspace_security_alert_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        policy_state: builtins.str,
        synapse_workspace_id: builtins.str,
        disabled_alerts: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_account_admins_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[jsii.Number] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_endpoint: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SynapseWorkspaceSecurityAlertPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy azurerm_synapse_workspace_security_alert_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param policy_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#policy_state SynapseWorkspaceSecurityAlertPolicy#policy_state}.
        :param synapse_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#synapse_workspace_id SynapseWorkspaceSecurityAlertPolicy#synapse_workspace_id}.
        :param disabled_alerts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#disabled_alerts SynapseWorkspaceSecurityAlertPolicy#disabled_alerts}.
        :param email_account_admins_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#email_account_admins_enabled SynapseWorkspaceSecurityAlertPolicy#email_account_admins_enabled}.
        :param email_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#email_addresses SynapseWorkspaceSecurityAlertPolicy#email_addresses}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#id SynapseWorkspaceSecurityAlertPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#retention_days SynapseWorkspaceSecurityAlertPolicy#retention_days}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#storage_account_access_key SynapseWorkspaceSecurityAlertPolicy#storage_account_access_key}.
        :param storage_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#storage_endpoint SynapseWorkspaceSecurityAlertPolicy#storage_endpoint}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#timeouts SynapseWorkspaceSecurityAlertPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceSecurityAlertPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SynapseWorkspaceSecurityAlertPolicyConfig(
            policy_state=policy_state,
            synapse_workspace_id=synapse_workspace_id,
            disabled_alerts=disabled_alerts,
            email_account_admins_enabled=email_account_admins_enabled,
            email_addresses=email_addresses,
            id=id,
            retention_days=retention_days,
            storage_account_access_key=storage_account_access_key,
            storage_endpoint=storage_endpoint,
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
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#create SynapseWorkspaceSecurityAlertPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#delete SynapseWorkspaceSecurityAlertPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#read SynapseWorkspaceSecurityAlertPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#update SynapseWorkspaceSecurityAlertPolicy#update}.
        '''
        value = SynapseWorkspaceSecurityAlertPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDisabledAlerts")
    def reset_disabled_alerts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabledAlerts", []))

    @jsii.member(jsii_name="resetEmailAccountAdminsEnabled")
    def reset_email_account_admins_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAccountAdminsEnabled", []))

    @jsii.member(jsii_name="resetEmailAddresses")
    def reset_email_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAddresses", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRetentionDays")
    def reset_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionDays", []))

    @jsii.member(jsii_name="resetStorageAccountAccessKey")
    def reset_storage_account_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountAccessKey", []))

    @jsii.member(jsii_name="resetStorageEndpoint")
    def reset_storage_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageEndpoint", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference":
        return typing.cast("SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="disabledAlertsInput")
    def disabled_alerts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disabledAlertsInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAccountAdminsEnabledInput")
    def email_account_admins_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "emailAccountAdminsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressesInput")
    def email_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="policyStateInput")
    def policy_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyStateInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaysInput")
    def retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKeyInput")
    def storage_account_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageEndpointInput")
    def storage_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="synapseWorkspaceIdInput")
    def synapse_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "synapseWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SynapseWorkspaceSecurityAlertPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SynapseWorkspaceSecurityAlertPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledAlerts")
    def disabled_alerts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disabledAlerts"))

    @disabled_alerts.setter
    def disabled_alerts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "disabled_alerts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabledAlerts", value)

    @builtins.property
    @jsii.member(jsii_name="emailAccountAdminsEnabled")
    def email_account_admins_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "emailAccountAdminsEnabled"))

    @email_account_admins_enabled.setter
    def email_account_admins_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "email_account_admins_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAccountAdminsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddresses")
    def email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailAddresses"))

    @email_addresses.setter
    def email_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "email_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="policyState")
    def policy_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyState"))

    @policy_state.setter
    def policy_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "policy_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyState", value)

    @builtins.property
    @jsii.member(jsii_name="retentionDays")
    def retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionDays"))

    @retention_days.setter
    def retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKey")
    def storage_account_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountAccessKey"))

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "storage_account_access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageEndpoint")
    def storage_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageEndpoint"))

    @storage_endpoint.setter
    def storage_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "storage_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="synapseWorkspaceId")
    def synapse_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "synapseWorkspaceId"))

    @synapse_workspace_id.setter
    def synapse_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicy, "synapse_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "synapseWorkspaceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspaceSecurityAlertPolicy.SynapseWorkspaceSecurityAlertPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "policy_state": "policyState",
        "synapse_workspace_id": "synapseWorkspaceId",
        "disabled_alerts": "disabledAlerts",
        "email_account_admins_enabled": "emailAccountAdminsEnabled",
        "email_addresses": "emailAddresses",
        "id": "id",
        "retention_days": "retentionDays",
        "storage_account_access_key": "storageAccountAccessKey",
        "storage_endpoint": "storageEndpoint",
        "timeouts": "timeouts",
    },
)
class SynapseWorkspaceSecurityAlertPolicyConfig(cdktf.TerraformMetaArguments):
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
        policy_state: builtins.str,
        synapse_workspace_id: builtins.str,
        disabled_alerts: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_account_admins_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[jsii.Number] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_endpoint: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SynapseWorkspaceSecurityAlertPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param policy_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#policy_state SynapseWorkspaceSecurityAlertPolicy#policy_state}.
        :param synapse_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#synapse_workspace_id SynapseWorkspaceSecurityAlertPolicy#synapse_workspace_id}.
        :param disabled_alerts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#disabled_alerts SynapseWorkspaceSecurityAlertPolicy#disabled_alerts}.
        :param email_account_admins_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#email_account_admins_enabled SynapseWorkspaceSecurityAlertPolicy#email_account_admins_enabled}.
        :param email_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#email_addresses SynapseWorkspaceSecurityAlertPolicy#email_addresses}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#id SynapseWorkspaceSecurityAlertPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#retention_days SynapseWorkspaceSecurityAlertPolicy#retention_days}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#storage_account_access_key SynapseWorkspaceSecurityAlertPolicy#storage_account_access_key}.
        :param storage_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#storage_endpoint SynapseWorkspaceSecurityAlertPolicy#storage_endpoint}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#timeouts SynapseWorkspaceSecurityAlertPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SynapseWorkspaceSecurityAlertPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceSecurityAlertPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument policy_state", value=policy_state, expected_type=type_hints["policy_state"])
            check_type(argname="argument synapse_workspace_id", value=synapse_workspace_id, expected_type=type_hints["synapse_workspace_id"])
            check_type(argname="argument disabled_alerts", value=disabled_alerts, expected_type=type_hints["disabled_alerts"])
            check_type(argname="argument email_account_admins_enabled", value=email_account_admins_enabled, expected_type=type_hints["email_account_admins_enabled"])
            check_type(argname="argument email_addresses", value=email_addresses, expected_type=type_hints["email_addresses"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
            check_type(argname="argument storage_account_access_key", value=storage_account_access_key, expected_type=type_hints["storage_account_access_key"])
            check_type(argname="argument storage_endpoint", value=storage_endpoint, expected_type=type_hints["storage_endpoint"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy_state": policy_state,
            "synapse_workspace_id": synapse_workspace_id,
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
        if disabled_alerts is not None:
            self._values["disabled_alerts"] = disabled_alerts
        if email_account_admins_enabled is not None:
            self._values["email_account_admins_enabled"] = email_account_admins_enabled
        if email_addresses is not None:
            self._values["email_addresses"] = email_addresses
        if id is not None:
            self._values["id"] = id
        if retention_days is not None:
            self._values["retention_days"] = retention_days
        if storage_account_access_key is not None:
            self._values["storage_account_access_key"] = storage_account_access_key
        if storage_endpoint is not None:
            self._values["storage_endpoint"] = storage_endpoint
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
    def policy_state(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#policy_state SynapseWorkspaceSecurityAlertPolicy#policy_state}.'''
        result = self._values.get("policy_state")
        assert result is not None, "Required property 'policy_state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def synapse_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#synapse_workspace_id SynapseWorkspaceSecurityAlertPolicy#synapse_workspace_id}.'''
        result = self._values.get("synapse_workspace_id")
        assert result is not None, "Required property 'synapse_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled_alerts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#disabled_alerts SynapseWorkspaceSecurityAlertPolicy#disabled_alerts}.'''
        result = self._values.get("disabled_alerts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_account_admins_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#email_account_admins_enabled SynapseWorkspaceSecurityAlertPolicy#email_account_admins_enabled}.'''
        result = self._values.get("email_account_admins_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def email_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#email_addresses SynapseWorkspaceSecurityAlertPolicy#email_addresses}.'''
        result = self._values.get("email_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#id SynapseWorkspaceSecurityAlertPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#retention_days SynapseWorkspaceSecurityAlertPolicy#retention_days}.'''
        result = self._values.get("retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_account_access_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#storage_account_access_key SynapseWorkspaceSecurityAlertPolicy#storage_account_access_key}.'''
        result = self._values.get("storage_account_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#storage_endpoint SynapseWorkspaceSecurityAlertPolicy#storage_endpoint}.'''
        result = self._values.get("storage_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["SynapseWorkspaceSecurityAlertPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#timeouts SynapseWorkspaceSecurityAlertPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SynapseWorkspaceSecurityAlertPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceSecurityAlertPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspaceSecurityAlertPolicy.SynapseWorkspaceSecurityAlertPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SynapseWorkspaceSecurityAlertPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#create SynapseWorkspaceSecurityAlertPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#delete SynapseWorkspaceSecurityAlertPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#read SynapseWorkspaceSecurityAlertPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#update SynapseWorkspaceSecurityAlertPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceSecurityAlertPolicyTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#create SynapseWorkspaceSecurityAlertPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#delete SynapseWorkspaceSecurityAlertPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#read SynapseWorkspaceSecurityAlertPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace_security_alert_policy#update SynapseWorkspaceSecurityAlertPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceSecurityAlertPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspaceSecurityAlertPolicy.SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SynapseWorkspaceSecurityAlertPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SynapseWorkspaceSecurityAlertPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SynapseWorkspaceSecurityAlertPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SynapseWorkspaceSecurityAlertPolicy",
    "SynapseWorkspaceSecurityAlertPolicyConfig",
    "SynapseWorkspaceSecurityAlertPolicyTimeouts",
    "SynapseWorkspaceSecurityAlertPolicyTimeoutsOutputReference",
]

publication.publish()
