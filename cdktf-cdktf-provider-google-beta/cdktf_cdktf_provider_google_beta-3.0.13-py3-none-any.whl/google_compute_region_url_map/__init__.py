'''
# `google_compute_region_url_map`

Refer to the Terraform Registory for docs: [`google_compute_region_url_map`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map).
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


class GoogleComputeRegionUrlMap(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMap",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map google_compute_region_url_map}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        default_service: typing.Optional[builtins.str] = None,
        default_url_redirect: typing.Optional[typing.Union["GoogleComputeRegionUrlMapDefaultUrlRedirect", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        host_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapHostRule", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        path_matcher: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcher", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        test: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapTest", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionUrlMapTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map google_compute_region_url_map} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        :param default_service: The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is additionally specified, advanced routing actions like URL Rewrites, etc. take effect prior to sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect or defaultRouteAction.weightedBackendService must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_service GoogleComputeRegionUrlMap#default_service}
        :param default_url_redirect: default_url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_url_redirect GoogleComputeRegionUrlMap#default_url_redirect}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        :param host_rule: host_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rule GoogleComputeRegionUrlMap#host_rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#id GoogleComputeRegionUrlMap#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path_matcher: path_matcher block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_matcher GoogleComputeRegionUrlMap#path_matcher}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#project GoogleComputeRegionUrlMap#project}.
        :param region: The Region in which the url map should reside. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#region GoogleComputeRegionUrlMap#region}
        :param test: test block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#test GoogleComputeRegionUrlMap#test}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeouts GoogleComputeRegionUrlMap#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMap.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeRegionUrlMapConfig(
            name=name,
            default_service=default_service,
            default_url_redirect=default_url_redirect,
            description=description,
            host_rule=host_rule,
            id=id,
            path_matcher=path_matcher,
            project=project,
            region=region,
            test=test,
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

    @jsii.member(jsii_name="putDefaultUrlRedirect")
    def put_default_url_redirect(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        value = GoogleComputeRegionUrlMapDefaultUrlRedirect(
            strip_query=strip_query,
            host_redirect=host_redirect,
            https_redirect=https_redirect,
            path_redirect=path_redirect,
            prefix_redirect=prefix_redirect,
            redirect_response_code=redirect_response_code,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultUrlRedirect", [value]))

    @jsii.member(jsii_name="putHostRule")
    def put_host_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapHostRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMap.put_host_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHostRule", [value]))

    @jsii.member(jsii_name="putPathMatcher")
    def put_path_matcher(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcher", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMap.put_path_matcher)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPathMatcher", [value]))

    @jsii.member(jsii_name="putTest")
    def put_test(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapTest", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMap.put_test)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTest", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#create GoogleComputeRegionUrlMap#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delete GoogleComputeRegionUrlMap#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#update GoogleComputeRegionUrlMap#update}.
        '''
        value = GoogleComputeRegionUrlMapTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDefaultService")
    def reset_default_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultService", []))

    @jsii.member(jsii_name="resetDefaultUrlRedirect")
    def reset_default_url_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultUrlRedirect", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHostRule")
    def reset_host_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRule", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPathMatcher")
    def reset_path_matcher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathMatcher", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetTest")
    def reset_test(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTest", []))

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
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="defaultUrlRedirect")
    def default_url_redirect(
        self,
    ) -> "GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference", jsii.get(self, "defaultUrlRedirect"))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="hostRule")
    def host_rule(self) -> "GoogleComputeRegionUrlMapHostRuleList":
        return typing.cast("GoogleComputeRegionUrlMapHostRuleList", jsii.get(self, "hostRule"))

    @builtins.property
    @jsii.member(jsii_name="mapId")
    def map_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mapId"))

    @builtins.property
    @jsii.member(jsii_name="pathMatcher")
    def path_matcher(self) -> "GoogleComputeRegionUrlMapPathMatcherList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherList", jsii.get(self, "pathMatcher"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="test")
    def test(self) -> "GoogleComputeRegionUrlMapTestList":
        return typing.cast("GoogleComputeRegionUrlMapTestList", jsii.get(self, "test"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeRegionUrlMapTimeoutsOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="defaultServiceInput")
    def default_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultUrlRedirectInput")
    def default_url_redirect_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapDefaultUrlRedirect"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapDefaultUrlRedirect"], jsii.get(self, "defaultUrlRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRuleInput")
    def host_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapHostRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapHostRule"]]], jsii.get(self, "hostRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathMatcherInput")
    def path_matcher_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcher"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcher"]]], jsii.get(self, "pathMatcherInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="testInput")
    def test_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapTest"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapTest"]]], jsii.get(self, "testInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeRegionUrlMapTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeRegionUrlMapTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultService")
    def default_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultService"))

    @default_service.setter
    def default_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMap, "default_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultService", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMap, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMap, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMap, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMap, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMap, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "default_service": "defaultService",
        "default_url_redirect": "defaultUrlRedirect",
        "description": "description",
        "host_rule": "hostRule",
        "id": "id",
        "path_matcher": "pathMatcher",
        "project": "project",
        "region": "region",
        "test": "test",
        "timeouts": "timeouts",
    },
)
class GoogleComputeRegionUrlMapConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        default_service: typing.Optional[builtins.str] = None,
        default_url_redirect: typing.Optional[typing.Union["GoogleComputeRegionUrlMapDefaultUrlRedirect", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        host_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapHostRule", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        path_matcher: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcher", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        test: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapTest", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionUrlMapTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        :param default_service: The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is additionally specified, advanced routing actions like URL Rewrites, etc. take effect prior to sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect or defaultRouteAction.weightedBackendService must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_service GoogleComputeRegionUrlMap#default_service}
        :param default_url_redirect: default_url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_url_redirect GoogleComputeRegionUrlMap#default_url_redirect}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        :param host_rule: host_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rule GoogleComputeRegionUrlMap#host_rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#id GoogleComputeRegionUrlMap#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path_matcher: path_matcher block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_matcher GoogleComputeRegionUrlMap#path_matcher}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#project GoogleComputeRegionUrlMap#project}.
        :param region: The Region in which the url map should reside. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#region GoogleComputeRegionUrlMap#region}
        :param test: test block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#test GoogleComputeRegionUrlMap#test}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeouts GoogleComputeRegionUrlMap#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_url_redirect, dict):
            default_url_redirect = GoogleComputeRegionUrlMapDefaultUrlRedirect(**default_url_redirect)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeRegionUrlMapTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_service", value=default_service, expected_type=type_hints["default_service"])
            check_type(argname="argument default_url_redirect", value=default_url_redirect, expected_type=type_hints["default_url_redirect"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument host_rule", value=host_rule, expected_type=type_hints["host_rule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path_matcher", value=path_matcher, expected_type=type_hints["path_matcher"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument test", value=test, expected_type=type_hints["test"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if default_service is not None:
            self._values["default_service"] = default_service
        if default_url_redirect is not None:
            self._values["default_url_redirect"] = default_url_redirect
        if description is not None:
            self._values["description"] = description
        if host_rule is not None:
            self._values["host_rule"] = host_rule
        if id is not None:
            self._values["id"] = id
        if path_matcher is not None:
            self._values["path_matcher"] = path_matcher
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if test is not None:
            self._values["test"] = test
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
    def name(self) -> builtins.str:
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_service(self) -> typing.Optional[builtins.str]:
        '''The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match.

        If defaultRouteAction is additionally specified, advanced
        routing actions like URL Rewrites, etc. take effect prior to sending the request to the
        backend. However, if defaultService is specified, defaultRouteAction cannot contain any
        weightedBackendServices. Conversely, if routeAction specifies any
        weightedBackendServices, service must not be specified.  Only one of defaultService,
        defaultUrlRedirect or defaultRouteAction.weightedBackendService must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_service GoogleComputeRegionUrlMap#default_service}
        '''
        result = self._values.get("default_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_url_redirect(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapDefaultUrlRedirect"]:
        '''default_url_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_url_redirect GoogleComputeRegionUrlMap#default_url_redirect}
        '''
        result = self._values.get("default_url_redirect")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapDefaultUrlRedirect"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapHostRule"]]]:
        '''host_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rule GoogleComputeRegionUrlMap#host_rule}
        '''
        result = self._values.get("host_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapHostRule"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#id GoogleComputeRegionUrlMap#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_matcher(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcher"]]]:
        '''path_matcher block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_matcher GoogleComputeRegionUrlMap#path_matcher}
        '''
        result = self._values.get("path_matcher")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcher"]]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#project GoogleComputeRegionUrlMap#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Region in which the url map should reside. If it is not provided, the provider region is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#region GoogleComputeRegionUrlMap#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapTest"]]]:
        '''test block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#test GoogleComputeRegionUrlMap#test}
        '''
        result = self._values.get("test")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapTest"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeRegionUrlMapTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeouts GoogleComputeRegionUrlMap#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapDefaultUrlRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "strip_query": "stripQuery",
        "host_redirect": "hostRedirect",
        "https_redirect": "httpsRedirect",
        "path_redirect": "pathRedirect",
        "prefix_redirect": "prefixRedirect",
        "redirect_response_code": "redirectResponseCode",
    },
)
class GoogleComputeRegionUrlMapDefaultUrlRedirect:
    def __init__(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapDefaultUrlRedirect.__init__)
            check_type(argname="argument strip_query", value=strip_query, expected_type=type_hints["strip_query"])
            check_type(argname="argument host_redirect", value=host_redirect, expected_type=type_hints["host_redirect"])
            check_type(argname="argument https_redirect", value=https_redirect, expected_type=type_hints["https_redirect"])
            check_type(argname="argument path_redirect", value=path_redirect, expected_type=type_hints["path_redirect"])
            check_type(argname="argument prefix_redirect", value=prefix_redirect, expected_type=type_hints["prefix_redirect"])
            check_type(argname="argument redirect_response_code", value=redirect_response_code, expected_type=type_hints["redirect_response_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "strip_query": strip_query,
        }
        if host_redirect is not None:
            self._values["host_redirect"] = host_redirect
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if path_redirect is not None:
            self._values["path_redirect"] = path_redirect
        if prefix_redirect is not None:
            self._values["prefix_redirect"] = prefix_redirect
        if redirect_response_code is not None:
            self._values["redirect_response_code"] = redirect_response_code

    @builtins.property
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request.

        If set to false, the query portion of the original URL is
        retained.
        This field is required to ensure an empty block is not set. The normal default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        '''
        result = self._values.get("strip_query")
        assert result is not None, "Required property 'strip_query' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def host_redirect(self) -> typing.Optional[builtins.str]:
        '''The host that will be used in the redirect response instead of the one that was supplied in the request.

        The value must be between 1 and 255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        '''
        result = self._values.get("host_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the URL scheme in the redirected request is set to https.

        If set to
        false, the URL scheme of the redirected request will remain the same as that of the
        request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this
        true for TargetHttpsProxy is not permitted. The default is set to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_redirect(self) -> typing.Optional[builtins.str]:
        '''The path that will be used in the redirect response instead of the one that was supplied in the request.

        pathRedirect cannot be supplied together with
        prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the
        original request will be used for the redirect. The value must be between 1 and 1024
        characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        '''
        result = self._values.get("path_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_redirect(self) -> typing.Optional[builtins.str]:
        '''The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request.

        prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or
        neither. If neither is supplied, the path of the original request will be used for
        the redirect. The value must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        '''
        result = self._values.get("prefix_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_response_code(self) -> typing.Optional[builtins.str]:
        '''The HTTP Status code to use for this RedirectAction. Supported values are:.

        MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.

        FOUND, which corresponds to 302.

        SEE_OTHER which corresponds to 303.

        TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        will be retained.

        PERMANENT_REDIRECT, which corresponds to 308. In this case,
        the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        result = self._values.get("redirect_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapDefaultUrlRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRedirect")
    def reset_host_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRedirect", []))

    @jsii.member(jsii_name="resetHttpsRedirect")
    def reset_https_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirect", []))

    @jsii.member(jsii_name="resetPathRedirect")
    def reset_path_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRedirect", []))

    @jsii.member(jsii_name="resetPrefixRedirect")
    def reset_prefix_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixRedirect", []))

    @jsii.member(jsii_name="resetRedirectResponseCode")
    def reset_redirect_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectResponseCode", []))

    @builtins.property
    @jsii.member(jsii_name="hostRedirectInput")
    def host_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectInput")
    def https_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRedirectInput")
    def path_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixRedirectInput")
    def prefix_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCodeInput")
    def redirect_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stripQueryInput")
    def strip_query_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRedirect")
    def host_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRedirect"))

    @host_redirect.setter
    def host_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference, "host_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirect")
    def https_redirect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirect"))

    @https_redirect.setter
    def https_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference, "https_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="pathRedirect")
    def path_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathRedirect"))

    @path_redirect.setter
    def path_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference, "path_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="prefixRedirect")
    def prefix_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixRedirect"))

    @prefix_redirect.setter
    def prefix_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference, "prefix_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCode")
    def redirect_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectResponseCode"))

    @redirect_response_code.setter
    def redirect_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference, "redirect_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="stripQuery")
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripQuery"))

    @strip_query.setter
    def strip_query(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference, "strip_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripQuery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapDefaultUrlRedirect]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapDefaultUrlRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapDefaultUrlRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapHostRule",
    jsii_struct_bases=[],
    name_mapping={
        "hosts": "hosts",
        "path_matcher": "pathMatcher",
        "description": "description",
    },
)
class GoogleComputeRegionUrlMapHostRule:
    def __init__(
        self,
        *,
        hosts: typing.Sequence[builtins.str],
        path_matcher: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosts: The list of host patterns to match. They must be valid hostnames, except * will match any string of ([a-z0-9-.]*). In that case, * must be the first character and must be followed in the pattern by either - or .. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#hosts GoogleComputeRegionUrlMap#hosts}
        :param path_matcher: The name of the PathMatcher to use to match the path portion of the URL if the hostRule matches the URL's host portion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_matcher GoogleComputeRegionUrlMap#path_matcher}
        :param description: An optional description of this HostRule. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapHostRule.__init__)
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument path_matcher", value=path_matcher, expected_type=type_hints["path_matcher"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "hosts": hosts,
            "path_matcher": path_matcher,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def hosts(self) -> typing.List[builtins.str]:
        '''The list of host patterns to match.

        They must be valid
        hostnames, except * will match any string of ([a-z0-9-.]*). In
        that case, * must be the first character and must be followed in
        the pattern by either - or ..

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#hosts GoogleComputeRegionUrlMap#hosts}
        '''
        result = self._values.get("hosts")
        assert result is not None, "Required property 'hosts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def path_matcher(self) -> builtins.str:
        '''The name of the PathMatcher to use to match the path portion of the URL if the hostRule matches the URL's host portion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_matcher GoogleComputeRegionUrlMap#path_matcher}
        '''
        result = self._values.get("path_matcher")
        assert result is not None, "Required property 'path_matcher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this HostRule. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapHostRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapHostRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapHostRuleList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapHostRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapHostRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapHostRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapHostRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapHostRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapHostRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapHostRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapHostRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapHostRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapHostRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapHostRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapHostRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapHostRuleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapHostRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathMatcherInput")
    def path_matcher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathMatcherInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapHostRuleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapHostRuleOutputReference, "hosts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="pathMatcher")
    def path_matcher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathMatcher"))

    @path_matcher.setter
    def path_matcher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapHostRuleOutputReference, "path_matcher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathMatcher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapHostRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapHostRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapHostRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapHostRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcher",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "default_service": "defaultService",
        "default_url_redirect": "defaultUrlRedirect",
        "description": "description",
        "path_rule": "pathRule",
        "route_rules": "routeRules",
    },
)
class GoogleComputeRegionUrlMapPathMatcher:
    def __init__(
        self,
        *,
        name: builtins.str,
        default_service: typing.Optional[builtins.str] = None,
        default_url_redirect: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        path_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRule", typing.Dict[str, typing.Any]]]]] = None,
        route_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRules", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: The name to which this PathMatcher is referred by the HostRule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        :param default_service: A reference to a RegionBackendService resource. This will be used if none of the pathRules defined by this PathMatcher is matched by the URL's path portion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_service GoogleComputeRegionUrlMap#default_service}
        :param default_url_redirect: default_url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_url_redirect GoogleComputeRegionUrlMap#default_url_redirect}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        :param path_rule: path_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_rule GoogleComputeRegionUrlMap#path_rule}
        :param route_rules: route_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#route_rules GoogleComputeRegionUrlMap#route_rules}
        '''
        if isinstance(default_url_redirect, dict):
            default_url_redirect = GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect(**default_url_redirect)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcher.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_service", value=default_service, expected_type=type_hints["default_service"])
            check_type(argname="argument default_url_redirect", value=default_url_redirect, expected_type=type_hints["default_url_redirect"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument path_rule", value=path_rule, expected_type=type_hints["path_rule"])
            check_type(argname="argument route_rules", value=route_rules, expected_type=type_hints["route_rules"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if default_service is not None:
            self._values["default_service"] = default_service
        if default_url_redirect is not None:
            self._values["default_url_redirect"] = default_url_redirect
        if description is not None:
            self._values["description"] = description
        if path_rule is not None:
            self._values["path_rule"] = path_rule
        if route_rules is not None:
            self._values["route_rules"] = route_rules

    @builtins.property
    def name(self) -> builtins.str:
        '''The name to which this PathMatcher is referred by the HostRule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_service(self) -> typing.Optional[builtins.str]:
        '''A reference to a RegionBackendService resource.

        This will be used if
        none of the pathRules defined by this PathMatcher is matched by
        the URL's path portion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_service GoogleComputeRegionUrlMap#default_service}
        '''
        result = self._values.get("default_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_url_redirect(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect"]:
        '''default_url_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#default_url_redirect GoogleComputeRegionUrlMap#default_url_redirect}
        '''
        result = self._values.get("default_url_redirect")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRule"]]]:
        '''path_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_rule GoogleComputeRegionUrlMap#path_rule}
        '''
        result = self._values.get("path_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRule"]]], result)

    @builtins.property
    def route_rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRules"]]]:
        '''route_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#route_rules GoogleComputeRegionUrlMap#route_rules}
        '''
        result = self._values.get("route_rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcher(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "strip_query": "stripQuery",
        "host_redirect": "hostRedirect",
        "https_redirect": "httpsRedirect",
        "path_redirect": "pathRedirect",
        "prefix_redirect": "prefixRedirect",
        "redirect_response_code": "redirectResponseCode",
    },
)
class GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect:
    def __init__(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect.__init__)
            check_type(argname="argument strip_query", value=strip_query, expected_type=type_hints["strip_query"])
            check_type(argname="argument host_redirect", value=host_redirect, expected_type=type_hints["host_redirect"])
            check_type(argname="argument https_redirect", value=https_redirect, expected_type=type_hints["https_redirect"])
            check_type(argname="argument path_redirect", value=path_redirect, expected_type=type_hints["path_redirect"])
            check_type(argname="argument prefix_redirect", value=prefix_redirect, expected_type=type_hints["prefix_redirect"])
            check_type(argname="argument redirect_response_code", value=redirect_response_code, expected_type=type_hints["redirect_response_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "strip_query": strip_query,
        }
        if host_redirect is not None:
            self._values["host_redirect"] = host_redirect
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if path_redirect is not None:
            self._values["path_redirect"] = path_redirect
        if prefix_redirect is not None:
            self._values["prefix_redirect"] = prefix_redirect
        if redirect_response_code is not None:
            self._values["redirect_response_code"] = redirect_response_code

    @builtins.property
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request.

        If set to false, the query portion of the original URL is
        retained.
        This field is required to ensure an empty block is not set. The normal default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        '''
        result = self._values.get("strip_query")
        assert result is not None, "Required property 'strip_query' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def host_redirect(self) -> typing.Optional[builtins.str]:
        '''The host that will be used in the redirect response instead of the one that was supplied in the request.

        The value must be between 1 and 255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        '''
        result = self._values.get("host_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the URL scheme in the redirected request is set to https.

        If set to
        false, the URL scheme of the redirected request will remain the same as that of the
        request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this
        true for TargetHttpsProxy is not permitted. The default is set to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_redirect(self) -> typing.Optional[builtins.str]:
        '''The path that will be used in the redirect response instead of the one that was supplied in the request.

        pathRedirect cannot be supplied together with
        prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the
        original request will be used for the redirect. The value must be between 1 and 1024
        characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        '''
        result = self._values.get("path_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_redirect(self) -> typing.Optional[builtins.str]:
        '''The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request.

        prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or
        neither. If neither is supplied, the path of the original request will be used for
        the redirect. The value must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        '''
        result = self._values.get("prefix_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_response_code(self) -> typing.Optional[builtins.str]:
        '''The HTTP Status code to use for this RedirectAction. Supported values are:.

        MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.

        FOUND, which corresponds to 302.

        SEE_OTHER which corresponds to 303.

        TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        will be retained.

        PERMANENT_REDIRECT, which corresponds to 308. In this case,
        the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        result = self._values.get("redirect_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRedirect")
    def reset_host_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRedirect", []))

    @jsii.member(jsii_name="resetHttpsRedirect")
    def reset_https_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirect", []))

    @jsii.member(jsii_name="resetPathRedirect")
    def reset_path_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRedirect", []))

    @jsii.member(jsii_name="resetPrefixRedirect")
    def reset_prefix_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixRedirect", []))

    @jsii.member(jsii_name="resetRedirectResponseCode")
    def reset_redirect_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectResponseCode", []))

    @builtins.property
    @jsii.member(jsii_name="hostRedirectInput")
    def host_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectInput")
    def https_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRedirectInput")
    def path_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixRedirectInput")
    def prefix_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCodeInput")
    def redirect_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stripQueryInput")
    def strip_query_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRedirect")
    def host_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRedirect"))

    @host_redirect.setter
    def host_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "host_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirect")
    def https_redirect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirect"))

    @https_redirect.setter
    def https_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "https_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="pathRedirect")
    def path_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathRedirect"))

    @path_redirect.setter
    def path_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "path_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="prefixRedirect")
    def prefix_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixRedirect"))

    @prefix_redirect.setter
    def prefix_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "prefix_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCode")
    def redirect_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectResponseCode"))

    @redirect_response_code.setter
    def redirect_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "redirect_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="stripQuery")
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripQuery"))

    @strip_query.setter
    def strip_query(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "strip_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripQuery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcher]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcher]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcher]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDefaultUrlRedirect")
    def put_default_url_redirect(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect(
            strip_query=strip_query,
            host_redirect=host_redirect,
            https_redirect=https_redirect,
            path_redirect=path_redirect,
            prefix_redirect=prefix_redirect,
            redirect_response_code=redirect_response_code,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultUrlRedirect", [value]))

    @jsii.member(jsii_name="putPathRule")
    def put_path_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherOutputReference.put_path_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPathRule", [value]))

    @jsii.member(jsii_name="putRouteRules")
    def put_route_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherOutputReference.put_route_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRouteRules", [value]))

    @jsii.member(jsii_name="resetDefaultService")
    def reset_default_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultService", []))

    @jsii.member(jsii_name="resetDefaultUrlRedirect")
    def reset_default_url_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultUrlRedirect", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPathRule")
    def reset_path_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRule", []))

    @jsii.member(jsii_name="resetRouteRules")
    def reset_route_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteRules", []))

    @builtins.property
    @jsii.member(jsii_name="defaultUrlRedirect")
    def default_url_redirect(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference, jsii.get(self, "defaultUrlRedirect"))

    @builtins.property
    @jsii.member(jsii_name="pathRule")
    def path_rule(self) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleList", jsii.get(self, "pathRule"))

    @builtins.property
    @jsii.member(jsii_name="routeRules")
    def route_rules(self) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesList", jsii.get(self, "routeRules"))

    @builtins.property
    @jsii.member(jsii_name="defaultServiceInput")
    def default_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultUrlRedirectInput")
    def default_url_redirect_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect], jsii.get(self, "defaultUrlRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRuleInput")
    def path_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRule"]]], jsii.get(self, "pathRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="routeRulesInput")
    def route_rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRules"]]], jsii.get(self, "routeRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultService")
    def default_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultService"))

    @default_service.setter
    def default_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherOutputReference, "default_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultService", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcher, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcher, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcher, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRule",
    jsii_struct_bases=[],
    name_mapping={
        "paths": "paths",
        "route_action": "routeAction",
        "service": "service",
        "url_redirect": "urlRedirect",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRule:
    def __init__(
        self,
        *,
        paths: typing.Sequence[builtins.str],
        route_action: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction", typing.Dict[str, typing.Any]]] = None,
        service: typing.Optional[builtins.str] = None,
        url_redirect: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param paths: The list of path patterns to match. Each must start with / and the only place a * is allowed is at the end following a /. The string fed to the path matcher does not include any text after the first ? or #, and those chars are not allowed here. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#paths GoogleComputeRegionUrlMap#paths}
        :param route_action: route_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#route_action GoogleComputeRegionUrlMap#route_action}
        :param service: The region backend service resource to which traffic is directed if this rule is matched. If routeAction is additionally specified, advanced routing actions like URL Rewrites, etc. take effect prior to sending the request to the backend. However, if service is specified, routeAction cannot contain any weightedBackendService s. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of urlRedirect, service or routeAction.weightedBackendService must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#service GoogleComputeRegionUrlMap#service}
        :param url_redirect: url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_redirect GoogleComputeRegionUrlMap#url_redirect}
        '''
        if isinstance(route_action, dict):
            route_action = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction(**route_action)
        if isinstance(url_redirect, dict):
            url_redirect = GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect(**url_redirect)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRule.__init__)
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
            check_type(argname="argument route_action", value=route_action, expected_type=type_hints["route_action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument url_redirect", value=url_redirect, expected_type=type_hints["url_redirect"])
        self._values: typing.Dict[str, typing.Any] = {
            "paths": paths,
        }
        if route_action is not None:
            self._values["route_action"] = route_action
        if service is not None:
            self._values["service"] = service
        if url_redirect is not None:
            self._values["url_redirect"] = url_redirect

    @builtins.property
    def paths(self) -> typing.List[builtins.str]:
        '''The list of path patterns to match.

        Each must start with / and the only place a

        - is allowed is at the end following a /. The string fed to the path matcher
          does not include any text after the first ? or #, and those chars are not
          allowed here.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#paths GoogleComputeRegionUrlMap#paths}
        '''
        result = self._values.get("paths")
        assert result is not None, "Required property 'paths' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def route_action(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction"]:
        '''route_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#route_action GoogleComputeRegionUrlMap#route_action}
        '''
        result = self._values.get("route_action")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction"], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''The region backend service resource to which traffic is directed if this rule is matched.

        If routeAction is additionally specified,
        advanced routing actions like URL Rewrites, etc. take effect prior to sending
        the request to the backend. However, if service is specified, routeAction cannot
        contain any weightedBackendService s. Conversely, if routeAction specifies any
        weightedBackendServices, service must not be specified. Only one of urlRedirect,
        service or routeAction.weightedBackendService must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#service GoogleComputeRegionUrlMap#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_redirect(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect"]:
        '''url_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_redirect GoogleComputeRegionUrlMap#url_redirect}
        '''
        result = self._values.get("url_redirect")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRouteAction")
    def put_route_action(
        self,
        *,
        cors_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy", typing.Dict[str, typing.Any]]] = None,
        fault_injection_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy", typing.Dict[str, typing.Any]]] = None,
        request_mirror_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout", typing.Dict[str, typing.Any]]] = None,
        url_rewrite: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite", typing.Dict[str, typing.Any]]] = None,
        weighted_backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cors_policy: cors_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#cors_policy GoogleComputeRegionUrlMap#cors_policy}
        :param fault_injection_policy: fault_injection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fault_injection_policy GoogleComputeRegionUrlMap#fault_injection_policy}
        :param request_mirror_policy: request_mirror_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_mirror_policy GoogleComputeRegionUrlMap#request_mirror_policy}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_policy GoogleComputeRegionUrlMap#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeout GoogleComputeRegionUrlMap#timeout}
        :param url_rewrite: url_rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_rewrite GoogleComputeRegionUrlMap#url_rewrite}
        :param weighted_backend_services: weighted_backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weighted_backend_services GoogleComputeRegionUrlMap#weighted_backend_services}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction(
            cors_policy=cors_policy,
            fault_injection_policy=fault_injection_policy,
            request_mirror_policy=request_mirror_policy,
            retry_policy=retry_policy,
            timeout=timeout,
            url_rewrite=url_rewrite,
            weighted_backend_services=weighted_backend_services,
        )

        return typing.cast(None, jsii.invoke(self, "putRouteAction", [value]))

    @jsii.member(jsii_name="putUrlRedirect")
    def put_url_redirect(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect(
            strip_query=strip_query,
            host_redirect=host_redirect,
            https_redirect=https_redirect,
            path_redirect=path_redirect,
            prefix_redirect=prefix_redirect,
            redirect_response_code=redirect_response_code,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRedirect", [value]))

    @jsii.member(jsii_name="resetRouteAction")
    def reset_route_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteAction", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetUrlRedirect")
    def reset_url_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRedirect", []))

    @builtins.property
    @jsii.member(jsii_name="routeAction")
    def route_action(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference", jsii.get(self, "routeAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirect")
    def url_redirect(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference", jsii.get(self, "urlRedirect"))

    @builtins.property
    @jsii.member(jsii_name="pathsInput")
    def paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathsInput"))

    @builtins.property
    @jsii.member(jsii_name="routeActionInput")
    def route_action_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction"], jsii.get(self, "routeActionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectInput")
    def url_redirect_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect"], jsii.get(self, "urlRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="paths")
    def paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "paths"))

    @paths.setter
    def paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference, "paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paths", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction",
    jsii_struct_bases=[],
    name_mapping={
        "cors_policy": "corsPolicy",
        "fault_injection_policy": "faultInjectionPolicy",
        "request_mirror_policy": "requestMirrorPolicy",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
        "url_rewrite": "urlRewrite",
        "weighted_backend_services": "weightedBackendServices",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction:
    def __init__(
        self,
        *,
        cors_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy", typing.Dict[str, typing.Any]]] = None,
        fault_injection_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy", typing.Dict[str, typing.Any]]] = None,
        request_mirror_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout", typing.Dict[str, typing.Any]]] = None,
        url_rewrite: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite", typing.Dict[str, typing.Any]]] = None,
        weighted_backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cors_policy: cors_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#cors_policy GoogleComputeRegionUrlMap#cors_policy}
        :param fault_injection_policy: fault_injection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fault_injection_policy GoogleComputeRegionUrlMap#fault_injection_policy}
        :param request_mirror_policy: request_mirror_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_mirror_policy GoogleComputeRegionUrlMap#request_mirror_policy}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_policy GoogleComputeRegionUrlMap#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeout GoogleComputeRegionUrlMap#timeout}
        :param url_rewrite: url_rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_rewrite GoogleComputeRegionUrlMap#url_rewrite}
        :param weighted_backend_services: weighted_backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weighted_backend_services GoogleComputeRegionUrlMap#weighted_backend_services}
        '''
        if isinstance(cors_policy, dict):
            cors_policy = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy(**cors_policy)
        if isinstance(fault_injection_policy, dict):
            fault_injection_policy = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy(**fault_injection_policy)
        if isinstance(request_mirror_policy, dict):
            request_mirror_policy = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy(**request_mirror_policy)
        if isinstance(retry_policy, dict):
            retry_policy = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout(**timeout)
        if isinstance(url_rewrite, dict):
            url_rewrite = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite(**url_rewrite)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction.__init__)
            check_type(argname="argument cors_policy", value=cors_policy, expected_type=type_hints["cors_policy"])
            check_type(argname="argument fault_injection_policy", value=fault_injection_policy, expected_type=type_hints["fault_injection_policy"])
            check_type(argname="argument request_mirror_policy", value=request_mirror_policy, expected_type=type_hints["request_mirror_policy"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument url_rewrite", value=url_rewrite, expected_type=type_hints["url_rewrite"])
            check_type(argname="argument weighted_backend_services", value=weighted_backend_services, expected_type=type_hints["weighted_backend_services"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cors_policy is not None:
            self._values["cors_policy"] = cors_policy
        if fault_injection_policy is not None:
            self._values["fault_injection_policy"] = fault_injection_policy
        if request_mirror_policy is not None:
            self._values["request_mirror_policy"] = request_mirror_policy
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout
        if url_rewrite is not None:
            self._values["url_rewrite"] = url_rewrite
        if weighted_backend_services is not None:
            self._values["weighted_backend_services"] = weighted_backend_services

    @builtins.property
    def cors_policy(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy"]:
        '''cors_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#cors_policy GoogleComputeRegionUrlMap#cors_policy}
        '''
        result = self._values.get("cors_policy")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy"], result)

    @builtins.property
    def fault_injection_policy(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy"]:
        '''fault_injection_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fault_injection_policy GoogleComputeRegionUrlMap#fault_injection_policy}
        '''
        result = self._values.get("fault_injection_policy")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy"], result)

    @builtins.property
    def request_mirror_policy(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy"]:
        '''request_mirror_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_mirror_policy GoogleComputeRegionUrlMap#request_mirror_policy}
        '''
        result = self._values.get("request_mirror_policy")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy"], result)

    @builtins.property
    def retry_policy(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_policy GoogleComputeRegionUrlMap#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy"], result)

    @builtins.property
    def timeout(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeout GoogleComputeRegionUrlMap#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout"], result)

    @builtins.property
    def url_rewrite(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite"]:
        '''url_rewrite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_rewrite GoogleComputeRegionUrlMap#url_rewrite}
        '''
        result = self._values.get("url_rewrite")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite"], result)

    @builtins.property
    def weighted_backend_services(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices"]]]:
        '''weighted_backend_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weighted_backend_services GoogleComputeRegionUrlMap#weighted_backend_services}
        '''
        result = self._values.get("weighted_backend_services")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "disabled": "disabled",
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origin_regexes": "allowOriginRegexes",
        "allow_origins": "allowOrigins",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy:
    def __init__(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin_regexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param disabled: If true, specifies the CORS policy is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#disabled GoogleComputeRegionUrlMap#disabled}
        :param allow_credentials: In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access- Control-Allow-Credentials header. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_credentials GoogleComputeRegionUrlMap#allow_credentials}
        :param allow_headers: Specifies the content for the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_headers GoogleComputeRegionUrlMap#allow_headers}
        :param allow_methods: Specifies the content for the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_methods GoogleComputeRegionUrlMap#allow_methods}
        :param allow_origin_regexes: Specifies the regular expression patterns that match allowed origins. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origin_regexes GoogleComputeRegionUrlMap#allow_origin_regexes}
        :param allow_origins: Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origins GoogleComputeRegionUrlMap#allow_origins}
        :param expose_headers: Specifies the content for the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#expose_headers GoogleComputeRegionUrlMap#expose_headers}
        :param max_age: Specifies how long the results of a preflight request can be cached. This translates to the content for the Access-Control-Max-Age header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#max_age GoogleComputeRegionUrlMap#max_age}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
            check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
            check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
            check_type(argname="argument allow_origin_regexes", value=allow_origin_regexes, expected_type=type_hints["allow_origin_regexes"])
            check_type(argname="argument allow_origins", value=allow_origins, expected_type=type_hints["allow_origins"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[str, typing.Any] = {
            "disabled": disabled,
        }
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origin_regexes is not None:
            self._values["allow_origin_regexes"] = allow_origin_regexes
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If true, specifies the CORS policy is disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#disabled GoogleComputeRegionUrlMap#disabled}
        '''
        result = self._values.get("disabled")
        assert result is not None, "Required property 'disabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def allow_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''In response to a preflight request, setting this to true indicates that the actual request can include user credentials.

        This translates to the Access-
        Control-Allow-Credentials header. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_credentials GoogleComputeRegionUrlMap#allow_credentials}
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Allow-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_headers GoogleComputeRegionUrlMap#allow_headers}
        '''
        result = self._values.get("allow_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Allow-Methods header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_methods GoogleComputeRegionUrlMap#allow_methods}
        '''
        result = self._values.get("allow_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origin_regexes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the regular expression patterns that match allowed origins.

        For
        regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript
        An origin is allowed if it matches either allow_origins or allow_origin_regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origin_regexes GoogleComputeRegionUrlMap#allow_origin_regexes}
        '''
        result = self._values.get("allow_origin_regexes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of origins that will be allowed to do CORS requests.

        An
        origin is allowed if it matches either allow_origins or allow_origin_regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origins GoogleComputeRegionUrlMap#allow_origins}
        '''
        result = self._values.get("allow_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Expose-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#expose_headers GoogleComputeRegionUrlMap#expose_headers}
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[jsii.Number]:
        '''Specifies how long the results of a preflight request can be cached.

        This
        translates to the content for the Access-Control-Max-Age header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#max_age GoogleComputeRegionUrlMap#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowCredentials")
    def reset_allow_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCredentials", []))

    @jsii.member(jsii_name="resetAllowHeaders")
    def reset_allow_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowHeaders", []))

    @jsii.member(jsii_name="resetAllowMethods")
    def reset_allow_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMethods", []))

    @jsii.member(jsii_name="resetAllowOriginRegexes")
    def reset_allow_origin_regexes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOriginRegexes", []))

    @jsii.member(jsii_name="resetAllowOrigins")
    def reset_allow_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOrigins", []))

    @jsii.member(jsii_name="resetExposeHeaders")
    def reset_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeHeaders", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @builtins.property
    @jsii.member(jsii_name="allowCredentialsInput")
    def allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowHeadersInput")
    def allow_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMethodsInput")
    def allow_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginRegexesInput")
    def allow_origin_regexes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowOriginRegexesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginsInput")
    def allow_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeHeadersInput")
    def expose_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentials")
    def allow_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCredentials"))

    @allow_credentials.setter
    def allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="allowHeaders")
    def allow_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowHeaders"))

    @allow_headers.setter
    def allow_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowMethods")
    def allow_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowMethods"))

    @allow_methods.setter
    def allow_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowOriginRegexes")
    def allow_origin_regexes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowOriginRegexes"))

    @allow_origin_regexes.setter
    def allow_origin_regexes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_origin_regexes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOriginRegexes", value)

    @builtins.property
    @jsii.member(jsii_name="allowOrigins")
    def allow_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowOrigins"))

    @allow_origins.setter
    def allow_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "allow_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="exposeHeaders")
    def expose_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposeHeaders"))

    @expose_headers.setter
    def expose_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "expose_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy",
    jsii_struct_bases=[],
    name_mapping={"abort": "abort", "delay": "delay"},
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy:
    def __init__(
        self,
        *,
        abort: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort", typing.Dict[str, typing.Any]]] = None,
        delay: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abort: abort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#abort GoogleComputeRegionUrlMap#abort}
        :param delay: delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delay GoogleComputeRegionUrlMap#delay}
        '''
        if isinstance(abort, dict):
            abort = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort(**abort)
        if isinstance(delay, dict):
            delay = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay(**delay)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy.__init__)
            check_type(argname="argument abort", value=abort, expected_type=type_hints["abort"])
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
        self._values: typing.Dict[str, typing.Any] = {}
        if abort is not None:
            self._values["abort"] = abort
        if delay is not None:
            self._values["delay"] = delay

    @builtins.property
    def abort(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort"]:
        '''abort block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#abort GoogleComputeRegionUrlMap#abort}
        '''
        result = self._values.get("abort")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort"], result)

    @builtins.property
    def delay(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay"]:
        '''delay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delay GoogleComputeRegionUrlMap#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort",
    jsii_struct_bases=[],
    name_mapping={"http_status": "httpStatus", "percentage": "percentage"},
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort:
    def __init__(self, *, http_status: jsii.Number, percentage: jsii.Number) -> None:
        '''
        :param http_status: The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#http_status GoogleComputeRegionUrlMap#http_status}
        :param percentage: The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort.__init__)
            check_type(argname="argument http_status", value=http_status, expected_type=type_hints["http_status"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_status": http_status,
            "percentage": percentage,
        }

    @builtins.property
    def http_status(self) -> jsii.Number:
        '''The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#http_status GoogleComputeRegionUrlMap#http_status}
        '''
        result = self._values.get("http_status")
        assert result is not None, "Required property 'http_status' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def percentage(self) -> jsii.Number:
        '''The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection.

        The value must be between 0.0 and 100.0
        inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        result = self._values.get("percentage")
        assert result is not None, "Required property 'percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="httpStatusInput")
    def http_status_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="httpStatus")
    def http_status(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpStatus"))

    @http_status.setter
    def http_status(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference, "http_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpStatus", value)

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay",
    jsii_struct_bases=[],
    name_mapping={"fixed_delay": "fixedDelay", "percentage": "percentage"},
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay:
    def __init__(
        self,
        *,
        fixed_delay: typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay", typing.Dict[str, typing.Any]],
        percentage: jsii.Number,
    ) -> None:
        '''
        :param fixed_delay: fixed_delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fixed_delay GoogleComputeRegionUrlMap#fixed_delay}
        :param percentage: The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        if isinstance(fixed_delay, dict):
            fixed_delay = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay(**fixed_delay)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay.__init__)
            check_type(argname="argument fixed_delay", value=fixed_delay, expected_type=type_hints["fixed_delay"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {
            "fixed_delay": fixed_delay,
            "percentage": percentage,
        }

    @builtins.property
    def fixed_delay(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay":
        '''fixed_delay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fixed_delay GoogleComputeRegionUrlMap#fixed_delay}
        '''
        result = self._values.get("fixed_delay")
        assert result is not None, "Required property 'fixed_delay' is missing"
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay", result)

    @builtins.property
    def percentage(self) -> jsii.Number:
        '''The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection.

        The value must be between 0.0 and
        100.0 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        result = self._values.get("percentage")
        assert result is not None, "Required property 'percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFixedDelay")
    def put_fixed_delay(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putFixedDelay", [value]))

    @builtins.property
    @jsii.member(jsii_name="fixedDelay")
    def fixed_delay(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, jsii.get(self, "fixedDelay"))

    @builtins.property
    @jsii.member(jsii_name="fixedDelayInput")
    def fixed_delay_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay], jsii.get(self, "fixedDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAbort")
    def put_abort(self, *, http_status: jsii.Number, percentage: jsii.Number) -> None:
        '''
        :param http_status: The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#http_status GoogleComputeRegionUrlMap#http_status}
        :param percentage: The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort(
            http_status=http_status, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putAbort", [value]))

    @jsii.member(jsii_name="putDelay")
    def put_delay(
        self,
        *,
        fixed_delay: typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay, typing.Dict[str, typing.Any]],
        percentage: jsii.Number,
    ) -> None:
        '''
        :param fixed_delay: fixed_delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fixed_delay GoogleComputeRegionUrlMap#fixed_delay}
        :param percentage: The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay(
            fixed_delay=fixed_delay, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putDelay", [value]))

    @jsii.member(jsii_name="resetAbort")
    def reset_abort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbort", []))

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @builtins.property
    @jsii.member(jsii_name="abort")
    def abort(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference, jsii.get(self, "abort"))

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference, jsii.get(self, "delay"))

    @builtins.property
    @jsii.member(jsii_name="abortInput")
    def abort_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort], jsii.get(self, "abortInput"))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCorsPolicy")
    def put_cors_policy(
        self,
        *,
        disabled: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin_regexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param disabled: If true, specifies the CORS policy is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#disabled GoogleComputeRegionUrlMap#disabled}
        :param allow_credentials: In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access- Control-Allow-Credentials header. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_credentials GoogleComputeRegionUrlMap#allow_credentials}
        :param allow_headers: Specifies the content for the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_headers GoogleComputeRegionUrlMap#allow_headers}
        :param allow_methods: Specifies the content for the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_methods GoogleComputeRegionUrlMap#allow_methods}
        :param allow_origin_regexes: Specifies the regular expression patterns that match allowed origins. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origin_regexes GoogleComputeRegionUrlMap#allow_origin_regexes}
        :param allow_origins: Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origins GoogleComputeRegionUrlMap#allow_origins}
        :param expose_headers: Specifies the content for the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#expose_headers GoogleComputeRegionUrlMap#expose_headers}
        :param max_age: Specifies how long the results of a preflight request can be cached. This translates to the content for the Access-Control-Max-Age header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#max_age GoogleComputeRegionUrlMap#max_age}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy(
            disabled=disabled,
            allow_credentials=allow_credentials,
            allow_headers=allow_headers,
            allow_methods=allow_methods,
            allow_origin_regexes=allow_origin_regexes,
            allow_origins=allow_origins,
            expose_headers=expose_headers,
            max_age=max_age,
        )

        return typing.cast(None, jsii.invoke(self, "putCorsPolicy", [value]))

    @jsii.member(jsii_name="putFaultInjectionPolicy")
    def put_fault_injection_policy(
        self,
        *,
        abort: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort, typing.Dict[str, typing.Any]]] = None,
        delay: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abort: abort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#abort GoogleComputeRegionUrlMap#abort}
        :param delay: delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delay GoogleComputeRegionUrlMap#delay}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy(
            abort=abort, delay=delay
        )

        return typing.cast(None, jsii.invoke(self, "putFaultInjectionPolicy", [value]))

    @jsii.member(jsii_name="putRequestMirrorPolicy")
    def put_request_mirror_policy(self, *, backend_service: builtins.str) -> None:
        '''
        :param backend_service: The RegionBackendService resource being mirrored to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy(
            backend_service=backend_service
        )

        return typing.cast(None, jsii.invoke(self, "putRequestMirrorPolicy", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        num_retries: typing.Optional[jsii.Number] = None,
        per_try_timeout: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout", typing.Dict[str, typing.Any]]] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param num_retries: Specifies the allowed number retries. This number must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#num_retries GoogleComputeRegionUrlMap#num_retries}
        :param per_try_timeout: per_try_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#per_try_timeout GoogleComputeRegionUrlMap#per_try_timeout}
        :param retry_conditions: Specifies one or more conditions when this retry rule applies. Valid values are:. - 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code, or if the backend service does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. - gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504. - connect-failure: Loadbalancer will retry on failures connecting to backend services, for example due to connection timeouts. - retriable-4xx: Loadbalancer will retry for retriable 4xx response codes. Currently the only retriable error supported is 409. - refused-stream: Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. - cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled - deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded - resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted - unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_conditions GoogleComputeRegionUrlMap#retry_conditions}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy(
            num_retries=num_retries,
            per_try_timeout=per_try_timeout,
            retry_conditions=retry_conditions,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="putUrlRewrite")
    def put_url_rewrite(
        self,
        *,
        host_rewrite: typing.Optional[builtins.str] = None,
        path_prefix_rewrite: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_rewrite: Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rewrite GoogleComputeRegionUrlMap#host_rewrite}
        :param path_prefix_rewrite: Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_prefix_rewrite GoogleComputeRegionUrlMap#path_prefix_rewrite}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite(
            host_rewrite=host_rewrite, path_prefix_rewrite=path_prefix_rewrite
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRewrite", [value]))

    @jsii.member(jsii_name="putWeightedBackendServices")
    def put_weighted_backend_services(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference.put_weighted_backend_services)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeightedBackendServices", [value]))

    @jsii.member(jsii_name="resetCorsPolicy")
    def reset_cors_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsPolicy", []))

    @jsii.member(jsii_name="resetFaultInjectionPolicy")
    def reset_fault_injection_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaultInjectionPolicy", []))

    @jsii.member(jsii_name="resetRequestMirrorPolicy")
    def reset_request_mirror_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMirrorPolicy", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetUrlRewrite")
    def reset_url_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRewrite", []))

    @jsii.member(jsii_name="resetWeightedBackendServices")
    def reset_weighted_backend_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedBackendServices", []))

    @builtins.property
    @jsii.member(jsii_name="corsPolicy")
    def cors_policy(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference, jsii.get(self, "corsPolicy"))

    @builtins.property
    @jsii.member(jsii_name="faultInjectionPolicy")
    def fault_injection_policy(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference, jsii.get(self, "faultInjectionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="requestMirrorPolicy")
    def request_mirror_policy(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference", jsii.get(self, "requestMirrorPolicy"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="urlRewrite")
    def url_rewrite(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference", jsii.get(self, "urlRewrite"))

    @builtins.property
    @jsii.member(jsii_name="weightedBackendServices")
    def weighted_backend_services(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList", jsii.get(self, "weightedBackendServices"))

    @builtins.property
    @jsii.member(jsii_name="corsPolicyInput")
    def cors_policy_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy], jsii.get(self, "corsPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="faultInjectionPolicyInput")
    def fault_injection_policy_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy], jsii.get(self, "faultInjectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMirrorPolicyInput")
    def request_mirror_policy_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy"], jsii.get(self, "requestMirrorPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteInput")
    def url_rewrite_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite"], jsii.get(self, "urlRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedBackendServicesInput")
    def weighted_backend_services_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices"]]], jsii.get(self, "weightedBackendServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy",
    jsii_struct_bases=[],
    name_mapping={"backend_service": "backendService"},
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy:
    def __init__(self, *, backend_service: builtins.str) -> None:
        '''
        :param backend_service: The RegionBackendService resource being mirrored to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy.__init__)
            check_type(argname="argument backend_service", value=backend_service, expected_type=type_hints["backend_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_service": backend_service,
        }

    @builtins.property
    def backend_service(self) -> builtins.str:
        '''The RegionBackendService resource being mirrored to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        '''
        result = self._values.get("backend_service")
        assert result is not None, "Required property 'backend_service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="backendServiceInput")
    def backend_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="backendService")
    def backend_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendService"))

    @backend_service.setter
    def backend_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference, "backend_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendService", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "num_retries": "numRetries",
        "per_try_timeout": "perTryTimeout",
        "retry_conditions": "retryConditions",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy:
    def __init__(
        self,
        *,
        num_retries: typing.Optional[jsii.Number] = None,
        per_try_timeout: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout", typing.Dict[str, typing.Any]]] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param num_retries: Specifies the allowed number retries. This number must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#num_retries GoogleComputeRegionUrlMap#num_retries}
        :param per_try_timeout: per_try_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#per_try_timeout GoogleComputeRegionUrlMap#per_try_timeout}
        :param retry_conditions: Specifies one or more conditions when this retry rule applies. Valid values are:. - 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code, or if the backend service does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. - gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504. - connect-failure: Loadbalancer will retry on failures connecting to backend services, for example due to connection timeouts. - retriable-4xx: Loadbalancer will retry for retriable 4xx response codes. Currently the only retriable error supported is 409. - refused-stream: Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. - cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled - deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded - resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted - unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_conditions GoogleComputeRegionUrlMap#retry_conditions}
        '''
        if isinstance(per_try_timeout, dict):
            per_try_timeout = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout(**per_try_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy.__init__)
            check_type(argname="argument num_retries", value=num_retries, expected_type=type_hints["num_retries"])
            check_type(argname="argument per_try_timeout", value=per_try_timeout, expected_type=type_hints["per_try_timeout"])
            check_type(argname="argument retry_conditions", value=retry_conditions, expected_type=type_hints["retry_conditions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if num_retries is not None:
            self._values["num_retries"] = num_retries
        if per_try_timeout is not None:
            self._values["per_try_timeout"] = per_try_timeout
        if retry_conditions is not None:
            self._values["retry_conditions"] = retry_conditions

    @builtins.property
    def num_retries(self) -> typing.Optional[jsii.Number]:
        '''Specifies the allowed number retries. This number must be > 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#num_retries GoogleComputeRegionUrlMap#num_retries}
        '''
        result = self._values.get("num_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def per_try_timeout(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout"]:
        '''per_try_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#per_try_timeout GoogleComputeRegionUrlMap#per_try_timeout}
        '''
        result = self._values.get("per_try_timeout")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout"], result)

    @builtins.property
    def retry_conditions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies one or more conditions when this retry rule applies. Valid values are:.

        - 5xx: Loadbalancer will attempt a retry if the backend service responds with
          any 5xx response code, or if the backend service does not respond at all,
          example: disconnects, reset, read timeout, connection failure, and refused
          streams.
        - gateway-error: Similar to 5xx, but only applies to response codes
          502, 503 or 504.
        - connect-failure: Loadbalancer will retry on failures
          connecting to backend services, for example due to connection timeouts.
        - retriable-4xx: Loadbalancer will retry for retriable 4xx response codes.
          Currently the only retriable error supported is 409.
        - refused-stream: Loadbalancer will retry if the backend service resets the stream with a
          REFUSED_STREAM error code. This reset type indicates that it is safe to retry.
        - cancelled: Loadbalancer will retry if the gRPC status code in the response
          header is set to cancelled
        - deadline-exceeded: Loadbalancer will retry if the
          gRPC status code in the response header is set to deadline-exceeded
        - resource-exhausted: Loadbalancer will retry if the gRPC status code in the response
          header is set to resource-exhausted
        - unavailable: Loadbalancer will retry if
          the gRPC status code in the response header is set to unavailable

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_conditions GoogleComputeRegionUrlMap#retry_conditions}
        '''
        result = self._values.get("retry_conditions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPerTryTimeout")
    def put_per_try_timeout(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putPerTryTimeout", [value]))

    @jsii.member(jsii_name="resetNumRetries")
    def reset_num_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumRetries", []))

    @jsii.member(jsii_name="resetPerTryTimeout")
    def reset_per_try_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerTryTimeout", []))

    @jsii.member(jsii_name="resetRetryConditions")
    def reset_retry_conditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryConditions", []))

    @builtins.property
    @jsii.member(jsii_name="perTryTimeout")
    def per_try_timeout(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference", jsii.get(self, "perTryTimeout"))

    @builtins.property
    @jsii.member(jsii_name="numRetriesInput")
    def num_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="perTryTimeoutInput")
    def per_try_timeout_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout"], jsii.get(self, "perTryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="retryConditionsInput")
    def retry_conditions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "retryConditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="numRetries")
    def num_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numRetries"))

    @num_retries.setter
    def num_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference, "num_retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numRetries", value)

    @builtins.property
    @jsii.member(jsii_name="retryConditions")
    def retry_conditions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "retryConditions"))

    @retry_conditions.setter
    def retry_conditions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference, "retry_conditions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryConditions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite",
    jsii_struct_bases=[],
    name_mapping={
        "host_rewrite": "hostRewrite",
        "path_prefix_rewrite": "pathPrefixRewrite",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite:
    def __init__(
        self,
        *,
        host_rewrite: typing.Optional[builtins.str] = None,
        path_prefix_rewrite: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_rewrite: Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rewrite GoogleComputeRegionUrlMap#host_rewrite}
        :param path_prefix_rewrite: Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_prefix_rewrite GoogleComputeRegionUrlMap#path_prefix_rewrite}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite.__init__)
            check_type(argname="argument host_rewrite", value=host_rewrite, expected_type=type_hints["host_rewrite"])
            check_type(argname="argument path_prefix_rewrite", value=path_prefix_rewrite, expected_type=type_hints["path_prefix_rewrite"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_rewrite is not None:
            self._values["host_rewrite"] = host_rewrite
        if path_prefix_rewrite is not None:
            self._values["path_prefix_rewrite"] = path_prefix_rewrite

    @builtins.property
    def host_rewrite(self) -> typing.Optional[builtins.str]:
        '''Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite.

        The value must be between 1 and
        255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rewrite GoogleComputeRegionUrlMap#host_rewrite}
        '''
        result = self._values.get("host_rewrite")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_prefix_rewrite(self) -> typing.Optional[builtins.str]:
        '''Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite.

        The value must
        be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_prefix_rewrite GoogleComputeRegionUrlMap#path_prefix_rewrite}
        '''
        result = self._values.get("path_prefix_rewrite")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRewrite")
    def reset_host_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRewrite", []))

    @jsii.member(jsii_name="resetPathPrefixRewrite")
    def reset_path_prefix_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPrefixRewrite", []))

    @builtins.property
    @jsii.member(jsii_name="hostRewriteInput")
    def host_rewrite_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixRewriteInput")
    def path_prefix_rewrite_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRewrite")
    def host_rewrite(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRewrite"))

    @host_rewrite.setter
    def host_rewrite(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference, "host_rewrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRewrite", value)

    @builtins.property
    @jsii.member(jsii_name="pathPrefixRewrite")
    def path_prefix_rewrite(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefixRewrite"))

    @path_prefix_rewrite.setter
    def path_prefix_rewrite(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference, "path_prefix_rewrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefixRewrite", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices",
    jsii_struct_bases=[],
    name_mapping={
        "backend_service": "backendService",
        "weight": "weight",
        "header_action": "headerAction",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices:
    def __init__(
        self,
        *,
        backend_service: builtins.str,
        weight: jsii.Number,
        header_action: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backend_service: The default RegionBackendService resource. Before forwarding the request to backendService, the loadbalancer applies any relevant headerActions specified as part of this backendServiceWeight. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        :param weight: Specifies the fraction of traffic sent to backendService, computed as weight / (sum of all weightedBackendService weights in routeAction) . The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backendService, subsequent requests will be sent to the same backendService as determined by the BackendService's session affinity policy. The value must be between 0 and 1000 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weight GoogleComputeRegionUrlMap#weight}
        :param header_action: header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_action GoogleComputeRegionUrlMap#header_action}
        '''
        if isinstance(header_action, dict):
            header_action = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction(**header_action)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices.__init__)
            check_type(argname="argument backend_service", value=backend_service, expected_type=type_hints["backend_service"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument header_action", value=header_action, expected_type=type_hints["header_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_service": backend_service,
            "weight": weight,
        }
        if header_action is not None:
            self._values["header_action"] = header_action

    @builtins.property
    def backend_service(self) -> builtins.str:
        '''The default RegionBackendService resource.

        Before
        forwarding the request to backendService, the loadbalancer applies any relevant
        headerActions specified as part of this backendServiceWeight.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        '''
        result = self._values.get("backend_service")
        assert result is not None, "Required property 'backend_service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Specifies the fraction of traffic sent to backendService, computed as weight / (sum of all weightedBackendService weights in routeAction) .

        The selection of a
        backend service is determined only for new traffic. Once a user's request has
        been directed to a backendService, subsequent requests will be sent to the same
        backendService as determined by the BackendService's session affinity policy.
        The value must be between 0 and 1000

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weight GoogleComputeRegionUrlMap#weight}
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def header_action(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction"]:
        '''header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_action GoogleComputeRegionUrlMap#header_action}
        '''
        result = self._values.get("header_action")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction",
    jsii_struct_bases=[],
    name_mapping={
        "request_headers_to_add": "requestHeadersToAdd",
        "request_headers_to_remove": "requestHeadersToRemove",
        "response_headers_to_add": "responseHeadersToAdd",
        "response_headers_to_remove": "responseHeadersToRemove",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction:
    def __init__(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction.__init__)
            check_type(argname="argument request_headers_to_add", value=request_headers_to_add, expected_type=type_hints["request_headers_to_add"])
            check_type(argname="argument request_headers_to_remove", value=request_headers_to_remove, expected_type=type_hints["request_headers_to_remove"])
            check_type(argname="argument response_headers_to_add", value=response_headers_to_add, expected_type=type_hints["response_headers_to_add"])
            check_type(argname="argument response_headers_to_remove", value=response_headers_to_remove, expected_type=type_hints["response_headers_to_remove"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request_headers_to_add is not None:
            self._values["request_headers_to_add"] = request_headers_to_add
        if request_headers_to_remove is not None:
            self._values["request_headers_to_remove"] = request_headers_to_remove
        if response_headers_to_add is not None:
            self._values["response_headers_to_add"] = response_headers_to_add
        if response_headers_to_remove is not None:
            self._values["response_headers_to_remove"] = response_headers_to_remove

    @builtins.property
    def request_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]]:
        '''request_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        '''
        result = self._values.get("request_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]], result)

    @builtins.property
    def request_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        '''
        result = self._values.get("request_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def response_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]]:
        '''response_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        '''
        result = self._values.get("response_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]], result)

    @builtins.property
    def response_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the response prior to sending the response back to the client.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        result = self._values.get("response_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestHeadersToAdd")
    def put_request_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference.put_request_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeadersToAdd", [value]))

    @jsii.member(jsii_name="putResponseHeadersToAdd")
    def put_response_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference.put_response_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeadersToAdd", [value]))

    @jsii.member(jsii_name="resetRequestHeadersToAdd")
    def reset_request_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToAdd", []))

    @jsii.member(jsii_name="resetRequestHeadersToRemove")
    def reset_request_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToRemove", []))

    @jsii.member(jsii_name="resetResponseHeadersToAdd")
    def reset_response_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToAdd", []))

    @jsii.member(jsii_name="resetResponseHeadersToRemove")
    def reset_response_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToRemove", []))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAdd")
    def request_headers_to_add(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList", jsii.get(self, "requestHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAdd")
    def response_headers_to_add(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList", jsii.get(self, "responseHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAddInput")
    def request_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]], jsii.get(self, "requestHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemoveInput")
    def request_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAddInput")
    def response_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]], jsii.get(self, "responseHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemoveInput")
    def response_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemove")
    def request_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestHeadersToRemove"))

    @request_headers_to_remove.setter
    def request_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference, "request_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemove")
    def response_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseHeadersToRemove"))

    @response_headers_to_remove.setter
    def response_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference, "response_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaderAction")
    def put_header_action(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction(
            request_headers_to_add=request_headers_to_add,
            request_headers_to_remove=request_headers_to_remove,
            response_headers_to_add=response_headers_to_add,
            response_headers_to_remove=response_headers_to_remove,
        )

        return typing.cast(None, jsii.invoke(self, "putHeaderAction", [value]))

    @jsii.member(jsii_name="resetHeaderAction")
    def reset_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderAction", []))

    @builtins.property
    @jsii.member(jsii_name="headerAction")
    def header_action(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference, jsii.get(self, "headerAction"))

    @builtins.property
    @jsii.member(jsii_name="backendServiceInput")
    def backend_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerActionInput")
    def header_action_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction], jsii.get(self, "headerActionInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="backendService")
    def backend_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendService"))

    @backend_service.setter
    def backend_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference, "backend_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendService", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "strip_query": "stripQuery",
        "host_redirect": "hostRedirect",
        "https_redirect": "httpsRedirect",
        "path_redirect": "pathRedirect",
        "prefix_redirect": "prefixRedirect",
        "redirect_response_code": "redirectResponseCode",
    },
)
class GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect:
    def __init__(
        self,
        *,
        strip_query: typing.Union[builtins.bool, cdktf.IResolvable],
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. This field is required to ensure an empty block is not set. The normal default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect.__init__)
            check_type(argname="argument strip_query", value=strip_query, expected_type=type_hints["strip_query"])
            check_type(argname="argument host_redirect", value=host_redirect, expected_type=type_hints["host_redirect"])
            check_type(argname="argument https_redirect", value=https_redirect, expected_type=type_hints["https_redirect"])
            check_type(argname="argument path_redirect", value=path_redirect, expected_type=type_hints["path_redirect"])
            check_type(argname="argument prefix_redirect", value=prefix_redirect, expected_type=type_hints["prefix_redirect"])
            check_type(argname="argument redirect_response_code", value=redirect_response_code, expected_type=type_hints["redirect_response_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "strip_query": strip_query,
        }
        if host_redirect is not None:
            self._values["host_redirect"] = host_redirect
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if path_redirect is not None:
            self._values["path_redirect"] = path_redirect
        if prefix_redirect is not None:
            self._values["prefix_redirect"] = prefix_redirect
        if redirect_response_code is not None:
            self._values["redirect_response_code"] = redirect_response_code

    @builtins.property
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request.

        If set to false, the query portion of the
        original URL is retained.
        This field is required to ensure an empty block is not set. The normal default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        '''
        result = self._values.get("strip_query")
        assert result is not None, "Required property 'strip_query' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def host_redirect(self) -> typing.Optional[builtins.str]:
        '''The host that will be used in the redirect response instead of the one that was supplied in the request.

        The value must be between 1 and 255
        characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        '''
        result = self._values.get("host_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the URL scheme in the redirected request is set to https.

        If set to false, the URL scheme of the redirected request will remain the
        same as that of the request. This must only be set for UrlMaps used in
        TargetHttpProxys. Setting this true for TargetHttpsProxy is not
        permitted. The default is set to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_redirect(self) -> typing.Optional[builtins.str]:
        '''The path that will be used in the redirect response instead of the one that was supplied in the request.

        pathRedirect cannot be supplied
        together with prefixRedirect. Supply one alone or neither. If neither is
        supplied, the path of the original request will be used for the redirect.
        The value must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        '''
        result = self._values.get("path_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_redirect(self) -> typing.Optional[builtins.str]:
        '''The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request.

        prefixRedirect cannot be supplied together with
        pathRedirect. Supply one alone or neither. If neither is supplied, the
        path of the original request will be used for the redirect. The value
        must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        '''
        result = self._values.get("prefix_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_response_code(self) -> typing.Optional[builtins.str]:
        '''The HTTP Status code to use for this RedirectAction. Supported values are:.

        MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.

        FOUND, which corresponds to 302.

        SEE_OTHER which corresponds to 303.

        TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        will be retained.

        PERMANENT_REDIRECT, which corresponds to 308. In this case,
        the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        result = self._values.get("redirect_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRedirect")
    def reset_host_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRedirect", []))

    @jsii.member(jsii_name="resetHttpsRedirect")
    def reset_https_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirect", []))

    @jsii.member(jsii_name="resetPathRedirect")
    def reset_path_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRedirect", []))

    @jsii.member(jsii_name="resetPrefixRedirect")
    def reset_prefix_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixRedirect", []))

    @jsii.member(jsii_name="resetRedirectResponseCode")
    def reset_redirect_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectResponseCode", []))

    @builtins.property
    @jsii.member(jsii_name="hostRedirectInput")
    def host_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectInput")
    def https_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRedirectInput")
    def path_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixRedirectInput")
    def prefix_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCodeInput")
    def redirect_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stripQueryInput")
    def strip_query_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRedirect")
    def host_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRedirect"))

    @host_redirect.setter
    def host_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "host_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirect")
    def https_redirect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirect"))

    @https_redirect.setter
    def https_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "https_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="pathRedirect")
    def path_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathRedirect"))

    @path_redirect.setter
    def path_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "path_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="prefixRedirect")
    def prefix_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixRedirect"))

    @prefix_redirect.setter
    def prefix_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "prefix_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCode")
    def redirect_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectResponseCode"))

    @redirect_response_code.setter
    def redirect_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "redirect_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="stripQuery")
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripQuery"))

    @strip_query.setter
    def strip_query(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "strip_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripQuery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRules",
    jsii_struct_bases=[],
    name_mapping={
        "priority": "priority",
        "header_action": "headerAction",
        "match_rules": "matchRules",
        "route_action": "routeAction",
        "service": "service",
        "url_redirect": "urlRedirect",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRules:
    def __init__(
        self,
        *,
        priority: jsii.Number,
        header_action: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction", typing.Dict[str, typing.Any]]] = None,
        match_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules", typing.Dict[str, typing.Any]]]]] = None,
        route_action: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction", typing.Dict[str, typing.Any]]] = None,
        service: typing.Optional[builtins.str] = None,
        url_redirect: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param priority: For routeRules within a given pathMatcher, priority determines the order in which load balancer will interpret routeRules. RouteRules are evaluated in order of priority, from the lowest to highest number. The priority of a rule decreases as its number increases (1, 2, 3, N+1). The first rule that matches the request is applied. You cannot configure two or more routeRules with the same priority. Priority for each rule must be set to a number between 0 and 2147483647 inclusive. Priority numbers can have gaps, which enable you to add or remove rules in the future without affecting the rest of the rules. For example, 1, 2, 3, 4, 5, 9, 12, 16 is a valid series of priority numbers to which you could add rules numbered from 6 to 8, 10 to 11, and 13 to 15 in the future without any impact on existing rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#priority GoogleComputeRegionUrlMap#priority}
        :param header_action: header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_action GoogleComputeRegionUrlMap#header_action}
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#match_rules GoogleComputeRegionUrlMap#match_rules}
        :param route_action: route_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#route_action GoogleComputeRegionUrlMap#route_action}
        :param service: The region backend service resource to which traffic is directed if this rule is matched. If routeAction is additionally specified, advanced routing actions like URL Rewrites, etc. take effect prior to sending the request to the backend. However, if service is specified, routeAction cannot contain any weightedBackendService s. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of urlRedirect, service or routeAction.weightedBackendService must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#service GoogleComputeRegionUrlMap#service}
        :param url_redirect: url_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_redirect GoogleComputeRegionUrlMap#url_redirect}
        '''
        if isinstance(header_action, dict):
            header_action = GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction(**header_action)
        if isinstance(route_action, dict):
            route_action = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction(**route_action)
        if isinstance(url_redirect, dict):
            url_redirect = GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect(**url_redirect)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRules.__init__)
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument header_action", value=header_action, expected_type=type_hints["header_action"])
            check_type(argname="argument match_rules", value=match_rules, expected_type=type_hints["match_rules"])
            check_type(argname="argument route_action", value=route_action, expected_type=type_hints["route_action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument url_redirect", value=url_redirect, expected_type=type_hints["url_redirect"])
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
        }
        if header_action is not None:
            self._values["header_action"] = header_action
        if match_rules is not None:
            self._values["match_rules"] = match_rules
        if route_action is not None:
            self._values["route_action"] = route_action
        if service is not None:
            self._values["service"] = service
        if url_redirect is not None:
            self._values["url_redirect"] = url_redirect

    @builtins.property
    def priority(self) -> jsii.Number:
        '''For routeRules within a given pathMatcher, priority determines the order in which load balancer will interpret routeRules.

        RouteRules are evaluated
        in order of priority, from the lowest to highest number. The priority of
        a rule decreases as its number increases (1, 2, 3, N+1). The first rule
        that matches the request is applied.

        You cannot configure two or more routeRules with the same priority.
        Priority for each rule must be set to a number between 0 and
        2147483647 inclusive.

        Priority numbers can have gaps, which enable you to add or remove rules
        in the future without affecting the rest of the rules. For example,
        1, 2, 3, 4, 5, 9, 12, 16 is a valid series of priority numbers to which
        you could add rules numbered from 6 to 8, 10 to 11, and 13 to 15 in the
        future without any impact on existing rules.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#priority GoogleComputeRegionUrlMap#priority}
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def header_action(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction"]:
        '''header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_action GoogleComputeRegionUrlMap#header_action}
        '''
        result = self._values.get("header_action")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction"], result)

    @builtins.property
    def match_rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules"]]]:
        '''match_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#match_rules GoogleComputeRegionUrlMap#match_rules}
        '''
        result = self._values.get("match_rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules"]]], result)

    @builtins.property
    def route_action(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction"]:
        '''route_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#route_action GoogleComputeRegionUrlMap#route_action}
        '''
        result = self._values.get("route_action")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction"], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''The region backend service resource to which traffic is directed if this rule is matched.

        If routeAction is additionally specified,
        advanced routing actions like URL Rewrites, etc. take effect prior to sending
        the request to the backend. However, if service is specified, routeAction cannot
        contain any weightedBackendService s. Conversely, if routeAction specifies any
        weightedBackendServices, service must not be specified. Only one of urlRedirect,
        service or routeAction.weightedBackendService must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#service GoogleComputeRegionUrlMap#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_redirect(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect"]:
        '''url_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_redirect GoogleComputeRegionUrlMap#url_redirect}
        '''
        result = self._values.get("url_redirect")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction",
    jsii_struct_bases=[],
    name_mapping={
        "request_headers_to_add": "requestHeadersToAdd",
        "request_headers_to_remove": "requestHeadersToRemove",
        "response_headers_to_add": "responseHeadersToAdd",
        "response_headers_to_remove": "responseHeadersToRemove",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction:
    def __init__(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction.__init__)
            check_type(argname="argument request_headers_to_add", value=request_headers_to_add, expected_type=type_hints["request_headers_to_add"])
            check_type(argname="argument request_headers_to_remove", value=request_headers_to_remove, expected_type=type_hints["request_headers_to_remove"])
            check_type(argname="argument response_headers_to_add", value=response_headers_to_add, expected_type=type_hints["response_headers_to_add"])
            check_type(argname="argument response_headers_to_remove", value=response_headers_to_remove, expected_type=type_hints["response_headers_to_remove"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request_headers_to_add is not None:
            self._values["request_headers_to_add"] = request_headers_to_add
        if request_headers_to_remove is not None:
            self._values["request_headers_to_remove"] = request_headers_to_remove
        if response_headers_to_add is not None:
            self._values["response_headers_to_add"] = response_headers_to_add
        if response_headers_to_remove is not None:
            self._values["response_headers_to_remove"] = response_headers_to_remove

    @builtins.property
    def request_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd"]]]:
        '''request_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        '''
        result = self._values.get("request_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd"]]], result)

    @builtins.property
    def request_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        '''
        result = self._values.get("request_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def response_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd"]]]:
        '''response_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        '''
        result = self._values.get("response_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd"]]], result)

    @builtins.property
    def response_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the response prior to sending the response back to the client.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        result = self._values.get("response_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestHeadersToAdd")
    def put_request_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference.put_request_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeadersToAdd", [value]))

    @jsii.member(jsii_name="putResponseHeadersToAdd")
    def put_response_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference.put_response_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeadersToAdd", [value]))

    @jsii.member(jsii_name="resetRequestHeadersToAdd")
    def reset_request_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToAdd", []))

    @jsii.member(jsii_name="resetRequestHeadersToRemove")
    def reset_request_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToRemove", []))

    @jsii.member(jsii_name="resetResponseHeadersToAdd")
    def reset_response_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToAdd", []))

    @jsii.member(jsii_name="resetResponseHeadersToRemove")
    def reset_response_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToRemove", []))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAdd")
    def request_headers_to_add(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList", jsii.get(self, "requestHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAdd")
    def response_headers_to_add(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList", jsii.get(self, "responseHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAddInput")
    def request_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd"]]], jsii.get(self, "requestHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemoveInput")
    def request_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAddInput")
    def response_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd"]]], jsii.get(self, "responseHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemoveInput")
    def response_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemove")
    def request_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestHeadersToRemove"))

    @request_headers_to_remove.setter
    def request_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference, "request_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemove")
    def response_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseHeadersToRemove"))

    @response_headers_to_remove.setter
    def response_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference, "response_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules",
    jsii_struct_bases=[],
    name_mapping={
        "full_path_match": "fullPathMatch",
        "header_matches": "headerMatches",
        "ignore_case": "ignoreCase",
        "metadata_filters": "metadataFilters",
        "prefix_match": "prefixMatch",
        "query_parameter_matches": "queryParameterMatches",
        "regex_match": "regexMatch",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules:
    def __init__(
        self,
        *,
        full_path_match: typing.Optional[builtins.str] = None,
        header_matches: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches", typing.Dict[str, typing.Any]]]]] = None,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metadata_filters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters", typing.Dict[str, typing.Any]]]]] = None,
        prefix_match: typing.Optional[builtins.str] = None,
        query_parameter_matches: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches", typing.Dict[str, typing.Any]]]]] = None,
        regex_match: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param full_path_match: For satisfying the matchRule condition, the path of the request must exactly match the value specified in fullPathMatch after removing any query parameters and anchor that may be part of the original URL. FullPathMatch must be between 1 and 1024 characters. Only one of prefixMatch, fullPathMatch or regexMatch must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#full_path_match GoogleComputeRegionUrlMap#full_path_match}
        :param header_matches: header_matches block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_matches GoogleComputeRegionUrlMap#header_matches}
        :param ignore_case: Specifies that prefixMatch and fullPathMatch matches are case sensitive. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#ignore_case GoogleComputeRegionUrlMap#ignore_case}
        :param metadata_filters: metadata_filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#metadata_filters GoogleComputeRegionUrlMap#metadata_filters}
        :param prefix_match: For satisfying the matchRule condition, the request's path must begin with the specified prefixMatch. prefixMatch must begin with a /. The value must be between 1 and 1024 characters. Only one of prefixMatch, fullPathMatch or regexMatch must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_match GoogleComputeRegionUrlMap#prefix_match}
        :param query_parameter_matches: query_parameter_matches block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#query_parameter_matches GoogleComputeRegionUrlMap#query_parameter_matches}
        :param regex_match: For satisfying the matchRule condition, the path of the request must satisfy the regular expression specified in regexMatch after removing any query parameters and anchor supplied with the original URL. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript Only one of prefixMatch, fullPathMatch or regexMatch must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#regex_match GoogleComputeRegionUrlMap#regex_match}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules.__init__)
            check_type(argname="argument full_path_match", value=full_path_match, expected_type=type_hints["full_path_match"])
            check_type(argname="argument header_matches", value=header_matches, expected_type=type_hints["header_matches"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument metadata_filters", value=metadata_filters, expected_type=type_hints["metadata_filters"])
            check_type(argname="argument prefix_match", value=prefix_match, expected_type=type_hints["prefix_match"])
            check_type(argname="argument query_parameter_matches", value=query_parameter_matches, expected_type=type_hints["query_parameter_matches"])
            check_type(argname="argument regex_match", value=regex_match, expected_type=type_hints["regex_match"])
        self._values: typing.Dict[str, typing.Any] = {}
        if full_path_match is not None:
            self._values["full_path_match"] = full_path_match
        if header_matches is not None:
            self._values["header_matches"] = header_matches
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if metadata_filters is not None:
            self._values["metadata_filters"] = metadata_filters
        if prefix_match is not None:
            self._values["prefix_match"] = prefix_match
        if query_parameter_matches is not None:
            self._values["query_parameter_matches"] = query_parameter_matches
        if regex_match is not None:
            self._values["regex_match"] = regex_match

    @builtins.property
    def full_path_match(self) -> typing.Optional[builtins.str]:
        '''For satisfying the matchRule condition, the path of the request must exactly match the value specified in fullPathMatch after removing any query parameters and anchor that may be part of the original URL.

        FullPathMatch must be between 1
        and 1024 characters. Only one of prefixMatch, fullPathMatch or regexMatch must
        be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#full_path_match GoogleComputeRegionUrlMap#full_path_match}
        '''
        result = self._values.get("full_path_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def header_matches(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches"]]]:
        '''header_matches block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_matches GoogleComputeRegionUrlMap#header_matches}
        '''
        result = self._values.get("header_matches")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches"]]], result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies that prefixMatch and fullPathMatch matches are case sensitive. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#ignore_case GoogleComputeRegionUrlMap#ignore_case}
        '''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metadata_filters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters"]]]:
        '''metadata_filters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#metadata_filters GoogleComputeRegionUrlMap#metadata_filters}
        '''
        result = self._values.get("metadata_filters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters"]]], result)

    @builtins.property
    def prefix_match(self) -> typing.Optional[builtins.str]:
        '''For satisfying the matchRule condition, the request's path must begin with the specified prefixMatch.

        prefixMatch must begin with a /. The value must be
        between 1 and 1024 characters. Only one of prefixMatch, fullPathMatch or
        regexMatch must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_match GoogleComputeRegionUrlMap#prefix_match}
        '''
        result = self._values.get("prefix_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_parameter_matches(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches"]]]:
        '''query_parameter_matches block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#query_parameter_matches GoogleComputeRegionUrlMap#query_parameter_matches}
        '''
        result = self._values.get("query_parameter_matches")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches"]]], result)

    @builtins.property
    def regex_match(self) -> typing.Optional[builtins.str]:
        '''For satisfying the matchRule condition, the path of the request must satisfy the regular expression specified in regexMatch after removing any query parameters and anchor supplied with the original URL.

        For regular expression grammar please
        see en.cppreference.com/w/cpp/regex/ecmascript  Only one of prefixMatch,
        fullPathMatch or regexMatch must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#regex_match GoogleComputeRegionUrlMap#regex_match}
        '''
        result = self._values.get("regex_match")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "exact_match": "exactMatch",
        "invert_match": "invertMatch",
        "prefix_match": "prefixMatch",
        "present_match": "presentMatch",
        "range_match": "rangeMatch",
        "regex_match": "regexMatch",
        "suffix_match": "suffixMatch",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        exact_match: typing.Optional[builtins.str] = None,
        invert_match: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        prefix_match: typing.Optional[builtins.str] = None,
        present_match: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        range_match: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch", typing.Dict[str, typing.Any]]] = None,
        regex_match: typing.Optional[builtins.str] = None,
        suffix_match: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param header_name: The name of the HTTP header to match. For matching against the HTTP request's authority, use a headerMatch with the header name ":authority". For matching a request's method, use the headerName ":method". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        :param exact_match: The value should exactly match contents of exactMatch. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#exact_match GoogleComputeRegionUrlMap#exact_match}
        :param invert_match: If set to false, the headerMatch is considered a match if the match criteria above are met. If set to true, the headerMatch is considered a match if the match criteria above are NOT met. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#invert_match GoogleComputeRegionUrlMap#invert_match}
        :param prefix_match: The value of the header must start with the contents of prefixMatch. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_match GoogleComputeRegionUrlMap#prefix_match}
        :param present_match: A header with the contents of headerName must exist. The match takes place whether or not the request's header has a value or not. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#present_match GoogleComputeRegionUrlMap#present_match}
        :param range_match: range_match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#range_match GoogleComputeRegionUrlMap#range_match}
        :param regex_match: The value of the header must match the regular expression specified in regexMatch. For regular expression grammar, please see: en.cppreference.com/w/cpp/regex/ecmascript For matching against a port specified in the HTTP request, use a headerMatch with headerName set to PORT and a regular expression that satisfies the RFC2616 Host header's port specifier. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#regex_match GoogleComputeRegionUrlMap#regex_match}
        :param suffix_match: The value of the header must end with the contents of suffixMatch. Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#suffix_match GoogleComputeRegionUrlMap#suffix_match}
        '''
        if isinstance(range_match, dict):
            range_match = GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch(**range_match)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument exact_match", value=exact_match, expected_type=type_hints["exact_match"])
            check_type(argname="argument invert_match", value=invert_match, expected_type=type_hints["invert_match"])
            check_type(argname="argument prefix_match", value=prefix_match, expected_type=type_hints["prefix_match"])
            check_type(argname="argument present_match", value=present_match, expected_type=type_hints["present_match"])
            check_type(argname="argument range_match", value=range_match, expected_type=type_hints["range_match"])
            check_type(argname="argument regex_match", value=regex_match, expected_type=type_hints["regex_match"])
            check_type(argname="argument suffix_match", value=suffix_match, expected_type=type_hints["suffix_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
        }
        if exact_match is not None:
            self._values["exact_match"] = exact_match
        if invert_match is not None:
            self._values["invert_match"] = invert_match
        if prefix_match is not None:
            self._values["prefix_match"] = prefix_match
        if present_match is not None:
            self._values["present_match"] = present_match
        if range_match is not None:
            self._values["range_match"] = range_match
        if regex_match is not None:
            self._values["regex_match"] = regex_match
        if suffix_match is not None:
            self._values["suffix_match"] = suffix_match

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the HTTP header to match.

        For matching against the HTTP request's
        authority, use a headerMatch with the header name ":authority". For matching a
        request's method, use the headerName ":method".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exact_match(self) -> typing.Optional[builtins.str]:
        '''The value should exactly match contents of exactMatch.

        Only one of exactMatch,
        prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#exact_match GoogleComputeRegionUrlMap#exact_match}
        '''
        result = self._values.get("exact_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invert_match(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to false, the headerMatch is considered a match if the match criteria above are met.

        If set to true, the headerMatch is considered a match if the
        match criteria above are NOT met. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#invert_match GoogleComputeRegionUrlMap#invert_match}
        '''
        result = self._values.get("invert_match")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def prefix_match(self) -> typing.Optional[builtins.str]:
        '''The value of the header must start with the contents of prefixMatch.

        Only one of
        exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch
        must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_match GoogleComputeRegionUrlMap#prefix_match}
        '''
        result = self._values.get("prefix_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def present_match(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A header with the contents of headerName must exist.

        The match takes place
        whether or not the request's header has a value or not. Only one of exactMatch,
        prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#present_match GoogleComputeRegionUrlMap#present_match}
        '''
        result = self._values.get("present_match")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def range_match(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch"]:
        '''range_match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#range_match GoogleComputeRegionUrlMap#range_match}
        '''
        result = self._values.get("range_match")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch"], result)

    @builtins.property
    def regex_match(self) -> typing.Optional[builtins.str]:
        '''The value of the header must match the regular expression specified in regexMatch.

        For regular expression grammar, please see:
        en.cppreference.com/w/cpp/regex/ecmascript  For matching against a port
        specified in the HTTP request, use a headerMatch with headerName set to PORT and
        a regular expression that satisfies the RFC2616 Host header's port specifier.
        Only one of exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or
        rangeMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#regex_match GoogleComputeRegionUrlMap#regex_match}
        '''
        result = self._values.get("regex_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix_match(self) -> typing.Optional[builtins.str]:
        '''The value of the header must end with the contents of suffixMatch.

        Only one of
        exactMatch, prefixMatch, suffixMatch, regexMatch, presentMatch or rangeMatch
        must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#suffix_match GoogleComputeRegionUrlMap#suffix_match}
        '''
        result = self._values.get("suffix_match")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRangeMatch")
    def put_range_match(
        self,
        *,
        range_end: jsii.Number,
        range_start: jsii.Number,
    ) -> None:
        '''
        :param range_end: The end of the range (exclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#range_end GoogleComputeRegionUrlMap#range_end}
        :param range_start: The start of the range (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#range_start GoogleComputeRegionUrlMap#range_start}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch(
            range_end=range_end, range_start=range_start
        )

        return typing.cast(None, jsii.invoke(self, "putRangeMatch", [value]))

    @jsii.member(jsii_name="resetExactMatch")
    def reset_exact_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExactMatch", []))

    @jsii.member(jsii_name="resetInvertMatch")
    def reset_invert_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvertMatch", []))

    @jsii.member(jsii_name="resetPrefixMatch")
    def reset_prefix_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixMatch", []))

    @jsii.member(jsii_name="resetPresentMatch")
    def reset_present_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresentMatch", []))

    @jsii.member(jsii_name="resetRangeMatch")
    def reset_range_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeMatch", []))

    @jsii.member(jsii_name="resetRegexMatch")
    def reset_regex_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexMatch", []))

    @jsii.member(jsii_name="resetSuffixMatch")
    def reset_suffix_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffixMatch", []))

    @builtins.property
    @jsii.member(jsii_name="rangeMatch")
    def range_match(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference", jsii.get(self, "rangeMatch"))

    @builtins.property
    @jsii.member(jsii_name="exactMatchInput")
    def exact_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="invertMatchInput")
    def invert_match_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "invertMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixMatchInput")
    def prefix_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="presentMatchInput")
    def present_match_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "presentMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeMatchInput")
    def range_match_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch"], jsii.get(self, "rangeMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="regexMatchInput")
    def regex_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixMatchInput")
    def suffix_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="exactMatch")
    def exact_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exactMatch"))

    @exact_match.setter
    def exact_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "exact_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exactMatch", value)

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="invertMatch")
    def invert_match(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "invertMatch"))

    @invert_match.setter
    def invert_match(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "invert_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invertMatch", value)

    @builtins.property
    @jsii.member(jsii_name="prefixMatch")
    def prefix_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixMatch"))

    @prefix_match.setter
    def prefix_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "prefix_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixMatch", value)

    @builtins.property
    @jsii.member(jsii_name="presentMatch")
    def present_match(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "presentMatch"))

    @present_match.setter
    def present_match(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "present_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presentMatch", value)

    @builtins.property
    @jsii.member(jsii_name="regexMatch")
    def regex_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexMatch"))

    @regex_match.setter
    def regex_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "regex_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexMatch", value)

    @builtins.property
    @jsii.member(jsii_name="suffixMatch")
    def suffix_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffixMatch"))

    @suffix_match.setter
    def suffix_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "suffix_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffixMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch",
    jsii_struct_bases=[],
    name_mapping={"range_end": "rangeEnd", "range_start": "rangeStart"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch:
    def __init__(self, *, range_end: jsii.Number, range_start: jsii.Number) -> None:
        '''
        :param range_end: The end of the range (exclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#range_end GoogleComputeRegionUrlMap#range_end}
        :param range_start: The start of the range (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#range_start GoogleComputeRegionUrlMap#range_start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch.__init__)
            check_type(argname="argument range_end", value=range_end, expected_type=type_hints["range_end"])
            check_type(argname="argument range_start", value=range_start, expected_type=type_hints["range_start"])
        self._values: typing.Dict[str, typing.Any] = {
            "range_end": range_end,
            "range_start": range_start,
        }

    @builtins.property
    def range_end(self) -> jsii.Number:
        '''The end of the range (exclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#range_end GoogleComputeRegionUrlMap#range_end}
        '''
        result = self._values.get("range_end")
        assert result is not None, "Required property 'range_end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def range_start(self) -> jsii.Number:
        '''The start of the range (inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#range_start GoogleComputeRegionUrlMap#range_start}
        '''
        result = self._values.get("range_start")
        assert result is not None, "Required property 'range_start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="rangeEndInput")
    def range_end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rangeEndInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeStartInput")
    def range_start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rangeStartInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeEnd")
    def range_end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rangeEnd"))

    @range_end.setter
    def range_end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference, "range_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeEnd", value)

    @builtins.property
    @jsii.member(jsii_name="rangeStart")
    def range_start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rangeStart"))

    @range_start.setter
    def range_start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference, "range_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeStart", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters",
    jsii_struct_bases=[],
    name_mapping={
        "filter_labels": "filterLabels",
        "filter_match_criteria": "filterMatchCriteria",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters:
    def __init__(
        self,
        *,
        filter_labels: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels", typing.Dict[str, typing.Any]]]],
        filter_match_criteria: builtins.str,
    ) -> None:
        '''
        :param filter_labels: filter_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#filter_labels GoogleComputeRegionUrlMap#filter_labels}
        :param filter_match_criteria: Specifies how individual filterLabel matches within the list of filterLabels contribute towards the overall metadataFilter match. Supported values are:. MATCH_ANY: At least one of the filterLabels must have a matching label in the provided metadata. MATCH_ALL: All filterLabels must have matching labels in the provided metadata. Possible values: ["MATCH_ALL", "MATCH_ANY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#filter_match_criteria GoogleComputeRegionUrlMap#filter_match_criteria}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters.__init__)
            check_type(argname="argument filter_labels", value=filter_labels, expected_type=type_hints["filter_labels"])
            check_type(argname="argument filter_match_criteria", value=filter_match_criteria, expected_type=type_hints["filter_match_criteria"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter_labels": filter_labels,
            "filter_match_criteria": filter_match_criteria,
        }

    @builtins.property
    def filter_labels(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels"]]:
        '''filter_labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#filter_labels GoogleComputeRegionUrlMap#filter_labels}
        '''
        result = self._values.get("filter_labels")
        assert result is not None, "Required property 'filter_labels' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels"]], result)

    @builtins.property
    def filter_match_criteria(self) -> builtins.str:
        '''Specifies how individual filterLabel matches within the list of filterLabels contribute towards the overall metadataFilter match. Supported values are:.

        MATCH_ANY: At least one of the filterLabels must have a matching label in the
        provided metadata.
        MATCH_ALL: All filterLabels must have matching labels in
        the provided metadata. Possible values: ["MATCH_ALL", "MATCH_ANY"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#filter_match_criteria GoogleComputeRegionUrlMap#filter_match_criteria}
        '''
        result = self._values.get("filter_match_criteria")
        assert result is not None, "Required property 'filter_match_criteria' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Name of metadata label. The name can have a maximum length of 1024 characters and must be at least 1 character long. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        :param value: The value of the label must match the specified value. value can have a maximum length of 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#value GoogleComputeRegionUrlMap#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of metadata label.

        The name can have a maximum length of 1024 characters
        and must be at least 1 character long.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the label must match the specified value. value can have a maximum length of 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#value GoogleComputeRegionUrlMap#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFilterLabels")
    def put_filter_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference.put_filter_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilterLabels", [value]))

    @builtins.property
    @jsii.member(jsii_name="filterLabels")
    def filter_labels(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList, jsii.get(self, "filterLabels"))

    @builtins.property
    @jsii.member(jsii_name="filterLabelsInput")
    def filter_labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels]]], jsii.get(self, "filterLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="filterMatchCriteriaInput")
    def filter_match_criteria_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterMatchCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="filterMatchCriteria")
    def filter_match_criteria(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterMatchCriteria"))

    @filter_match_criteria.setter
    def filter_match_criteria(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference, "filter_match_criteria").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterMatchCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaderMatches")
    def put_header_matches(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference.put_header_matches)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaderMatches", [value]))

    @jsii.member(jsii_name="putMetadataFilters")
    def put_metadata_filters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference.put_metadata_filters)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetadataFilters", [value]))

    @jsii.member(jsii_name="putQueryParameterMatches")
    def put_query_parameter_matches(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference.put_query_parameter_matches)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryParameterMatches", [value]))

    @jsii.member(jsii_name="resetFullPathMatch")
    def reset_full_path_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullPathMatch", []))

    @jsii.member(jsii_name="resetHeaderMatches")
    def reset_header_matches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderMatches", []))

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetMetadataFilters")
    def reset_metadata_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataFilters", []))

    @jsii.member(jsii_name="resetPrefixMatch")
    def reset_prefix_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixMatch", []))

    @jsii.member(jsii_name="resetQueryParameterMatches")
    def reset_query_parameter_matches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryParameterMatches", []))

    @jsii.member(jsii_name="resetRegexMatch")
    def reset_regex_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexMatch", []))

    @builtins.property
    @jsii.member(jsii_name="headerMatches")
    def header_matches(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList, jsii.get(self, "headerMatches"))

    @builtins.property
    @jsii.member(jsii_name="metadataFilters")
    def metadata_filters(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList, jsii.get(self, "metadataFilters"))

    @builtins.property
    @jsii.member(jsii_name="queryParameterMatches")
    def query_parameter_matches(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList", jsii.get(self, "queryParameterMatches"))

    @builtins.property
    @jsii.member(jsii_name="fullPathMatchInput")
    def full_path_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fullPathMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="headerMatchesInput")
    def header_matches_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches]]], jsii.get(self, "headerMatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataFiltersInput")
    def metadata_filters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters]]], jsii.get(self, "metadataFiltersInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixMatchInput")
    def prefix_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParameterMatchesInput")
    def query_parameter_matches_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches"]]], jsii.get(self, "queryParameterMatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="regexMatchInput")
    def regex_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="fullPathMatch")
    def full_path_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullPathMatch"))

    @full_path_match.setter
    def full_path_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "full_path_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullPathMatch", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="prefixMatch")
    def prefix_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixMatch"))

    @prefix_match.setter
    def prefix_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "prefix_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixMatch", value)

    @builtins.property
    @jsii.member(jsii_name="regexMatch")
    def regex_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexMatch"))

    @regex_match.setter
    def regex_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "regex_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "exact_match": "exactMatch",
        "present_match": "presentMatch",
        "regex_match": "regexMatch",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches:
    def __init__(
        self,
        *,
        name: builtins.str,
        exact_match: typing.Optional[builtins.str] = None,
        present_match: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        regex_match: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the query parameter to match. The query parameter must exist in the request, in the absence of which the request match fails. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        :param exact_match: The queryParameterMatch matches if the value of the parameter exactly matches the contents of exactMatch. Only one of presentMatch, exactMatch and regexMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#exact_match GoogleComputeRegionUrlMap#exact_match}
        :param present_match: Specifies that the queryParameterMatch matches if the request contains the query parameter, irrespective of whether the parameter has a value or not. Only one of presentMatch, exactMatch and regexMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#present_match GoogleComputeRegionUrlMap#present_match}
        :param regex_match: The queryParameterMatch matches if the value of the parameter matches the regular expression specified by regexMatch. For the regular expression grammar, please see en.cppreference.com/w/cpp/regex/ecmascript Only one of presentMatch, exactMatch and regexMatch must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#regex_match GoogleComputeRegionUrlMap#regex_match}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument exact_match", value=exact_match, expected_type=type_hints["exact_match"])
            check_type(argname="argument present_match", value=present_match, expected_type=type_hints["present_match"])
            check_type(argname="argument regex_match", value=regex_match, expected_type=type_hints["regex_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if exact_match is not None:
            self._values["exact_match"] = exact_match
        if present_match is not None:
            self._values["present_match"] = present_match
        if regex_match is not None:
            self._values["regex_match"] = regex_match

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the query parameter to match.

        The query parameter must exist in the
        request, in the absence of which the request match fails.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#name GoogleComputeRegionUrlMap#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exact_match(self) -> typing.Optional[builtins.str]:
        '''The queryParameterMatch matches if the value of the parameter exactly matches the contents of exactMatch.

        Only one of presentMatch, exactMatch and regexMatch
        must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#exact_match GoogleComputeRegionUrlMap#exact_match}
        '''
        result = self._values.get("exact_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def present_match(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies that the queryParameterMatch matches if the request contains the query parameter, irrespective of whether the parameter has a value or not.

        Only one of
        presentMatch, exactMatch and regexMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#present_match GoogleComputeRegionUrlMap#present_match}
        '''
        result = self._values.get("present_match")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def regex_match(self) -> typing.Optional[builtins.str]:
        '''The queryParameterMatch matches if the value of the parameter matches the regular expression specified by regexMatch.

        For the regular expression grammar,
        please see en.cppreference.com/w/cpp/regex/ecmascript  Only one of presentMatch,
        exactMatch and regexMatch must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#regex_match GoogleComputeRegionUrlMap#regex_match}
        '''
        result = self._values.get("regex_match")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExactMatch")
    def reset_exact_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExactMatch", []))

    @jsii.member(jsii_name="resetPresentMatch")
    def reset_present_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPresentMatch", []))

    @jsii.member(jsii_name="resetRegexMatch")
    def reset_regex_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexMatch", []))

    @builtins.property
    @jsii.member(jsii_name="exactMatchInput")
    def exact_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="presentMatchInput")
    def present_match_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "presentMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="regexMatchInput")
    def regex_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="exactMatch")
    def exact_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exactMatch"))

    @exact_match.setter
    def exact_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "exact_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exactMatch", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="presentMatch")
    def present_match(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "presentMatch"))

    @present_match.setter
    def present_match(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "present_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presentMatch", value)

    @builtins.property
    @jsii.member(jsii_name="regexMatch")
    def regex_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexMatch"))

    @regex_match.setter
    def regex_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "regex_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaderAction")
    def put_header_action(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction(
            request_headers_to_add=request_headers_to_add,
            request_headers_to_remove=request_headers_to_remove,
            response_headers_to_add=response_headers_to_add,
            response_headers_to_remove=response_headers_to_remove,
        )

        return typing.cast(None, jsii.invoke(self, "putHeaderAction", [value]))

    @jsii.member(jsii_name="putMatchRules")
    def put_match_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference.put_match_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchRules", [value]))

    @jsii.member(jsii_name="putRouteAction")
    def put_route_action(
        self,
        *,
        cors_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy", typing.Dict[str, typing.Any]]] = None,
        fault_injection_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy", typing.Dict[str, typing.Any]]] = None,
        request_mirror_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout", typing.Dict[str, typing.Any]]] = None,
        url_rewrite: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite", typing.Dict[str, typing.Any]]] = None,
        weighted_backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cors_policy: cors_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#cors_policy GoogleComputeRegionUrlMap#cors_policy}
        :param fault_injection_policy: fault_injection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fault_injection_policy GoogleComputeRegionUrlMap#fault_injection_policy}
        :param request_mirror_policy: request_mirror_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_mirror_policy GoogleComputeRegionUrlMap#request_mirror_policy}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_policy GoogleComputeRegionUrlMap#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeout GoogleComputeRegionUrlMap#timeout}
        :param url_rewrite: url_rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_rewrite GoogleComputeRegionUrlMap#url_rewrite}
        :param weighted_backend_services: weighted_backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weighted_backend_services GoogleComputeRegionUrlMap#weighted_backend_services}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction(
            cors_policy=cors_policy,
            fault_injection_policy=fault_injection_policy,
            request_mirror_policy=request_mirror_policy,
            retry_policy=retry_policy,
            timeout=timeout,
            url_rewrite=url_rewrite,
            weighted_backend_services=weighted_backend_services,
        )

        return typing.cast(None, jsii.invoke(self, "putRouteAction", [value]))

    @jsii.member(jsii_name="putUrlRedirect")
    def put_url_redirect(
        self,
        *,
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
        strip_query: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect(
            host_redirect=host_redirect,
            https_redirect=https_redirect,
            path_redirect=path_redirect,
            prefix_redirect=prefix_redirect,
            redirect_response_code=redirect_response_code,
            strip_query=strip_query,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRedirect", [value]))

    @jsii.member(jsii_name="resetHeaderAction")
    def reset_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderAction", []))

    @jsii.member(jsii_name="resetMatchRules")
    def reset_match_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchRules", []))

    @jsii.member(jsii_name="resetRouteAction")
    def reset_route_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteAction", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetUrlRedirect")
    def reset_url_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRedirect", []))

    @builtins.property
    @jsii.member(jsii_name="headerAction")
    def header_action(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference, jsii.get(self, "headerAction"))

    @builtins.property
    @jsii.member(jsii_name="matchRules")
    def match_rules(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList, jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="routeAction")
    def route_action(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference", jsii.get(self, "routeAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirect")
    def url_redirect(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference", jsii.get(self, "urlRedirect"))

    @builtins.property
    @jsii.member(jsii_name="headerActionInput")
    def header_action_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction], jsii.get(self, "headerActionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules]]], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="routeActionInput")
    def route_action_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction"], jsii.get(self, "routeActionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectInput")
    def url_redirect_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect"], jsii.get(self, "urlRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction",
    jsii_struct_bases=[],
    name_mapping={
        "cors_policy": "corsPolicy",
        "fault_injection_policy": "faultInjectionPolicy",
        "request_mirror_policy": "requestMirrorPolicy",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
        "url_rewrite": "urlRewrite",
        "weighted_backend_services": "weightedBackendServices",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction:
    def __init__(
        self,
        *,
        cors_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy", typing.Dict[str, typing.Any]]] = None,
        fault_injection_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy", typing.Dict[str, typing.Any]]] = None,
        request_mirror_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy", typing.Dict[str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout", typing.Dict[str, typing.Any]]] = None,
        url_rewrite: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite", typing.Dict[str, typing.Any]]] = None,
        weighted_backend_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cors_policy: cors_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#cors_policy GoogleComputeRegionUrlMap#cors_policy}
        :param fault_injection_policy: fault_injection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fault_injection_policy GoogleComputeRegionUrlMap#fault_injection_policy}
        :param request_mirror_policy: request_mirror_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_mirror_policy GoogleComputeRegionUrlMap#request_mirror_policy}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_policy GoogleComputeRegionUrlMap#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeout GoogleComputeRegionUrlMap#timeout}
        :param url_rewrite: url_rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_rewrite GoogleComputeRegionUrlMap#url_rewrite}
        :param weighted_backend_services: weighted_backend_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weighted_backend_services GoogleComputeRegionUrlMap#weighted_backend_services}
        '''
        if isinstance(cors_policy, dict):
            cors_policy = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy(**cors_policy)
        if isinstance(fault_injection_policy, dict):
            fault_injection_policy = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy(**fault_injection_policy)
        if isinstance(request_mirror_policy, dict):
            request_mirror_policy = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy(**request_mirror_policy)
        if isinstance(retry_policy, dict):
            retry_policy = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout(**timeout)
        if isinstance(url_rewrite, dict):
            url_rewrite = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite(**url_rewrite)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction.__init__)
            check_type(argname="argument cors_policy", value=cors_policy, expected_type=type_hints["cors_policy"])
            check_type(argname="argument fault_injection_policy", value=fault_injection_policy, expected_type=type_hints["fault_injection_policy"])
            check_type(argname="argument request_mirror_policy", value=request_mirror_policy, expected_type=type_hints["request_mirror_policy"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument url_rewrite", value=url_rewrite, expected_type=type_hints["url_rewrite"])
            check_type(argname="argument weighted_backend_services", value=weighted_backend_services, expected_type=type_hints["weighted_backend_services"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cors_policy is not None:
            self._values["cors_policy"] = cors_policy
        if fault_injection_policy is not None:
            self._values["fault_injection_policy"] = fault_injection_policy
        if request_mirror_policy is not None:
            self._values["request_mirror_policy"] = request_mirror_policy
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout
        if url_rewrite is not None:
            self._values["url_rewrite"] = url_rewrite
        if weighted_backend_services is not None:
            self._values["weighted_backend_services"] = weighted_backend_services

    @builtins.property
    def cors_policy(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy"]:
        '''cors_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#cors_policy GoogleComputeRegionUrlMap#cors_policy}
        '''
        result = self._values.get("cors_policy")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy"], result)

    @builtins.property
    def fault_injection_policy(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy"]:
        '''fault_injection_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fault_injection_policy GoogleComputeRegionUrlMap#fault_injection_policy}
        '''
        result = self._values.get("fault_injection_policy")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy"], result)

    @builtins.property
    def request_mirror_policy(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy"]:
        '''request_mirror_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_mirror_policy GoogleComputeRegionUrlMap#request_mirror_policy}
        '''
        result = self._values.get("request_mirror_policy")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy"], result)

    @builtins.property
    def retry_policy(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_policy GoogleComputeRegionUrlMap#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy"], result)

    @builtins.property
    def timeout(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#timeout GoogleComputeRegionUrlMap#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout"], result)

    @builtins.property
    def url_rewrite(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite"]:
        '''url_rewrite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#url_rewrite GoogleComputeRegionUrlMap#url_rewrite}
        '''
        result = self._values.get("url_rewrite")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite"], result)

    @builtins.property
    def weighted_backend_services(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices"]]]:
        '''weighted_backend_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weighted_backend_services GoogleComputeRegionUrlMap#weighted_backend_services}
        '''
        result = self._values.get("weighted_backend_services")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origin_regexes": "allowOriginRegexes",
        "allow_origins": "allowOrigins",
        "disabled": "disabled",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy:
    def __init__(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin_regexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allow_credentials: In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access- Control-Allow-Credentials header. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_credentials GoogleComputeRegionUrlMap#allow_credentials}
        :param allow_headers: Specifies the content for the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_headers GoogleComputeRegionUrlMap#allow_headers}
        :param allow_methods: Specifies the content for the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_methods GoogleComputeRegionUrlMap#allow_methods}
        :param allow_origin_regexes: Specifies the regular expression patterns that match allowed origins. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origin_regexes GoogleComputeRegionUrlMap#allow_origin_regexes}
        :param allow_origins: Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origins GoogleComputeRegionUrlMap#allow_origins}
        :param disabled: If true, specifies the CORS policy is disabled. which indicates that the CORS policy is in effect. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#disabled GoogleComputeRegionUrlMap#disabled}
        :param expose_headers: Specifies the content for the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#expose_headers GoogleComputeRegionUrlMap#expose_headers}
        :param max_age: Specifies how long the results of a preflight request can be cached. This translates to the content for the Access-Control-Max-Age header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#max_age GoogleComputeRegionUrlMap#max_age}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy.__init__)
            check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
            check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
            check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
            check_type(argname="argument allow_origin_regexes", value=allow_origin_regexes, expected_type=type_hints["allow_origin_regexes"])
            check_type(argname="argument allow_origins", value=allow_origins, expected_type=type_hints["allow_origins"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origin_regexes is not None:
            self._values["allow_origin_regexes"] = allow_origin_regexes
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if disabled is not None:
            self._values["disabled"] = disabled
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def allow_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''In response to a preflight request, setting this to true indicates that the actual request can include user credentials.

        This translates to the Access-
        Control-Allow-Credentials header. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_credentials GoogleComputeRegionUrlMap#allow_credentials}
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Allow-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_headers GoogleComputeRegionUrlMap#allow_headers}
        '''
        result = self._values.get("allow_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Allow-Methods header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_methods GoogleComputeRegionUrlMap#allow_methods}
        '''
        result = self._values.get("allow_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origin_regexes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the regular expression patterns that match allowed origins.

        For
        regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript
        An origin is allowed if it matches either allow_origins or allow_origin_regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origin_regexes GoogleComputeRegionUrlMap#allow_origin_regexes}
        '''
        result = self._values.get("allow_origin_regexes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of origins that will be allowed to do CORS requests.

        An
        origin is allowed if it matches either allow_origins or allow_origin_regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origins GoogleComputeRegionUrlMap#allow_origins}
        '''
        result = self._values.get("allow_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, specifies the CORS policy is disabled. which indicates that the CORS policy is in effect. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#disabled GoogleComputeRegionUrlMap#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the content for the Access-Control-Expose-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#expose_headers GoogleComputeRegionUrlMap#expose_headers}
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[jsii.Number]:
        '''Specifies how long the results of a preflight request can be cached.

        This
        translates to the content for the Access-Control-Max-Age header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#max_age GoogleComputeRegionUrlMap#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowCredentials")
    def reset_allow_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCredentials", []))

    @jsii.member(jsii_name="resetAllowHeaders")
    def reset_allow_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowHeaders", []))

    @jsii.member(jsii_name="resetAllowMethods")
    def reset_allow_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMethods", []))

    @jsii.member(jsii_name="resetAllowOriginRegexes")
    def reset_allow_origin_regexes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOriginRegexes", []))

    @jsii.member(jsii_name="resetAllowOrigins")
    def reset_allow_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOrigins", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetExposeHeaders")
    def reset_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeHeaders", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @builtins.property
    @jsii.member(jsii_name="allowCredentialsInput")
    def allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowHeadersInput")
    def allow_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMethodsInput")
    def allow_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginRegexesInput")
    def allow_origin_regexes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowOriginRegexesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginsInput")
    def allow_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeHeadersInput")
    def expose_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentials")
    def allow_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCredentials"))

    @allow_credentials.setter
    def allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="allowHeaders")
    def allow_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowHeaders"))

    @allow_headers.setter
    def allow_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowMethods")
    def allow_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowMethods"))

    @allow_methods.setter
    def allow_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowOriginRegexes")
    def allow_origin_regexes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowOriginRegexes"))

    @allow_origin_regexes.setter
    def allow_origin_regexes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_origin_regexes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOriginRegexes", value)

    @builtins.property
    @jsii.member(jsii_name="allowOrigins")
    def allow_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowOrigins"))

    @allow_origins.setter
    def allow_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "allow_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="exposeHeaders")
    def expose_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposeHeaders"))

    @expose_headers.setter
    def expose_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "expose_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy",
    jsii_struct_bases=[],
    name_mapping={"abort": "abort", "delay": "delay"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy:
    def __init__(
        self,
        *,
        abort: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort", typing.Dict[str, typing.Any]]] = None,
        delay: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abort: abort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#abort GoogleComputeRegionUrlMap#abort}
        :param delay: delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delay GoogleComputeRegionUrlMap#delay}
        '''
        if isinstance(abort, dict):
            abort = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort(**abort)
        if isinstance(delay, dict):
            delay = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay(**delay)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy.__init__)
            check_type(argname="argument abort", value=abort, expected_type=type_hints["abort"])
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
        self._values: typing.Dict[str, typing.Any] = {}
        if abort is not None:
            self._values["abort"] = abort
        if delay is not None:
            self._values["delay"] = delay

    @builtins.property
    def abort(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort"]:
        '''abort block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#abort GoogleComputeRegionUrlMap#abort}
        '''
        result = self._values.get("abort")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort"], result)

    @builtins.property
    def delay(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay"]:
        '''delay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delay GoogleComputeRegionUrlMap#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort",
    jsii_struct_bases=[],
    name_mapping={"http_status": "httpStatus", "percentage": "percentage"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort:
    def __init__(
        self,
        *,
        http_status: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_status: The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#http_status GoogleComputeRegionUrlMap#http_status}
        :param percentage: The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort.__init__)
            check_type(argname="argument http_status", value=http_status, expected_type=type_hints["http_status"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_status is not None:
            self._values["http_status"] = http_status
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def http_status(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#http_status GoogleComputeRegionUrlMap#http_status}
        '''
        result = self._values.get("http_status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection.

        The value must be between 0.0 and 100.0
        inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpStatus")
    def reset_http_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpStatus", []))

    @jsii.member(jsii_name="resetPercentage")
    def reset_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="httpStatusInput")
    def http_status_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="httpStatus")
    def http_status(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpStatus"))

    @http_status.setter
    def http_status(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference, "http_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpStatus", value)

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay",
    jsii_struct_bases=[],
    name_mapping={"fixed_delay": "fixedDelay", "percentage": "percentage"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay:
    def __init__(
        self,
        *,
        fixed_delay: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay", typing.Dict[str, typing.Any]]] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed_delay: fixed_delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fixed_delay GoogleComputeRegionUrlMap#fixed_delay}
        :param percentage: The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        if isinstance(fixed_delay, dict):
            fixed_delay = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay(**fixed_delay)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay.__init__)
            check_type(argname="argument fixed_delay", value=fixed_delay, expected_type=type_hints["fixed_delay"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fixed_delay is not None:
            self._values["fixed_delay"] = fixed_delay
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def fixed_delay(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay"]:
        '''fixed_delay block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fixed_delay GoogleComputeRegionUrlMap#fixed_delay}
        '''
        result = self._values.get("fixed_delay")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay"], result)

    @builtins.property
    def percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection.

        The value must be between 0.0 and
        100.0 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFixedDelay")
    def put_fixed_delay(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putFixedDelay", [value]))

    @jsii.member(jsii_name="resetFixedDelay")
    def reset_fixed_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedDelay", []))

    @jsii.member(jsii_name="resetPercentage")
    def reset_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="fixedDelay")
    def fixed_delay(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference, jsii.get(self, "fixedDelay"))

    @builtins.property
    @jsii.member(jsii_name="fixedDelayInput")
    def fixed_delay_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay], jsii.get(self, "fixedDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference, "percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAbort")
    def put_abort(
        self,
        *,
        http_status: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_status: The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#http_status GoogleComputeRegionUrlMap#http_status}
        :param percentage: The percentage of traffic (connections/operations/requests) which will be aborted as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort(
            http_status=http_status, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putAbort", [value]))

    @jsii.member(jsii_name="putDelay")
    def put_delay(
        self,
        *,
        fixed_delay: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay, typing.Dict[str, typing.Any]]] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fixed_delay: fixed_delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#fixed_delay GoogleComputeRegionUrlMap#fixed_delay}
        :param percentage: The percentage of traffic (connections/operations/requests) on which delay will be introduced as part of fault injection. The value must be between 0.0 and 100.0 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#percentage GoogleComputeRegionUrlMap#percentage}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay(
            fixed_delay=fixed_delay, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putDelay", [value]))

    @jsii.member(jsii_name="resetAbort")
    def reset_abort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbort", []))

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @builtins.property
    @jsii.member(jsii_name="abort")
    def abort(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference, jsii.get(self, "abort"))

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference, jsii.get(self, "delay"))

    @builtins.property
    @jsii.member(jsii_name="abortInput")
    def abort_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort], jsii.get(self, "abortInput"))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCorsPolicy")
    def put_cors_policy(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin_regexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allow_credentials: In response to a preflight request, setting this to true indicates that the actual request can include user credentials. This translates to the Access- Control-Allow-Credentials header. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_credentials GoogleComputeRegionUrlMap#allow_credentials}
        :param allow_headers: Specifies the content for the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_headers GoogleComputeRegionUrlMap#allow_headers}
        :param allow_methods: Specifies the content for the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_methods GoogleComputeRegionUrlMap#allow_methods}
        :param allow_origin_regexes: Specifies the regular expression patterns that match allowed origins. For regular expression grammar please see en.cppreference.com/w/cpp/regex/ecmascript An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origin_regexes GoogleComputeRegionUrlMap#allow_origin_regexes}
        :param allow_origins: Specifies the list of origins that will be allowed to do CORS requests. An origin is allowed if it matches either allow_origins or allow_origin_regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#allow_origins GoogleComputeRegionUrlMap#allow_origins}
        :param disabled: If true, specifies the CORS policy is disabled. which indicates that the CORS policy is in effect. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#disabled GoogleComputeRegionUrlMap#disabled}
        :param expose_headers: Specifies the content for the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#expose_headers GoogleComputeRegionUrlMap#expose_headers}
        :param max_age: Specifies how long the results of a preflight request can be cached. This translates to the content for the Access-Control-Max-Age header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#max_age GoogleComputeRegionUrlMap#max_age}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy(
            allow_credentials=allow_credentials,
            allow_headers=allow_headers,
            allow_methods=allow_methods,
            allow_origin_regexes=allow_origin_regexes,
            allow_origins=allow_origins,
            disabled=disabled,
            expose_headers=expose_headers,
            max_age=max_age,
        )

        return typing.cast(None, jsii.invoke(self, "putCorsPolicy", [value]))

    @jsii.member(jsii_name="putFaultInjectionPolicy")
    def put_fault_injection_policy(
        self,
        *,
        abort: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort, typing.Dict[str, typing.Any]]] = None,
        delay: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abort: abort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#abort GoogleComputeRegionUrlMap#abort}
        :param delay: delay block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delay GoogleComputeRegionUrlMap#delay}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy(
            abort=abort, delay=delay
        )

        return typing.cast(None, jsii.invoke(self, "putFaultInjectionPolicy", [value]))

    @jsii.member(jsii_name="putRequestMirrorPolicy")
    def put_request_mirror_policy(self, *, backend_service: builtins.str) -> None:
        '''
        :param backend_service: The RegionBackendService resource being mirrored to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy(
            backend_service=backend_service
        )

        return typing.cast(None, jsii.invoke(self, "putRequestMirrorPolicy", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        num_retries: jsii.Number,
        per_try_timeout: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout", typing.Dict[str, typing.Any]]] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param num_retries: Specifies the allowed number retries. This number must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#num_retries GoogleComputeRegionUrlMap#num_retries}
        :param per_try_timeout: per_try_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#per_try_timeout GoogleComputeRegionUrlMap#per_try_timeout}
        :param retry_conditions: Specifies one or more conditions when this retry rule applies. Valid values are:. 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code, or if the backend service does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504. connect-failure: Loadbalancer will retry on failures connecting to backend services, for example due to connection timeouts. retriable-4xx: Loadbalancer will retry for retriable 4xx response codes. Currently the only retriable error supported is 409. refused-stream: Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_conditions GoogleComputeRegionUrlMap#retry_conditions}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy(
            num_retries=num_retries,
            per_try_timeout=per_try_timeout,
            retry_conditions=retry_conditions,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="putUrlRewrite")
    def put_url_rewrite(
        self,
        *,
        host_rewrite: typing.Optional[builtins.str] = None,
        path_prefix_rewrite: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_rewrite: Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rewrite GoogleComputeRegionUrlMap#host_rewrite}
        :param path_prefix_rewrite: Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_prefix_rewrite GoogleComputeRegionUrlMap#path_prefix_rewrite}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite(
            host_rewrite=host_rewrite, path_prefix_rewrite=path_prefix_rewrite
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRewrite", [value]))

    @jsii.member(jsii_name="putWeightedBackendServices")
    def put_weighted_backend_services(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference.put_weighted_backend_services)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeightedBackendServices", [value]))

    @jsii.member(jsii_name="resetCorsPolicy")
    def reset_cors_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsPolicy", []))

    @jsii.member(jsii_name="resetFaultInjectionPolicy")
    def reset_fault_injection_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaultInjectionPolicy", []))

    @jsii.member(jsii_name="resetRequestMirrorPolicy")
    def reset_request_mirror_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMirrorPolicy", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetUrlRewrite")
    def reset_url_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRewrite", []))

    @jsii.member(jsii_name="resetWeightedBackendServices")
    def reset_weighted_backend_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedBackendServices", []))

    @builtins.property
    @jsii.member(jsii_name="corsPolicy")
    def cors_policy(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference, jsii.get(self, "corsPolicy"))

    @builtins.property
    @jsii.member(jsii_name="faultInjectionPolicy")
    def fault_injection_policy(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference, jsii.get(self, "faultInjectionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="requestMirrorPolicy")
    def request_mirror_policy(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference", jsii.get(self, "requestMirrorPolicy"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="urlRewrite")
    def url_rewrite(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference", jsii.get(self, "urlRewrite"))

    @builtins.property
    @jsii.member(jsii_name="weightedBackendServices")
    def weighted_backend_services(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList", jsii.get(self, "weightedBackendServices"))

    @builtins.property
    @jsii.member(jsii_name="corsPolicyInput")
    def cors_policy_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy], jsii.get(self, "corsPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="faultInjectionPolicyInput")
    def fault_injection_policy_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy], jsii.get(self, "faultInjectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMirrorPolicyInput")
    def request_mirror_policy_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy"], jsii.get(self, "requestMirrorPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteInput")
    def url_rewrite_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite"], jsii.get(self, "urlRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedBackendServicesInput")
    def weighted_backend_services_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices"]]], jsii.get(self, "weightedBackendServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy",
    jsii_struct_bases=[],
    name_mapping={"backend_service": "backendService"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy:
    def __init__(self, *, backend_service: builtins.str) -> None:
        '''
        :param backend_service: The RegionBackendService resource being mirrored to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy.__init__)
            check_type(argname="argument backend_service", value=backend_service, expected_type=type_hints["backend_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_service": backend_service,
        }

    @builtins.property
    def backend_service(self) -> builtins.str:
        '''The RegionBackendService resource being mirrored to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        '''
        result = self._values.get("backend_service")
        assert result is not None, "Required property 'backend_service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="backendServiceInput")
    def backend_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="backendService")
    def backend_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendService"))

    @backend_service.setter
    def backend_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference, "backend_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendService", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "num_retries": "numRetries",
        "per_try_timeout": "perTryTimeout",
        "retry_conditions": "retryConditions",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy:
    def __init__(
        self,
        *,
        num_retries: jsii.Number,
        per_try_timeout: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout", typing.Dict[str, typing.Any]]] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param num_retries: Specifies the allowed number retries. This number must be > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#num_retries GoogleComputeRegionUrlMap#num_retries}
        :param per_try_timeout: per_try_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#per_try_timeout GoogleComputeRegionUrlMap#per_try_timeout}
        :param retry_conditions: Specifies one or more conditions when this retry rule applies. Valid values are:. 5xx: Loadbalancer will attempt a retry if the backend service responds with any 5xx response code, or if the backend service does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or 504. connect-failure: Loadbalancer will retry on failures connecting to backend services, for example due to connection timeouts. retriable-4xx: Loadbalancer will retry for retriable 4xx response codes. Currently the only retriable error supported is 409. refused-stream: Loadbalancer will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. cancelled: Loadbalancer will retry if the gRPC status code in the response header is set to cancelled deadline-exceeded: Loadbalancer will retry if the gRPC status code in the response header is set to deadline-exceeded resource-exhausted: Loadbalancer will retry if the gRPC status code in the response header is set to resource-exhausted unavailable: Loadbalancer will retry if the gRPC status code in the response header is set to unavailable Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_conditions GoogleComputeRegionUrlMap#retry_conditions}
        '''
        if isinstance(per_try_timeout, dict):
            per_try_timeout = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout(**per_try_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy.__init__)
            check_type(argname="argument num_retries", value=num_retries, expected_type=type_hints["num_retries"])
            check_type(argname="argument per_try_timeout", value=per_try_timeout, expected_type=type_hints["per_try_timeout"])
            check_type(argname="argument retry_conditions", value=retry_conditions, expected_type=type_hints["retry_conditions"])
        self._values: typing.Dict[str, typing.Any] = {
            "num_retries": num_retries,
        }
        if per_try_timeout is not None:
            self._values["per_try_timeout"] = per_try_timeout
        if retry_conditions is not None:
            self._values["retry_conditions"] = retry_conditions

    @builtins.property
    def num_retries(self) -> jsii.Number:
        '''Specifies the allowed number retries. This number must be > 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#num_retries GoogleComputeRegionUrlMap#num_retries}
        '''
        result = self._values.get("num_retries")
        assert result is not None, "Required property 'num_retries' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def per_try_timeout(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout"]:
        '''per_try_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#per_try_timeout GoogleComputeRegionUrlMap#per_try_timeout}
        '''
        result = self._values.get("per_try_timeout")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout"], result)

    @builtins.property
    def retry_conditions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies one or more conditions when this retry rule applies. Valid values are:.

        5xx: Loadbalancer will attempt a retry if the backend service responds with
        any 5xx response code, or if the backend service does not respond at all,
        example: disconnects, reset, read timeout, connection failure, and refused
        streams.
        gateway-error: Similar to 5xx, but only applies to response codes
        502, 503 or 504.
        connect-failure: Loadbalancer will retry on failures
        connecting to backend services, for example due to connection timeouts.
        retriable-4xx: Loadbalancer will retry for retriable 4xx response codes.
        Currently the only retriable error supported is 409.
        refused-stream: Loadbalancer will retry if the backend service resets the stream with a
        REFUSED_STREAM error code. This reset type indicates that it is safe to retry.
        cancelled: Loadbalancer will retry if the gRPC status code in the response
        header is set to cancelled
        deadline-exceeded: Loadbalancer will retry if the
        gRPC status code in the response header is set to deadline-exceeded
        resource-exhausted: Loadbalancer will retry if the gRPC status code in the response
        header is set to resource-exhausted
        unavailable: Loadbalancer will retry if the gRPC status code in
        the response header is set to unavailable

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#retry_conditions GoogleComputeRegionUrlMap#retry_conditions}
        '''
        result = self._values.get("retry_conditions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPerTryTimeout")
    def put_per_try_timeout(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putPerTryTimeout", [value]))

    @jsii.member(jsii_name="resetPerTryTimeout")
    def reset_per_try_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerTryTimeout", []))

    @jsii.member(jsii_name="resetRetryConditions")
    def reset_retry_conditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryConditions", []))

    @builtins.property
    @jsii.member(jsii_name="perTryTimeout")
    def per_try_timeout(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference", jsii.get(self, "perTryTimeout"))

    @builtins.property
    @jsii.member(jsii_name="numRetriesInput")
    def num_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="perTryTimeoutInput")
    def per_try_timeout_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout"]:
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout"], jsii.get(self, "perTryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="retryConditionsInput")
    def retry_conditions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "retryConditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="numRetries")
    def num_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numRetries"))

    @num_retries.setter
    def num_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference, "num_retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numRetries", value)

    @builtins.property
    @jsii.member(jsii_name="retryConditions")
    def retry_conditions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "retryConditions"))

    @retry_conditions.setter
    def retry_conditions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference, "retry_conditions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryConditions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout:
    def __init__(
        self,
        *,
        seconds: builtins.str,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> builtins.str:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#seconds GoogleComputeRegionUrlMap#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#nanos GoogleComputeRegionUrlMap#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite",
    jsii_struct_bases=[],
    name_mapping={
        "host_rewrite": "hostRewrite",
        "path_prefix_rewrite": "pathPrefixRewrite",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite:
    def __init__(
        self,
        *,
        host_rewrite: typing.Optional[builtins.str] = None,
        path_prefix_rewrite: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_rewrite: Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rewrite GoogleComputeRegionUrlMap#host_rewrite}
        :param path_prefix_rewrite: Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_prefix_rewrite GoogleComputeRegionUrlMap#path_prefix_rewrite}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite.__init__)
            check_type(argname="argument host_rewrite", value=host_rewrite, expected_type=type_hints["host_rewrite"])
            check_type(argname="argument path_prefix_rewrite", value=path_prefix_rewrite, expected_type=type_hints["path_prefix_rewrite"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_rewrite is not None:
            self._values["host_rewrite"] = host_rewrite
        if path_prefix_rewrite is not None:
            self._values["path_prefix_rewrite"] = path_prefix_rewrite

    @builtins.property
    def host_rewrite(self) -> typing.Optional[builtins.str]:
        '''Prior to forwarding the request to the selected service, the request's host header is replaced with contents of hostRewrite.

        The value must be between 1 and
        255 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_rewrite GoogleComputeRegionUrlMap#host_rewrite}
        '''
        result = self._values.get("host_rewrite")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_prefix_rewrite(self) -> typing.Optional[builtins.str]:
        '''Prior to forwarding the request to the selected backend service, the matching portion of the request's path is replaced by pathPrefixRewrite.

        The value must
        be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_prefix_rewrite GoogleComputeRegionUrlMap#path_prefix_rewrite}
        '''
        result = self._values.get("path_prefix_rewrite")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRewrite")
    def reset_host_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRewrite", []))

    @jsii.member(jsii_name="resetPathPrefixRewrite")
    def reset_path_prefix_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPrefixRewrite", []))

    @builtins.property
    @jsii.member(jsii_name="hostRewriteInput")
    def host_rewrite_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixRewriteInput")
    def path_prefix_rewrite_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixRewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRewrite")
    def host_rewrite(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRewrite"))

    @host_rewrite.setter
    def host_rewrite(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference, "host_rewrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRewrite", value)

    @builtins.property
    @jsii.member(jsii_name="pathPrefixRewrite")
    def path_prefix_rewrite(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefixRewrite"))

    @path_prefix_rewrite.setter
    def path_prefix_rewrite(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference, "path_prefix_rewrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefixRewrite", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices",
    jsii_struct_bases=[],
    name_mapping={
        "backend_service": "backendService",
        "weight": "weight",
        "header_action": "headerAction",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices:
    def __init__(
        self,
        *,
        backend_service: builtins.str,
        weight: jsii.Number,
        header_action: typing.Optional[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backend_service: The default RegionBackendService resource. Before forwarding the request to backendService, the loadbalancer applies any relevant headerActions specified as part of this backendServiceWeight. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        :param weight: Specifies the fraction of traffic sent to backendService, computed as weight / (sum of all weightedBackendService weights in routeAction) . The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backendService, subsequent requests will be sent to the same backendService as determined by the BackendService's session affinity policy. The value must be between 0 and 1000 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weight GoogleComputeRegionUrlMap#weight}
        :param header_action: header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_action GoogleComputeRegionUrlMap#header_action}
        '''
        if isinstance(header_action, dict):
            header_action = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction(**header_action)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices.__init__)
            check_type(argname="argument backend_service", value=backend_service, expected_type=type_hints["backend_service"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument header_action", value=header_action, expected_type=type_hints["header_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_service": backend_service,
            "weight": weight,
        }
        if header_action is not None:
            self._values["header_action"] = header_action

    @builtins.property
    def backend_service(self) -> builtins.str:
        '''The default RegionBackendService resource.

        Before
        forwarding the request to backendService, the loadbalancer applies any relevant
        headerActions specified as part of this backendServiceWeight.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#backend_service GoogleComputeRegionUrlMap#backend_service}
        '''
        result = self._values.get("backend_service")
        assert result is not None, "Required property 'backend_service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Specifies the fraction of traffic sent to backendService, computed as weight / (sum of all weightedBackendService weights in routeAction) .

        The selection of a
        backend service is determined only for new traffic. Once a user's request has
        been directed to a backendService, subsequent requests will be sent to the same
        backendService as determined by the BackendService's session affinity policy.
        The value must be between 0 and 1000

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#weight GoogleComputeRegionUrlMap#weight}
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def header_action(
        self,
    ) -> typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction"]:
        '''header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_action GoogleComputeRegionUrlMap#header_action}
        '''
        result = self._values.get("header_action")
        return typing.cast(typing.Optional["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction",
    jsii_struct_bases=[],
    name_mapping={
        "request_headers_to_add": "requestHeadersToAdd",
        "request_headers_to_remove": "requestHeadersToRemove",
        "response_headers_to_add": "responseHeadersToAdd",
        "response_headers_to_remove": "responseHeadersToRemove",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction:
    def __init__(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction.__init__)
            check_type(argname="argument request_headers_to_add", value=request_headers_to_add, expected_type=type_hints["request_headers_to_add"])
            check_type(argname="argument request_headers_to_remove", value=request_headers_to_remove, expected_type=type_hints["request_headers_to_remove"])
            check_type(argname="argument response_headers_to_add", value=response_headers_to_add, expected_type=type_hints["response_headers_to_add"])
            check_type(argname="argument response_headers_to_remove", value=response_headers_to_remove, expected_type=type_hints["response_headers_to_remove"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request_headers_to_add is not None:
            self._values["request_headers_to_add"] = request_headers_to_add
        if request_headers_to_remove is not None:
            self._values["request_headers_to_remove"] = request_headers_to_remove
        if response_headers_to_add is not None:
            self._values["response_headers_to_add"] = response_headers_to_add
        if response_headers_to_remove is not None:
            self._values["response_headers_to_remove"] = response_headers_to_remove

    @builtins.property
    def request_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]]:
        '''request_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        '''
        result = self._values.get("request_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]], result)

    @builtins.property
    def request_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        '''
        result = self._values.get("request_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def response_headers_to_add(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]]:
        '''response_headers_to_add block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        '''
        result = self._values.get("response_headers_to_add")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]], result)

    @builtins.property
    def response_headers_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of header names for headers that need to be removed from the response prior to sending the response back to the client.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        result = self._values.get("response_headers_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestHeadersToAdd")
    def put_request_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference.put_request_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeadersToAdd", [value]))

    @jsii.member(jsii_name="putResponseHeadersToAdd")
    def put_response_headers_to_add(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference.put_response_headers_to_add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeadersToAdd", [value]))

    @jsii.member(jsii_name="resetRequestHeadersToAdd")
    def reset_request_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToAdd", []))

    @jsii.member(jsii_name="resetRequestHeadersToRemove")
    def reset_request_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeadersToRemove", []))

    @jsii.member(jsii_name="resetResponseHeadersToAdd")
    def reset_response_headers_to_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToAdd", []))

    @jsii.member(jsii_name="resetResponseHeadersToRemove")
    def reset_response_headers_to_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeadersToRemove", []))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAdd")
    def request_headers_to_add(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList", jsii.get(self, "requestHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAdd")
    def response_headers_to_add(
        self,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList":
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList", jsii.get(self, "responseHeadersToAdd"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToAddInput")
    def request_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd"]]], jsii.get(self, "requestHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemoveInput")
    def request_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToAddInput")
    def response_headers_to_add_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd"]]], jsii.get(self, "responseHeadersToAddInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemoveInput")
    def response_headers_to_remove_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseHeadersToRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersToRemove")
    def request_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestHeadersToRemove"))

    @request_headers_to_remove.setter
    def request_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference, "request_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeadersToRemove")
    def response_headers_to_remove(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseHeadersToRemove"))

    @response_headers_to_remove.setter
    def response_headers_to_remove(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference, "response_headers_to_remove").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeadersToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "header_value": "headerValue",
        "replace": "replace",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
        replace: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param header_name: The name of the header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        :param header_value: The value of the header to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        :param replace: If false, headerValue is appended to any values that already exist for the header. If true, headerValue is set for the header, discarding any values that were set for that header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            check_type(argname="argument replace", value=replace, expected_type=type_hints["replace"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
            "replace": replace,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_name GoogleComputeRegionUrlMap#header_name}
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The value of the header to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#header_value GoogleComputeRegionUrlMap#header_value}
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If false, headerValue is appended to any values that already exist for the header.

        If true, headerValue is set for the header, discarding any values that
        were set for that header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#replace GoogleComputeRegionUrlMap#replace}
        '''
        result = self._values.get("replace")
        assert result is not None, "Required property 'replace' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="headerValueInput")
    def header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerValueInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceInput")
    def replace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "replaceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="headerValue")
    def header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerValue"))

    @header_value.setter
    def header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerValue", value)

    @builtins.property
    @jsii.member(jsii_name="replace")
    def replace(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "replace"))

    @replace.setter
    def replace(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "replace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaderAction")
    def put_header_action(
        self,
        *,
        request_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        request_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_headers_to_add: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd, typing.Dict[str, typing.Any]]]]] = None,
        response_headers_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param request_headers_to_add: request_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_add GoogleComputeRegionUrlMap#request_headers_to_add}
        :param request_headers_to_remove: A list of header names for headers that need to be removed from the request prior to forwarding the request to the backendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#request_headers_to_remove GoogleComputeRegionUrlMap#request_headers_to_remove}
        :param response_headers_to_add: response_headers_to_add block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_add GoogleComputeRegionUrlMap#response_headers_to_add}
        :param response_headers_to_remove: A list of header names for headers that need to be removed from the response prior to sending the response back to the client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#response_headers_to_remove GoogleComputeRegionUrlMap#response_headers_to_remove}
        '''
        value = GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction(
            request_headers_to_add=request_headers_to_add,
            request_headers_to_remove=request_headers_to_remove,
            response_headers_to_add=response_headers_to_add,
            response_headers_to_remove=response_headers_to_remove,
        )

        return typing.cast(None, jsii.invoke(self, "putHeaderAction", [value]))

    @jsii.member(jsii_name="resetHeaderAction")
    def reset_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderAction", []))

    @builtins.property
    @jsii.member(jsii_name="headerAction")
    def header_action(
        self,
    ) -> GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference:
        return typing.cast(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference, jsii.get(self, "headerAction"))

    @builtins.property
    @jsii.member(jsii_name="backendServiceInput")
    def backend_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="headerActionInput")
    def header_action_input(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction], jsii.get(self, "headerActionInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="backendService")
    def backend_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendService"))

    @backend_service.setter
    def backend_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference, "backend_service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendService", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "host_redirect": "hostRedirect",
        "https_redirect": "httpsRedirect",
        "path_redirect": "pathRedirect",
        "prefix_redirect": "prefixRedirect",
        "redirect_response_code": "redirectResponseCode",
        "strip_query": "stripQuery",
    },
)
class GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect:
    def __init__(
        self,
        *,
        host_redirect: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path_redirect: typing.Optional[builtins.str] = None,
        prefix_redirect: typing.Optional[builtins.str] = None,
        redirect_response_code: typing.Optional[builtins.str] = None,
        strip_query: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param host_redirect: The host that will be used in the redirect response instead of the one that was supplied in the request. The value must be between 1 and 255 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        :param https_redirect: If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this true for TargetHttpsProxy is not permitted. The default is set to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        :param path_redirect: The path that will be used in the redirect response instead of the one that was supplied in the request. pathRedirect cannot be supplied together with prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        :param prefix_redirect: The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request. prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. The value must be between 1 and 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        :param redirect_response_code: The HTTP Status code to use for this RedirectAction. Supported values are:. MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301. FOUND, which corresponds to 302. SEE_OTHER which corresponds to 303. TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method will be retained. PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        :param strip_query: If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect.__init__)
            check_type(argname="argument host_redirect", value=host_redirect, expected_type=type_hints["host_redirect"])
            check_type(argname="argument https_redirect", value=https_redirect, expected_type=type_hints["https_redirect"])
            check_type(argname="argument path_redirect", value=path_redirect, expected_type=type_hints["path_redirect"])
            check_type(argname="argument prefix_redirect", value=prefix_redirect, expected_type=type_hints["prefix_redirect"])
            check_type(argname="argument redirect_response_code", value=redirect_response_code, expected_type=type_hints["redirect_response_code"])
            check_type(argname="argument strip_query", value=strip_query, expected_type=type_hints["strip_query"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_redirect is not None:
            self._values["host_redirect"] = host_redirect
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if path_redirect is not None:
            self._values["path_redirect"] = path_redirect
        if prefix_redirect is not None:
            self._values["prefix_redirect"] = prefix_redirect
        if redirect_response_code is not None:
            self._values["redirect_response_code"] = redirect_response_code
        if strip_query is not None:
            self._values["strip_query"] = strip_query

    @builtins.property
    def host_redirect(self) -> typing.Optional[builtins.str]:
        '''The host that will be used in the redirect response instead of the one that was supplied in the request.

        The value must be between 1 and 255
        characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host_redirect GoogleComputeRegionUrlMap#host_redirect}
        '''
        result = self._values.get("host_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the URL scheme in the redirected request is set to https.

        If set to false, the URL scheme of the redirected request will remain the
        same as that of the request. This must only be set for UrlMaps used in
        TargetHttpProxys. Setting this true for TargetHttpsProxy is not
        permitted. The default is set to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#https_redirect GoogleComputeRegionUrlMap#https_redirect}
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path_redirect(self) -> typing.Optional[builtins.str]:
        '''The path that will be used in the redirect response instead of the one that was supplied in the request.

        pathRedirect cannot be supplied
        together with prefixRedirect. Supply one alone or neither. If neither is
        supplied, the path of the original request will be used for the redirect.
        The value must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path_redirect GoogleComputeRegionUrlMap#path_redirect}
        '''
        result = self._values.get("path_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_redirect(self) -> typing.Optional[builtins.str]:
        '''The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch, retaining the remaining portion of the URL before redirecting the request.

        prefixRedirect cannot be supplied together with
        pathRedirect. Supply one alone or neither. If neither is supplied, the
        path of the original request will be used for the redirect. The value
        must be between 1 and 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#prefix_redirect GoogleComputeRegionUrlMap#prefix_redirect}
        '''
        result = self._values.get("prefix_redirect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_response_code(self) -> typing.Optional[builtins.str]:
        '''The HTTP Status code to use for this RedirectAction. Supported values are:.

        MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.

        FOUND, which corresponds to 302.

        SEE_OTHER which corresponds to 303.

        TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        will be retained.

        PERMANENT_REDIRECT, which corresponds to 308. In this case,
        the request method will be retained. Possible values: ["FOUND", "MOVED_PERMANENTLY_DEFAULT", "PERMANENT_REDIRECT", "SEE_OTHER", "TEMPORARY_REDIRECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#redirect_response_code GoogleComputeRegionUrlMap#redirect_response_code}
        '''
        result = self._values.get("redirect_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def strip_query(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, any accompanying query portion of the original URL is removed prior to redirecting the request.

        If set to false, the query
        portion of the original URL is retained. The default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#strip_query GoogleComputeRegionUrlMap#strip_query}
        '''
        result = self._values.get("strip_query")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostRedirect")
    def reset_host_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostRedirect", []))

    @jsii.member(jsii_name="resetHttpsRedirect")
    def reset_https_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsRedirect", []))

    @jsii.member(jsii_name="resetPathRedirect")
    def reset_path_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathRedirect", []))

    @jsii.member(jsii_name="resetPrefixRedirect")
    def reset_prefix_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixRedirect", []))

    @jsii.member(jsii_name="resetRedirectResponseCode")
    def reset_redirect_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectResponseCode", []))

    @jsii.member(jsii_name="resetStripQuery")
    def reset_strip_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStripQuery", []))

    @builtins.property
    @jsii.member(jsii_name="hostRedirectInput")
    def host_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectInput")
    def https_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpsRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="pathRedirectInput")
    def path_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixRedirectInput")
    def prefix_redirect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCodeInput")
    def redirect_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="stripQueryInput")
    def strip_query_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stripQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostRedirect")
    def host_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostRedirect"))

    @host_redirect.setter
    def host_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "host_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirect")
    def https_redirect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "httpsRedirect"))

    @https_redirect.setter
    def https_redirect(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "https_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="pathRedirect")
    def path_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathRedirect"))

    @path_redirect.setter
    def path_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "path_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="prefixRedirect")
    def prefix_redirect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixRedirect"))

    @prefix_redirect.setter
    def prefix_redirect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "prefix_redirect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixRedirect", value)

    @builtins.property
    @jsii.member(jsii_name="redirectResponseCode")
    def redirect_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectResponseCode"))

    @redirect_response_code.setter
    def redirect_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "redirect_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="stripQuery")
    def strip_query(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stripQuery"))

    @strip_query.setter
    def strip_query(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "strip_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripQuery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect]:
        return typing.cast(typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapTest",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "path": "path",
        "service": "service",
        "description": "description",
    },
)
class GoogleComputeRegionUrlMapTest:
    def __init__(
        self,
        *,
        host: builtins.str,
        path: builtins.str,
        service: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Host portion of the URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host GoogleComputeRegionUrlMap#host}
        :param path: Path portion of the URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path GoogleComputeRegionUrlMap#path}
        :param service: A reference to expected RegionBackendService resource the given URL should be mapped to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#service GoogleComputeRegionUrlMap#service}
        :param description: Description of this test case. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapTest.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "path": path,
            "service": service,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def host(self) -> builtins.str:
        '''Host portion of the URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#host GoogleComputeRegionUrlMap#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path portion of the URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#path GoogleComputeRegionUrlMap#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''A reference to expected RegionBackendService resource the given URL should be mapped to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#service GoogleComputeRegionUrlMap#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of this test case.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#description GoogleComputeRegionUrlMap#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapTest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapTestList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapTestList",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapTestList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleComputeRegionUrlMapTestOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapTestList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionUrlMapTestOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapTest]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapTest]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRegionUrlMapTest]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionUrlMapTestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapTestOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapTestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapTest, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapTest, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapTest, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeRegionUrlMapTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#create GoogleComputeRegionUrlMap#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delete GoogleComputeRegionUrlMap#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#update GoogleComputeRegionUrlMap#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#create GoogleComputeRegionUrlMap#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#delete GoogleComputeRegionUrlMap#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_url_map#update GoogleComputeRegionUrlMap#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionUrlMapTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionUrlMapTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionUrlMap.GoogleComputeRegionUrlMapTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRegionUrlMapTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionUrlMapTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionUrlMapTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionUrlMapTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionUrlMapTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeRegionUrlMap",
    "GoogleComputeRegionUrlMapConfig",
    "GoogleComputeRegionUrlMapDefaultUrlRedirect",
    "GoogleComputeRegionUrlMapDefaultUrlRedirectOutputReference",
    "GoogleComputeRegionUrlMapHostRule",
    "GoogleComputeRegionUrlMapHostRuleList",
    "GoogleComputeRegionUrlMapHostRuleOutputReference",
    "GoogleComputeRegionUrlMapPathMatcher",
    "GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirect",
    "GoogleComputeRegionUrlMapPathMatcherDefaultUrlRedirectOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherList",
    "GoogleComputeRegionUrlMapPathMatcherOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRule",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleList",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteAction",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicy",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionCorsPolicyOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicy",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicy",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicy",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeout",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionTimeoutOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewrite",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionUrlRewriteOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServices",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderAction",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesList",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleRouteActionWeightedBackendServicesOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirect",
    "GoogleComputeRegionUrlMapPathMatcherPathRuleUrlRedirectOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRules",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderAction",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAdd",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionRequestHeadersToAddOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAdd",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesHeaderActionResponseHeadersToAddOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRules",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatches",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatch",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesHeaderMatchesRangeMatchOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFilters",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabels",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersFilterLabelsOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesMetadataFiltersOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatches",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesMatchRulesQueryParameterMatchesOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteAction",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicy",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionCorsPolicyOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicy",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbort",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyAbortOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelay",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelay",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayFixedDelayOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyDelayOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionFaultInjectionPolicyOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicy",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRequestMirrorPolicyOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicy",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeout",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionRetryPolicyPerTryTimeoutOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeout",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionTimeoutOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewrite",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionUrlRewriteOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServices",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderAction",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAdd",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionRequestHeadersToAddOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAdd",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesHeaderActionResponseHeadersToAddOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesList",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesRouteActionWeightedBackendServicesOutputReference",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirect",
    "GoogleComputeRegionUrlMapPathMatcherRouteRulesUrlRedirectOutputReference",
    "GoogleComputeRegionUrlMapTest",
    "GoogleComputeRegionUrlMapTestList",
    "GoogleComputeRegionUrlMapTestOutputReference",
    "GoogleComputeRegionUrlMapTimeouts",
    "GoogleComputeRegionUrlMapTimeoutsOutputReference",
]

publication.publish()
