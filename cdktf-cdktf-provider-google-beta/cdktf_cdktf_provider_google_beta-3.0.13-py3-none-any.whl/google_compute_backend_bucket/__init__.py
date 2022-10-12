'''
# `google_compute_backend_bucket`

Refer to the Terraform Registory for docs: [`google_compute_backend_bucket`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket).
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


class GoogleComputeBackendBucket(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucket",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket google_compute_backend_bucket}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        bucket_name: builtins.str,
        name: builtins.str,
        cdn_policy: typing.Optional[typing.Union["GoogleComputeBackendBucketCdnPolicy", typing.Dict[str, typing.Any]]] = None,
        compression_mode: typing.Optional[builtins.str] = None,
        custom_response_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        edge_security_policy: typing.Optional[builtins.str] = None,
        enable_cdn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeBackendBucketTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket google_compute_backend_bucket} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket_name: Cloud Storage bucket name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#bucket_name GoogleComputeBackendBucket#bucket_name}
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#name GoogleComputeBackendBucket#name}
        :param cdn_policy: cdn_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cdn_policy GoogleComputeBackendBucket#cdn_policy}
        :param compression_mode: Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header. Possible values: ["AUTOMATIC", "DISABLED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#compression_mode GoogleComputeBackendBucket#compression_mode}
        :param custom_response_headers: Headers that the HTTP/S load balancer should add to proxied responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#custom_response_headers GoogleComputeBackendBucket#custom_response_headers}
        :param description: An optional textual description of the resource; provided by the client when the resource is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#description GoogleComputeBackendBucket#description}
        :param edge_security_policy: The security policy associated with this backend bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#edge_security_policy GoogleComputeBackendBucket#edge_security_policy}
        :param enable_cdn: If true, enable Cloud CDN for this BackendBucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#enable_cdn GoogleComputeBackendBucket#enable_cdn}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#id GoogleComputeBackendBucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#project GoogleComputeBackendBucket#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#timeouts GoogleComputeBackendBucket#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucket.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeBackendBucketConfig(
            bucket_name=bucket_name,
            name=name,
            cdn_policy=cdn_policy,
            compression_mode=compression_mode,
            custom_response_headers=custom_response_headers,
            description=description,
            edge_security_policy=edge_security_policy,
            enable_cdn=enable_cdn,
            id=id,
            project=project,
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

    @jsii.member(jsii_name="putCdnPolicy")
    def put_cdn_policy(
        self,
        *,
        bypass_cache_on_request_headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders", typing.Dict[str, typing.Any]]]]] = None,
        cache_key_policy: typing.Optional[typing.Union["GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy", typing.Dict[str, typing.Any]]] = None,
        cache_mode: typing.Optional[builtins.str] = None,
        client_ttl: typing.Optional[jsii.Number] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        negative_caching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        negative_caching_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy", typing.Dict[str, typing.Any]]]]] = None,
        request_coalescing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        serve_while_stale: typing.Optional[jsii.Number] = None,
        signed_url_cache_max_age_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param bypass_cache_on_request_headers: bypass_cache_on_request_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#bypass_cache_on_request_headers GoogleComputeBackendBucket#bypass_cache_on_request_headers}
        :param cache_key_policy: cache_key_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cache_key_policy GoogleComputeBackendBucket#cache_key_policy}
        :param cache_mode: Specifies the cache setting for all responses from this backend. The possible values are: USE_ORIGIN_HEADERS, FORCE_CACHE_ALL and CACHE_ALL_STATIC Possible values: ["USE_ORIGIN_HEADERS", "FORCE_CACHE_ALL", "CACHE_ALL_STATIC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cache_mode GoogleComputeBackendBucket#cache_mode}
        :param client_ttl: Specifies the maximum allowed TTL for cached content served by this origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#client_ttl GoogleComputeBackendBucket#client_ttl}
        :param default_ttl: Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-max-age). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#default_ttl GoogleComputeBackendBucket#default_ttl}
        :param max_ttl: Specifies the maximum allowed TTL for cached content served by this origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#max_ttl GoogleComputeBackendBucket#max_ttl}
        :param negative_caching: Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#negative_caching GoogleComputeBackendBucket#negative_caching}
        :param negative_caching_policy: negative_caching_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#negative_caching_policy GoogleComputeBackendBucket#negative_caching_policy}
        :param request_coalescing: If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#request_coalescing GoogleComputeBackendBucket#request_coalescing}
        :param serve_while_stale: Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#serve_while_stale GoogleComputeBackendBucket#serve_while_stale}
        :param signed_url_cache_max_age_sec: Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served. When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a "Cache-Control: public, max-age=[TTL]" header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#signed_url_cache_max_age_sec GoogleComputeBackendBucket#signed_url_cache_max_age_sec}
        '''
        value = GoogleComputeBackendBucketCdnPolicy(
            bypass_cache_on_request_headers=bypass_cache_on_request_headers,
            cache_key_policy=cache_key_policy,
            cache_mode=cache_mode,
            client_ttl=client_ttl,
            default_ttl=default_ttl,
            max_ttl=max_ttl,
            negative_caching=negative_caching,
            negative_caching_policy=negative_caching_policy,
            request_coalescing=request_coalescing,
            serve_while_stale=serve_while_stale,
            signed_url_cache_max_age_sec=signed_url_cache_max_age_sec,
        )

        return typing.cast(None, jsii.invoke(self, "putCdnPolicy", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#create GoogleComputeBackendBucket#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#delete GoogleComputeBackendBucket#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#update GoogleComputeBackendBucket#update}.
        '''
        value = GoogleComputeBackendBucketTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCdnPolicy")
    def reset_cdn_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdnPolicy", []))

    @jsii.member(jsii_name="resetCompressionMode")
    def reset_compression_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionMode", []))

    @jsii.member(jsii_name="resetCustomResponseHeaders")
    def reset_custom_response_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomResponseHeaders", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEdgeSecurityPolicy")
    def reset_edge_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeSecurityPolicy", []))

    @jsii.member(jsii_name="resetEnableCdn")
    def reset_enable_cdn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableCdn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="cdnPolicy")
    def cdn_policy(self) -> "GoogleComputeBackendBucketCdnPolicyOutputReference":
        return typing.cast("GoogleComputeBackendBucketCdnPolicyOutputReference", jsii.get(self, "cdnPolicy"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeBackendBucketTimeoutsOutputReference":
        return typing.cast("GoogleComputeBackendBucketTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnPolicyInput")
    def cdn_policy_input(
        self,
    ) -> typing.Optional["GoogleComputeBackendBucketCdnPolicy"]:
        return typing.cast(typing.Optional["GoogleComputeBackendBucketCdnPolicy"], jsii.get(self, "cdnPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionModeInput")
    def compression_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="customResponseHeadersInput")
    def custom_response_headers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customResponseHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeSecurityPolicyInput")
    def edge_security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeSecurityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="enableCdnInput")
    def enable_cdn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableCdnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeBackendBucketTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeBackendBucketTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="compressionMode")
    def compression_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionMode"))

    @compression_mode.setter
    def compression_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "compression_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionMode", value)

    @builtins.property
    @jsii.member(jsii_name="customResponseHeaders")
    def custom_response_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customResponseHeaders"))

    @custom_response_headers.setter
    def custom_response_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "custom_response_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customResponseHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="edgeSecurityPolicy")
    def edge_security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeSecurityPolicy"))

    @edge_security_policy.setter
    def edge_security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "edge_security_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeSecurityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="enableCdn")
    def enable_cdn(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableCdn"))

    @enable_cdn.setter
    def enable_cdn(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "enable_cdn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCdn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucket, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "bypass_cache_on_request_headers": "bypassCacheOnRequestHeaders",
        "cache_key_policy": "cacheKeyPolicy",
        "cache_mode": "cacheMode",
        "client_ttl": "clientTtl",
        "default_ttl": "defaultTtl",
        "max_ttl": "maxTtl",
        "negative_caching": "negativeCaching",
        "negative_caching_policy": "negativeCachingPolicy",
        "request_coalescing": "requestCoalescing",
        "serve_while_stale": "serveWhileStale",
        "signed_url_cache_max_age_sec": "signedUrlCacheMaxAgeSec",
    },
)
class GoogleComputeBackendBucketCdnPolicy:
    def __init__(
        self,
        *,
        bypass_cache_on_request_headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders", typing.Dict[str, typing.Any]]]]] = None,
        cache_key_policy: typing.Optional[typing.Union["GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy", typing.Dict[str, typing.Any]]] = None,
        cache_mode: typing.Optional[builtins.str] = None,
        client_ttl: typing.Optional[jsii.Number] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        negative_caching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        negative_caching_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy", typing.Dict[str, typing.Any]]]]] = None,
        request_coalescing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        serve_while_stale: typing.Optional[jsii.Number] = None,
        signed_url_cache_max_age_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param bypass_cache_on_request_headers: bypass_cache_on_request_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#bypass_cache_on_request_headers GoogleComputeBackendBucket#bypass_cache_on_request_headers}
        :param cache_key_policy: cache_key_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cache_key_policy GoogleComputeBackendBucket#cache_key_policy}
        :param cache_mode: Specifies the cache setting for all responses from this backend. The possible values are: USE_ORIGIN_HEADERS, FORCE_CACHE_ALL and CACHE_ALL_STATIC Possible values: ["USE_ORIGIN_HEADERS", "FORCE_CACHE_ALL", "CACHE_ALL_STATIC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cache_mode GoogleComputeBackendBucket#cache_mode}
        :param client_ttl: Specifies the maximum allowed TTL for cached content served by this origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#client_ttl GoogleComputeBackendBucket#client_ttl}
        :param default_ttl: Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-max-age). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#default_ttl GoogleComputeBackendBucket#default_ttl}
        :param max_ttl: Specifies the maximum allowed TTL for cached content served by this origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#max_ttl GoogleComputeBackendBucket#max_ttl}
        :param negative_caching: Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#negative_caching GoogleComputeBackendBucket#negative_caching}
        :param negative_caching_policy: negative_caching_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#negative_caching_policy GoogleComputeBackendBucket#negative_caching_policy}
        :param request_coalescing: If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#request_coalescing GoogleComputeBackendBucket#request_coalescing}
        :param serve_while_stale: Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#serve_while_stale GoogleComputeBackendBucket#serve_while_stale}
        :param signed_url_cache_max_age_sec: Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served. When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a "Cache-Control: public, max-age=[TTL]" header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#signed_url_cache_max_age_sec GoogleComputeBackendBucket#signed_url_cache_max_age_sec}
        '''
        if isinstance(cache_key_policy, dict):
            cache_key_policy = GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy(**cache_key_policy)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicy.__init__)
            check_type(argname="argument bypass_cache_on_request_headers", value=bypass_cache_on_request_headers, expected_type=type_hints["bypass_cache_on_request_headers"])
            check_type(argname="argument cache_key_policy", value=cache_key_policy, expected_type=type_hints["cache_key_policy"])
            check_type(argname="argument cache_mode", value=cache_mode, expected_type=type_hints["cache_mode"])
            check_type(argname="argument client_ttl", value=client_ttl, expected_type=type_hints["client_ttl"])
            check_type(argname="argument default_ttl", value=default_ttl, expected_type=type_hints["default_ttl"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument negative_caching", value=negative_caching, expected_type=type_hints["negative_caching"])
            check_type(argname="argument negative_caching_policy", value=negative_caching_policy, expected_type=type_hints["negative_caching_policy"])
            check_type(argname="argument request_coalescing", value=request_coalescing, expected_type=type_hints["request_coalescing"])
            check_type(argname="argument serve_while_stale", value=serve_while_stale, expected_type=type_hints["serve_while_stale"])
            check_type(argname="argument signed_url_cache_max_age_sec", value=signed_url_cache_max_age_sec, expected_type=type_hints["signed_url_cache_max_age_sec"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bypass_cache_on_request_headers is not None:
            self._values["bypass_cache_on_request_headers"] = bypass_cache_on_request_headers
        if cache_key_policy is not None:
            self._values["cache_key_policy"] = cache_key_policy
        if cache_mode is not None:
            self._values["cache_mode"] = cache_mode
        if client_ttl is not None:
            self._values["client_ttl"] = client_ttl
        if default_ttl is not None:
            self._values["default_ttl"] = default_ttl
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if negative_caching is not None:
            self._values["negative_caching"] = negative_caching
        if negative_caching_policy is not None:
            self._values["negative_caching_policy"] = negative_caching_policy
        if request_coalescing is not None:
            self._values["request_coalescing"] = request_coalescing
        if serve_while_stale is not None:
            self._values["serve_while_stale"] = serve_while_stale
        if signed_url_cache_max_age_sec is not None:
            self._values["signed_url_cache_max_age_sec"] = signed_url_cache_max_age_sec

    @builtins.property
    def bypass_cache_on_request_headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders"]]]:
        '''bypass_cache_on_request_headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#bypass_cache_on_request_headers GoogleComputeBackendBucket#bypass_cache_on_request_headers}
        '''
        result = self._values.get("bypass_cache_on_request_headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders"]]], result)

    @builtins.property
    def cache_key_policy(
        self,
    ) -> typing.Optional["GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy"]:
        '''cache_key_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cache_key_policy GoogleComputeBackendBucket#cache_key_policy}
        '''
        result = self._values.get("cache_key_policy")
        return typing.cast(typing.Optional["GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy"], result)

    @builtins.property
    def cache_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies the cache setting for all responses from this backend.

        The possible values are: USE_ORIGIN_HEADERS, FORCE_CACHE_ALL and CACHE_ALL_STATIC Possible values: ["USE_ORIGIN_HEADERS", "FORCE_CACHE_ALL", "CACHE_ALL_STATIC"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cache_mode GoogleComputeBackendBucket#cache_mode}
        '''
        result = self._values.get("cache_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_ttl(self) -> typing.Optional[jsii.Number]:
        '''Specifies the maximum allowed TTL for cached content served by this origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#client_ttl GoogleComputeBackendBucket#client_ttl}
        '''
        result = self._values.get("client_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_ttl(self) -> typing.Optional[jsii.Number]:
        '''Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-max-age).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#default_ttl GoogleComputeBackendBucket#default_ttl}
        '''
        result = self._values.get("default_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Specifies the maximum allowed TTL for cached content served by this origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#max_ttl GoogleComputeBackendBucket#max_ttl}
        '''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def negative_caching(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#negative_caching GoogleComputeBackendBucket#negative_caching}
        '''
        result = self._values.get("negative_caching")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def negative_caching_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy"]]]:
        '''negative_caching_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#negative_caching_policy GoogleComputeBackendBucket#negative_caching_policy}
        '''
        result = self._values.get("negative_caching_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy"]]], result)

    @builtins.property
    def request_coalescing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#request_coalescing GoogleComputeBackendBucket#request_coalescing}
        '''
        result = self._values.get("request_coalescing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def serve_while_stale(self) -> typing.Optional[jsii.Number]:
        '''Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#serve_while_stale GoogleComputeBackendBucket#serve_while_stale}
        '''
        result = self._values.get("serve_while_stale")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def signed_url_cache_max_age_sec(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds the response to a signed URL request will be considered fresh.

        After this time period,
        the response will be revalidated before being served.
        When serving responses to signed URL requests,
        Cloud CDN will internally behave as though
        all responses from this backend had a "Cache-Control: public,
        max-age=[TTL]" header, regardless of any existing Cache-Control
        header. The actual headers served in responses will not be altered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#signed_url_cache_max_age_sec GoogleComputeBackendBucket#signed_url_cache_max_age_sec}
        '''
        result = self._values.get("signed_url_cache_max_age_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendBucketCdnPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders",
    jsii_struct_bases=[],
    name_mapping={"header_name": "headerName"},
)
class GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders:
    def __init__(self, *, header_name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param header_name: The header field name to match on when bypassing cache. Values are case-insensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#header_name GoogleComputeBackendBucket#header_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if header_name is not None:
            self._values["header_name"] = header_name

    @builtins.property
    def header_name(self) -> typing.Optional[builtins.str]:
        '''The header field name to match on when bypassing cache. Values are case-insensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#header_name GoogleComputeBackendBucket#header_name}
        '''
        result = self._values.get("header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHeaderName")
    def reset_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderName", []))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "include_http_headers": "includeHttpHeaders",
        "query_string_whitelist": "queryStringWhitelist",
    },
)
class GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy:
    def __init__(
        self,
        *,
        include_http_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param include_http_headers: Allows HTTP request headers (by name) to be used in the cache key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#include_http_headers GoogleComputeBackendBucket#include_http_headers}
        :param query_string_whitelist: Names of query string parameters to include in cache keys. Default parameters are always included. '&' and '=' will be percent encoded and not treated as delimiters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#query_string_whitelist GoogleComputeBackendBucket#query_string_whitelist}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy.__init__)
            check_type(argname="argument include_http_headers", value=include_http_headers, expected_type=type_hints["include_http_headers"])
            check_type(argname="argument query_string_whitelist", value=query_string_whitelist, expected_type=type_hints["query_string_whitelist"])
        self._values: typing.Dict[str, typing.Any] = {}
        if include_http_headers is not None:
            self._values["include_http_headers"] = include_http_headers
        if query_string_whitelist is not None:
            self._values["query_string_whitelist"] = query_string_whitelist

    @builtins.property
    def include_http_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Allows HTTP request headers (by name) to be used in the cache key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#include_http_headers GoogleComputeBackendBucket#include_http_headers}
        '''
        result = self._values.get("include_http_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of query string parameters to include in cache keys.

        Default parameters are always included. '&' and '=' will
        be percent encoded and not treated as delimiters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#query_string_whitelist GoogleComputeBackendBucket#query_string_whitelist}
        '''
        result = self._values.get("query_string_whitelist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeHttpHeaders")
    def reset_include_http_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeHttpHeaders", []))

    @jsii.member(jsii_name="resetQueryStringWhitelist")
    def reset_query_string_whitelist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringWhitelist", []))

    @builtins.property
    @jsii.member(jsii_name="includeHttpHeadersInput")
    def include_http_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeHttpHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringWhitelistInput")
    def query_string_whitelist_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryStringWhitelistInput"))

    @builtins.property
    @jsii.member(jsii_name="includeHttpHeaders")
    def include_http_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includeHttpHeaders"))

    @include_http_headers.setter
    def include_http_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference, "include_http_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeHttpHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringWhitelist")
    def query_string_whitelist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStringWhitelist"))

    @query_string_whitelist.setter
    def query_string_whitelist(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference, "query_string_whitelist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringWhitelist", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy]:
        return typing.cast(typing.Optional[GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy",
    jsii_struct_bases=[],
    name_mapping={"code": "code", "ttl": "ttl"},
)
class GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy:
    def __init__(
        self,
        *,
        code: typing.Optional[jsii.Number] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param code: The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#code GoogleComputeBackendBucket#code}
        :param ttl: The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes), noting that infrequently accessed objects may be evicted from the cache before the defined TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#ttl GoogleComputeBackendBucket#ttl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy.__init__)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if code is not None:
            self._values["code"] = code
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def code(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status code to define a TTL against.

        Only HTTP status codes 300, 301, 308, 404, 405, 410, 421, 451 and 501
        can be specified as values, and you cannot specify a status code more than once.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#code GoogleComputeBackendBucket#code}
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''The TTL (in seconds) for which to cache responses with the corresponding status code.

        The maximum allowed value is 1800s
        (30 minutes), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#ttl GoogleComputeBackendBucket#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "code"))

    @code.setter
    def code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference, "code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendBucketCdnPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketCdnPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBypassCacheOnRequestHeaders")
    def put_bypass_cache_on_request_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyOutputReference.put_bypass_cache_on_request_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBypassCacheOnRequestHeaders", [value]))

    @jsii.member(jsii_name="putCacheKeyPolicy")
    def put_cache_key_policy(
        self,
        *,
        include_http_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param include_http_headers: Allows HTTP request headers (by name) to be used in the cache key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#include_http_headers GoogleComputeBackendBucket#include_http_headers}
        :param query_string_whitelist: Names of query string parameters to include in cache keys. Default parameters are always included. '&' and '=' will be percent encoded and not treated as delimiters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#query_string_whitelist GoogleComputeBackendBucket#query_string_whitelist}
        '''
        value = GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy(
            include_http_headers=include_http_headers,
            query_string_whitelist=query_string_whitelist,
        )

        return typing.cast(None, jsii.invoke(self, "putCacheKeyPolicy", [value]))

    @jsii.member(jsii_name="putNegativeCachingPolicy")
    def put_negative_caching_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketCdnPolicyOutputReference.put_negative_caching_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNegativeCachingPolicy", [value]))

    @jsii.member(jsii_name="resetBypassCacheOnRequestHeaders")
    def reset_bypass_cache_on_request_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBypassCacheOnRequestHeaders", []))

    @jsii.member(jsii_name="resetCacheKeyPolicy")
    def reset_cache_key_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheKeyPolicy", []))

    @jsii.member(jsii_name="resetCacheMode")
    def reset_cache_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheMode", []))

    @jsii.member(jsii_name="resetClientTtl")
    def reset_client_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTtl", []))

    @jsii.member(jsii_name="resetDefaultTtl")
    def reset_default_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTtl", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetNegativeCaching")
    def reset_negative_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegativeCaching", []))

    @jsii.member(jsii_name="resetNegativeCachingPolicy")
    def reset_negative_caching_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegativeCachingPolicy", []))

    @jsii.member(jsii_name="resetRequestCoalescing")
    def reset_request_coalescing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestCoalescing", []))

    @jsii.member(jsii_name="resetServeWhileStale")
    def reset_serve_while_stale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServeWhileStale", []))

    @jsii.member(jsii_name="resetSignedUrlCacheMaxAgeSec")
    def reset_signed_url_cache_max_age_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignedUrlCacheMaxAgeSec", []))

    @builtins.property
    @jsii.member(jsii_name="bypassCacheOnRequestHeaders")
    def bypass_cache_on_request_headers(
        self,
    ) -> GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList:
        return typing.cast(GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList, jsii.get(self, "bypassCacheOnRequestHeaders"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyPolicy")
    def cache_key_policy(
        self,
    ) -> GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference:
        return typing.cast(GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference, jsii.get(self, "cacheKeyPolicy"))

    @builtins.property
    @jsii.member(jsii_name="negativeCachingPolicy")
    def negative_caching_policy(
        self,
    ) -> GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList:
        return typing.cast(GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList, jsii.get(self, "negativeCachingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="bypassCacheOnRequestHeadersInput")
    def bypass_cache_on_request_headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders]]], jsii.get(self, "bypassCacheOnRequestHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyPolicyInput")
    def cache_key_policy_input(
        self,
    ) -> typing.Optional[GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy]:
        return typing.cast(typing.Optional[GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy], jsii.get(self, "cacheKeyPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheModeInput")
    def cache_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheModeInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTtlInput")
    def client_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTtlInput")
    def default_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="negativeCachingInput")
    def negative_caching_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negativeCachingInput"))

    @builtins.property
    @jsii.member(jsii_name="negativeCachingPolicyInput")
    def negative_caching_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy]]], jsii.get(self, "negativeCachingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="requestCoalescingInput")
    def request_coalescing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requestCoalescingInput"))

    @builtins.property
    @jsii.member(jsii_name="serveWhileStaleInput")
    def serve_while_stale_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serveWhileStaleInput"))

    @builtins.property
    @jsii.member(jsii_name="signedUrlCacheMaxAgeSecInput")
    def signed_url_cache_max_age_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "signedUrlCacheMaxAgeSecInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheMode")
    def cache_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheMode"))

    @cache_mode.setter
    def cache_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "cache_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheMode", value)

    @builtins.property
    @jsii.member(jsii_name="clientTtl")
    def client_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientTtl"))

    @client_ttl.setter
    def client_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "client_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTtl", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTtl")
    def default_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTtl"))

    @default_ttl.setter
    def default_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "default_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTtl", value)

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="negativeCaching")
    def negative_caching(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negativeCaching"))

    @negative_caching.setter
    def negative_caching(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "negative_caching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negativeCaching", value)

    @builtins.property
    @jsii.member(jsii_name="requestCoalescing")
    def request_coalescing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requestCoalescing"))

    @request_coalescing.setter
    def request_coalescing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "request_coalescing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestCoalescing", value)

    @builtins.property
    @jsii.member(jsii_name="serveWhileStale")
    def serve_while_stale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serveWhileStale"))

    @serve_while_stale.setter
    def serve_while_stale(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "serve_while_stale").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serveWhileStale", value)

    @builtins.property
    @jsii.member(jsii_name="signedUrlCacheMaxAgeSec")
    def signed_url_cache_max_age_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "signedUrlCacheMaxAgeSec"))

    @signed_url_cache_max_age_sec.setter
    def signed_url_cache_max_age_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "signed_url_cache_max_age_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signedUrlCacheMaxAgeSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeBackendBucketCdnPolicy]:
        return typing.cast(typing.Optional[GoogleComputeBackendBucketCdnPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendBucketCdnPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketCdnPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket_name": "bucketName",
        "name": "name",
        "cdn_policy": "cdnPolicy",
        "compression_mode": "compressionMode",
        "custom_response_headers": "customResponseHeaders",
        "description": "description",
        "edge_security_policy": "edgeSecurityPolicy",
        "enable_cdn": "enableCdn",
        "id": "id",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleComputeBackendBucketConfig(cdktf.TerraformMetaArguments):
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
        bucket_name: builtins.str,
        name: builtins.str,
        cdn_policy: typing.Optional[typing.Union[GoogleComputeBackendBucketCdnPolicy, typing.Dict[str, typing.Any]]] = None,
        compression_mode: typing.Optional[builtins.str] = None,
        custom_response_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        edge_security_policy: typing.Optional[builtins.str] = None,
        enable_cdn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeBackendBucketTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket_name: Cloud Storage bucket name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#bucket_name GoogleComputeBackendBucket#bucket_name}
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#name GoogleComputeBackendBucket#name}
        :param cdn_policy: cdn_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cdn_policy GoogleComputeBackendBucket#cdn_policy}
        :param compression_mode: Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header. Possible values: ["AUTOMATIC", "DISABLED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#compression_mode GoogleComputeBackendBucket#compression_mode}
        :param custom_response_headers: Headers that the HTTP/S load balancer should add to proxied responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#custom_response_headers GoogleComputeBackendBucket#custom_response_headers}
        :param description: An optional textual description of the resource; provided by the client when the resource is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#description GoogleComputeBackendBucket#description}
        :param edge_security_policy: The security policy associated with this backend bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#edge_security_policy GoogleComputeBackendBucket#edge_security_policy}
        :param enable_cdn: If true, enable Cloud CDN for this BackendBucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#enable_cdn GoogleComputeBackendBucket#enable_cdn}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#id GoogleComputeBackendBucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#project GoogleComputeBackendBucket#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#timeouts GoogleComputeBackendBucket#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cdn_policy, dict):
            cdn_policy = GoogleComputeBackendBucketCdnPolicy(**cdn_policy)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeBackendBucketTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cdn_policy", value=cdn_policy, expected_type=type_hints["cdn_policy"])
            check_type(argname="argument compression_mode", value=compression_mode, expected_type=type_hints["compression_mode"])
            check_type(argname="argument custom_response_headers", value=custom_response_headers, expected_type=type_hints["custom_response_headers"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument edge_security_policy", value=edge_security_policy, expected_type=type_hints["edge_security_policy"])
            check_type(argname="argument enable_cdn", value=enable_cdn, expected_type=type_hints["enable_cdn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "name": name,
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
        if cdn_policy is not None:
            self._values["cdn_policy"] = cdn_policy
        if compression_mode is not None:
            self._values["compression_mode"] = compression_mode
        if custom_response_headers is not None:
            self._values["custom_response_headers"] = custom_response_headers
        if description is not None:
            self._values["description"] = description
        if edge_security_policy is not None:
            self._values["edge_security_policy"] = edge_security_policy
        if enable_cdn is not None:
            self._values["enable_cdn"] = enable_cdn
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
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
    def bucket_name(self) -> builtins.str:
        '''Cloud Storage bucket name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#bucket_name GoogleComputeBackendBucket#bucket_name}
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035.  Specifically, the name must be 1-63 characters long and
        match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means
        the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the
        last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#name GoogleComputeBackendBucket#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdn_policy(self) -> typing.Optional[GoogleComputeBackendBucketCdnPolicy]:
        '''cdn_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#cdn_policy GoogleComputeBackendBucket#cdn_policy}
        '''
        result = self._values.get("cdn_policy")
        return typing.cast(typing.Optional[GoogleComputeBackendBucketCdnPolicy], result)

    @builtins.property
    def compression_mode(self) -> typing.Optional[builtins.str]:
        '''Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header. Possible values: ["AUTOMATIC", "DISABLED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#compression_mode GoogleComputeBackendBucket#compression_mode}
        '''
        result = self._values.get("compression_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_response_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Headers that the HTTP/S load balancer should add to proxied responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#custom_response_headers GoogleComputeBackendBucket#custom_response_headers}
        '''
        result = self._values.get("custom_response_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional textual description of the resource; provided by the client when the resource is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#description GoogleComputeBackendBucket#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edge_security_policy(self) -> typing.Optional[builtins.str]:
        '''The security policy associated with this backend bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#edge_security_policy GoogleComputeBackendBucket#edge_security_policy}
        '''
        result = self._values.get("edge_security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_cdn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, enable Cloud CDN for this BackendBucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#enable_cdn GoogleComputeBackendBucket#enable_cdn}
        '''
        result = self._values.get("enable_cdn")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#id GoogleComputeBackendBucket#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#project GoogleComputeBackendBucket#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeBackendBucketTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#timeouts GoogleComputeBackendBucket#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeBackendBucketTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendBucketConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeBackendBucketTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#create GoogleComputeBackendBucket#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#delete GoogleComputeBackendBucket#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#update GoogleComputeBackendBucket#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#create GoogleComputeBackendBucket#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#delete GoogleComputeBackendBucket#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_bucket#update GoogleComputeBackendBucket#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendBucketTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendBucketTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendBucket.GoogleComputeBackendBucketTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendBucketTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeBackendBucketTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeBackendBucketTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeBackendBucketTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendBucketTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeBackendBucket",
    "GoogleComputeBackendBucketCdnPolicy",
    "GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeaders",
    "GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersList",
    "GoogleComputeBackendBucketCdnPolicyBypassCacheOnRequestHeadersOutputReference",
    "GoogleComputeBackendBucketCdnPolicyCacheKeyPolicy",
    "GoogleComputeBackendBucketCdnPolicyCacheKeyPolicyOutputReference",
    "GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicy",
    "GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyList",
    "GoogleComputeBackendBucketCdnPolicyNegativeCachingPolicyOutputReference",
    "GoogleComputeBackendBucketCdnPolicyOutputReference",
    "GoogleComputeBackendBucketConfig",
    "GoogleComputeBackendBucketTimeouts",
    "GoogleComputeBackendBucketTimeoutsOutputReference",
]

publication.publish()
