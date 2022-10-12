'''
# `google_monitoring_uptime_check_config`

Refer to the Terraform Registory for docs: [`google_monitoring_uptime_check_config`](https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config).
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


class GoogleMonitoringUptimeCheckConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config google_monitoring_uptime_check_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        timeout: builtins.str,
        checker_type: typing.Optional[builtins.str] = None,
        content_matchers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringUptimeCheckConfigContentMatchers", typing.Dict[str, typing.Any]]]]] = None,
        http_check: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigHttpCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        monitored_resource: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigMonitoredResource", typing.Dict[str, typing.Any]]] = None,
        period: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        resource_group: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigResourceGroup", typing.Dict[str, typing.Any]]] = None,
        selected_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tcp_check: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigTcpCheck", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config google_monitoring_uptime_check_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#display_name GoogleMonitoringUptimeCheckConfig#display_name}
        :param timeout: The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#timeout GoogleMonitoringUptimeCheckConfig#timeout}
        :param checker_type: The checker type to use for the check. If the monitored resource type is servicedirectory_service, checkerType must be set to VPC_CHECKERS. Possible values: ["STATIC_IP_CHECKERS", "VPC_CHECKERS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#checker_type GoogleMonitoringUptimeCheckConfig#checker_type}
        :param content_matchers: content_matchers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#content_matchers GoogleMonitoringUptimeCheckConfig#content_matchers}
        :param http_check: http_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#http_check GoogleMonitoringUptimeCheckConfig#http_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#id GoogleMonitoringUptimeCheckConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monitored_resource: monitored_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#monitored_resource GoogleMonitoringUptimeCheckConfig#monitored_resource}
        :param period: How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#period GoogleMonitoringUptimeCheckConfig#period}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#project GoogleMonitoringUptimeCheckConfig#project}.
        :param resource_group: resource_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#resource_group GoogleMonitoringUptimeCheckConfig#resource_group}
        :param selected_regions: The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error message is returned. Not specifying this field will result in uptime checks running from all regions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#selected_regions GoogleMonitoringUptimeCheckConfig#selected_regions}
        :param tcp_check: tcp_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#tcp_check GoogleMonitoringUptimeCheckConfig#tcp_check}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#timeouts GoogleMonitoringUptimeCheckConfig#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleMonitoringUptimeCheckConfigConfig(
            display_name=display_name,
            timeout=timeout,
            checker_type=checker_type,
            content_matchers=content_matchers,
            http_check=http_check,
            id=id,
            monitored_resource=monitored_resource,
            period=period,
            project=project,
            resource_group=resource_group,
            selected_regions=selected_regions,
            tcp_check=tcp_check,
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

    @jsii.member(jsii_name="putContentMatchers")
    def put_content_matchers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringUptimeCheckConfigContentMatchers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfig.put_content_matchers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContentMatchers", [value]))

    @jsii.member(jsii_name="putHttpCheck")
    def put_http_check(
        self,
        *,
        accepted_response_status_codes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes", typing.Dict[str, typing.Any]]]]] = None,
        auth_info: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        mask_headers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        request_method: typing.Optional[builtins.str] = None,
        use_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        validate_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param accepted_response_status_codes: accepted_response_status_codes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#accepted_response_status_codes GoogleMonitoringUptimeCheckConfig#accepted_response_status_codes}
        :param auth_info: auth_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#auth_info GoogleMonitoringUptimeCheckConfig#auth_info}
        :param body: The request body associated with the HTTP POST request. If contentType is URL_ENCODED, the body passed in must be URL-encoded. Users can provide a Content-Length header via the headers field or the API will do so. If the requestMethod is GET and body is not empty, the API will return an error. The maximum byte size is 1 megabyte. Note - As with all bytes fields JSON representations are base64 encoded. e.g. "foo=bar" in URL-encoded form is "foo%3Dbar" and in base64 encoding is "Zm9vJTI1M0RiYXI=". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#body GoogleMonitoringUptimeCheckConfig#body}
        :param content_type: The content type to use for the check. Possible values: ["TYPE_UNSPECIFIED", "URL_ENCODED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#content_type GoogleMonitoringUptimeCheckConfig#content_type}
        :param headers: The list of headers to send as part of the uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at https://www.w3.org/Protocols/rfc2616/rfc2616.txt (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#headers GoogleMonitoringUptimeCheckConfig#headers}
        :param mask_headers: Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to True then the headers will be obscured with ******. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#mask_headers GoogleMonitoringUptimeCheckConfig#mask_headers}
        :param path: The path to the page to run the check against. Will be combined with the host (specified within the MonitoredResource) and port to construct the full URL. If the provided path does not begin with "/", a "/" will be prepended automatically. Optional (defaults to "/"). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#path GoogleMonitoringUptimeCheckConfig#path}
        :param port: The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) and path to construct the full URL. Optional (defaults to 80 without SSL, or 443 with SSL). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#port GoogleMonitoringUptimeCheckConfig#port}
        :param request_method: The HTTP request method to use for the check. If set to METHOD_UNSPECIFIED then requestMethod defaults to GET. Default value: "GET" Possible values: ["METHOD_UNSPECIFIED", "GET", "POST"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#request_method GoogleMonitoringUptimeCheckConfig#request_method}
        :param use_ssl: If true, use HTTPS instead of HTTP to run the check. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#use_ssl GoogleMonitoringUptimeCheckConfig#use_ssl}
        :param validate_ssl: Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where monitoredResource is set to uptime_url. If useSsl is false, setting validateSsl to true has no effect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#validate_ssl GoogleMonitoringUptimeCheckConfig#validate_ssl}
        '''
        value = GoogleMonitoringUptimeCheckConfigHttpCheck(
            accepted_response_status_codes=accepted_response_status_codes,
            auth_info=auth_info,
            body=body,
            content_type=content_type,
            headers=headers,
            mask_headers=mask_headers,
            path=path,
            port=port,
            request_method=request_method,
            use_ssl=use_ssl,
            validate_ssl=validate_ssl,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpCheck", [value]))

    @jsii.member(jsii_name="putMonitoredResource")
    def put_monitored_resource(
        self,
        *,
        labels: typing.Mapping[builtins.str, builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param labels: Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels "project_id", "instance_id", and "zone". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#labels GoogleMonitoringUptimeCheckConfig#labels}
        :param type: The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor) object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (https://cloud.google.com/monitoring/api/resources) and Logging resource types (https://cloud.google.com/logging/docs/api/v2/resource-list). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#type GoogleMonitoringUptimeCheckConfig#type}
        '''
        value = GoogleMonitoringUptimeCheckConfigMonitoredResource(
            labels=labels, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putMonitoredResource", [value]))

    @jsii.member(jsii_name="putResourceGroup")
    def put_resource_group(
        self,
        *,
        group_id: typing.Optional[builtins.str] = None,
        resource_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group_id: The group of resources being monitored. Should be the 'name' of a group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#group_id GoogleMonitoringUptimeCheckConfig#group_id}
        :param resource_type: The resource type of the group members. Possible values: ["RESOURCE_TYPE_UNSPECIFIED", "INSTANCE", "AWS_ELB_LOAD_BALANCER"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#resource_type GoogleMonitoringUptimeCheckConfig#resource_type}
        '''
        value = GoogleMonitoringUptimeCheckConfigResourceGroup(
            group_id=group_id, resource_type=resource_type
        )

        return typing.cast(None, jsii.invoke(self, "putResourceGroup", [value]))

    @jsii.member(jsii_name="putTcpCheck")
    def put_tcp_check(self, *, port: jsii.Number) -> None:
        '''
        :param port: The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#port GoogleMonitoringUptimeCheckConfig#port}
        '''
        value = GoogleMonitoringUptimeCheckConfigTcpCheck(port=port)

        return typing.cast(None, jsii.invoke(self, "putTcpCheck", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#create GoogleMonitoringUptimeCheckConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#delete GoogleMonitoringUptimeCheckConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#update GoogleMonitoringUptimeCheckConfig#update}.
        '''
        value = GoogleMonitoringUptimeCheckConfigTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCheckerType")
    def reset_checker_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckerType", []))

    @jsii.member(jsii_name="resetContentMatchers")
    def reset_content_matchers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentMatchers", []))

    @jsii.member(jsii_name="resetHttpCheck")
    def reset_http_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpCheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMonitoredResource")
    def reset_monitored_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoredResource", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetResourceGroup")
    def reset_resource_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceGroup", []))

    @jsii.member(jsii_name="resetSelectedRegions")
    def reset_selected_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectedRegions", []))

    @jsii.member(jsii_name="resetTcpCheck")
    def reset_tcp_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcpCheck", []))

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
    @jsii.member(jsii_name="contentMatchers")
    def content_matchers(
        self,
    ) -> "GoogleMonitoringUptimeCheckConfigContentMatchersList":
        return typing.cast("GoogleMonitoringUptimeCheckConfigContentMatchersList", jsii.get(self, "contentMatchers"))

    @builtins.property
    @jsii.member(jsii_name="httpCheck")
    def http_check(self) -> "GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference":
        return typing.cast("GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference", jsii.get(self, "httpCheck"))

    @builtins.property
    @jsii.member(jsii_name="monitoredResource")
    def monitored_resource(
        self,
    ) -> "GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference":
        return typing.cast("GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference", jsii.get(self, "monitoredResource"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroup")
    def resource_group(
        self,
    ) -> "GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference":
        return typing.cast("GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference", jsii.get(self, "resourceGroup"))

    @builtins.property
    @jsii.member(jsii_name="tcpCheck")
    def tcp_check(self) -> "GoogleMonitoringUptimeCheckConfigTcpCheckOutputReference":
        return typing.cast("GoogleMonitoringUptimeCheckConfigTcpCheckOutputReference", jsii.get(self, "tcpCheck"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference":
        return typing.cast("GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uptimeCheckId")
    def uptime_check_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uptimeCheckId"))

    @builtins.property
    @jsii.member(jsii_name="checkerTypeInput")
    def checker_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="contentMatchersInput")
    def content_matchers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringUptimeCheckConfigContentMatchers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringUptimeCheckConfigContentMatchers"]]], jsii.get(self, "contentMatchersInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="httpCheckInput")
    def http_check_input(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigHttpCheck"]:
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigHttpCheck"], jsii.get(self, "httpCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoredResourceInput")
    def monitored_resource_input(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigMonitoredResource"]:
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigMonitoredResource"], jsii.get(self, "monitoredResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupInput")
    def resource_group_input(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigResourceGroup"]:
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigResourceGroup"], jsii.get(self, "resourceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="selectedRegionsInput")
    def selected_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "selectedRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpCheckInput")
    def tcp_check_input(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigTcpCheck"]:
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigTcpCheck"], jsii.get(self, "tcpCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="checkerType")
    def checker_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkerType"))

    @checker_type.setter
    def checker_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfig, "checker_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkerType", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfig, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "period"))

    @period.setter
    def period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfig, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfig, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="selectedRegions")
    def selected_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "selectedRegions"))

    @selected_regions.setter
    def selected_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfig, "selected_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectedRegions", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfig, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "timeout": "timeout",
        "checker_type": "checkerType",
        "content_matchers": "contentMatchers",
        "http_check": "httpCheck",
        "id": "id",
        "monitored_resource": "monitoredResource",
        "period": "period",
        "project": "project",
        "resource_group": "resourceGroup",
        "selected_regions": "selectedRegions",
        "tcp_check": "tcpCheck",
        "timeouts": "timeouts",
    },
)
class GoogleMonitoringUptimeCheckConfigConfig(cdktf.TerraformMetaArguments):
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
        display_name: builtins.str,
        timeout: builtins.str,
        checker_type: typing.Optional[builtins.str] = None,
        content_matchers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringUptimeCheckConfigContentMatchers", typing.Dict[str, typing.Any]]]]] = None,
        http_check: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigHttpCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        monitored_resource: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigMonitoredResource", typing.Dict[str, typing.Any]]] = None,
        period: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        resource_group: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigResourceGroup", typing.Dict[str, typing.Any]]] = None,
        selected_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tcp_check: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigTcpCheck", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#display_name GoogleMonitoringUptimeCheckConfig#display_name}
        :param timeout: The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#timeout GoogleMonitoringUptimeCheckConfig#timeout}
        :param checker_type: The checker type to use for the check. If the monitored resource type is servicedirectory_service, checkerType must be set to VPC_CHECKERS. Possible values: ["STATIC_IP_CHECKERS", "VPC_CHECKERS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#checker_type GoogleMonitoringUptimeCheckConfig#checker_type}
        :param content_matchers: content_matchers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#content_matchers GoogleMonitoringUptimeCheckConfig#content_matchers}
        :param http_check: http_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#http_check GoogleMonitoringUptimeCheckConfig#http_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#id GoogleMonitoringUptimeCheckConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monitored_resource: monitored_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#monitored_resource GoogleMonitoringUptimeCheckConfig#monitored_resource}
        :param period: How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#period GoogleMonitoringUptimeCheckConfig#period}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#project GoogleMonitoringUptimeCheckConfig#project}.
        :param resource_group: resource_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#resource_group GoogleMonitoringUptimeCheckConfig#resource_group}
        :param selected_regions: The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error message is returned. Not specifying this field will result in uptime checks running from all regions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#selected_regions GoogleMonitoringUptimeCheckConfig#selected_regions}
        :param tcp_check: tcp_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#tcp_check GoogleMonitoringUptimeCheckConfig#tcp_check}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#timeouts GoogleMonitoringUptimeCheckConfig#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(http_check, dict):
            http_check = GoogleMonitoringUptimeCheckConfigHttpCheck(**http_check)
        if isinstance(monitored_resource, dict):
            monitored_resource = GoogleMonitoringUptimeCheckConfigMonitoredResource(**monitored_resource)
        if isinstance(resource_group, dict):
            resource_group = GoogleMonitoringUptimeCheckConfigResourceGroup(**resource_group)
        if isinstance(tcp_check, dict):
            tcp_check = GoogleMonitoringUptimeCheckConfigTcpCheck(**tcp_check)
        if isinstance(timeouts, dict):
            timeouts = GoogleMonitoringUptimeCheckConfigTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument checker_type", value=checker_type, expected_type=type_hints["checker_type"])
            check_type(argname="argument content_matchers", value=content_matchers, expected_type=type_hints["content_matchers"])
            check_type(argname="argument http_check", value=http_check, expected_type=type_hints["http_check"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument monitored_resource", value=monitored_resource, expected_type=type_hints["monitored_resource"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument resource_group", value=resource_group, expected_type=type_hints["resource_group"])
            check_type(argname="argument selected_regions", value=selected_regions, expected_type=type_hints["selected_regions"])
            check_type(argname="argument tcp_check", value=tcp_check, expected_type=type_hints["tcp_check"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "timeout": timeout,
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
        if checker_type is not None:
            self._values["checker_type"] = checker_type
        if content_matchers is not None:
            self._values["content_matchers"] = content_matchers
        if http_check is not None:
            self._values["http_check"] = http_check
        if id is not None:
            self._values["id"] = id
        if monitored_resource is not None:
            self._values["monitored_resource"] = monitored_resource
        if period is not None:
            self._values["period"] = period
        if project is not None:
            self._values["project"] = project
        if resource_group is not None:
            self._values["resource_group"] = resource_group
        if selected_regions is not None:
            self._values["selected_regions"] = selected_regions
        if tcp_check is not None:
            self._values["tcp_check"] = tcp_check
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
    def display_name(self) -> builtins.str:
        '''A human-friendly name for the uptime check configuration.

        The display name should be unique within a Stackdriver Workspace in order to make it easier to identify; however, uniqueness is not enforced.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#display_name GoogleMonitoringUptimeCheckConfig#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout(self) -> builtins.str:
        '''The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds).

        Accepted formats https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#timeout GoogleMonitoringUptimeCheckConfig#timeout}
        '''
        result = self._values.get("timeout")
        assert result is not None, "Required property 'timeout' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def checker_type(self) -> typing.Optional[builtins.str]:
        '''The checker type to use for the check.

        If the monitored resource type is servicedirectory_service, checkerType must be set to VPC_CHECKERS. Possible values: ["STATIC_IP_CHECKERS", "VPC_CHECKERS"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#checker_type GoogleMonitoringUptimeCheckConfig#checker_type}
        '''
        result = self._values.get("checker_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_matchers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringUptimeCheckConfigContentMatchers"]]]:
        '''content_matchers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#content_matchers GoogleMonitoringUptimeCheckConfig#content_matchers}
        '''
        result = self._values.get("content_matchers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringUptimeCheckConfigContentMatchers"]]], result)

    @builtins.property
    def http_check(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigHttpCheck"]:
        '''http_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#http_check GoogleMonitoringUptimeCheckConfig#http_check}
        '''
        result = self._values.get("http_check")
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigHttpCheck"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#id GoogleMonitoringUptimeCheckConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitored_resource(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigMonitoredResource"]:
        '''monitored_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#monitored_resource GoogleMonitoringUptimeCheckConfig#monitored_resource}
        '''
        result = self._values.get("monitored_resource")
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigMonitoredResource"], result)

    @builtins.property
    def period(self) -> typing.Optional[builtins.str]:
        '''How often, in seconds, the uptime check is performed.

        Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#period GoogleMonitoringUptimeCheckConfig#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#project GoogleMonitoringUptimeCheckConfig#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_group(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigResourceGroup"]:
        '''resource_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#resource_group GoogleMonitoringUptimeCheckConfig#resource_group}
        '''
        result = self._values.get("resource_group")
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigResourceGroup"], result)

    @builtins.property
    def selected_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of regions from which the check will be run.

        Some regions contain one location, and others contain more than one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error message is returned. Not specifying this field will result in uptime checks running from all regions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#selected_regions GoogleMonitoringUptimeCheckConfig#selected_regions}
        '''
        result = self._values.get("selected_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tcp_check(self) -> typing.Optional["GoogleMonitoringUptimeCheckConfigTcpCheck"]:
        '''tcp_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#tcp_check GoogleMonitoringUptimeCheckConfig#tcp_check}
        '''
        result = self._values.get("tcp_check")
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigTcpCheck"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleMonitoringUptimeCheckConfigTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#timeouts GoogleMonitoringUptimeCheckConfig#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigContentMatchers",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "json_path_matcher": "jsonPathMatcher",
        "matcher": "matcher",
    },
)
class GoogleMonitoringUptimeCheckConfigContentMatchers:
    def __init__(
        self,
        *,
        content: builtins.str,
        json_path_matcher: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher", typing.Dict[str, typing.Any]]] = None,
        matcher: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: String or regex content to match (max 1024 bytes). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#content GoogleMonitoringUptimeCheckConfig#content}
        :param json_path_matcher: json_path_matcher block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#json_path_matcher GoogleMonitoringUptimeCheckConfig#json_path_matcher}
        :param matcher: The type of content matcher that will be applied to the server output, compared to the content string when the check is run. Default value: "CONTAINS_STRING" Possible values: ["CONTAINS_STRING", "NOT_CONTAINS_STRING", "MATCHES_REGEX", "NOT_MATCHES_REGEX", "MATCHES_JSON_PATH", "NOT_MATCHES_JSON_PATH"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#matcher GoogleMonitoringUptimeCheckConfig#matcher}
        '''
        if isinstance(json_path_matcher, dict):
            json_path_matcher = GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher(**json_path_matcher)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigContentMatchers.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument json_path_matcher", value=json_path_matcher, expected_type=type_hints["json_path_matcher"])
            check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if json_path_matcher is not None:
            self._values["json_path_matcher"] = json_path_matcher
        if matcher is not None:
            self._values["matcher"] = matcher

    @builtins.property
    def content(self) -> builtins.str:
        '''String or regex content to match (max 1024 bytes).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#content GoogleMonitoringUptimeCheckConfig#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def json_path_matcher(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher"]:
        '''json_path_matcher block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#json_path_matcher GoogleMonitoringUptimeCheckConfig#json_path_matcher}
        '''
        result = self._values.get("json_path_matcher")
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher"], result)

    @builtins.property
    def matcher(self) -> typing.Optional[builtins.str]:
        '''The type of content matcher that will be applied to the server output, compared to the content string when the check is run.

        Default value: "CONTAINS_STRING" Possible values: ["CONTAINS_STRING", "NOT_CONTAINS_STRING", "MATCHES_REGEX", "NOT_MATCHES_REGEX", "MATCHES_JSON_PATH", "NOT_MATCHES_JSON_PATH"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#matcher GoogleMonitoringUptimeCheckConfig#matcher}
        '''
        result = self._values.get("matcher")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigContentMatchers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher",
    jsii_struct_bases=[],
    name_mapping={"json_path": "jsonPath", "json_matcher": "jsonMatcher"},
)
class GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher:
    def __init__(
        self,
        *,
        json_path: builtins.str,
        json_matcher: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param json_path: JSONPath within the response output pointing to the expected 'ContentMatcher::content' to match against. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#json_path GoogleMonitoringUptimeCheckConfig#json_path}
        :param json_matcher: Options to perform JSONPath content matching. Default value: "EXACT_MATCH" Possible values: ["EXACT_MATCH", "REGEX_MATCH"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#json_matcher GoogleMonitoringUptimeCheckConfig#json_matcher}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher.__init__)
            check_type(argname="argument json_path", value=json_path, expected_type=type_hints["json_path"])
            check_type(argname="argument json_matcher", value=json_matcher, expected_type=type_hints["json_matcher"])
        self._values: typing.Dict[str, typing.Any] = {
            "json_path": json_path,
        }
        if json_matcher is not None:
            self._values["json_matcher"] = json_matcher

    @builtins.property
    def json_path(self) -> builtins.str:
        '''JSONPath within the response output pointing to the expected 'ContentMatcher::content' to match against.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#json_path GoogleMonitoringUptimeCheckConfig#json_path}
        '''
        result = self._values.get("json_path")
        assert result is not None, "Required property 'json_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def json_matcher(self) -> typing.Optional[builtins.str]:
        '''Options to perform JSONPath content matching. Default value: "EXACT_MATCH" Possible values: ["EXACT_MATCH", "REGEX_MATCH"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#json_matcher GoogleMonitoringUptimeCheckConfig#json_matcher}
        '''
        result = self._values.get("json_matcher")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetJsonMatcher")
    def reset_json_matcher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonMatcher", []))

    @builtins.property
    @jsii.member(jsii_name="jsonMatcherInput")
    def json_matcher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonMatcherInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonPathInput")
    def json_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonPathInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonMatcher")
    def json_matcher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonMatcher"))

    @json_matcher.setter
    def json_matcher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference, "json_matcher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonMatcher", value)

    @builtins.property
    @jsii.member(jsii_name="jsonPath")
    def json_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonPath"))

    @json_path.setter
    def json_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference, "json_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher]:
        return typing.cast(typing.Optional[GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringUptimeCheckConfigContentMatchersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigContentMatchersList",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigContentMatchersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigContentMatchersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringUptimeCheckConfigContentMatchers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringUptimeCheckConfigContentMatchers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringUptimeCheckConfigContentMatchers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putJsonPathMatcher")
    def put_json_path_matcher(
        self,
        *,
        json_path: builtins.str,
        json_matcher: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param json_path: JSONPath within the response output pointing to the expected 'ContentMatcher::content' to match against. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#json_path GoogleMonitoringUptimeCheckConfig#json_path}
        :param json_matcher: Options to perform JSONPath content matching. Default value: "EXACT_MATCH" Possible values: ["EXACT_MATCH", "REGEX_MATCH"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#json_matcher GoogleMonitoringUptimeCheckConfig#json_matcher}
        '''
        value = GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher(
            json_path=json_path, json_matcher=json_matcher
        )

        return typing.cast(None, jsii.invoke(self, "putJsonPathMatcher", [value]))

    @jsii.member(jsii_name="resetJsonPathMatcher")
    def reset_json_path_matcher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonPathMatcher", []))

    @jsii.member(jsii_name="resetMatcher")
    def reset_matcher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatcher", []))

    @builtins.property
    @jsii.member(jsii_name="jsonPathMatcher")
    def json_path_matcher(
        self,
    ) -> GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference:
        return typing.cast(GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference, jsii.get(self, "jsonPathMatcher"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonPathMatcherInput")
    def json_path_matcher_input(
        self,
    ) -> typing.Optional[GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher]:
        return typing.cast(typing.Optional[GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher], jsii.get(self, "jsonPathMatcherInput"))

    @builtins.property
    @jsii.member(jsii_name="matcherInput")
    def matcher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matcherInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="matcher")
    def matcher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matcher"))

    @matcher.setter
    def matcher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference, "matcher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matcher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigContentMatchers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigContentMatchers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigContentMatchers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigHttpCheck",
    jsii_struct_bases=[],
    name_mapping={
        "accepted_response_status_codes": "acceptedResponseStatusCodes",
        "auth_info": "authInfo",
        "body": "body",
        "content_type": "contentType",
        "headers": "headers",
        "mask_headers": "maskHeaders",
        "path": "path",
        "port": "port",
        "request_method": "requestMethod",
        "use_ssl": "useSsl",
        "validate_ssl": "validateSsl",
    },
)
class GoogleMonitoringUptimeCheckConfigHttpCheck:
    def __init__(
        self,
        *,
        accepted_response_status_codes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes", typing.Dict[str, typing.Any]]]]] = None,
        auth_info: typing.Optional[typing.Union["GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        mask_headers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        request_method: typing.Optional[builtins.str] = None,
        use_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        validate_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param accepted_response_status_codes: accepted_response_status_codes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#accepted_response_status_codes GoogleMonitoringUptimeCheckConfig#accepted_response_status_codes}
        :param auth_info: auth_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#auth_info GoogleMonitoringUptimeCheckConfig#auth_info}
        :param body: The request body associated with the HTTP POST request. If contentType is URL_ENCODED, the body passed in must be URL-encoded. Users can provide a Content-Length header via the headers field or the API will do so. If the requestMethod is GET and body is not empty, the API will return an error. The maximum byte size is 1 megabyte. Note - As with all bytes fields JSON representations are base64 encoded. e.g. "foo=bar" in URL-encoded form is "foo%3Dbar" and in base64 encoding is "Zm9vJTI1M0RiYXI=". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#body GoogleMonitoringUptimeCheckConfig#body}
        :param content_type: The content type to use for the check. Possible values: ["TYPE_UNSPECIFIED", "URL_ENCODED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#content_type GoogleMonitoringUptimeCheckConfig#content_type}
        :param headers: The list of headers to send as part of the uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at https://www.w3.org/Protocols/rfc2616/rfc2616.txt (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#headers GoogleMonitoringUptimeCheckConfig#headers}
        :param mask_headers: Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to True then the headers will be obscured with ******. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#mask_headers GoogleMonitoringUptimeCheckConfig#mask_headers}
        :param path: The path to the page to run the check against. Will be combined with the host (specified within the MonitoredResource) and port to construct the full URL. If the provided path does not begin with "/", a "/" will be prepended automatically. Optional (defaults to "/"). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#path GoogleMonitoringUptimeCheckConfig#path}
        :param port: The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) and path to construct the full URL. Optional (defaults to 80 without SSL, or 443 with SSL). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#port GoogleMonitoringUptimeCheckConfig#port}
        :param request_method: The HTTP request method to use for the check. If set to METHOD_UNSPECIFIED then requestMethod defaults to GET. Default value: "GET" Possible values: ["METHOD_UNSPECIFIED", "GET", "POST"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#request_method GoogleMonitoringUptimeCheckConfig#request_method}
        :param use_ssl: If true, use HTTPS instead of HTTP to run the check. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#use_ssl GoogleMonitoringUptimeCheckConfig#use_ssl}
        :param validate_ssl: Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where monitoredResource is set to uptime_url. If useSsl is false, setting validateSsl to true has no effect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#validate_ssl GoogleMonitoringUptimeCheckConfig#validate_ssl}
        '''
        if isinstance(auth_info, dict):
            auth_info = GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo(**auth_info)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheck.__init__)
            check_type(argname="argument accepted_response_status_codes", value=accepted_response_status_codes, expected_type=type_hints["accepted_response_status_codes"])
            check_type(argname="argument auth_info", value=auth_info, expected_type=type_hints["auth_info"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument mask_headers", value=mask_headers, expected_type=type_hints["mask_headers"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument request_method", value=request_method, expected_type=type_hints["request_method"])
            check_type(argname="argument use_ssl", value=use_ssl, expected_type=type_hints["use_ssl"])
            check_type(argname="argument validate_ssl", value=validate_ssl, expected_type=type_hints["validate_ssl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accepted_response_status_codes is not None:
            self._values["accepted_response_status_codes"] = accepted_response_status_codes
        if auth_info is not None:
            self._values["auth_info"] = auth_info
        if body is not None:
            self._values["body"] = body
        if content_type is not None:
            self._values["content_type"] = content_type
        if headers is not None:
            self._values["headers"] = headers
        if mask_headers is not None:
            self._values["mask_headers"] = mask_headers
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if request_method is not None:
            self._values["request_method"] = request_method
        if use_ssl is not None:
            self._values["use_ssl"] = use_ssl
        if validate_ssl is not None:
            self._values["validate_ssl"] = validate_ssl

    @builtins.property
    def accepted_response_status_codes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes"]]]:
        '''accepted_response_status_codes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#accepted_response_status_codes GoogleMonitoringUptimeCheckConfig#accepted_response_status_codes}
        '''
        result = self._values.get("accepted_response_status_codes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes"]]], result)

    @builtins.property
    def auth_info(
        self,
    ) -> typing.Optional["GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo"]:
        '''auth_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#auth_info GoogleMonitoringUptimeCheckConfig#auth_info}
        '''
        result = self._values.get("auth_info")
        return typing.cast(typing.Optional["GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo"], result)

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''The request body associated with the HTTP POST request.

        If contentType is URL_ENCODED, the body passed in must be URL-encoded. Users can provide a Content-Length header via the headers field or the API will do so. If the requestMethod is GET and body is not empty, the API will return an error. The maximum byte size is 1 megabyte. Note - As with all bytes fields JSON representations are base64 encoded. e.g. "foo=bar" in URL-encoded form is "foo%3Dbar" and in base64 encoding is "Zm9vJTI1M0RiYXI=".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#body GoogleMonitoringUptimeCheckConfig#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The content type to use for the check. Possible values: ["TYPE_UNSPECIFIED", "URL_ENCODED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#content_type GoogleMonitoringUptimeCheckConfig#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The list of headers to send as part of the uptime check request.

        If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at https://www.w3.org/Protocols/rfc2616/rfc2616.txt (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#headers GoogleMonitoringUptimeCheckConfig#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def mask_headers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean specifying whether to encrypt the header information.

        Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to True then the headers will be obscured with ******.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#mask_headers GoogleMonitoringUptimeCheckConfig#mask_headers}
        '''
        result = self._values.get("mask_headers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the page to run the check against.

        Will be combined with the host (specified within the MonitoredResource) and port to construct the full URL. If the provided path does not begin with "/", a "/" will be prepended automatically. Optional (defaults to "/").

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#path GoogleMonitoringUptimeCheckConfig#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port to the page to run the check against.

        Will be combined with host (specified within the MonitoredResource) and path to construct the full URL. Optional (defaults to 80 without SSL, or 443 with SSL).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#port GoogleMonitoringUptimeCheckConfig#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def request_method(self) -> typing.Optional[builtins.str]:
        '''The HTTP request method to use for the check.

        If set to METHOD_UNSPECIFIED then requestMethod defaults to GET. Default value: "GET" Possible values: ["METHOD_UNSPECIFIED", "GET", "POST"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#request_method GoogleMonitoringUptimeCheckConfig#request_method}
        '''
        result = self._values.get("request_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, use HTTPS instead of HTTP to run the check.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#use_ssl GoogleMonitoringUptimeCheckConfig#use_ssl}
        '''
        result = self._values.get("use_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def validate_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Boolean specifying whether to include SSL certificate validation as a part of the Uptime check.

        Only applies to checks where monitoredResource is set to uptime_url. If useSsl is false, setting validateSsl to true has no effect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#validate_ssl GoogleMonitoringUptimeCheckConfig#validate_ssl}
        '''
        result = self._values.get("validate_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigHttpCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes",
    jsii_struct_bases=[],
    name_mapping={"status_class": "statusClass", "status_value": "statusValue"},
)
class GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes:
    def __init__(
        self,
        *,
        status_class: typing.Optional[builtins.str] = None,
        status_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param status_class: A class of status codes to accept. Possible values: ["STATUS_CLASS_1XX", "STATUS_CLASS_2XX", "STATUS_CLASS_3XX", "STATUS_CLASS_4XX", "STATUS_CLASS_5XX", "STATUS_CLASS_ANY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#status_class GoogleMonitoringUptimeCheckConfig#status_class}
        :param status_value: A status code to accept. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#status_value GoogleMonitoringUptimeCheckConfig#status_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes.__init__)
            check_type(argname="argument status_class", value=status_class, expected_type=type_hints["status_class"])
            check_type(argname="argument status_value", value=status_value, expected_type=type_hints["status_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if status_class is not None:
            self._values["status_class"] = status_class
        if status_value is not None:
            self._values["status_value"] = status_value

    @builtins.property
    def status_class(self) -> typing.Optional[builtins.str]:
        '''A class of status codes to accept. Possible values: ["STATUS_CLASS_1XX", "STATUS_CLASS_2XX", "STATUS_CLASS_3XX", "STATUS_CLASS_4XX", "STATUS_CLASS_5XX", "STATUS_CLASS_ANY"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#status_class GoogleMonitoringUptimeCheckConfig#status_class}
        '''
        result = self._values.get("status_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_value(self) -> typing.Optional[jsii.Number]:
        '''A status code to accept.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#status_value GoogleMonitoringUptimeCheckConfig#status_value}
        '''
        result = self._values.get("status_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetStatusClass")
    def reset_status_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusClass", []))

    @jsii.member(jsii_name="resetStatusValue")
    def reset_status_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusValue", []))

    @builtins.property
    @jsii.member(jsii_name="statusClassInput")
    def status_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusClassInput"))

    @builtins.property
    @jsii.member(jsii_name="statusValueInput")
    def status_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusValueInput"))

    @builtins.property
    @jsii.member(jsii_name="statusClass")
    def status_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusClass"))

    @status_class.setter
    def status_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference, "status_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusClass", value)

    @builtins.property
    @jsii.member(jsii_name="statusValue")
    def status_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusValue"))

    @status_value.setter
    def status_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference, "status_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: The password to authenticate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#password GoogleMonitoringUptimeCheckConfig#password}
        :param username: The username to authenticate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#username GoogleMonitoringUptimeCheckConfig#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''The password to authenticate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#password GoogleMonitoringUptimeCheckConfig#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The username to authenticate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#username GoogleMonitoringUptimeCheckConfig#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo]:
        return typing.cast(typing.Optional[GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAcceptedResponseStatusCodes")
    def put_accepted_response_status_codes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference.put_accepted_response_status_codes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAcceptedResponseStatusCodes", [value]))

    @jsii.member(jsii_name="putAuthInfo")
    def put_auth_info(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: The password to authenticate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#password GoogleMonitoringUptimeCheckConfig#password}
        :param username: The username to authenticate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#username GoogleMonitoringUptimeCheckConfig#username}
        '''
        value = GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putAuthInfo", [value]))

    @jsii.member(jsii_name="resetAcceptedResponseStatusCodes")
    def reset_accepted_response_status_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceptedResponseStatusCodes", []))

    @jsii.member(jsii_name="resetAuthInfo")
    def reset_auth_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthInfo", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetMaskHeaders")
    def reset_mask_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaskHeaders", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetRequestMethod")
    def reset_request_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMethod", []))

    @jsii.member(jsii_name="resetUseSsl")
    def reset_use_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseSsl", []))

    @jsii.member(jsii_name="resetValidateSsl")
    def reset_validate_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateSsl", []))

    @builtins.property
    @jsii.member(jsii_name="acceptedResponseStatusCodes")
    def accepted_response_status_codes(
        self,
    ) -> GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList:
        return typing.cast(GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList, jsii.get(self, "acceptedResponseStatusCodes"))

    @builtins.property
    @jsii.member(jsii_name="authInfo")
    def auth_info(
        self,
    ) -> GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference:
        return typing.cast(GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference, jsii.get(self, "authInfo"))

    @builtins.property
    @jsii.member(jsii_name="acceptedResponseStatusCodesInput")
    def accepted_response_status_codes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes]]], jsii.get(self, "acceptedResponseStatusCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="authInfoInput")
    def auth_info_input(
        self,
    ) -> typing.Optional[GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo]:
        return typing.cast(typing.Optional[GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo], jsii.get(self, "authInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="maskHeadersInput")
    def mask_headers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "maskHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMethodInput")
    def request_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="useSslInput")
    def use_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useSslInput"))

    @builtins.property
    @jsii.member(jsii_name="validateSslInput")
    def validate_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "validateSslInput"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="maskHeaders")
    def mask_headers(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "maskHeaders"))

    @mask_headers.setter
    def mask_headers(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "mask_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maskHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="requestMethod")
    def request_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestMethod"))

    @request_method.setter
    def request_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "request_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMethod", value)

    @builtins.property
    @jsii.member(jsii_name="useSsl")
    def use_ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useSsl"))

    @use_ssl.setter
    def use_ssl(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "use_ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useSsl", value)

    @builtins.property
    @jsii.member(jsii_name="validateSsl")
    def validate_ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "validateSsl"))

    @validate_ssl.setter
    def validate_ssl(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "validate_ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validateSsl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringUptimeCheckConfigHttpCheck]:
        return typing.cast(typing.Optional[GoogleMonitoringUptimeCheckConfigHttpCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringUptimeCheckConfigHttpCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigMonitoredResource",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels", "type": "type"},
)
class GoogleMonitoringUptimeCheckConfigMonitoredResource:
    def __init__(
        self,
        *,
        labels: typing.Mapping[builtins.str, builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param labels: Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels "project_id", "instance_id", and "zone". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#labels GoogleMonitoringUptimeCheckConfig#labels}
        :param type: The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor) object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (https://cloud.google.com/monitoring/api/resources) and Logging resource types (https://cloud.google.com/logging/docs/api/v2/resource-list). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#type GoogleMonitoringUptimeCheckConfig#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigMonitoredResource.__init__)
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "labels": labels,
            "type": type,
        }

    @builtins.property
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Values for all of the labels listed in the associated monitored resource descriptor.

        For example, Compute Engine VM instances use the labels "project_id", "instance_id", and "zone".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#labels GoogleMonitoringUptimeCheckConfig#labels}
        '''
        result = self._values.get("labels")
        assert result is not None, "Required property 'labels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The monitored resource type.

        This field must match the type field of a MonitoredResourceDescriptor (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor) object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (https://cloud.google.com/monitoring/api/resources) and Logging resource types (https://cloud.google.com/logging/docs/api/v2/resource-list).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#type GoogleMonitoringUptimeCheckConfig#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigMonitoredResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringUptimeCheckConfigMonitoredResource]:
        return typing.cast(typing.Optional[GoogleMonitoringUptimeCheckConfigMonitoredResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringUptimeCheckConfigMonitoredResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigResourceGroup",
    jsii_struct_bases=[],
    name_mapping={"group_id": "groupId", "resource_type": "resourceType"},
)
class GoogleMonitoringUptimeCheckConfigResourceGroup:
    def __init__(
        self,
        *,
        group_id: typing.Optional[builtins.str] = None,
        resource_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group_id: The group of resources being monitored. Should be the 'name' of a group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#group_id GoogleMonitoringUptimeCheckConfig#group_id}
        :param resource_type: The resource type of the group members. Possible values: ["RESOURCE_TYPE_UNSPECIFIED", "INSTANCE", "AWS_ELB_LOAD_BALANCER"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#resource_type GoogleMonitoringUptimeCheckConfig#resource_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigResourceGroup.__init__)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if group_id is not None:
            self._values["group_id"] = group_id
        if resource_type is not None:
            self._values["resource_type"] = resource_type

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''The group of resources being monitored. Should be the 'name' of a group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#group_id GoogleMonitoringUptimeCheckConfig#group_id}
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The resource type of the group members. Possible values: ["RESOURCE_TYPE_UNSPECIFIED", "INSTANCE", "AWS_ELB_LOAD_BALANCER"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#resource_type GoogleMonitoringUptimeCheckConfig#resource_type}
        '''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigResourceGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetResourceType")
    def reset_resource_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceType", []))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference, "resource_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringUptimeCheckConfigResourceGroup]:
        return typing.cast(typing.Optional[GoogleMonitoringUptimeCheckConfigResourceGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringUptimeCheckConfigResourceGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigTcpCheck",
    jsii_struct_bases=[],
    name_mapping={"port": "port"},
)
class GoogleMonitoringUptimeCheckConfigTcpCheck:
    def __init__(self, *, port: jsii.Number) -> None:
        '''
        :param port: The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#port GoogleMonitoringUptimeCheckConfig#port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigTcpCheck.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
        }

    @builtins.property
    def port(self) -> jsii.Number:
        '''The port to the page to run the check against.

        Will be combined with host (specified within the MonitoredResource) to construct the full URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#port GoogleMonitoringUptimeCheckConfig#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigTcpCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringUptimeCheckConfigTcpCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigTcpCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigTcpCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigTcpCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringUptimeCheckConfigTcpCheck]:
        return typing.cast(typing.Optional[GoogleMonitoringUptimeCheckConfigTcpCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringUptimeCheckConfigTcpCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigTcpCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleMonitoringUptimeCheckConfigTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#create GoogleMonitoringUptimeCheckConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#delete GoogleMonitoringUptimeCheckConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#update GoogleMonitoringUptimeCheckConfig#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#create GoogleMonitoringUptimeCheckConfig#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#delete GoogleMonitoringUptimeCheckConfig#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_uptime_check_config#update GoogleMonitoringUptimeCheckConfig#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringUptimeCheckConfigTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringUptimeCheckConfig.GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringUptimeCheckConfigTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleMonitoringUptimeCheckConfig",
    "GoogleMonitoringUptimeCheckConfigConfig",
    "GoogleMonitoringUptimeCheckConfigContentMatchers",
    "GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcher",
    "GoogleMonitoringUptimeCheckConfigContentMatchersJsonPathMatcherOutputReference",
    "GoogleMonitoringUptimeCheckConfigContentMatchersList",
    "GoogleMonitoringUptimeCheckConfigContentMatchersOutputReference",
    "GoogleMonitoringUptimeCheckConfigHttpCheck",
    "GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodes",
    "GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesList",
    "GoogleMonitoringUptimeCheckConfigHttpCheckAcceptedResponseStatusCodesOutputReference",
    "GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfo",
    "GoogleMonitoringUptimeCheckConfigHttpCheckAuthInfoOutputReference",
    "GoogleMonitoringUptimeCheckConfigHttpCheckOutputReference",
    "GoogleMonitoringUptimeCheckConfigMonitoredResource",
    "GoogleMonitoringUptimeCheckConfigMonitoredResourceOutputReference",
    "GoogleMonitoringUptimeCheckConfigResourceGroup",
    "GoogleMonitoringUptimeCheckConfigResourceGroupOutputReference",
    "GoogleMonitoringUptimeCheckConfigTcpCheck",
    "GoogleMonitoringUptimeCheckConfigTcpCheckOutputReference",
    "GoogleMonitoringUptimeCheckConfigTimeouts",
    "GoogleMonitoringUptimeCheckConfigTimeoutsOutputReference",
]

publication.publish()
