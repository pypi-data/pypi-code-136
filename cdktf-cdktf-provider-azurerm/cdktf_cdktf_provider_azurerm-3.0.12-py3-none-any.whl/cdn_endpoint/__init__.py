'''
# `azurerm_cdn_endpoint`

Refer to the Terraform Registory for docs: [`azurerm_cdn_endpoint`](https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint).
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


class CdnEndpoint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint azurerm_cdn_endpoint}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        origin: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointOrigin", typing.Dict[str, typing.Any]]]],
        profile_name: builtins.str,
        resource_group_name: builtins.str,
        content_types_to_compress: typing.Optional[typing.Sequence[builtins.str]] = None,
        delivery_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRule", typing.Dict[str, typing.Any]]]]] = None,
        geo_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointGeoFilter", typing.Dict[str, typing.Any]]]]] = None,
        global_delivery_rule: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRule", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_compression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_http_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_https_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        optimization_type: typing.Optional[builtins.str] = None,
        origin_host_header: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        probe_path: typing.Optional[builtins.str] = None,
        querystring_caching_behaviour: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CdnEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint azurerm_cdn_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#location CdnEndpoint#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.
        :param origin: origin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin CdnEndpoint#origin}
        :param profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#profile_name CdnEndpoint#profile_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#resource_group_name CdnEndpoint#resource_group_name}.
        :param content_types_to_compress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#content_types_to_compress CdnEndpoint#content_types_to_compress}.
        :param delivery_rule: delivery_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#delivery_rule CdnEndpoint#delivery_rule}
        :param geo_filter: geo_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#geo_filter CdnEndpoint#geo_filter}
        :param global_delivery_rule: global_delivery_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#global_delivery_rule CdnEndpoint#global_delivery_rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#id CdnEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_compression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_compression_enabled CdnEndpoint#is_compression_enabled}.
        :param is_http_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_http_allowed CdnEndpoint#is_http_allowed}.
        :param is_https_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_https_allowed CdnEndpoint#is_https_allowed}.
        :param optimization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#optimization_type CdnEndpoint#optimization_type}.
        :param origin_host_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin_host_header CdnEndpoint#origin_host_header}.
        :param origin_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin_path CdnEndpoint#origin_path}.
        :param probe_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#probe_path CdnEndpoint#probe_path}.
        :param querystring_caching_behaviour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#querystring_caching_behaviour CdnEndpoint#querystring_caching_behaviour}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#tags CdnEndpoint#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#timeouts CdnEndpoint#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpoint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CdnEndpointConfig(
            location=location,
            name=name,
            origin=origin,
            profile_name=profile_name,
            resource_group_name=resource_group_name,
            content_types_to_compress=content_types_to_compress,
            delivery_rule=delivery_rule,
            geo_filter=geo_filter,
            global_delivery_rule=global_delivery_rule,
            id=id,
            is_compression_enabled=is_compression_enabled,
            is_http_allowed=is_http_allowed,
            is_https_allowed=is_https_allowed,
            optimization_type=optimization_type,
            origin_host_header=origin_host_header,
            origin_path=origin_path,
            probe_path=probe_path,
            querystring_caching_behaviour=querystring_caching_behaviour,
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

    @jsii.member(jsii_name="putDeliveryRule")
    def put_delivery_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpoint.put_delivery_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeliveryRule", [value]))

    @jsii.member(jsii_name="putGeoFilter")
    def put_geo_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointGeoFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpoint.put_geo_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGeoFilter", [value]))

    @jsii.member(jsii_name="putGlobalDeliveryRule")
    def put_global_delivery_rule(
        self,
        *,
        cache_expiration_action: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRuleCacheExpirationAction", typing.Dict[str, typing.Any]]] = None,
        cache_key_query_string_action: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction", typing.Dict[str, typing.Any]]] = None,
        modify_request_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        modify_response_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        url_redirect_action: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRuleUrlRedirectAction", typing.Dict[str, typing.Any]]] = None,
        url_rewrite_action: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRuleUrlRewriteAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cache_expiration_action: cache_expiration_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_expiration_action CdnEndpoint#cache_expiration_action}
        :param cache_key_query_string_action: cache_key_query_string_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_key_query_string_action CdnEndpoint#cache_key_query_string_action}
        :param modify_request_header_action: modify_request_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_request_header_action CdnEndpoint#modify_request_header_action}
        :param modify_response_header_action: modify_response_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_response_header_action CdnEndpoint#modify_response_header_action}
        :param url_redirect_action: url_redirect_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_redirect_action CdnEndpoint#url_redirect_action}
        :param url_rewrite_action: url_rewrite_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_rewrite_action CdnEndpoint#url_rewrite_action}
        '''
        value = CdnEndpointGlobalDeliveryRule(
            cache_expiration_action=cache_expiration_action,
            cache_key_query_string_action=cache_key_query_string_action,
            modify_request_header_action=modify_request_header_action,
            modify_response_header_action=modify_response_header_action,
            url_redirect_action=url_redirect_action,
            url_rewrite_action=url_rewrite_action,
        )

        return typing.cast(None, jsii.invoke(self, "putGlobalDeliveryRule", [value]))

    @jsii.member(jsii_name="putOrigin")
    def put_origin(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointOrigin", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpoint.put_origin)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrigin", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#create CdnEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#delete CdnEndpoint#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#read CdnEndpoint#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#update CdnEndpoint#update}.
        '''
        value = CdnEndpointTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetContentTypesToCompress")
    def reset_content_types_to_compress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentTypesToCompress", []))

    @jsii.member(jsii_name="resetDeliveryRule")
    def reset_delivery_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryRule", []))

    @jsii.member(jsii_name="resetGeoFilter")
    def reset_geo_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoFilter", []))

    @jsii.member(jsii_name="resetGlobalDeliveryRule")
    def reset_global_delivery_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalDeliveryRule", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsCompressionEnabled")
    def reset_is_compression_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsCompressionEnabled", []))

    @jsii.member(jsii_name="resetIsHttpAllowed")
    def reset_is_http_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsHttpAllowed", []))

    @jsii.member(jsii_name="resetIsHttpsAllowed")
    def reset_is_https_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsHttpsAllowed", []))

    @jsii.member(jsii_name="resetOptimizationType")
    def reset_optimization_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptimizationType", []))

    @jsii.member(jsii_name="resetOriginHostHeader")
    def reset_origin_host_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginHostHeader", []))

    @jsii.member(jsii_name="resetOriginPath")
    def reset_origin_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginPath", []))

    @jsii.member(jsii_name="resetProbePath")
    def reset_probe_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProbePath", []))

    @jsii.member(jsii_name="resetQuerystringCachingBehaviour")
    def reset_querystring_caching_behaviour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuerystringCachingBehaviour", []))

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
    @jsii.member(jsii_name="deliveryRule")
    def delivery_rule(self) -> "CdnEndpointDeliveryRuleList":
        return typing.cast("CdnEndpointDeliveryRuleList", jsii.get(self, "deliveryRule"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="geoFilter")
    def geo_filter(self) -> "CdnEndpointGeoFilterList":
        return typing.cast("CdnEndpointGeoFilterList", jsii.get(self, "geoFilter"))

    @builtins.property
    @jsii.member(jsii_name="globalDeliveryRule")
    def global_delivery_rule(self) -> "CdnEndpointGlobalDeliveryRuleOutputReference":
        return typing.cast("CdnEndpointGlobalDeliveryRuleOutputReference", jsii.get(self, "globalDeliveryRule"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> "CdnEndpointOriginList":
        return typing.cast("CdnEndpointOriginList", jsii.get(self, "origin"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CdnEndpointTimeoutsOutputReference":
        return typing.cast("CdnEndpointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="contentTypesToCompressInput")
    def content_types_to_compress_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contentTypesToCompressInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryRuleInput")
    def delivery_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRule"]]], jsii.get(self, "deliveryRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="geoFilterInput")
    def geo_filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointGeoFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointGeoFilter"]]], jsii.get(self, "geoFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="globalDeliveryRuleInput")
    def global_delivery_rule_input(
        self,
    ) -> typing.Optional["CdnEndpointGlobalDeliveryRule"]:
        return typing.cast(typing.Optional["CdnEndpointGlobalDeliveryRule"], jsii.get(self, "globalDeliveryRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isCompressionEnabledInput")
    def is_compression_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isCompressionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="isHttpAllowedInput")
    def is_http_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isHttpAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="isHttpsAllowedInput")
    def is_https_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isHttpsAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optimizationTypeInput")
    def optimization_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optimizationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="originHostHeaderInput")
    def origin_host_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originHostHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="originInput")
    def origin_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointOrigin"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointOrigin"]]], jsii.get(self, "originInput"))

    @builtins.property
    @jsii.member(jsii_name="originPathInput")
    def origin_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originPathInput"))

    @builtins.property
    @jsii.member(jsii_name="probePathInput")
    def probe_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "probePathInput"))

    @builtins.property
    @jsii.member(jsii_name="profileNameInput")
    def profile_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="querystringCachingBehaviourInput")
    def querystring_caching_behaviour_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "querystringCachingBehaviourInput"))

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
    ) -> typing.Optional[typing.Union["CdnEndpointTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CdnEndpointTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypesToCompress")
    def content_types_to_compress(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contentTypesToCompress"))

    @content_types_to_compress.setter
    def content_types_to_compress(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "content_types_to_compress").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentTypesToCompress", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isCompressionEnabled")
    def is_compression_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isCompressionEnabled"))

    @is_compression_enabled.setter
    def is_compression_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "is_compression_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCompressionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isHttpAllowed")
    def is_http_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isHttpAllowed"))

    @is_http_allowed.setter
    def is_http_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "is_http_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isHttpAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="isHttpsAllowed")
    def is_https_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isHttpsAllowed"))

    @is_https_allowed.setter
    def is_https_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "is_https_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isHttpsAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="optimizationType")
    def optimization_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "optimizationType"))

    @optimization_type.setter
    def optimization_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "optimization_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optimizationType", value)

    @builtins.property
    @jsii.member(jsii_name="originHostHeader")
    def origin_host_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originHostHeader"))

    @origin_host_header.setter
    def origin_host_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "origin_host_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originHostHeader", value)

    @builtins.property
    @jsii.member(jsii_name="originPath")
    def origin_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originPath"))

    @origin_path.setter
    def origin_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "origin_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originPath", value)

    @builtins.property
    @jsii.member(jsii_name="probePath")
    def probe_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "probePath"))

    @probe_path.setter
    def probe_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "probe_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "probePath", value)

    @builtins.property
    @jsii.member(jsii_name="profileName")
    def profile_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profileName"))

    @profile_name.setter
    def profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "profile_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileName", value)

    @builtins.property
    @jsii.member(jsii_name="querystringCachingBehaviour")
    def querystring_caching_behaviour(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "querystringCachingBehaviour"))

    @querystring_caching_behaviour.setter
    def querystring_caching_behaviour(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "querystring_caching_behaviour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "querystringCachingBehaviour", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpoint, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointConfig",
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
        "origin": "origin",
        "profile_name": "profileName",
        "resource_group_name": "resourceGroupName",
        "content_types_to_compress": "contentTypesToCompress",
        "delivery_rule": "deliveryRule",
        "geo_filter": "geoFilter",
        "global_delivery_rule": "globalDeliveryRule",
        "id": "id",
        "is_compression_enabled": "isCompressionEnabled",
        "is_http_allowed": "isHttpAllowed",
        "is_https_allowed": "isHttpsAllowed",
        "optimization_type": "optimizationType",
        "origin_host_header": "originHostHeader",
        "origin_path": "originPath",
        "probe_path": "probePath",
        "querystring_caching_behaviour": "querystringCachingBehaviour",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class CdnEndpointConfig(cdktf.TerraformMetaArguments):
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
        origin: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointOrigin", typing.Dict[str, typing.Any]]]],
        profile_name: builtins.str,
        resource_group_name: builtins.str,
        content_types_to_compress: typing.Optional[typing.Sequence[builtins.str]] = None,
        delivery_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRule", typing.Dict[str, typing.Any]]]]] = None,
        geo_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointGeoFilter", typing.Dict[str, typing.Any]]]]] = None,
        global_delivery_rule: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRule", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_compression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_http_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_https_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        optimization_type: typing.Optional[builtins.str] = None,
        origin_host_header: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        probe_path: typing.Optional[builtins.str] = None,
        querystring_caching_behaviour: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CdnEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#location CdnEndpoint#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.
        :param origin: origin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin CdnEndpoint#origin}
        :param profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#profile_name CdnEndpoint#profile_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#resource_group_name CdnEndpoint#resource_group_name}.
        :param content_types_to_compress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#content_types_to_compress CdnEndpoint#content_types_to_compress}.
        :param delivery_rule: delivery_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#delivery_rule CdnEndpoint#delivery_rule}
        :param geo_filter: geo_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#geo_filter CdnEndpoint#geo_filter}
        :param global_delivery_rule: global_delivery_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#global_delivery_rule CdnEndpoint#global_delivery_rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#id CdnEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_compression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_compression_enabled CdnEndpoint#is_compression_enabled}.
        :param is_http_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_http_allowed CdnEndpoint#is_http_allowed}.
        :param is_https_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_https_allowed CdnEndpoint#is_https_allowed}.
        :param optimization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#optimization_type CdnEndpoint#optimization_type}.
        :param origin_host_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin_host_header CdnEndpoint#origin_host_header}.
        :param origin_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin_path CdnEndpoint#origin_path}.
        :param probe_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#probe_path CdnEndpoint#probe_path}.
        :param querystring_caching_behaviour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#querystring_caching_behaviour CdnEndpoint#querystring_caching_behaviour}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#tags CdnEndpoint#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#timeouts CdnEndpoint#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(global_delivery_rule, dict):
            global_delivery_rule = CdnEndpointGlobalDeliveryRule(**global_delivery_rule)
        if isinstance(timeouts, dict):
            timeouts = CdnEndpointTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument profile_name", value=profile_name, expected_type=type_hints["profile_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument content_types_to_compress", value=content_types_to_compress, expected_type=type_hints["content_types_to_compress"])
            check_type(argname="argument delivery_rule", value=delivery_rule, expected_type=type_hints["delivery_rule"])
            check_type(argname="argument geo_filter", value=geo_filter, expected_type=type_hints["geo_filter"])
            check_type(argname="argument global_delivery_rule", value=global_delivery_rule, expected_type=type_hints["global_delivery_rule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_compression_enabled", value=is_compression_enabled, expected_type=type_hints["is_compression_enabled"])
            check_type(argname="argument is_http_allowed", value=is_http_allowed, expected_type=type_hints["is_http_allowed"])
            check_type(argname="argument is_https_allowed", value=is_https_allowed, expected_type=type_hints["is_https_allowed"])
            check_type(argname="argument optimization_type", value=optimization_type, expected_type=type_hints["optimization_type"])
            check_type(argname="argument origin_host_header", value=origin_host_header, expected_type=type_hints["origin_host_header"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument probe_path", value=probe_path, expected_type=type_hints["probe_path"])
            check_type(argname="argument querystring_caching_behaviour", value=querystring_caching_behaviour, expected_type=type_hints["querystring_caching_behaviour"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "origin": origin,
            "profile_name": profile_name,
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
        if content_types_to_compress is not None:
            self._values["content_types_to_compress"] = content_types_to_compress
        if delivery_rule is not None:
            self._values["delivery_rule"] = delivery_rule
        if geo_filter is not None:
            self._values["geo_filter"] = geo_filter
        if global_delivery_rule is not None:
            self._values["global_delivery_rule"] = global_delivery_rule
        if id is not None:
            self._values["id"] = id
        if is_compression_enabled is not None:
            self._values["is_compression_enabled"] = is_compression_enabled
        if is_http_allowed is not None:
            self._values["is_http_allowed"] = is_http_allowed
        if is_https_allowed is not None:
            self._values["is_https_allowed"] = is_https_allowed
        if optimization_type is not None:
            self._values["optimization_type"] = optimization_type
        if origin_host_header is not None:
            self._values["origin_host_header"] = origin_host_header
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if probe_path is not None:
            self._values["probe_path"] = probe_path
        if querystring_caching_behaviour is not None:
            self._values["querystring_caching_behaviour"] = querystring_caching_behaviour
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#location CdnEndpoint#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["CdnEndpointOrigin"]]:
        '''origin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin CdnEndpoint#origin}
        '''
        result = self._values.get("origin")
        assert result is not None, "Required property 'origin' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["CdnEndpointOrigin"]], result)

    @builtins.property
    def profile_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#profile_name CdnEndpoint#profile_name}.'''
        result = self._values.get("profile_name")
        assert result is not None, "Required property 'profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#resource_group_name CdnEndpoint#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_types_to_compress(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#content_types_to_compress CdnEndpoint#content_types_to_compress}.'''
        result = self._values.get("content_types_to_compress")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def delivery_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRule"]]]:
        '''delivery_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#delivery_rule CdnEndpoint#delivery_rule}
        '''
        result = self._values.get("delivery_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRule"]]], result)

    @builtins.property
    def geo_filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointGeoFilter"]]]:
        '''geo_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#geo_filter CdnEndpoint#geo_filter}
        '''
        result = self._values.get("geo_filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointGeoFilter"]]], result)

    @builtins.property
    def global_delivery_rule(self) -> typing.Optional["CdnEndpointGlobalDeliveryRule"]:
        '''global_delivery_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#global_delivery_rule CdnEndpoint#global_delivery_rule}
        '''
        result = self._values.get("global_delivery_rule")
        return typing.cast(typing.Optional["CdnEndpointGlobalDeliveryRule"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#id CdnEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_compression_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_compression_enabled CdnEndpoint#is_compression_enabled}.'''
        result = self._values.get("is_compression_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_http_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_http_allowed CdnEndpoint#is_http_allowed}.'''
        result = self._values.get("is_http_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_https_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#is_https_allowed CdnEndpoint#is_https_allowed}.'''
        result = self._values.get("is_https_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def optimization_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#optimization_type CdnEndpoint#optimization_type}.'''
        result = self._values.get("optimization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_host_header(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin_host_header CdnEndpoint#origin_host_header}.'''
        result = self._values.get("origin_host_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#origin_path CdnEndpoint#origin_path}.'''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def probe_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#probe_path CdnEndpoint#probe_path}.'''
        result = self._values.get("probe_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def querystring_caching_behaviour(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#querystring_caching_behaviour CdnEndpoint#querystring_caching_behaviour}.'''
        result = self._values.get("querystring_caching_behaviour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#tags CdnEndpoint#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CdnEndpointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#timeouts CdnEndpoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CdnEndpointTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRule",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "order": "order",
        "cache_expiration_action": "cacheExpirationAction",
        "cache_key_query_string_action": "cacheKeyQueryStringAction",
        "cookies_condition": "cookiesCondition",
        "device_condition": "deviceCondition",
        "http_version_condition": "httpVersionCondition",
        "modify_request_header_action": "modifyRequestHeaderAction",
        "modify_response_header_action": "modifyResponseHeaderAction",
        "post_arg_condition": "postArgCondition",
        "query_string_condition": "queryStringCondition",
        "remote_address_condition": "remoteAddressCondition",
        "request_body_condition": "requestBodyCondition",
        "request_header_condition": "requestHeaderCondition",
        "request_method_condition": "requestMethodCondition",
        "request_scheme_condition": "requestSchemeCondition",
        "request_uri_condition": "requestUriCondition",
        "url_file_extension_condition": "urlFileExtensionCondition",
        "url_file_name_condition": "urlFileNameCondition",
        "url_path_condition": "urlPathCondition",
        "url_redirect_action": "urlRedirectAction",
        "url_rewrite_action": "urlRewriteAction",
    },
)
class CdnEndpointDeliveryRule:
    def __init__(
        self,
        *,
        name: builtins.str,
        order: jsii.Number,
        cache_expiration_action: typing.Optional[typing.Union["CdnEndpointDeliveryRuleCacheExpirationAction", typing.Dict[str, typing.Any]]] = None,
        cache_key_query_string_action: typing.Optional[typing.Union["CdnEndpointDeliveryRuleCacheKeyQueryStringAction", typing.Dict[str, typing.Any]]] = None,
        cookies_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleCookiesCondition", typing.Dict[str, typing.Any]]]]] = None,
        device_condition: typing.Optional[typing.Union["CdnEndpointDeliveryRuleDeviceCondition", typing.Dict[str, typing.Any]]] = None,
        http_version_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleHttpVersionCondition", typing.Dict[str, typing.Any]]]]] = None,
        modify_request_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleModifyRequestHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        modify_response_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleModifyResponseHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        post_arg_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRulePostArgCondition", typing.Dict[str, typing.Any]]]]] = None,
        query_string_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleQueryStringCondition", typing.Dict[str, typing.Any]]]]] = None,
        remote_address_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleRemoteAddressCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_body_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleRequestBodyCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_header_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleRequestHeaderCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_method_condition: typing.Optional[typing.Union["CdnEndpointDeliveryRuleRequestMethodCondition", typing.Dict[str, typing.Any]]] = None,
        request_scheme_condition: typing.Optional[typing.Union["CdnEndpointDeliveryRuleRequestSchemeCondition", typing.Dict[str, typing.Any]]] = None,
        request_uri_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleRequestUriCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_file_extension_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleUrlFileExtensionCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_file_name_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleUrlFileNameCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_path_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleUrlPathCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_redirect_action: typing.Optional[typing.Union["CdnEndpointDeliveryRuleUrlRedirectAction", typing.Dict[str, typing.Any]]] = None,
        url_rewrite_action: typing.Optional[typing.Union["CdnEndpointDeliveryRuleUrlRewriteAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#order CdnEndpoint#order}.
        :param cache_expiration_action: cache_expiration_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_expiration_action CdnEndpoint#cache_expiration_action}
        :param cache_key_query_string_action: cache_key_query_string_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_key_query_string_action CdnEndpoint#cache_key_query_string_action}
        :param cookies_condition: cookies_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cookies_condition CdnEndpoint#cookies_condition}
        :param device_condition: device_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#device_condition CdnEndpoint#device_condition}
        :param http_version_condition: http_version_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#http_version_condition CdnEndpoint#http_version_condition}
        :param modify_request_header_action: modify_request_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_request_header_action CdnEndpoint#modify_request_header_action}
        :param modify_response_header_action: modify_response_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_response_header_action CdnEndpoint#modify_response_header_action}
        :param post_arg_condition: post_arg_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#post_arg_condition CdnEndpoint#post_arg_condition}
        :param query_string_condition: query_string_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#query_string_condition CdnEndpoint#query_string_condition}
        :param remote_address_condition: remote_address_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#remote_address_condition CdnEndpoint#remote_address_condition}
        :param request_body_condition: request_body_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_body_condition CdnEndpoint#request_body_condition}
        :param request_header_condition: request_header_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_header_condition CdnEndpoint#request_header_condition}
        :param request_method_condition: request_method_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_method_condition CdnEndpoint#request_method_condition}
        :param request_scheme_condition: request_scheme_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_scheme_condition CdnEndpoint#request_scheme_condition}
        :param request_uri_condition: request_uri_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_uri_condition CdnEndpoint#request_uri_condition}
        :param url_file_extension_condition: url_file_extension_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_file_extension_condition CdnEndpoint#url_file_extension_condition}
        :param url_file_name_condition: url_file_name_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_file_name_condition CdnEndpoint#url_file_name_condition}
        :param url_path_condition: url_path_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_path_condition CdnEndpoint#url_path_condition}
        :param url_redirect_action: url_redirect_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_redirect_action CdnEndpoint#url_redirect_action}
        :param url_rewrite_action: url_rewrite_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_rewrite_action CdnEndpoint#url_rewrite_action}
        '''
        if isinstance(cache_expiration_action, dict):
            cache_expiration_action = CdnEndpointDeliveryRuleCacheExpirationAction(**cache_expiration_action)
        if isinstance(cache_key_query_string_action, dict):
            cache_key_query_string_action = CdnEndpointDeliveryRuleCacheKeyQueryStringAction(**cache_key_query_string_action)
        if isinstance(device_condition, dict):
            device_condition = CdnEndpointDeliveryRuleDeviceCondition(**device_condition)
        if isinstance(request_method_condition, dict):
            request_method_condition = CdnEndpointDeliveryRuleRequestMethodCondition(**request_method_condition)
        if isinstance(request_scheme_condition, dict):
            request_scheme_condition = CdnEndpointDeliveryRuleRequestSchemeCondition(**request_scheme_condition)
        if isinstance(url_redirect_action, dict):
            url_redirect_action = CdnEndpointDeliveryRuleUrlRedirectAction(**url_redirect_action)
        if isinstance(url_rewrite_action, dict):
            url_rewrite_action = CdnEndpointDeliveryRuleUrlRewriteAction(**url_rewrite_action)
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRule.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument cache_expiration_action", value=cache_expiration_action, expected_type=type_hints["cache_expiration_action"])
            check_type(argname="argument cache_key_query_string_action", value=cache_key_query_string_action, expected_type=type_hints["cache_key_query_string_action"])
            check_type(argname="argument cookies_condition", value=cookies_condition, expected_type=type_hints["cookies_condition"])
            check_type(argname="argument device_condition", value=device_condition, expected_type=type_hints["device_condition"])
            check_type(argname="argument http_version_condition", value=http_version_condition, expected_type=type_hints["http_version_condition"])
            check_type(argname="argument modify_request_header_action", value=modify_request_header_action, expected_type=type_hints["modify_request_header_action"])
            check_type(argname="argument modify_response_header_action", value=modify_response_header_action, expected_type=type_hints["modify_response_header_action"])
            check_type(argname="argument post_arg_condition", value=post_arg_condition, expected_type=type_hints["post_arg_condition"])
            check_type(argname="argument query_string_condition", value=query_string_condition, expected_type=type_hints["query_string_condition"])
            check_type(argname="argument remote_address_condition", value=remote_address_condition, expected_type=type_hints["remote_address_condition"])
            check_type(argname="argument request_body_condition", value=request_body_condition, expected_type=type_hints["request_body_condition"])
            check_type(argname="argument request_header_condition", value=request_header_condition, expected_type=type_hints["request_header_condition"])
            check_type(argname="argument request_method_condition", value=request_method_condition, expected_type=type_hints["request_method_condition"])
            check_type(argname="argument request_scheme_condition", value=request_scheme_condition, expected_type=type_hints["request_scheme_condition"])
            check_type(argname="argument request_uri_condition", value=request_uri_condition, expected_type=type_hints["request_uri_condition"])
            check_type(argname="argument url_file_extension_condition", value=url_file_extension_condition, expected_type=type_hints["url_file_extension_condition"])
            check_type(argname="argument url_file_name_condition", value=url_file_name_condition, expected_type=type_hints["url_file_name_condition"])
            check_type(argname="argument url_path_condition", value=url_path_condition, expected_type=type_hints["url_path_condition"])
            check_type(argname="argument url_redirect_action", value=url_redirect_action, expected_type=type_hints["url_redirect_action"])
            check_type(argname="argument url_rewrite_action", value=url_rewrite_action, expected_type=type_hints["url_rewrite_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "order": order,
        }
        if cache_expiration_action is not None:
            self._values["cache_expiration_action"] = cache_expiration_action
        if cache_key_query_string_action is not None:
            self._values["cache_key_query_string_action"] = cache_key_query_string_action
        if cookies_condition is not None:
            self._values["cookies_condition"] = cookies_condition
        if device_condition is not None:
            self._values["device_condition"] = device_condition
        if http_version_condition is not None:
            self._values["http_version_condition"] = http_version_condition
        if modify_request_header_action is not None:
            self._values["modify_request_header_action"] = modify_request_header_action
        if modify_response_header_action is not None:
            self._values["modify_response_header_action"] = modify_response_header_action
        if post_arg_condition is not None:
            self._values["post_arg_condition"] = post_arg_condition
        if query_string_condition is not None:
            self._values["query_string_condition"] = query_string_condition
        if remote_address_condition is not None:
            self._values["remote_address_condition"] = remote_address_condition
        if request_body_condition is not None:
            self._values["request_body_condition"] = request_body_condition
        if request_header_condition is not None:
            self._values["request_header_condition"] = request_header_condition
        if request_method_condition is not None:
            self._values["request_method_condition"] = request_method_condition
        if request_scheme_condition is not None:
            self._values["request_scheme_condition"] = request_scheme_condition
        if request_uri_condition is not None:
            self._values["request_uri_condition"] = request_uri_condition
        if url_file_extension_condition is not None:
            self._values["url_file_extension_condition"] = url_file_extension_condition
        if url_file_name_condition is not None:
            self._values["url_file_name_condition"] = url_file_name_condition
        if url_path_condition is not None:
            self._values["url_path_condition"] = url_path_condition
        if url_redirect_action is not None:
            self._values["url_redirect_action"] = url_redirect_action
        if url_rewrite_action is not None:
            self._values["url_rewrite_action"] = url_rewrite_action

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def order(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#order CdnEndpoint#order}.'''
        result = self._values.get("order")
        assert result is not None, "Required property 'order' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cache_expiration_action(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleCacheExpirationAction"]:
        '''cache_expiration_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_expiration_action CdnEndpoint#cache_expiration_action}
        '''
        result = self._values.get("cache_expiration_action")
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleCacheExpirationAction"], result)

    @builtins.property
    def cache_key_query_string_action(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleCacheKeyQueryStringAction"]:
        '''cache_key_query_string_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_key_query_string_action CdnEndpoint#cache_key_query_string_action}
        '''
        result = self._values.get("cache_key_query_string_action")
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleCacheKeyQueryStringAction"], result)

    @builtins.property
    def cookies_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleCookiesCondition"]]]:
        '''cookies_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cookies_condition CdnEndpoint#cookies_condition}
        '''
        result = self._values.get("cookies_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleCookiesCondition"]]], result)

    @builtins.property
    def device_condition(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleDeviceCondition"]:
        '''device_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#device_condition CdnEndpoint#device_condition}
        '''
        result = self._values.get("device_condition")
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleDeviceCondition"], result)

    @builtins.property
    def http_version_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleHttpVersionCondition"]]]:
        '''http_version_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#http_version_condition CdnEndpoint#http_version_condition}
        '''
        result = self._values.get("http_version_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleHttpVersionCondition"]]], result)

    @builtins.property
    def modify_request_header_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleModifyRequestHeaderAction"]]]:
        '''modify_request_header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_request_header_action CdnEndpoint#modify_request_header_action}
        '''
        result = self._values.get("modify_request_header_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleModifyRequestHeaderAction"]]], result)

    @builtins.property
    def modify_response_header_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleModifyResponseHeaderAction"]]]:
        '''modify_response_header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_response_header_action CdnEndpoint#modify_response_header_action}
        '''
        result = self._values.get("modify_response_header_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleModifyResponseHeaderAction"]]], result)

    @builtins.property
    def post_arg_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRulePostArgCondition"]]]:
        '''post_arg_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#post_arg_condition CdnEndpoint#post_arg_condition}
        '''
        result = self._values.get("post_arg_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRulePostArgCondition"]]], result)

    @builtins.property
    def query_string_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleQueryStringCondition"]]]:
        '''query_string_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#query_string_condition CdnEndpoint#query_string_condition}
        '''
        result = self._values.get("query_string_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleQueryStringCondition"]]], result)

    @builtins.property
    def remote_address_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRemoteAddressCondition"]]]:
        '''remote_address_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#remote_address_condition CdnEndpoint#remote_address_condition}
        '''
        result = self._values.get("remote_address_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRemoteAddressCondition"]]], result)

    @builtins.property
    def request_body_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestBodyCondition"]]]:
        '''request_body_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_body_condition CdnEndpoint#request_body_condition}
        '''
        result = self._values.get("request_body_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestBodyCondition"]]], result)

    @builtins.property
    def request_header_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestHeaderCondition"]]]:
        '''request_header_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_header_condition CdnEndpoint#request_header_condition}
        '''
        result = self._values.get("request_header_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestHeaderCondition"]]], result)

    @builtins.property
    def request_method_condition(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleRequestMethodCondition"]:
        '''request_method_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_method_condition CdnEndpoint#request_method_condition}
        '''
        result = self._values.get("request_method_condition")
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleRequestMethodCondition"], result)

    @builtins.property
    def request_scheme_condition(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleRequestSchemeCondition"]:
        '''request_scheme_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_scheme_condition CdnEndpoint#request_scheme_condition}
        '''
        result = self._values.get("request_scheme_condition")
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleRequestSchemeCondition"], result)

    @builtins.property
    def request_uri_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestUriCondition"]]]:
        '''request_uri_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#request_uri_condition CdnEndpoint#request_uri_condition}
        '''
        result = self._values.get("request_uri_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestUriCondition"]]], result)

    @builtins.property
    def url_file_extension_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlFileExtensionCondition"]]]:
        '''url_file_extension_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_file_extension_condition CdnEndpoint#url_file_extension_condition}
        '''
        result = self._values.get("url_file_extension_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlFileExtensionCondition"]]], result)

    @builtins.property
    def url_file_name_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlFileNameCondition"]]]:
        '''url_file_name_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_file_name_condition CdnEndpoint#url_file_name_condition}
        '''
        result = self._values.get("url_file_name_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlFileNameCondition"]]], result)

    @builtins.property
    def url_path_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlPathCondition"]]]:
        '''url_path_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_path_condition CdnEndpoint#url_path_condition}
        '''
        result = self._values.get("url_path_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlPathCondition"]]], result)

    @builtins.property
    def url_redirect_action(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleUrlRedirectAction"]:
        '''url_redirect_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_redirect_action CdnEndpoint#url_redirect_action}
        '''
        result = self._values.get("url_redirect_action")
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleUrlRedirectAction"], result)

    @builtins.property
    def url_rewrite_action(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleUrlRewriteAction"]:
        '''url_rewrite_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_rewrite_action CdnEndpoint#url_rewrite_action}
        '''
        result = self._values.get("url_rewrite_action")
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleUrlRewriteAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleCacheExpirationAction",
    jsii_struct_bases=[],
    name_mapping={"behavior": "behavior", "duration": "duration"},
)
class CdnEndpointDeliveryRuleCacheExpirationAction:
    def __init__(
        self,
        *,
        behavior: builtins.str,
        duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#duration CdnEndpoint#duration}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleCacheExpirationAction.__init__)
            check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
        self._values: typing.Dict[str, typing.Any] = {
            "behavior": behavior,
        }
        if duration is not None:
            self._values["duration"] = duration

    @builtins.property
    def behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.'''
        result = self._values.get("behavior")
        assert result is not None, "Required property 'behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#duration CdnEndpoint#duration}.'''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleCacheExpirationAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleCacheExpirationActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleCacheExpirationActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleCacheExpirationActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @builtins.property
    @jsii.member(jsii_name="behaviorInput")
    def behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "behaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="behavior")
    def behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behavior"))

    @behavior.setter
    def behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCacheExpirationActionOutputReference, "behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behavior", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCacheExpirationActionOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleCacheExpirationAction]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleCacheExpirationAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointDeliveryRuleCacheExpirationAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCacheExpirationActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleCacheKeyQueryStringAction",
    jsii_struct_bases=[],
    name_mapping={"behavior": "behavior", "parameters": "parameters"},
)
class CdnEndpointDeliveryRuleCacheKeyQueryStringAction:
    def __init__(
        self,
        *,
        behavior: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#parameters CdnEndpoint#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleCacheKeyQueryStringAction.__init__)
            check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "behavior": behavior,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.'''
        result = self._values.get("behavior")
        assert result is not None, "Required property 'behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#parameters CdnEndpoint#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleCacheKeyQueryStringAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="behaviorInput")
    def behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "behaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="behavior")
    def behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behavior"))

    @behavior.setter
    def behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference, "behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behavior", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleCacheKeyQueryStringAction]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleCacheKeyQueryStringAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointDeliveryRuleCacheKeyQueryStringAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleCookiesCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "selector": "selector",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRuleCookiesCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        selector: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#selector CdnEndpoint#selector}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleCookiesCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "selector": selector,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#selector CdnEndpoint#selector}.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleCookiesCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleCookiesConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleCookiesConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleCookiesConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleCookiesConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleCookiesConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleCookiesConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleCookiesCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleCookiesCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleCookiesCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleCookiesConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleCookiesConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleCookiesConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleCookiesCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleCookiesCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleCookiesCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleCookiesConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleDeviceCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnEndpointDeliveryRuleDeviceCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleDeviceCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleDeviceCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleDeviceConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleDeviceConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleDeviceConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleDeviceConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleDeviceConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleDeviceConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CdnEndpointDeliveryRuleDeviceCondition]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleDeviceCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointDeliveryRuleDeviceCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleDeviceConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleHttpVersionCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnEndpointDeliveryRuleHttpVersionCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleHttpVersionCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleHttpVersionCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleHttpVersionConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleHttpVersionConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleHttpVersionConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleHttpVersionConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleHttpVersionConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleHttpVersionConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleHttpVersionConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleHttpVersionConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleHttpVersionConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleHttpVersionCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleHttpVersionCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleHttpVersionCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleHttpVersionConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleHttpVersionConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleHttpVersionConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleHttpVersionConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleHttpVersionConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleHttpVersionConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleHttpVersionConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleHttpVersionCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleHttpVersionCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleHttpVersionCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleHttpVersionConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CdnEndpointDeliveryRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleModifyRequestHeaderAction",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "name": "name", "value": "value"},
)
class CdnEndpointDeliveryRuleModifyRequestHeaderAction:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#value CdnEndpoint#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleModifyRequestHeaderAction.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#value CdnEndpoint#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleModifyRequestHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleModifyRequestHeaderActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleModifyRequestHeaderActionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleModifyRequestHeaderActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleModifyRequestHeaderActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyRequestHeaderActionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyRequestHeaderActionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyRequestHeaderActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyRequestHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyRequestHeaderAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyRequestHeaderAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyRequestHeaderActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleModifyRequestHeaderAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleModifyRequestHeaderAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleModifyRequestHeaderAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleModifyResponseHeaderAction",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "name": "name", "value": "value"},
)
class CdnEndpointDeliveryRuleModifyResponseHeaderAction:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#value CdnEndpoint#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleModifyResponseHeaderAction.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#value CdnEndpoint#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleModifyResponseHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleModifyResponseHeaderActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleModifyResponseHeaderActionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleModifyResponseHeaderActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleModifyResponseHeaderActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyResponseHeaderActionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyResponseHeaderActionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyResponseHeaderActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyResponseHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyResponseHeaderAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyResponseHeaderAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyResponseHeaderActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleModifyResponseHeaderAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleModifyResponseHeaderAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleModifyResponseHeaderAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCacheExpirationAction")
    def put_cache_expiration_action(
        self,
        *,
        behavior: builtins.str,
        duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#duration CdnEndpoint#duration}.
        '''
        value = CdnEndpointDeliveryRuleCacheExpirationAction(
            behavior=behavior, duration=duration
        )

        return typing.cast(None, jsii.invoke(self, "putCacheExpirationAction", [value]))

    @jsii.member(jsii_name="putCacheKeyQueryStringAction")
    def put_cache_key_query_string_action(
        self,
        *,
        behavior: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#parameters CdnEndpoint#parameters}.
        '''
        value = CdnEndpointDeliveryRuleCacheKeyQueryStringAction(
            behavior=behavior, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putCacheKeyQueryStringAction", [value]))

    @jsii.member(jsii_name="putCookiesCondition")
    def put_cookies_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnEndpointDeliveryRuleCookiesCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_cookies_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCookiesCondition", [value]))

    @jsii.member(jsii_name="putDeviceCondition")
    def put_device_condition(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        '''
        value = CdnEndpointDeliveryRuleDeviceCondition(
            match_values=match_values,
            negate_condition=negate_condition,
            operator=operator,
        )

        return typing.cast(None, jsii.invoke(self, "putDeviceCondition", [value]))

    @jsii.member(jsii_name="putHttpVersionCondition")
    def put_http_version_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnEndpointDeliveryRuleHttpVersionCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_http_version_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpVersionCondition", [value]))

    @jsii.member(jsii_name="putModifyRequestHeaderAction")
    def put_modify_request_header_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnEndpointDeliveryRuleModifyRequestHeaderAction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_modify_request_header_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putModifyRequestHeaderAction", [value]))

    @jsii.member(jsii_name="putModifyResponseHeaderAction")
    def put_modify_response_header_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnEndpointDeliveryRuleModifyResponseHeaderAction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_modify_response_header_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putModifyResponseHeaderAction", [value]))

    @jsii.member(jsii_name="putPostArgCondition")
    def put_post_arg_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRulePostArgCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_post_arg_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostArgCondition", [value]))

    @jsii.member(jsii_name="putQueryStringCondition")
    def put_query_string_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleQueryStringCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_query_string_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryStringCondition", [value]))

    @jsii.member(jsii_name="putRemoteAddressCondition")
    def put_remote_address_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleRemoteAddressCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_remote_address_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRemoteAddressCondition", [value]))

    @jsii.member(jsii_name="putRequestBodyCondition")
    def put_request_body_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleRequestBodyCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_request_body_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestBodyCondition", [value]))

    @jsii.member(jsii_name="putRequestHeaderCondition")
    def put_request_header_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleRequestHeaderCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_request_header_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeaderCondition", [value]))

    @jsii.member(jsii_name="putRequestMethodCondition")
    def put_request_method_condition(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        '''
        value = CdnEndpointDeliveryRuleRequestMethodCondition(
            match_values=match_values,
            negate_condition=negate_condition,
            operator=operator,
        )

        return typing.cast(None, jsii.invoke(self, "putRequestMethodCondition", [value]))

    @jsii.member(jsii_name="putRequestSchemeCondition")
    def put_request_scheme_condition(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        '''
        value = CdnEndpointDeliveryRuleRequestSchemeCondition(
            match_values=match_values,
            negate_condition=negate_condition,
            operator=operator,
        )

        return typing.cast(None, jsii.invoke(self, "putRequestSchemeCondition", [value]))

    @jsii.member(jsii_name="putRequestUriCondition")
    def put_request_uri_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleRequestUriCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_request_uri_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestUriCondition", [value]))

    @jsii.member(jsii_name="putUrlFileExtensionCondition")
    def put_url_file_extension_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleUrlFileExtensionCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_url_file_extension_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlFileExtensionCondition", [value]))

    @jsii.member(jsii_name="putUrlFileNameCondition")
    def put_url_file_name_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleUrlFileNameCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_url_file_name_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlFileNameCondition", [value]))

    @jsii.member(jsii_name="putUrlPathCondition")
    def put_url_path_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointDeliveryRuleUrlPathCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleOutputReference.put_url_path_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlPathCondition", [value]))

    @jsii.member(jsii_name="putUrlRedirectAction")
    def put_url_redirect_action(
        self,
        *,
        redirect_type: builtins.str,
        fragment: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        query_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#redirect_type CdnEndpoint#redirect_type}.
        :param fragment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#fragment CdnEndpoint#fragment}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#hostname CdnEndpoint#hostname}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#path CdnEndpoint#path}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#protocol CdnEndpoint#protocol}.
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#query_string CdnEndpoint#query_string}.
        '''
        value = CdnEndpointDeliveryRuleUrlRedirectAction(
            redirect_type=redirect_type,
            fragment=fragment,
            hostname=hostname,
            path=path,
            protocol=protocol,
            query_string=query_string,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRedirectAction", [value]))

    @jsii.member(jsii_name="putUrlRewriteAction")
    def put_url_rewrite_action(
        self,
        *,
        destination: builtins.str,
        source_pattern: builtins.str,
        preserve_unmatched_path: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#destination CdnEndpoint#destination}.
        :param source_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#source_pattern CdnEndpoint#source_pattern}.
        :param preserve_unmatched_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#preserve_unmatched_path CdnEndpoint#preserve_unmatched_path}.
        '''
        value = CdnEndpointDeliveryRuleUrlRewriteAction(
            destination=destination,
            source_pattern=source_pattern,
            preserve_unmatched_path=preserve_unmatched_path,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRewriteAction", [value]))

    @jsii.member(jsii_name="resetCacheExpirationAction")
    def reset_cache_expiration_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheExpirationAction", []))

    @jsii.member(jsii_name="resetCacheKeyQueryStringAction")
    def reset_cache_key_query_string_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheKeyQueryStringAction", []))

    @jsii.member(jsii_name="resetCookiesCondition")
    def reset_cookies_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookiesCondition", []))

    @jsii.member(jsii_name="resetDeviceCondition")
    def reset_device_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceCondition", []))

    @jsii.member(jsii_name="resetHttpVersionCondition")
    def reset_http_version_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpVersionCondition", []))

    @jsii.member(jsii_name="resetModifyRequestHeaderAction")
    def reset_modify_request_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModifyRequestHeaderAction", []))

    @jsii.member(jsii_name="resetModifyResponseHeaderAction")
    def reset_modify_response_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModifyResponseHeaderAction", []))

    @jsii.member(jsii_name="resetPostArgCondition")
    def reset_post_arg_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostArgCondition", []))

    @jsii.member(jsii_name="resetQueryStringCondition")
    def reset_query_string_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringCondition", []))

    @jsii.member(jsii_name="resetRemoteAddressCondition")
    def reset_remote_address_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteAddressCondition", []))

    @jsii.member(jsii_name="resetRequestBodyCondition")
    def reset_request_body_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestBodyCondition", []))

    @jsii.member(jsii_name="resetRequestHeaderCondition")
    def reset_request_header_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeaderCondition", []))

    @jsii.member(jsii_name="resetRequestMethodCondition")
    def reset_request_method_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMethodCondition", []))

    @jsii.member(jsii_name="resetRequestSchemeCondition")
    def reset_request_scheme_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestSchemeCondition", []))

    @jsii.member(jsii_name="resetRequestUriCondition")
    def reset_request_uri_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestUriCondition", []))

    @jsii.member(jsii_name="resetUrlFileExtensionCondition")
    def reset_url_file_extension_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlFileExtensionCondition", []))

    @jsii.member(jsii_name="resetUrlFileNameCondition")
    def reset_url_file_name_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlFileNameCondition", []))

    @jsii.member(jsii_name="resetUrlPathCondition")
    def reset_url_path_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlPathCondition", []))

    @jsii.member(jsii_name="resetUrlRedirectAction")
    def reset_url_redirect_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRedirectAction", []))

    @jsii.member(jsii_name="resetUrlRewriteAction")
    def reset_url_rewrite_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRewriteAction", []))

    @builtins.property
    @jsii.member(jsii_name="cacheExpirationAction")
    def cache_expiration_action(
        self,
    ) -> CdnEndpointDeliveryRuleCacheExpirationActionOutputReference:
        return typing.cast(CdnEndpointDeliveryRuleCacheExpirationActionOutputReference, jsii.get(self, "cacheExpirationAction"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyQueryStringAction")
    def cache_key_query_string_action(
        self,
    ) -> CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference:
        return typing.cast(CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference, jsii.get(self, "cacheKeyQueryStringAction"))

    @builtins.property
    @jsii.member(jsii_name="cookiesCondition")
    def cookies_condition(self) -> CdnEndpointDeliveryRuleCookiesConditionList:
        return typing.cast(CdnEndpointDeliveryRuleCookiesConditionList, jsii.get(self, "cookiesCondition"))

    @builtins.property
    @jsii.member(jsii_name="deviceCondition")
    def device_condition(self) -> CdnEndpointDeliveryRuleDeviceConditionOutputReference:
        return typing.cast(CdnEndpointDeliveryRuleDeviceConditionOutputReference, jsii.get(self, "deviceCondition"))

    @builtins.property
    @jsii.member(jsii_name="httpVersionCondition")
    def http_version_condition(self) -> CdnEndpointDeliveryRuleHttpVersionConditionList:
        return typing.cast(CdnEndpointDeliveryRuleHttpVersionConditionList, jsii.get(self, "httpVersionCondition"))

    @builtins.property
    @jsii.member(jsii_name="modifyRequestHeaderAction")
    def modify_request_header_action(
        self,
    ) -> CdnEndpointDeliveryRuleModifyRequestHeaderActionList:
        return typing.cast(CdnEndpointDeliveryRuleModifyRequestHeaderActionList, jsii.get(self, "modifyRequestHeaderAction"))

    @builtins.property
    @jsii.member(jsii_name="modifyResponseHeaderAction")
    def modify_response_header_action(
        self,
    ) -> CdnEndpointDeliveryRuleModifyResponseHeaderActionList:
        return typing.cast(CdnEndpointDeliveryRuleModifyResponseHeaderActionList, jsii.get(self, "modifyResponseHeaderAction"))

    @builtins.property
    @jsii.member(jsii_name="postArgCondition")
    def post_arg_condition(self) -> "CdnEndpointDeliveryRulePostArgConditionList":
        return typing.cast("CdnEndpointDeliveryRulePostArgConditionList", jsii.get(self, "postArgCondition"))

    @builtins.property
    @jsii.member(jsii_name="queryStringCondition")
    def query_string_condition(
        self,
    ) -> "CdnEndpointDeliveryRuleQueryStringConditionList":
        return typing.cast("CdnEndpointDeliveryRuleQueryStringConditionList", jsii.get(self, "queryStringCondition"))

    @builtins.property
    @jsii.member(jsii_name="remoteAddressCondition")
    def remote_address_condition(
        self,
    ) -> "CdnEndpointDeliveryRuleRemoteAddressConditionList":
        return typing.cast("CdnEndpointDeliveryRuleRemoteAddressConditionList", jsii.get(self, "remoteAddressCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestBodyCondition")
    def request_body_condition(
        self,
    ) -> "CdnEndpointDeliveryRuleRequestBodyConditionList":
        return typing.cast("CdnEndpointDeliveryRuleRequestBodyConditionList", jsii.get(self, "requestBodyCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderCondition")
    def request_header_condition(
        self,
    ) -> "CdnEndpointDeliveryRuleRequestHeaderConditionList":
        return typing.cast("CdnEndpointDeliveryRuleRequestHeaderConditionList", jsii.get(self, "requestHeaderCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestMethodCondition")
    def request_method_condition(
        self,
    ) -> "CdnEndpointDeliveryRuleRequestMethodConditionOutputReference":
        return typing.cast("CdnEndpointDeliveryRuleRequestMethodConditionOutputReference", jsii.get(self, "requestMethodCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestSchemeCondition")
    def request_scheme_condition(
        self,
    ) -> "CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference":
        return typing.cast("CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference", jsii.get(self, "requestSchemeCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestUriCondition")
    def request_uri_condition(self) -> "CdnEndpointDeliveryRuleRequestUriConditionList":
        return typing.cast("CdnEndpointDeliveryRuleRequestUriConditionList", jsii.get(self, "requestUriCondition"))

    @builtins.property
    @jsii.member(jsii_name="urlFileExtensionCondition")
    def url_file_extension_condition(
        self,
    ) -> "CdnEndpointDeliveryRuleUrlFileExtensionConditionList":
        return typing.cast("CdnEndpointDeliveryRuleUrlFileExtensionConditionList", jsii.get(self, "urlFileExtensionCondition"))

    @builtins.property
    @jsii.member(jsii_name="urlFileNameCondition")
    def url_file_name_condition(
        self,
    ) -> "CdnEndpointDeliveryRuleUrlFileNameConditionList":
        return typing.cast("CdnEndpointDeliveryRuleUrlFileNameConditionList", jsii.get(self, "urlFileNameCondition"))

    @builtins.property
    @jsii.member(jsii_name="urlPathCondition")
    def url_path_condition(self) -> "CdnEndpointDeliveryRuleUrlPathConditionList":
        return typing.cast("CdnEndpointDeliveryRuleUrlPathConditionList", jsii.get(self, "urlPathCondition"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectAction")
    def url_redirect_action(
        self,
    ) -> "CdnEndpointDeliveryRuleUrlRedirectActionOutputReference":
        return typing.cast("CdnEndpointDeliveryRuleUrlRedirectActionOutputReference", jsii.get(self, "urlRedirectAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteAction")
    def url_rewrite_action(
        self,
    ) -> "CdnEndpointDeliveryRuleUrlRewriteActionOutputReference":
        return typing.cast("CdnEndpointDeliveryRuleUrlRewriteActionOutputReference", jsii.get(self, "urlRewriteAction"))

    @builtins.property
    @jsii.member(jsii_name="cacheExpirationActionInput")
    def cache_expiration_action_input(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleCacheExpirationAction]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleCacheExpirationAction], jsii.get(self, "cacheExpirationActionInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyQueryStringActionInput")
    def cache_key_query_string_action_input(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleCacheKeyQueryStringAction]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleCacheKeyQueryStringAction], jsii.get(self, "cacheKeyQueryStringActionInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesConditionInput")
    def cookies_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleCookiesCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleCookiesCondition]]], jsii.get(self, "cookiesConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceConditionInput")
    def device_condition_input(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleDeviceCondition]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleDeviceCondition], jsii.get(self, "deviceConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="httpVersionConditionInput")
    def http_version_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleHttpVersionCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleHttpVersionCondition]]], jsii.get(self, "httpVersionConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="modifyRequestHeaderActionInput")
    def modify_request_header_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyRequestHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyRequestHeaderAction]]], jsii.get(self, "modifyRequestHeaderActionInput"))

    @builtins.property
    @jsii.member(jsii_name="modifyResponseHeaderActionInput")
    def modify_response_header_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyResponseHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleModifyResponseHeaderAction]]], jsii.get(self, "modifyResponseHeaderActionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="postArgConditionInput")
    def post_arg_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRulePostArgCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRulePostArgCondition"]]], jsii.get(self, "postArgConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringConditionInput")
    def query_string_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleQueryStringCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleQueryStringCondition"]]], jsii.get(self, "queryStringConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteAddressConditionInput")
    def remote_address_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRemoteAddressCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRemoteAddressCondition"]]], jsii.get(self, "remoteAddressConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestBodyConditionInput")
    def request_body_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestBodyCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestBodyCondition"]]], jsii.get(self, "requestBodyConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderConditionInput")
    def request_header_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestHeaderCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestHeaderCondition"]]], jsii.get(self, "requestHeaderConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMethodConditionInput")
    def request_method_condition_input(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleRequestMethodCondition"]:
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleRequestMethodCondition"], jsii.get(self, "requestMethodConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestSchemeConditionInput")
    def request_scheme_condition_input(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleRequestSchemeCondition"]:
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleRequestSchemeCondition"], jsii.get(self, "requestSchemeConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestUriConditionInput")
    def request_uri_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestUriCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleRequestUriCondition"]]], jsii.get(self, "requestUriConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlFileExtensionConditionInput")
    def url_file_extension_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlFileExtensionCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlFileExtensionCondition"]]], jsii.get(self, "urlFileExtensionConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlFileNameConditionInput")
    def url_file_name_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlFileNameCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlFileNameCondition"]]], jsii.get(self, "urlFileNameConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlPathConditionInput")
    def url_path_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlPathCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointDeliveryRuleUrlPathCondition"]]], jsii.get(self, "urlPathConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectActionInput")
    def url_redirect_action_input(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleUrlRedirectAction"]:
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleUrlRedirectAction"], jsii.get(self, "urlRedirectActionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteActionInput")
    def url_rewrite_action_input(
        self,
    ) -> typing.Optional["CdnEndpointDeliveryRuleUrlRewriteAction"]:
        return typing.cast(typing.Optional["CdnEndpointDeliveryRuleUrlRewriteAction"], jsii.get(self, "urlRewriteActionInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "order"))

    @order.setter
    def order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleOutputReference, "order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRulePostArgCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "selector": "selector",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRulePostArgCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        selector: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#selector CdnEndpoint#selector}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRulePostArgCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "selector": selector,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#selector CdnEndpoint#selector}.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRulePostArgCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRulePostArgConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRulePostArgConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRulePostArgConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRulePostArgConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRulePostArgConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRulePostArgConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRulePostArgCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRulePostArgCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRulePostArgCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRulePostArgConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRulePostArgConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRulePostArgConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRulePostArgCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRulePostArgCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRulePostArgCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRulePostArgConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleQueryStringCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRuleQueryStringCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleQueryStringCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleQueryStringCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleQueryStringConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleQueryStringConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleQueryStringConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleQueryStringConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleQueryStringConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleQueryStringConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleQueryStringCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleQueryStringCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleQueryStringCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleQueryStringConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleQueryStringConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleQueryStringConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleQueryStringCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleQueryStringCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleQueryStringCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleQueryStringConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRemoteAddressCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
    },
)
class CdnEndpointDeliveryRuleRemoteAddressCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRemoteAddressCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleRemoteAddressCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleRemoteAddressConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRemoteAddressConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRemoteAddressConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRemoteAddressConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRemoteAddressConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRemoteAddressConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRemoteAddressConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRemoteAddressCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRemoteAddressCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRemoteAddressCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRemoteAddressConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleRemoteAddressCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleRemoteAddressCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleRemoteAddressCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestBodyCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRuleRequestBodyCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestBodyCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleRequestBodyCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleRequestBodyConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestBodyConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestBodyConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleRequestBodyConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestBodyConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleRequestBodyConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestBodyCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestBodyCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestBodyCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleRequestBodyConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestBodyConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestBodyConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestBodyCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestBodyCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestBodyCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestBodyConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestHeaderCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "selector": "selector",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRuleRequestHeaderCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        selector: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#selector CdnEndpoint#selector}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestHeaderCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "selector": selector,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#selector CdnEndpoint#selector}.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleRequestHeaderCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleRequestHeaderConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestHeaderConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestHeaderConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestHeaderConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestHeaderCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestHeaderCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestHeaderCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestHeaderCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestHeaderCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestHeaderCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestMethodCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnEndpointDeliveryRuleRequestMethodCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestMethodCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleRequestMethodCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleRequestMethodConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestMethodConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestMethodConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestMethodConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestMethodConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestMethodConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleRequestMethodCondition]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleRequestMethodCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointDeliveryRuleRequestMethodCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestMethodConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestSchemeCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnEndpointDeliveryRuleRequestSchemeCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestSchemeCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleRequestSchemeCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleRequestSchemeCondition]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleRequestSchemeCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointDeliveryRuleRequestSchemeCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestUriCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRuleRequestUriCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestUriCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleRequestUriCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleRequestUriConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestUriConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestUriConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleRequestUriConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestUriConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleRequestUriConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestUriCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestUriCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleRequestUriCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleRequestUriConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleRequestUriConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleRequestUriConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestUriCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestUriCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleRequestUriCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleRequestUriConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlFileExtensionCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRuleUrlFileExtensionCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlFileExtensionCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleUrlFileExtensionCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleUrlFileExtensionConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlFileExtensionConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlFileExtensionConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlFileExtensionConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlFileExtensionCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlFileExtensionCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlFileExtensionCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlFileExtensionCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlFileExtensionCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlFileExtensionCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlFileNameCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRuleUrlFileNameCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlFileNameCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleUrlFileNameCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleUrlFileNameConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlFileNameConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlFileNameConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlFileNameConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlFileNameCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlFileNameCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlFileNameCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlFileNameCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlFileNameCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlFileNameCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlPathCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnEndpointDeliveryRuleUrlPathCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlPathCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#operator CdnEndpoint#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#match_values CdnEndpoint#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#negate_condition CdnEndpoint#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#transforms CdnEndpoint#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleUrlPathCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleUrlPathConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlPathConditionList",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlPathConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointDeliveryRuleUrlPathConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlPathConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointDeliveryRuleUrlPathConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlPathCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlPathCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointDeliveryRuleUrlPathCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointDeliveryRuleUrlPathConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlPathConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlPathConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

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
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlPathCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlPathCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointDeliveryRuleUrlPathCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlPathConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlRedirectAction",
    jsii_struct_bases=[],
    name_mapping={
        "redirect_type": "redirectType",
        "fragment": "fragment",
        "hostname": "hostname",
        "path": "path",
        "protocol": "protocol",
        "query_string": "queryString",
    },
)
class CdnEndpointDeliveryRuleUrlRedirectAction:
    def __init__(
        self,
        *,
        redirect_type: builtins.str,
        fragment: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        query_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#redirect_type CdnEndpoint#redirect_type}.
        :param fragment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#fragment CdnEndpoint#fragment}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#hostname CdnEndpoint#hostname}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#path CdnEndpoint#path}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#protocol CdnEndpoint#protocol}.
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#query_string CdnEndpoint#query_string}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlRedirectAction.__init__)
            check_type(argname="argument redirect_type", value=redirect_type, expected_type=type_hints["redirect_type"])
            check_type(argname="argument fragment", value=fragment, expected_type=type_hints["fragment"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
        self._values: typing.Dict[str, typing.Any] = {
            "redirect_type": redirect_type,
        }
        if fragment is not None:
            self._values["fragment"] = fragment
        if hostname is not None:
            self._values["hostname"] = hostname
        if path is not None:
            self._values["path"] = path
        if protocol is not None:
            self._values["protocol"] = protocol
        if query_string is not None:
            self._values["query_string"] = query_string

    @builtins.property
    def redirect_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#redirect_type CdnEndpoint#redirect_type}.'''
        result = self._values.get("redirect_type")
        assert result is not None, "Required property 'redirect_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fragment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#fragment CdnEndpoint#fragment}.'''
        result = self._values.get("fragment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#hostname CdnEndpoint#hostname}.'''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#path CdnEndpoint#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#protocol CdnEndpoint#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#query_string CdnEndpoint#query_string}.'''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleUrlRedirectAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleUrlRedirectActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlRedirectActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlRedirectActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFragment")
    def reset_fragment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFragment", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @builtins.property
    @jsii.member(jsii_name="fragmentInput")
    def fragment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fragmentInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectTypeInput")
    def redirect_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fragment")
    def fragment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fragment"))

    @fragment.setter
    def fragment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRedirectActionOutputReference, "fragment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fragment", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRedirectActionOutputReference, "hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRedirectActionOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRedirectActionOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRedirectActionOutputReference, "query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="redirectType")
    def redirect_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectType"))

    @redirect_type.setter
    def redirect_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRedirectActionOutputReference, "redirect_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleUrlRedirectAction]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleUrlRedirectAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointDeliveryRuleUrlRedirectAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRedirectActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlRewriteAction",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "source_pattern": "sourcePattern",
        "preserve_unmatched_path": "preserveUnmatchedPath",
    },
)
class CdnEndpointDeliveryRuleUrlRewriteAction:
    def __init__(
        self,
        *,
        destination: builtins.str,
        source_pattern: builtins.str,
        preserve_unmatched_path: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#destination CdnEndpoint#destination}.
        :param source_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#source_pattern CdnEndpoint#source_pattern}.
        :param preserve_unmatched_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#preserve_unmatched_path CdnEndpoint#preserve_unmatched_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlRewriteAction.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument source_pattern", value=source_pattern, expected_type=type_hints["source_pattern"])
            check_type(argname="argument preserve_unmatched_path", value=preserve_unmatched_path, expected_type=type_hints["preserve_unmatched_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
            "source_pattern": source_pattern,
        }
        if preserve_unmatched_path is not None:
            self._values["preserve_unmatched_path"] = preserve_unmatched_path

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#destination CdnEndpoint#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_pattern(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#source_pattern CdnEndpoint#source_pattern}.'''
        result = self._values.get("source_pattern")
        assert result is not None, "Required property 'source_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preserve_unmatched_path(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#preserve_unmatched_path CdnEndpoint#preserve_unmatched_path}.'''
        result = self._values.get("preserve_unmatched_path")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointDeliveryRuleUrlRewriteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointDeliveryRuleUrlRewriteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointDeliveryRuleUrlRewriteActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointDeliveryRuleUrlRewriteActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPreserveUnmatchedPath")
    def reset_preserve_unmatched_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveUnmatchedPath", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveUnmatchedPathInput")
    def preserve_unmatched_path_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preserveUnmatchedPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePatternInput")
    def source_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePatternInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRewriteActionOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="preserveUnmatchedPath")
    def preserve_unmatched_path(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preserveUnmatchedPath"))

    @preserve_unmatched_path.setter
    def preserve_unmatched_path(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRewriteActionOutputReference, "preserve_unmatched_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveUnmatchedPath", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePattern")
    def source_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourcePattern"))

    @source_pattern.setter
    def source_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRewriteActionOutputReference, "source_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePattern", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointDeliveryRuleUrlRewriteAction]:
        return typing.cast(typing.Optional[CdnEndpointDeliveryRuleUrlRewriteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointDeliveryRuleUrlRewriteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointDeliveryRuleUrlRewriteActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGeoFilter",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "country_codes": "countryCodes",
        "relative_path": "relativePath",
    },
)
class CdnEndpointGeoFilter:
    def __init__(
        self,
        *,
        action: builtins.str,
        country_codes: typing.Sequence[builtins.str],
        relative_path: builtins.str,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.
        :param country_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#country_codes CdnEndpoint#country_codes}.
        :param relative_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#relative_path CdnEndpoint#relative_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGeoFilter.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument country_codes", value=country_codes, expected_type=type_hints["country_codes"])
            check_type(argname="argument relative_path", value=relative_path, expected_type=type_hints["relative_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "country_codes": country_codes,
            "relative_path": relative_path,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_codes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#country_codes CdnEndpoint#country_codes}.'''
        result = self._values.get("country_codes")
        assert result is not None, "Required property 'country_codes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def relative_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#relative_path CdnEndpoint#relative_path}.'''
        result = self._values.get("relative_path")
        assert result is not None, "Required property 'relative_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointGeoFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointGeoFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGeoFilterList",
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
            type_hints = typing.get_type_hints(CdnEndpointGeoFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CdnEndpointGeoFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGeoFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointGeoFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGeoFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointGeoFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointGeoFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGeoFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGeoFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGeoFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGeoFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointGeoFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGeoFilterOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointGeoFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodesInput")
    def country_codes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "countryCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="relativePathInput")
    def relative_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativePathInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGeoFilterOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="countryCodes")
    def country_codes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "countryCodes"))

    @country_codes.setter
    def country_codes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGeoFilterOutputReference, "country_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCodes", value)

    @builtins.property
    @jsii.member(jsii_name="relativePath")
    def relative_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativePath"))

    @relative_path.setter
    def relative_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGeoFilterOutputReference, "relative_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativePath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointGeoFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointGeoFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointGeoFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGeoFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRule",
    jsii_struct_bases=[],
    name_mapping={
        "cache_expiration_action": "cacheExpirationAction",
        "cache_key_query_string_action": "cacheKeyQueryStringAction",
        "modify_request_header_action": "modifyRequestHeaderAction",
        "modify_response_header_action": "modifyResponseHeaderAction",
        "url_redirect_action": "urlRedirectAction",
        "url_rewrite_action": "urlRewriteAction",
    },
)
class CdnEndpointGlobalDeliveryRule:
    def __init__(
        self,
        *,
        cache_expiration_action: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRuleCacheExpirationAction", typing.Dict[str, typing.Any]]] = None,
        cache_key_query_string_action: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction", typing.Dict[str, typing.Any]]] = None,
        modify_request_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        modify_response_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        url_redirect_action: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRuleUrlRedirectAction", typing.Dict[str, typing.Any]]] = None,
        url_rewrite_action: typing.Optional[typing.Union["CdnEndpointGlobalDeliveryRuleUrlRewriteAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cache_expiration_action: cache_expiration_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_expiration_action CdnEndpoint#cache_expiration_action}
        :param cache_key_query_string_action: cache_key_query_string_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_key_query_string_action CdnEndpoint#cache_key_query_string_action}
        :param modify_request_header_action: modify_request_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_request_header_action CdnEndpoint#modify_request_header_action}
        :param modify_response_header_action: modify_response_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_response_header_action CdnEndpoint#modify_response_header_action}
        :param url_redirect_action: url_redirect_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_redirect_action CdnEndpoint#url_redirect_action}
        :param url_rewrite_action: url_rewrite_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_rewrite_action CdnEndpoint#url_rewrite_action}
        '''
        if isinstance(cache_expiration_action, dict):
            cache_expiration_action = CdnEndpointGlobalDeliveryRuleCacheExpirationAction(**cache_expiration_action)
        if isinstance(cache_key_query_string_action, dict):
            cache_key_query_string_action = CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction(**cache_key_query_string_action)
        if isinstance(url_redirect_action, dict):
            url_redirect_action = CdnEndpointGlobalDeliveryRuleUrlRedirectAction(**url_redirect_action)
        if isinstance(url_rewrite_action, dict):
            url_rewrite_action = CdnEndpointGlobalDeliveryRuleUrlRewriteAction(**url_rewrite_action)
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRule.__init__)
            check_type(argname="argument cache_expiration_action", value=cache_expiration_action, expected_type=type_hints["cache_expiration_action"])
            check_type(argname="argument cache_key_query_string_action", value=cache_key_query_string_action, expected_type=type_hints["cache_key_query_string_action"])
            check_type(argname="argument modify_request_header_action", value=modify_request_header_action, expected_type=type_hints["modify_request_header_action"])
            check_type(argname="argument modify_response_header_action", value=modify_response_header_action, expected_type=type_hints["modify_response_header_action"])
            check_type(argname="argument url_redirect_action", value=url_redirect_action, expected_type=type_hints["url_redirect_action"])
            check_type(argname="argument url_rewrite_action", value=url_rewrite_action, expected_type=type_hints["url_rewrite_action"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cache_expiration_action is not None:
            self._values["cache_expiration_action"] = cache_expiration_action
        if cache_key_query_string_action is not None:
            self._values["cache_key_query_string_action"] = cache_key_query_string_action
        if modify_request_header_action is not None:
            self._values["modify_request_header_action"] = modify_request_header_action
        if modify_response_header_action is not None:
            self._values["modify_response_header_action"] = modify_response_header_action
        if url_redirect_action is not None:
            self._values["url_redirect_action"] = url_redirect_action
        if url_rewrite_action is not None:
            self._values["url_rewrite_action"] = url_rewrite_action

    @builtins.property
    def cache_expiration_action(
        self,
    ) -> typing.Optional["CdnEndpointGlobalDeliveryRuleCacheExpirationAction"]:
        '''cache_expiration_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_expiration_action CdnEndpoint#cache_expiration_action}
        '''
        result = self._values.get("cache_expiration_action")
        return typing.cast(typing.Optional["CdnEndpointGlobalDeliveryRuleCacheExpirationAction"], result)

    @builtins.property
    def cache_key_query_string_action(
        self,
    ) -> typing.Optional["CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction"]:
        '''cache_key_query_string_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#cache_key_query_string_action CdnEndpoint#cache_key_query_string_action}
        '''
        result = self._values.get("cache_key_query_string_action")
        return typing.cast(typing.Optional["CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction"], result)

    @builtins.property
    def modify_request_header_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction"]]]:
        '''modify_request_header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_request_header_action CdnEndpoint#modify_request_header_action}
        '''
        result = self._values.get("modify_request_header_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction"]]], result)

    @builtins.property
    def modify_response_header_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction"]]]:
        '''modify_response_header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#modify_response_header_action CdnEndpoint#modify_response_header_action}
        '''
        result = self._values.get("modify_response_header_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction"]]], result)

    @builtins.property
    def url_redirect_action(
        self,
    ) -> typing.Optional["CdnEndpointGlobalDeliveryRuleUrlRedirectAction"]:
        '''url_redirect_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_redirect_action CdnEndpoint#url_redirect_action}
        '''
        result = self._values.get("url_redirect_action")
        return typing.cast(typing.Optional["CdnEndpointGlobalDeliveryRuleUrlRedirectAction"], result)

    @builtins.property
    def url_rewrite_action(
        self,
    ) -> typing.Optional["CdnEndpointGlobalDeliveryRuleUrlRewriteAction"]:
        '''url_rewrite_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#url_rewrite_action CdnEndpoint#url_rewrite_action}
        '''
        result = self._values.get("url_rewrite_action")
        return typing.cast(typing.Optional["CdnEndpointGlobalDeliveryRuleUrlRewriteAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointGlobalDeliveryRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleCacheExpirationAction",
    jsii_struct_bases=[],
    name_mapping={"behavior": "behavior", "duration": "duration"},
)
class CdnEndpointGlobalDeliveryRuleCacheExpirationAction:
    def __init__(
        self,
        *,
        behavior: builtins.str,
        duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#duration CdnEndpoint#duration}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleCacheExpirationAction.__init__)
            check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
        self._values: typing.Dict[str, typing.Any] = {
            "behavior": behavior,
        }
        if duration is not None:
            self._values["duration"] = duration

    @builtins.property
    def behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.'''
        result = self._values.get("behavior")
        assert result is not None, "Required property 'behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#duration CdnEndpoint#duration}.'''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointGlobalDeliveryRuleCacheExpirationAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @builtins.property
    @jsii.member(jsii_name="behaviorInput")
    def behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "behaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="behavior")
    def behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behavior"))

    @behavior.setter
    def behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference, "behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behavior", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointGlobalDeliveryRuleCacheExpirationAction]:
        return typing.cast(typing.Optional[CdnEndpointGlobalDeliveryRuleCacheExpirationAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointGlobalDeliveryRuleCacheExpirationAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction",
    jsii_struct_bases=[],
    name_mapping={"behavior": "behavior", "parameters": "parameters"},
)
class CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction:
    def __init__(
        self,
        *,
        behavior: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#parameters CdnEndpoint#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction.__init__)
            check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "behavior": behavior,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.'''
        result = self._values.get("behavior")
        assert result is not None, "Required property 'behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#parameters CdnEndpoint#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="behaviorInput")
    def behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "behaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="behavior")
    def behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behavior"))

    @behavior.setter
    def behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference, "behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behavior", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction]:
        return typing.cast(typing.Optional[CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "name": "name", "value": "value"},
)
class CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#value CdnEndpoint#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#value CdnEndpoint#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "name": "name", "value": "value"},
)
class CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#value CdnEndpoint#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#action CdnEndpoint#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#value CdnEndpoint#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointGlobalDeliveryRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCacheExpirationAction")
    def put_cache_expiration_action(
        self,
        *,
        behavior: builtins.str,
        duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#duration CdnEndpoint#duration}.
        '''
        value = CdnEndpointGlobalDeliveryRuleCacheExpirationAction(
            behavior=behavior, duration=duration
        )

        return typing.cast(None, jsii.invoke(self, "putCacheExpirationAction", [value]))

    @jsii.member(jsii_name="putCacheKeyQueryStringAction")
    def put_cache_key_query_string_action(
        self,
        *,
        behavior: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#behavior CdnEndpoint#behavior}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#parameters CdnEndpoint#parameters}.
        '''
        value = CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction(
            behavior=behavior, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putCacheKeyQueryStringAction", [value]))

    @jsii.member(jsii_name="putModifyRequestHeaderAction")
    def put_modify_request_header_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleOutputReference.put_modify_request_header_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putModifyRequestHeaderAction", [value]))

    @jsii.member(jsii_name="putModifyResponseHeaderAction")
    def put_modify_response_header_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleOutputReference.put_modify_response_header_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putModifyResponseHeaderAction", [value]))

    @jsii.member(jsii_name="putUrlRedirectAction")
    def put_url_redirect_action(
        self,
        *,
        redirect_type: builtins.str,
        fragment: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        query_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#redirect_type CdnEndpoint#redirect_type}.
        :param fragment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#fragment CdnEndpoint#fragment}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#hostname CdnEndpoint#hostname}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#path CdnEndpoint#path}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#protocol CdnEndpoint#protocol}.
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#query_string CdnEndpoint#query_string}.
        '''
        value = CdnEndpointGlobalDeliveryRuleUrlRedirectAction(
            redirect_type=redirect_type,
            fragment=fragment,
            hostname=hostname,
            path=path,
            protocol=protocol,
            query_string=query_string,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRedirectAction", [value]))

    @jsii.member(jsii_name="putUrlRewriteAction")
    def put_url_rewrite_action(
        self,
        *,
        destination: builtins.str,
        source_pattern: builtins.str,
        preserve_unmatched_path: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#destination CdnEndpoint#destination}.
        :param source_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#source_pattern CdnEndpoint#source_pattern}.
        :param preserve_unmatched_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#preserve_unmatched_path CdnEndpoint#preserve_unmatched_path}.
        '''
        value = CdnEndpointGlobalDeliveryRuleUrlRewriteAction(
            destination=destination,
            source_pattern=source_pattern,
            preserve_unmatched_path=preserve_unmatched_path,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRewriteAction", [value]))

    @jsii.member(jsii_name="resetCacheExpirationAction")
    def reset_cache_expiration_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheExpirationAction", []))

    @jsii.member(jsii_name="resetCacheKeyQueryStringAction")
    def reset_cache_key_query_string_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheKeyQueryStringAction", []))

    @jsii.member(jsii_name="resetModifyRequestHeaderAction")
    def reset_modify_request_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModifyRequestHeaderAction", []))

    @jsii.member(jsii_name="resetModifyResponseHeaderAction")
    def reset_modify_response_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModifyResponseHeaderAction", []))

    @jsii.member(jsii_name="resetUrlRedirectAction")
    def reset_url_redirect_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRedirectAction", []))

    @jsii.member(jsii_name="resetUrlRewriteAction")
    def reset_url_rewrite_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRewriteAction", []))

    @builtins.property
    @jsii.member(jsii_name="cacheExpirationAction")
    def cache_expiration_action(
        self,
    ) -> CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference:
        return typing.cast(CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference, jsii.get(self, "cacheExpirationAction"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyQueryStringAction")
    def cache_key_query_string_action(
        self,
    ) -> CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference:
        return typing.cast(CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference, jsii.get(self, "cacheKeyQueryStringAction"))

    @builtins.property
    @jsii.member(jsii_name="modifyRequestHeaderAction")
    def modify_request_header_action(
        self,
    ) -> CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList:
        return typing.cast(CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList, jsii.get(self, "modifyRequestHeaderAction"))

    @builtins.property
    @jsii.member(jsii_name="modifyResponseHeaderAction")
    def modify_response_header_action(
        self,
    ) -> CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList:
        return typing.cast(CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList, jsii.get(self, "modifyResponseHeaderAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectAction")
    def url_redirect_action(
        self,
    ) -> "CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference":
        return typing.cast("CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference", jsii.get(self, "urlRedirectAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteAction")
    def url_rewrite_action(
        self,
    ) -> "CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference":
        return typing.cast("CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference", jsii.get(self, "urlRewriteAction"))

    @builtins.property
    @jsii.member(jsii_name="cacheExpirationActionInput")
    def cache_expiration_action_input(
        self,
    ) -> typing.Optional[CdnEndpointGlobalDeliveryRuleCacheExpirationAction]:
        return typing.cast(typing.Optional[CdnEndpointGlobalDeliveryRuleCacheExpirationAction], jsii.get(self, "cacheExpirationActionInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyQueryStringActionInput")
    def cache_key_query_string_action_input(
        self,
    ) -> typing.Optional[CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction]:
        return typing.cast(typing.Optional[CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction], jsii.get(self, "cacheKeyQueryStringActionInput"))

    @builtins.property
    @jsii.member(jsii_name="modifyRequestHeaderActionInput")
    def modify_request_header_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction]]], jsii.get(self, "modifyRequestHeaderActionInput"))

    @builtins.property
    @jsii.member(jsii_name="modifyResponseHeaderActionInput")
    def modify_response_header_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction]]], jsii.get(self, "modifyResponseHeaderActionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectActionInput")
    def url_redirect_action_input(
        self,
    ) -> typing.Optional["CdnEndpointGlobalDeliveryRuleUrlRedirectAction"]:
        return typing.cast(typing.Optional["CdnEndpointGlobalDeliveryRuleUrlRedirectAction"], jsii.get(self, "urlRedirectActionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteActionInput")
    def url_rewrite_action_input(
        self,
    ) -> typing.Optional["CdnEndpointGlobalDeliveryRuleUrlRewriteAction"]:
        return typing.cast(typing.Optional["CdnEndpointGlobalDeliveryRuleUrlRewriteAction"], jsii.get(self, "urlRewriteActionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CdnEndpointGlobalDeliveryRule]:
        return typing.cast(typing.Optional[CdnEndpointGlobalDeliveryRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointGlobalDeliveryRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleUrlRedirectAction",
    jsii_struct_bases=[],
    name_mapping={
        "redirect_type": "redirectType",
        "fragment": "fragment",
        "hostname": "hostname",
        "path": "path",
        "protocol": "protocol",
        "query_string": "queryString",
    },
)
class CdnEndpointGlobalDeliveryRuleUrlRedirectAction:
    def __init__(
        self,
        *,
        redirect_type: builtins.str,
        fragment: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        query_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#redirect_type CdnEndpoint#redirect_type}.
        :param fragment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#fragment CdnEndpoint#fragment}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#hostname CdnEndpoint#hostname}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#path CdnEndpoint#path}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#protocol CdnEndpoint#protocol}.
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#query_string CdnEndpoint#query_string}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleUrlRedirectAction.__init__)
            check_type(argname="argument redirect_type", value=redirect_type, expected_type=type_hints["redirect_type"])
            check_type(argname="argument fragment", value=fragment, expected_type=type_hints["fragment"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
        self._values: typing.Dict[str, typing.Any] = {
            "redirect_type": redirect_type,
        }
        if fragment is not None:
            self._values["fragment"] = fragment
        if hostname is not None:
            self._values["hostname"] = hostname
        if path is not None:
            self._values["path"] = path
        if protocol is not None:
            self._values["protocol"] = protocol
        if query_string is not None:
            self._values["query_string"] = query_string

    @builtins.property
    def redirect_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#redirect_type CdnEndpoint#redirect_type}.'''
        result = self._values.get("redirect_type")
        assert result is not None, "Required property 'redirect_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fragment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#fragment CdnEndpoint#fragment}.'''
        result = self._values.get("fragment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#hostname CdnEndpoint#hostname}.'''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#path CdnEndpoint#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#protocol CdnEndpoint#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#query_string CdnEndpoint#query_string}.'''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointGlobalDeliveryRuleUrlRedirectAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFragment")
    def reset_fragment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFragment", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @builtins.property
    @jsii.member(jsii_name="fragmentInput")
    def fragment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fragmentInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectTypeInput")
    def redirect_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fragment")
    def fragment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fragment"))

    @fragment.setter
    def fragment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference, "fragment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fragment", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference, "hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference, "query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="redirectType")
    def redirect_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectType"))

    @redirect_type.setter
    def redirect_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference, "redirect_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointGlobalDeliveryRuleUrlRedirectAction]:
        return typing.cast(typing.Optional[CdnEndpointGlobalDeliveryRuleUrlRedirectAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointGlobalDeliveryRuleUrlRedirectAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleUrlRewriteAction",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "source_pattern": "sourcePattern",
        "preserve_unmatched_path": "preserveUnmatchedPath",
    },
)
class CdnEndpointGlobalDeliveryRuleUrlRewriteAction:
    def __init__(
        self,
        *,
        destination: builtins.str,
        source_pattern: builtins.str,
        preserve_unmatched_path: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#destination CdnEndpoint#destination}.
        :param source_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#source_pattern CdnEndpoint#source_pattern}.
        :param preserve_unmatched_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#preserve_unmatched_path CdnEndpoint#preserve_unmatched_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleUrlRewriteAction.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument source_pattern", value=source_pattern, expected_type=type_hints["source_pattern"])
            check_type(argname="argument preserve_unmatched_path", value=preserve_unmatched_path, expected_type=type_hints["preserve_unmatched_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
            "source_pattern": source_pattern,
        }
        if preserve_unmatched_path is not None:
            self._values["preserve_unmatched_path"] = preserve_unmatched_path

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#destination CdnEndpoint#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_pattern(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#source_pattern CdnEndpoint#source_pattern}.'''
        result = self._values.get("source_pattern")
        assert result is not None, "Required property 'source_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preserve_unmatched_path(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#preserve_unmatched_path CdnEndpoint#preserve_unmatched_path}.'''
        result = self._values.get("preserve_unmatched_path")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointGlobalDeliveryRuleUrlRewriteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPreserveUnmatchedPath")
    def reset_preserve_unmatched_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveUnmatchedPath", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveUnmatchedPathInput")
    def preserve_unmatched_path_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preserveUnmatchedPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePatternInput")
    def source_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePatternInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="preserveUnmatchedPath")
    def preserve_unmatched_path(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preserveUnmatchedPath"))

    @preserve_unmatched_path.setter
    def preserve_unmatched_path(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference, "preserve_unmatched_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveUnmatchedPath", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePattern")
    def source_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourcePattern"))

    @source_pattern.setter
    def source_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference, "source_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePattern", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnEndpointGlobalDeliveryRuleUrlRewriteAction]:
        return typing.cast(typing.Optional[CdnEndpointGlobalDeliveryRuleUrlRewriteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnEndpointGlobalDeliveryRuleUrlRewriteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointOrigin",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "name": "name",
        "http_port": "httpPort",
        "https_port": "httpsPort",
    },
)
class CdnEndpointOrigin:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        name: builtins.str,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#host_name CdnEndpoint#host_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.
        :param http_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#http_port CdnEndpoint#http_port}.
        :param https_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#https_port CdnEndpoint#https_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointOrigin.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
            "name": name,
        }
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#host_name CdnEndpoint#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#name CdnEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#http_port CdnEndpoint#http_port}.'''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#https_port CdnEndpoint#https_port}.'''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointOrigin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointOriginList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointOriginList",
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
            type_hints = typing.get_type_hints(CdnEndpointOriginList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CdnEndpointOriginOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointOriginList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnEndpointOriginOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointOrigin]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointOrigin]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnEndpointOrigin]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnEndpointOriginOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointOriginOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointOriginOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHttpPort")
    def reset_http_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpPort", []))

    @jsii.member(jsii_name="resetHttpsPort")
    def reset_https_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsPort", []))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="httpPortInput")
    def http_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpPortInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsPortInput")
    def https_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpsPortInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="httpPort")
    def http_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPort"))

    @http_port.setter
    def http_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginOutputReference, "http_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPort", value)

    @builtins.property
    @jsii.member(jsii_name="httpsPort")
    def https_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpsPort"))

    @https_port.setter
    def https_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginOutputReference, "https_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsPort", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointOrigin, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointOrigin, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointOrigin, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointOriginOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CdnEndpointTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#create CdnEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#delete CdnEndpoint#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#read CdnEndpoint#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#update CdnEndpoint#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnEndpointTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#create CdnEndpoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#delete CdnEndpoint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#read CdnEndpoint#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint#update CdnEndpoint#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnEndpointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnEndpointTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnEndpoint.CdnEndpointTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CdnEndpointTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CdnEndpointTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnEndpointTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnEndpointTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnEndpointTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnEndpointTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CdnEndpoint",
    "CdnEndpointConfig",
    "CdnEndpointDeliveryRule",
    "CdnEndpointDeliveryRuleCacheExpirationAction",
    "CdnEndpointDeliveryRuleCacheExpirationActionOutputReference",
    "CdnEndpointDeliveryRuleCacheKeyQueryStringAction",
    "CdnEndpointDeliveryRuleCacheKeyQueryStringActionOutputReference",
    "CdnEndpointDeliveryRuleCookiesCondition",
    "CdnEndpointDeliveryRuleCookiesConditionList",
    "CdnEndpointDeliveryRuleCookiesConditionOutputReference",
    "CdnEndpointDeliveryRuleDeviceCondition",
    "CdnEndpointDeliveryRuleDeviceConditionOutputReference",
    "CdnEndpointDeliveryRuleHttpVersionCondition",
    "CdnEndpointDeliveryRuleHttpVersionConditionList",
    "CdnEndpointDeliveryRuleHttpVersionConditionOutputReference",
    "CdnEndpointDeliveryRuleList",
    "CdnEndpointDeliveryRuleModifyRequestHeaderAction",
    "CdnEndpointDeliveryRuleModifyRequestHeaderActionList",
    "CdnEndpointDeliveryRuleModifyRequestHeaderActionOutputReference",
    "CdnEndpointDeliveryRuleModifyResponseHeaderAction",
    "CdnEndpointDeliveryRuleModifyResponseHeaderActionList",
    "CdnEndpointDeliveryRuleModifyResponseHeaderActionOutputReference",
    "CdnEndpointDeliveryRuleOutputReference",
    "CdnEndpointDeliveryRulePostArgCondition",
    "CdnEndpointDeliveryRulePostArgConditionList",
    "CdnEndpointDeliveryRulePostArgConditionOutputReference",
    "CdnEndpointDeliveryRuleQueryStringCondition",
    "CdnEndpointDeliveryRuleQueryStringConditionList",
    "CdnEndpointDeliveryRuleQueryStringConditionOutputReference",
    "CdnEndpointDeliveryRuleRemoteAddressCondition",
    "CdnEndpointDeliveryRuleRemoteAddressConditionList",
    "CdnEndpointDeliveryRuleRemoteAddressConditionOutputReference",
    "CdnEndpointDeliveryRuleRequestBodyCondition",
    "CdnEndpointDeliveryRuleRequestBodyConditionList",
    "CdnEndpointDeliveryRuleRequestBodyConditionOutputReference",
    "CdnEndpointDeliveryRuleRequestHeaderCondition",
    "CdnEndpointDeliveryRuleRequestHeaderConditionList",
    "CdnEndpointDeliveryRuleRequestHeaderConditionOutputReference",
    "CdnEndpointDeliveryRuleRequestMethodCondition",
    "CdnEndpointDeliveryRuleRequestMethodConditionOutputReference",
    "CdnEndpointDeliveryRuleRequestSchemeCondition",
    "CdnEndpointDeliveryRuleRequestSchemeConditionOutputReference",
    "CdnEndpointDeliveryRuleRequestUriCondition",
    "CdnEndpointDeliveryRuleRequestUriConditionList",
    "CdnEndpointDeliveryRuleRequestUriConditionOutputReference",
    "CdnEndpointDeliveryRuleUrlFileExtensionCondition",
    "CdnEndpointDeliveryRuleUrlFileExtensionConditionList",
    "CdnEndpointDeliveryRuleUrlFileExtensionConditionOutputReference",
    "CdnEndpointDeliveryRuleUrlFileNameCondition",
    "CdnEndpointDeliveryRuleUrlFileNameConditionList",
    "CdnEndpointDeliveryRuleUrlFileNameConditionOutputReference",
    "CdnEndpointDeliveryRuleUrlPathCondition",
    "CdnEndpointDeliveryRuleUrlPathConditionList",
    "CdnEndpointDeliveryRuleUrlPathConditionOutputReference",
    "CdnEndpointDeliveryRuleUrlRedirectAction",
    "CdnEndpointDeliveryRuleUrlRedirectActionOutputReference",
    "CdnEndpointDeliveryRuleUrlRewriteAction",
    "CdnEndpointDeliveryRuleUrlRewriteActionOutputReference",
    "CdnEndpointGeoFilter",
    "CdnEndpointGeoFilterList",
    "CdnEndpointGeoFilterOutputReference",
    "CdnEndpointGlobalDeliveryRule",
    "CdnEndpointGlobalDeliveryRuleCacheExpirationAction",
    "CdnEndpointGlobalDeliveryRuleCacheExpirationActionOutputReference",
    "CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringAction",
    "CdnEndpointGlobalDeliveryRuleCacheKeyQueryStringActionOutputReference",
    "CdnEndpointGlobalDeliveryRuleModifyRequestHeaderAction",
    "CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionList",
    "CdnEndpointGlobalDeliveryRuleModifyRequestHeaderActionOutputReference",
    "CdnEndpointGlobalDeliveryRuleModifyResponseHeaderAction",
    "CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionList",
    "CdnEndpointGlobalDeliveryRuleModifyResponseHeaderActionOutputReference",
    "CdnEndpointGlobalDeliveryRuleOutputReference",
    "CdnEndpointGlobalDeliveryRuleUrlRedirectAction",
    "CdnEndpointGlobalDeliveryRuleUrlRedirectActionOutputReference",
    "CdnEndpointGlobalDeliveryRuleUrlRewriteAction",
    "CdnEndpointGlobalDeliveryRuleUrlRewriteActionOutputReference",
    "CdnEndpointOrigin",
    "CdnEndpointOriginList",
    "CdnEndpointOriginOutputReference",
    "CdnEndpointTimeouts",
    "CdnEndpointTimeoutsOutputReference",
]

publication.publish()
