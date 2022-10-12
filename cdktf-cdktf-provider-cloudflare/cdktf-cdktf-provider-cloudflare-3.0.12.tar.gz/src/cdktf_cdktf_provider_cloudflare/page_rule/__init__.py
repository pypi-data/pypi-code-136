'''
# `cloudflare_page_rule`

Refer to the Terraform Registory for docs: [`cloudflare_page_rule`](https://www.terraform.io/docs/providers/cloudflare/r/page_rule).
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


class PageRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule cloudflare_page_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        actions: typing.Union["PageRuleActions", typing.Dict[str, typing.Any]],
        target: builtins.str,
        zone_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule cloudflare_page_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#actions PageRule#actions}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#target PageRule#target}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#zone_id PageRule#zone_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#id PageRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#priority PageRule#priority}
        :param status: Defaults to ``active``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#status PageRule#status}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PageRuleConfig(
            actions=actions,
            target=target,
            zone_id=zone_id,
            id=id,
            priority=priority,
            status=status,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        *,
        always_use_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        automatic_https_rewrites: typing.Optional[builtins.str] = None,
        browser_cache_ttl: typing.Optional[builtins.str] = None,
        browser_check: typing.Optional[builtins.str] = None,
        bypass_cache_on_cookie: typing.Optional[builtins.str] = None,
        cache_by_device_type: typing.Optional[builtins.str] = None,
        cache_deception_armor: typing.Optional[builtins.str] = None,
        cache_key_fields: typing.Optional[typing.Union["PageRuleActionsCacheKeyFields", typing.Dict[str, typing.Any]]] = None,
        cache_level: typing.Optional[builtins.str] = None,
        cache_on_cookie: typing.Optional[builtins.str] = None,
        cache_ttl_by_status: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PageRuleActionsCacheTtlByStatus", typing.Dict[str, typing.Any]]]]] = None,
        disable_apps: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_performance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_railgun: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_security: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_zaraz: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        edge_cache_ttl: typing.Optional[jsii.Number] = None,
        email_obfuscation: typing.Optional[builtins.str] = None,
        explicit_cache_control: typing.Optional[builtins.str] = None,
        forwarding_url: typing.Optional[typing.Union["PageRuleActionsForwardingUrl", typing.Dict[str, typing.Any]]] = None,
        host_header_override: typing.Optional[builtins.str] = None,
        ip_geolocation: typing.Optional[builtins.str] = None,
        minify: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PageRuleActionsMinify", typing.Dict[str, typing.Any]]]]] = None,
        mirage: typing.Optional[builtins.str] = None,
        opportunistic_encryption: typing.Optional[builtins.str] = None,
        origin_error_page_pass_thru: typing.Optional[builtins.str] = None,
        polish: typing.Optional[builtins.str] = None,
        resolve_override: typing.Optional[builtins.str] = None,
        respect_strong_etag: typing.Optional[builtins.str] = None,
        response_buffering: typing.Optional[builtins.str] = None,
        rocket_loader: typing.Optional[builtins.str] = None,
        security_level: typing.Optional[builtins.str] = None,
        server_side_exclude: typing.Optional[builtins.str] = None,
        sort_query_string_for_cache: typing.Optional[builtins.str] = None,
        ssl: typing.Optional[builtins.str] = None,
        true_client_ip_header: typing.Optional[builtins.str] = None,
        waf: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param always_use_https: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#always_use_https PageRule#always_use_https}
        :param automatic_https_rewrites: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#automatic_https_rewrites PageRule#automatic_https_rewrites}.
        :param browser_cache_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#browser_cache_ttl PageRule#browser_cache_ttl}.
        :param browser_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#browser_check PageRule#browser_check}.
        :param bypass_cache_on_cookie: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#bypass_cache_on_cookie PageRule#bypass_cache_on_cookie}.
        :param cache_by_device_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_by_device_type PageRule#cache_by_device_type}.
        :param cache_deception_armor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_deception_armor PageRule#cache_deception_armor}.
        :param cache_key_fields: cache_key_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_key_fields PageRule#cache_key_fields}
        :param cache_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_level PageRule#cache_level}.
        :param cache_on_cookie: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_on_cookie PageRule#cache_on_cookie}.
        :param cache_ttl_by_status: cache_ttl_by_status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_ttl_by_status PageRule#cache_ttl_by_status}
        :param disable_apps: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_apps PageRule#disable_apps}
        :param disable_performance: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_performance PageRule#disable_performance}
        :param disable_railgun: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_railgun PageRule#disable_railgun}
        :param disable_security: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_security PageRule#disable_security}
        :param disable_zaraz: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_zaraz PageRule#disable_zaraz}
        :param edge_cache_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#edge_cache_ttl PageRule#edge_cache_ttl}.
        :param email_obfuscation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#email_obfuscation PageRule#email_obfuscation}.
        :param explicit_cache_control: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#explicit_cache_control PageRule#explicit_cache_control}.
        :param forwarding_url: forwarding_url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#forwarding_url PageRule#forwarding_url}
        :param host_header_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#host_header_override PageRule#host_header_override}.
        :param ip_geolocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ip_geolocation PageRule#ip_geolocation}.
        :param minify: minify block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#minify PageRule#minify}
        :param mirage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#mirage PageRule#mirage}.
        :param opportunistic_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#opportunistic_encryption PageRule#opportunistic_encryption}.
        :param origin_error_page_pass_thru: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#origin_error_page_pass_thru PageRule#origin_error_page_pass_thru}.
        :param polish: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#polish PageRule#polish}.
        :param resolve_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#resolve_override PageRule#resolve_override}.
        :param respect_strong_etag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#respect_strong_etag PageRule#respect_strong_etag}.
        :param response_buffering: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#response_buffering PageRule#response_buffering}.
        :param rocket_loader: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#rocket_loader PageRule#rocket_loader}.
        :param security_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#security_level PageRule#security_level}.
        :param server_side_exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#server_side_exclude PageRule#server_side_exclude}.
        :param sort_query_string_for_cache: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#sort_query_string_for_cache PageRule#sort_query_string_for_cache}.
        :param ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ssl PageRule#ssl}.
        :param true_client_ip_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#true_client_ip_header PageRule#true_client_ip_header}.
        :param waf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#waf PageRule#waf}.
        '''
        value = PageRuleActions(
            always_use_https=always_use_https,
            automatic_https_rewrites=automatic_https_rewrites,
            browser_cache_ttl=browser_cache_ttl,
            browser_check=browser_check,
            bypass_cache_on_cookie=bypass_cache_on_cookie,
            cache_by_device_type=cache_by_device_type,
            cache_deception_armor=cache_deception_armor,
            cache_key_fields=cache_key_fields,
            cache_level=cache_level,
            cache_on_cookie=cache_on_cookie,
            cache_ttl_by_status=cache_ttl_by_status,
            disable_apps=disable_apps,
            disable_performance=disable_performance,
            disable_railgun=disable_railgun,
            disable_security=disable_security,
            disable_zaraz=disable_zaraz,
            edge_cache_ttl=edge_cache_ttl,
            email_obfuscation=email_obfuscation,
            explicit_cache_control=explicit_cache_control,
            forwarding_url=forwarding_url,
            host_header_override=host_header_override,
            ip_geolocation=ip_geolocation,
            minify=minify,
            mirage=mirage,
            opportunistic_encryption=opportunistic_encryption,
            origin_error_page_pass_thru=origin_error_page_pass_thru,
            polish=polish,
            resolve_override=resolve_override,
            respect_strong_etag=respect_strong_etag,
            response_buffering=response_buffering,
            rocket_loader=rocket_loader,
            security_level=security_level,
            server_side_exclude=server_side_exclude,
            sort_query_string_for_cache=sort_query_string_for_cache,
            ssl=ssl,
            true_client_ip_header=true_client_ip_header,
            waf=waf,
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> "PageRuleActionsOutputReference":
        return typing.cast("PageRuleActionsOutputReference", jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional["PageRuleActions"]:
        return typing.cast(typing.Optional["PageRuleActions"], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRule, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRule, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRule, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRule, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActions",
    jsii_struct_bases=[],
    name_mapping={
        "always_use_https": "alwaysUseHttps",
        "automatic_https_rewrites": "automaticHttpsRewrites",
        "browser_cache_ttl": "browserCacheTtl",
        "browser_check": "browserCheck",
        "bypass_cache_on_cookie": "bypassCacheOnCookie",
        "cache_by_device_type": "cacheByDeviceType",
        "cache_deception_armor": "cacheDeceptionArmor",
        "cache_key_fields": "cacheKeyFields",
        "cache_level": "cacheLevel",
        "cache_on_cookie": "cacheOnCookie",
        "cache_ttl_by_status": "cacheTtlByStatus",
        "disable_apps": "disableApps",
        "disable_performance": "disablePerformance",
        "disable_railgun": "disableRailgun",
        "disable_security": "disableSecurity",
        "disable_zaraz": "disableZaraz",
        "edge_cache_ttl": "edgeCacheTtl",
        "email_obfuscation": "emailObfuscation",
        "explicit_cache_control": "explicitCacheControl",
        "forwarding_url": "forwardingUrl",
        "host_header_override": "hostHeaderOverride",
        "ip_geolocation": "ipGeolocation",
        "minify": "minify",
        "mirage": "mirage",
        "opportunistic_encryption": "opportunisticEncryption",
        "origin_error_page_pass_thru": "originErrorPagePassThru",
        "polish": "polish",
        "resolve_override": "resolveOverride",
        "respect_strong_etag": "respectStrongEtag",
        "response_buffering": "responseBuffering",
        "rocket_loader": "rocketLoader",
        "security_level": "securityLevel",
        "server_side_exclude": "serverSideExclude",
        "sort_query_string_for_cache": "sortQueryStringForCache",
        "ssl": "ssl",
        "true_client_ip_header": "trueClientIpHeader",
        "waf": "waf",
    },
)
class PageRuleActions:
    def __init__(
        self,
        *,
        always_use_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        automatic_https_rewrites: typing.Optional[builtins.str] = None,
        browser_cache_ttl: typing.Optional[builtins.str] = None,
        browser_check: typing.Optional[builtins.str] = None,
        bypass_cache_on_cookie: typing.Optional[builtins.str] = None,
        cache_by_device_type: typing.Optional[builtins.str] = None,
        cache_deception_armor: typing.Optional[builtins.str] = None,
        cache_key_fields: typing.Optional[typing.Union["PageRuleActionsCacheKeyFields", typing.Dict[str, typing.Any]]] = None,
        cache_level: typing.Optional[builtins.str] = None,
        cache_on_cookie: typing.Optional[builtins.str] = None,
        cache_ttl_by_status: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PageRuleActionsCacheTtlByStatus", typing.Dict[str, typing.Any]]]]] = None,
        disable_apps: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_performance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_railgun: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_security: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_zaraz: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        edge_cache_ttl: typing.Optional[jsii.Number] = None,
        email_obfuscation: typing.Optional[builtins.str] = None,
        explicit_cache_control: typing.Optional[builtins.str] = None,
        forwarding_url: typing.Optional[typing.Union["PageRuleActionsForwardingUrl", typing.Dict[str, typing.Any]]] = None,
        host_header_override: typing.Optional[builtins.str] = None,
        ip_geolocation: typing.Optional[builtins.str] = None,
        minify: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PageRuleActionsMinify", typing.Dict[str, typing.Any]]]]] = None,
        mirage: typing.Optional[builtins.str] = None,
        opportunistic_encryption: typing.Optional[builtins.str] = None,
        origin_error_page_pass_thru: typing.Optional[builtins.str] = None,
        polish: typing.Optional[builtins.str] = None,
        resolve_override: typing.Optional[builtins.str] = None,
        respect_strong_etag: typing.Optional[builtins.str] = None,
        response_buffering: typing.Optional[builtins.str] = None,
        rocket_loader: typing.Optional[builtins.str] = None,
        security_level: typing.Optional[builtins.str] = None,
        server_side_exclude: typing.Optional[builtins.str] = None,
        sort_query_string_for_cache: typing.Optional[builtins.str] = None,
        ssl: typing.Optional[builtins.str] = None,
        true_client_ip_header: typing.Optional[builtins.str] = None,
        waf: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param always_use_https: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#always_use_https PageRule#always_use_https}
        :param automatic_https_rewrites: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#automatic_https_rewrites PageRule#automatic_https_rewrites}.
        :param browser_cache_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#browser_cache_ttl PageRule#browser_cache_ttl}.
        :param browser_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#browser_check PageRule#browser_check}.
        :param bypass_cache_on_cookie: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#bypass_cache_on_cookie PageRule#bypass_cache_on_cookie}.
        :param cache_by_device_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_by_device_type PageRule#cache_by_device_type}.
        :param cache_deception_armor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_deception_armor PageRule#cache_deception_armor}.
        :param cache_key_fields: cache_key_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_key_fields PageRule#cache_key_fields}
        :param cache_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_level PageRule#cache_level}.
        :param cache_on_cookie: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_on_cookie PageRule#cache_on_cookie}.
        :param cache_ttl_by_status: cache_ttl_by_status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_ttl_by_status PageRule#cache_ttl_by_status}
        :param disable_apps: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_apps PageRule#disable_apps}
        :param disable_performance: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_performance PageRule#disable_performance}
        :param disable_railgun: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_railgun PageRule#disable_railgun}
        :param disable_security: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_security PageRule#disable_security}
        :param disable_zaraz: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_zaraz PageRule#disable_zaraz}
        :param edge_cache_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#edge_cache_ttl PageRule#edge_cache_ttl}.
        :param email_obfuscation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#email_obfuscation PageRule#email_obfuscation}.
        :param explicit_cache_control: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#explicit_cache_control PageRule#explicit_cache_control}.
        :param forwarding_url: forwarding_url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#forwarding_url PageRule#forwarding_url}
        :param host_header_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#host_header_override PageRule#host_header_override}.
        :param ip_geolocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ip_geolocation PageRule#ip_geolocation}.
        :param minify: minify block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#minify PageRule#minify}
        :param mirage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#mirage PageRule#mirage}.
        :param opportunistic_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#opportunistic_encryption PageRule#opportunistic_encryption}.
        :param origin_error_page_pass_thru: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#origin_error_page_pass_thru PageRule#origin_error_page_pass_thru}.
        :param polish: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#polish PageRule#polish}.
        :param resolve_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#resolve_override PageRule#resolve_override}.
        :param respect_strong_etag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#respect_strong_etag PageRule#respect_strong_etag}.
        :param response_buffering: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#response_buffering PageRule#response_buffering}.
        :param rocket_loader: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#rocket_loader PageRule#rocket_loader}.
        :param security_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#security_level PageRule#security_level}.
        :param server_side_exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#server_side_exclude PageRule#server_side_exclude}.
        :param sort_query_string_for_cache: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#sort_query_string_for_cache PageRule#sort_query_string_for_cache}.
        :param ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ssl PageRule#ssl}.
        :param true_client_ip_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#true_client_ip_header PageRule#true_client_ip_header}.
        :param waf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#waf PageRule#waf}.
        '''
        if isinstance(cache_key_fields, dict):
            cache_key_fields = PageRuleActionsCacheKeyFields(**cache_key_fields)
        if isinstance(forwarding_url, dict):
            forwarding_url = PageRuleActionsForwardingUrl(**forwarding_url)
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActions.__init__)
            check_type(argname="argument always_use_https", value=always_use_https, expected_type=type_hints["always_use_https"])
            check_type(argname="argument automatic_https_rewrites", value=automatic_https_rewrites, expected_type=type_hints["automatic_https_rewrites"])
            check_type(argname="argument browser_cache_ttl", value=browser_cache_ttl, expected_type=type_hints["browser_cache_ttl"])
            check_type(argname="argument browser_check", value=browser_check, expected_type=type_hints["browser_check"])
            check_type(argname="argument bypass_cache_on_cookie", value=bypass_cache_on_cookie, expected_type=type_hints["bypass_cache_on_cookie"])
            check_type(argname="argument cache_by_device_type", value=cache_by_device_type, expected_type=type_hints["cache_by_device_type"])
            check_type(argname="argument cache_deception_armor", value=cache_deception_armor, expected_type=type_hints["cache_deception_armor"])
            check_type(argname="argument cache_key_fields", value=cache_key_fields, expected_type=type_hints["cache_key_fields"])
            check_type(argname="argument cache_level", value=cache_level, expected_type=type_hints["cache_level"])
            check_type(argname="argument cache_on_cookie", value=cache_on_cookie, expected_type=type_hints["cache_on_cookie"])
            check_type(argname="argument cache_ttl_by_status", value=cache_ttl_by_status, expected_type=type_hints["cache_ttl_by_status"])
            check_type(argname="argument disable_apps", value=disable_apps, expected_type=type_hints["disable_apps"])
            check_type(argname="argument disable_performance", value=disable_performance, expected_type=type_hints["disable_performance"])
            check_type(argname="argument disable_railgun", value=disable_railgun, expected_type=type_hints["disable_railgun"])
            check_type(argname="argument disable_security", value=disable_security, expected_type=type_hints["disable_security"])
            check_type(argname="argument disable_zaraz", value=disable_zaraz, expected_type=type_hints["disable_zaraz"])
            check_type(argname="argument edge_cache_ttl", value=edge_cache_ttl, expected_type=type_hints["edge_cache_ttl"])
            check_type(argname="argument email_obfuscation", value=email_obfuscation, expected_type=type_hints["email_obfuscation"])
            check_type(argname="argument explicit_cache_control", value=explicit_cache_control, expected_type=type_hints["explicit_cache_control"])
            check_type(argname="argument forwarding_url", value=forwarding_url, expected_type=type_hints["forwarding_url"])
            check_type(argname="argument host_header_override", value=host_header_override, expected_type=type_hints["host_header_override"])
            check_type(argname="argument ip_geolocation", value=ip_geolocation, expected_type=type_hints["ip_geolocation"])
            check_type(argname="argument minify", value=minify, expected_type=type_hints["minify"])
            check_type(argname="argument mirage", value=mirage, expected_type=type_hints["mirage"])
            check_type(argname="argument opportunistic_encryption", value=opportunistic_encryption, expected_type=type_hints["opportunistic_encryption"])
            check_type(argname="argument origin_error_page_pass_thru", value=origin_error_page_pass_thru, expected_type=type_hints["origin_error_page_pass_thru"])
            check_type(argname="argument polish", value=polish, expected_type=type_hints["polish"])
            check_type(argname="argument resolve_override", value=resolve_override, expected_type=type_hints["resolve_override"])
            check_type(argname="argument respect_strong_etag", value=respect_strong_etag, expected_type=type_hints["respect_strong_etag"])
            check_type(argname="argument response_buffering", value=response_buffering, expected_type=type_hints["response_buffering"])
            check_type(argname="argument rocket_loader", value=rocket_loader, expected_type=type_hints["rocket_loader"])
            check_type(argname="argument security_level", value=security_level, expected_type=type_hints["security_level"])
            check_type(argname="argument server_side_exclude", value=server_side_exclude, expected_type=type_hints["server_side_exclude"])
            check_type(argname="argument sort_query_string_for_cache", value=sort_query_string_for_cache, expected_type=type_hints["sort_query_string_for_cache"])
            check_type(argname="argument ssl", value=ssl, expected_type=type_hints["ssl"])
            check_type(argname="argument true_client_ip_header", value=true_client_ip_header, expected_type=type_hints["true_client_ip_header"])
            check_type(argname="argument waf", value=waf, expected_type=type_hints["waf"])
        self._values: typing.Dict[str, typing.Any] = {}
        if always_use_https is not None:
            self._values["always_use_https"] = always_use_https
        if automatic_https_rewrites is not None:
            self._values["automatic_https_rewrites"] = automatic_https_rewrites
        if browser_cache_ttl is not None:
            self._values["browser_cache_ttl"] = browser_cache_ttl
        if browser_check is not None:
            self._values["browser_check"] = browser_check
        if bypass_cache_on_cookie is not None:
            self._values["bypass_cache_on_cookie"] = bypass_cache_on_cookie
        if cache_by_device_type is not None:
            self._values["cache_by_device_type"] = cache_by_device_type
        if cache_deception_armor is not None:
            self._values["cache_deception_armor"] = cache_deception_armor
        if cache_key_fields is not None:
            self._values["cache_key_fields"] = cache_key_fields
        if cache_level is not None:
            self._values["cache_level"] = cache_level
        if cache_on_cookie is not None:
            self._values["cache_on_cookie"] = cache_on_cookie
        if cache_ttl_by_status is not None:
            self._values["cache_ttl_by_status"] = cache_ttl_by_status
        if disable_apps is not None:
            self._values["disable_apps"] = disable_apps
        if disable_performance is not None:
            self._values["disable_performance"] = disable_performance
        if disable_railgun is not None:
            self._values["disable_railgun"] = disable_railgun
        if disable_security is not None:
            self._values["disable_security"] = disable_security
        if disable_zaraz is not None:
            self._values["disable_zaraz"] = disable_zaraz
        if edge_cache_ttl is not None:
            self._values["edge_cache_ttl"] = edge_cache_ttl
        if email_obfuscation is not None:
            self._values["email_obfuscation"] = email_obfuscation
        if explicit_cache_control is not None:
            self._values["explicit_cache_control"] = explicit_cache_control
        if forwarding_url is not None:
            self._values["forwarding_url"] = forwarding_url
        if host_header_override is not None:
            self._values["host_header_override"] = host_header_override
        if ip_geolocation is not None:
            self._values["ip_geolocation"] = ip_geolocation
        if minify is not None:
            self._values["minify"] = minify
        if mirage is not None:
            self._values["mirage"] = mirage
        if opportunistic_encryption is not None:
            self._values["opportunistic_encryption"] = opportunistic_encryption
        if origin_error_page_pass_thru is not None:
            self._values["origin_error_page_pass_thru"] = origin_error_page_pass_thru
        if polish is not None:
            self._values["polish"] = polish
        if resolve_override is not None:
            self._values["resolve_override"] = resolve_override
        if respect_strong_etag is not None:
            self._values["respect_strong_etag"] = respect_strong_etag
        if response_buffering is not None:
            self._values["response_buffering"] = response_buffering
        if rocket_loader is not None:
            self._values["rocket_loader"] = rocket_loader
        if security_level is not None:
            self._values["security_level"] = security_level
        if server_side_exclude is not None:
            self._values["server_side_exclude"] = server_side_exclude
        if sort_query_string_for_cache is not None:
            self._values["sort_query_string_for_cache"] = sort_query_string_for_cache
        if ssl is not None:
            self._values["ssl"] = ssl
        if true_client_ip_header is not None:
            self._values["true_client_ip_header"] = true_client_ip_header
        if waf is not None:
            self._values["waf"] = waf

    @builtins.property
    def always_use_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#always_use_https PageRule#always_use_https}
        '''
        result = self._values.get("always_use_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def automatic_https_rewrites(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#automatic_https_rewrites PageRule#automatic_https_rewrites}.'''
        result = self._values.get("automatic_https_rewrites")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def browser_cache_ttl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#browser_cache_ttl PageRule#browser_cache_ttl}.'''
        result = self._values.get("browser_cache_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def browser_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#browser_check PageRule#browser_check}.'''
        result = self._values.get("browser_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bypass_cache_on_cookie(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#bypass_cache_on_cookie PageRule#bypass_cache_on_cookie}.'''
        result = self._values.get("bypass_cache_on_cookie")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_by_device_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_by_device_type PageRule#cache_by_device_type}.'''
        result = self._values.get("cache_by_device_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_deception_armor(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_deception_armor PageRule#cache_deception_armor}.'''
        result = self._values.get("cache_deception_armor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_key_fields(self) -> typing.Optional["PageRuleActionsCacheKeyFields"]:
        '''cache_key_fields block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_key_fields PageRule#cache_key_fields}
        '''
        result = self._values.get("cache_key_fields")
        return typing.cast(typing.Optional["PageRuleActionsCacheKeyFields"], result)

    @builtins.property
    def cache_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_level PageRule#cache_level}.'''
        result = self._values.get("cache_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_on_cookie(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_on_cookie PageRule#cache_on_cookie}.'''
        result = self._values.get("cache_on_cookie")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_ttl_by_status(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PageRuleActionsCacheTtlByStatus"]]]:
        '''cache_ttl_by_status block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cache_ttl_by_status PageRule#cache_ttl_by_status}
        '''
        result = self._values.get("cache_ttl_by_status")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PageRuleActionsCacheTtlByStatus"]]], result)

    @builtins.property
    def disable_apps(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_apps PageRule#disable_apps}
        '''
        result = self._values.get("disable_apps")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_performance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_performance PageRule#disable_performance}
        '''
        result = self._values.get("disable_performance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_railgun(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_railgun PageRule#disable_railgun}
        '''
        result = self._values.get("disable_railgun")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_security PageRule#disable_security}
        '''
        result = self._values.get("disable_security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_zaraz(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#disable_zaraz PageRule#disable_zaraz}
        '''
        result = self._values.get("disable_zaraz")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def edge_cache_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#edge_cache_ttl PageRule#edge_cache_ttl}.'''
        result = self._values.get("edge_cache_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def email_obfuscation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#email_obfuscation PageRule#email_obfuscation}.'''
        result = self._values.get("email_obfuscation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def explicit_cache_control(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#explicit_cache_control PageRule#explicit_cache_control}.'''
        result = self._values.get("explicit_cache_control")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forwarding_url(self) -> typing.Optional["PageRuleActionsForwardingUrl"]:
        '''forwarding_url block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#forwarding_url PageRule#forwarding_url}
        '''
        result = self._values.get("forwarding_url")
        return typing.cast(typing.Optional["PageRuleActionsForwardingUrl"], result)

    @builtins.property
    def host_header_override(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#host_header_override PageRule#host_header_override}.'''
        result = self._values.get("host_header_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_geolocation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ip_geolocation PageRule#ip_geolocation}.'''
        result = self._values.get("ip_geolocation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minify(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PageRuleActionsMinify"]]]:
        '''minify block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#minify PageRule#minify}
        '''
        result = self._values.get("minify")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PageRuleActionsMinify"]]], result)

    @builtins.property
    def mirage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#mirage PageRule#mirage}.'''
        result = self._values.get("mirage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opportunistic_encryption(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#opportunistic_encryption PageRule#opportunistic_encryption}.'''
        result = self._values.get("opportunistic_encryption")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_error_page_pass_thru(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#origin_error_page_pass_thru PageRule#origin_error_page_pass_thru}.'''
        result = self._values.get("origin_error_page_pass_thru")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def polish(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#polish PageRule#polish}.'''
        result = self._values.get("polish")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolve_override(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#resolve_override PageRule#resolve_override}.'''
        result = self._values.get("resolve_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def respect_strong_etag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#respect_strong_etag PageRule#respect_strong_etag}.'''
        result = self._values.get("respect_strong_etag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_buffering(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#response_buffering PageRule#response_buffering}.'''
        result = self._values.get("response_buffering")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rocket_loader(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#rocket_loader PageRule#rocket_loader}.'''
        result = self._values.get("rocket_loader")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#security_level PageRule#security_level}.'''
        result = self._values.get("security_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_exclude(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#server_side_exclude PageRule#server_side_exclude}.'''
        result = self._values.get("server_side_exclude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort_query_string_for_cache(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#sort_query_string_for_cache PageRule#sort_query_string_for_cache}.'''
        result = self._values.get("sort_query_string_for_cache")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ssl PageRule#ssl}.'''
        result = self._values.get("ssl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def true_client_ip_header(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#true_client_ip_header PageRule#true_client_ip_header}.'''
        result = self._values.get("true_client_ip_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def waf(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#waf PageRule#waf}.'''
        result = self._values.get("waf")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFields",
    jsii_struct_bases=[],
    name_mapping={
        "cookie": "cookie",
        "header": "header",
        "host": "host",
        "query_string": "queryString",
        "user": "user",
    },
)
class PageRuleActionsCacheKeyFields:
    def __init__(
        self,
        *,
        cookie: typing.Union["PageRuleActionsCacheKeyFieldsCookie", typing.Dict[str, typing.Any]],
        header: typing.Union["PageRuleActionsCacheKeyFieldsHeader", typing.Dict[str, typing.Any]],
        host: typing.Union["PageRuleActionsCacheKeyFieldsHost", typing.Dict[str, typing.Any]],
        query_string: typing.Union["PageRuleActionsCacheKeyFieldsQueryString", typing.Dict[str, typing.Any]],
        user: typing.Union["PageRuleActionsCacheKeyFieldsUser", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param cookie: cookie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cookie PageRule#cookie}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#header PageRule#header}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#host PageRule#host}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#query_string PageRule#query_string}
        :param user: user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#user PageRule#user}
        '''
        if isinstance(cookie, dict):
            cookie = PageRuleActionsCacheKeyFieldsCookie(**cookie)
        if isinstance(header, dict):
            header = PageRuleActionsCacheKeyFieldsHeader(**header)
        if isinstance(host, dict):
            host = PageRuleActionsCacheKeyFieldsHost(**host)
        if isinstance(query_string, dict):
            query_string = PageRuleActionsCacheKeyFieldsQueryString(**query_string)
        if isinstance(user, dict):
            user = PageRuleActionsCacheKeyFieldsUser(**user)
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFields.__init__)
            check_type(argname="argument cookie", value=cookie, expected_type=type_hints["cookie"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[str, typing.Any] = {
            "cookie": cookie,
            "header": header,
            "host": host,
            "query_string": query_string,
            "user": user,
        }

    @builtins.property
    def cookie(self) -> "PageRuleActionsCacheKeyFieldsCookie":
        '''cookie block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cookie PageRule#cookie}
        '''
        result = self._values.get("cookie")
        assert result is not None, "Required property 'cookie' is missing"
        return typing.cast("PageRuleActionsCacheKeyFieldsCookie", result)

    @builtins.property
    def header(self) -> "PageRuleActionsCacheKeyFieldsHeader":
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#header PageRule#header}
        '''
        result = self._values.get("header")
        assert result is not None, "Required property 'header' is missing"
        return typing.cast("PageRuleActionsCacheKeyFieldsHeader", result)

    @builtins.property
    def host(self) -> "PageRuleActionsCacheKeyFieldsHost":
        '''host block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#host PageRule#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast("PageRuleActionsCacheKeyFieldsHost", result)

    @builtins.property
    def query_string(self) -> "PageRuleActionsCacheKeyFieldsQueryString":
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#query_string PageRule#query_string}
        '''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast("PageRuleActionsCacheKeyFieldsQueryString", result)

    @builtins.property
    def user(self) -> "PageRuleActionsCacheKeyFieldsUser":
        '''user block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#user PageRule#user}
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast("PageRuleActionsCacheKeyFieldsUser", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsCacheKeyFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsCookie",
    jsii_struct_bases=[],
    name_mapping={"check_presence": "checkPresence", "include": "include"},
)
class PageRuleActionsCacheKeyFieldsCookie:
    def __init__(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#check_presence PageRule#check_presence}.
        :param include: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsCookie.__init__)
            check_type(argname="argument check_presence", value=check_presence, expected_type=type_hints["check_presence"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[str, typing.Any] = {}
        if check_presence is not None:
            self._values["check_presence"] = check_presence
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def check_presence(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#check_presence PageRule#check_presence}.'''
        result = self._values.get("check_presence")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.'''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsCacheKeyFieldsCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PageRuleActionsCacheKeyFieldsCookieOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsCookieOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsCookieOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckPresence")
    def reset_check_presence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckPresence", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="checkPresenceInput")
    def check_presence_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "checkPresenceInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="checkPresence")
    def check_presence(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "checkPresence"))

    @check_presence.setter
    def check_presence(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsCookieOutputReference, "check_presence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkPresence", value)

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsCookieOutputReference, "include").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PageRuleActionsCacheKeyFieldsCookie]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFieldsCookie], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PageRuleActionsCacheKeyFieldsCookie],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsCookieOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsHeader",
    jsii_struct_bases=[],
    name_mapping={
        "check_presence": "checkPresence",
        "exclude": "exclude",
        "include": "include",
    },
)
class PageRuleActionsCacheKeyFieldsHeader:
    def __init__(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#check_presence PageRule#check_presence}.
        :param exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#exclude PageRule#exclude}.
        :param include: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsHeader.__init__)
            check_type(argname="argument check_presence", value=check_presence, expected_type=type_hints["check_presence"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[str, typing.Any] = {}
        if check_presence is not None:
            self._values["check_presence"] = check_presence
        if exclude is not None:
            self._values["exclude"] = exclude
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def check_presence(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#check_presence PageRule#check_presence}.'''
        result = self._values.get("check_presence")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#exclude PageRule#exclude}.'''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.'''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsCacheKeyFieldsHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PageRuleActionsCacheKeyFieldsHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsHeaderOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckPresence")
    def reset_check_presence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckPresence", []))

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="checkPresenceInput")
    def check_presence_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "checkPresenceInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="checkPresence")
    def check_presence(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "checkPresence"))

    @check_presence.setter
    def check_presence(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsHeaderOutputReference, "check_presence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkPresence", value)

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsHeaderOutputReference, "exclude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value)

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsHeaderOutputReference, "include").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PageRuleActionsCacheKeyFieldsHeader]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFieldsHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PageRuleActionsCacheKeyFieldsHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsHost",
    jsii_struct_bases=[],
    name_mapping={"resolved": "resolved"},
)
class PageRuleActionsCacheKeyFieldsHost:
    def __init__(
        self,
        *,
        resolved: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param resolved: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#resolved PageRule#resolved}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsHost.__init__)
            check_type(argname="argument resolved", value=resolved, expected_type=type_hints["resolved"])
        self._values: typing.Dict[str, typing.Any] = {}
        if resolved is not None:
            self._values["resolved"] = resolved

    @builtins.property
    def resolved(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#resolved PageRule#resolved}
        '''
        result = self._values.get("resolved")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsCacheKeyFieldsHost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PageRuleActionsCacheKeyFieldsHostOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsHostOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsHostOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResolved")
    def reset_resolved(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolved", []))

    @builtins.property
    @jsii.member(jsii_name="resolvedInput")
    def resolved_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "resolvedInput"))

    @builtins.property
    @jsii.member(jsii_name="resolved")
    def resolved(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "resolved"))

    @resolved.setter
    def resolved(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsHostOutputReference, "resolved").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolved", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PageRuleActionsCacheKeyFieldsHost]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFieldsHost], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PageRuleActionsCacheKeyFieldsHost],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsHostOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PageRuleActionsCacheKeyFieldsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCookie")
    def put_cookie(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#check_presence PageRule#check_presence}.
        :param include: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.
        '''
        value = PageRuleActionsCacheKeyFieldsCookie(
            check_presence=check_presence, include=include
        )

        return typing.cast(None, jsii.invoke(self, "putCookie", [value]))

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#check_presence PageRule#check_presence}.
        :param exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#exclude PageRule#exclude}.
        :param include: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.
        '''
        value = PageRuleActionsCacheKeyFieldsHeader(
            check_presence=check_presence, exclude=exclude, include=include
        )

        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putHost")
    def put_host(
        self,
        *,
        resolved: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param resolved: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#resolved PageRule#resolved}
        '''
        value = PageRuleActionsCacheKeyFieldsHost(resolved=resolved)

        return typing.cast(None, jsii.invoke(self, "putHost", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        ignore: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#exclude PageRule#exclude}.
        :param ignore: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ignore PageRule#ignore}.
        :param include: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.
        '''
        value = PageRuleActionsCacheKeyFieldsQueryString(
            exclude=exclude, ignore=ignore, include=include
        )

        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        *,
        device_type: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        geo: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lang: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param device_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#device_type PageRule#device_type}.
        :param geo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#geo PageRule#geo}.
        :param lang: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#lang PageRule#lang}.
        '''
        value = PageRuleActionsCacheKeyFieldsUser(
            device_type=device_type, geo=geo, lang=lang
        )

        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @builtins.property
    @jsii.member(jsii_name="cookie")
    def cookie(self) -> PageRuleActionsCacheKeyFieldsCookieOutputReference:
        return typing.cast(PageRuleActionsCacheKeyFieldsCookieOutputReference, jsii.get(self, "cookie"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> PageRuleActionsCacheKeyFieldsHeaderOutputReference:
        return typing.cast(PageRuleActionsCacheKeyFieldsHeaderOutputReference, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> PageRuleActionsCacheKeyFieldsHostOutputReference:
        return typing.cast(PageRuleActionsCacheKeyFieldsHostOutputReference, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> "PageRuleActionsCacheKeyFieldsQueryStringOutputReference":
        return typing.cast("PageRuleActionsCacheKeyFieldsQueryStringOutputReference", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "PageRuleActionsCacheKeyFieldsUserOutputReference":
        return typing.cast("PageRuleActionsCacheKeyFieldsUserOutputReference", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="cookieInput")
    def cookie_input(self) -> typing.Optional[PageRuleActionsCacheKeyFieldsCookie]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFieldsCookie], jsii.get(self, "cookieInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(self) -> typing.Optional[PageRuleActionsCacheKeyFieldsHeader]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFieldsHeader], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[PageRuleActionsCacheKeyFieldsHost]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFieldsHost], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional["PageRuleActionsCacheKeyFieldsQueryString"]:
        return typing.cast(typing.Optional["PageRuleActionsCacheKeyFieldsQueryString"], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional["PageRuleActionsCacheKeyFieldsUser"]:
        return typing.cast(typing.Optional["PageRuleActionsCacheKeyFieldsUser"], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PageRuleActionsCacheKeyFields]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFields], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PageRuleActionsCacheKeyFields],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsQueryString",
    jsii_struct_bases=[],
    name_mapping={"exclude": "exclude", "ignore": "ignore", "include": "include"},
)
class PageRuleActionsCacheKeyFieldsQueryString:
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        ignore: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#exclude PageRule#exclude}.
        :param ignore: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ignore PageRule#ignore}.
        :param include: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsQueryString.__init__)
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument ignore", value=ignore, expected_type=type_hints["ignore"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if ignore is not None:
            self._values["ignore"] = ignore
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#exclude PageRule#exclude}.'''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ignore(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ignore PageRule#ignore}.'''
        result = self._values.get("ignore")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#include PageRule#include}.'''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsCacheKeyFieldsQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PageRuleActionsCacheKeyFieldsQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsQueryStringOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetIgnore")
    def reset_ignore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnore", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreInput")
    def ignore_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsQueryStringOutputReference, "exclude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value)

    @builtins.property
    @jsii.member(jsii_name="ignore")
    def ignore(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignore"))

    @ignore.setter
    def ignore(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsQueryStringOutputReference, "ignore").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignore", value)

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsQueryStringOutputReference, "include").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PageRuleActionsCacheKeyFieldsQueryString]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFieldsQueryString], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PageRuleActionsCacheKeyFieldsQueryString],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsUser",
    jsii_struct_bases=[],
    name_mapping={"device_type": "deviceType", "geo": "geo", "lang": "lang"},
)
class PageRuleActionsCacheKeyFieldsUser:
    def __init__(
        self,
        *,
        device_type: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        geo: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lang: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param device_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#device_type PageRule#device_type}.
        :param geo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#geo PageRule#geo}.
        :param lang: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#lang PageRule#lang}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsUser.__init__)
            check_type(argname="argument device_type", value=device_type, expected_type=type_hints["device_type"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument lang", value=lang, expected_type=type_hints["lang"])
        self._values: typing.Dict[str, typing.Any] = {}
        if device_type is not None:
            self._values["device_type"] = device_type
        if geo is not None:
            self._values["geo"] = geo
        if lang is not None:
            self._values["lang"] = lang

    @builtins.property
    def device_type(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#device_type PageRule#device_type}.'''
        result = self._values.get("device_type")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def geo(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#geo PageRule#geo}.'''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def lang(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#lang PageRule#lang}.'''
        result = self._values.get("lang")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsCacheKeyFieldsUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PageRuleActionsCacheKeyFieldsUserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheKeyFieldsUserOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsCacheKeyFieldsUserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeviceType")
    def reset_device_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceType", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetLang")
    def reset_lang(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLang", []))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeInput")
    def device_type_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="langInput")
    def lang_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "langInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceType")
    def device_type(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deviceType"))

    @device_type.setter
    def device_type(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsUserOutputReference, "device_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceType", value)

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "geo"))

    @geo.setter
    def geo(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsUserOutputReference, "geo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value)

    @builtins.property
    @jsii.member(jsii_name="lang")
    def lang(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "lang"))

    @lang.setter
    def lang(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsUserOutputReference, "lang").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lang", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PageRuleActionsCacheKeyFieldsUser]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFieldsUser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PageRuleActionsCacheKeyFieldsUser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheKeyFieldsUserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheTtlByStatus",
    jsii_struct_bases=[],
    name_mapping={"codes": "codes", "ttl": "ttl"},
)
class PageRuleActionsCacheTtlByStatus:
    def __init__(self, *, codes: builtins.str, ttl: jsii.Number) -> None:
        '''
        :param codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#codes PageRule#codes}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ttl PageRule#ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsCacheTtlByStatus.__init__)
            check_type(argname="argument codes", value=codes, expected_type=type_hints["codes"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "codes": codes,
            "ttl": ttl,
        }

    @builtins.property
    def codes(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#codes PageRule#codes}.'''
        result = self._values.get("codes")
        assert result is not None, "Required property 'codes' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ttl(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#ttl PageRule#ttl}.'''
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsCacheTtlByStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PageRuleActionsCacheTtlByStatusList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheTtlByStatusList",
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
            type_hints = typing.get_type_hints(PageRuleActionsCacheTtlByStatusList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PageRuleActionsCacheTtlByStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsCacheTtlByStatusList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PageRuleActionsCacheTtlByStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheTtlByStatusList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheTtlByStatusList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheTtlByStatusList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsCacheTtlByStatus]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsCacheTtlByStatus]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsCacheTtlByStatus]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheTtlByStatusList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PageRuleActionsCacheTtlByStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsCacheTtlByStatusOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsCacheTtlByStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="codesInput")
    def codes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codesInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="codes")
    def codes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codes"))

    @codes.setter
    def codes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheTtlByStatusOutputReference, "codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codes", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheTtlByStatusOutputReference, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PageRuleActionsCacheTtlByStatus, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PageRuleActionsCacheTtlByStatus, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PageRuleActionsCacheTtlByStatus, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsCacheTtlByStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsForwardingUrl",
    jsii_struct_bases=[],
    name_mapping={"status_code": "statusCode", "url": "url"},
)
class PageRuleActionsForwardingUrl:
    def __init__(self, *, status_code: jsii.Number, url: builtins.str) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#status_code PageRule#status_code}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#url PageRule#url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsForwardingUrl.__init__)
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "status_code": status_code,
            "url": url,
        }

    @builtins.property
    def status_code(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#status_code PageRule#status_code}.'''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#url PageRule#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsForwardingUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PageRuleActionsForwardingUrlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsForwardingUrlOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsForwardingUrlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsForwardingUrlOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsForwardingUrlOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PageRuleActionsForwardingUrl]:
        return typing.cast(typing.Optional[PageRuleActionsForwardingUrl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PageRuleActionsForwardingUrl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsForwardingUrlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsMinify",
    jsii_struct_bases=[],
    name_mapping={"css": "css", "html": "html", "js": "js"},
)
class PageRuleActionsMinify:
    def __init__(
        self,
        *,
        css: builtins.str,
        html: builtins.str,
        js: builtins.str,
    ) -> None:
        '''
        :param css: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#css PageRule#css}.
        :param html: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#html PageRule#html}.
        :param js: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#js PageRule#js}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsMinify.__init__)
            check_type(argname="argument css", value=css, expected_type=type_hints["css"])
            check_type(argname="argument html", value=html, expected_type=type_hints["html"])
            check_type(argname="argument js", value=js, expected_type=type_hints["js"])
        self._values: typing.Dict[str, typing.Any] = {
            "css": css,
            "html": html,
            "js": js,
        }

    @builtins.property
    def css(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#css PageRule#css}.'''
        result = self._values.get("css")
        assert result is not None, "Required property 'css' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def html(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#html PageRule#html}.'''
        result = self._values.get("html")
        assert result is not None, "Required property 'html' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def js(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#js PageRule#js}.'''
        result = self._values.get("js")
        assert result is not None, "Required property 'js' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleActionsMinify(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PageRuleActionsMinifyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsMinifyList",
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
            type_hints = typing.get_type_hints(PageRuleActionsMinifyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PageRuleActionsMinifyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsMinifyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PageRuleActionsMinifyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsMinifyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PageRuleActionsMinifyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PageRuleActionsMinifyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsMinify]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsMinify]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsMinify]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsMinifyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PageRuleActionsMinifyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsMinifyOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsMinifyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cssInput")
    def css_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cssInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlInput")
    def html_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlInput"))

    @builtins.property
    @jsii.member(jsii_name="jsInput")
    def js_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsInput"))

    @builtins.property
    @jsii.member(jsii_name="css")
    def css(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "css"))

    @css.setter
    def css(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsMinifyOutputReference, "css").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "css", value)

    @builtins.property
    @jsii.member(jsii_name="html")
    def html(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "html"))

    @html.setter
    def html(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsMinifyOutputReference, "html").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "html", value)

    @builtins.property
    @jsii.member(jsii_name="js")
    def js(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "js"))

    @js.setter
    def js(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsMinifyOutputReference, "js").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "js", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PageRuleActionsMinify, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PageRuleActionsMinify, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PageRuleActionsMinify, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsMinifyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PageRuleActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleActionsOutputReference",
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
            type_hints = typing.get_type_hints(PageRuleActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCacheKeyFields")
    def put_cache_key_fields(
        self,
        *,
        cookie: typing.Union[PageRuleActionsCacheKeyFieldsCookie, typing.Dict[str, typing.Any]],
        header: typing.Union[PageRuleActionsCacheKeyFieldsHeader, typing.Dict[str, typing.Any]],
        host: typing.Union[PageRuleActionsCacheKeyFieldsHost, typing.Dict[str, typing.Any]],
        query_string: typing.Union[PageRuleActionsCacheKeyFieldsQueryString, typing.Dict[str, typing.Any]],
        user: typing.Union[PageRuleActionsCacheKeyFieldsUser, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param cookie: cookie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#cookie PageRule#cookie}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#header PageRule#header}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#host PageRule#host}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#query_string PageRule#query_string}
        :param user: user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#user PageRule#user}
        '''
        value = PageRuleActionsCacheKeyFields(
            cookie=cookie,
            header=header,
            host=host,
            query_string=query_string,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putCacheKeyFields", [value]))

    @jsii.member(jsii_name="putCacheTtlByStatus")
    def put_cache_ttl_by_status(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PageRuleActionsCacheTtlByStatus, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsOutputReference.put_cache_ttl_by_status)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCacheTtlByStatus", [value]))

    @jsii.member(jsii_name="putForwardingUrl")
    def put_forwarding_url(
        self,
        *,
        status_code: jsii.Number,
        url: builtins.str,
    ) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#status_code PageRule#status_code}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#url PageRule#url}.
        '''
        value = PageRuleActionsForwardingUrl(status_code=status_code, url=url)

        return typing.cast(None, jsii.invoke(self, "putForwardingUrl", [value]))

    @jsii.member(jsii_name="putMinify")
    def put_minify(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PageRuleActionsMinify, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleActionsOutputReference.put_minify)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMinify", [value]))

    @jsii.member(jsii_name="resetAlwaysUseHttps")
    def reset_always_use_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlwaysUseHttps", []))

    @jsii.member(jsii_name="resetAutomaticHttpsRewrites")
    def reset_automatic_https_rewrites(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticHttpsRewrites", []))

    @jsii.member(jsii_name="resetBrowserCacheTtl")
    def reset_browser_cache_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserCacheTtl", []))

    @jsii.member(jsii_name="resetBrowserCheck")
    def reset_browser_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserCheck", []))

    @jsii.member(jsii_name="resetBypassCacheOnCookie")
    def reset_bypass_cache_on_cookie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBypassCacheOnCookie", []))

    @jsii.member(jsii_name="resetCacheByDeviceType")
    def reset_cache_by_device_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheByDeviceType", []))

    @jsii.member(jsii_name="resetCacheDeceptionArmor")
    def reset_cache_deception_armor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheDeceptionArmor", []))

    @jsii.member(jsii_name="resetCacheKeyFields")
    def reset_cache_key_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheKeyFields", []))

    @jsii.member(jsii_name="resetCacheLevel")
    def reset_cache_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheLevel", []))

    @jsii.member(jsii_name="resetCacheOnCookie")
    def reset_cache_on_cookie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheOnCookie", []))

    @jsii.member(jsii_name="resetCacheTtlByStatus")
    def reset_cache_ttl_by_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheTtlByStatus", []))

    @jsii.member(jsii_name="resetDisableApps")
    def reset_disable_apps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableApps", []))

    @jsii.member(jsii_name="resetDisablePerformance")
    def reset_disable_performance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisablePerformance", []))

    @jsii.member(jsii_name="resetDisableRailgun")
    def reset_disable_railgun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRailgun", []))

    @jsii.member(jsii_name="resetDisableSecurity")
    def reset_disable_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableSecurity", []))

    @jsii.member(jsii_name="resetDisableZaraz")
    def reset_disable_zaraz(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableZaraz", []))

    @jsii.member(jsii_name="resetEdgeCacheTtl")
    def reset_edge_cache_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeCacheTtl", []))

    @jsii.member(jsii_name="resetEmailObfuscation")
    def reset_email_obfuscation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailObfuscation", []))

    @jsii.member(jsii_name="resetExplicitCacheControl")
    def reset_explicit_cache_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExplicitCacheControl", []))

    @jsii.member(jsii_name="resetForwardingUrl")
    def reset_forwarding_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingUrl", []))

    @jsii.member(jsii_name="resetHostHeaderOverride")
    def reset_host_header_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostHeaderOverride", []))

    @jsii.member(jsii_name="resetIpGeolocation")
    def reset_ip_geolocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpGeolocation", []))

    @jsii.member(jsii_name="resetMinify")
    def reset_minify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinify", []))

    @jsii.member(jsii_name="resetMirage")
    def reset_mirage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMirage", []))

    @jsii.member(jsii_name="resetOpportunisticEncryption")
    def reset_opportunistic_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpportunisticEncryption", []))

    @jsii.member(jsii_name="resetOriginErrorPagePassThru")
    def reset_origin_error_page_pass_thru(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginErrorPagePassThru", []))

    @jsii.member(jsii_name="resetPolish")
    def reset_polish(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolish", []))

    @jsii.member(jsii_name="resetResolveOverride")
    def reset_resolve_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolveOverride", []))

    @jsii.member(jsii_name="resetRespectStrongEtag")
    def reset_respect_strong_etag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRespectStrongEtag", []))

    @jsii.member(jsii_name="resetResponseBuffering")
    def reset_response_buffering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseBuffering", []))

    @jsii.member(jsii_name="resetRocketLoader")
    def reset_rocket_loader(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRocketLoader", []))

    @jsii.member(jsii_name="resetSecurityLevel")
    def reset_security_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityLevel", []))

    @jsii.member(jsii_name="resetServerSideExclude")
    def reset_server_side_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideExclude", []))

    @jsii.member(jsii_name="resetSortQueryStringForCache")
    def reset_sort_query_string_for_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortQueryStringForCache", []))

    @jsii.member(jsii_name="resetSsl")
    def reset_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsl", []))

    @jsii.member(jsii_name="resetTrueClientIpHeader")
    def reset_true_client_ip_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrueClientIpHeader", []))

    @jsii.member(jsii_name="resetWaf")
    def reset_waf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaf", []))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyFields")
    def cache_key_fields(self) -> PageRuleActionsCacheKeyFieldsOutputReference:
        return typing.cast(PageRuleActionsCacheKeyFieldsOutputReference, jsii.get(self, "cacheKeyFields"))

    @builtins.property
    @jsii.member(jsii_name="cacheTtlByStatus")
    def cache_ttl_by_status(self) -> PageRuleActionsCacheTtlByStatusList:
        return typing.cast(PageRuleActionsCacheTtlByStatusList, jsii.get(self, "cacheTtlByStatus"))

    @builtins.property
    @jsii.member(jsii_name="forwardingUrl")
    def forwarding_url(self) -> PageRuleActionsForwardingUrlOutputReference:
        return typing.cast(PageRuleActionsForwardingUrlOutputReference, jsii.get(self, "forwardingUrl"))

    @builtins.property
    @jsii.member(jsii_name="minify")
    def minify(self) -> PageRuleActionsMinifyList:
        return typing.cast(PageRuleActionsMinifyList, jsii.get(self, "minify"))

    @builtins.property
    @jsii.member(jsii_name="alwaysUseHttpsInput")
    def always_use_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "alwaysUseHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewritesInput")
    def automatic_https_rewrites_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automaticHttpsRewritesInput"))

    @builtins.property
    @jsii.member(jsii_name="browserCacheTtlInput")
    def browser_cache_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "browserCacheTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="browserCheckInput")
    def browser_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "browserCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="bypassCacheOnCookieInput")
    def bypass_cache_on_cookie_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bypassCacheOnCookieInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheByDeviceTypeInput")
    def cache_by_device_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheByDeviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheDeceptionArmorInput")
    def cache_deception_armor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheDeceptionArmorInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyFieldsInput")
    def cache_key_fields_input(self) -> typing.Optional[PageRuleActionsCacheKeyFields]:
        return typing.cast(typing.Optional[PageRuleActionsCacheKeyFields], jsii.get(self, "cacheKeyFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheLevelInput")
    def cache_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheOnCookieInput")
    def cache_on_cookie_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheOnCookieInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheTtlByStatusInput")
    def cache_ttl_by_status_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsCacheTtlByStatus]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsCacheTtlByStatus]]], jsii.get(self, "cacheTtlByStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="disableAppsInput")
    def disable_apps_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableAppsInput"))

    @builtins.property
    @jsii.member(jsii_name="disablePerformanceInput")
    def disable_performance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disablePerformanceInput"))

    @builtins.property
    @jsii.member(jsii_name="disableRailgunInput")
    def disable_railgun_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableRailgunInput"))

    @builtins.property
    @jsii.member(jsii_name="disableSecurityInput")
    def disable_security_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableSecurityInput"))

    @builtins.property
    @jsii.member(jsii_name="disableZarazInput")
    def disable_zaraz_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableZarazInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeCacheTtlInput")
    def edge_cache_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "edgeCacheTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="emailObfuscationInput")
    def email_obfuscation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailObfuscationInput"))

    @builtins.property
    @jsii.member(jsii_name="explicitCacheControlInput")
    def explicit_cache_control_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "explicitCacheControlInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingUrlInput")
    def forwarding_url_input(self) -> typing.Optional[PageRuleActionsForwardingUrl]:
        return typing.cast(typing.Optional[PageRuleActionsForwardingUrl], jsii.get(self, "forwardingUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="hostHeaderOverrideInput")
    def host_header_override_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostHeaderOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="ipGeolocationInput")
    def ip_geolocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipGeolocationInput"))

    @builtins.property
    @jsii.member(jsii_name="minifyInput")
    def minify_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsMinify]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PageRuleActionsMinify]]], jsii.get(self, "minifyInput"))

    @builtins.property
    @jsii.member(jsii_name="mirageInput")
    def mirage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mirageInput"))

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryptionInput")
    def opportunistic_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opportunisticEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassThruInput")
    def origin_error_page_pass_thru_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originErrorPagePassThruInput"))

    @builtins.property
    @jsii.member(jsii_name="polishInput")
    def polish_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "polishInput"))

    @builtins.property
    @jsii.member(jsii_name="resolveOverrideInput")
    def resolve_override_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolveOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="respectStrongEtagInput")
    def respect_strong_etag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "respectStrongEtagInput"))

    @builtins.property
    @jsii.member(jsii_name="responseBufferingInput")
    def response_buffering_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseBufferingInput"))

    @builtins.property
    @jsii.member(jsii_name="rocketLoaderInput")
    def rocket_loader_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rocketLoaderInput"))

    @builtins.property
    @jsii.member(jsii_name="securityLevelInput")
    def security_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideExcludeInput")
    def server_side_exclude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSideExcludeInput"))

    @builtins.property
    @jsii.member(jsii_name="sortQueryStringForCacheInput")
    def sort_query_string_for_cache_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sortQueryStringForCacheInput"))

    @builtins.property
    @jsii.member(jsii_name="sslInput")
    def ssl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslInput"))

    @builtins.property
    @jsii.member(jsii_name="trueClientIpHeaderInput")
    def true_client_ip_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trueClientIpHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="wafInput")
    def waf_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "wafInput"))

    @builtins.property
    @jsii.member(jsii_name="alwaysUseHttps")
    def always_use_https(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "alwaysUseHttps"))

    @always_use_https.setter
    def always_use_https(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "always_use_https").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysUseHttps", value)

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewrites")
    def automatic_https_rewrites(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "automaticHttpsRewrites"))

    @automatic_https_rewrites.setter
    def automatic_https_rewrites(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "automatic_https_rewrites").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticHttpsRewrites", value)

    @builtins.property
    @jsii.member(jsii_name="browserCacheTtl")
    def browser_cache_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserCacheTtl"))

    @browser_cache_ttl.setter
    def browser_cache_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "browser_cache_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserCacheTtl", value)

    @builtins.property
    @jsii.member(jsii_name="browserCheck")
    def browser_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserCheck"))

    @browser_check.setter
    def browser_check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "browser_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserCheck", value)

    @builtins.property
    @jsii.member(jsii_name="bypassCacheOnCookie")
    def bypass_cache_on_cookie(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bypassCacheOnCookie"))

    @bypass_cache_on_cookie.setter
    def bypass_cache_on_cookie(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "bypass_cache_on_cookie").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypassCacheOnCookie", value)

    @builtins.property
    @jsii.member(jsii_name="cacheByDeviceType")
    def cache_by_device_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheByDeviceType"))

    @cache_by_device_type.setter
    def cache_by_device_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "cache_by_device_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheByDeviceType", value)

    @builtins.property
    @jsii.member(jsii_name="cacheDeceptionArmor")
    def cache_deception_armor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheDeceptionArmor"))

    @cache_deception_armor.setter
    def cache_deception_armor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "cache_deception_armor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheDeceptionArmor", value)

    @builtins.property
    @jsii.member(jsii_name="cacheLevel")
    def cache_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheLevel"))

    @cache_level.setter
    def cache_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "cache_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheLevel", value)

    @builtins.property
    @jsii.member(jsii_name="cacheOnCookie")
    def cache_on_cookie(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheOnCookie"))

    @cache_on_cookie.setter
    def cache_on_cookie(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "cache_on_cookie").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheOnCookie", value)

    @builtins.property
    @jsii.member(jsii_name="disableApps")
    def disable_apps(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableApps"))

    @disable_apps.setter
    def disable_apps(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "disable_apps").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableApps", value)

    @builtins.property
    @jsii.member(jsii_name="disablePerformance")
    def disable_performance(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disablePerformance"))

    @disable_performance.setter
    def disable_performance(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "disable_performance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablePerformance", value)

    @builtins.property
    @jsii.member(jsii_name="disableRailgun")
    def disable_railgun(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableRailgun"))

    @disable_railgun.setter
    def disable_railgun(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "disable_railgun").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRailgun", value)

    @builtins.property
    @jsii.member(jsii_name="disableSecurity")
    def disable_security(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableSecurity"))

    @disable_security.setter
    def disable_security(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "disable_security").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableSecurity", value)

    @builtins.property
    @jsii.member(jsii_name="disableZaraz")
    def disable_zaraz(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableZaraz"))

    @disable_zaraz.setter
    def disable_zaraz(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "disable_zaraz").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableZaraz", value)

    @builtins.property
    @jsii.member(jsii_name="edgeCacheTtl")
    def edge_cache_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "edgeCacheTtl"))

    @edge_cache_ttl.setter
    def edge_cache_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "edge_cache_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeCacheTtl", value)

    @builtins.property
    @jsii.member(jsii_name="emailObfuscation")
    def email_obfuscation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailObfuscation"))

    @email_obfuscation.setter
    def email_obfuscation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "email_obfuscation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailObfuscation", value)

    @builtins.property
    @jsii.member(jsii_name="explicitCacheControl")
    def explicit_cache_control(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "explicitCacheControl"))

    @explicit_cache_control.setter
    def explicit_cache_control(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "explicit_cache_control").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "explicitCacheControl", value)

    @builtins.property
    @jsii.member(jsii_name="hostHeaderOverride")
    def host_header_override(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostHeaderOverride"))

    @host_header_override.setter
    def host_header_override(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "host_header_override").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostHeaderOverride", value)

    @builtins.property
    @jsii.member(jsii_name="ipGeolocation")
    def ip_geolocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipGeolocation"))

    @ip_geolocation.setter
    def ip_geolocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "ip_geolocation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipGeolocation", value)

    @builtins.property
    @jsii.member(jsii_name="mirage")
    def mirage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mirage"))

    @mirage.setter
    def mirage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "mirage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mirage", value)

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryption")
    def opportunistic_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opportunisticEncryption"))

    @opportunistic_encryption.setter
    def opportunistic_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "opportunistic_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opportunisticEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassThru")
    def origin_error_page_pass_thru(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originErrorPagePassThru"))

    @origin_error_page_pass_thru.setter
    def origin_error_page_pass_thru(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "origin_error_page_pass_thru").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originErrorPagePassThru", value)

    @builtins.property
    @jsii.member(jsii_name="polish")
    def polish(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "polish"))

    @polish.setter
    def polish(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "polish").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "polish", value)

    @builtins.property
    @jsii.member(jsii_name="resolveOverride")
    def resolve_override(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resolveOverride"))

    @resolve_override.setter
    def resolve_override(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "resolve_override").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolveOverride", value)

    @builtins.property
    @jsii.member(jsii_name="respectStrongEtag")
    def respect_strong_etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "respectStrongEtag"))

    @respect_strong_etag.setter
    def respect_strong_etag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "respect_strong_etag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "respectStrongEtag", value)

    @builtins.property
    @jsii.member(jsii_name="responseBuffering")
    def response_buffering(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseBuffering"))

    @response_buffering.setter
    def response_buffering(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "response_buffering").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseBuffering", value)

    @builtins.property
    @jsii.member(jsii_name="rocketLoader")
    def rocket_loader(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rocketLoader"))

    @rocket_loader.setter
    def rocket_loader(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "rocket_loader").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rocketLoader", value)

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityLevel"))

    @security_level.setter
    def security_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "security_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideExclude")
    def server_side_exclude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideExclude"))

    @server_side_exclude.setter
    def server_side_exclude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "server_side_exclude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideExclude", value)

    @builtins.property
    @jsii.member(jsii_name="sortQueryStringForCache")
    def sort_query_string_for_cache(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sortQueryStringForCache"))

    @sort_query_string_for_cache.setter
    def sort_query_string_for_cache(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "sort_query_string_for_cache").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortQueryStringForCache", value)

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssl"))

    @ssl.setter
    def ssl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssl", value)

    @builtins.property
    @jsii.member(jsii_name="trueClientIpHeader")
    def true_client_ip_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trueClientIpHeader"))

    @true_client_ip_header.setter
    def true_client_ip_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "true_client_ip_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trueClientIpHeader", value)

    @builtins.property
    @jsii.member(jsii_name="waf")
    def waf(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waf"))

    @waf.setter
    def waf(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "waf").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waf", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PageRuleActions]:
        return typing.cast(typing.Optional[PageRuleActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PageRuleActions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PageRuleActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.pageRule.PageRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "actions": "actions",
        "target": "target",
        "zone_id": "zoneId",
        "id": "id",
        "priority": "priority",
        "status": "status",
    },
)
class PageRuleConfig(cdktf.TerraformMetaArguments):
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
        actions: typing.Union[PageRuleActions, typing.Dict[str, typing.Any]],
        target: builtins.str,
        zone_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#actions PageRule#actions}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#target PageRule#target}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#zone_id PageRule#zone_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#id PageRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#priority PageRule#priority}
        :param status: Defaults to ``active``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#status PageRule#status}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(actions, dict):
            actions = PageRuleActions(**actions)
        if __debug__:
            type_hints = typing.get_type_hints(PageRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "target": target,
            "zone_id": zone_id,
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
        if priority is not None:
            self._values["priority"] = priority
        if status is not None:
            self._values["status"] = status

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
    def actions(self) -> PageRuleActions:
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#actions PageRule#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(PageRuleActions, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#target PageRule#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#zone_id PageRule#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#id PageRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Defaults to ``1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#priority PageRule#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``active``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/page_rule#status PageRule#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PageRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PageRule",
    "PageRuleActions",
    "PageRuleActionsCacheKeyFields",
    "PageRuleActionsCacheKeyFieldsCookie",
    "PageRuleActionsCacheKeyFieldsCookieOutputReference",
    "PageRuleActionsCacheKeyFieldsHeader",
    "PageRuleActionsCacheKeyFieldsHeaderOutputReference",
    "PageRuleActionsCacheKeyFieldsHost",
    "PageRuleActionsCacheKeyFieldsHostOutputReference",
    "PageRuleActionsCacheKeyFieldsOutputReference",
    "PageRuleActionsCacheKeyFieldsQueryString",
    "PageRuleActionsCacheKeyFieldsQueryStringOutputReference",
    "PageRuleActionsCacheKeyFieldsUser",
    "PageRuleActionsCacheKeyFieldsUserOutputReference",
    "PageRuleActionsCacheTtlByStatus",
    "PageRuleActionsCacheTtlByStatusList",
    "PageRuleActionsCacheTtlByStatusOutputReference",
    "PageRuleActionsForwardingUrl",
    "PageRuleActionsForwardingUrlOutputReference",
    "PageRuleActionsMinify",
    "PageRuleActionsMinifyList",
    "PageRuleActionsMinifyOutputReference",
    "PageRuleActionsOutputReference",
    "PageRuleConfig",
]

publication.publish()
