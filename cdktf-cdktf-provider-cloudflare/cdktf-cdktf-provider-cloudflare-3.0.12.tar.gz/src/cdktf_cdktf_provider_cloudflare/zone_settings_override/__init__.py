'''
# `cloudflare_zone_settings_override`

Refer to the Terraform Registory for docs: [`cloudflare_zone_settings_override`](https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override).
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


class ZoneSettingsOverride(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverride",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override cloudflare_zone_settings_override}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        zone_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union["ZoneSettingsOverrideSettings", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override cloudflare_zone_settings_override} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#zone_id ZoneSettingsOverride#zone_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#id ZoneSettingsOverride#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#settings ZoneSettingsOverride#settings}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverride.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ZoneSettingsOverrideConfig(
            zone_id=zone_id,
            id=id,
            settings=settings,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        *,
        always_online: typing.Optional[builtins.str] = None,
        always_use_https: typing.Optional[builtins.str] = None,
        automatic_https_rewrites: typing.Optional[builtins.str] = None,
        binary_ast: typing.Optional[builtins.str] = None,
        brotli: typing.Optional[builtins.str] = None,
        browser_cache_ttl: typing.Optional[jsii.Number] = None,
        browser_check: typing.Optional[builtins.str] = None,
        cache_level: typing.Optional[builtins.str] = None,
        challenge_ttl: typing.Optional[jsii.Number] = None,
        ciphers: typing.Optional[typing.Sequence[builtins.str]] = None,
        cname_flattening: typing.Optional[builtins.str] = None,
        development_mode: typing.Optional[builtins.str] = None,
        early_hints: typing.Optional[builtins.str] = None,
        email_obfuscation: typing.Optional[builtins.str] = None,
        filter_logs_to_cloudflare: typing.Optional[builtins.str] = None,
        h2_prioritization: typing.Optional[builtins.str] = None,
        hotlink_protection: typing.Optional[builtins.str] = None,
        http2: typing.Optional[builtins.str] = None,
        http3: typing.Optional[builtins.str] = None,
        image_resizing: typing.Optional[builtins.str] = None,
        ip_geolocation: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[builtins.str] = None,
        log_to_cloudflare: typing.Optional[builtins.str] = None,
        max_upload: typing.Optional[jsii.Number] = None,
        minify: typing.Optional[typing.Union["ZoneSettingsOverrideSettingsMinify", typing.Dict[str, typing.Any]]] = None,
        min_tls_version: typing.Optional[builtins.str] = None,
        mirage: typing.Optional[builtins.str] = None,
        mobile_redirect: typing.Optional[typing.Union["ZoneSettingsOverrideSettingsMobileRedirect", typing.Dict[str, typing.Any]]] = None,
        opportunistic_encryption: typing.Optional[builtins.str] = None,
        opportunistic_onion: typing.Optional[builtins.str] = None,
        orange_to_orange: typing.Optional[builtins.str] = None,
        origin_error_page_pass_thru: typing.Optional[builtins.str] = None,
        origin_max_http_version: typing.Optional[builtins.str] = None,
        polish: typing.Optional[builtins.str] = None,
        prefetch_preload: typing.Optional[builtins.str] = None,
        privacy_pass: typing.Optional[builtins.str] = None,
        proxy_read_timeout: typing.Optional[builtins.str] = None,
        pseudo_ipv4: typing.Optional[builtins.str] = None,
        response_buffering: typing.Optional[builtins.str] = None,
        rocket_loader: typing.Optional[builtins.str] = None,
        security_header: typing.Optional[typing.Union["ZoneSettingsOverrideSettingsSecurityHeader", typing.Dict[str, typing.Any]]] = None,
        security_level: typing.Optional[builtins.str] = None,
        server_side_exclude: typing.Optional[builtins.str] = None,
        sort_query_string_for_cache: typing.Optional[builtins.str] = None,
        ssl: typing.Optional[builtins.str] = None,
        tls12_only: typing.Optional[builtins.str] = None,
        tls13: typing.Optional[builtins.str] = None,
        tls_client_auth: typing.Optional[builtins.str] = None,
        true_client_ip_header: typing.Optional[builtins.str] = None,
        universal_ssl: typing.Optional[builtins.str] = None,
        visitor_ip: typing.Optional[builtins.str] = None,
        waf: typing.Optional[builtins.str] = None,
        webp: typing.Optional[builtins.str] = None,
        websockets: typing.Optional[builtins.str] = None,
        zero_rtt: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param always_online: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#always_online ZoneSettingsOverride#always_online}.
        :param always_use_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#always_use_https ZoneSettingsOverride#always_use_https}.
        :param automatic_https_rewrites: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#automatic_https_rewrites ZoneSettingsOverride#automatic_https_rewrites}.
        :param binary_ast: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#binary_ast ZoneSettingsOverride#binary_ast}.
        :param brotli: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#brotli ZoneSettingsOverride#brotli}.
        :param browser_cache_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#browser_cache_ttl ZoneSettingsOverride#browser_cache_ttl}.
        :param browser_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#browser_check ZoneSettingsOverride#browser_check}.
        :param cache_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#cache_level ZoneSettingsOverride#cache_level}.
        :param challenge_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#challenge_ttl ZoneSettingsOverride#challenge_ttl}.
        :param ciphers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ciphers ZoneSettingsOverride#ciphers}.
        :param cname_flattening: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#cname_flattening ZoneSettingsOverride#cname_flattening}.
        :param development_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#development_mode ZoneSettingsOverride#development_mode}.
        :param early_hints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#early_hints ZoneSettingsOverride#early_hints}.
        :param email_obfuscation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#email_obfuscation ZoneSettingsOverride#email_obfuscation}.
        :param filter_logs_to_cloudflare: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#filter_logs_to_cloudflare ZoneSettingsOverride#filter_logs_to_cloudflare}.
        :param h2_prioritization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#h2_prioritization ZoneSettingsOverride#h2_prioritization}.
        :param hotlink_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#hotlink_protection ZoneSettingsOverride#hotlink_protection}.
        :param http2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#http2 ZoneSettingsOverride#http2}.
        :param http3: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#http3 ZoneSettingsOverride#http3}.
        :param image_resizing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#image_resizing ZoneSettingsOverride#image_resizing}.
        :param ip_geolocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ip_geolocation ZoneSettingsOverride#ip_geolocation}.
        :param ipv6: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ipv6 ZoneSettingsOverride#ipv6}.
        :param log_to_cloudflare: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#log_to_cloudflare ZoneSettingsOverride#log_to_cloudflare}.
        :param max_upload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#max_upload ZoneSettingsOverride#max_upload}.
        :param minify: minify block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#minify ZoneSettingsOverride#minify}
        :param min_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#min_tls_version ZoneSettingsOverride#min_tls_version}.
        :param mirage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mirage ZoneSettingsOverride#mirage}.
        :param mobile_redirect: mobile_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mobile_redirect ZoneSettingsOverride#mobile_redirect}
        :param opportunistic_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#opportunistic_encryption ZoneSettingsOverride#opportunistic_encryption}.
        :param opportunistic_onion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#opportunistic_onion ZoneSettingsOverride#opportunistic_onion}.
        :param orange_to_orange: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#orange_to_orange ZoneSettingsOverride#orange_to_orange}.
        :param origin_error_page_pass_thru: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#origin_error_page_pass_thru ZoneSettingsOverride#origin_error_page_pass_thru}.
        :param origin_max_http_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#origin_max_http_version ZoneSettingsOverride#origin_max_http_version}.
        :param polish: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#polish ZoneSettingsOverride#polish}.
        :param prefetch_preload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#prefetch_preload ZoneSettingsOverride#prefetch_preload}.
        :param privacy_pass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#privacy_pass ZoneSettingsOverride#privacy_pass}.
        :param proxy_read_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#proxy_read_timeout ZoneSettingsOverride#proxy_read_timeout}.
        :param pseudo_ipv4: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#pseudo_ipv4 ZoneSettingsOverride#pseudo_ipv4}.
        :param response_buffering: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#response_buffering ZoneSettingsOverride#response_buffering}.
        :param rocket_loader: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#rocket_loader ZoneSettingsOverride#rocket_loader}.
        :param security_header: security_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#security_header ZoneSettingsOverride#security_header}
        :param security_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#security_level ZoneSettingsOverride#security_level}.
        :param server_side_exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#server_side_exclude ZoneSettingsOverride#server_side_exclude}.
        :param sort_query_string_for_cache: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#sort_query_string_for_cache ZoneSettingsOverride#sort_query_string_for_cache}.
        :param ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ssl ZoneSettingsOverride#ssl}.
        :param tls12_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_1_2_only ZoneSettingsOverride#tls_1_2_only}.
        :param tls13: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_1_3 ZoneSettingsOverride#tls_1_3}.
        :param tls_client_auth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_client_auth ZoneSettingsOverride#tls_client_auth}.
        :param true_client_ip_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#true_client_ip_header ZoneSettingsOverride#true_client_ip_header}.
        :param universal_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#universal_ssl ZoneSettingsOverride#universal_ssl}.
        :param visitor_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#visitor_ip ZoneSettingsOverride#visitor_ip}.
        :param waf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#waf ZoneSettingsOverride#waf}.
        :param webp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#webp ZoneSettingsOverride#webp}.
        :param websockets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#websockets ZoneSettingsOverride#websockets}.
        :param zero_rtt: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#zero_rtt ZoneSettingsOverride#zero_rtt}.
        '''
        value = ZoneSettingsOverrideSettings(
            always_online=always_online,
            always_use_https=always_use_https,
            automatic_https_rewrites=automatic_https_rewrites,
            binary_ast=binary_ast,
            brotli=brotli,
            browser_cache_ttl=browser_cache_ttl,
            browser_check=browser_check,
            cache_level=cache_level,
            challenge_ttl=challenge_ttl,
            ciphers=ciphers,
            cname_flattening=cname_flattening,
            development_mode=development_mode,
            early_hints=early_hints,
            email_obfuscation=email_obfuscation,
            filter_logs_to_cloudflare=filter_logs_to_cloudflare,
            h2_prioritization=h2_prioritization,
            hotlink_protection=hotlink_protection,
            http2=http2,
            http3=http3,
            image_resizing=image_resizing,
            ip_geolocation=ip_geolocation,
            ipv6=ipv6,
            log_to_cloudflare=log_to_cloudflare,
            max_upload=max_upload,
            minify=minify,
            min_tls_version=min_tls_version,
            mirage=mirage,
            mobile_redirect=mobile_redirect,
            opportunistic_encryption=opportunistic_encryption,
            opportunistic_onion=opportunistic_onion,
            orange_to_orange=orange_to_orange,
            origin_error_page_pass_thru=origin_error_page_pass_thru,
            origin_max_http_version=origin_max_http_version,
            polish=polish,
            prefetch_preload=prefetch_preload,
            privacy_pass=privacy_pass,
            proxy_read_timeout=proxy_read_timeout,
            pseudo_ipv4=pseudo_ipv4,
            response_buffering=response_buffering,
            rocket_loader=rocket_loader,
            security_header=security_header,
            security_level=security_level,
            server_side_exclude=server_side_exclude,
            sort_query_string_for_cache=sort_query_string_for_cache,
            ssl=ssl,
            tls12_only=tls12_only,
            tls13=tls13,
            tls_client_auth=tls_client_auth,
            true_client_ip_header=true_client_ip_header,
            universal_ssl=universal_ssl,
            visitor_ip=visitor_ip,
            waf=waf,
            webp=webp,
            websockets=websockets,
            zero_rtt=zero_rtt,
        )

        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="initialSettings")
    def initial_settings(self) -> "ZoneSettingsOverrideInitialSettingsList":
        return typing.cast("ZoneSettingsOverrideInitialSettingsList", jsii.get(self, "initialSettings"))

    @builtins.property
    @jsii.member(jsii_name="initialSettingsReadAt")
    def initial_settings_read_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialSettingsReadAt"))

    @builtins.property
    @jsii.member(jsii_name="readonlySettings")
    def readonly_settings(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "readonlySettings"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "ZoneSettingsOverrideSettingsOutputReference":
        return typing.cast("ZoneSettingsOverrideSettingsOutputReference", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="zoneStatus")
    def zone_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneStatus"))

    @builtins.property
    @jsii.member(jsii_name="zoneType")
    def zone_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneType"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional["ZoneSettingsOverrideSettings"]:
        return typing.cast(typing.Optional["ZoneSettingsOverrideSettings"], jsii.get(self, "settingsInput"))

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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverride, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverride, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "zone_id": "zoneId",
        "id": "id",
        "settings": "settings",
    },
)
class ZoneSettingsOverrideConfig(cdktf.TerraformMetaArguments):
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
        zone_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union["ZoneSettingsOverrideSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#zone_id ZoneSettingsOverride#zone_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#id ZoneSettingsOverride#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#settings ZoneSettingsOverride#settings}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(settings, dict):
            settings = ZoneSettingsOverrideSettings(**settings)
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if settings is not None:
            self._values["settings"] = settings

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
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#zone_id ZoneSettingsOverride#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#id ZoneSettingsOverride#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional["ZoneSettingsOverrideSettings"]:
        '''settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#settings ZoneSettingsOverride#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional["ZoneSettingsOverrideSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettings",
    jsii_struct_bases=[],
    name_mapping={},
)
class ZoneSettingsOverrideInitialSettings:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideInitialSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneSettingsOverrideInitialSettingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsList",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ZoneSettingsOverrideInitialSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ZoneSettingsOverrideInitialSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsMinify",
    jsii_struct_bases=[],
    name_mapping={},
)
class ZoneSettingsOverrideInitialSettingsMinify:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideInitialSettingsMinify(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneSettingsOverrideInitialSettingsMinifyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsMinifyList",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsMinifyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ZoneSettingsOverrideInitialSettingsMinifyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsMinifyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ZoneSettingsOverrideInitialSettingsMinifyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsMinifyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsMinifyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsMinifyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ZoneSettingsOverrideInitialSettingsMinifyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsMinifyOutputReference",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsMinifyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="css")
    def css(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "css"))

    @builtins.property
    @jsii.member(jsii_name="html")
    def html(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "html"))

    @builtins.property
    @jsii.member(jsii_name="js")
    def js(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "js"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ZoneSettingsOverrideInitialSettingsMinify]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideInitialSettingsMinify], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ZoneSettingsOverrideInitialSettingsMinify],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsMinifyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsMobileRedirect",
    jsii_struct_bases=[],
    name_mapping={},
)
class ZoneSettingsOverrideInitialSettingsMobileRedirect:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideInitialSettingsMobileRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneSettingsOverrideInitialSettingsMobileRedirectList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsMobileRedirectList",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsMobileRedirectList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ZoneSettingsOverrideInitialSettingsMobileRedirectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsMobileRedirectList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ZoneSettingsOverrideInitialSettingsMobileRedirectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsMobileRedirectList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsMobileRedirectList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsMobileRedirectList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ZoneSettingsOverrideInitialSettingsMobileRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsMobileRedirectOutputReference",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsMobileRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="mobileSubdomain")
    def mobile_subdomain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mobileSubdomain"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="stripUri")
    def strip_uri(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "stripUri"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ZoneSettingsOverrideInitialSettingsMobileRedirect]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideInitialSettingsMobileRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ZoneSettingsOverrideInitialSettingsMobileRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsMobileRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ZoneSettingsOverrideInitialSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsOutputReference",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="alwaysOnline")
    def always_online(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alwaysOnline"))

    @builtins.property
    @jsii.member(jsii_name="alwaysUseHttps")
    def always_use_https(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alwaysUseHttps"))

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewrites")
    def automatic_https_rewrites(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "automaticHttpsRewrites"))

    @builtins.property
    @jsii.member(jsii_name="binaryAst")
    def binary_ast(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "binaryAst"))

    @builtins.property
    @jsii.member(jsii_name="brotli")
    def brotli(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "brotli"))

    @builtins.property
    @jsii.member(jsii_name="browserCacheTtl")
    def browser_cache_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "browserCacheTtl"))

    @builtins.property
    @jsii.member(jsii_name="browserCheck")
    def browser_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserCheck"))

    @builtins.property
    @jsii.member(jsii_name="cacheLevel")
    def cache_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheLevel"))

    @builtins.property
    @jsii.member(jsii_name="challengeTtl")
    def challenge_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "challengeTtl"))

    @builtins.property
    @jsii.member(jsii_name="ciphers")
    def ciphers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ciphers"))

    @builtins.property
    @jsii.member(jsii_name="cnameFlattening")
    def cname_flattening(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cnameFlattening"))

    @builtins.property
    @jsii.member(jsii_name="developmentMode")
    def development_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "developmentMode"))

    @builtins.property
    @jsii.member(jsii_name="earlyHints")
    def early_hints(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "earlyHints"))

    @builtins.property
    @jsii.member(jsii_name="emailObfuscation")
    def email_obfuscation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailObfuscation"))

    @builtins.property
    @jsii.member(jsii_name="filterLogsToCloudflare")
    def filter_logs_to_cloudflare(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterLogsToCloudflare"))

    @builtins.property
    @jsii.member(jsii_name="h2Prioritization")
    def h2_prioritization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "h2Prioritization"))

    @builtins.property
    @jsii.member(jsii_name="hotlinkProtection")
    def hotlink_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hotlinkProtection"))

    @builtins.property
    @jsii.member(jsii_name="http2")
    def http2(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "http2"))

    @builtins.property
    @jsii.member(jsii_name="http3")
    def http3(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "http3"))

    @builtins.property
    @jsii.member(jsii_name="imageResizing")
    def image_resizing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageResizing"))

    @builtins.property
    @jsii.member(jsii_name="ipGeolocation")
    def ip_geolocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipGeolocation"))

    @builtins.property
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6"))

    @builtins.property
    @jsii.member(jsii_name="logToCloudflare")
    def log_to_cloudflare(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logToCloudflare"))

    @builtins.property
    @jsii.member(jsii_name="maxUpload")
    def max_upload(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUpload"))

    @builtins.property
    @jsii.member(jsii_name="minify")
    def minify(self) -> ZoneSettingsOverrideInitialSettingsMinifyList:
        return typing.cast(ZoneSettingsOverrideInitialSettingsMinifyList, jsii.get(self, "minify"))

    @builtins.property
    @jsii.member(jsii_name="minTlsVersion")
    def min_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTlsVersion"))

    @builtins.property
    @jsii.member(jsii_name="mirage")
    def mirage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mirage"))

    @builtins.property
    @jsii.member(jsii_name="mobileRedirect")
    def mobile_redirect(self) -> ZoneSettingsOverrideInitialSettingsMobileRedirectList:
        return typing.cast(ZoneSettingsOverrideInitialSettingsMobileRedirectList, jsii.get(self, "mobileRedirect"))

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryption")
    def opportunistic_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opportunisticEncryption"))

    @builtins.property
    @jsii.member(jsii_name="opportunisticOnion")
    def opportunistic_onion(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opportunisticOnion"))

    @builtins.property
    @jsii.member(jsii_name="orangeToOrange")
    def orange_to_orange(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orangeToOrange"))

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassThru")
    def origin_error_page_pass_thru(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originErrorPagePassThru"))

    @builtins.property
    @jsii.member(jsii_name="originMaxHttpVersion")
    def origin_max_http_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originMaxHttpVersion"))

    @builtins.property
    @jsii.member(jsii_name="polish")
    def polish(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "polish"))

    @builtins.property
    @jsii.member(jsii_name="prefetchPreload")
    def prefetch_preload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefetchPreload"))

    @builtins.property
    @jsii.member(jsii_name="privacyPass")
    def privacy_pass(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privacyPass"))

    @builtins.property
    @jsii.member(jsii_name="proxyReadTimeout")
    def proxy_read_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyReadTimeout"))

    @builtins.property
    @jsii.member(jsii_name="pseudoIpv4")
    def pseudo_ipv4(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pseudoIpv4"))

    @builtins.property
    @jsii.member(jsii_name="responseBuffering")
    def response_buffering(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseBuffering"))

    @builtins.property
    @jsii.member(jsii_name="rocketLoader")
    def rocket_loader(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rocketLoader"))

    @builtins.property
    @jsii.member(jsii_name="securityHeader")
    def security_header(
        self,
    ) -> "ZoneSettingsOverrideInitialSettingsSecurityHeaderList":
        return typing.cast("ZoneSettingsOverrideInitialSettingsSecurityHeaderList", jsii.get(self, "securityHeader"))

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityLevel"))

    @builtins.property
    @jsii.member(jsii_name="serverSideExclude")
    def server_side_exclude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideExclude"))

    @builtins.property
    @jsii.member(jsii_name="sortQueryStringForCache")
    def sort_query_string_for_cache(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sortQueryStringForCache"))

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssl"))

    @builtins.property
    @jsii.member(jsii_name="tls12Only")
    def tls12_only(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tls12Only"))

    @builtins.property
    @jsii.member(jsii_name="tls13")
    def tls13(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tls13"))

    @builtins.property
    @jsii.member(jsii_name="tlsClientAuth")
    def tls_client_auth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsClientAuth"))

    @builtins.property
    @jsii.member(jsii_name="trueClientIpHeader")
    def true_client_ip_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trueClientIpHeader"))

    @builtins.property
    @jsii.member(jsii_name="universalSsl")
    def universal_ssl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "universalSsl"))

    @builtins.property
    @jsii.member(jsii_name="visitorIp")
    def visitor_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visitorIp"))

    @builtins.property
    @jsii.member(jsii_name="waf")
    def waf(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waf"))

    @builtins.property
    @jsii.member(jsii_name="webp")
    def webp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webp"))

    @builtins.property
    @jsii.member(jsii_name="websockets")
    def websockets(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "websockets"))

    @builtins.property
    @jsii.member(jsii_name="zeroRtt")
    def zero_rtt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zeroRtt"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ZoneSettingsOverrideInitialSettings]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideInitialSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ZoneSettingsOverrideInitialSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsSecurityHeader",
    jsii_struct_bases=[],
    name_mapping={},
)
class ZoneSettingsOverrideInitialSettingsSecurityHeader:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideInitialSettingsSecurityHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneSettingsOverrideInitialSettingsSecurityHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsSecurityHeaderList",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsSecurityHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ZoneSettingsOverrideInitialSettingsSecurityHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsSecurityHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ZoneSettingsOverrideInitialSettingsSecurityHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsSecurityHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsSecurityHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsSecurityHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ZoneSettingsOverrideInitialSettingsSecurityHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideInitialSettingsSecurityHeaderOutputReference",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideInitialSettingsSecurityHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="includeSubdomains")
    def include_subdomains(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "includeSubdomains"))

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @builtins.property
    @jsii.member(jsii_name="nosniff")
    def nosniff(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "nosniff"))

    @builtins.property
    @jsii.member(jsii_name="preload")
    def preload(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "preload"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ZoneSettingsOverrideInitialSettingsSecurityHeader]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideInitialSettingsSecurityHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ZoneSettingsOverrideInitialSettingsSecurityHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideInitialSettingsSecurityHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideSettings",
    jsii_struct_bases=[],
    name_mapping={
        "always_online": "alwaysOnline",
        "always_use_https": "alwaysUseHttps",
        "automatic_https_rewrites": "automaticHttpsRewrites",
        "binary_ast": "binaryAst",
        "brotli": "brotli",
        "browser_cache_ttl": "browserCacheTtl",
        "browser_check": "browserCheck",
        "cache_level": "cacheLevel",
        "challenge_ttl": "challengeTtl",
        "ciphers": "ciphers",
        "cname_flattening": "cnameFlattening",
        "development_mode": "developmentMode",
        "early_hints": "earlyHints",
        "email_obfuscation": "emailObfuscation",
        "filter_logs_to_cloudflare": "filterLogsToCloudflare",
        "h2_prioritization": "h2Prioritization",
        "hotlink_protection": "hotlinkProtection",
        "http2": "http2",
        "http3": "http3",
        "image_resizing": "imageResizing",
        "ip_geolocation": "ipGeolocation",
        "ipv6": "ipv6",
        "log_to_cloudflare": "logToCloudflare",
        "max_upload": "maxUpload",
        "minify": "minify",
        "min_tls_version": "minTlsVersion",
        "mirage": "mirage",
        "mobile_redirect": "mobileRedirect",
        "opportunistic_encryption": "opportunisticEncryption",
        "opportunistic_onion": "opportunisticOnion",
        "orange_to_orange": "orangeToOrange",
        "origin_error_page_pass_thru": "originErrorPagePassThru",
        "origin_max_http_version": "originMaxHttpVersion",
        "polish": "polish",
        "prefetch_preload": "prefetchPreload",
        "privacy_pass": "privacyPass",
        "proxy_read_timeout": "proxyReadTimeout",
        "pseudo_ipv4": "pseudoIpv4",
        "response_buffering": "responseBuffering",
        "rocket_loader": "rocketLoader",
        "security_header": "securityHeader",
        "security_level": "securityLevel",
        "server_side_exclude": "serverSideExclude",
        "sort_query_string_for_cache": "sortQueryStringForCache",
        "ssl": "ssl",
        "tls12_only": "tls12Only",
        "tls13": "tls13",
        "tls_client_auth": "tlsClientAuth",
        "true_client_ip_header": "trueClientIpHeader",
        "universal_ssl": "universalSsl",
        "visitor_ip": "visitorIp",
        "waf": "waf",
        "webp": "webp",
        "websockets": "websockets",
        "zero_rtt": "zeroRtt",
    },
)
class ZoneSettingsOverrideSettings:
    def __init__(
        self,
        *,
        always_online: typing.Optional[builtins.str] = None,
        always_use_https: typing.Optional[builtins.str] = None,
        automatic_https_rewrites: typing.Optional[builtins.str] = None,
        binary_ast: typing.Optional[builtins.str] = None,
        brotli: typing.Optional[builtins.str] = None,
        browser_cache_ttl: typing.Optional[jsii.Number] = None,
        browser_check: typing.Optional[builtins.str] = None,
        cache_level: typing.Optional[builtins.str] = None,
        challenge_ttl: typing.Optional[jsii.Number] = None,
        ciphers: typing.Optional[typing.Sequence[builtins.str]] = None,
        cname_flattening: typing.Optional[builtins.str] = None,
        development_mode: typing.Optional[builtins.str] = None,
        early_hints: typing.Optional[builtins.str] = None,
        email_obfuscation: typing.Optional[builtins.str] = None,
        filter_logs_to_cloudflare: typing.Optional[builtins.str] = None,
        h2_prioritization: typing.Optional[builtins.str] = None,
        hotlink_protection: typing.Optional[builtins.str] = None,
        http2: typing.Optional[builtins.str] = None,
        http3: typing.Optional[builtins.str] = None,
        image_resizing: typing.Optional[builtins.str] = None,
        ip_geolocation: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[builtins.str] = None,
        log_to_cloudflare: typing.Optional[builtins.str] = None,
        max_upload: typing.Optional[jsii.Number] = None,
        minify: typing.Optional[typing.Union["ZoneSettingsOverrideSettingsMinify", typing.Dict[str, typing.Any]]] = None,
        min_tls_version: typing.Optional[builtins.str] = None,
        mirage: typing.Optional[builtins.str] = None,
        mobile_redirect: typing.Optional[typing.Union["ZoneSettingsOverrideSettingsMobileRedirect", typing.Dict[str, typing.Any]]] = None,
        opportunistic_encryption: typing.Optional[builtins.str] = None,
        opportunistic_onion: typing.Optional[builtins.str] = None,
        orange_to_orange: typing.Optional[builtins.str] = None,
        origin_error_page_pass_thru: typing.Optional[builtins.str] = None,
        origin_max_http_version: typing.Optional[builtins.str] = None,
        polish: typing.Optional[builtins.str] = None,
        prefetch_preload: typing.Optional[builtins.str] = None,
        privacy_pass: typing.Optional[builtins.str] = None,
        proxy_read_timeout: typing.Optional[builtins.str] = None,
        pseudo_ipv4: typing.Optional[builtins.str] = None,
        response_buffering: typing.Optional[builtins.str] = None,
        rocket_loader: typing.Optional[builtins.str] = None,
        security_header: typing.Optional[typing.Union["ZoneSettingsOverrideSettingsSecurityHeader", typing.Dict[str, typing.Any]]] = None,
        security_level: typing.Optional[builtins.str] = None,
        server_side_exclude: typing.Optional[builtins.str] = None,
        sort_query_string_for_cache: typing.Optional[builtins.str] = None,
        ssl: typing.Optional[builtins.str] = None,
        tls12_only: typing.Optional[builtins.str] = None,
        tls13: typing.Optional[builtins.str] = None,
        tls_client_auth: typing.Optional[builtins.str] = None,
        true_client_ip_header: typing.Optional[builtins.str] = None,
        universal_ssl: typing.Optional[builtins.str] = None,
        visitor_ip: typing.Optional[builtins.str] = None,
        waf: typing.Optional[builtins.str] = None,
        webp: typing.Optional[builtins.str] = None,
        websockets: typing.Optional[builtins.str] = None,
        zero_rtt: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param always_online: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#always_online ZoneSettingsOverride#always_online}.
        :param always_use_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#always_use_https ZoneSettingsOverride#always_use_https}.
        :param automatic_https_rewrites: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#automatic_https_rewrites ZoneSettingsOverride#automatic_https_rewrites}.
        :param binary_ast: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#binary_ast ZoneSettingsOverride#binary_ast}.
        :param brotli: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#brotli ZoneSettingsOverride#brotli}.
        :param browser_cache_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#browser_cache_ttl ZoneSettingsOverride#browser_cache_ttl}.
        :param browser_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#browser_check ZoneSettingsOverride#browser_check}.
        :param cache_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#cache_level ZoneSettingsOverride#cache_level}.
        :param challenge_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#challenge_ttl ZoneSettingsOverride#challenge_ttl}.
        :param ciphers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ciphers ZoneSettingsOverride#ciphers}.
        :param cname_flattening: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#cname_flattening ZoneSettingsOverride#cname_flattening}.
        :param development_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#development_mode ZoneSettingsOverride#development_mode}.
        :param early_hints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#early_hints ZoneSettingsOverride#early_hints}.
        :param email_obfuscation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#email_obfuscation ZoneSettingsOverride#email_obfuscation}.
        :param filter_logs_to_cloudflare: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#filter_logs_to_cloudflare ZoneSettingsOverride#filter_logs_to_cloudflare}.
        :param h2_prioritization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#h2_prioritization ZoneSettingsOverride#h2_prioritization}.
        :param hotlink_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#hotlink_protection ZoneSettingsOverride#hotlink_protection}.
        :param http2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#http2 ZoneSettingsOverride#http2}.
        :param http3: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#http3 ZoneSettingsOverride#http3}.
        :param image_resizing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#image_resizing ZoneSettingsOverride#image_resizing}.
        :param ip_geolocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ip_geolocation ZoneSettingsOverride#ip_geolocation}.
        :param ipv6: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ipv6 ZoneSettingsOverride#ipv6}.
        :param log_to_cloudflare: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#log_to_cloudflare ZoneSettingsOverride#log_to_cloudflare}.
        :param max_upload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#max_upload ZoneSettingsOverride#max_upload}.
        :param minify: minify block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#minify ZoneSettingsOverride#minify}
        :param min_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#min_tls_version ZoneSettingsOverride#min_tls_version}.
        :param mirage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mirage ZoneSettingsOverride#mirage}.
        :param mobile_redirect: mobile_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mobile_redirect ZoneSettingsOverride#mobile_redirect}
        :param opportunistic_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#opportunistic_encryption ZoneSettingsOverride#opportunistic_encryption}.
        :param opportunistic_onion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#opportunistic_onion ZoneSettingsOverride#opportunistic_onion}.
        :param orange_to_orange: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#orange_to_orange ZoneSettingsOverride#orange_to_orange}.
        :param origin_error_page_pass_thru: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#origin_error_page_pass_thru ZoneSettingsOverride#origin_error_page_pass_thru}.
        :param origin_max_http_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#origin_max_http_version ZoneSettingsOverride#origin_max_http_version}.
        :param polish: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#polish ZoneSettingsOverride#polish}.
        :param prefetch_preload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#prefetch_preload ZoneSettingsOverride#prefetch_preload}.
        :param privacy_pass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#privacy_pass ZoneSettingsOverride#privacy_pass}.
        :param proxy_read_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#proxy_read_timeout ZoneSettingsOverride#proxy_read_timeout}.
        :param pseudo_ipv4: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#pseudo_ipv4 ZoneSettingsOverride#pseudo_ipv4}.
        :param response_buffering: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#response_buffering ZoneSettingsOverride#response_buffering}.
        :param rocket_loader: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#rocket_loader ZoneSettingsOverride#rocket_loader}.
        :param security_header: security_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#security_header ZoneSettingsOverride#security_header}
        :param security_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#security_level ZoneSettingsOverride#security_level}.
        :param server_side_exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#server_side_exclude ZoneSettingsOverride#server_side_exclude}.
        :param sort_query_string_for_cache: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#sort_query_string_for_cache ZoneSettingsOverride#sort_query_string_for_cache}.
        :param ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ssl ZoneSettingsOverride#ssl}.
        :param tls12_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_1_2_only ZoneSettingsOverride#tls_1_2_only}.
        :param tls13: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_1_3 ZoneSettingsOverride#tls_1_3}.
        :param tls_client_auth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_client_auth ZoneSettingsOverride#tls_client_auth}.
        :param true_client_ip_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#true_client_ip_header ZoneSettingsOverride#true_client_ip_header}.
        :param universal_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#universal_ssl ZoneSettingsOverride#universal_ssl}.
        :param visitor_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#visitor_ip ZoneSettingsOverride#visitor_ip}.
        :param waf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#waf ZoneSettingsOverride#waf}.
        :param webp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#webp ZoneSettingsOverride#webp}.
        :param websockets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#websockets ZoneSettingsOverride#websockets}.
        :param zero_rtt: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#zero_rtt ZoneSettingsOverride#zero_rtt}.
        '''
        if isinstance(minify, dict):
            minify = ZoneSettingsOverrideSettingsMinify(**minify)
        if isinstance(mobile_redirect, dict):
            mobile_redirect = ZoneSettingsOverrideSettingsMobileRedirect(**mobile_redirect)
        if isinstance(security_header, dict):
            security_header = ZoneSettingsOverrideSettingsSecurityHeader(**security_header)
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideSettings.__init__)
            check_type(argname="argument always_online", value=always_online, expected_type=type_hints["always_online"])
            check_type(argname="argument always_use_https", value=always_use_https, expected_type=type_hints["always_use_https"])
            check_type(argname="argument automatic_https_rewrites", value=automatic_https_rewrites, expected_type=type_hints["automatic_https_rewrites"])
            check_type(argname="argument binary_ast", value=binary_ast, expected_type=type_hints["binary_ast"])
            check_type(argname="argument brotli", value=brotli, expected_type=type_hints["brotli"])
            check_type(argname="argument browser_cache_ttl", value=browser_cache_ttl, expected_type=type_hints["browser_cache_ttl"])
            check_type(argname="argument browser_check", value=browser_check, expected_type=type_hints["browser_check"])
            check_type(argname="argument cache_level", value=cache_level, expected_type=type_hints["cache_level"])
            check_type(argname="argument challenge_ttl", value=challenge_ttl, expected_type=type_hints["challenge_ttl"])
            check_type(argname="argument ciphers", value=ciphers, expected_type=type_hints["ciphers"])
            check_type(argname="argument cname_flattening", value=cname_flattening, expected_type=type_hints["cname_flattening"])
            check_type(argname="argument development_mode", value=development_mode, expected_type=type_hints["development_mode"])
            check_type(argname="argument early_hints", value=early_hints, expected_type=type_hints["early_hints"])
            check_type(argname="argument email_obfuscation", value=email_obfuscation, expected_type=type_hints["email_obfuscation"])
            check_type(argname="argument filter_logs_to_cloudflare", value=filter_logs_to_cloudflare, expected_type=type_hints["filter_logs_to_cloudflare"])
            check_type(argname="argument h2_prioritization", value=h2_prioritization, expected_type=type_hints["h2_prioritization"])
            check_type(argname="argument hotlink_protection", value=hotlink_protection, expected_type=type_hints["hotlink_protection"])
            check_type(argname="argument http2", value=http2, expected_type=type_hints["http2"])
            check_type(argname="argument http3", value=http3, expected_type=type_hints["http3"])
            check_type(argname="argument image_resizing", value=image_resizing, expected_type=type_hints["image_resizing"])
            check_type(argname="argument ip_geolocation", value=ip_geolocation, expected_type=type_hints["ip_geolocation"])
            check_type(argname="argument ipv6", value=ipv6, expected_type=type_hints["ipv6"])
            check_type(argname="argument log_to_cloudflare", value=log_to_cloudflare, expected_type=type_hints["log_to_cloudflare"])
            check_type(argname="argument max_upload", value=max_upload, expected_type=type_hints["max_upload"])
            check_type(argname="argument minify", value=minify, expected_type=type_hints["minify"])
            check_type(argname="argument min_tls_version", value=min_tls_version, expected_type=type_hints["min_tls_version"])
            check_type(argname="argument mirage", value=mirage, expected_type=type_hints["mirage"])
            check_type(argname="argument mobile_redirect", value=mobile_redirect, expected_type=type_hints["mobile_redirect"])
            check_type(argname="argument opportunistic_encryption", value=opportunistic_encryption, expected_type=type_hints["opportunistic_encryption"])
            check_type(argname="argument opportunistic_onion", value=opportunistic_onion, expected_type=type_hints["opportunistic_onion"])
            check_type(argname="argument orange_to_orange", value=orange_to_orange, expected_type=type_hints["orange_to_orange"])
            check_type(argname="argument origin_error_page_pass_thru", value=origin_error_page_pass_thru, expected_type=type_hints["origin_error_page_pass_thru"])
            check_type(argname="argument origin_max_http_version", value=origin_max_http_version, expected_type=type_hints["origin_max_http_version"])
            check_type(argname="argument polish", value=polish, expected_type=type_hints["polish"])
            check_type(argname="argument prefetch_preload", value=prefetch_preload, expected_type=type_hints["prefetch_preload"])
            check_type(argname="argument privacy_pass", value=privacy_pass, expected_type=type_hints["privacy_pass"])
            check_type(argname="argument proxy_read_timeout", value=proxy_read_timeout, expected_type=type_hints["proxy_read_timeout"])
            check_type(argname="argument pseudo_ipv4", value=pseudo_ipv4, expected_type=type_hints["pseudo_ipv4"])
            check_type(argname="argument response_buffering", value=response_buffering, expected_type=type_hints["response_buffering"])
            check_type(argname="argument rocket_loader", value=rocket_loader, expected_type=type_hints["rocket_loader"])
            check_type(argname="argument security_header", value=security_header, expected_type=type_hints["security_header"])
            check_type(argname="argument security_level", value=security_level, expected_type=type_hints["security_level"])
            check_type(argname="argument server_side_exclude", value=server_side_exclude, expected_type=type_hints["server_side_exclude"])
            check_type(argname="argument sort_query_string_for_cache", value=sort_query_string_for_cache, expected_type=type_hints["sort_query_string_for_cache"])
            check_type(argname="argument ssl", value=ssl, expected_type=type_hints["ssl"])
            check_type(argname="argument tls12_only", value=tls12_only, expected_type=type_hints["tls12_only"])
            check_type(argname="argument tls13", value=tls13, expected_type=type_hints["tls13"])
            check_type(argname="argument tls_client_auth", value=tls_client_auth, expected_type=type_hints["tls_client_auth"])
            check_type(argname="argument true_client_ip_header", value=true_client_ip_header, expected_type=type_hints["true_client_ip_header"])
            check_type(argname="argument universal_ssl", value=universal_ssl, expected_type=type_hints["universal_ssl"])
            check_type(argname="argument visitor_ip", value=visitor_ip, expected_type=type_hints["visitor_ip"])
            check_type(argname="argument waf", value=waf, expected_type=type_hints["waf"])
            check_type(argname="argument webp", value=webp, expected_type=type_hints["webp"])
            check_type(argname="argument websockets", value=websockets, expected_type=type_hints["websockets"])
            check_type(argname="argument zero_rtt", value=zero_rtt, expected_type=type_hints["zero_rtt"])
        self._values: typing.Dict[str, typing.Any] = {}
        if always_online is not None:
            self._values["always_online"] = always_online
        if always_use_https is not None:
            self._values["always_use_https"] = always_use_https
        if automatic_https_rewrites is not None:
            self._values["automatic_https_rewrites"] = automatic_https_rewrites
        if binary_ast is not None:
            self._values["binary_ast"] = binary_ast
        if brotli is not None:
            self._values["brotli"] = brotli
        if browser_cache_ttl is not None:
            self._values["browser_cache_ttl"] = browser_cache_ttl
        if browser_check is not None:
            self._values["browser_check"] = browser_check
        if cache_level is not None:
            self._values["cache_level"] = cache_level
        if challenge_ttl is not None:
            self._values["challenge_ttl"] = challenge_ttl
        if ciphers is not None:
            self._values["ciphers"] = ciphers
        if cname_flattening is not None:
            self._values["cname_flattening"] = cname_flattening
        if development_mode is not None:
            self._values["development_mode"] = development_mode
        if early_hints is not None:
            self._values["early_hints"] = early_hints
        if email_obfuscation is not None:
            self._values["email_obfuscation"] = email_obfuscation
        if filter_logs_to_cloudflare is not None:
            self._values["filter_logs_to_cloudflare"] = filter_logs_to_cloudflare
        if h2_prioritization is not None:
            self._values["h2_prioritization"] = h2_prioritization
        if hotlink_protection is not None:
            self._values["hotlink_protection"] = hotlink_protection
        if http2 is not None:
            self._values["http2"] = http2
        if http3 is not None:
            self._values["http3"] = http3
        if image_resizing is not None:
            self._values["image_resizing"] = image_resizing
        if ip_geolocation is not None:
            self._values["ip_geolocation"] = ip_geolocation
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if log_to_cloudflare is not None:
            self._values["log_to_cloudflare"] = log_to_cloudflare
        if max_upload is not None:
            self._values["max_upload"] = max_upload
        if minify is not None:
            self._values["minify"] = minify
        if min_tls_version is not None:
            self._values["min_tls_version"] = min_tls_version
        if mirage is not None:
            self._values["mirage"] = mirage
        if mobile_redirect is not None:
            self._values["mobile_redirect"] = mobile_redirect
        if opportunistic_encryption is not None:
            self._values["opportunistic_encryption"] = opportunistic_encryption
        if opportunistic_onion is not None:
            self._values["opportunistic_onion"] = opportunistic_onion
        if orange_to_orange is not None:
            self._values["orange_to_orange"] = orange_to_orange
        if origin_error_page_pass_thru is not None:
            self._values["origin_error_page_pass_thru"] = origin_error_page_pass_thru
        if origin_max_http_version is not None:
            self._values["origin_max_http_version"] = origin_max_http_version
        if polish is not None:
            self._values["polish"] = polish
        if prefetch_preload is not None:
            self._values["prefetch_preload"] = prefetch_preload
        if privacy_pass is not None:
            self._values["privacy_pass"] = privacy_pass
        if proxy_read_timeout is not None:
            self._values["proxy_read_timeout"] = proxy_read_timeout
        if pseudo_ipv4 is not None:
            self._values["pseudo_ipv4"] = pseudo_ipv4
        if response_buffering is not None:
            self._values["response_buffering"] = response_buffering
        if rocket_loader is not None:
            self._values["rocket_loader"] = rocket_loader
        if security_header is not None:
            self._values["security_header"] = security_header
        if security_level is not None:
            self._values["security_level"] = security_level
        if server_side_exclude is not None:
            self._values["server_side_exclude"] = server_side_exclude
        if sort_query_string_for_cache is not None:
            self._values["sort_query_string_for_cache"] = sort_query_string_for_cache
        if ssl is not None:
            self._values["ssl"] = ssl
        if tls12_only is not None:
            self._values["tls12_only"] = tls12_only
        if tls13 is not None:
            self._values["tls13"] = tls13
        if tls_client_auth is not None:
            self._values["tls_client_auth"] = tls_client_auth
        if true_client_ip_header is not None:
            self._values["true_client_ip_header"] = true_client_ip_header
        if universal_ssl is not None:
            self._values["universal_ssl"] = universal_ssl
        if visitor_ip is not None:
            self._values["visitor_ip"] = visitor_ip
        if waf is not None:
            self._values["waf"] = waf
        if webp is not None:
            self._values["webp"] = webp
        if websockets is not None:
            self._values["websockets"] = websockets
        if zero_rtt is not None:
            self._values["zero_rtt"] = zero_rtt

    @builtins.property
    def always_online(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#always_online ZoneSettingsOverride#always_online}.'''
        result = self._values.get("always_online")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def always_use_https(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#always_use_https ZoneSettingsOverride#always_use_https}.'''
        result = self._values.get("always_use_https")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automatic_https_rewrites(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#automatic_https_rewrites ZoneSettingsOverride#automatic_https_rewrites}.'''
        result = self._values.get("automatic_https_rewrites")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def binary_ast(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#binary_ast ZoneSettingsOverride#binary_ast}.'''
        result = self._values.get("binary_ast")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def brotli(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#brotli ZoneSettingsOverride#brotli}.'''
        result = self._values.get("brotli")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def browser_cache_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#browser_cache_ttl ZoneSettingsOverride#browser_cache_ttl}.'''
        result = self._values.get("browser_cache_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def browser_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#browser_check ZoneSettingsOverride#browser_check}.'''
        result = self._values.get("browser_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#cache_level ZoneSettingsOverride#cache_level}.'''
        result = self._values.get("cache_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def challenge_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#challenge_ttl ZoneSettingsOverride#challenge_ttl}.'''
        result = self._values.get("challenge_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ciphers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ciphers ZoneSettingsOverride#ciphers}.'''
        result = self._values.get("ciphers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cname_flattening(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#cname_flattening ZoneSettingsOverride#cname_flattening}.'''
        result = self._values.get("cname_flattening")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def development_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#development_mode ZoneSettingsOverride#development_mode}.'''
        result = self._values.get("development_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def early_hints(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#early_hints ZoneSettingsOverride#early_hints}.'''
        result = self._values.get("early_hints")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_obfuscation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#email_obfuscation ZoneSettingsOverride#email_obfuscation}.'''
        result = self._values.get("email_obfuscation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_logs_to_cloudflare(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#filter_logs_to_cloudflare ZoneSettingsOverride#filter_logs_to_cloudflare}.'''
        result = self._values.get("filter_logs_to_cloudflare")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def h2_prioritization(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#h2_prioritization ZoneSettingsOverride#h2_prioritization}.'''
        result = self._values.get("h2_prioritization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hotlink_protection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#hotlink_protection ZoneSettingsOverride#hotlink_protection}.'''
        result = self._values.get("hotlink_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http2(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#http2 ZoneSettingsOverride#http2}.'''
        result = self._values.get("http2")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http3(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#http3 ZoneSettingsOverride#http3}.'''
        result = self._values.get("http3")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_resizing(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#image_resizing ZoneSettingsOverride#image_resizing}.'''
        result = self._values.get("image_resizing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_geolocation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ip_geolocation ZoneSettingsOverride#ip_geolocation}.'''
        result = self._values.get("ip_geolocation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ipv6 ZoneSettingsOverride#ipv6}.'''
        result = self._values.get("ipv6")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_to_cloudflare(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#log_to_cloudflare ZoneSettingsOverride#log_to_cloudflare}.'''
        result = self._values.get("log_to_cloudflare")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_upload(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#max_upload ZoneSettingsOverride#max_upload}.'''
        result = self._values.get("max_upload")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minify(self) -> typing.Optional["ZoneSettingsOverrideSettingsMinify"]:
        '''minify block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#minify ZoneSettingsOverride#minify}
        '''
        result = self._values.get("minify")
        return typing.cast(typing.Optional["ZoneSettingsOverrideSettingsMinify"], result)

    @builtins.property
    def min_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#min_tls_version ZoneSettingsOverride#min_tls_version}.'''
        result = self._values.get("min_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mirage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mirage ZoneSettingsOverride#mirage}.'''
        result = self._values.get("mirage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile_redirect(
        self,
    ) -> typing.Optional["ZoneSettingsOverrideSettingsMobileRedirect"]:
        '''mobile_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mobile_redirect ZoneSettingsOverride#mobile_redirect}
        '''
        result = self._values.get("mobile_redirect")
        return typing.cast(typing.Optional["ZoneSettingsOverrideSettingsMobileRedirect"], result)

    @builtins.property
    def opportunistic_encryption(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#opportunistic_encryption ZoneSettingsOverride#opportunistic_encryption}.'''
        result = self._values.get("opportunistic_encryption")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opportunistic_onion(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#opportunistic_onion ZoneSettingsOverride#opportunistic_onion}.'''
        result = self._values.get("opportunistic_onion")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def orange_to_orange(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#orange_to_orange ZoneSettingsOverride#orange_to_orange}.'''
        result = self._values.get("orange_to_orange")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_error_page_pass_thru(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#origin_error_page_pass_thru ZoneSettingsOverride#origin_error_page_pass_thru}.'''
        result = self._values.get("origin_error_page_pass_thru")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_max_http_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#origin_max_http_version ZoneSettingsOverride#origin_max_http_version}.'''
        result = self._values.get("origin_max_http_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def polish(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#polish ZoneSettingsOverride#polish}.'''
        result = self._values.get("polish")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefetch_preload(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#prefetch_preload ZoneSettingsOverride#prefetch_preload}.'''
        result = self._values.get("prefetch_preload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def privacy_pass(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#privacy_pass ZoneSettingsOverride#privacy_pass}.'''
        result = self._values.get("privacy_pass")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_read_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#proxy_read_timeout ZoneSettingsOverride#proxy_read_timeout}.'''
        result = self._values.get("proxy_read_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pseudo_ipv4(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#pseudo_ipv4 ZoneSettingsOverride#pseudo_ipv4}.'''
        result = self._values.get("pseudo_ipv4")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_buffering(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#response_buffering ZoneSettingsOverride#response_buffering}.'''
        result = self._values.get("response_buffering")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rocket_loader(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#rocket_loader ZoneSettingsOverride#rocket_loader}.'''
        result = self._values.get("rocket_loader")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_header(
        self,
    ) -> typing.Optional["ZoneSettingsOverrideSettingsSecurityHeader"]:
        '''security_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#security_header ZoneSettingsOverride#security_header}
        '''
        result = self._values.get("security_header")
        return typing.cast(typing.Optional["ZoneSettingsOverrideSettingsSecurityHeader"], result)

    @builtins.property
    def security_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#security_level ZoneSettingsOverride#security_level}.'''
        result = self._values.get("security_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_exclude(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#server_side_exclude ZoneSettingsOverride#server_side_exclude}.'''
        result = self._values.get("server_side_exclude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort_query_string_for_cache(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#sort_query_string_for_cache ZoneSettingsOverride#sort_query_string_for_cache}.'''
        result = self._values.get("sort_query_string_for_cache")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#ssl ZoneSettingsOverride#ssl}.'''
        result = self._values.get("ssl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls12_only(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_1_2_only ZoneSettingsOverride#tls_1_2_only}.'''
        result = self._values.get("tls12_only")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls13(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_1_3 ZoneSettingsOverride#tls_1_3}.'''
        result = self._values.get("tls13")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_client_auth(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#tls_client_auth ZoneSettingsOverride#tls_client_auth}.'''
        result = self._values.get("tls_client_auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def true_client_ip_header(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#true_client_ip_header ZoneSettingsOverride#true_client_ip_header}.'''
        result = self._values.get("true_client_ip_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def universal_ssl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#universal_ssl ZoneSettingsOverride#universal_ssl}.'''
        result = self._values.get("universal_ssl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visitor_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#visitor_ip ZoneSettingsOverride#visitor_ip}.'''
        result = self._values.get("visitor_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def waf(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#waf ZoneSettingsOverride#waf}.'''
        result = self._values.get("waf")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webp(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#webp ZoneSettingsOverride#webp}.'''
        result = self._values.get("webp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def websockets(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#websockets ZoneSettingsOverride#websockets}.'''
        result = self._values.get("websockets")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zero_rtt(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#zero_rtt ZoneSettingsOverride#zero_rtt}.'''
        result = self._values.get("zero_rtt")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideSettingsMinify",
    jsii_struct_bases=[],
    name_mapping={"css": "css", "html": "html", "js": "js"},
)
class ZoneSettingsOverrideSettingsMinify:
    def __init__(
        self,
        *,
        css: builtins.str,
        html: builtins.str,
        js: builtins.str,
    ) -> None:
        '''
        :param css: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#css ZoneSettingsOverride#css}.
        :param html: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#html ZoneSettingsOverride#html}.
        :param js: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#js ZoneSettingsOverride#js}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideSettingsMinify.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#css ZoneSettingsOverride#css}.'''
        result = self._values.get("css")
        assert result is not None, "Required property 'css' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def html(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#html ZoneSettingsOverride#html}.'''
        result = self._values.get("html")
        assert result is not None, "Required property 'html' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def js(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#js ZoneSettingsOverride#js}.'''
        result = self._values.get("js")
        assert result is not None, "Required property 'js' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideSettingsMinify(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneSettingsOverrideSettingsMinifyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideSettingsMinifyOutputReference",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideSettingsMinifyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsMinifyOutputReference, "css").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "css", value)

    @builtins.property
    @jsii.member(jsii_name="html")
    def html(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "html"))

    @html.setter
    def html(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsMinifyOutputReference, "html").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "html", value)

    @builtins.property
    @jsii.member(jsii_name="js")
    def js(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "js"))

    @js.setter
    def js(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsMinifyOutputReference, "js").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "js", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ZoneSettingsOverrideSettingsMinify]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideSettingsMinify], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ZoneSettingsOverrideSettingsMinify],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsMinifyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideSettingsMobileRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "mobile_subdomain": "mobileSubdomain",
        "status": "status",
        "strip_uri": "stripUri",
    },
)
class ZoneSettingsOverrideSettingsMobileRedirect:
    def __init__(
        self,
        *,
        mobile_subdomain: builtins.str,
        status: builtins.str,
        strip_uri: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param mobile_subdomain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mobile_subdomain ZoneSettingsOverride#mobile_subdomain}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#status ZoneSettingsOverride#status}.
        :param strip_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#strip_uri ZoneSettingsOverride#strip_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideSettingsMobileRedirect.__init__)
            check_type(argname="argument mobile_subdomain", value=mobile_subdomain, expected_type=type_hints["mobile_subdomain"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument strip_uri", value=strip_uri, expected_type=type_hints["strip_uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "mobile_subdomain": mobile_subdomain,
            "status": status,
            "strip_uri": strip_uri,
        }

    @builtins.property
    def mobile_subdomain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mobile_subdomain ZoneSettingsOverride#mobile_subdomain}.'''
        result = self._values.get("mobile_subdomain")
        assert result is not None, "Required property 'mobile_subdomain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#status ZoneSettingsOverride#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def strip_uri(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#strip_uri ZoneSettingsOverride#strip_uri}.'''
        result = self._values.get("strip_uri")
        assert result is not None, "Required property 'strip_uri' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideSettingsMobileRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneSettingsOverrideSettingsMobileRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideSettingsMobileRedirectOutputReference",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideSettingsMobileRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="mobileSubdomainInput")
    def mobile_subdomain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mobileSubdomainInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="stripUriInput")
    def strip_uri_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripUriInput"))

    @builtins.property
    @jsii.member(jsii_name="mobileSubdomain")
    def mobile_subdomain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mobileSubdomain"))

    @mobile_subdomain.setter
    def mobile_subdomain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsMobileRedirectOutputReference, "mobile_subdomain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mobileSubdomain", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsMobileRedirectOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="stripUri")
    def strip_uri(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripUri"))

    @strip_uri.setter
    def strip_uri(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsMobileRedirectOutputReference, "strip_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ZoneSettingsOverrideSettingsMobileRedirect]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideSettingsMobileRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ZoneSettingsOverrideSettingsMobileRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsMobileRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ZoneSettingsOverrideSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideSettingsOutputReference",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMinify")
    def put_minify(
        self,
        *,
        css: builtins.str,
        html: builtins.str,
        js: builtins.str,
    ) -> None:
        '''
        :param css: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#css ZoneSettingsOverride#css}.
        :param html: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#html ZoneSettingsOverride#html}.
        :param js: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#js ZoneSettingsOverride#js}.
        '''
        value = ZoneSettingsOverrideSettingsMinify(css=css, html=html, js=js)

        return typing.cast(None, jsii.invoke(self, "putMinify", [value]))

    @jsii.member(jsii_name="putMobileRedirect")
    def put_mobile_redirect(
        self,
        *,
        mobile_subdomain: builtins.str,
        status: builtins.str,
        strip_uri: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param mobile_subdomain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#mobile_subdomain ZoneSettingsOverride#mobile_subdomain}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#status ZoneSettingsOverride#status}.
        :param strip_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#strip_uri ZoneSettingsOverride#strip_uri}.
        '''
        value = ZoneSettingsOverrideSettingsMobileRedirect(
            mobile_subdomain=mobile_subdomain, status=status, strip_uri=strip_uri
        )

        return typing.cast(None, jsii.invoke(self, "putMobileRedirect", [value]))

    @jsii.member(jsii_name="putSecurityHeader")
    def put_security_header(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_subdomains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_age: typing.Optional[jsii.Number] = None,
        nosniff: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preload: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#enabled ZoneSettingsOverride#enabled}.
        :param include_subdomains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#include_subdomains ZoneSettingsOverride#include_subdomains}.
        :param max_age: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#max_age ZoneSettingsOverride#max_age}.
        :param nosniff: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#nosniff ZoneSettingsOverride#nosniff}.
        :param preload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#preload ZoneSettingsOverride#preload}.
        '''
        value = ZoneSettingsOverrideSettingsSecurityHeader(
            enabled=enabled,
            include_subdomains=include_subdomains,
            max_age=max_age,
            nosniff=nosniff,
            preload=preload,
        )

        return typing.cast(None, jsii.invoke(self, "putSecurityHeader", [value]))

    @jsii.member(jsii_name="resetAlwaysOnline")
    def reset_always_online(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlwaysOnline", []))

    @jsii.member(jsii_name="resetAlwaysUseHttps")
    def reset_always_use_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlwaysUseHttps", []))

    @jsii.member(jsii_name="resetAutomaticHttpsRewrites")
    def reset_automatic_https_rewrites(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticHttpsRewrites", []))

    @jsii.member(jsii_name="resetBinaryAst")
    def reset_binary_ast(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBinaryAst", []))

    @jsii.member(jsii_name="resetBrotli")
    def reset_brotli(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrotli", []))

    @jsii.member(jsii_name="resetBrowserCacheTtl")
    def reset_browser_cache_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserCacheTtl", []))

    @jsii.member(jsii_name="resetBrowserCheck")
    def reset_browser_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserCheck", []))

    @jsii.member(jsii_name="resetCacheLevel")
    def reset_cache_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheLevel", []))

    @jsii.member(jsii_name="resetChallengeTtl")
    def reset_challenge_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChallengeTtl", []))

    @jsii.member(jsii_name="resetCiphers")
    def reset_ciphers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCiphers", []))

    @jsii.member(jsii_name="resetCnameFlattening")
    def reset_cname_flattening(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCnameFlattening", []))

    @jsii.member(jsii_name="resetDevelopmentMode")
    def reset_development_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevelopmentMode", []))

    @jsii.member(jsii_name="resetEarlyHints")
    def reset_early_hints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEarlyHints", []))

    @jsii.member(jsii_name="resetEmailObfuscation")
    def reset_email_obfuscation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailObfuscation", []))

    @jsii.member(jsii_name="resetFilterLogsToCloudflare")
    def reset_filter_logs_to_cloudflare(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterLogsToCloudflare", []))

    @jsii.member(jsii_name="resetH2Prioritization")
    def reset_h2_prioritization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetH2Prioritization", []))

    @jsii.member(jsii_name="resetHotlinkProtection")
    def reset_hotlink_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHotlinkProtection", []))

    @jsii.member(jsii_name="resetHttp2")
    def reset_http2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2", []))

    @jsii.member(jsii_name="resetHttp3")
    def reset_http3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp3", []))

    @jsii.member(jsii_name="resetImageResizing")
    def reset_image_resizing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageResizing", []))

    @jsii.member(jsii_name="resetIpGeolocation")
    def reset_ip_geolocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpGeolocation", []))

    @jsii.member(jsii_name="resetIpv6")
    def reset_ipv6(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6", []))

    @jsii.member(jsii_name="resetLogToCloudflare")
    def reset_log_to_cloudflare(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogToCloudflare", []))

    @jsii.member(jsii_name="resetMaxUpload")
    def reset_max_upload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUpload", []))

    @jsii.member(jsii_name="resetMinify")
    def reset_minify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinify", []))

    @jsii.member(jsii_name="resetMinTlsVersion")
    def reset_min_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTlsVersion", []))

    @jsii.member(jsii_name="resetMirage")
    def reset_mirage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMirage", []))

    @jsii.member(jsii_name="resetMobileRedirect")
    def reset_mobile_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMobileRedirect", []))

    @jsii.member(jsii_name="resetOpportunisticEncryption")
    def reset_opportunistic_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpportunisticEncryption", []))

    @jsii.member(jsii_name="resetOpportunisticOnion")
    def reset_opportunistic_onion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpportunisticOnion", []))

    @jsii.member(jsii_name="resetOrangeToOrange")
    def reset_orange_to_orange(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrangeToOrange", []))

    @jsii.member(jsii_name="resetOriginErrorPagePassThru")
    def reset_origin_error_page_pass_thru(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginErrorPagePassThru", []))

    @jsii.member(jsii_name="resetOriginMaxHttpVersion")
    def reset_origin_max_http_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginMaxHttpVersion", []))

    @jsii.member(jsii_name="resetPolish")
    def reset_polish(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolish", []))

    @jsii.member(jsii_name="resetPrefetchPreload")
    def reset_prefetch_preload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefetchPreload", []))

    @jsii.member(jsii_name="resetPrivacyPass")
    def reset_privacy_pass(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivacyPass", []))

    @jsii.member(jsii_name="resetProxyReadTimeout")
    def reset_proxy_read_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyReadTimeout", []))

    @jsii.member(jsii_name="resetPseudoIpv4")
    def reset_pseudo_ipv4(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPseudoIpv4", []))

    @jsii.member(jsii_name="resetResponseBuffering")
    def reset_response_buffering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseBuffering", []))

    @jsii.member(jsii_name="resetRocketLoader")
    def reset_rocket_loader(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRocketLoader", []))

    @jsii.member(jsii_name="resetSecurityHeader")
    def reset_security_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityHeader", []))

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

    @jsii.member(jsii_name="resetTls12Only")
    def reset_tls12_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls12Only", []))

    @jsii.member(jsii_name="resetTls13")
    def reset_tls13(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls13", []))

    @jsii.member(jsii_name="resetTlsClientAuth")
    def reset_tls_client_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsClientAuth", []))

    @jsii.member(jsii_name="resetTrueClientIpHeader")
    def reset_true_client_ip_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrueClientIpHeader", []))

    @jsii.member(jsii_name="resetUniversalSsl")
    def reset_universal_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUniversalSsl", []))

    @jsii.member(jsii_name="resetVisitorIp")
    def reset_visitor_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisitorIp", []))

    @jsii.member(jsii_name="resetWaf")
    def reset_waf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaf", []))

    @jsii.member(jsii_name="resetWebp")
    def reset_webp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebp", []))

    @jsii.member(jsii_name="resetWebsockets")
    def reset_websockets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebsockets", []))

    @jsii.member(jsii_name="resetZeroRtt")
    def reset_zero_rtt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZeroRtt", []))

    @builtins.property
    @jsii.member(jsii_name="minify")
    def minify(self) -> ZoneSettingsOverrideSettingsMinifyOutputReference:
        return typing.cast(ZoneSettingsOverrideSettingsMinifyOutputReference, jsii.get(self, "minify"))

    @builtins.property
    @jsii.member(jsii_name="mobileRedirect")
    def mobile_redirect(
        self,
    ) -> ZoneSettingsOverrideSettingsMobileRedirectOutputReference:
        return typing.cast(ZoneSettingsOverrideSettingsMobileRedirectOutputReference, jsii.get(self, "mobileRedirect"))

    @builtins.property
    @jsii.member(jsii_name="securityHeader")
    def security_header(
        self,
    ) -> "ZoneSettingsOverrideSettingsSecurityHeaderOutputReference":
        return typing.cast("ZoneSettingsOverrideSettingsSecurityHeaderOutputReference", jsii.get(self, "securityHeader"))

    @builtins.property
    @jsii.member(jsii_name="alwaysOnlineInput")
    def always_online_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alwaysOnlineInput"))

    @builtins.property
    @jsii.member(jsii_name="alwaysUseHttpsInput")
    def always_use_https_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alwaysUseHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewritesInput")
    def automatic_https_rewrites_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automaticHttpsRewritesInput"))

    @builtins.property
    @jsii.member(jsii_name="binaryAstInput")
    def binary_ast_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "binaryAstInput"))

    @builtins.property
    @jsii.member(jsii_name="brotliInput")
    def brotli_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "brotliInput"))

    @builtins.property
    @jsii.member(jsii_name="browserCacheTtlInput")
    def browser_cache_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "browserCacheTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="browserCheckInput")
    def browser_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "browserCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheLevelInput")
    def cache_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="challengeTtlInput")
    def challenge_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "challengeTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="ciphersInput")
    def ciphers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ciphersInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameFlatteningInput")
    def cname_flattening_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameFlatteningInput"))

    @builtins.property
    @jsii.member(jsii_name="developmentModeInput")
    def development_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "developmentModeInput"))

    @builtins.property
    @jsii.member(jsii_name="earlyHintsInput")
    def early_hints_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "earlyHintsInput"))

    @builtins.property
    @jsii.member(jsii_name="emailObfuscationInput")
    def email_obfuscation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailObfuscationInput"))

    @builtins.property
    @jsii.member(jsii_name="filterLogsToCloudflareInput")
    def filter_logs_to_cloudflare_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterLogsToCloudflareInput"))

    @builtins.property
    @jsii.member(jsii_name="h2PrioritizationInput")
    def h2_prioritization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "h2PrioritizationInput"))

    @builtins.property
    @jsii.member(jsii_name="hotlinkProtectionInput")
    def hotlink_protection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hotlinkProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="http2Input")
    def http2_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "http2Input"))

    @builtins.property
    @jsii.member(jsii_name="http3Input")
    def http3_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "http3Input"))

    @builtins.property
    @jsii.member(jsii_name="imageResizingInput")
    def image_resizing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageResizingInput"))

    @builtins.property
    @jsii.member(jsii_name="ipGeolocationInput")
    def ip_geolocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipGeolocationInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6Input")
    def ipv6_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6Input"))

    @builtins.property
    @jsii.member(jsii_name="logToCloudflareInput")
    def log_to_cloudflare_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logToCloudflareInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUploadInput")
    def max_upload_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUploadInput"))

    @builtins.property
    @jsii.member(jsii_name="minifyInput")
    def minify_input(self) -> typing.Optional[ZoneSettingsOverrideSettingsMinify]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideSettingsMinify], jsii.get(self, "minifyInput"))

    @builtins.property
    @jsii.member(jsii_name="minTlsVersionInput")
    def min_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="mirageInput")
    def mirage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mirageInput"))

    @builtins.property
    @jsii.member(jsii_name="mobileRedirectInput")
    def mobile_redirect_input(
        self,
    ) -> typing.Optional[ZoneSettingsOverrideSettingsMobileRedirect]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideSettingsMobileRedirect], jsii.get(self, "mobileRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryptionInput")
    def opportunistic_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opportunisticEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="opportunisticOnionInput")
    def opportunistic_onion_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opportunisticOnionInput"))

    @builtins.property
    @jsii.member(jsii_name="orangeToOrangeInput")
    def orange_to_orange_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orangeToOrangeInput"))

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassThruInput")
    def origin_error_page_pass_thru_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originErrorPagePassThruInput"))

    @builtins.property
    @jsii.member(jsii_name="originMaxHttpVersionInput")
    def origin_max_http_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originMaxHttpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="polishInput")
    def polish_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "polishInput"))

    @builtins.property
    @jsii.member(jsii_name="prefetchPreloadInput")
    def prefetch_preload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefetchPreloadInput"))

    @builtins.property
    @jsii.member(jsii_name="privacyPassInput")
    def privacy_pass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privacyPassInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyReadTimeoutInput")
    def proxy_read_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyReadTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="pseudoIpv4Input")
    def pseudo_ipv4_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pseudoIpv4Input"))

    @builtins.property
    @jsii.member(jsii_name="responseBufferingInput")
    def response_buffering_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseBufferingInput"))

    @builtins.property
    @jsii.member(jsii_name="rocketLoaderInput")
    def rocket_loader_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rocketLoaderInput"))

    @builtins.property
    @jsii.member(jsii_name="securityHeaderInput")
    def security_header_input(
        self,
    ) -> typing.Optional["ZoneSettingsOverrideSettingsSecurityHeader"]:
        return typing.cast(typing.Optional["ZoneSettingsOverrideSettingsSecurityHeader"], jsii.get(self, "securityHeaderInput"))

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
    @jsii.member(jsii_name="tls12OnlyInput")
    def tls12_only_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tls12OnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="tls13Input")
    def tls13_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tls13Input"))

    @builtins.property
    @jsii.member(jsii_name="tlsClientAuthInput")
    def tls_client_auth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsClientAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="trueClientIpHeaderInput")
    def true_client_ip_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trueClientIpHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="universalSslInput")
    def universal_ssl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "universalSslInput"))

    @builtins.property
    @jsii.member(jsii_name="visitorIpInput")
    def visitor_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visitorIpInput"))

    @builtins.property
    @jsii.member(jsii_name="wafInput")
    def waf_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "wafInput"))

    @builtins.property
    @jsii.member(jsii_name="webpInput")
    def webp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webpInput"))

    @builtins.property
    @jsii.member(jsii_name="websocketsInput")
    def websockets_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "websocketsInput"))

    @builtins.property
    @jsii.member(jsii_name="zeroRttInput")
    def zero_rtt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zeroRttInput"))

    @builtins.property
    @jsii.member(jsii_name="alwaysOnline")
    def always_online(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alwaysOnline"))

    @always_online.setter
    def always_online(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "always_online").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysOnline", value)

    @builtins.property
    @jsii.member(jsii_name="alwaysUseHttps")
    def always_use_https(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alwaysUseHttps"))

    @always_use_https.setter
    def always_use_https(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "always_use_https").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysUseHttps", value)

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewrites")
    def automatic_https_rewrites(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "automaticHttpsRewrites"))

    @automatic_https_rewrites.setter
    def automatic_https_rewrites(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "automatic_https_rewrites").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticHttpsRewrites", value)

    @builtins.property
    @jsii.member(jsii_name="binaryAst")
    def binary_ast(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "binaryAst"))

    @binary_ast.setter
    def binary_ast(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "binary_ast").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "binaryAst", value)

    @builtins.property
    @jsii.member(jsii_name="brotli")
    def brotli(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "brotli"))

    @brotli.setter
    def brotli(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "brotli").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "brotli", value)

    @builtins.property
    @jsii.member(jsii_name="browserCacheTtl")
    def browser_cache_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "browserCacheTtl"))

    @browser_cache_ttl.setter
    def browser_cache_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "browser_cache_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserCacheTtl", value)

    @builtins.property
    @jsii.member(jsii_name="browserCheck")
    def browser_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserCheck"))

    @browser_check.setter
    def browser_check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "browser_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserCheck", value)

    @builtins.property
    @jsii.member(jsii_name="cacheLevel")
    def cache_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheLevel"))

    @cache_level.setter
    def cache_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "cache_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheLevel", value)

    @builtins.property
    @jsii.member(jsii_name="challengeTtl")
    def challenge_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "challengeTtl"))

    @challenge_ttl.setter
    def challenge_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "challenge_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "challengeTtl", value)

    @builtins.property
    @jsii.member(jsii_name="ciphers")
    def ciphers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ciphers"))

    @ciphers.setter
    def ciphers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "ciphers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ciphers", value)

    @builtins.property
    @jsii.member(jsii_name="cnameFlattening")
    def cname_flattening(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cnameFlattening"))

    @cname_flattening.setter
    def cname_flattening(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "cname_flattening").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cnameFlattening", value)

    @builtins.property
    @jsii.member(jsii_name="developmentMode")
    def development_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "developmentMode"))

    @development_mode.setter
    def development_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "development_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "developmentMode", value)

    @builtins.property
    @jsii.member(jsii_name="earlyHints")
    def early_hints(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "earlyHints"))

    @early_hints.setter
    def early_hints(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "early_hints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "earlyHints", value)

    @builtins.property
    @jsii.member(jsii_name="emailObfuscation")
    def email_obfuscation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailObfuscation"))

    @email_obfuscation.setter
    def email_obfuscation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "email_obfuscation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailObfuscation", value)

    @builtins.property
    @jsii.member(jsii_name="filterLogsToCloudflare")
    def filter_logs_to_cloudflare(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterLogsToCloudflare"))

    @filter_logs_to_cloudflare.setter
    def filter_logs_to_cloudflare(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "filter_logs_to_cloudflare").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterLogsToCloudflare", value)

    @builtins.property
    @jsii.member(jsii_name="h2Prioritization")
    def h2_prioritization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "h2Prioritization"))

    @h2_prioritization.setter
    def h2_prioritization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "h2_prioritization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "h2Prioritization", value)

    @builtins.property
    @jsii.member(jsii_name="hotlinkProtection")
    def hotlink_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hotlinkProtection"))

    @hotlink_protection.setter
    def hotlink_protection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "hotlink_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hotlinkProtection", value)

    @builtins.property
    @jsii.member(jsii_name="http2")
    def http2(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "http2"))

    @http2.setter
    def http2(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "http2").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "http2", value)

    @builtins.property
    @jsii.member(jsii_name="http3")
    def http3(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "http3"))

    @http3.setter
    def http3(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "http3").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "http3", value)

    @builtins.property
    @jsii.member(jsii_name="imageResizing")
    def image_resizing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageResizing"))

    @image_resizing.setter
    def image_resizing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "image_resizing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageResizing", value)

    @builtins.property
    @jsii.member(jsii_name="ipGeolocation")
    def ip_geolocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipGeolocation"))

    @ip_geolocation.setter
    def ip_geolocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "ip_geolocation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipGeolocation", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6"))

    @ipv6.setter
    def ipv6(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "ipv6").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6", value)

    @builtins.property
    @jsii.member(jsii_name="logToCloudflare")
    def log_to_cloudflare(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logToCloudflare"))

    @log_to_cloudflare.setter
    def log_to_cloudflare(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "log_to_cloudflare").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logToCloudflare", value)

    @builtins.property
    @jsii.member(jsii_name="maxUpload")
    def max_upload(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUpload"))

    @max_upload.setter
    def max_upload(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "max_upload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUpload", value)

    @builtins.property
    @jsii.member(jsii_name="minTlsVersion")
    def min_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTlsVersion"))

    @min_tls_version.setter
    def min_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "min_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="mirage")
    def mirage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mirage"))

    @mirage.setter
    def mirage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "mirage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mirage", value)

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryption")
    def opportunistic_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opportunisticEncryption"))

    @opportunistic_encryption.setter
    def opportunistic_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "opportunistic_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opportunisticEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="opportunisticOnion")
    def opportunistic_onion(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opportunisticOnion"))

    @opportunistic_onion.setter
    def opportunistic_onion(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "opportunistic_onion").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opportunisticOnion", value)

    @builtins.property
    @jsii.member(jsii_name="orangeToOrange")
    def orange_to_orange(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orangeToOrange"))

    @orange_to_orange.setter
    def orange_to_orange(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "orange_to_orange").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orangeToOrange", value)

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassThru")
    def origin_error_page_pass_thru(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originErrorPagePassThru"))

    @origin_error_page_pass_thru.setter
    def origin_error_page_pass_thru(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "origin_error_page_pass_thru").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originErrorPagePassThru", value)

    @builtins.property
    @jsii.member(jsii_name="originMaxHttpVersion")
    def origin_max_http_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originMaxHttpVersion"))

    @origin_max_http_version.setter
    def origin_max_http_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "origin_max_http_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originMaxHttpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="polish")
    def polish(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "polish"))

    @polish.setter
    def polish(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "polish").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "polish", value)

    @builtins.property
    @jsii.member(jsii_name="prefetchPreload")
    def prefetch_preload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefetchPreload"))

    @prefetch_preload.setter
    def prefetch_preload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "prefetch_preload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefetchPreload", value)

    @builtins.property
    @jsii.member(jsii_name="privacyPass")
    def privacy_pass(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privacyPass"))

    @privacy_pass.setter
    def privacy_pass(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "privacy_pass").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privacyPass", value)

    @builtins.property
    @jsii.member(jsii_name="proxyReadTimeout")
    def proxy_read_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyReadTimeout"))

    @proxy_read_timeout.setter
    def proxy_read_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "proxy_read_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyReadTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="pseudoIpv4")
    def pseudo_ipv4(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pseudoIpv4"))

    @pseudo_ipv4.setter
    def pseudo_ipv4(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "pseudo_ipv4").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pseudoIpv4", value)

    @builtins.property
    @jsii.member(jsii_name="responseBuffering")
    def response_buffering(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseBuffering"))

    @response_buffering.setter
    def response_buffering(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "response_buffering").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseBuffering", value)

    @builtins.property
    @jsii.member(jsii_name="rocketLoader")
    def rocket_loader(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rocketLoader"))

    @rocket_loader.setter
    def rocket_loader(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "rocket_loader").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rocketLoader", value)

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityLevel"))

    @security_level.setter
    def security_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "security_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideExclude")
    def server_side_exclude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideExclude"))

    @server_side_exclude.setter
    def server_side_exclude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "server_side_exclude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideExclude", value)

    @builtins.property
    @jsii.member(jsii_name="sortQueryStringForCache")
    def sort_query_string_for_cache(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sortQueryStringForCache"))

    @sort_query_string_for_cache.setter
    def sort_query_string_for_cache(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "sort_query_string_for_cache").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortQueryStringForCache", value)

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssl"))

    @ssl.setter
    def ssl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssl", value)

    @builtins.property
    @jsii.member(jsii_name="tls12Only")
    def tls12_only(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tls12Only"))

    @tls12_only.setter
    def tls12_only(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "tls12_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls12Only", value)

    @builtins.property
    @jsii.member(jsii_name="tls13")
    def tls13(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tls13"))

    @tls13.setter
    def tls13(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "tls13").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls13", value)

    @builtins.property
    @jsii.member(jsii_name="tlsClientAuth")
    def tls_client_auth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsClientAuth"))

    @tls_client_auth.setter
    def tls_client_auth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "tls_client_auth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsClientAuth", value)

    @builtins.property
    @jsii.member(jsii_name="trueClientIpHeader")
    def true_client_ip_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trueClientIpHeader"))

    @true_client_ip_header.setter
    def true_client_ip_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "true_client_ip_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trueClientIpHeader", value)

    @builtins.property
    @jsii.member(jsii_name="universalSsl")
    def universal_ssl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "universalSsl"))

    @universal_ssl.setter
    def universal_ssl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "universal_ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "universalSsl", value)

    @builtins.property
    @jsii.member(jsii_name="visitorIp")
    def visitor_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visitorIp"))

    @visitor_ip.setter
    def visitor_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "visitor_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visitorIp", value)

    @builtins.property
    @jsii.member(jsii_name="waf")
    def waf(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waf"))

    @waf.setter
    def waf(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "waf").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waf", value)

    @builtins.property
    @jsii.member(jsii_name="webp")
    def webp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webp"))

    @webp.setter
    def webp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "webp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webp", value)

    @builtins.property
    @jsii.member(jsii_name="websockets")
    def websockets(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "websockets"))

    @websockets.setter
    def websockets(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "websockets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "websockets", value)

    @builtins.property
    @jsii.member(jsii_name="zeroRtt")
    def zero_rtt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zeroRtt"))

    @zero_rtt.setter
    def zero_rtt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "zero_rtt").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zeroRtt", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ZoneSettingsOverrideSettings]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ZoneSettingsOverrideSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideSettingsSecurityHeader",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "include_subdomains": "includeSubdomains",
        "max_age": "maxAge",
        "nosniff": "nosniff",
        "preload": "preload",
    },
)
class ZoneSettingsOverrideSettingsSecurityHeader:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_subdomains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_age: typing.Optional[jsii.Number] = None,
        nosniff: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preload: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#enabled ZoneSettingsOverride#enabled}.
        :param include_subdomains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#include_subdomains ZoneSettingsOverride#include_subdomains}.
        :param max_age: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#max_age ZoneSettingsOverride#max_age}.
        :param nosniff: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#nosniff ZoneSettingsOverride#nosniff}.
        :param preload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#preload ZoneSettingsOverride#preload}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ZoneSettingsOverrideSettingsSecurityHeader.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument include_subdomains", value=include_subdomains, expected_type=type_hints["include_subdomains"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
            check_type(argname="argument nosniff", value=nosniff, expected_type=type_hints["nosniff"])
            check_type(argname="argument preload", value=preload, expected_type=type_hints["preload"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if include_subdomains is not None:
            self._values["include_subdomains"] = include_subdomains
        if max_age is not None:
            self._values["max_age"] = max_age
        if nosniff is not None:
            self._values["nosniff"] = nosniff
        if preload is not None:
            self._values["preload"] = preload

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#enabled ZoneSettingsOverride#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_subdomains(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#include_subdomains ZoneSettingsOverride#include_subdomains}.'''
        result = self._values.get("include_subdomains")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#max_age ZoneSettingsOverride#max_age}.'''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nosniff(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#nosniff ZoneSettingsOverride#nosniff}.'''
        result = self._values.get("nosniff")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def preload(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/zone_settings_override#preload ZoneSettingsOverride#preload}.'''
        result = self._values.get("preload")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSettingsOverrideSettingsSecurityHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneSettingsOverrideSettingsSecurityHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.zoneSettingsOverride.ZoneSettingsOverrideSettingsSecurityHeaderOutputReference",
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
            type_hints = typing.get_type_hints(ZoneSettingsOverrideSettingsSecurityHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetIncludeSubdomains")
    def reset_include_subdomains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSubdomains", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @jsii.member(jsii_name="resetNosniff")
    def reset_nosniff(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNosniff", []))

    @jsii.member(jsii_name="resetPreload")
    def reset_preload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreload", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="includeSubdomainsInput")
    def include_subdomains_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeSubdomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="nosniffInput")
    def nosniff_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "nosniffInput"))

    @builtins.property
    @jsii.member(jsii_name="preloadInput")
    def preload_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preloadInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsSecurityHeaderOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="includeSubdomains")
    def include_subdomains(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeSubdomains"))

    @include_subdomains.setter
    def include_subdomains(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsSecurityHeaderOutputReference, "include_subdomains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeSubdomains", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsSecurityHeaderOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="nosniff")
    def nosniff(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "nosniff"))

    @nosniff.setter
    def nosniff(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsSecurityHeaderOutputReference, "nosniff").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nosniff", value)

    @builtins.property
    @jsii.member(jsii_name="preload")
    def preload(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preload"))

    @preload.setter
    def preload(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsSecurityHeaderOutputReference, "preload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ZoneSettingsOverrideSettingsSecurityHeader]:
        return typing.cast(typing.Optional[ZoneSettingsOverrideSettingsSecurityHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ZoneSettingsOverrideSettingsSecurityHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ZoneSettingsOverrideSettingsSecurityHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ZoneSettingsOverride",
    "ZoneSettingsOverrideConfig",
    "ZoneSettingsOverrideInitialSettings",
    "ZoneSettingsOverrideInitialSettingsList",
    "ZoneSettingsOverrideInitialSettingsMinify",
    "ZoneSettingsOverrideInitialSettingsMinifyList",
    "ZoneSettingsOverrideInitialSettingsMinifyOutputReference",
    "ZoneSettingsOverrideInitialSettingsMobileRedirect",
    "ZoneSettingsOverrideInitialSettingsMobileRedirectList",
    "ZoneSettingsOverrideInitialSettingsMobileRedirectOutputReference",
    "ZoneSettingsOverrideInitialSettingsOutputReference",
    "ZoneSettingsOverrideInitialSettingsSecurityHeader",
    "ZoneSettingsOverrideInitialSettingsSecurityHeaderList",
    "ZoneSettingsOverrideInitialSettingsSecurityHeaderOutputReference",
    "ZoneSettingsOverrideSettings",
    "ZoneSettingsOverrideSettingsMinify",
    "ZoneSettingsOverrideSettingsMinifyOutputReference",
    "ZoneSettingsOverrideSettingsMobileRedirect",
    "ZoneSettingsOverrideSettingsMobileRedirectOutputReference",
    "ZoneSettingsOverrideSettingsOutputReference",
    "ZoneSettingsOverrideSettingsSecurityHeader",
    "ZoneSettingsOverrideSettingsSecurityHeaderOutputReference",
]

publication.publish()
