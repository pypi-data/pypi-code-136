'''
# `azurerm_web_application_firewall_policy`

Refer to the Terraform Registory for docs: [`azurerm_web_application_firewall_policy`](https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy).
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


class WebApplicationFirewallPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy azurerm_web_application_firewall_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        managed_rules: typing.Union["WebApplicationFirewallPolicyManagedRules", typing.Dict[str, typing.Any]],
        name: builtins.str,
        resource_group_name: builtins.str,
        custom_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyCustomRules", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        policy_settings: typing.Optional[typing.Union["WebApplicationFirewallPolicyPolicySettings", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["WebApplicationFirewallPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy azurerm_web_application_firewall_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#location WebApplicationFirewallPolicy#location}.
        :param managed_rules: managed_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#managed_rules WebApplicationFirewallPolicy#managed_rules}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#name WebApplicationFirewallPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#resource_group_name WebApplicationFirewallPolicy#resource_group_name}.
        :param custom_rules: custom_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#custom_rules WebApplicationFirewallPolicy#custom_rules}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#id WebApplicationFirewallPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy_settings: policy_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#policy_settings WebApplicationFirewallPolicy#policy_settings}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#tags WebApplicationFirewallPolicy#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#timeouts WebApplicationFirewallPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WebApplicationFirewallPolicyConfig(
            location=location,
            managed_rules=managed_rules,
            name=name,
            resource_group_name=resource_group_name,
            custom_rules=custom_rules,
            id=id,
            policy_settings=policy_settings,
            tags=tags,
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

    @jsii.member(jsii_name="putCustomRules")
    def put_custom_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyCustomRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicy.put_custom_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomRules", [value]))

    @jsii.member(jsii_name="putManagedRules")
    def put_managed_rules(
        self,
        *,
        managed_rule_set: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyManagedRulesManagedRuleSet", typing.Dict[str, typing.Any]]]],
        exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyManagedRulesExclusion", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param managed_rule_set: managed_rule_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#managed_rule_set WebApplicationFirewallPolicy#managed_rule_set}
        :param exclusion: exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#exclusion WebApplicationFirewallPolicy#exclusion}
        '''
        value = WebApplicationFirewallPolicyManagedRules(
            managed_rule_set=managed_rule_set, exclusion=exclusion
        )

        return typing.cast(None, jsii.invoke(self, "putManagedRules", [value]))

    @jsii.member(jsii_name="putPolicySettings")
    def put_policy_settings(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        file_upload_limit_in_mb: typing.Optional[jsii.Number] = None,
        max_request_body_size_in_kb: typing.Optional[jsii.Number] = None,
        mode: typing.Optional[builtins.str] = None,
        request_body_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#enabled WebApplicationFirewallPolicy#enabled}.
        :param file_upload_limit_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#file_upload_limit_in_mb WebApplicationFirewallPolicy#file_upload_limit_in_mb}.
        :param max_request_body_size_in_kb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#max_request_body_size_in_kb WebApplicationFirewallPolicy#max_request_body_size_in_kb}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#mode WebApplicationFirewallPolicy#mode}.
        :param request_body_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#request_body_check WebApplicationFirewallPolicy#request_body_check}.
        '''
        value = WebApplicationFirewallPolicyPolicySettings(
            enabled=enabled,
            file_upload_limit_in_mb=file_upload_limit_in_mb,
            max_request_body_size_in_kb=max_request_body_size_in_kb,
            mode=mode,
            request_body_check=request_body_check,
        )

        return typing.cast(None, jsii.invoke(self, "putPolicySettings", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#create WebApplicationFirewallPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#delete WebApplicationFirewallPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#read WebApplicationFirewallPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#update WebApplicationFirewallPolicy#update}.
        '''
        value = WebApplicationFirewallPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCustomRules")
    def reset_custom_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomRules", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPolicySettings")
    def reset_policy_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicySettings", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="customRules")
    def custom_rules(self) -> "WebApplicationFirewallPolicyCustomRulesList":
        return typing.cast("WebApplicationFirewallPolicyCustomRulesList", jsii.get(self, "customRules"))

    @builtins.property
    @jsii.member(jsii_name="httpListenerIds")
    def http_listener_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "httpListenerIds"))

    @builtins.property
    @jsii.member(jsii_name="managedRules")
    def managed_rules(
        self,
    ) -> "WebApplicationFirewallPolicyManagedRulesOutputReference":
        return typing.cast("WebApplicationFirewallPolicyManagedRulesOutputReference", jsii.get(self, "managedRules"))

    @builtins.property
    @jsii.member(jsii_name="pathBasedRuleIds")
    def path_based_rule_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pathBasedRuleIds"))

    @builtins.property
    @jsii.member(jsii_name="policySettings")
    def policy_settings(
        self,
    ) -> "WebApplicationFirewallPolicyPolicySettingsOutputReference":
        return typing.cast("WebApplicationFirewallPolicyPolicySettingsOutputReference", jsii.get(self, "policySettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "WebApplicationFirewallPolicyTimeoutsOutputReference":
        return typing.cast("WebApplicationFirewallPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="customRulesInput")
    def custom_rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyCustomRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyCustomRules"]]], jsii.get(self, "customRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managedRulesInput")
    def managed_rules_input(
        self,
    ) -> typing.Optional["WebApplicationFirewallPolicyManagedRules"]:
        return typing.cast(typing.Optional["WebApplicationFirewallPolicyManagedRules"], jsii.get(self, "managedRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policySettingsInput")
    def policy_settings_input(
        self,
    ) -> typing.Optional["WebApplicationFirewallPolicyPolicySettings"]:
        return typing.cast(typing.Optional["WebApplicationFirewallPolicyPolicySettings"], jsii.get(self, "policySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["WebApplicationFirewallPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["WebApplicationFirewallPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicy, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicy, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicy, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "managed_rules": "managedRules",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "custom_rules": "customRules",
        "id": "id",
        "policy_settings": "policySettings",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class WebApplicationFirewallPolicyConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        managed_rules: typing.Union["WebApplicationFirewallPolicyManagedRules", typing.Dict[str, typing.Any]],
        name: builtins.str,
        resource_group_name: builtins.str,
        custom_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyCustomRules", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        policy_settings: typing.Optional[typing.Union["WebApplicationFirewallPolicyPolicySettings", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["WebApplicationFirewallPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#location WebApplicationFirewallPolicy#location}.
        :param managed_rules: managed_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#managed_rules WebApplicationFirewallPolicy#managed_rules}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#name WebApplicationFirewallPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#resource_group_name WebApplicationFirewallPolicy#resource_group_name}.
        :param custom_rules: custom_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#custom_rules WebApplicationFirewallPolicy#custom_rules}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#id WebApplicationFirewallPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy_settings: policy_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#policy_settings WebApplicationFirewallPolicy#policy_settings}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#tags WebApplicationFirewallPolicy#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#timeouts WebApplicationFirewallPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(managed_rules, dict):
            managed_rules = WebApplicationFirewallPolicyManagedRules(**managed_rules)
        if isinstance(policy_settings, dict):
            policy_settings = WebApplicationFirewallPolicyPolicySettings(**policy_settings)
        if isinstance(timeouts, dict):
            timeouts = WebApplicationFirewallPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument managed_rules", value=managed_rules, expected_type=type_hints["managed_rules"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument custom_rules", value=custom_rules, expected_type=type_hints["custom_rules"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument policy_settings", value=policy_settings, expected_type=type_hints["policy_settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "managed_rules": managed_rules,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if custom_rules is not None:
            self._values["custom_rules"] = custom_rules
        if id is not None:
            self._values["id"] = id
        if policy_settings is not None:
            self._values["policy_settings"] = policy_settings
        if tags is not None:
            self._values["tags"] = tags
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#location WebApplicationFirewallPolicy#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_rules(self) -> "WebApplicationFirewallPolicyManagedRules":
        '''managed_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#managed_rules WebApplicationFirewallPolicy#managed_rules}
        '''
        result = self._values.get("managed_rules")
        assert result is not None, "Required property 'managed_rules' is missing"
        return typing.cast("WebApplicationFirewallPolicyManagedRules", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#name WebApplicationFirewallPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#resource_group_name WebApplicationFirewallPolicy#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyCustomRules"]]]:
        '''custom_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#custom_rules WebApplicationFirewallPolicy#custom_rules}
        '''
        result = self._values.get("custom_rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyCustomRules"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#id WebApplicationFirewallPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_settings(
        self,
    ) -> typing.Optional["WebApplicationFirewallPolicyPolicySettings"]:
        '''policy_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#policy_settings WebApplicationFirewallPolicy#policy_settings}
        '''
        result = self._values.get("policy_settings")
        return typing.cast(typing.Optional["WebApplicationFirewallPolicyPolicySettings"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#tags WebApplicationFirewallPolicy#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["WebApplicationFirewallPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#timeouts WebApplicationFirewallPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["WebApplicationFirewallPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRules",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "match_conditions": "matchConditions",
        "priority": "priority",
        "rule_type": "ruleType",
        "name": "name",
    },
)
class WebApplicationFirewallPolicyCustomRules:
    def __init__(
        self,
        *,
        action: builtins.str,
        match_conditions: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyCustomRulesMatchConditions", typing.Dict[str, typing.Any]]]],
        priority: jsii.Number,
        rule_type: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#action WebApplicationFirewallPolicy#action}.
        :param match_conditions: match_conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#match_conditions WebApplicationFirewallPolicy#match_conditions}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#priority WebApplicationFirewallPolicy#priority}.
        :param rule_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_type WebApplicationFirewallPolicy#rule_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#name WebApplicationFirewallPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRules.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match_conditions", value=match_conditions, expected_type=type_hints["match_conditions"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument rule_type", value=rule_type, expected_type=type_hints["rule_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "match_conditions": match_conditions,
            "priority": priority,
            "rule_type": rule_type,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#action WebApplicationFirewallPolicy#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_conditions(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyCustomRulesMatchConditions"]]:
        '''match_conditions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#match_conditions WebApplicationFirewallPolicy#match_conditions}
        '''
        result = self._values.get("match_conditions")
        assert result is not None, "Required property 'match_conditions' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyCustomRulesMatchConditions"]], result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#priority WebApplicationFirewallPolicy#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_type WebApplicationFirewallPolicy#rule_type}.'''
        result = self._values.get("rule_type")
        assert result is not None, "Required property 'rule_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#name WebApplicationFirewallPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyCustomRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyCustomRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRulesList",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WebApplicationFirewallPolicyCustomRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WebApplicationFirewallPolicyCustomRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRulesMatchConditions",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "match_variables": "matchVariables",
        "operator": "operator",
        "negation_condition": "negationCondition",
        "transforms": "transforms",
    },
)
class WebApplicationFirewallPolicyCustomRulesMatchConditions:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        match_variables: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables", typing.Dict[str, typing.Any]]]],
        operator: builtins.str,
        negation_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#match_values WebApplicationFirewallPolicy#match_values}.
        :param match_variables: match_variables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#match_variables WebApplicationFirewallPolicy#match_variables}
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#operator WebApplicationFirewallPolicy#operator}.
        :param negation_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#negation_condition WebApplicationFirewallPolicy#negation_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#transforms WebApplicationFirewallPolicy#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditions.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument match_variables", value=match_variables, expected_type=type_hints["match_variables"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument negation_condition", value=negation_condition, expected_type=type_hints["negation_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
            "match_variables": match_variables,
            "operator": operator,
        }
        if negation_condition is not None:
            self._values["negation_condition"] = negation_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#match_values WebApplicationFirewallPolicy#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def match_variables(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables"]]:
        '''match_variables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#match_variables WebApplicationFirewallPolicy#match_variables}
        '''
        result = self._values.get("match_variables")
        assert result is not None, "Required property 'match_variables' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables"]], result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#operator WebApplicationFirewallPolicy#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def negation_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#negation_condition WebApplicationFirewallPolicy#negation_condition}.'''
        result = self._values.get("negation_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#transforms WebApplicationFirewallPolicy#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyCustomRulesMatchConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyCustomRulesMatchConditionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRulesMatchConditionsList",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables",
    jsii_struct_bases=[],
    name_mapping={"variable_name": "variableName", "selector": "selector"},
)
class WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables:
    def __init__(
        self,
        *,
        variable_name: builtins.str,
        selector: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param variable_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#variable_name WebApplicationFirewallPolicy#variable_name}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#selector WebApplicationFirewallPolicy#selector}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables.__init__)
            check_type(argname="argument variable_name", value=variable_name, expected_type=type_hints["variable_name"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "variable_name": variable_name,
        }
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def variable_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#variable_name WebApplicationFirewallPolicy#variable_name}.'''
        result = self._values.get("variable_name")
        assert result is not None, "Required property 'variable_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#selector WebApplicationFirewallPolicy#selector}.'''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="variableNameInput")
    def variable_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="variableName")
    def variable_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "variableName"))

    @variable_name.setter
    def variable_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference, "variable_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchVariables")
    def put_match_variables(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference.put_match_variables)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchVariables", [value]))

    @jsii.member(jsii_name="resetNegationCondition")
    def reset_negation_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegationCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchVariables")
    def match_variables(
        self,
    ) -> WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList:
        return typing.cast(WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList, jsii.get(self, "matchVariables"))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="matchVariablesInput")
    def match_variables_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables]]], jsii.get(self, "matchVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="negationConditionInput")
    def negation_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negationConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negationCondition")
    def negation_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negationCondition"))

    @negation_condition.setter
    def negation_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference, "negation_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negationCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRulesMatchConditions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRulesMatchConditions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRulesMatchConditions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyCustomRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyCustomRulesOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchConditions")
    def put_match_conditions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WebApplicationFirewallPolicyCustomRulesMatchConditions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyCustomRulesOutputReference.put_match_conditions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchConditions", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="matchConditions")
    def match_conditions(
        self,
    ) -> WebApplicationFirewallPolicyCustomRulesMatchConditionsList:
        return typing.cast(WebApplicationFirewallPolicyCustomRulesMatchConditionsList, jsii.get(self, "matchConditions"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchConditionsInput")
    def match_conditions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyCustomRulesMatchConditions]]], jsii.get(self, "matchConditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleTypeInput")
    def rule_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="ruleType")
    def rule_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleType"))

    @rule_type.setter
    def rule_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesOutputReference, "rule_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WebApplicationFirewallPolicyCustomRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyCustomRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRules",
    jsii_struct_bases=[],
    name_mapping={"managed_rule_set": "managedRuleSet", "exclusion": "exclusion"},
)
class WebApplicationFirewallPolicyManagedRules:
    def __init__(
        self,
        *,
        managed_rule_set: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyManagedRulesManagedRuleSet", typing.Dict[str, typing.Any]]]],
        exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyManagedRulesExclusion", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param managed_rule_set: managed_rule_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#managed_rule_set WebApplicationFirewallPolicy#managed_rule_set}
        :param exclusion: exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#exclusion WebApplicationFirewallPolicy#exclusion}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRules.__init__)
            check_type(argname="argument managed_rule_set", value=managed_rule_set, expected_type=type_hints["managed_rule_set"])
            check_type(argname="argument exclusion", value=exclusion, expected_type=type_hints["exclusion"])
        self._values: typing.Dict[str, typing.Any] = {
            "managed_rule_set": managed_rule_set,
        }
        if exclusion is not None:
            self._values["exclusion"] = exclusion

    @builtins.property
    def managed_rule_set(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesManagedRuleSet"]]:
        '''managed_rule_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#managed_rule_set WebApplicationFirewallPolicy#managed_rule_set}
        '''
        result = self._values.get("managed_rule_set")
        assert result is not None, "Required property 'managed_rule_set' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesManagedRuleSet"]], result)

    @builtins.property
    def exclusion(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesExclusion"]]]:
        '''exclusion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#exclusion WebApplicationFirewallPolicy#exclusion}
        '''
        result = self._values.get("exclusion")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesExclusion"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyManagedRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesExclusion",
    jsii_struct_bases=[],
    name_mapping={
        "match_variable": "matchVariable",
        "selector": "selector",
        "selector_match_operator": "selectorMatchOperator",
        "excluded_rule_set": "excludedRuleSet",
    },
)
class WebApplicationFirewallPolicyManagedRulesExclusion:
    def __init__(
        self,
        *,
        match_variable: builtins.str,
        selector: builtins.str,
        selector_match_operator: builtins.str,
        excluded_rule_set: typing.Optional[typing.Union["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param match_variable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#match_variable WebApplicationFirewallPolicy#match_variable}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#selector WebApplicationFirewallPolicy#selector}.
        :param selector_match_operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#selector_match_operator WebApplicationFirewallPolicy#selector_match_operator}.
        :param excluded_rule_set: excluded_rule_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#excluded_rule_set WebApplicationFirewallPolicy#excluded_rule_set}
        '''
        if isinstance(excluded_rule_set, dict):
            excluded_rule_set = WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet(**excluded_rule_set)
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusion.__init__)
            check_type(argname="argument match_variable", value=match_variable, expected_type=type_hints["match_variable"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument selector_match_operator", value=selector_match_operator, expected_type=type_hints["selector_match_operator"])
            check_type(argname="argument excluded_rule_set", value=excluded_rule_set, expected_type=type_hints["excluded_rule_set"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_variable": match_variable,
            "selector": selector,
            "selector_match_operator": selector_match_operator,
        }
        if excluded_rule_set is not None:
            self._values["excluded_rule_set"] = excluded_rule_set

    @builtins.property
    def match_variable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#match_variable WebApplicationFirewallPolicy#match_variable}.'''
        result = self._values.get("match_variable")
        assert result is not None, "Required property 'match_variable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#selector WebApplicationFirewallPolicy#selector}.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector_match_operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#selector_match_operator WebApplicationFirewallPolicy#selector_match_operator}.'''
        result = self._values.get("selector_match_operator")
        assert result is not None, "Required property 'selector_match_operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def excluded_rule_set(
        self,
    ) -> typing.Optional["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet"]:
        '''excluded_rule_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#excluded_rule_set WebApplicationFirewallPolicy#excluded_rule_set}
        '''
        result = self._values.get("excluded_rule_set")
        return typing.cast(typing.Optional["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyManagedRulesExclusion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet",
    jsii_struct_bases=[],
    name_mapping={"rule_group": "ruleGroup", "type": "type", "version": "version"},
)
class WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet:
    def __init__(
        self,
        *,
        rule_group: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup", typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rule_group: rule_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group WebApplicationFirewallPolicy#rule_group}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#type WebApplicationFirewallPolicy#type}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#version WebApplicationFirewallPolicy#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet.__init__)
            check_type(argname="argument rule_group", value=rule_group, expected_type=type_hints["rule_group"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if rule_group is not None:
            self._values["rule_group"] = rule_group
        if type is not None:
            self._values["type"] = type
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def rule_group(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup"]]]:
        '''rule_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group WebApplicationFirewallPolicy#rule_group}
        '''
        result = self._values.get("rule_group")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup"]]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#type WebApplicationFirewallPolicy#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#version WebApplicationFirewallPolicy#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRuleGroup")
    def put_rule_group(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference.put_rule_group)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRuleGroup", [value]))

    @jsii.member(jsii_name="resetRuleGroup")
    def reset_rule_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleGroup", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="ruleGroup")
    def rule_group(
        self,
    ) -> "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList":
        return typing.cast("WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList", jsii.get(self, "ruleGroup"))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupInput")
    def rule_group_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup"]]], jsii.get(self, "ruleGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet]:
        return typing.cast(typing.Optional[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup",
    jsii_struct_bases=[],
    name_mapping={
        "rule_group_name": "ruleGroupName",
        "excluded_rules": "excludedRules",
    },
)
class WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup:
    def __init__(
        self,
        *,
        rule_group_name: builtins.str,
        excluded_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param rule_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group_name WebApplicationFirewallPolicy#rule_group_name}.
        :param excluded_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#excluded_rules WebApplicationFirewallPolicy#excluded_rules}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup.__init__)
            check_type(argname="argument rule_group_name", value=rule_group_name, expected_type=type_hints["rule_group_name"])
            check_type(argname="argument excluded_rules", value=excluded_rules, expected_type=type_hints["excluded_rules"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule_group_name": rule_group_name,
        }
        if excluded_rules is not None:
            self._values["excluded_rules"] = excluded_rules

    @builtins.property
    def rule_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group_name WebApplicationFirewallPolicy#rule_group_name}.'''
        result = self._values.get("rule_group_name")
        assert result is not None, "Required property 'rule_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def excluded_rules(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#excluded_rules WebApplicationFirewallPolicy#excluded_rules}.'''
        result = self._values.get("excluded_rules")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExcludedRules")
    def reset_excluded_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedRules", []))

    @builtins.property
    @jsii.member(jsii_name="excludedRulesInput")
    def excluded_rules_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupNameInput")
    def rule_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedRules")
    def excluded_rules(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedRules"))

    @excluded_rules.setter
    def excluded_rules(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference, "excluded_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedRules", value)

    @builtins.property
    @jsii.member(jsii_name="ruleGroupName")
    def rule_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleGroupName"))

    @rule_group_name.setter
    def rule_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference, "rule_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyManagedRulesExclusionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesExclusionList",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WebApplicationFirewallPolicyManagedRulesExclusionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WebApplicationFirewallPolicyManagedRulesExclusionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesExclusion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesExclusion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyManagedRulesExclusionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesExclusionOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesExclusionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExcludedRuleSet")
    def put_excluded_rule_set(
        self,
        *,
        rule_group: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup, typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rule_group: rule_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group WebApplicationFirewallPolicy#rule_group}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#type WebApplicationFirewallPolicy#type}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#version WebApplicationFirewallPolicy#version}.
        '''
        value = WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet(
            rule_group=rule_group, type=type, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putExcludedRuleSet", [value]))

    @jsii.member(jsii_name="resetExcludedRuleSet")
    def reset_excluded_rule_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedRuleSet", []))

    @builtins.property
    @jsii.member(jsii_name="excludedRuleSet")
    def excluded_rule_set(
        self,
    ) -> WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference:
        return typing.cast(WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference, jsii.get(self, "excludedRuleSet"))

    @builtins.property
    @jsii.member(jsii_name="excludedRuleSetInput")
    def excluded_rule_set_input(
        self,
    ) -> typing.Optional[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet]:
        return typing.cast(typing.Optional[WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet], jsii.get(self, "excludedRuleSetInput"))

    @builtins.property
    @jsii.member(jsii_name="matchVariableInput")
    def match_variable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorMatchOperatorInput")
    def selector_match_operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorMatchOperatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchVariable")
    def match_variable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchVariable"))

    @match_variable.setter
    def match_variable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionOutputReference, "match_variable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchVariable", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="selectorMatchOperator")
    def selector_match_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectorMatchOperator"))

    @selector_match_operator.setter
    def selector_match_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionOutputReference, "selector_match_operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectorMatchOperator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesExclusion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesExclusion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesExclusion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesExclusionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesManagedRuleSet",
    jsii_struct_bases=[],
    name_mapping={
        "version": "version",
        "rule_group_override": "ruleGroupOverride",
        "type": "type",
    },
)
class WebApplicationFirewallPolicyManagedRulesManagedRuleSet:
    def __init__(
        self,
        *,
        version: builtins.str,
        rule_group_override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride", typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#version WebApplicationFirewallPolicy#version}.
        :param rule_group_override: rule_group_override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group_override WebApplicationFirewallPolicy#rule_group_override}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#type WebApplicationFirewallPolicy#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSet.__init__)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument rule_group_override", value=rule_group_override, expected_type=type_hints["rule_group_override"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "version": version,
        }
        if rule_group_override is not None:
            self._values["rule_group_override"] = rule_group_override
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#version WebApplicationFirewallPolicy#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_group_override(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride"]]]:
        '''rule_group_override block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group_override WebApplicationFirewallPolicy#rule_group_override}
        '''
        result = self._values.get("rule_group_override")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride"]]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#type WebApplicationFirewallPolicy#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyManagedRulesManagedRuleSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyManagedRulesManagedRuleSetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesManagedRuleSetList",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSetList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSetList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesManagedRuleSet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesManagedRuleSet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesManagedRuleSet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRuleGroupOverride")
    def put_rule_group_override(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference.put_rule_group_override)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRuleGroupOverride", [value]))

    @jsii.member(jsii_name="resetRuleGroupOverride")
    def reset_rule_group_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleGroupOverride", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupOverride")
    def rule_group_override(
        self,
    ) -> "WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList":
        return typing.cast("WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList", jsii.get(self, "ruleGroupOverride"))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupOverrideInput")
    def rule_group_override_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride"]]], jsii.get(self, "ruleGroupOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesManagedRuleSet, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesManagedRuleSet, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesManagedRuleSet, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride",
    jsii_struct_bases=[],
    name_mapping={
        "rule_group_name": "ruleGroupName",
        "disabled_rules": "disabledRules",
    },
)
class WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride:
    def __init__(
        self,
        *,
        rule_group_name: builtins.str,
        disabled_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param rule_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group_name WebApplicationFirewallPolicy#rule_group_name}.
        :param disabled_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#disabled_rules WebApplicationFirewallPolicy#disabled_rules}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride.__init__)
            check_type(argname="argument rule_group_name", value=rule_group_name, expected_type=type_hints["rule_group_name"])
            check_type(argname="argument disabled_rules", value=disabled_rules, expected_type=type_hints["disabled_rules"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule_group_name": rule_group_name,
        }
        if disabled_rules is not None:
            self._values["disabled_rules"] = disabled_rules

    @builtins.property
    def rule_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#rule_group_name WebApplicationFirewallPolicy#rule_group_name}.'''
        result = self._values.get("rule_group_name")
        assert result is not None, "Required property 'rule_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled_rules(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#disabled_rules WebApplicationFirewallPolicy#disabled_rules}.'''
        result = self._values.get("disabled_rules")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisabledRules")
    def reset_disabled_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabledRules", []))

    @builtins.property
    @jsii.member(jsii_name="disabledRulesInput")
    def disabled_rules_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disabledRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupNameInput")
    def rule_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledRules")
    def disabled_rules(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disabledRules"))

    @disabled_rules.setter
    def disabled_rules(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference, "disabled_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabledRules", value)

    @builtins.property
    @jsii.member(jsii_name="ruleGroupName")
    def rule_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleGroupName"))

    @rule_group_name.setter
    def rule_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference, "rule_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WebApplicationFirewallPolicyManagedRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyManagedRulesOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExclusion")
    def put_exclusion(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WebApplicationFirewallPolicyManagedRulesExclusion, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesOutputReference.put_exclusion)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclusion", [value]))

    @jsii.member(jsii_name="putManagedRuleSet")
    def put_managed_rule_set(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WebApplicationFirewallPolicyManagedRulesManagedRuleSet, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyManagedRulesOutputReference.put_managed_rule_set)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedRuleSet", [value]))

    @jsii.member(jsii_name="resetExclusion")
    def reset_exclusion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusion", []))

    @builtins.property
    @jsii.member(jsii_name="exclusion")
    def exclusion(self) -> WebApplicationFirewallPolicyManagedRulesExclusionList:
        return typing.cast(WebApplicationFirewallPolicyManagedRulesExclusionList, jsii.get(self, "exclusion"))

    @builtins.property
    @jsii.member(jsii_name="managedRuleSet")
    def managed_rule_set(
        self,
    ) -> WebApplicationFirewallPolicyManagedRulesManagedRuleSetList:
        return typing.cast(WebApplicationFirewallPolicyManagedRulesManagedRuleSetList, jsii.get(self, "managedRuleSet"))

    @builtins.property
    @jsii.member(jsii_name="exclusionInput")
    def exclusion_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesExclusion]]], jsii.get(self, "exclusionInput"))

    @builtins.property
    @jsii.member(jsii_name="managedRuleSetInput")
    def managed_rule_set_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesManagedRuleSet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WebApplicationFirewallPolicyManagedRulesManagedRuleSet]]], jsii.get(self, "managedRuleSetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WebApplicationFirewallPolicyManagedRules]:
        return typing.cast(typing.Optional[WebApplicationFirewallPolicyManagedRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WebApplicationFirewallPolicyManagedRules],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyManagedRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyPolicySettings",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "file_upload_limit_in_mb": "fileUploadLimitInMb",
        "max_request_body_size_in_kb": "maxRequestBodySizeInKb",
        "mode": "mode",
        "request_body_check": "requestBodyCheck",
    },
)
class WebApplicationFirewallPolicyPolicySettings:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        file_upload_limit_in_mb: typing.Optional[jsii.Number] = None,
        max_request_body_size_in_kb: typing.Optional[jsii.Number] = None,
        mode: typing.Optional[builtins.str] = None,
        request_body_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#enabled WebApplicationFirewallPolicy#enabled}.
        :param file_upload_limit_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#file_upload_limit_in_mb WebApplicationFirewallPolicy#file_upload_limit_in_mb}.
        :param max_request_body_size_in_kb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#max_request_body_size_in_kb WebApplicationFirewallPolicy#max_request_body_size_in_kb}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#mode WebApplicationFirewallPolicy#mode}.
        :param request_body_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#request_body_check WebApplicationFirewallPolicy#request_body_check}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyPolicySettings.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument file_upload_limit_in_mb", value=file_upload_limit_in_mb, expected_type=type_hints["file_upload_limit_in_mb"])
            check_type(argname="argument max_request_body_size_in_kb", value=max_request_body_size_in_kb, expected_type=type_hints["max_request_body_size_in_kb"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument request_body_check", value=request_body_check, expected_type=type_hints["request_body_check"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if file_upload_limit_in_mb is not None:
            self._values["file_upload_limit_in_mb"] = file_upload_limit_in_mb
        if max_request_body_size_in_kb is not None:
            self._values["max_request_body_size_in_kb"] = max_request_body_size_in_kb
        if mode is not None:
            self._values["mode"] = mode
        if request_body_check is not None:
            self._values["request_body_check"] = request_body_check

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#enabled WebApplicationFirewallPolicy#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def file_upload_limit_in_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#file_upload_limit_in_mb WebApplicationFirewallPolicy#file_upload_limit_in_mb}.'''
        result = self._values.get("file_upload_limit_in_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_request_body_size_in_kb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#max_request_body_size_in_kb WebApplicationFirewallPolicy#max_request_body_size_in_kb}.'''
        result = self._values.get("max_request_body_size_in_kb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#mode WebApplicationFirewallPolicy#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_body_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#request_body_check WebApplicationFirewallPolicy#request_body_check}.'''
        result = self._values.get("request_body_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyPolicySettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyPolicySettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyPolicySettingsOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyPolicySettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFileUploadLimitInMb")
    def reset_file_upload_limit_in_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUploadLimitInMb", []))

    @jsii.member(jsii_name="resetMaxRequestBodySizeInKb")
    def reset_max_request_body_size_in_kb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRequestBodySizeInKb", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetRequestBodyCheck")
    def reset_request_body_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestBodyCheck", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUploadLimitInMbInput")
    def file_upload_limit_in_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fileUploadLimitInMbInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRequestBodySizeInKbInput")
    def max_request_body_size_in_kb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRequestBodySizeInKbInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="requestBodyCheckInput")
    def request_body_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requestBodyCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyPolicySettingsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="fileUploadLimitInMb")
    def file_upload_limit_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fileUploadLimitInMb"))

    @file_upload_limit_in_mb.setter
    def file_upload_limit_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyPolicySettingsOutputReference, "file_upload_limit_in_mb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUploadLimitInMb", value)

    @builtins.property
    @jsii.member(jsii_name="maxRequestBodySizeInKb")
    def max_request_body_size_in_kb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequestBodySizeInKb"))

    @max_request_body_size_in_kb.setter
    def max_request_body_size_in_kb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyPolicySettingsOutputReference, "max_request_body_size_in_kb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequestBodySizeInKb", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyPolicySettingsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="requestBodyCheck")
    def request_body_check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requestBodyCheck"))

    @request_body_check.setter
    def request_body_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyPolicySettingsOutputReference, "request_body_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestBodyCheck", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WebApplicationFirewallPolicyPolicySettings]:
        return typing.cast(typing.Optional[WebApplicationFirewallPolicyPolicySettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WebApplicationFirewallPolicyPolicySettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyPolicySettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class WebApplicationFirewallPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#create WebApplicationFirewallPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#delete WebApplicationFirewallPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#read WebApplicationFirewallPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#update WebApplicationFirewallPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#create WebApplicationFirewallPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#delete WebApplicationFirewallPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#read WebApplicationFirewallPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/web_application_firewall_policy#update WebApplicationFirewallPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebApplicationFirewallPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebApplicationFirewallPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.webApplicationFirewallPolicy.WebApplicationFirewallPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(WebApplicationFirewallPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WebApplicationFirewallPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WebApplicationFirewallPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WebApplicationFirewallPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WebApplicationFirewallPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WebApplicationFirewallPolicy",
    "WebApplicationFirewallPolicyConfig",
    "WebApplicationFirewallPolicyCustomRules",
    "WebApplicationFirewallPolicyCustomRulesList",
    "WebApplicationFirewallPolicyCustomRulesMatchConditions",
    "WebApplicationFirewallPolicyCustomRulesMatchConditionsList",
    "WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariables",
    "WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesList",
    "WebApplicationFirewallPolicyCustomRulesMatchConditionsMatchVariablesOutputReference",
    "WebApplicationFirewallPolicyCustomRulesMatchConditionsOutputReference",
    "WebApplicationFirewallPolicyCustomRulesOutputReference",
    "WebApplicationFirewallPolicyManagedRules",
    "WebApplicationFirewallPolicyManagedRulesExclusion",
    "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSet",
    "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetOutputReference",
    "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroup",
    "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupList",
    "WebApplicationFirewallPolicyManagedRulesExclusionExcludedRuleSetRuleGroupOutputReference",
    "WebApplicationFirewallPolicyManagedRulesExclusionList",
    "WebApplicationFirewallPolicyManagedRulesExclusionOutputReference",
    "WebApplicationFirewallPolicyManagedRulesManagedRuleSet",
    "WebApplicationFirewallPolicyManagedRulesManagedRuleSetList",
    "WebApplicationFirewallPolicyManagedRulesManagedRuleSetOutputReference",
    "WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverride",
    "WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideList",
    "WebApplicationFirewallPolicyManagedRulesManagedRuleSetRuleGroupOverrideOutputReference",
    "WebApplicationFirewallPolicyManagedRulesOutputReference",
    "WebApplicationFirewallPolicyPolicySettings",
    "WebApplicationFirewallPolicyPolicySettingsOutputReference",
    "WebApplicationFirewallPolicyTimeouts",
    "WebApplicationFirewallPolicyTimeoutsOutputReference",
]

publication.publish()
