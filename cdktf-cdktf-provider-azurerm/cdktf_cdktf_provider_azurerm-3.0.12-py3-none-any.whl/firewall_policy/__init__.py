'''
# `azurerm_firewall_policy`

Refer to the Terraform Registory for docs: [`azurerm_firewall_policy`](https://www.terraform.io/docs/providers/azurerm/r/firewall_policy).
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


class FirewallPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy azurerm_firewall_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        base_policy_id: typing.Optional[builtins.str] = None,
        dns: typing.Optional[typing.Union["FirewallPolicyDns", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["FirewallPolicyIdentity", typing.Dict[str, typing.Any]]] = None,
        insights: typing.Optional[typing.Union["FirewallPolicyInsights", typing.Dict[str, typing.Any]]] = None,
        intrusion_detection: typing.Optional[typing.Union["FirewallPolicyIntrusionDetection", typing.Dict[str, typing.Any]]] = None,
        private_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        sku: typing.Optional[builtins.str] = None,
        sql_redirect_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        threat_intelligence_allowlist: typing.Optional[typing.Union["FirewallPolicyThreatIntelligenceAllowlist", typing.Dict[str, typing.Any]]] = None,
        threat_intelligence_mode: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["FirewallPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        tls_certificate: typing.Optional[typing.Union["FirewallPolicyTlsCertificate", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy azurerm_firewall_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#location FirewallPolicy#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#name FirewallPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#resource_group_name FirewallPolicy#resource_group_name}.
        :param base_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#base_policy_id FirewallPolicy#base_policy_id}.
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#dns FirewallPolicy#dns}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#id FirewallPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#identity FirewallPolicy#identity}
        :param insights: insights block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#insights FirewallPolicy#insights}
        :param intrusion_detection: intrusion_detection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#intrusion_detection FirewallPolicy#intrusion_detection}
        :param private_ip_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#private_ip_ranges FirewallPolicy#private_ip_ranges}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#sku FirewallPolicy#sku}.
        :param sql_redirect_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#sql_redirect_allowed FirewallPolicy#sql_redirect_allowed}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#tags FirewallPolicy#tags}.
        :param threat_intelligence_allowlist: threat_intelligence_allowlist block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#threat_intelligence_allowlist FirewallPolicy#threat_intelligence_allowlist}
        :param threat_intelligence_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#threat_intelligence_mode FirewallPolicy#threat_intelligence_mode}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#timeouts FirewallPolicy#timeouts}
        :param tls_certificate: tls_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#tls_certificate FirewallPolicy#tls_certificate}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FirewallPolicyConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            base_policy_id=base_policy_id,
            dns=dns,
            id=id,
            identity=identity,
            insights=insights,
            intrusion_detection=intrusion_detection,
            private_ip_ranges=private_ip_ranges,
            sku=sku,
            sql_redirect_allowed=sql_redirect_allowed,
            tags=tags,
            threat_intelligence_allowlist=threat_intelligence_allowlist,
            threat_intelligence_mode=threat_intelligence_mode,
            timeouts=timeouts,
            tls_certificate=tls_certificate,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDns")
    def put_dns(
        self,
        *,
        proxy_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param proxy_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#proxy_enabled FirewallPolicy#proxy_enabled}.
        :param servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#servers FirewallPolicy#servers}.
        '''
        value = FirewallPolicyDns(proxy_enabled=proxy_enabled, servers=servers)

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#identity_ids FirewallPolicy#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#type FirewallPolicy#type}.
        '''
        value = FirewallPolicyIdentity(identity_ids=identity_ids, type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putInsights")
    def put_insights(
        self,
        *,
        default_log_analytics_workspace_id: builtins.str,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        log_analytics_workspace: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyInsightsLogAnalyticsWorkspace", typing.Dict[str, typing.Any]]]]] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param default_log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#default_log_analytics_workspace_id FirewallPolicy#default_log_analytics_workspace_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#enabled FirewallPolicy#enabled}.
        :param log_analytics_workspace: log_analytics_workspace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#log_analytics_workspace FirewallPolicy#log_analytics_workspace}
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#retention_in_days FirewallPolicy#retention_in_days}.
        '''
        value = FirewallPolicyInsights(
            default_log_analytics_workspace_id=default_log_analytics_workspace_id,
            enabled=enabled,
            log_analytics_workspace=log_analytics_workspace,
            retention_in_days=retention_in_days,
        )

        return typing.cast(None, jsii.invoke(self, "putInsights", [value]))

    @jsii.member(jsii_name="putIntrusionDetection")
    def put_intrusion_detection(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        private_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        signature_overrides: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyIntrusionDetectionSignatureOverrides", typing.Dict[str, typing.Any]]]]] = None,
        traffic_bypass: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyIntrusionDetectionTrafficBypass", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#mode FirewallPolicy#mode}.
        :param private_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#private_ranges FirewallPolicy#private_ranges}.
        :param signature_overrides: signature_overrides block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#signature_overrides FirewallPolicy#signature_overrides}
        :param traffic_bypass: traffic_bypass block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#traffic_bypass FirewallPolicy#traffic_bypass}
        '''
        value = FirewallPolicyIntrusionDetection(
            mode=mode,
            private_ranges=private_ranges,
            signature_overrides=signature_overrides,
            traffic_bypass=traffic_bypass,
        )

        return typing.cast(None, jsii.invoke(self, "putIntrusionDetection", [value]))

    @jsii.member(jsii_name="putThreatIntelligenceAllowlist")
    def put_threat_intelligence_allowlist(
        self,
        *,
        fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#fqdns FirewallPolicy#fqdns}.
        :param ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#ip_addresses FirewallPolicy#ip_addresses}.
        '''
        value = FirewallPolicyThreatIntelligenceAllowlist(
            fqdns=fqdns, ip_addresses=ip_addresses
        )

        return typing.cast(None, jsii.invoke(self, "putThreatIntelligenceAllowlist", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#create FirewallPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#delete FirewallPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#read FirewallPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#update FirewallPolicy#update}.
        '''
        value = FirewallPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTlsCertificate")
    def put_tls_certificate(
        self,
        *,
        key_vault_secret_id: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param key_vault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#key_vault_secret_id FirewallPolicy#key_vault_secret_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#name FirewallPolicy#name}.
        '''
        value = FirewallPolicyTlsCertificate(
            key_vault_secret_id=key_vault_secret_id, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putTlsCertificate", [value]))

    @jsii.member(jsii_name="resetBasePolicyId")
    def reset_base_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasePolicyId", []))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetInsights")
    def reset_insights(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsights", []))

    @jsii.member(jsii_name="resetIntrusionDetection")
    def reset_intrusion_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntrusionDetection", []))

    @jsii.member(jsii_name="resetPrivateIpRanges")
    def reset_private_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpRanges", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @jsii.member(jsii_name="resetSqlRedirectAllowed")
    def reset_sql_redirect_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlRedirectAllowed", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetThreatIntelligenceAllowlist")
    def reset_threat_intelligence_allowlist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreatIntelligenceAllowlist", []))

    @jsii.member(jsii_name="resetThreatIntelligenceMode")
    def reset_threat_intelligence_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreatIntelligenceMode", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTlsCertificate")
    def reset_tls_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsCertificate", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="childPolicies")
    def child_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "childPolicies"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> "FirewallPolicyDnsOutputReference":
        return typing.cast("FirewallPolicyDnsOutputReference", jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="firewalls")
    def firewalls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "firewalls"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "FirewallPolicyIdentityOutputReference":
        return typing.cast("FirewallPolicyIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="insights")
    def insights(self) -> "FirewallPolicyInsightsOutputReference":
        return typing.cast("FirewallPolicyInsightsOutputReference", jsii.get(self, "insights"))

    @builtins.property
    @jsii.member(jsii_name="intrusionDetection")
    def intrusion_detection(self) -> "FirewallPolicyIntrusionDetectionOutputReference":
        return typing.cast("FirewallPolicyIntrusionDetectionOutputReference", jsii.get(self, "intrusionDetection"))

    @builtins.property
    @jsii.member(jsii_name="ruleCollectionGroups")
    def rule_collection_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ruleCollectionGroups"))

    @builtins.property
    @jsii.member(jsii_name="threatIntelligenceAllowlist")
    def threat_intelligence_allowlist(
        self,
    ) -> "FirewallPolicyThreatIntelligenceAllowlistOutputReference":
        return typing.cast("FirewallPolicyThreatIntelligenceAllowlistOutputReference", jsii.get(self, "threatIntelligenceAllowlist"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FirewallPolicyTimeoutsOutputReference":
        return typing.cast("FirewallPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tlsCertificate")
    def tls_certificate(self) -> "FirewallPolicyTlsCertificateOutputReference":
        return typing.cast("FirewallPolicyTlsCertificateOutputReference", jsii.get(self, "tlsCertificate"))

    @builtins.property
    @jsii.member(jsii_name="basePolicyIdInput")
    def base_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basePolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional["FirewallPolicyDns"]:
        return typing.cast(typing.Optional["FirewallPolicyDns"], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["FirewallPolicyIdentity"]:
        return typing.cast(typing.Optional["FirewallPolicyIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="insightsInput")
    def insights_input(self) -> typing.Optional["FirewallPolicyInsights"]:
        return typing.cast(typing.Optional["FirewallPolicyInsights"], jsii.get(self, "insightsInput"))

    @builtins.property
    @jsii.member(jsii_name="intrusionDetectionInput")
    def intrusion_detection_input(
        self,
    ) -> typing.Optional["FirewallPolicyIntrusionDetection"]:
        return typing.cast(typing.Optional["FirewallPolicyIntrusionDetection"], jsii.get(self, "intrusionDetectionInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

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
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlRedirectAllowedInput")
    def sql_redirect_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sqlRedirectAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="threatIntelligenceAllowlistInput")
    def threat_intelligence_allowlist_input(
        self,
    ) -> typing.Optional["FirewallPolicyThreatIntelligenceAllowlist"]:
        return typing.cast(typing.Optional["FirewallPolicyThreatIntelligenceAllowlist"], jsii.get(self, "threatIntelligenceAllowlistInput"))

    @builtins.property
    @jsii.member(jsii_name="threatIntelligenceModeInput")
    def threat_intelligence_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "threatIntelligenceModeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["FirewallPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FirewallPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsCertificateInput")
    def tls_certificate_input(self) -> typing.Optional["FirewallPolicyTlsCertificate"]:
        return typing.cast(typing.Optional["FirewallPolicyTlsCertificate"], jsii.get(self, "tlsCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="basePolicyId")
    def base_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basePolicyId"))

    @base_policy_id.setter
    def base_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "base_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basePolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpRanges")
    def private_ip_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIpRanges"))

    @private_ip_ranges.setter
    def private_ip_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "private_ip_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpRanges", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="sqlRedirectAllowed")
    def sql_redirect_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sqlRedirectAllowed"))

    @sql_redirect_allowed.setter
    def sql_redirect_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "sql_redirect_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlRedirectAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="threatIntelligenceMode")
    def threat_intelligence_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "threatIntelligenceMode"))

    @threat_intelligence_mode.setter
    def threat_intelligence_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicy, "threat_intelligence_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threatIntelligenceMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyConfig",
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
        "base_policy_id": "basePolicyId",
        "dns": "dns",
        "id": "id",
        "identity": "identity",
        "insights": "insights",
        "intrusion_detection": "intrusionDetection",
        "private_ip_ranges": "privateIpRanges",
        "sku": "sku",
        "sql_redirect_allowed": "sqlRedirectAllowed",
        "tags": "tags",
        "threat_intelligence_allowlist": "threatIntelligenceAllowlist",
        "threat_intelligence_mode": "threatIntelligenceMode",
        "timeouts": "timeouts",
        "tls_certificate": "tlsCertificate",
    },
)
class FirewallPolicyConfig(cdktf.TerraformMetaArguments):
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
        base_policy_id: typing.Optional[builtins.str] = None,
        dns: typing.Optional[typing.Union["FirewallPolicyDns", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["FirewallPolicyIdentity", typing.Dict[str, typing.Any]]] = None,
        insights: typing.Optional[typing.Union["FirewallPolicyInsights", typing.Dict[str, typing.Any]]] = None,
        intrusion_detection: typing.Optional[typing.Union["FirewallPolicyIntrusionDetection", typing.Dict[str, typing.Any]]] = None,
        private_ip_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        sku: typing.Optional[builtins.str] = None,
        sql_redirect_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        threat_intelligence_allowlist: typing.Optional[typing.Union["FirewallPolicyThreatIntelligenceAllowlist", typing.Dict[str, typing.Any]]] = None,
        threat_intelligence_mode: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["FirewallPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        tls_certificate: typing.Optional[typing.Union["FirewallPolicyTlsCertificate", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#location FirewallPolicy#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#name FirewallPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#resource_group_name FirewallPolicy#resource_group_name}.
        :param base_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#base_policy_id FirewallPolicy#base_policy_id}.
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#dns FirewallPolicy#dns}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#id FirewallPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#identity FirewallPolicy#identity}
        :param insights: insights block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#insights FirewallPolicy#insights}
        :param intrusion_detection: intrusion_detection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#intrusion_detection FirewallPolicy#intrusion_detection}
        :param private_ip_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#private_ip_ranges FirewallPolicy#private_ip_ranges}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#sku FirewallPolicy#sku}.
        :param sql_redirect_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#sql_redirect_allowed FirewallPolicy#sql_redirect_allowed}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#tags FirewallPolicy#tags}.
        :param threat_intelligence_allowlist: threat_intelligence_allowlist block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#threat_intelligence_allowlist FirewallPolicy#threat_intelligence_allowlist}
        :param threat_intelligence_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#threat_intelligence_mode FirewallPolicy#threat_intelligence_mode}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#timeouts FirewallPolicy#timeouts}
        :param tls_certificate: tls_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#tls_certificate FirewallPolicy#tls_certificate}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dns, dict):
            dns = FirewallPolicyDns(**dns)
        if isinstance(identity, dict):
            identity = FirewallPolicyIdentity(**identity)
        if isinstance(insights, dict):
            insights = FirewallPolicyInsights(**insights)
        if isinstance(intrusion_detection, dict):
            intrusion_detection = FirewallPolicyIntrusionDetection(**intrusion_detection)
        if isinstance(threat_intelligence_allowlist, dict):
            threat_intelligence_allowlist = FirewallPolicyThreatIntelligenceAllowlist(**threat_intelligence_allowlist)
        if isinstance(timeouts, dict):
            timeouts = FirewallPolicyTimeouts(**timeouts)
        if isinstance(tls_certificate, dict):
            tls_certificate = FirewallPolicyTlsCertificate(**tls_certificate)
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyConfig.__init__)
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
            check_type(argname="argument base_policy_id", value=base_policy_id, expected_type=type_hints["base_policy_id"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument insights", value=insights, expected_type=type_hints["insights"])
            check_type(argname="argument intrusion_detection", value=intrusion_detection, expected_type=type_hints["intrusion_detection"])
            check_type(argname="argument private_ip_ranges", value=private_ip_ranges, expected_type=type_hints["private_ip_ranges"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument sql_redirect_allowed", value=sql_redirect_allowed, expected_type=type_hints["sql_redirect_allowed"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument threat_intelligence_allowlist", value=threat_intelligence_allowlist, expected_type=type_hints["threat_intelligence_allowlist"])
            check_type(argname="argument threat_intelligence_mode", value=threat_intelligence_mode, expected_type=type_hints["threat_intelligence_mode"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument tls_certificate", value=tls_certificate, expected_type=type_hints["tls_certificate"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
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
        if base_policy_id is not None:
            self._values["base_policy_id"] = base_policy_id
        if dns is not None:
            self._values["dns"] = dns
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if insights is not None:
            self._values["insights"] = insights
        if intrusion_detection is not None:
            self._values["intrusion_detection"] = intrusion_detection
        if private_ip_ranges is not None:
            self._values["private_ip_ranges"] = private_ip_ranges
        if sku is not None:
            self._values["sku"] = sku
        if sql_redirect_allowed is not None:
            self._values["sql_redirect_allowed"] = sql_redirect_allowed
        if tags is not None:
            self._values["tags"] = tags
        if threat_intelligence_allowlist is not None:
            self._values["threat_intelligence_allowlist"] = threat_intelligence_allowlist
        if threat_intelligence_mode is not None:
            self._values["threat_intelligence_mode"] = threat_intelligence_mode
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if tls_certificate is not None:
            self._values["tls_certificate"] = tls_certificate

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#location FirewallPolicy#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#name FirewallPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#resource_group_name FirewallPolicy#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#base_policy_id FirewallPolicy#base_policy_id}.'''
        result = self._values.get("base_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns(self) -> typing.Optional["FirewallPolicyDns"]:
        '''dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#dns FirewallPolicy#dns}
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional["FirewallPolicyDns"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#id FirewallPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["FirewallPolicyIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#identity FirewallPolicy#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["FirewallPolicyIdentity"], result)

    @builtins.property
    def insights(self) -> typing.Optional["FirewallPolicyInsights"]:
        '''insights block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#insights FirewallPolicy#insights}
        '''
        result = self._values.get("insights")
        return typing.cast(typing.Optional["FirewallPolicyInsights"], result)

    @builtins.property
    def intrusion_detection(
        self,
    ) -> typing.Optional["FirewallPolicyIntrusionDetection"]:
        '''intrusion_detection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#intrusion_detection FirewallPolicy#intrusion_detection}
        '''
        result = self._values.get("intrusion_detection")
        return typing.cast(typing.Optional["FirewallPolicyIntrusionDetection"], result)

    @builtins.property
    def private_ip_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#private_ip_ranges FirewallPolicy#private_ip_ranges}.'''
        result = self._values.get("private_ip_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#sku FirewallPolicy#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_redirect_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#sql_redirect_allowed FirewallPolicy#sql_redirect_allowed}.'''
        result = self._values.get("sql_redirect_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#tags FirewallPolicy#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def threat_intelligence_allowlist(
        self,
    ) -> typing.Optional["FirewallPolicyThreatIntelligenceAllowlist"]:
        '''threat_intelligence_allowlist block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#threat_intelligence_allowlist FirewallPolicy#threat_intelligence_allowlist}
        '''
        result = self._values.get("threat_intelligence_allowlist")
        return typing.cast(typing.Optional["FirewallPolicyThreatIntelligenceAllowlist"], result)

    @builtins.property
    def threat_intelligence_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#threat_intelligence_mode FirewallPolicy#threat_intelligence_mode}.'''
        result = self._values.get("threat_intelligence_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FirewallPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#timeouts FirewallPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FirewallPolicyTimeouts"], result)

    @builtins.property
    def tls_certificate(self) -> typing.Optional["FirewallPolicyTlsCertificate"]:
        '''tls_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#tls_certificate FirewallPolicy#tls_certificate}
        '''
        result = self._values.get("tls_certificate")
        return typing.cast(typing.Optional["FirewallPolicyTlsCertificate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyDns",
    jsii_struct_bases=[],
    name_mapping={"proxy_enabled": "proxyEnabled", "servers": "servers"},
)
class FirewallPolicyDns:
    def __init__(
        self,
        *,
        proxy_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param proxy_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#proxy_enabled FirewallPolicy#proxy_enabled}.
        :param servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#servers FirewallPolicy#servers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyDns.__init__)
            check_type(argname="argument proxy_enabled", value=proxy_enabled, expected_type=type_hints["proxy_enabled"])
            check_type(argname="argument servers", value=servers, expected_type=type_hints["servers"])
        self._values: typing.Dict[str, typing.Any] = {}
        if proxy_enabled is not None:
            self._values["proxy_enabled"] = proxy_enabled
        if servers is not None:
            self._values["servers"] = servers

    @builtins.property
    def proxy_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#proxy_enabled FirewallPolicy#proxy_enabled}.'''
        result = self._values.get("proxy_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#servers FirewallPolicy#servers}.'''
        result = self._values.get("servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyDnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyDnsOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyDnsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProxyEnabled")
    def reset_proxy_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyEnabled", []))

    @jsii.member(jsii_name="resetServers")
    def reset_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServers", []))

    @builtins.property
    @jsii.member(jsii_name="proxyEnabledInput")
    def proxy_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "proxyEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="serversInput")
    def servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serversInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyEnabled")
    def proxy_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "proxyEnabled"))

    @proxy_enabled.setter
    def proxy_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyDnsOutputReference, "proxy_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="servers")
    def servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "servers"))

    @servers.setter
    def servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyDnsOutputReference, "servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FirewallPolicyDns]:
        return typing.cast(typing.Optional[FirewallPolicyDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[FirewallPolicyDns]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyDnsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIdentity",
    jsii_struct_bases=[],
    name_mapping={"identity_ids": "identityIds", "type": "type"},
)
class FirewallPolicyIdentity:
    def __init__(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#identity_ids FirewallPolicy#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#type FirewallPolicy#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyIdentity.__init__)
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_ids": identity_ids,
            "type": type,
        }

    @builtins.property
    def identity_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#identity_ids FirewallPolicy#identity_ids}.'''
        result = self._values.get("identity_ids")
        assert result is not None, "Required property 'identity_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#type FirewallPolicy#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIdentityOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FirewallPolicyIdentity]:
        return typing.cast(typing.Optional[FirewallPolicyIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[FirewallPolicyIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyInsights",
    jsii_struct_bases=[],
    name_mapping={
        "default_log_analytics_workspace_id": "defaultLogAnalyticsWorkspaceId",
        "enabled": "enabled",
        "log_analytics_workspace": "logAnalyticsWorkspace",
        "retention_in_days": "retentionInDays",
    },
)
class FirewallPolicyInsights:
    def __init__(
        self,
        *,
        default_log_analytics_workspace_id: builtins.str,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        log_analytics_workspace: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyInsightsLogAnalyticsWorkspace", typing.Dict[str, typing.Any]]]]] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param default_log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#default_log_analytics_workspace_id FirewallPolicy#default_log_analytics_workspace_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#enabled FirewallPolicy#enabled}.
        :param log_analytics_workspace: log_analytics_workspace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#log_analytics_workspace FirewallPolicy#log_analytics_workspace}
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#retention_in_days FirewallPolicy#retention_in_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyInsights.__init__)
            check_type(argname="argument default_log_analytics_workspace_id", value=default_log_analytics_workspace_id, expected_type=type_hints["default_log_analytics_workspace_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_analytics_workspace", value=log_analytics_workspace, expected_type=type_hints["log_analytics_workspace"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_log_analytics_workspace_id": default_log_analytics_workspace_id,
            "enabled": enabled,
        }
        if log_analytics_workspace is not None:
            self._values["log_analytics_workspace"] = log_analytics_workspace
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days

    @builtins.property
    def default_log_analytics_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#default_log_analytics_workspace_id FirewallPolicy#default_log_analytics_workspace_id}.'''
        result = self._values.get("default_log_analytics_workspace_id")
        assert result is not None, "Required property 'default_log_analytics_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#enabled FirewallPolicy#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def log_analytics_workspace(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyInsightsLogAnalyticsWorkspace"]]]:
        '''log_analytics_workspace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#log_analytics_workspace FirewallPolicy#log_analytics_workspace}
        '''
        result = self._values.get("log_analytics_workspace")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyInsightsLogAnalyticsWorkspace"]]], result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#retention_in_days FirewallPolicy#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyInsights(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyInsightsLogAnalyticsWorkspace",
    jsii_struct_bases=[],
    name_mapping={"firewall_location": "firewallLocation", "id": "id"},
)
class FirewallPolicyInsightsLogAnalyticsWorkspace:
    def __init__(self, *, firewall_location: builtins.str, id: builtins.str) -> None:
        '''
        :param firewall_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#firewall_location FirewallPolicy#firewall_location}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#id FirewallPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyInsightsLogAnalyticsWorkspace.__init__)
            check_type(argname="argument firewall_location", value=firewall_location, expected_type=type_hints["firewall_location"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "firewall_location": firewall_location,
            "id": id,
        }

    @builtins.property
    def firewall_location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#firewall_location FirewallPolicy#firewall_location}.'''
        result = self._values.get("firewall_location")
        assert result is not None, "Required property 'firewall_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#id FirewallPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyInsightsLogAnalyticsWorkspace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyInsightsLogAnalyticsWorkspaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyInsightsLogAnalyticsWorkspaceList",
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
            type_hints = typing.get_type_hints(FirewallPolicyInsightsLogAnalyticsWorkspaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyInsightsLogAnalyticsWorkspaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsLogAnalyticsWorkspaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsLogAnalyticsWorkspaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsLogAnalyticsWorkspaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyInsightsLogAnalyticsWorkspace]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyInsightsLogAnalyticsWorkspace]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyInsightsLogAnalyticsWorkspace]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsLogAnalyticsWorkspaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="firewallLocationInput")
    def firewall_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallLocation")
    def firewall_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallLocation"))

    @firewall_location.setter
    def firewall_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference, "firewall_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallLocation", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyInsightsLogAnalyticsWorkspace, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyInsightsLogAnalyticsWorkspace, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyInsightsLogAnalyticsWorkspace, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyInsightsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyInsightsOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyInsightsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogAnalyticsWorkspace")
    def put_log_analytics_workspace(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FirewallPolicyInsightsLogAnalyticsWorkspace, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyInsightsOutputReference.put_log_analytics_workspace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogAnalyticsWorkspace", [value]))

    @jsii.member(jsii_name="resetLogAnalyticsWorkspace")
    def reset_log_analytics_workspace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogAnalyticsWorkspace", []))

    @jsii.member(jsii_name="resetRetentionInDays")
    def reset_retention_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionInDays", []))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspace")
    def log_analytics_workspace(
        self,
    ) -> FirewallPolicyInsightsLogAnalyticsWorkspaceList:
        return typing.cast(FirewallPolicyInsightsLogAnalyticsWorkspaceList, jsii.get(self, "logAnalyticsWorkspace"))

    @builtins.property
    @jsii.member(jsii_name="defaultLogAnalyticsWorkspaceIdInput")
    def default_log_analytics_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultLogAnalyticsWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceInput")
    def log_analytics_workspace_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyInsightsLogAnalyticsWorkspace]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyInsightsLogAnalyticsWorkspace]]], jsii.get(self, "logAnalyticsWorkspaceInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLogAnalyticsWorkspaceId")
    def default_log_analytics_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLogAnalyticsWorkspaceId"))

    @default_log_analytics_workspace_id.setter
    def default_log_analytics_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsOutputReference, "default_log_analytics_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLogAnalyticsWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsOutputReference, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FirewallPolicyInsights]:
        return typing.cast(typing.Optional[FirewallPolicyInsights], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[FirewallPolicyInsights]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyInsightsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIntrusionDetection",
    jsii_struct_bases=[],
    name_mapping={
        "mode": "mode",
        "private_ranges": "privateRanges",
        "signature_overrides": "signatureOverrides",
        "traffic_bypass": "trafficBypass",
    },
)
class FirewallPolicyIntrusionDetection:
    def __init__(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        private_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        signature_overrides: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyIntrusionDetectionSignatureOverrides", typing.Dict[str, typing.Any]]]]] = None,
        traffic_bypass: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyIntrusionDetectionTrafficBypass", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#mode FirewallPolicy#mode}.
        :param private_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#private_ranges FirewallPolicy#private_ranges}.
        :param signature_overrides: signature_overrides block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#signature_overrides FirewallPolicy#signature_overrides}
        :param traffic_bypass: traffic_bypass block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#traffic_bypass FirewallPolicy#traffic_bypass}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetection.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument private_ranges", value=private_ranges, expected_type=type_hints["private_ranges"])
            check_type(argname="argument signature_overrides", value=signature_overrides, expected_type=type_hints["signature_overrides"])
            check_type(argname="argument traffic_bypass", value=traffic_bypass, expected_type=type_hints["traffic_bypass"])
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if private_ranges is not None:
            self._values["private_ranges"] = private_ranges
        if signature_overrides is not None:
            self._values["signature_overrides"] = signature_overrides
        if traffic_bypass is not None:
            self._values["traffic_bypass"] = traffic_bypass

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#mode FirewallPolicy#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#private_ranges FirewallPolicy#private_ranges}.'''
        result = self._values.get("private_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def signature_overrides(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyIntrusionDetectionSignatureOverrides"]]]:
        '''signature_overrides block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#signature_overrides FirewallPolicy#signature_overrides}
        '''
        result = self._values.get("signature_overrides")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyIntrusionDetectionSignatureOverrides"]]], result)

    @builtins.property
    def traffic_bypass(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyIntrusionDetectionTrafficBypass"]]]:
        '''traffic_bypass block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#traffic_bypass FirewallPolicy#traffic_bypass}
        '''
        result = self._values.get("traffic_bypass")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyIntrusionDetectionTrafficBypass"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyIntrusionDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyIntrusionDetectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIntrusionDetectionOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSignatureOverrides")
    def put_signature_overrides(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyIntrusionDetectionSignatureOverrides", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionOutputReference.put_signature_overrides)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSignatureOverrides", [value]))

    @jsii.member(jsii_name="putTrafficBypass")
    def put_traffic_bypass(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FirewallPolicyIntrusionDetectionTrafficBypass", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionOutputReference.put_traffic_bypass)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrafficBypass", [value]))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetPrivateRanges")
    def reset_private_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateRanges", []))

    @jsii.member(jsii_name="resetSignatureOverrides")
    def reset_signature_overrides(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureOverrides", []))

    @jsii.member(jsii_name="resetTrafficBypass")
    def reset_traffic_bypass(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficBypass", []))

    @builtins.property
    @jsii.member(jsii_name="signatureOverrides")
    def signature_overrides(
        self,
    ) -> "FirewallPolicyIntrusionDetectionSignatureOverridesList":
        return typing.cast("FirewallPolicyIntrusionDetectionSignatureOverridesList", jsii.get(self, "signatureOverrides"))

    @builtins.property
    @jsii.member(jsii_name="trafficBypass")
    def traffic_bypass(self) -> "FirewallPolicyIntrusionDetectionTrafficBypassList":
        return typing.cast("FirewallPolicyIntrusionDetectionTrafficBypassList", jsii.get(self, "trafficBypass"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="privateRangesInput")
    def private_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privateRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureOverridesInput")
    def signature_overrides_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyIntrusionDetectionSignatureOverrides"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyIntrusionDetectionSignatureOverrides"]]], jsii.get(self, "signatureOverridesInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficBypassInput")
    def traffic_bypass_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyIntrusionDetectionTrafficBypass"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FirewallPolicyIntrusionDetectionTrafficBypass"]]], jsii.get(self, "trafficBypassInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="privateRanges")
    def private_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateRanges"))

    @private_ranges.setter
    def private_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionOutputReference, "private_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateRanges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FirewallPolicyIntrusionDetection]:
        return typing.cast(typing.Optional[FirewallPolicyIntrusionDetection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FirewallPolicyIntrusionDetection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIntrusionDetectionSignatureOverrides",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "state": "state"},
)
class FirewallPolicyIntrusionDetectionSignatureOverrides:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#id FirewallPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#state FirewallPolicy#state}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionSignatureOverrides.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if state is not None:
            self._values["state"] = state

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#id FirewallPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#state FirewallPolicy#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyIntrusionDetectionSignatureOverrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyIntrusionDetectionSignatureOverridesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIntrusionDetectionSignatureOverridesList",
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
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionSignatureOverridesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionSignatureOverridesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionSignatureOverridesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionSignatureOverridesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionSignatureOverridesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyIntrusionDetectionSignatureOverrides]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyIntrusionDetectionSignatureOverrides]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyIntrusionDetectionSignatureOverrides]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionSignatureOverridesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyIntrusionDetectionSignatureOverrides, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyIntrusionDetectionSignatureOverrides, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyIntrusionDetectionSignatureOverrides, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIntrusionDetectionTrafficBypass",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "protocol": "protocol",
        "description": "description",
        "destination_addresses": "destinationAddresses",
        "destination_ip_groups": "destinationIpGroups",
        "destination_ports": "destinationPorts",
        "source_addresses": "sourceAddresses",
        "source_ip_groups": "sourceIpGroups",
    },
)
class FirewallPolicyIntrusionDetectionTrafficBypass:
    def __init__(
        self,
        *,
        name: builtins.str,
        protocol: builtins.str,
        description: typing.Optional[builtins.str] = None,
        destination_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_ip_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_ip_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#name FirewallPolicy#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#protocol FirewallPolicy#protocol}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#description FirewallPolicy#description}.
        :param destination_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#destination_addresses FirewallPolicy#destination_addresses}.
        :param destination_ip_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#destination_ip_groups FirewallPolicy#destination_ip_groups}.
        :param destination_ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#destination_ports FirewallPolicy#destination_ports}.
        :param source_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#source_addresses FirewallPolicy#source_addresses}.
        :param source_ip_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#source_ip_groups FirewallPolicy#source_ip_groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionTrafficBypass.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument destination_addresses", value=destination_addresses, expected_type=type_hints["destination_addresses"])
            check_type(argname="argument destination_ip_groups", value=destination_ip_groups, expected_type=type_hints["destination_ip_groups"])
            check_type(argname="argument destination_ports", value=destination_ports, expected_type=type_hints["destination_ports"])
            check_type(argname="argument source_addresses", value=source_addresses, expected_type=type_hints["source_addresses"])
            check_type(argname="argument source_ip_groups", value=source_ip_groups, expected_type=type_hints["source_ip_groups"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "protocol": protocol,
        }
        if description is not None:
            self._values["description"] = description
        if destination_addresses is not None:
            self._values["destination_addresses"] = destination_addresses
        if destination_ip_groups is not None:
            self._values["destination_ip_groups"] = destination_ip_groups
        if destination_ports is not None:
            self._values["destination_ports"] = destination_ports
        if source_addresses is not None:
            self._values["source_addresses"] = source_addresses
        if source_ip_groups is not None:
            self._values["source_ip_groups"] = source_ip_groups

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#name FirewallPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#protocol FirewallPolicy#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#description FirewallPolicy#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#destination_addresses FirewallPolicy#destination_addresses}.'''
        result = self._values.get("destination_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_ip_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#destination_ip_groups FirewallPolicy#destination_ip_groups}.'''
        result = self._values.get("destination_ip_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#destination_ports FirewallPolicy#destination_ports}.'''
        result = self._values.get("destination_ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#source_addresses FirewallPolicy#source_addresses}.'''
        result = self._values.get("source_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_ip_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#source_ip_groups FirewallPolicy#source_ip_groups}.'''
        result = self._values.get("source_ip_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyIntrusionDetectionTrafficBypass(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyIntrusionDetectionTrafficBypassList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIntrusionDetectionTrafficBypassList",
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
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionTrafficBypassList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FirewallPolicyIntrusionDetectionTrafficBypassOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionTrafficBypassList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FirewallPolicyIntrusionDetectionTrafficBypassOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyIntrusionDetectionTrafficBypass]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyIntrusionDetectionTrafficBypass]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FirewallPolicyIntrusionDetectionTrafficBypass]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FirewallPolicyIntrusionDetectionTrafficBypassOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyIntrusionDetectionTrafficBypassOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDestinationAddresses")
    def reset_destination_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddresses", []))

    @jsii.member(jsii_name="resetDestinationIpGroups")
    def reset_destination_ip_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationIpGroups", []))

    @jsii.member(jsii_name="resetDestinationPorts")
    def reset_destination_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPorts", []))

    @jsii.member(jsii_name="resetSourceAddresses")
    def reset_source_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddresses", []))

    @jsii.member(jsii_name="resetSourceIpGroups")
    def reset_source_ip_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpGroups", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressesInput")
    def destination_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationIpGroupsInput")
    def destination_ip_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationIpGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortsInput")
    def destination_ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressesInput")
    def source_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpGroupsInput")
    def source_ip_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIpGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddresses"))

    @destination_addresses.setter
    def destination_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "destination_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="destinationIpGroups")
    def destination_ip_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationIpGroups"))

    @destination_ip_groups.setter
    def destination_ip_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "destination_ip_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationIpGroups", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPorts")
    def destination_ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationPorts"))

    @destination_ports.setter
    def destination_ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "destination_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPorts", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @source_addresses.setter
    def source_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "source_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpGroups")
    def source_ip_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceIpGroups"))

    @source_ip_groups.setter
    def source_ip_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "source_ip_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyIntrusionDetectionTrafficBypass, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyIntrusionDetectionTrafficBypass, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyIntrusionDetectionTrafficBypass, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyIntrusionDetectionTrafficBypassOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyThreatIntelligenceAllowlist",
    jsii_struct_bases=[],
    name_mapping={"fqdns": "fqdns", "ip_addresses": "ipAddresses"},
)
class FirewallPolicyThreatIntelligenceAllowlist:
    def __init__(
        self,
        *,
        fqdns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fqdns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#fqdns FirewallPolicy#fqdns}.
        :param ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#ip_addresses FirewallPolicy#ip_addresses}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyThreatIntelligenceAllowlist.__init__)
            check_type(argname="argument fqdns", value=fqdns, expected_type=type_hints["fqdns"])
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=type_hints["ip_addresses"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fqdns is not None:
            self._values["fqdns"] = fqdns
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses

    @builtins.property
    def fqdns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#fqdns FirewallPolicy#fqdns}.'''
        result = self._values.get("fqdns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#ip_addresses FirewallPolicy#ip_addresses}.'''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyThreatIntelligenceAllowlist(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyThreatIntelligenceAllowlistOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyThreatIntelligenceAllowlistOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyThreatIntelligenceAllowlistOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFqdns")
    def reset_fqdns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFqdns", []))

    @jsii.member(jsii_name="resetIpAddresses")
    def reset_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddresses", []))

    @builtins.property
    @jsii.member(jsii_name="fqdnsInput")
    def fqdns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fqdnsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressesInput")
    def ip_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="fqdns")
    def fqdns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fqdns"))

    @fqdns.setter
    def fqdns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyThreatIntelligenceAllowlistOutputReference, "fqdns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fqdns", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyThreatIntelligenceAllowlistOutputReference, "ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FirewallPolicyThreatIntelligenceAllowlist]:
        return typing.cast(typing.Optional[FirewallPolicyThreatIntelligenceAllowlist], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FirewallPolicyThreatIntelligenceAllowlist],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyThreatIntelligenceAllowlistOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class FirewallPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#create FirewallPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#delete FirewallPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#read FirewallPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#update FirewallPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#create FirewallPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#delete FirewallPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#read FirewallPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#update FirewallPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(FirewallPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FirewallPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FirewallPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FirewallPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"key_vault_secret_id": "keyVaultSecretId", "name": "name"},
)
class FirewallPolicyTlsCertificate:
    def __init__(
        self,
        *,
        key_vault_secret_id: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param key_vault_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#key_vault_secret_id FirewallPolicy#key_vault_secret_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#name FirewallPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FirewallPolicyTlsCertificate.__init__)
            check_type(argname="argument key_vault_secret_id", value=key_vault_secret_id, expected_type=type_hints["key_vault_secret_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_vault_secret_id": key_vault_secret_id,
            "name": name,
        }

    @builtins.property
    def key_vault_secret_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#key_vault_secret_id FirewallPolicy#key_vault_secret_id}.'''
        result = self._values.get("key_vault_secret_id")
        assert result is not None, "Required property 'key_vault_secret_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/firewall_policy#name FirewallPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallPolicyTlsCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.firewallPolicy.FirewallPolicyTlsCertificateOutputReference",
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
            type_hints = typing.get_type_hints(FirewallPolicyTlsCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretIdInput")
    def key_vault_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultSecretId")
    def key_vault_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultSecretId"))

    @key_vault_secret_id.setter
    def key_vault_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyTlsCertificateOutputReference, "key_vault_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyTlsCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FirewallPolicyTlsCertificate]:
        return typing.cast(typing.Optional[FirewallPolicyTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FirewallPolicyTlsCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FirewallPolicyTlsCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FirewallPolicy",
    "FirewallPolicyConfig",
    "FirewallPolicyDns",
    "FirewallPolicyDnsOutputReference",
    "FirewallPolicyIdentity",
    "FirewallPolicyIdentityOutputReference",
    "FirewallPolicyInsights",
    "FirewallPolicyInsightsLogAnalyticsWorkspace",
    "FirewallPolicyInsightsLogAnalyticsWorkspaceList",
    "FirewallPolicyInsightsLogAnalyticsWorkspaceOutputReference",
    "FirewallPolicyInsightsOutputReference",
    "FirewallPolicyIntrusionDetection",
    "FirewallPolicyIntrusionDetectionOutputReference",
    "FirewallPolicyIntrusionDetectionSignatureOverrides",
    "FirewallPolicyIntrusionDetectionSignatureOverridesList",
    "FirewallPolicyIntrusionDetectionSignatureOverridesOutputReference",
    "FirewallPolicyIntrusionDetectionTrafficBypass",
    "FirewallPolicyIntrusionDetectionTrafficBypassList",
    "FirewallPolicyIntrusionDetectionTrafficBypassOutputReference",
    "FirewallPolicyThreatIntelligenceAllowlist",
    "FirewallPolicyThreatIntelligenceAllowlistOutputReference",
    "FirewallPolicyTimeouts",
    "FirewallPolicyTimeoutsOutputReference",
    "FirewallPolicyTlsCertificate",
    "FirewallPolicyTlsCertificateOutputReference",
]

publication.publish()
