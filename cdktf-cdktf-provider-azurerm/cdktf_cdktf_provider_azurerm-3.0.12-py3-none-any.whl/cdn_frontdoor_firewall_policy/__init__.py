'''
# `azurerm_cdn_frontdoor_firewall_policy`

Refer to the Terraform Registory for docs: [`azurerm_cdn_frontdoor_firewall_policy`](https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy).
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


class CdnFrontdoorFirewallPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy azurerm_cdn_frontdoor_firewall_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        mode: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        custom_block_response_body: typing.Optional[builtins.str] = None,
        custom_block_response_status_code: typing.Optional[jsii.Number] = None,
        custom_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyCustomRule", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        managed_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRule", typing.Dict[str, typing.Any]]]]] = None,
        redirect_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorFirewallPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy azurerm_cdn_frontdoor_firewall_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#mode CdnFrontdoorFirewallPolicy#mode}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#name CdnFrontdoorFirewallPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#resource_group_name CdnFrontdoorFirewallPolicy#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#sku_name CdnFrontdoorFirewallPolicy#sku_name}.
        :param custom_block_response_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_block_response_body CdnFrontdoorFirewallPolicy#custom_block_response_body}.
        :param custom_block_response_status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_block_response_status_code CdnFrontdoorFirewallPolicy#custom_block_response_status_code}.
        :param custom_rule: custom_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_rule CdnFrontdoorFirewallPolicy#custom_rule}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#enabled CdnFrontdoorFirewallPolicy#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#id CdnFrontdoorFirewallPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param managed_rule: managed_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#managed_rule CdnFrontdoorFirewallPolicy#managed_rule}
        :param redirect_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#redirect_url CdnFrontdoorFirewallPolicy#redirect_url}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#tags CdnFrontdoorFirewallPolicy#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#timeouts CdnFrontdoorFirewallPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CdnFrontdoorFirewallPolicyConfig(
            mode=mode,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            custom_block_response_body=custom_block_response_body,
            custom_block_response_status_code=custom_block_response_status_code,
            custom_rule=custom_rule,
            enabled=enabled,
            id=id,
            managed_rule=managed_rule,
            redirect_url=redirect_url,
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

    @jsii.member(jsii_name="putCustomRule")
    def put_custom_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyCustomRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicy.put_custom_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomRule", [value]))

    @jsii.member(jsii_name="putManagedRule")
    def put_managed_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicy.put_managed_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedRule", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#create CdnFrontdoorFirewallPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#delete CdnFrontdoorFirewallPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#read CdnFrontdoorFirewallPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#update CdnFrontdoorFirewallPolicy#update}.
        '''
        value = CdnFrontdoorFirewallPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCustomBlockResponseBody")
    def reset_custom_block_response_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomBlockResponseBody", []))

    @jsii.member(jsii_name="resetCustomBlockResponseStatusCode")
    def reset_custom_block_response_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomBlockResponseStatusCode", []))

    @jsii.member(jsii_name="resetCustomRule")
    def reset_custom_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomRule", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetManagedRule")
    def reset_managed_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedRule", []))

    @jsii.member(jsii_name="resetRedirectUrl")
    def reset_redirect_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUrl", []))

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
    @jsii.member(jsii_name="customRule")
    def custom_rule(self) -> "CdnFrontdoorFirewallPolicyCustomRuleList":
        return typing.cast("CdnFrontdoorFirewallPolicyCustomRuleList", jsii.get(self, "customRule"))

    @builtins.property
    @jsii.member(jsii_name="frontendEndpointIds")
    def frontend_endpoint_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "frontendEndpointIds"))

    @builtins.property
    @jsii.member(jsii_name="managedRule")
    def managed_rule(self) -> "CdnFrontdoorFirewallPolicyManagedRuleList":
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleList", jsii.get(self, "managedRule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CdnFrontdoorFirewallPolicyTimeoutsOutputReference":
        return typing.cast("CdnFrontdoorFirewallPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="customBlockResponseBodyInput")
    def custom_block_response_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customBlockResponseBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="customBlockResponseStatusCodeInput")
    def custom_block_response_status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "customBlockResponseStatusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="customRuleInput")
    def custom_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyCustomRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyCustomRule"]]], jsii.get(self, "customRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="managedRuleInput")
    def managed_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRule"]]], jsii.get(self, "managedRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUrlInput")
    def redirect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CdnFrontdoorFirewallPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CdnFrontdoorFirewallPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="customBlockResponseBody")
    def custom_block_response_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customBlockResponseBody"))

    @custom_block_response_body.setter
    def custom_block_response_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "custom_block_response_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customBlockResponseBody", value)

    @builtins.property
    @jsii.member(jsii_name="customBlockResponseStatusCode")
    def custom_block_response_status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "customBlockResponseStatusCode"))

    @custom_block_response_status_code.setter
    def custom_block_response_status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "custom_block_response_status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customBlockResponseStatusCode", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUrl")
    def redirect_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUrl"))

    @redirect_url.setter
    def redirect_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "redirect_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicy, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "mode": "mode",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "custom_block_response_body": "customBlockResponseBody",
        "custom_block_response_status_code": "customBlockResponseStatusCode",
        "custom_rule": "customRule",
        "enabled": "enabled",
        "id": "id",
        "managed_rule": "managedRule",
        "redirect_url": "redirectUrl",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class CdnFrontdoorFirewallPolicyConfig(cdktf.TerraformMetaArguments):
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
        mode: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        custom_block_response_body: typing.Optional[builtins.str] = None,
        custom_block_response_status_code: typing.Optional[jsii.Number] = None,
        custom_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyCustomRule", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        managed_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRule", typing.Dict[str, typing.Any]]]]] = None,
        redirect_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorFirewallPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#mode CdnFrontdoorFirewallPolicy#mode}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#name CdnFrontdoorFirewallPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#resource_group_name CdnFrontdoorFirewallPolicy#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#sku_name CdnFrontdoorFirewallPolicy#sku_name}.
        :param custom_block_response_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_block_response_body CdnFrontdoorFirewallPolicy#custom_block_response_body}.
        :param custom_block_response_status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_block_response_status_code CdnFrontdoorFirewallPolicy#custom_block_response_status_code}.
        :param custom_rule: custom_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_rule CdnFrontdoorFirewallPolicy#custom_rule}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#enabled CdnFrontdoorFirewallPolicy#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#id CdnFrontdoorFirewallPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param managed_rule: managed_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#managed_rule CdnFrontdoorFirewallPolicy#managed_rule}
        :param redirect_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#redirect_url CdnFrontdoorFirewallPolicy#redirect_url}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#tags CdnFrontdoorFirewallPolicy#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#timeouts CdnFrontdoorFirewallPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = CdnFrontdoorFirewallPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument custom_block_response_body", value=custom_block_response_body, expected_type=type_hints["custom_block_response_body"])
            check_type(argname="argument custom_block_response_status_code", value=custom_block_response_status_code, expected_type=type_hints["custom_block_response_status_code"])
            check_type(argname="argument custom_rule", value=custom_rule, expected_type=type_hints["custom_rule"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument managed_rule", value=managed_rule, expected_type=type_hints["managed_rule"])
            check_type(argname="argument redirect_url", value=redirect_url, expected_type=type_hints["redirect_url"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
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
        if custom_block_response_body is not None:
            self._values["custom_block_response_body"] = custom_block_response_body
        if custom_block_response_status_code is not None:
            self._values["custom_block_response_status_code"] = custom_block_response_status_code
        if custom_rule is not None:
            self._values["custom_rule"] = custom_rule
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if managed_rule is not None:
            self._values["managed_rule"] = managed_rule
        if redirect_url is not None:
            self._values["redirect_url"] = redirect_url
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
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#mode CdnFrontdoorFirewallPolicy#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#name CdnFrontdoorFirewallPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#resource_group_name CdnFrontdoorFirewallPolicy#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#sku_name CdnFrontdoorFirewallPolicy#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_block_response_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_block_response_body CdnFrontdoorFirewallPolicy#custom_block_response_body}.'''
        result = self._values.get("custom_block_response_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_block_response_status_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_block_response_status_code CdnFrontdoorFirewallPolicy#custom_block_response_status_code}.'''
        result = self._values.get("custom_block_response_status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def custom_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyCustomRule"]]]:
        '''custom_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#custom_rule CdnFrontdoorFirewallPolicy#custom_rule}
        '''
        result = self._values.get("custom_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyCustomRule"]]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#enabled CdnFrontdoorFirewallPolicy#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#id CdnFrontdoorFirewallPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRule"]]]:
        '''managed_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#managed_rule CdnFrontdoorFirewallPolicy#managed_rule}
        '''
        result = self._values.get("managed_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRule"]]], result)

    @builtins.property
    def redirect_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#redirect_url CdnFrontdoorFirewallPolicy#redirect_url}.'''
        result = self._values.get("redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#tags CdnFrontdoorFirewallPolicy#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CdnFrontdoorFirewallPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#timeouts CdnFrontdoorFirewallPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CdnFrontdoorFirewallPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyCustomRule",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "name": "name",
        "type": "type",
        "enabled": "enabled",
        "match_condition": "matchCondition",
        "priority": "priority",
        "rate_limit_duration_in_minutes": "rateLimitDurationInMinutes",
        "rate_limit_threshold": "rateLimitThreshold",
    },
)
class CdnFrontdoorFirewallPolicyCustomRule:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        type: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        match_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyCustomRuleMatchCondition", typing.Dict[str, typing.Any]]]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        rate_limit_duration_in_minutes: typing.Optional[jsii.Number] = None,
        rate_limit_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#action CdnFrontdoorFirewallPolicy#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#name CdnFrontdoorFirewallPolicy#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#type CdnFrontdoorFirewallPolicy#type}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#enabled CdnFrontdoorFirewallPolicy#enabled}.
        :param match_condition: match_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_condition CdnFrontdoorFirewallPolicy#match_condition}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#priority CdnFrontdoorFirewallPolicy#priority}.
        :param rate_limit_duration_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rate_limit_duration_in_minutes CdnFrontdoorFirewallPolicy#rate_limit_duration_in_minutes}.
        :param rate_limit_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rate_limit_threshold CdnFrontdoorFirewallPolicy#rate_limit_threshold}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument match_condition", value=match_condition, expected_type=type_hints["match_condition"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument rate_limit_duration_in_minutes", value=rate_limit_duration_in_minutes, expected_type=type_hints["rate_limit_duration_in_minutes"])
            check_type(argname="argument rate_limit_threshold", value=rate_limit_threshold, expected_type=type_hints["rate_limit_threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
            "type": type,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if match_condition is not None:
            self._values["match_condition"] = match_condition
        if priority is not None:
            self._values["priority"] = priority
        if rate_limit_duration_in_minutes is not None:
            self._values["rate_limit_duration_in_minutes"] = rate_limit_duration_in_minutes
        if rate_limit_threshold is not None:
            self._values["rate_limit_threshold"] = rate_limit_threshold

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#action CdnFrontdoorFirewallPolicy#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#name CdnFrontdoorFirewallPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#type CdnFrontdoorFirewallPolicy#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#enabled CdnFrontdoorFirewallPolicy#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def match_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyCustomRuleMatchCondition"]]]:
        '''match_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_condition CdnFrontdoorFirewallPolicy#match_condition}
        '''
        result = self._values.get("match_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyCustomRuleMatchCondition"]]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#priority CdnFrontdoorFirewallPolicy#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rate_limit_duration_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rate_limit_duration_in_minutes CdnFrontdoorFirewallPolicy#rate_limit_duration_in_minutes}.'''
        result = self._values.get("rate_limit_duration_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rate_limit_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rate_limit_threshold CdnFrontdoorFirewallPolicy#rate_limit_threshold}.'''
        result = self._values.get("rate_limit_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyCustomRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorFirewallPolicyCustomRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyCustomRuleList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorFirewallPolicyCustomRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorFirewallPolicyCustomRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyCustomRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyCustomRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyCustomRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyCustomRuleMatchCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "match_variable": "matchVariable",
        "operator": "operator",
        "negation_condition": "negationCondition",
        "selector": "selector",
        "transforms": "transforms",
    },
)
class CdnFrontdoorFirewallPolicyCustomRuleMatchCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        match_variable: builtins.str,
        operator: builtins.str,
        negation_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        selector: typing.Optional[builtins.str] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_values CdnFrontdoorFirewallPolicy#match_values}.
        :param match_variable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_variable CdnFrontdoorFirewallPolicy#match_variable}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#operator CdnFrontdoorFirewallPolicy#operator}.
        :param negation_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#negation_condition CdnFrontdoorFirewallPolicy#negation_condition}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#selector CdnFrontdoorFirewallPolicy#selector}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#transforms CdnFrontdoorFirewallPolicy#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRuleMatchCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument match_variable", value=match_variable, expected_type=type_hints["match_variable"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument negation_condition", value=negation_condition, expected_type=type_hints["negation_condition"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
            "match_variable": match_variable,
            "operator": operator,
        }
        if negation_condition is not None:
            self._values["negation_condition"] = negation_condition
        if selector is not None:
            self._values["selector"] = selector
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_values CdnFrontdoorFirewallPolicy#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def match_variable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_variable CdnFrontdoorFirewallPolicy#match_variable}.'''
        result = self._values.get("match_variable")
        assert result is not None, "Required property 'match_variable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#operator CdnFrontdoorFirewallPolicy#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def negation_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#negation_condition CdnFrontdoorFirewallPolicy#negation_condition}.'''
        result = self._values.get("negation_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def selector(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#selector CdnFrontdoorFirewallPolicy#selector}.'''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#transforms CdnFrontdoorFirewallPolicy#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyCustomRuleMatchCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegationCondition")
    def reset_negation_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegationCondition", []))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="matchVariableInput")
    def match_variable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchVariableInput"))

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
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="matchVariable")
    def match_variable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchVariable"))

    @match_variable.setter
    def match_variable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference, "match_variable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchVariable", value)

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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference, "negation_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negationCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyCustomRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyCustomRuleOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchCondition")
    def put_match_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyCustomRuleOutputReference.put_match_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchCondition", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetMatchCondition")
    def reset_match_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchCondition", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetRateLimitDurationInMinutes")
    def reset_rate_limit_duration_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRateLimitDurationInMinutes", []))

    @jsii.member(jsii_name="resetRateLimitThreshold")
    def reset_rate_limit_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRateLimitThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="matchCondition")
    def match_condition(self) -> CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList:
        return typing.cast(CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList, jsii.get(self, "matchCondition"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="matchConditionInput")
    def match_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyCustomRuleMatchCondition]]], jsii.get(self, "matchConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitDurationInMinutesInput")
    def rate_limit_duration_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rateLimitDurationInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitThresholdInput")
    def rate_limit_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rateLimitThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="rateLimitDurationInMinutes")
    def rate_limit_duration_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rateLimitDurationInMinutes"))

    @rate_limit_duration_in_minutes.setter
    def rate_limit_duration_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleOutputReference, "rate_limit_duration_in_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rateLimitDurationInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="rateLimitThreshold")
    def rate_limit_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rateLimitThreshold"))

    @rate_limit_threshold.setter
    def rate_limit_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleOutputReference, "rate_limit_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rateLimitThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyCustomRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyCustomRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyCustomRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyCustomRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRule",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "type": "type",
        "version": "version",
        "exclusion": "exclusion",
        "override": "override",
    },
)
class CdnFrontdoorFirewallPolicyManagedRule:
    def __init__(
        self,
        *,
        action: builtins.str,
        type: builtins.str,
        version: builtins.str,
        exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRuleExclusion", typing.Dict[str, typing.Any]]]]] = None,
        override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRuleOverride", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#action CdnFrontdoorFirewallPolicy#action}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#type CdnFrontdoorFirewallPolicy#type}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#version CdnFrontdoorFirewallPolicy#version}.
        :param exclusion: exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#exclusion CdnFrontdoorFirewallPolicy#exclusion}
        :param override: override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#override CdnFrontdoorFirewallPolicy#override}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument exclusion", value=exclusion, expected_type=type_hints["exclusion"])
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "type": type,
            "version": version,
        }
        if exclusion is not None:
            self._values["exclusion"] = exclusion
        if override is not None:
            self._values["override"] = override

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#action CdnFrontdoorFirewallPolicy#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#type CdnFrontdoorFirewallPolicy#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#version CdnFrontdoorFirewallPolicy#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusion(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleExclusion"]]]:
        '''exclusion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#exclusion CdnFrontdoorFirewallPolicy#exclusion}
        '''
        result = self._values.get("exclusion")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleExclusion"]]], result)

    @builtins.property
    def override(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverride"]]]:
        '''override block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#override CdnFrontdoorFirewallPolicy#override}
        '''
        result = self._values.get("override")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverride"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyManagedRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleExclusion",
    jsii_struct_bases=[],
    name_mapping={
        "match_variable": "matchVariable",
        "operator": "operator",
        "selector": "selector",
    },
)
class CdnFrontdoorFirewallPolicyManagedRuleExclusion:
    def __init__(
        self,
        *,
        match_variable: builtins.str,
        operator: builtins.str,
        selector: builtins.str,
    ) -> None:
        '''
        :param match_variable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_variable CdnFrontdoorFirewallPolicy#match_variable}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#operator CdnFrontdoorFirewallPolicy#operator}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#selector CdnFrontdoorFirewallPolicy#selector}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleExclusion.__init__)
            check_type(argname="argument match_variable", value=match_variable, expected_type=type_hints["match_variable"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_variable": match_variable,
            "operator": operator,
            "selector": selector,
        }

    @builtins.property
    def match_variable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_variable CdnFrontdoorFirewallPolicy#match_variable}.'''
        result = self._values.get("match_variable")
        assert result is not None, "Required property 'match_variable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#operator CdnFrontdoorFirewallPolicy#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#selector CdnFrontdoorFirewallPolicy#selector}.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyManagedRuleExclusion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorFirewallPolicyManagedRuleExclusionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleExclusionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleExclusionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleExclusionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleExclusionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleExclusionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleExclusionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleExclusion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleExclusion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleExclusionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="matchVariableInput")
    def match_variable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchVariable")
    def match_variable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchVariable"))

    @match_variable.setter
    def match_variable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference, "match_variable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchVariable", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleExclusion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleExclusion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleExclusion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorFirewallPolicyManagedRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExclusion")
    def put_exclusion(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleExclusion, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOutputReference.put_exclusion)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclusion", [value]))

    @jsii.member(jsii_name="putOverride")
    def put_override(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRuleOverride", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOutputReference.put_override)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOverride", [value]))

    @jsii.member(jsii_name="resetExclusion")
    def reset_exclusion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusion", []))

    @jsii.member(jsii_name="resetOverride")
    def reset_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverride", []))

    @builtins.property
    @jsii.member(jsii_name="exclusion")
    def exclusion(self) -> CdnFrontdoorFirewallPolicyManagedRuleExclusionList:
        return typing.cast(CdnFrontdoorFirewallPolicyManagedRuleExclusionList, jsii.get(self, "exclusion"))

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(self) -> "CdnFrontdoorFirewallPolicyManagedRuleOverrideList":
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleOverrideList", jsii.get(self, "override"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionInput")
    def exclusion_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleExclusion]]], jsii.get(self, "exclusionInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverride"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverride"]]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverride",
    jsii_struct_bases=[],
    name_mapping={
        "rule_group_name": "ruleGroupName",
        "exclusion": "exclusion",
        "rule": "rule",
    },
)
class CdnFrontdoorFirewallPolicyManagedRuleOverride:
    def __init__(
        self,
        *,
        rule_group_name: builtins.str,
        exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion", typing.Dict[str, typing.Any]]]]] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRuleOverrideRule", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rule_group_name CdnFrontdoorFirewallPolicy#rule_group_name}.
        :param exclusion: exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#exclusion CdnFrontdoorFirewallPolicy#exclusion}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rule CdnFrontdoorFirewallPolicy#rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverride.__init__)
            check_type(argname="argument rule_group_name", value=rule_group_name, expected_type=type_hints["rule_group_name"])
            check_type(argname="argument exclusion", value=exclusion, expected_type=type_hints["exclusion"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule_group_name": rule_group_name,
        }
        if exclusion is not None:
            self._values["exclusion"] = exclusion
        if rule is not None:
            self._values["rule"] = rule

    @builtins.property
    def rule_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rule_group_name CdnFrontdoorFirewallPolicy#rule_group_name}.'''
        result = self._values.get("rule_group_name")
        assert result is not None, "Required property 'rule_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusion(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion"]]]:
        '''exclusion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#exclusion CdnFrontdoorFirewallPolicy#exclusion}
        '''
        result = self._values.get("exclusion")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion"]]], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverrideRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rule CdnFrontdoorFirewallPolicy#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverrideRule"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyManagedRuleOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion",
    jsii_struct_bases=[],
    name_mapping={
        "match_variable": "matchVariable",
        "operator": "operator",
        "selector": "selector",
    },
)
class CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion:
    def __init__(
        self,
        *,
        match_variable: builtins.str,
        operator: builtins.str,
        selector: builtins.str,
    ) -> None:
        '''
        :param match_variable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_variable CdnFrontdoorFirewallPolicy#match_variable}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#operator CdnFrontdoorFirewallPolicy#operator}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#selector CdnFrontdoorFirewallPolicy#selector}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion.__init__)
            check_type(argname="argument match_variable", value=match_variable, expected_type=type_hints["match_variable"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_variable": match_variable,
            "operator": operator,
            "selector": selector,
        }

    @builtins.property
    def match_variable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_variable CdnFrontdoorFirewallPolicy#match_variable}.'''
        result = self._values.get("match_variable")
        assert result is not None, "Required property 'match_variable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#operator CdnFrontdoorFirewallPolicy#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#selector CdnFrontdoorFirewallPolicy#selector}.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="matchVariableInput")
    def match_variable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchVariable")
    def match_variable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchVariable"))

    @match_variable.setter
    def match_variable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference, "match_variable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchVariable", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleOverrideList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverride]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverride]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverride]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExclusion")
    def put_exclusion(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference.put_exclusion)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclusion", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRuleOverrideRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference.put_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetExclusion")
    def reset_exclusion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusion", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @builtins.property
    @jsii.member(jsii_name="exclusion")
    def exclusion(self) -> CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList:
        return typing.cast(CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList, jsii.get(self, "exclusion"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList":
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="exclusionInput")
    def exclusion_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion]]], jsii.get(self, "exclusionInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupNameInput")
    def rule_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverrideRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverrideRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupName")
    def rule_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleGroupName"))

    @rule_group_name.setter
    def rule_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference, "rule_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverride, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverride, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverride, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideRule",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "rule_id": "ruleId",
        "enabled": "enabled",
        "exclusion": "exclusion",
    },
)
class CdnFrontdoorFirewallPolicyManagedRuleOverrideRule:
    def __init__(
        self,
        *,
        action: builtins.str,
        rule_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclusion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#action CdnFrontdoorFirewallPolicy#action}.
        :param rule_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rule_id CdnFrontdoorFirewallPolicy#rule_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#enabled CdnFrontdoorFirewallPolicy#enabled}.
        :param exclusion: exclusion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#exclusion CdnFrontdoorFirewallPolicy#exclusion}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument exclusion", value=exclusion, expected_type=type_hints["exclusion"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "rule_id": rule_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if exclusion is not None:
            self._values["exclusion"] = exclusion

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#action CdnFrontdoorFirewallPolicy#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#rule_id CdnFrontdoorFirewallPolicy#rule_id}.'''
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#enabled CdnFrontdoorFirewallPolicy#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exclusion(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion"]]]:
        '''exclusion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#exclusion CdnFrontdoorFirewallPolicy#exclusion}
        '''
        result = self._values.get("exclusion")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyManagedRuleOverrideRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion",
    jsii_struct_bases=[],
    name_mapping={
        "match_variable": "matchVariable",
        "operator": "operator",
        "selector": "selector",
    },
)
class CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion:
    def __init__(
        self,
        *,
        match_variable: builtins.str,
        operator: builtins.str,
        selector: builtins.str,
    ) -> None:
        '''
        :param match_variable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_variable CdnFrontdoorFirewallPolicy#match_variable}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#operator CdnFrontdoorFirewallPolicy#operator}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#selector CdnFrontdoorFirewallPolicy#selector}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion.__init__)
            check_type(argname="argument match_variable", value=match_variable, expected_type=type_hints["match_variable"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_variable": match_variable,
            "operator": operator,
            "selector": selector,
        }

    @builtins.property
    def match_variable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#match_variable CdnFrontdoorFirewallPolicy#match_variable}.'''
        result = self._values.get("match_variable")
        assert result is not None, "Required property 'match_variable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#operator CdnFrontdoorFirewallPolicy#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#selector CdnFrontdoorFirewallPolicy#selector}.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="matchVariableInput")
    def match_variable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchVariable")
    def match_variable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchVariable"))

    @match_variable.setter
    def match_variable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference, "match_variable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchVariable", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExclusion")
    def put_exclusion(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference.put_exclusion)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclusion", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetExclusion")
    def reset_exclusion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusion", []))

    @builtins.property
    @jsii.member(jsii_name="exclusion")
    def exclusion(
        self,
    ) -> CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList:
        return typing.cast(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList, jsii.get(self, "exclusion"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionInput")
    def exclusion_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion]]], jsii.get(self, "exclusionInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleIdInput")
    def rule_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="ruleId")
    def rule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleId"))

    @rule_id.setter
    def rule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference, "rule_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyManagedRuleOverrideRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CdnFrontdoorFirewallPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#create CdnFrontdoorFirewallPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#delete CdnFrontdoorFirewallPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#read CdnFrontdoorFirewallPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#update CdnFrontdoorFirewallPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#create CdnFrontdoorFirewallPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#delete CdnFrontdoorFirewallPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#read CdnFrontdoorFirewallPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_firewall_policy#update CdnFrontdoorFirewallPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorFirewallPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorFirewallPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorFirewallPolicy.CdnFrontdoorFirewallPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorFirewallPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorFirewallPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorFirewallPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CdnFrontdoorFirewallPolicy",
    "CdnFrontdoorFirewallPolicyConfig",
    "CdnFrontdoorFirewallPolicyCustomRule",
    "CdnFrontdoorFirewallPolicyCustomRuleList",
    "CdnFrontdoorFirewallPolicyCustomRuleMatchCondition",
    "CdnFrontdoorFirewallPolicyCustomRuleMatchConditionList",
    "CdnFrontdoorFirewallPolicyCustomRuleMatchConditionOutputReference",
    "CdnFrontdoorFirewallPolicyCustomRuleOutputReference",
    "CdnFrontdoorFirewallPolicyManagedRule",
    "CdnFrontdoorFirewallPolicyManagedRuleExclusion",
    "CdnFrontdoorFirewallPolicyManagedRuleExclusionList",
    "CdnFrontdoorFirewallPolicyManagedRuleExclusionOutputReference",
    "CdnFrontdoorFirewallPolicyManagedRuleList",
    "CdnFrontdoorFirewallPolicyManagedRuleOutputReference",
    "CdnFrontdoorFirewallPolicyManagedRuleOverride",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusion",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionList",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideExclusionOutputReference",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideList",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideOutputReference",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideRule",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusion",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionList",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleExclusionOutputReference",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleList",
    "CdnFrontdoorFirewallPolicyManagedRuleOverrideRuleOutputReference",
    "CdnFrontdoorFirewallPolicyTimeouts",
    "CdnFrontdoorFirewallPolicyTimeoutsOutputReference",
]

publication.publish()
