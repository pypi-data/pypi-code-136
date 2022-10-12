'''
# `azurerm_cdn_frontdoor_route`

Refer to the Terraform Registory for docs: [`azurerm_cdn_frontdoor_route`](https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route).
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


class CdnFrontdoorRoute(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRoute.CdnFrontdoorRoute",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route azurerm_cdn_frontdoor_route}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cdn_frontdoor_endpoint_id: builtins.str,
        cdn_frontdoor_origin_group_id: builtins.str,
        cdn_frontdoor_origin_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        patterns_to_match: typing.Sequence[builtins.str],
        supported_protocols: typing.Sequence[builtins.str],
        cache: typing.Optional[typing.Union["CdnFrontdoorRouteCache", typing.Dict[str, typing.Any]]] = None,
        cdn_frontdoor_origin_path: typing.Optional[builtins.str] = None,
        cdn_frontdoor_rule_set_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_protocol: typing.Optional[builtins.str] = None,
        https_redirect_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorRouteTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route azurerm_cdn_frontdoor_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cdn_frontdoor_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_endpoint_id CdnFrontdoorRoute#cdn_frontdoor_endpoint_id}.
        :param cdn_frontdoor_origin_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_group_id CdnFrontdoorRoute#cdn_frontdoor_origin_group_id}.
        :param cdn_frontdoor_origin_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_ids CdnFrontdoorRoute#cdn_frontdoor_origin_ids}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#name CdnFrontdoorRoute#name}.
        :param patterns_to_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#patterns_to_match CdnFrontdoorRoute#patterns_to_match}.
        :param supported_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#supported_protocols CdnFrontdoorRoute#supported_protocols}.
        :param cache: cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cache CdnFrontdoorRoute#cache}
        :param cdn_frontdoor_origin_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_path CdnFrontdoorRoute#cdn_frontdoor_origin_path}.
        :param cdn_frontdoor_rule_set_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_rule_set_ids CdnFrontdoorRoute#cdn_frontdoor_rule_set_ids}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#enabled CdnFrontdoorRoute#enabled}.
        :param forwarding_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#forwarding_protocol CdnFrontdoorRoute#forwarding_protocol}.
        :param https_redirect_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#https_redirect_enabled CdnFrontdoorRoute#https_redirect_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#id CdnFrontdoorRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#timeouts CdnFrontdoorRoute#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRoute.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CdnFrontdoorRouteConfig(
            cdn_frontdoor_endpoint_id=cdn_frontdoor_endpoint_id,
            cdn_frontdoor_origin_group_id=cdn_frontdoor_origin_group_id,
            cdn_frontdoor_origin_ids=cdn_frontdoor_origin_ids,
            name=name,
            patterns_to_match=patterns_to_match,
            supported_protocols=supported_protocols,
            cache=cache,
            cdn_frontdoor_origin_path=cdn_frontdoor_origin_path,
            cdn_frontdoor_rule_set_ids=cdn_frontdoor_rule_set_ids,
            enabled=enabled,
            forwarding_protocol=forwarding_protocol,
            https_redirect_enabled=https_redirect_enabled,
            id=id,
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

    @jsii.member(jsii_name="putCache")
    def put_cache(
        self,
        *,
        compression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        content_types_to_compress: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_caching_behavior: typing.Optional[builtins.str] = None,
        query_strings: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param compression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#compression_enabled CdnFrontdoorRoute#compression_enabled}.
        :param content_types_to_compress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#content_types_to_compress CdnFrontdoorRoute#content_types_to_compress}.
        :param query_string_caching_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#query_string_caching_behavior CdnFrontdoorRoute#query_string_caching_behavior}.
        :param query_strings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#query_strings CdnFrontdoorRoute#query_strings}.
        '''
        value = CdnFrontdoorRouteCache(
            compression_enabled=compression_enabled,
            content_types_to_compress=content_types_to_compress,
            query_string_caching_behavior=query_string_caching_behavior,
            query_strings=query_strings,
        )

        return typing.cast(None, jsii.invoke(self, "putCache", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#create CdnFrontdoorRoute#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#delete CdnFrontdoorRoute#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#read CdnFrontdoorRoute#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#update CdnFrontdoorRoute#update}.
        '''
        value = CdnFrontdoorRouteTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCache")
    def reset_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCache", []))

    @jsii.member(jsii_name="resetCdnFrontdoorOriginPath")
    def reset_cdn_frontdoor_origin_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdnFrontdoorOriginPath", []))

    @jsii.member(jsii_name="resetCdnFrontdoorRuleSetIds")
    def reset_cdn_frontdoor_rule_set_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdnFrontdoorRuleSetIds", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetForwardingProtocol")
    def reset_forwarding_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingProtocol", []))

    @jsii.member(jsii_name="resetHttpsRedirectEnabled")
    def reset_https_redirect_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirectEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="cache")
    def cache(self) -> "CdnFrontdoorRouteCacheOutputReference":
        return typing.cast("CdnFrontdoorRouteCacheOutputReference", jsii.get(self, "cache"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CdnFrontdoorRouteTimeoutsOutputReference":
        return typing.cast("CdnFrontdoorRouteTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="cacheInput")
    def cache_input(self) -> typing.Optional["CdnFrontdoorRouteCache"]:
        return typing.cast(typing.Optional["CdnFrontdoorRouteCache"], jsii.get(self, "cacheInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorEndpointIdInput")
    def cdn_frontdoor_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorOriginGroupIdInput")
    def cdn_frontdoor_origin_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorOriginGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorOriginIdsInput")
    def cdn_frontdoor_origin_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cdnFrontdoorOriginIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorOriginPathInput")
    def cdn_frontdoor_origin_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorOriginPathInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorRuleSetIdsInput")
    def cdn_frontdoor_rule_set_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cdnFrontdoorRuleSetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingProtocolInput")
    def forwarding_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardingProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectEnabledInput")
    def https_redirect_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="patternsToMatchInput")
    def patterns_to_match_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patternsToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="supportedProtocolsInput")
    def supported_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "supportedProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CdnFrontdoorRouteTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CdnFrontdoorRouteTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorEndpointId")
    def cdn_frontdoor_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorEndpointId"))

    @cdn_frontdoor_endpoint_id.setter
    def cdn_frontdoor_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "cdn_frontdoor_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorOriginGroupId")
    def cdn_frontdoor_origin_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorOriginGroupId"))

    @cdn_frontdoor_origin_group_id.setter
    def cdn_frontdoor_origin_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "cdn_frontdoor_origin_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorOriginGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorOriginIds")
    def cdn_frontdoor_origin_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cdnFrontdoorOriginIds"))

    @cdn_frontdoor_origin_ids.setter
    def cdn_frontdoor_origin_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "cdn_frontdoor_origin_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorOriginIds", value)

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorOriginPath")
    def cdn_frontdoor_origin_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorOriginPath"))

    @cdn_frontdoor_origin_path.setter
    def cdn_frontdoor_origin_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "cdn_frontdoor_origin_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorOriginPath", value)

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorRuleSetIds")
    def cdn_frontdoor_rule_set_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cdnFrontdoorRuleSetIds"))

    @cdn_frontdoor_rule_set_ids.setter
    def cdn_frontdoor_rule_set_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "cdn_frontdoor_rule_set_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorRuleSetIds", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="forwardingProtocol")
    def forwarding_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardingProtocol"))

    @forwarding_protocol.setter
    def forwarding_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "forwarding_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardingProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectEnabled")
    def https_redirect_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirectEnabled"))

    @https_redirect_enabled.setter
    def https_redirect_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "https_redirect_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirectEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="patternsToMatch")
    def patterns_to_match(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "patternsToMatch"))

    @patterns_to_match.setter
    def patterns_to_match(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "patterns_to_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patternsToMatch", value)

    @builtins.property
    @jsii.member(jsii_name="supportedProtocols")
    def supported_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportedProtocols"))

    @supported_protocols.setter
    def supported_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRoute, "supported_protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportedProtocols", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRoute.CdnFrontdoorRouteCache",
    jsii_struct_bases=[],
    name_mapping={
        "compression_enabled": "compressionEnabled",
        "content_types_to_compress": "contentTypesToCompress",
        "query_string_caching_behavior": "queryStringCachingBehavior",
        "query_strings": "queryStrings",
    },
)
class CdnFrontdoorRouteCache:
    def __init__(
        self,
        *,
        compression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        content_types_to_compress: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_caching_behavior: typing.Optional[builtins.str] = None,
        query_strings: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param compression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#compression_enabled CdnFrontdoorRoute#compression_enabled}.
        :param content_types_to_compress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#content_types_to_compress CdnFrontdoorRoute#content_types_to_compress}.
        :param query_string_caching_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#query_string_caching_behavior CdnFrontdoorRoute#query_string_caching_behavior}.
        :param query_strings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#query_strings CdnFrontdoorRoute#query_strings}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRouteCache.__init__)
            check_type(argname="argument compression_enabled", value=compression_enabled, expected_type=type_hints["compression_enabled"])
            check_type(argname="argument content_types_to_compress", value=content_types_to_compress, expected_type=type_hints["content_types_to_compress"])
            check_type(argname="argument query_string_caching_behavior", value=query_string_caching_behavior, expected_type=type_hints["query_string_caching_behavior"])
            check_type(argname="argument query_strings", value=query_strings, expected_type=type_hints["query_strings"])
        self._values: typing.Dict[str, typing.Any] = {}
        if compression_enabled is not None:
            self._values["compression_enabled"] = compression_enabled
        if content_types_to_compress is not None:
            self._values["content_types_to_compress"] = content_types_to_compress
        if query_string_caching_behavior is not None:
            self._values["query_string_caching_behavior"] = query_string_caching_behavior
        if query_strings is not None:
            self._values["query_strings"] = query_strings

    @builtins.property
    def compression_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#compression_enabled CdnFrontdoorRoute#compression_enabled}.'''
        result = self._values.get("compression_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def content_types_to_compress(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#content_types_to_compress CdnFrontdoorRoute#content_types_to_compress}.'''
        result = self._values.get("content_types_to_compress")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_caching_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#query_string_caching_behavior CdnFrontdoorRoute#query_string_caching_behavior}.'''
        result = self._values.get("query_string_caching_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_strings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#query_strings CdnFrontdoorRoute#query_strings}.'''
        result = self._values.get("query_strings")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRouteCache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRouteCacheOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRoute.CdnFrontdoorRouteCacheOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRouteCacheOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompressionEnabled")
    def reset_compression_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionEnabled", []))

    @jsii.member(jsii_name="resetContentTypesToCompress")
    def reset_content_types_to_compress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentTypesToCompress", []))

    @jsii.member(jsii_name="resetQueryStringCachingBehavior")
    def reset_query_string_caching_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringCachingBehavior", []))

    @jsii.member(jsii_name="resetQueryStrings")
    def reset_query_strings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStrings", []))

    @builtins.property
    @jsii.member(jsii_name="compressionEnabledInput")
    def compression_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "compressionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypesToCompressInput")
    def content_types_to_compress_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contentTypesToCompressInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringCachingBehaviorInput")
    def query_string_caching_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryStringCachingBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringsInput")
    def query_strings_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryStringsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionEnabled")
    def compression_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "compressionEnabled"))

    @compression_enabled.setter
    def compression_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteCacheOutputReference, "compression_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="contentTypesToCompress")
    def content_types_to_compress(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contentTypesToCompress"))

    @content_types_to_compress.setter
    def content_types_to_compress(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteCacheOutputReference, "content_types_to_compress").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentTypesToCompress", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringCachingBehavior")
    def query_string_caching_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryStringCachingBehavior"))

    @query_string_caching_behavior.setter
    def query_string_caching_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteCacheOutputReference, "query_string_caching_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringCachingBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="queryStrings")
    def query_strings(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStrings"))

    @query_strings.setter
    def query_strings(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteCacheOutputReference, "query_strings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStrings", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CdnFrontdoorRouteCache]:
        return typing.cast(typing.Optional[CdnFrontdoorRouteCache], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CdnFrontdoorRouteCache]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteCacheOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRoute.CdnFrontdoorRouteConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cdn_frontdoor_endpoint_id": "cdnFrontdoorEndpointId",
        "cdn_frontdoor_origin_group_id": "cdnFrontdoorOriginGroupId",
        "cdn_frontdoor_origin_ids": "cdnFrontdoorOriginIds",
        "name": "name",
        "patterns_to_match": "patternsToMatch",
        "supported_protocols": "supportedProtocols",
        "cache": "cache",
        "cdn_frontdoor_origin_path": "cdnFrontdoorOriginPath",
        "cdn_frontdoor_rule_set_ids": "cdnFrontdoorRuleSetIds",
        "enabled": "enabled",
        "forwarding_protocol": "forwardingProtocol",
        "https_redirect_enabled": "httpsRedirectEnabled",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class CdnFrontdoorRouteConfig(cdktf.TerraformMetaArguments):
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
        cdn_frontdoor_endpoint_id: builtins.str,
        cdn_frontdoor_origin_group_id: builtins.str,
        cdn_frontdoor_origin_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        patterns_to_match: typing.Sequence[builtins.str],
        supported_protocols: typing.Sequence[builtins.str],
        cache: typing.Optional[typing.Union[CdnFrontdoorRouteCache, typing.Dict[str, typing.Any]]] = None,
        cdn_frontdoor_origin_path: typing.Optional[builtins.str] = None,
        cdn_frontdoor_rule_set_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_protocol: typing.Optional[builtins.str] = None,
        https_redirect_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorRouteTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cdn_frontdoor_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_endpoint_id CdnFrontdoorRoute#cdn_frontdoor_endpoint_id}.
        :param cdn_frontdoor_origin_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_group_id CdnFrontdoorRoute#cdn_frontdoor_origin_group_id}.
        :param cdn_frontdoor_origin_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_ids CdnFrontdoorRoute#cdn_frontdoor_origin_ids}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#name CdnFrontdoorRoute#name}.
        :param patterns_to_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#patterns_to_match CdnFrontdoorRoute#patterns_to_match}.
        :param supported_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#supported_protocols CdnFrontdoorRoute#supported_protocols}.
        :param cache: cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cache CdnFrontdoorRoute#cache}
        :param cdn_frontdoor_origin_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_path CdnFrontdoorRoute#cdn_frontdoor_origin_path}.
        :param cdn_frontdoor_rule_set_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_rule_set_ids CdnFrontdoorRoute#cdn_frontdoor_rule_set_ids}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#enabled CdnFrontdoorRoute#enabled}.
        :param forwarding_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#forwarding_protocol CdnFrontdoorRoute#forwarding_protocol}.
        :param https_redirect_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#https_redirect_enabled CdnFrontdoorRoute#https_redirect_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#id CdnFrontdoorRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#timeouts CdnFrontdoorRoute#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cache, dict):
            cache = CdnFrontdoorRouteCache(**cache)
        if isinstance(timeouts, dict):
            timeouts = CdnFrontdoorRouteTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRouteConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cdn_frontdoor_endpoint_id", value=cdn_frontdoor_endpoint_id, expected_type=type_hints["cdn_frontdoor_endpoint_id"])
            check_type(argname="argument cdn_frontdoor_origin_group_id", value=cdn_frontdoor_origin_group_id, expected_type=type_hints["cdn_frontdoor_origin_group_id"])
            check_type(argname="argument cdn_frontdoor_origin_ids", value=cdn_frontdoor_origin_ids, expected_type=type_hints["cdn_frontdoor_origin_ids"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument patterns_to_match", value=patterns_to_match, expected_type=type_hints["patterns_to_match"])
            check_type(argname="argument supported_protocols", value=supported_protocols, expected_type=type_hints["supported_protocols"])
            check_type(argname="argument cache", value=cache, expected_type=type_hints["cache"])
            check_type(argname="argument cdn_frontdoor_origin_path", value=cdn_frontdoor_origin_path, expected_type=type_hints["cdn_frontdoor_origin_path"])
            check_type(argname="argument cdn_frontdoor_rule_set_ids", value=cdn_frontdoor_rule_set_ids, expected_type=type_hints["cdn_frontdoor_rule_set_ids"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument forwarding_protocol", value=forwarding_protocol, expected_type=type_hints["forwarding_protocol"])
            check_type(argname="argument https_redirect_enabled", value=https_redirect_enabled, expected_type=type_hints["https_redirect_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cdn_frontdoor_endpoint_id": cdn_frontdoor_endpoint_id,
            "cdn_frontdoor_origin_group_id": cdn_frontdoor_origin_group_id,
            "cdn_frontdoor_origin_ids": cdn_frontdoor_origin_ids,
            "name": name,
            "patterns_to_match": patterns_to_match,
            "supported_protocols": supported_protocols,
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
        if cache is not None:
            self._values["cache"] = cache
        if cdn_frontdoor_origin_path is not None:
            self._values["cdn_frontdoor_origin_path"] = cdn_frontdoor_origin_path
        if cdn_frontdoor_rule_set_ids is not None:
            self._values["cdn_frontdoor_rule_set_ids"] = cdn_frontdoor_rule_set_ids
        if enabled is not None:
            self._values["enabled"] = enabled
        if forwarding_protocol is not None:
            self._values["forwarding_protocol"] = forwarding_protocol
        if https_redirect_enabled is not None:
            self._values["https_redirect_enabled"] = https_redirect_enabled
        if id is not None:
            self._values["id"] = id
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
    def cdn_frontdoor_endpoint_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_endpoint_id CdnFrontdoorRoute#cdn_frontdoor_endpoint_id}.'''
        result = self._values.get("cdn_frontdoor_endpoint_id")
        assert result is not None, "Required property 'cdn_frontdoor_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdn_frontdoor_origin_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_group_id CdnFrontdoorRoute#cdn_frontdoor_origin_group_id}.'''
        result = self._values.get("cdn_frontdoor_origin_group_id")
        assert result is not None, "Required property 'cdn_frontdoor_origin_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdn_frontdoor_origin_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_ids CdnFrontdoorRoute#cdn_frontdoor_origin_ids}.'''
        result = self._values.get("cdn_frontdoor_origin_ids")
        assert result is not None, "Required property 'cdn_frontdoor_origin_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#name CdnFrontdoorRoute#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def patterns_to_match(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#patterns_to_match CdnFrontdoorRoute#patterns_to_match}.'''
        result = self._values.get("patterns_to_match")
        assert result is not None, "Required property 'patterns_to_match' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def supported_protocols(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#supported_protocols CdnFrontdoorRoute#supported_protocols}.'''
        result = self._values.get("supported_protocols")
        assert result is not None, "Required property 'supported_protocols' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cache(self) -> typing.Optional[CdnFrontdoorRouteCache]:
        '''cache block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cache CdnFrontdoorRoute#cache}
        '''
        result = self._values.get("cache")
        return typing.cast(typing.Optional[CdnFrontdoorRouteCache], result)

    @builtins.property
    def cdn_frontdoor_origin_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_origin_path CdnFrontdoorRoute#cdn_frontdoor_origin_path}.'''
        result = self._values.get("cdn_frontdoor_origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdn_frontdoor_rule_set_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#cdn_frontdoor_rule_set_ids CdnFrontdoorRoute#cdn_frontdoor_rule_set_ids}.'''
        result = self._values.get("cdn_frontdoor_rule_set_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#enabled CdnFrontdoorRoute#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forwarding_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#forwarding_protocol CdnFrontdoorRoute#forwarding_protocol}.'''
        result = self._values.get("forwarding_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#https_redirect_enabled CdnFrontdoorRoute#https_redirect_enabled}.'''
        result = self._values.get("https_redirect_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#id CdnFrontdoorRoute#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CdnFrontdoorRouteTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#timeouts CdnFrontdoorRoute#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CdnFrontdoorRouteTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRoute.CdnFrontdoorRouteTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CdnFrontdoorRouteTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#create CdnFrontdoorRoute#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#delete CdnFrontdoorRoute#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#read CdnFrontdoorRoute#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#update CdnFrontdoorRoute#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRouteTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#create CdnFrontdoorRoute#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#delete CdnFrontdoorRoute#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#read CdnFrontdoorRoute#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_route#update CdnFrontdoorRoute#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRouteTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRouteTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRoute.CdnFrontdoorRouteTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRouteTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRouteTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRouteTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRouteTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRouteTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CdnFrontdoorRoute",
    "CdnFrontdoorRouteCache",
    "CdnFrontdoorRouteCacheOutputReference",
    "CdnFrontdoorRouteConfig",
    "CdnFrontdoorRouteTimeouts",
    "CdnFrontdoorRouteTimeoutsOutputReference",
]

publication.publish()
