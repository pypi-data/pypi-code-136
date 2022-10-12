'''
# `google_compute_firewall_policy_rule`

Refer to the Terraform Registory for docs: [`google_compute_firewall_policy_rule`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule).
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


class GoogleComputeFirewallPolicyRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule google_compute_firewall_policy_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        action: builtins.str,
        direction: builtins.str,
        firewall_policy: builtins.str,
        match: typing.Union["GoogleComputeFirewallPolicyRuleMatch", typing.Dict[str, typing.Any]],
        priority: jsii.Number,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        target_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeFirewallPolicyRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule google_compute_firewall_policy_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: The Action to perform when the client connection triggers the rule. Can currently be either "allow" or "deny()" where valid values for status are 403, 404, and 502. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#action GoogleComputeFirewallPolicyRule#action}
        :param direction: The direction in which this rule applies. Possible values: INGRESS, EGRESS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#direction GoogleComputeFirewallPolicyRule#direction}
        :param firewall_policy: The firewall policy of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#firewall_policy GoogleComputeFirewallPolicyRule#firewall_policy}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#match GoogleComputeFirewallPolicyRule#match}
        :param priority: An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest prority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#priority GoogleComputeFirewallPolicyRule#priority}
        :param description: An optional description for this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#description GoogleComputeFirewallPolicyRule#description}
        :param disabled: Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#disabled GoogleComputeFirewallPolicyRule#disabled}
        :param enable_logging: Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#enable_logging GoogleComputeFirewallPolicyRule#enable_logging}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#id GoogleComputeFirewallPolicyRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param target_resources: A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#target_resources GoogleComputeFirewallPolicyRule#target_resources}
        :param target_service_accounts: A list of service accounts indicating the sets of instances that are applied with this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#target_service_accounts GoogleComputeFirewallPolicyRule#target_service_accounts}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#timeouts GoogleComputeFirewallPolicyRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeFirewallPolicyRuleConfig(
            action=action,
            direction=direction,
            firewall_policy=firewall_policy,
            match=match,
            priority=priority,
            description=description,
            disabled=disabled,
            enable_logging=enable_logging,
            id=id,
            target_resources=target_resources,
            target_service_accounts=target_service_accounts,
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

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        layer4_configs: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeFirewallPolicyRuleMatchLayer4Configs", typing.Dict[str, typing.Any]]]],
        dest_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param layer4_configs: layer4_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#layer4_configs GoogleComputeFirewallPolicyRule#layer4_configs}
        :param dest_ip_ranges: CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 256. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#dest_ip_ranges GoogleComputeFirewallPolicyRule#dest_ip_ranges}
        :param src_ip_ranges: CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 256. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#src_ip_ranges GoogleComputeFirewallPolicyRule#src_ip_ranges}
        '''
        value = GoogleComputeFirewallPolicyRuleMatch(
            layer4_configs=layer4_configs,
            dest_ip_ranges=dest_ip_ranges,
            src_ip_ranges=src_ip_ranges,
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#create GoogleComputeFirewallPolicyRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#delete GoogleComputeFirewallPolicyRule#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#update GoogleComputeFirewallPolicyRule#update}.
        '''
        value = GoogleComputeFirewallPolicyRuleTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetEnableLogging")
    def reset_enable_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLogging", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTargetResources")
    def reset_target_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResources", []))

    @jsii.member(jsii_name="resetTargetServiceAccounts")
    def reset_target_service_accounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetServiceAccounts", []))

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
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> "GoogleComputeFirewallPolicyRuleMatchOutputReference":
        return typing.cast("GoogleComputeFirewallPolicyRuleMatchOutputReference", jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="ruleTupleCount")
    def rule_tuple_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleTupleCount"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeFirewallPolicyRuleTimeoutsOutputReference":
        return typing.cast("GoogleComputeFirewallPolicyRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="directionInput")
    def direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLoggingInput")
    def enable_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyInput")
    def firewall_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional["GoogleComputeFirewallPolicyRuleMatch"]:
        return typing.cast(typing.Optional["GoogleComputeFirewallPolicyRuleMatch"], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourcesInput")
    def target_resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetResourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetServiceAccountsInput")
    def target_service_accounts_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetServiceAccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeFirewallPolicyRuleTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeFirewallPolicyRuleTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="enableLogging")
    def enable_logging(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLogging"))

    @enable_logging.setter
    def enable_logging(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "enable_logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogging", value)

    @builtins.property
    @jsii.member(jsii_name="firewallPolicy")
    def firewall_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicy"))

    @firewall_policy.setter
    def firewall_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "firewall_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="targetResources")
    def target_resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetResources"))

    @target_resources.setter
    def target_resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "target_resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResources", value)

    @builtins.property
    @jsii.member(jsii_name="targetServiceAccounts")
    def target_service_accounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetServiceAccounts"))

    @target_service_accounts.setter
    def target_service_accounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRule, "target_service_accounts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetServiceAccounts", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "direction": "direction",
        "firewall_policy": "firewallPolicy",
        "match": "match",
        "priority": "priority",
        "description": "description",
        "disabled": "disabled",
        "enable_logging": "enableLogging",
        "id": "id",
        "target_resources": "targetResources",
        "target_service_accounts": "targetServiceAccounts",
        "timeouts": "timeouts",
    },
)
class GoogleComputeFirewallPolicyRuleConfig(cdktf.TerraformMetaArguments):
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
        action: builtins.str,
        direction: builtins.str,
        firewall_policy: builtins.str,
        match: typing.Union["GoogleComputeFirewallPolicyRuleMatch", typing.Dict[str, typing.Any]],
        priority: jsii.Number,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        target_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeFirewallPolicyRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action: The Action to perform when the client connection triggers the rule. Can currently be either "allow" or "deny()" where valid values for status are 403, 404, and 502. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#action GoogleComputeFirewallPolicyRule#action}
        :param direction: The direction in which this rule applies. Possible values: INGRESS, EGRESS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#direction GoogleComputeFirewallPolicyRule#direction}
        :param firewall_policy: The firewall policy of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#firewall_policy GoogleComputeFirewallPolicyRule#firewall_policy}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#match GoogleComputeFirewallPolicyRule#match}
        :param priority: An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest prority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#priority GoogleComputeFirewallPolicyRule#priority}
        :param description: An optional description for this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#description GoogleComputeFirewallPolicyRule#description}
        :param disabled: Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#disabled GoogleComputeFirewallPolicyRule#disabled}
        :param enable_logging: Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#enable_logging GoogleComputeFirewallPolicyRule#enable_logging}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#id GoogleComputeFirewallPolicyRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param target_resources: A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#target_resources GoogleComputeFirewallPolicyRule#target_resources}
        :param target_service_accounts: A list of service accounts indicating the sets of instances that are applied with this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#target_service_accounts GoogleComputeFirewallPolicyRule#target_service_accounts}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#timeouts GoogleComputeFirewallPolicyRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(match, dict):
            match = GoogleComputeFirewallPolicyRuleMatch(**match)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeFirewallPolicyRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument firewall_policy", value=firewall_policy, expected_type=type_hints["firewall_policy"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target_resources", value=target_resources, expected_type=type_hints["target_resources"])
            check_type(argname="argument target_service_accounts", value=target_service_accounts, expected_type=type_hints["target_service_accounts"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "direction": direction,
            "firewall_policy": firewall_policy,
            "match": match,
            "priority": priority,
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
        if disabled is not None:
            self._values["disabled"] = disabled
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if id is not None:
            self._values["id"] = id
        if target_resources is not None:
            self._values["target_resources"] = target_resources
        if target_service_accounts is not None:
            self._values["target_service_accounts"] = target_service_accounts
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
    def action(self) -> builtins.str:
        '''The Action to perform when the client connection triggers the rule.

        Can currently be either "allow" or "deny()" where valid values for status are 403, 404, and 502.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#action GoogleComputeFirewallPolicyRule#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def direction(self) -> builtins.str:
        '''The direction in which this rule applies. Possible values: INGRESS, EGRESS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#direction GoogleComputeFirewallPolicyRule#direction}
        '''
        result = self._values.get("direction")
        assert result is not None, "Required property 'direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_policy(self) -> builtins.str:
        '''The firewall policy of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#firewall_policy GoogleComputeFirewallPolicyRule#firewall_policy}
        '''
        result = self._values.get("firewall_policy")
        assert result is not None, "Required property 'firewall_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match(self) -> "GoogleComputeFirewallPolicyRuleMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#match GoogleComputeFirewallPolicyRule#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("GoogleComputeFirewallPolicyRuleMatch", result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''An integer indicating the priority of a rule in the list.

        The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest prority.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#priority GoogleComputeFirewallPolicyRule#priority}
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#description GoogleComputeFirewallPolicyRule#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Denotes whether the firewall policy rule is disabled.

        When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#disabled GoogleComputeFirewallPolicyRule#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Denotes whether to enable logging for a particular rule.

        If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#enable_logging GoogleComputeFirewallPolicyRule#enable_logging}
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#id GoogleComputeFirewallPolicyRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of network resource URLs to which this rule applies.

        This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#target_resources GoogleComputeFirewallPolicyRule#target_resources}
        '''
        result = self._values.get("target_resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_service_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of service accounts indicating the sets of instances that are applied with this rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#target_service_accounts GoogleComputeFirewallPolicyRule#target_service_accounts}
        '''
        result = self._values.get("target_service_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeFirewallPolicyRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#timeouts GoogleComputeFirewallPolicyRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeFirewallPolicyRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallPolicyRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRuleMatch",
    jsii_struct_bases=[],
    name_mapping={
        "layer4_configs": "layer4Configs",
        "dest_ip_ranges": "destIpRanges",
        "src_ip_ranges": "srcIpRanges",
    },
)
class GoogleComputeFirewallPolicyRuleMatch:
    def __init__(
        self,
        *,
        layer4_configs: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeFirewallPolicyRuleMatchLayer4Configs", typing.Dict[str, typing.Any]]]],
        dest_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param layer4_configs: layer4_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#layer4_configs GoogleComputeFirewallPolicyRule#layer4_configs}
        :param dest_ip_ranges: CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 256. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#dest_ip_ranges GoogleComputeFirewallPolicyRule#dest_ip_ranges}
        :param src_ip_ranges: CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 256. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#src_ip_ranges GoogleComputeFirewallPolicyRule#src_ip_ranges}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleMatch.__init__)
            check_type(argname="argument layer4_configs", value=layer4_configs, expected_type=type_hints["layer4_configs"])
            check_type(argname="argument dest_ip_ranges", value=dest_ip_ranges, expected_type=type_hints["dest_ip_ranges"])
            check_type(argname="argument src_ip_ranges", value=src_ip_ranges, expected_type=type_hints["src_ip_ranges"])
        self._values: typing.Dict[str, typing.Any] = {
            "layer4_configs": layer4_configs,
        }
        if dest_ip_ranges is not None:
            self._values["dest_ip_ranges"] = dest_ip_ranges
        if src_ip_ranges is not None:
            self._values["src_ip_ranges"] = src_ip_ranges

    @builtins.property
    def layer4_configs(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleComputeFirewallPolicyRuleMatchLayer4Configs"]]:
        '''layer4_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#layer4_configs GoogleComputeFirewallPolicyRule#layer4_configs}
        '''
        result = self._values.get("layer4_configs")
        assert result is not None, "Required property 'layer4_configs' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleComputeFirewallPolicyRuleMatchLayer4Configs"]], result)

    @builtins.property
    def dest_ip_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''CIDR IP address range. Maximum number of destination CIDR IP ranges allowed is 256.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#dest_ip_ranges GoogleComputeFirewallPolicyRule#dest_ip_ranges}
        '''
        result = self._values.get("dest_ip_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def src_ip_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''CIDR IP address range. Maximum number of source CIDR IP ranges allowed is 256.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#src_ip_ranges GoogleComputeFirewallPolicyRule#src_ip_ranges}
        '''
        result = self._values.get("src_ip_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallPolicyRuleMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRuleMatchLayer4Configs",
    jsii_struct_bases=[],
    name_mapping={"ip_protocol": "ipProtocol", "ports": "ports"},
)
class GoogleComputeFirewallPolicyRuleMatchLayer4Configs:
    def __init__(
        self,
        *,
        ip_protocol: builtins.str,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ip_protocol: The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (``tcp``, ``udp``, ``icmp``, ``esp``, ``ah``, ``ipip``, ``sctp``), or the IP protocol number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#ip_protocol GoogleComputeFirewallPolicyRule#ip_protocol}
        :param ports: An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port. Example inputs include: ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#ports GoogleComputeFirewallPolicyRule#ports}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleMatchLayer4Configs.__init__)
            check_type(argname="argument ip_protocol", value=ip_protocol, expected_type=type_hints["ip_protocol"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_protocol": ip_protocol,
        }
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def ip_protocol(self) -> builtins.str:
        '''The IP protocol to which this rule applies.

        The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (``tcp``, ``udp``, ``icmp``, ``esp``, ``ah``, ``ipip``, ``sctp``), or the IP protocol number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#ip_protocol GoogleComputeFirewallPolicyRule#ip_protocol}
        '''
        result = self._values.get("ip_protocol")
        assert result is not None, "Required property 'ip_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional list of ports to which this rule applies.

        This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port. Example inputs include: ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#ports GoogleComputeFirewallPolicyRule#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallPolicyRuleMatchLayer4Configs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallPolicyRuleMatchLayer4Configs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallPolicyRuleMatchLayer4Configs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallPolicyRuleMatchLayer4Configs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="ipProtocolInput")
    def ip_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipProtocol")
    def ip_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipProtocol"))

    @ip_protocol.setter
    def ip_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference, "ip_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference, "ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeFirewallPolicyRuleMatchLayer4Configs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeFirewallPolicyRuleMatchLayer4Configs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeFirewallPolicyRuleMatchLayer4Configs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeFirewallPolicyRuleMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRuleMatchOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLayer4Configs")
    def put_layer4_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeFirewallPolicyRuleMatchLayer4Configs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleMatchOutputReference.put_layer4_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLayer4Configs", [value]))

    @jsii.member(jsii_name="resetDestIpRanges")
    def reset_dest_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestIpRanges", []))

    @jsii.member(jsii_name="resetSrcIpRanges")
    def reset_src_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrcIpRanges", []))

    @builtins.property
    @jsii.member(jsii_name="layer4Configs")
    def layer4_configs(self) -> GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList:
        return typing.cast(GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList, jsii.get(self, "layer4Configs"))

    @builtins.property
    @jsii.member(jsii_name="destIpRangesInput")
    def dest_ip_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="layer4ConfigsInput")
    def layer4_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallPolicyRuleMatchLayer4Configs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallPolicyRuleMatchLayer4Configs]]], jsii.get(self, "layer4ConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="srcIpRangesInput")
    def src_ip_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "srcIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="destIpRanges")
    def dest_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destIpRanges"))

    @dest_ip_ranges.setter
    def dest_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchOutputReference, "dest_ip_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="srcIpRanges")
    def src_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "srcIpRanges"))

    @src_ip_ranges.setter
    def src_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchOutputReference, "src_ip_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "srcIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeFirewallPolicyRuleMatch]:
        return typing.cast(typing.Optional[GoogleComputeFirewallPolicyRuleMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeFirewallPolicyRuleMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeFirewallPolicyRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#create GoogleComputeFirewallPolicyRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#delete GoogleComputeFirewallPolicyRule#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#update GoogleComputeFirewallPolicyRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#create GoogleComputeFirewallPolicyRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#delete GoogleComputeFirewallPolicyRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall_policy_rule#update GoogleComputeFirewallPolicyRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallPolicyRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeFirewallPolicyRuleTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewallPolicyRule.GoogleComputeFirewallPolicyRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallPolicyRuleTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeFirewallPolicyRuleTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeFirewallPolicyRuleTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeFirewallPolicyRuleTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallPolicyRuleTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeFirewallPolicyRule",
    "GoogleComputeFirewallPolicyRuleConfig",
    "GoogleComputeFirewallPolicyRuleMatch",
    "GoogleComputeFirewallPolicyRuleMatchLayer4Configs",
    "GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsList",
    "GoogleComputeFirewallPolicyRuleMatchLayer4ConfigsOutputReference",
    "GoogleComputeFirewallPolicyRuleMatchOutputReference",
    "GoogleComputeFirewallPolicyRuleTimeouts",
    "GoogleComputeFirewallPolicyRuleTimeoutsOutputReference",
]

publication.publish()
