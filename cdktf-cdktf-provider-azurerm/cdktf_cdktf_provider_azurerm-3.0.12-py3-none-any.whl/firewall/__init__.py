'''
# `azurerm_firewall`

Refer to the Terraform Registory for docs: [`azurerm_firewall`](https://www.terraform.io/docs/providers/azurerm/r/firewall).
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


class Firewall(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewall.Firewall",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/firewall azurerm_firewall}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        sku_tier: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        firewall_policy_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallIpConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        management_ip_configuration: typing.Optional[typing.Union["FirewallManagementIpConfiguration", typing.Dict[str, typing.Any]]] = None,
        private_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        threat_intel_mode: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["FirewallTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_hub: typing.Optional[typing.Union["FirewallVirtualHub", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/firewall azurerm_firewall} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#location Firewall#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#name Firewall#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#resource_group_name Firewall#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#sku_name Firewall#sku_name}.
        :param sku_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#sku_tier Firewall#sku_tier}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#dns_servers Firewall#dns_servers}.
        :param firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#firewall_policy_id Firewall#firewall_policy_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#id Firewall#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#ip_configuration Firewall#ip_configuration}
        :param management_ip_configuration: management_ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#management_ip_configuration Firewall#management_ip_configuration}
        :param private_ip_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#private_ip_ranges Firewall#private_ip_ranges}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#tags Firewall#tags}.
        :param threat_intel_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#threat_intel_mode Firewall#threat_intel_mode}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#timeouts Firewall#timeouts}
        :param virtual_hub: virtual_hub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#virtual_hub Firewall#virtual_hub}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#zones Firewall#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Firewall.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FirewallConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            sku_tier=sku_tier,
            dns_servers=dns_servers,
            firewall_policy_id=firewall_policy_id,
            id=id,
            ip_configuration=ip_configuration,
            management_ip_configuration=management_ip_configuration,
            private_ip_ranges=private_ip_ranges,
            tags=tags,
            threat_intel_mode=threat_intel_mode,
            timeouts=timeouts,
            virtual_hub=virtual_hub,
            zones=zones,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallIpConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Firewall.put_ip_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

    @jsii.member(jsii_name="putManagementIpConfiguration")
    def put_management_ip_configuration(
        self,
        *,
        name: builtins.str,
        public_ip_address_id: builtins.str,
        subnet_id: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#name Firewall#name}.
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#public_ip_address_id Firewall#public_ip_address_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#subnet_id Firewall#subnet_id}.
        '''
        value = FirewallManagementIpConfiguration(
            name=name, public_ip_address_id=public_ip_address_id, subnet_id=subnet_id
        )

        return typing.cast(None, jsii.invoke(self, "putManagementIpConfiguration", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#create Firewall#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#delete Firewall#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#read Firewall#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#update Firewall#update}.
        '''
        value = FirewallTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVirtualHub")
    def put_virtual_hub(
        self,
        *,
        virtual_hub_id: builtins.str,
        public_ip_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param virtual_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#virtual_hub_id Firewall#virtual_hub_id}.
        :param public_ip_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#public_ip_count Firewall#public_ip_count}.
        '''
        value = FirewallVirtualHub(
            virtual_hub_id=virtual_hub_id, public_ip_count=public_ip_count
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualHub", [value]))

    @jsii.member(jsii_name="resetDnsServers")
    def reset_dns_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServers", []))

    @jsii.member(jsii_name="resetFirewallPolicyId")
    def reset_firewall_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewallPolicyId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpConfiguration")
    def reset_ip_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpConfiguration", []))

    @jsii.member(jsii_name="resetManagementIpConfiguration")
    def reset_management_ip_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagementIpConfiguration", []))

    @jsii.member(jsii_name="resetPrivateIpRanges")
    def reset_private_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpRanges", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetThreatIntelMode")
    def reset_threat_intel_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreatIntelMode", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVirtualHub")
    def reset_virtual_hub(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualHub", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(self) -> "FirewallIpConfigurationList":
        return typing.cast("FirewallIpConfigurationList", jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="managementIpConfiguration")
    def management_ip_configuration(
        self,
    ) -> "FirewallManagementIpConfigurationOutputReference":
        return typing.cast("FirewallManagementIpConfigurationOutputReference", jsii.get(self, "managementIpConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FirewallTimeoutsOutputReference":
        return typing.cast("FirewallTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualHub")
    def virtual_hub(self) -> "FirewallVirtualHubOutputReference":
        return typing.cast("FirewallVirtualHubOutputReference", jsii.get(self, "virtualHub"))

    @builtins.property
    @jsii.member(jsii_name="dnsServersInput")
    def dns_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsServersInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyIdInput")
    def firewall_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallIpConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallIpConfiguration"]]], jsii.get(self, "ipConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managementIpConfigurationInput")
    def management_ip_configuration_input(
        self,
    ) -> typing.Optional["FirewallManagementIpConfiguration"]:
        return typing.cast(typing.Optional["FirewallManagementIpConfiguration"], jsii.get(self, "managementIpConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpRangesInput")
    def private_ip_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privateIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuTierInput")
    def sku_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuTierInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="threatIntelModeInput")
    def threat_intel_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "threatIntelModeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["FirewallTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FirewallTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualHubInput")
    def virtual_hub_input(self) -> typing.Optional["FirewallVirtualHub"]:
        return typing.cast(typing.Optional["FirewallVirtualHub"], jsii.get(self, "virtualHubInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServers")
    def dns_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsServers"))

    @dns_servers.setter
    def dns_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "dns_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServers", value)

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyId")
    def firewall_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallPolicyId"))

    @firewall_policy_id.setter
    def firewall_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "firewall_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpRanges")
    def private_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIpRanges"))

    @private_ip_ranges.setter
    def private_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "private_ip_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="skuTier")
    def sku_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuTier"))

    @sku_tier.setter
    def sku_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "sku_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuTier", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="threatIntelMode")
    def threat_intel_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "threatIntelMode"))

    @threat_intel_mode.setter
    def threat_intel_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "threat_intel_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threatIntelMode", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Firewall, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallConfig",
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
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "sku_tier": "skuTier",
        "dns_servers": "dnsServers",
        "firewall_policy_id": "firewallPolicyId",
        "id": "id",
        "ip_configuration": "ipConfiguration",
        "management_ip_configuration": "managementIpConfiguration",
        "private_ip_ranges": "privateIpRanges",
        "tags": "tags",
        "threat_intel_mode": "threatIntelMode",
        "timeouts": "timeouts",
        "virtual_hub": "virtualHub",
        "zones": "zones",
    },
)
class FirewallConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        sku_tier: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        firewall_policy_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallIpConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        management_ip_configuration: typing.Optional[typing.Union["FirewallManagementIpConfiguration", typing.Dict[str, typing.Any]]] = None,
        private_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        threat_intel_mode: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["FirewallTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_hub: typing.Optional[typing.Union["FirewallVirtualHub", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#location Firewall#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#name Firewall#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#resource_group_name Firewall#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#sku_name Firewall#sku_name}.
        :param sku_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#sku_tier Firewall#sku_tier}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#dns_servers Firewall#dns_servers}.
        :param firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#firewall_policy_id Firewall#firewall_policy_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#id Firewall#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#ip_configuration Firewall#ip_configuration}
        :param management_ip_configuration: management_ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#management_ip_configuration Firewall#management_ip_configuration}
        :param private_ip_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#private_ip_ranges Firewall#private_ip_ranges}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#tags Firewall#tags}.
        :param threat_intel_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#threat_intel_mode Firewall#threat_intel_mode}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#timeouts Firewall#timeouts}
        :param virtual_hub: virtual_hub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#virtual_hub Firewall#virtual_hub}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#zones Firewall#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(management_ip_configuration, dict):
            management_ip_configuration = FirewallManagementIpConfiguration(**management_ip_configuration)
        if isinstance(timeouts, dict):
            timeouts = FirewallTimeouts(**timeouts)
        if isinstance(virtual_hub, dict):
            virtual_hub = FirewallVirtualHub(**virtual_hub)
        if __debug__:
            type_hints = typing.get_type_hints(FirewallConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument sku_tier", value=sku_tier, expected_type=type_hints["sku_tier"])
            check_type(argname="argument dns_servers", value=dns_servers, expected_type=type_hints["dns_servers"])
            check_type(argname="argument firewall_policy_id", value=firewall_policy_id, expected_type=type_hints["firewall_policy_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument management_ip_configuration", value=management_ip_configuration, expected_type=type_hints["management_ip_configuration"])
            check_type(argname="argument private_ip_ranges", value=private_ip_ranges, expected_type=type_hints["private_ip_ranges"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument threat_intel_mode", value=threat_intel_mode, expected_type=type_hints["threat_intel_mode"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_hub", value=virtual_hub, expected_type=type_hints["virtual_hub"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
            "sku_tier": sku_tier,
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
        if dns_servers is not None:
            self._values["dns_servers"] = dns_servers
        if firewall_policy_id is not None:
            self._values["firewall_policy_id"] = firewall_policy_id
        if id is not None:
            self._values["id"] = id
        if ip_configuration is not None:
            self._values["ip_configuration"] = ip_configuration
        if management_ip_configuration is not None:
            self._values["management_ip_configuration"] = management_ip_configuration
        if private_ip_ranges is not None:
            self._values["private_ip_ranges"] = private_ip_ranges
        if tags is not None:
            self._values["tags"] = tags
        if threat_intel_mode is not None:
            self._values["threat_intel_mode"] = threat_intel_mode
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if virtual_hub is not None:
            self._values["virtual_hub"] = virtual_hub
        if zones is not None:
            self._values["zones"] = zones

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#location Firewall#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#name Firewall#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#resource_group_name Firewall#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#sku_name Firewall#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_tier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#sku_tier Firewall#sku_tier}.'''
        result = self._values.get("sku_tier")
        assert result is not None, "Required property 'sku_tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#dns_servers Firewall#dns_servers}.'''
        result = self._values.get("dns_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def firewall_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#firewall_policy_id Firewall#firewall_policy_id}.'''
        result = self._values.get("firewall_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#id Firewall#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallIpConfiguration"]]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#ip_configuration Firewall#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallIpConfiguration"]]], result)

    @builtins.property
    def management_ip_configuration(
        self,
    ) -> typing.Optional["FirewallManagementIpConfiguration"]:
        '''management_ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#management_ip_configuration Firewall#management_ip_configuration}
        '''
        result = self._values.get("management_ip_configuration")
        return typing.cast(typing.Optional["FirewallManagementIpConfiguration"], result)

    @builtins.property
    def private_ip_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#private_ip_ranges Firewall#private_ip_ranges}.'''
        result = self._values.get("private_ip_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#tags Firewall#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def threat_intel_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#threat_intel_mode Firewall#threat_intel_mode}.'''
        result = self._values.get("threat_intel_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FirewallTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#timeouts Firewall#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FirewallTimeouts"], result)

    @builtins.property
    def virtual_hub(self) -> typing.Optional["FirewallVirtualHub"]:
        '''virtual_hub block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#virtual_hub Firewall#virtual_hub}
        '''
        result = self._values.get("virtual_hub")
        return typing.cast(typing.Optional["FirewallVirtualHub"], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#zones Firewall#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "public_ip_address_id": "publicIpAddressId",
        "subnet_id": "subnetId",
    },
)
class FirewallIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        public_ip_address_id: builtins.str,
        subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#name Firewall#name}.
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#public_ip_address_id Firewall#public_ip_address_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#subnet_id Firewall#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallIpConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_ip_address_id", value=public_ip_address_id, expected_type=type_hints["public_ip_address_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "public_ip_address_id": public_ip_address_id,
        }
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#name Firewall#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_ip_address_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#public_ip_address_id Firewall#public_ip_address_id}.'''
        result = self._values.get("public_ip_address_id")
        assert result is not None, "Required property 'public_ip_address_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#subnet_id Firewall#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallIpConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallIpConfigurationList",
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
            type_hints = typing.get_type_hints(FirewallIpConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FirewallIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallIpConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallIpConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallIpConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallIpConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallIpConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(FirewallIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressIdInput")
    def public_ip_address_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpAddressIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressId")
    def public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressId"))

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallIpConfigurationOutputReference, "public_ip_address_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallIpConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallIpConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallIpConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallIpConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallManagementIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "public_ip_address_id": "publicIpAddressId",
        "subnet_id": "subnetId",
    },
)
class FirewallManagementIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        public_ip_address_id: builtins.str,
        subnet_id: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#name Firewall#name}.
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#public_ip_address_id Firewall#public_ip_address_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#subnet_id Firewall#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallManagementIpConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_ip_address_id", value=public_ip_address_id, expected_type=type_hints["public_ip_address_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "public_ip_address_id": public_ip_address_id,
            "subnet_id": subnet_id,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#name Firewall#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_ip_address_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#public_ip_address_id Firewall#public_ip_address_id}.'''
        result = self._values.get("public_ip_address_id")
        assert result is not None, "Required property 'public_ip_address_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#subnet_id Firewall#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallManagementIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallManagementIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallManagementIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(FirewallManagementIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressIdInput")
    def public_ip_address_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpAddressIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallManagementIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressId")
    def public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressId"))

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallManagementIpConfigurationOutputReference, "public_ip_address_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallManagementIpConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FirewallManagementIpConfiguration]:
        return typing.cast(typing.Optional[FirewallManagementIpConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FirewallManagementIpConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallManagementIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class FirewallTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#create Firewall#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#delete Firewall#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#read Firewall#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#update Firewall#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#create Firewall#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#delete Firewall#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#read Firewall#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#update Firewall#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(FirewallTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(FirewallTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallVirtualHub",
    jsii_struct_bases=[],
    name_mapping={
        "virtual_hub_id": "virtualHubId",
        "public_ip_count": "publicIpCount",
    },
)
class FirewallVirtualHub:
    def __init__(
        self,
        *,
        virtual_hub_id: builtins.str,
        public_ip_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param virtual_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#virtual_hub_id Firewall#virtual_hub_id}.
        :param public_ip_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#public_ip_count Firewall#public_ip_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallVirtualHub.__init__)
            check_type(argname="argument virtual_hub_id", value=virtual_hub_id, expected_type=type_hints["virtual_hub_id"])
            check_type(argname="argument public_ip_count", value=public_ip_count, expected_type=type_hints["public_ip_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_hub_id": virtual_hub_id,
        }
        if public_ip_count is not None:
            self._values["public_ip_count"] = public_ip_count

    @builtins.property
    def virtual_hub_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#virtual_hub_id Firewall#virtual_hub_id}.'''
        result = self._values.get("virtual_hub_id")
        assert result is not None, "Required property 'virtual_hub_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_ip_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall#public_ip_count Firewall#public_ip_count}.'''
        result = self._values.get("public_ip_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallVirtualHub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallVirtualHubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewall.FirewallVirtualHubOutputReference",
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
            type_hints = typing.get_type_hints(FirewallVirtualHubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPublicIpCount")
    def reset_public_ip_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpCount", []))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddresses")
    def public_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "publicIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="publicIpCountInput")
    def public_ip_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "publicIpCountInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualHubIdInput")
    def virtual_hub_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualHubIdInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpCount")
    def public_ip_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "publicIpCount"))

    @public_ip_count.setter
    def public_ip_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallVirtualHubOutputReference, "public_ip_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpCount", value)

    @builtins.property
    @jsii.member(jsii_name="virtualHubId")
    def virtual_hub_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualHubId"))

    @virtual_hub_id.setter
    def virtual_hub_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallVirtualHubOutputReference, "virtual_hub_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualHubId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FirewallVirtualHub]:
        return typing.cast(typing.Optional[FirewallVirtualHub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[FirewallVirtualHub]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallVirtualHubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Firewall",
    "FirewallConfig",
    "FirewallIpConfiguration",
    "FirewallIpConfigurationList",
    "FirewallIpConfigurationOutputReference",
    "FirewallManagementIpConfiguration",
    "FirewallManagementIpConfigurationOutputReference",
    "FirewallTimeouts",
    "FirewallTimeoutsOutputReference",
    "FirewallVirtualHub",
    "FirewallVirtualHubOutputReference",
]

publication.publish()
