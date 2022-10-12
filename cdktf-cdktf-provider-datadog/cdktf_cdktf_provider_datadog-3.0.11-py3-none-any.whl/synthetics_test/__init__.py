'''
# `datadog_synthetics_test`

Refer to the Terraform Registory for docs: [`datadog_synthetics_test`](https://www.terraform.io/docs/providers/datadog/r/synthetics_test).
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


class SyntheticsTest(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTest",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test datadog_synthetics_test}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        locations: typing.Sequence[builtins.str],
        name: builtins.str,
        status: builtins.str,
        type: builtins.str,
        api_step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestApiStep", typing.Dict[str, typing.Any]]]]] = None,
        assertion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestAssertion", typing.Dict[str, typing.Any]]]]] = None,
        browser_step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestBrowserStep", typing.Dict[str, typing.Any]]]]] = None,
        browser_variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestBrowserVariable", typing.Dict[str, typing.Any]]]]] = None,
        config_variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestConfigVariable", typing.Dict[str, typing.Any]]]]] = None,
        device_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        options_list: typing.Optional[typing.Union["SyntheticsTestOptionsList", typing.Dict[str, typing.Any]]] = None,
        request_basicauth: typing.Optional[typing.Union["SyntheticsTestRequestBasicauth", typing.Dict[str, typing.Any]]] = None,
        request_client_certificate: typing.Optional[typing.Union["SyntheticsTestRequestClientCertificate", typing.Dict[str, typing.Any]]] = None,
        request_definition: typing.Optional[typing.Union["SyntheticsTestRequestDefinition", typing.Dict[str, typing.Any]]] = None,
        request_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_proxy: typing.Optional[typing.Union["SyntheticsTestRequestProxy", typing.Dict[str, typing.Any]]] = None,
        request_query: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        set_cookie: typing.Optional[builtins.str] = None,
        subtype: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test datadog_synthetics_test} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param locations: Array of locations used to run the test. Refer to `the Datadog Synthetics location data source <https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/synthetics_locations>`_ to retrieve the list of locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#locations SyntheticsTest#locations}
        :param name: Name of Datadog synthetics test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        :param status: Define whether you want to start (``live``) or pause (``paused``) a Synthetic test. Valid values are ``live``, ``paused``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#status SyntheticsTest#status}
        :param type: Synthetics test type. Valid values are ``api``, ``browser``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param api_step: api_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#api_step SyntheticsTest#api_step}
        :param assertion: assertion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#assertion SyntheticsTest#assertion}
        :param browser_step: browser_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#browser_step SyntheticsTest#browser_step}
        :param browser_variable: browser_variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#browser_variable SyntheticsTest#browser_variable}
        :param config_variable: config_variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#config_variable SyntheticsTest#config_variable}
        :param device_ids: Required if ``type = "browser"``. Array with the different device IDs used to run the test. Valid values are ``laptop_large``, ``tablet``, ``mobile_small``, ``chrome.laptop_large``, ``chrome.tablet``, ``chrome.mobile_small``, ``firefox.laptop_large``, ``firefox.tablet``, ``firefox.mobile_small``, ``edge.laptop_large``, ``edge.tablet``, ``edge.mobile_small``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#device_ids SyntheticsTest#device_ids}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#id SyntheticsTest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param message: A message to include with notifications for this synthetics test. Email notifications can be sent to specific users by using the same ``@username`` notation as events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        :param options_list: options_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#options_list SyntheticsTest#options_list}
        :param request_basicauth: request_basicauth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_basicauth SyntheticsTest#request_basicauth}
        :param request_client_certificate: request_client_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_client_certificate SyntheticsTest#request_client_certificate}
        :param request_definition: request_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_definition SyntheticsTest#request_definition}
        :param request_headers: Header name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_headers SyntheticsTest#request_headers}
        :param request_proxy: request_proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_proxy SyntheticsTest#request_proxy}
        :param request_query: Query arguments name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_query SyntheticsTest#request_query}
        :param set_cookie: Cookies to be used for a browser test request, using the `Set-Cookie <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie>`_ syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#set_cookie SyntheticsTest#set_cookie}
        :param subtype: The subtype of the Synthetic API test. Defaults to ``http``. Valid values are ``http``, ``ssl``, ``tcp``, ``dns``, ``multi``, ``icmp``, ``udp``, ``websocket``, ``grpc``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#subtype SyntheticsTest#subtype}
        :param tags: A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI. Default is an empty list (``[]``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#tags SyntheticsTest#tags}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTest.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SyntheticsTestConfig(
            locations=locations,
            name=name,
            status=status,
            type=type,
            api_step=api_step,
            assertion=assertion,
            browser_step=browser_step,
            browser_variable=browser_variable,
            config_variable=config_variable,
            device_ids=device_ids,
            id=id,
            message=message,
            options_list=options_list,
            request_basicauth=request_basicauth,
            request_client_certificate=request_client_certificate,
            request_definition=request_definition,
            request_headers=request_headers,
            request_proxy=request_proxy,
            request_query=request_query,
            set_cookie=set_cookie,
            subtype=subtype,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApiStep")
    def put_api_step(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestApiStep", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTest.put_api_step)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApiStep", [value]))

    @jsii.member(jsii_name="putAssertion")
    def put_assertion(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestAssertion", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTest.put_assertion)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssertion", [value]))

    @jsii.member(jsii_name="putBrowserStep")
    def put_browser_step(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestBrowserStep", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTest.put_browser_step)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBrowserStep", [value]))

    @jsii.member(jsii_name="putBrowserVariable")
    def put_browser_variable(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestBrowserVariable", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTest.put_browser_variable)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBrowserVariable", [value]))

    @jsii.member(jsii_name="putConfigVariable")
    def put_config_variable(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestConfigVariable", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTest.put_config_variable)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigVariable", [value]))

    @jsii.member(jsii_name="putOptionsList")
    def put_options_list(
        self,
        *,
        tick_every: jsii.Number,
        accept_self_signed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_certificate_revocation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ci: typing.Optional[typing.Union["SyntheticsTestOptionsListCi", typing.Dict[str, typing.Any]]] = None,
        disable_csp: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        follow_redirects: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ignore_server_certificate_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        initial_navigation_timeout: typing.Optional[jsii.Number] = None,
        min_failure_duration: typing.Optional[jsii.Number] = None,
        min_location_failed: typing.Optional[jsii.Number] = None,
        monitor_name: typing.Optional[builtins.str] = None,
        monitor_options: typing.Optional[typing.Union["SyntheticsTestOptionsListMonitorOptions", typing.Dict[str, typing.Any]]] = None,
        monitor_priority: typing.Optional[jsii.Number] = None,
        no_screenshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restricted_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        retry: typing.Optional[typing.Union["SyntheticsTestOptionsListRetry", typing.Dict[str, typing.Any]]] = None,
        rum_settings: typing.Optional[typing.Union["SyntheticsTestOptionsListRumSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tick_every: How often the test should run (in seconds). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#tick_every SyntheticsTest#tick_every}
        :param accept_self_signed: For SSL test, whether or not the test should allow self signed certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#accept_self_signed SyntheticsTest#accept_self_signed}
        :param allow_insecure: Allows loading insecure content for an HTTP test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_insecure SyntheticsTest#allow_insecure}
        :param check_certificate_revocation: For SSL test, whether or not the test should fail on revoked certificate in stapled OCSP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#check_certificate_revocation SyntheticsTest#check_certificate_revocation}
        :param ci: ci block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#ci SyntheticsTest#ci}
        :param disable_csp: Disable Content Security Policy for browser tests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#disable_csp SyntheticsTest#disable_csp}
        :param follow_redirects: Determines whether or not the API HTTP test should follow redirects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#follow_redirects SyntheticsTest#follow_redirects}
        :param ignore_server_certificate_error: Ignore server certificate error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#ignore_server_certificate_error SyntheticsTest#ignore_server_certificate_error}
        :param initial_navigation_timeout: Timeout before declaring the initial step as failed (in seconds) for browser tests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#initial_navigation_timeout SyntheticsTest#initial_navigation_timeout}
        :param min_failure_duration: Minimum amount of time in failure required to trigger an alert. Default is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#min_failure_duration SyntheticsTest#min_failure_duration}
        :param min_location_failed: Minimum number of locations in failure required to trigger an alert. Default is ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#min_location_failed SyntheticsTest#min_location_failed}
        :param monitor_name: The monitor name is used for the alert title as well as for all monitor dashboard widgets and SLOs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_name SyntheticsTest#monitor_name}
        :param monitor_options: monitor_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_options SyntheticsTest#monitor_options}
        :param monitor_priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_priority SyntheticsTest#monitor_priority}.
        :param no_screenshot: Prevents saving screenshots of the steps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_screenshot SyntheticsTest#no_screenshot}
        :param restricted_roles: A list of role identifiers pulled from the Roles API to restrict read and write access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#restricted_roles SyntheticsTest#restricted_roles}
        :param retry: retry block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#retry SyntheticsTest#retry}
        :param rum_settings: rum_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#rum_settings SyntheticsTest#rum_settings}
        '''
        value = SyntheticsTestOptionsList(
            tick_every=tick_every,
            accept_self_signed=accept_self_signed,
            allow_insecure=allow_insecure,
            check_certificate_revocation=check_certificate_revocation,
            ci=ci,
            disable_csp=disable_csp,
            follow_redirects=follow_redirects,
            ignore_server_certificate_error=ignore_server_certificate_error,
            initial_navigation_timeout=initial_navigation_timeout,
            min_failure_duration=min_failure_duration,
            min_location_failed=min_location_failed,
            monitor_name=monitor_name,
            monitor_options=monitor_options,
            monitor_priority=monitor_priority,
            no_screenshot=no_screenshot,
            restricted_roles=restricted_roles,
            retry=retry,
            rum_settings=rum_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putOptionsList", [value]))

    @jsii.member(jsii_name="putRequestBasicauth")
    def put_request_basicauth(
        self,
        *,
        access_key: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        service_name: typing.Optional[builtins.str] = None,
        session_token: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        workstation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_key: Access key for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#access_key SyntheticsTest#access_key}
        :param domain: Domain for ``ntlm`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#domain SyntheticsTest#domain}
        :param password: Password for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#password SyntheticsTest#password}
        :param region: Region for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#region SyntheticsTest#region}
        :param secret_key: Secret key for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#secret_key SyntheticsTest#secret_key}
        :param service_name: Service name for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service_name SyntheticsTest#service_name}
        :param session_token: Session token for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#session_token SyntheticsTest#session_token}
        :param type: Type of basic authentication to use when performing the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param username: Username for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#username SyntheticsTest#username}
        :param workstation: Workstation for ``ntlm`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#workstation SyntheticsTest#workstation}
        '''
        value = SyntheticsTestRequestBasicauth(
            access_key=access_key,
            domain=domain,
            password=password,
            region=region,
            secret_key=secret_key,
            service_name=service_name,
            session_token=session_token,
            type=type,
            username=username,
            workstation=workstation,
        )

        return typing.cast(None, jsii.invoke(self, "putRequestBasicauth", [value]))

    @jsii.member(jsii_name="putRequestClientCertificate")
    def put_request_client_certificate(
        self,
        *,
        cert: typing.Union["SyntheticsTestRequestClientCertificateCert", typing.Dict[str, typing.Any]],
        key: typing.Union["SyntheticsTestRequestClientCertificateKey", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param cert: cert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#cert SyntheticsTest#cert}
        :param key: key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#key SyntheticsTest#key}
        '''
        value = SyntheticsTestRequestClientCertificate(cert=cert, key=key)

        return typing.cast(None, jsii.invoke(self, "putRequestClientCertificate", [value]))

    @jsii.member(jsii_name="putRequestDefinition")
    def put_request_definition(
        self,
        *,
        body: typing.Optional[builtins.str] = None,
        certificate_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_server: typing.Optional[builtins.str] = None,
        dns_server_port: typing.Optional[jsii.Number] = None,
        host: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        method: typing.Optional[builtins.str] = None,
        no_saving_response_body: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        number_of_packets: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        servername: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        should_track_hops: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param body: The request body. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#body SyntheticsTest#body}
        :param certificate_domains: By default, the client certificate is applied on the domain of the starting URL for browser tests. If you want your client certificate to be applied on other domains instead, add them in ``certificate_domains``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#certificate_domains SyntheticsTest#certificate_domains}
        :param dns_server: DNS server to use for DNS tests (``subtype = "dns"``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server SyntheticsTest#dns_server}
        :param dns_server_port: DNS server port to use for DNS tests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server_port SyntheticsTest#dns_server_port}
        :param host: Host name to perform the test with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#host SyntheticsTest#host}
        :param message: For UDP and websocket tests, message to send with the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        :param method: The HTTP method. Valid values are ``GET``, ``POST``, ``PATCH``, ``PUT``, ``DELETE``, ``HEAD``, ``OPTIONS``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#method SyntheticsTest#method}
        :param no_saving_response_body: Determines whether or not to save the response body. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_saving_response_body SyntheticsTest#no_saving_response_body}
        :param number_of_packets: Number of pings to use per test for ICMP tests (``subtype = "icmp"``) between 0 and 10. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#number_of_packets SyntheticsTest#number_of_packets}
        :param port: Port to use when performing the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#port SyntheticsTest#port}
        :param servername: For SSL tests, it specifies on which server you want to initiate the TLS handshake, allowing the server to present one of multiple possible certificates on the same IP address and TCP port number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#servername SyntheticsTest#servername}
        :param service: For gRPC tests, service to target for healthcheck. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service SyntheticsTest#service}
        :param should_track_hops: This will turn on a traceroute probe to discover all gateways along the path to the host destination. For ICMP tests (``subtype = "icmp"``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#should_track_hops SyntheticsTest#should_track_hops}
        :param timeout: Timeout in seconds for the test. Defaults to ``60``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#timeout SyntheticsTest#timeout}
        :param url: The URL to send the request to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        '''
        value = SyntheticsTestRequestDefinition(
            body=body,
            certificate_domains=certificate_domains,
            dns_server=dns_server,
            dns_server_port=dns_server_port,
            host=host,
            message=message,
            method=method,
            no_saving_response_body=no_saving_response_body,
            number_of_packets=number_of_packets,
            port=port,
            servername=servername,
            service=service,
            should_track_hops=should_track_hops,
            timeout=timeout,
            url=url,
        )

        return typing.cast(None, jsii.invoke(self, "putRequestDefinition", [value]))

    @jsii.member(jsii_name="putRequestProxy")
    def put_request_proxy(
        self,
        *,
        url: builtins.str,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: URL of the proxy to perform the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        :param headers: Header name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#headers SyntheticsTest#headers}
        '''
        value = SyntheticsTestRequestProxy(url=url, headers=headers)

        return typing.cast(None, jsii.invoke(self, "putRequestProxy", [value]))

    @jsii.member(jsii_name="resetApiStep")
    def reset_api_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiStep", []))

    @jsii.member(jsii_name="resetAssertion")
    def reset_assertion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssertion", []))

    @jsii.member(jsii_name="resetBrowserStep")
    def reset_browser_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserStep", []))

    @jsii.member(jsii_name="resetBrowserVariable")
    def reset_browser_variable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserVariable", []))

    @jsii.member(jsii_name="resetConfigVariable")
    def reset_config_variable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigVariable", []))

    @jsii.member(jsii_name="resetDeviceIds")
    def reset_device_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceIds", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetOptionsList")
    def reset_options_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionsList", []))

    @jsii.member(jsii_name="resetRequestBasicauth")
    def reset_request_basicauth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestBasicauth", []))

    @jsii.member(jsii_name="resetRequestClientCertificate")
    def reset_request_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestClientCertificate", []))

    @jsii.member(jsii_name="resetRequestDefinition")
    def reset_request_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestDefinition", []))

    @jsii.member(jsii_name="resetRequestHeaders")
    def reset_request_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeaders", []))

    @jsii.member(jsii_name="resetRequestProxy")
    def reset_request_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestProxy", []))

    @jsii.member(jsii_name="resetRequestQuery")
    def reset_request_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestQuery", []))

    @jsii.member(jsii_name="resetSetCookie")
    def reset_set_cookie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetCookie", []))

    @jsii.member(jsii_name="resetSubtype")
    def reset_subtype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubtype", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="apiStep")
    def api_step(self) -> "SyntheticsTestApiStepList":
        return typing.cast("SyntheticsTestApiStepList", jsii.get(self, "apiStep"))

    @builtins.property
    @jsii.member(jsii_name="assertion")
    def assertion(self) -> "SyntheticsTestAssertionList":
        return typing.cast("SyntheticsTestAssertionList", jsii.get(self, "assertion"))

    @builtins.property
    @jsii.member(jsii_name="browserStep")
    def browser_step(self) -> "SyntheticsTestBrowserStepList":
        return typing.cast("SyntheticsTestBrowserStepList", jsii.get(self, "browserStep"))

    @builtins.property
    @jsii.member(jsii_name="browserVariable")
    def browser_variable(self) -> "SyntheticsTestBrowserVariableList":
        return typing.cast("SyntheticsTestBrowserVariableList", jsii.get(self, "browserVariable"))

    @builtins.property
    @jsii.member(jsii_name="configVariable")
    def config_variable(self) -> "SyntheticsTestConfigVariableList":
        return typing.cast("SyntheticsTestConfigVariableList", jsii.get(self, "configVariable"))

    @builtins.property
    @jsii.member(jsii_name="monitorId")
    def monitor_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monitorId"))

    @builtins.property
    @jsii.member(jsii_name="optionsList")
    def options_list(self) -> "SyntheticsTestOptionsListOutputReference":
        return typing.cast("SyntheticsTestOptionsListOutputReference", jsii.get(self, "optionsList"))

    @builtins.property
    @jsii.member(jsii_name="requestBasicauth")
    def request_basicauth(self) -> "SyntheticsTestRequestBasicauthOutputReference":
        return typing.cast("SyntheticsTestRequestBasicauthOutputReference", jsii.get(self, "requestBasicauth"))

    @builtins.property
    @jsii.member(jsii_name="requestClientCertificate")
    def request_client_certificate(
        self,
    ) -> "SyntheticsTestRequestClientCertificateOutputReference":
        return typing.cast("SyntheticsTestRequestClientCertificateOutputReference", jsii.get(self, "requestClientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="requestDefinition")
    def request_definition(self) -> "SyntheticsTestRequestDefinitionOutputReference":
        return typing.cast("SyntheticsTestRequestDefinitionOutputReference", jsii.get(self, "requestDefinition"))

    @builtins.property
    @jsii.member(jsii_name="requestProxy")
    def request_proxy(self) -> "SyntheticsTestRequestProxyOutputReference":
        return typing.cast("SyntheticsTestRequestProxyOutputReference", jsii.get(self, "requestProxy"))

    @builtins.property
    @jsii.member(jsii_name="apiStepInput")
    def api_step_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestApiStep"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestApiStep"]]], jsii.get(self, "apiStepInput"))

    @builtins.property
    @jsii.member(jsii_name="assertionInput")
    def assertion_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestAssertion"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestAssertion"]]], jsii.get(self, "assertionInput"))

    @builtins.property
    @jsii.member(jsii_name="browserStepInput")
    def browser_step_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestBrowserStep"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestBrowserStep"]]], jsii.get(self, "browserStepInput"))

    @builtins.property
    @jsii.member(jsii_name="browserVariableInput")
    def browser_variable_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestBrowserVariable"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestBrowserVariable"]]], jsii.get(self, "browserVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="configVariableInput")
    def config_variable_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestConfigVariable"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestConfigVariable"]]], jsii.get(self, "configVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceIdsInput")
    def device_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deviceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationsInput")
    def locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsListInput")
    def options_list_input(self) -> typing.Optional["SyntheticsTestOptionsList"]:
        return typing.cast(typing.Optional["SyntheticsTestOptionsList"], jsii.get(self, "optionsListInput"))

    @builtins.property
    @jsii.member(jsii_name="requestBasicauthInput")
    def request_basicauth_input(
        self,
    ) -> typing.Optional["SyntheticsTestRequestBasicauth"]:
        return typing.cast(typing.Optional["SyntheticsTestRequestBasicauth"], jsii.get(self, "requestBasicauthInput"))

    @builtins.property
    @jsii.member(jsii_name="requestClientCertificateInput")
    def request_client_certificate_input(
        self,
    ) -> typing.Optional["SyntheticsTestRequestClientCertificate"]:
        return typing.cast(typing.Optional["SyntheticsTestRequestClientCertificate"], jsii.get(self, "requestClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="requestDefinitionInput")
    def request_definition_input(
        self,
    ) -> typing.Optional["SyntheticsTestRequestDefinition"]:
        return typing.cast(typing.Optional["SyntheticsTestRequestDefinition"], jsii.get(self, "requestDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersInput")
    def request_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="requestProxyInput")
    def request_proxy_input(self) -> typing.Optional["SyntheticsTestRequestProxy"]:
        return typing.cast(typing.Optional["SyntheticsTestRequestProxy"], jsii.get(self, "requestProxyInput"))

    @builtins.property
    @jsii.member(jsii_name="requestQueryInput")
    def request_query_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="setCookieInput")
    def set_cookie_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "setCookieInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="subtypeInput")
    def subtype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceIds")
    def device_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deviceIds"))

    @device_ids.setter
    def device_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "device_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceIds", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "locations"))

    @locations.setter
    def locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="requestHeaders")
    def request_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestHeaders"))

    @request_headers.setter
    def request_headers(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "request_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="requestQuery")
    def request_query(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestQuery"))

    @request_query.setter
    def request_query(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "request_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestQuery", value)

    @builtins.property
    @jsii.member(jsii_name="setCookie")
    def set_cookie(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "setCookie"))

    @set_cookie.setter
    def set_cookie(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "set_cookie").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setCookie", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="subtype")
    def subtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subtype"))

    @subtype.setter
    def subtype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "subtype").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subtype", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTest, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStep",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allow_failure": "allowFailure",
        "assertion": "assertion",
        "extracted_value": "extractedValue",
        "is_critical": "isCritical",
        "request_basicauth": "requestBasicauth",
        "request_client_certificate": "requestClientCertificate",
        "request_definition": "requestDefinition",
        "request_headers": "requestHeaders",
        "request_proxy": "requestProxy",
        "request_query": "requestQuery",
        "retry": "retry",
        "subtype": "subtype",
    },
)
class SyntheticsTestApiStep:
    def __init__(
        self,
        *,
        name: builtins.str,
        allow_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        assertion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestApiStepAssertion", typing.Dict[str, typing.Any]]]]] = None,
        extracted_value: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestApiStepExtractedValue", typing.Dict[str, typing.Any]]]]] = None,
        is_critical: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        request_basicauth: typing.Optional[typing.Union["SyntheticsTestApiStepRequestBasicauth", typing.Dict[str, typing.Any]]] = None,
        request_client_certificate: typing.Optional[typing.Union["SyntheticsTestApiStepRequestClientCertificate", typing.Dict[str, typing.Any]]] = None,
        request_definition: typing.Optional[typing.Union["SyntheticsTestApiStepRequestDefinition", typing.Dict[str, typing.Any]]] = None,
        request_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_proxy: typing.Optional[typing.Union["SyntheticsTestApiStepRequestProxy", typing.Dict[str, typing.Any]]] = None,
        request_query: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        retry: typing.Optional[typing.Union["SyntheticsTestApiStepRetry", typing.Dict[str, typing.Any]]] = None,
        subtype: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        :param allow_failure: Determines whether or not to continue with test if this step fails. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_failure SyntheticsTest#allow_failure}
        :param assertion: assertion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#assertion SyntheticsTest#assertion}
        :param extracted_value: extracted_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#extracted_value SyntheticsTest#extracted_value}
        :param is_critical: Determines whether or not to consider the entire test as failed if this step fails. Can be used only if ``allow_failure`` is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#is_critical SyntheticsTest#is_critical}
        :param request_basicauth: request_basicauth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_basicauth SyntheticsTest#request_basicauth}
        :param request_client_certificate: request_client_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_client_certificate SyntheticsTest#request_client_certificate}
        :param request_definition: request_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_definition SyntheticsTest#request_definition}
        :param request_headers: Header name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_headers SyntheticsTest#request_headers}
        :param request_proxy: request_proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_proxy SyntheticsTest#request_proxy}
        :param request_query: Query arguments name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_query SyntheticsTest#request_query}
        :param retry: retry block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#retry SyntheticsTest#retry}
        :param subtype: The subtype of the Synthetic multistep API test step. Valid values are ``http``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#subtype SyntheticsTest#subtype}
        '''
        if isinstance(request_basicauth, dict):
            request_basicauth = SyntheticsTestApiStepRequestBasicauth(**request_basicauth)
        if isinstance(request_client_certificate, dict):
            request_client_certificate = SyntheticsTestApiStepRequestClientCertificate(**request_client_certificate)
        if isinstance(request_definition, dict):
            request_definition = SyntheticsTestApiStepRequestDefinition(**request_definition)
        if isinstance(request_proxy, dict):
            request_proxy = SyntheticsTestApiStepRequestProxy(**request_proxy)
        if isinstance(retry, dict):
            retry = SyntheticsTestApiStepRetry(**retry)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStep.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allow_failure", value=allow_failure, expected_type=type_hints["allow_failure"])
            check_type(argname="argument assertion", value=assertion, expected_type=type_hints["assertion"])
            check_type(argname="argument extracted_value", value=extracted_value, expected_type=type_hints["extracted_value"])
            check_type(argname="argument is_critical", value=is_critical, expected_type=type_hints["is_critical"])
            check_type(argname="argument request_basicauth", value=request_basicauth, expected_type=type_hints["request_basicauth"])
            check_type(argname="argument request_client_certificate", value=request_client_certificate, expected_type=type_hints["request_client_certificate"])
            check_type(argname="argument request_definition", value=request_definition, expected_type=type_hints["request_definition"])
            check_type(argname="argument request_headers", value=request_headers, expected_type=type_hints["request_headers"])
            check_type(argname="argument request_proxy", value=request_proxy, expected_type=type_hints["request_proxy"])
            check_type(argname="argument request_query", value=request_query, expected_type=type_hints["request_query"])
            check_type(argname="argument retry", value=retry, expected_type=type_hints["retry"])
            check_type(argname="argument subtype", value=subtype, expected_type=type_hints["subtype"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allow_failure is not None:
            self._values["allow_failure"] = allow_failure
        if assertion is not None:
            self._values["assertion"] = assertion
        if extracted_value is not None:
            self._values["extracted_value"] = extracted_value
        if is_critical is not None:
            self._values["is_critical"] = is_critical
        if request_basicauth is not None:
            self._values["request_basicauth"] = request_basicauth
        if request_client_certificate is not None:
            self._values["request_client_certificate"] = request_client_certificate
        if request_definition is not None:
            self._values["request_definition"] = request_definition
        if request_headers is not None:
            self._values["request_headers"] = request_headers
        if request_proxy is not None:
            self._values["request_proxy"] = request_proxy
        if request_query is not None:
            self._values["request_query"] = request_query
        if retry is not None:
            self._values["retry"] = retry
        if subtype is not None:
            self._values["subtype"] = subtype

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines whether or not to continue with test if this step fails.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_failure SyntheticsTest#allow_failure}
        '''
        result = self._values.get("allow_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def assertion(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestApiStepAssertion"]]]:
        '''assertion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#assertion SyntheticsTest#assertion}
        '''
        result = self._values.get("assertion")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestApiStepAssertion"]]], result)

    @builtins.property
    def extracted_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestApiStepExtractedValue"]]]:
        '''extracted_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#extracted_value SyntheticsTest#extracted_value}
        '''
        result = self._values.get("extracted_value")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestApiStepExtractedValue"]]], result)

    @builtins.property
    def is_critical(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines whether or not to consider the entire test as failed if this step fails.

        Can be used only if ``allow_failure`` is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#is_critical SyntheticsTest#is_critical}
        '''
        result = self._values.get("is_critical")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def request_basicauth(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepRequestBasicauth"]:
        '''request_basicauth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_basicauth SyntheticsTest#request_basicauth}
        '''
        result = self._values.get("request_basicauth")
        return typing.cast(typing.Optional["SyntheticsTestApiStepRequestBasicauth"], result)

    @builtins.property
    def request_client_certificate(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepRequestClientCertificate"]:
        '''request_client_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_client_certificate SyntheticsTest#request_client_certificate}
        '''
        result = self._values.get("request_client_certificate")
        return typing.cast(typing.Optional["SyntheticsTestApiStepRequestClientCertificate"], result)

    @builtins.property
    def request_definition(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepRequestDefinition"]:
        '''request_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_definition SyntheticsTest#request_definition}
        '''
        result = self._values.get("request_definition")
        return typing.cast(typing.Optional["SyntheticsTestApiStepRequestDefinition"], result)

    @builtins.property
    def request_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Header name and value map.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_headers SyntheticsTest#request_headers}
        '''
        result = self._values.get("request_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def request_proxy(self) -> typing.Optional["SyntheticsTestApiStepRequestProxy"]:
        '''request_proxy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_proxy SyntheticsTest#request_proxy}
        '''
        result = self._values.get("request_proxy")
        return typing.cast(typing.Optional["SyntheticsTestApiStepRequestProxy"], result)

    @builtins.property
    def request_query(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Query arguments name and value map.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_query SyntheticsTest#request_query}
        '''
        result = self._values.get("request_query")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def retry(self) -> typing.Optional["SyntheticsTestApiStepRetry"]:
        '''retry block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#retry SyntheticsTest#retry}
        '''
        result = self._values.get("retry")
        return typing.cast(typing.Optional["SyntheticsTestApiStepRetry"], result)

    @builtins.property
    def subtype(self) -> typing.Optional[builtins.str]:
        '''The subtype of the Synthetic multistep API test step. Valid values are ``http``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#subtype SyntheticsTest#subtype}
        '''
        result = self._values.get("subtype")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepAssertion",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "type": "type",
        "property": "property",
        "target": "target",
        "targetjsonpath": "targetjsonpath",
    },
)
class SyntheticsTestApiStepAssertion:
    def __init__(
        self,
        *,
        operator: builtins.str,
        type: builtins.str,
        property: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        targetjsonpath: typing.Optional[typing.Union["SyntheticsTestApiStepAssertionTargetjsonpath", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param operator: Assertion operator. **Note** Only some combinations of ``type`` and ``operator`` are valid (please refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        :param type: Type of assertion. **Note** Only some combinations of ``type`` and ``operator`` are valid (please refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_). Valid values are ``body``, ``header``, ``statusCode``, ``certificate``, ``responseTime``, ``property``, ``recordEvery``, ``recordSome``, ``tlsVersion``, ``minTlsVersion``, ``latency``, ``packetLossPercentage``, ``packetsReceived``, ``networkHop``, ``receivedMessage``, ``grpcHealthcheckStatus``, ``connection``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param property: If assertion type is ``header``, this is the header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#property SyntheticsTest#property}
        :param target: Expected value. Depends on the assertion type, refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_ for details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#target SyntheticsTest#target}
        :param targetjsonpath: targetjsonpath block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetjsonpath SyntheticsTest#targetjsonpath}
        '''
        if isinstance(targetjsonpath, dict):
            targetjsonpath = SyntheticsTestApiStepAssertionTargetjsonpath(**targetjsonpath)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepAssertion.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument property", value=property, expected_type=type_hints["property"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument targetjsonpath", value=targetjsonpath, expected_type=type_hints["targetjsonpath"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "type": type,
        }
        if property is not None:
            self._values["property"] = property
        if target is not None:
            self._values["target"] = target
        if targetjsonpath is not None:
            self._values["targetjsonpath"] = targetjsonpath

    @builtins.property
    def operator(self) -> builtins.str:
        '''Assertion operator. **Note** Only some combinations of ``type`` and ``operator`` are valid (please refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of assertion.

        **Note** Only some combinations of ``type`` and ``operator`` are valid (please refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_). Valid values are ``body``, ``header``, ``statusCode``, ``certificate``, ``responseTime``, ``property``, ``recordEvery``, ``recordSome``, ``tlsVersion``, ``minTlsVersion``, ``latency``, ``packetLossPercentage``, ``packetsReceived``, ``networkHop``, ``receivedMessage``, ``grpcHealthcheckStatus``, ``connection``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def property(self) -> typing.Optional[builtins.str]:
        '''If assertion type is ``header``, this is the header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#property SyntheticsTest#property}
        '''
        result = self._values.get("property")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Expected value. Depends on the assertion type, refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_ for details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#target SyntheticsTest#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targetjsonpath(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepAssertionTargetjsonpath"]:
        '''targetjsonpath block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetjsonpath SyntheticsTest#targetjsonpath}
        '''
        result = self._values.get("targetjsonpath")
        return typing.cast(typing.Optional["SyntheticsTestApiStepAssertionTargetjsonpath"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepAssertion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepAssertionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepAssertionList",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepAssertionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SyntheticsTestApiStepAssertionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepAssertionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsTestApiStepAssertionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepAssertion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepAssertion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepAssertion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestApiStepAssertionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepAssertionOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepAssertionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTargetjsonpath")
    def put_targetjsonpath(
        self,
        *,
        jsonpath: builtins.str,
        operator: builtins.str,
        targetvalue: builtins.str,
    ) -> None:
        '''
        :param jsonpath: The JSON path to assert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#jsonpath SyntheticsTest#jsonpath}
        :param operator: The specific operator to use on the path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        :param targetvalue: Expected matching value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetvalue SyntheticsTest#targetvalue}
        '''
        value = SyntheticsTestApiStepAssertionTargetjsonpath(
            jsonpath=jsonpath, operator=operator, targetvalue=targetvalue
        )

        return typing.cast(None, jsii.invoke(self, "putTargetjsonpath", [value]))

    @jsii.member(jsii_name="resetProperty")
    def reset_property(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperty", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTargetjsonpath")
    def reset_targetjsonpath(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetjsonpath", []))

    @builtins.property
    @jsii.member(jsii_name="targetjsonpath")
    def targetjsonpath(
        self,
    ) -> "SyntheticsTestApiStepAssertionTargetjsonpathOutputReference":
        return typing.cast("SyntheticsTestApiStepAssertionTargetjsonpathOutputReference", jsii.get(self, "targetjsonpath"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyInput")
    def property_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propertyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetjsonpathInput")
    def targetjsonpath_input(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepAssertionTargetjsonpath"]:
        return typing.cast(typing.Optional["SyntheticsTestApiStepAssertionTargetjsonpath"], jsii.get(self, "targetjsonpathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @property.setter
    def property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionOutputReference, "property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "property", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsTestApiStepAssertion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsTestApiStepAssertion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsTestApiStepAssertion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepAssertionTargetjsonpath",
    jsii_struct_bases=[],
    name_mapping={
        "jsonpath": "jsonpath",
        "operator": "operator",
        "targetvalue": "targetvalue",
    },
)
class SyntheticsTestApiStepAssertionTargetjsonpath:
    def __init__(
        self,
        *,
        jsonpath: builtins.str,
        operator: builtins.str,
        targetvalue: builtins.str,
    ) -> None:
        '''
        :param jsonpath: The JSON path to assert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#jsonpath SyntheticsTest#jsonpath}
        :param operator: The specific operator to use on the path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        :param targetvalue: Expected matching value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetvalue SyntheticsTest#targetvalue}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepAssertionTargetjsonpath.__init__)
            check_type(argname="argument jsonpath", value=jsonpath, expected_type=type_hints["jsonpath"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument targetvalue", value=targetvalue, expected_type=type_hints["targetvalue"])
        self._values: typing.Dict[str, typing.Any] = {
            "jsonpath": jsonpath,
            "operator": operator,
            "targetvalue": targetvalue,
        }

    @builtins.property
    def jsonpath(self) -> builtins.str:
        '''The JSON path to assert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#jsonpath SyntheticsTest#jsonpath}
        '''
        result = self._values.get("jsonpath")
        assert result is not None, "Required property 'jsonpath' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''The specific operator to use on the path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targetvalue(self) -> builtins.str:
        '''Expected matching value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetvalue SyntheticsTest#targetvalue}
        '''
        result = self._values.get("targetvalue")
        assert result is not None, "Required property 'targetvalue' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepAssertionTargetjsonpath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepAssertionTargetjsonpathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepAssertionTargetjsonpathOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepAssertionTargetjsonpathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="jsonpathInput")
    def jsonpath_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonpathInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="targetvalueInput")
    def targetvalue_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetvalueInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonpath")
    def jsonpath(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonpath"))

    @jsonpath.setter
    def jsonpath(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionTargetjsonpathOutputReference, "jsonpath").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonpath", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionTargetjsonpathOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="targetvalue")
    def targetvalue(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetvalue"))

    @targetvalue.setter
    def targetvalue(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionTargetjsonpathOutputReference, "targetvalue").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetvalue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestApiStepAssertionTargetjsonpath]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepAssertionTargetjsonpath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepAssertionTargetjsonpath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepAssertionTargetjsonpathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepExtractedValue",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "parser": "parser",
        "type": "type",
        "field": "field",
    },
)
class SyntheticsTestApiStepExtractedValue:
    def __init__(
        self,
        *,
        name: builtins.str,
        parser: typing.Union["SyntheticsTestApiStepExtractedValueParser", typing.Dict[str, typing.Any]],
        type: builtins.str,
        field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}.
        :param parser: parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#parser SyntheticsTest#parser}
        :param type: Property of the Synthetics Test Response to use for the variable. Valid values are ``http_body``, ``http_header``, ``local_variable``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param field: When type is ``http_header``, name of the header to use to extract the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#field SyntheticsTest#field}
        '''
        if isinstance(parser, dict):
            parser = SyntheticsTestApiStepExtractedValueParser(**parser)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepExtractedValue.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parser", value=parser, expected_type=type_hints["parser"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "parser": parser,
            "type": type,
        }
        if field is not None:
            self._values["field"] = field

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parser(self) -> "SyntheticsTestApiStepExtractedValueParser":
        '''parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#parser SyntheticsTest#parser}
        '''
        result = self._values.get("parser")
        assert result is not None, "Required property 'parser' is missing"
        return typing.cast("SyntheticsTestApiStepExtractedValueParser", result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Property of the Synthetics Test Response to use for the variable. Valid values are ``http_body``, ``http_header``, ``local_variable``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        '''When type is ``http_header``, name of the header to use to extract the value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#field SyntheticsTest#field}
        '''
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepExtractedValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepExtractedValueList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepExtractedValueList",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepExtractedValueList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SyntheticsTestApiStepExtractedValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepExtractedValueList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsTestApiStepExtractedValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepExtractedValue]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepExtractedValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepExtractedValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestApiStepExtractedValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepExtractedValueOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepExtractedValueOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParser")
    def put_parser(
        self,
        *,
        type: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of parser for a Synthetics global variable from a synthetics test. Valid values are ``raw``, ``json_path``, ``regex``, ``x_path``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param value: Regex or JSON path used for the parser. Not used with type ``raw``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        '''
        value_ = SyntheticsTestApiStepExtractedValueParser(type=type, value=value)

        return typing.cast(None, jsii.invoke(self, "putParser", [value_]))

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @builtins.property
    @jsii.member(jsii_name="parser")
    def parser(self) -> "SyntheticsTestApiStepExtractedValueParserOutputReference":
        return typing.cast("SyntheticsTestApiStepExtractedValueParserOutputReference", jsii.get(self, "parser"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parserInput")
    def parser_input(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepExtractedValueParser"]:
        return typing.cast(typing.Optional["SyntheticsTestApiStepExtractedValueParser"], jsii.get(self, "parserInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueOutputReference, "field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsTestApiStepExtractedValue, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsTestApiStepExtractedValue, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsTestApiStepExtractedValue, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepExtractedValueParser",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class SyntheticsTestApiStepExtractedValueParser:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of parser for a Synthetics global variable from a synthetics test. Valid values are ``raw``, ``json_path``, ``regex``, ``x_path``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param value: Regex or JSON path used for the parser. Not used with type ``raw``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepExtractedValueParser.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of parser for a Synthetics global variable from a synthetics test. Valid values are ``raw``, ``json_path``, ``regex``, ``x_path``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Regex or JSON path used for the parser. Not used with type ``raw``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepExtractedValueParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepExtractedValueParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepExtractedValueParserOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepExtractedValueParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueParserOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueParserOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestApiStepExtractedValueParser]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepExtractedValueParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepExtractedValueParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepExtractedValueParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestApiStepList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepList",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SyntheticsTestApiStepOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsTestApiStepOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStep]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStep]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStep]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestApiStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssertion")
    def put_assertion(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsTestApiStepAssertion, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepOutputReference.put_assertion)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssertion", [value]))

    @jsii.member(jsii_name="putExtractedValue")
    def put_extracted_value(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsTestApiStepExtractedValue, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepOutputReference.put_extracted_value)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtractedValue", [value]))

    @jsii.member(jsii_name="putRequestBasicauth")
    def put_request_basicauth(
        self,
        *,
        access_key: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        service_name: typing.Optional[builtins.str] = None,
        session_token: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        workstation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_key: Access key for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#access_key SyntheticsTest#access_key}
        :param domain: Domain for ``ntlm`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#domain SyntheticsTest#domain}
        :param password: Password for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#password SyntheticsTest#password}
        :param region: Region for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#region SyntheticsTest#region}
        :param secret_key: Secret key for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#secret_key SyntheticsTest#secret_key}
        :param service_name: Service name for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service_name SyntheticsTest#service_name}
        :param session_token: Session token for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#session_token SyntheticsTest#session_token}
        :param type: Type of basic authentication to use when performing the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param username: Username for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#username SyntheticsTest#username}
        :param workstation: Workstation for ``ntlm`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#workstation SyntheticsTest#workstation}
        '''
        value = SyntheticsTestApiStepRequestBasicauth(
            access_key=access_key,
            domain=domain,
            password=password,
            region=region,
            secret_key=secret_key,
            service_name=service_name,
            session_token=session_token,
            type=type,
            username=username,
            workstation=workstation,
        )

        return typing.cast(None, jsii.invoke(self, "putRequestBasicauth", [value]))

    @jsii.member(jsii_name="putRequestClientCertificate")
    def put_request_client_certificate(
        self,
        *,
        cert: typing.Union["SyntheticsTestApiStepRequestClientCertificateCert", typing.Dict[str, typing.Any]],
        key: typing.Union["SyntheticsTestApiStepRequestClientCertificateKey", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param cert: cert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#cert SyntheticsTest#cert}
        :param key: key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#key SyntheticsTest#key}
        '''
        value = SyntheticsTestApiStepRequestClientCertificate(cert=cert, key=key)

        return typing.cast(None, jsii.invoke(self, "putRequestClientCertificate", [value]))

    @jsii.member(jsii_name="putRequestDefinition")
    def put_request_definition(
        self,
        *,
        allow_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        body: typing.Optional[builtins.str] = None,
        certificate_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_server: typing.Optional[builtins.str] = None,
        dns_server_port: typing.Optional[jsii.Number] = None,
        follow_redirects: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        method: typing.Optional[builtins.str] = None,
        no_saving_response_body: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        number_of_packets: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        servername: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        should_track_hops: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_insecure: Allows loading insecure content for an HTTP test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_insecure SyntheticsTest#allow_insecure}
        :param body: The request body. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#body SyntheticsTest#body}
        :param certificate_domains: By default, the client certificate is applied on the domain of the starting URL for browser tests. If you want your client certificate to be applied on other domains instead, add them in ``certificate_domains``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#certificate_domains SyntheticsTest#certificate_domains}
        :param dns_server: DNS server to use for DNS tests (``subtype = "dns"``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server SyntheticsTest#dns_server}
        :param dns_server_port: DNS server port to use for DNS tests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server_port SyntheticsTest#dns_server_port}
        :param follow_redirects: Determines whether or not the API HTTP test should follow redirects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#follow_redirects SyntheticsTest#follow_redirects}
        :param host: Host name to perform the test with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#host SyntheticsTest#host}
        :param message: For UDP and websocket tests, message to send with the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        :param method: The HTTP method. Valid values are ``GET``, ``POST``, ``PATCH``, ``PUT``, ``DELETE``, ``HEAD``, ``OPTIONS``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#method SyntheticsTest#method}
        :param no_saving_response_body: Determines whether or not to save the response body. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_saving_response_body SyntheticsTest#no_saving_response_body}
        :param number_of_packets: Number of pings to use per test for ICMP tests (``subtype = "icmp"``) between 0 and 10. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#number_of_packets SyntheticsTest#number_of_packets}
        :param port: Port to use when performing the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#port SyntheticsTest#port}
        :param servername: For SSL tests, it specifies on which server you want to initiate the TLS handshake, allowing the server to present one of multiple possible certificates on the same IP address and TCP port number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#servername SyntheticsTest#servername}
        :param service: For gRPC tests, service to target for healthcheck. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service SyntheticsTest#service}
        :param should_track_hops: This will turn on a traceroute probe to discover all gateways along the path to the host destination. For ICMP tests (``subtype = "icmp"``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#should_track_hops SyntheticsTest#should_track_hops}
        :param timeout: Timeout in seconds for the test. Defaults to ``60``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#timeout SyntheticsTest#timeout}
        :param url: The URL to send the request to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        '''
        value = SyntheticsTestApiStepRequestDefinition(
            allow_insecure=allow_insecure,
            body=body,
            certificate_domains=certificate_domains,
            dns_server=dns_server,
            dns_server_port=dns_server_port,
            follow_redirects=follow_redirects,
            host=host,
            message=message,
            method=method,
            no_saving_response_body=no_saving_response_body,
            number_of_packets=number_of_packets,
            port=port,
            servername=servername,
            service=service,
            should_track_hops=should_track_hops,
            timeout=timeout,
            url=url,
        )

        return typing.cast(None, jsii.invoke(self, "putRequestDefinition", [value]))

    @jsii.member(jsii_name="putRequestProxy")
    def put_request_proxy(
        self,
        *,
        url: builtins.str,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: URL of the proxy to perform the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        :param headers: Header name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#headers SyntheticsTest#headers}
        '''
        value = SyntheticsTestApiStepRequestProxy(url=url, headers=headers)

        return typing.cast(None, jsii.invoke(self, "putRequestProxy", [value]))

    @jsii.member(jsii_name="putRetry")
    def put_retry(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: Number of retries needed to consider a location as failed before sending a notification alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#count SyntheticsTest#count}
        :param interval: Interval between a failed test and the next retry in milliseconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#interval SyntheticsTest#interval}
        '''
        value = SyntheticsTestApiStepRetry(count=count, interval=interval)

        return typing.cast(None, jsii.invoke(self, "putRetry", [value]))

    @jsii.member(jsii_name="resetAllowFailure")
    def reset_allow_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowFailure", []))

    @jsii.member(jsii_name="resetAssertion")
    def reset_assertion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssertion", []))

    @jsii.member(jsii_name="resetExtractedValue")
    def reset_extracted_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtractedValue", []))

    @jsii.member(jsii_name="resetIsCritical")
    def reset_is_critical(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsCritical", []))

    @jsii.member(jsii_name="resetRequestBasicauth")
    def reset_request_basicauth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestBasicauth", []))

    @jsii.member(jsii_name="resetRequestClientCertificate")
    def reset_request_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestClientCertificate", []))

    @jsii.member(jsii_name="resetRequestDefinition")
    def reset_request_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestDefinition", []))

    @jsii.member(jsii_name="resetRequestHeaders")
    def reset_request_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeaders", []))

    @jsii.member(jsii_name="resetRequestProxy")
    def reset_request_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestProxy", []))

    @jsii.member(jsii_name="resetRequestQuery")
    def reset_request_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestQuery", []))

    @jsii.member(jsii_name="resetRetry")
    def reset_retry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetry", []))

    @jsii.member(jsii_name="resetSubtype")
    def reset_subtype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubtype", []))

    @builtins.property
    @jsii.member(jsii_name="assertion")
    def assertion(self) -> SyntheticsTestApiStepAssertionList:
        return typing.cast(SyntheticsTestApiStepAssertionList, jsii.get(self, "assertion"))

    @builtins.property
    @jsii.member(jsii_name="extractedValue")
    def extracted_value(self) -> SyntheticsTestApiStepExtractedValueList:
        return typing.cast(SyntheticsTestApiStepExtractedValueList, jsii.get(self, "extractedValue"))

    @builtins.property
    @jsii.member(jsii_name="requestBasicauth")
    def request_basicauth(
        self,
    ) -> "SyntheticsTestApiStepRequestBasicauthOutputReference":
        return typing.cast("SyntheticsTestApiStepRequestBasicauthOutputReference", jsii.get(self, "requestBasicauth"))

    @builtins.property
    @jsii.member(jsii_name="requestClientCertificate")
    def request_client_certificate(
        self,
    ) -> "SyntheticsTestApiStepRequestClientCertificateOutputReference":
        return typing.cast("SyntheticsTestApiStepRequestClientCertificateOutputReference", jsii.get(self, "requestClientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="requestDefinition")
    def request_definition(
        self,
    ) -> "SyntheticsTestApiStepRequestDefinitionOutputReference":
        return typing.cast("SyntheticsTestApiStepRequestDefinitionOutputReference", jsii.get(self, "requestDefinition"))

    @builtins.property
    @jsii.member(jsii_name="requestProxy")
    def request_proxy(self) -> "SyntheticsTestApiStepRequestProxyOutputReference":
        return typing.cast("SyntheticsTestApiStepRequestProxyOutputReference", jsii.get(self, "requestProxy"))

    @builtins.property
    @jsii.member(jsii_name="retry")
    def retry(self) -> "SyntheticsTestApiStepRetryOutputReference":
        return typing.cast("SyntheticsTestApiStepRetryOutputReference", jsii.get(self, "retry"))

    @builtins.property
    @jsii.member(jsii_name="allowFailureInput")
    def allow_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="assertionInput")
    def assertion_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepAssertion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepAssertion]]], jsii.get(self, "assertionInput"))

    @builtins.property
    @jsii.member(jsii_name="extractedValueInput")
    def extracted_value_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepExtractedValue]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStepExtractedValue]]], jsii.get(self, "extractedValueInput"))

    @builtins.property
    @jsii.member(jsii_name="isCriticalInput")
    def is_critical_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isCriticalInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requestBasicauthInput")
    def request_basicauth_input(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepRequestBasicauth"]:
        return typing.cast(typing.Optional["SyntheticsTestApiStepRequestBasicauth"], jsii.get(self, "requestBasicauthInput"))

    @builtins.property
    @jsii.member(jsii_name="requestClientCertificateInput")
    def request_client_certificate_input(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepRequestClientCertificate"]:
        return typing.cast(typing.Optional["SyntheticsTestApiStepRequestClientCertificate"], jsii.get(self, "requestClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="requestDefinitionInput")
    def request_definition_input(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepRequestDefinition"]:
        return typing.cast(typing.Optional["SyntheticsTestApiStepRequestDefinition"], jsii.get(self, "requestDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeadersInput")
    def request_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="requestProxyInput")
    def request_proxy_input(
        self,
    ) -> typing.Optional["SyntheticsTestApiStepRequestProxy"]:
        return typing.cast(typing.Optional["SyntheticsTestApiStepRequestProxy"], jsii.get(self, "requestProxyInput"))

    @builtins.property
    @jsii.member(jsii_name="requestQueryInput")
    def request_query_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="retryInput")
    def retry_input(self) -> typing.Optional["SyntheticsTestApiStepRetry"]:
        return typing.cast(typing.Optional["SyntheticsTestApiStepRetry"], jsii.get(self, "retryInput"))

    @builtins.property
    @jsii.member(jsii_name="subtypeInput")
    def subtype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowFailure")
    def allow_failure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowFailure"))

    @allow_failure.setter
    def allow_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepOutputReference, "allow_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowFailure", value)

    @builtins.property
    @jsii.member(jsii_name="isCritical")
    def is_critical(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isCritical"))

    @is_critical.setter
    def is_critical(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepOutputReference, "is_critical").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCritical", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="requestHeaders")
    def request_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestHeaders"))

    @request_headers.setter
    def request_headers(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepOutputReference, "request_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="requestQuery")
    def request_query(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestQuery"))

    @request_query.setter
    def request_query(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepOutputReference, "request_query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestQuery", value)

    @builtins.property
    @jsii.member(jsii_name="subtype")
    def subtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subtype"))

    @subtype.setter
    def subtype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepOutputReference, "subtype").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subtype", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsTestApiStep, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsTestApiStep, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsTestApiStep, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestBasicauth",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "domain": "domain",
        "password": "password",
        "region": "region",
        "secret_key": "secretKey",
        "service_name": "serviceName",
        "session_token": "sessionToken",
        "type": "type",
        "username": "username",
        "workstation": "workstation",
    },
)
class SyntheticsTestApiStepRequestBasicauth:
    def __init__(
        self,
        *,
        access_key: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        service_name: typing.Optional[builtins.str] = None,
        session_token: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        workstation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_key: Access key for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#access_key SyntheticsTest#access_key}
        :param domain: Domain for ``ntlm`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#domain SyntheticsTest#domain}
        :param password: Password for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#password SyntheticsTest#password}
        :param region: Region for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#region SyntheticsTest#region}
        :param secret_key: Secret key for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#secret_key SyntheticsTest#secret_key}
        :param service_name: Service name for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service_name SyntheticsTest#service_name}
        :param session_token: Session token for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#session_token SyntheticsTest#session_token}
        :param type: Type of basic authentication to use when performing the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param username: Username for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#username SyntheticsTest#username}
        :param workstation: Workstation for ``ntlm`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#workstation SyntheticsTest#workstation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestBasicauth.__init__)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument session_token", value=session_token, expected_type=type_hints["session_token"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument workstation", value=workstation, expected_type=type_hints["workstation"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_key is not None:
            self._values["access_key"] = access_key
        if domain is not None:
            self._values["domain"] = domain
        if password is not None:
            self._values["password"] = password
        if region is not None:
            self._values["region"] = region
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if service_name is not None:
            self._values["service_name"] = service_name
        if session_token is not None:
            self._values["session_token"] = session_token
        if type is not None:
            self._values["type"] = type
        if username is not None:
            self._values["username"] = username
        if workstation is not None:
            self._values["workstation"] = workstation

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''Access key for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#access_key SyntheticsTest#access_key}
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''Domain for ``ntlm`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#domain SyntheticsTest#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#password SyntheticsTest#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#region SyntheticsTest#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''Secret key for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#secret_key SyntheticsTest#secret_key}
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Service name for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service_name SyntheticsTest#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_token(self) -> typing.Optional[builtins.str]:
        '''Session token for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#session_token SyntheticsTest#session_token}
        '''
        result = self._values.get("session_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type of basic authentication to use when performing the test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#username SyntheticsTest#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workstation(self) -> typing.Optional[builtins.str]:
        '''Workstation for ``ntlm`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#workstation SyntheticsTest#workstation}
        '''
        result = self._values.get("workstation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepRequestBasicauth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepRequestBasicauthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestBasicauthOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestBasicauthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSecretKey")
    def reset_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretKey", []))

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @jsii.member(jsii_name="resetSessionToken")
    def reset_session_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionToken", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetWorkstation")
    def reset_workstation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkstation", []))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTokenInput")
    def session_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="workstationInput")
    def workstation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workstationInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "secret_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="sessionToken")
    def session_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionToken"))

    @session_token.setter
    def session_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "session_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionToken", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="workstation")
    def workstation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workstation"))

    @workstation.setter
    def workstation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "workstation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workstation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestApiStepRequestBasicauth]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRequestBasicauth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepRequestBasicauth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestBasicauthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestClientCertificate",
    jsii_struct_bases=[],
    name_mapping={"cert": "cert", "key": "key"},
)
class SyntheticsTestApiStepRequestClientCertificate:
    def __init__(
        self,
        *,
        cert: typing.Union["SyntheticsTestApiStepRequestClientCertificateCert", typing.Dict[str, typing.Any]],
        key: typing.Union["SyntheticsTestApiStepRequestClientCertificateKey", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param cert: cert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#cert SyntheticsTest#cert}
        :param key: key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#key SyntheticsTest#key}
        '''
        if isinstance(cert, dict):
            cert = SyntheticsTestApiStepRequestClientCertificateCert(**cert)
        if isinstance(key, dict):
            key = SyntheticsTestApiStepRequestClientCertificateKey(**key)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestClientCertificate.__init__)
            check_type(argname="argument cert", value=cert, expected_type=type_hints["cert"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "cert": cert,
            "key": key,
        }

    @builtins.property
    def cert(self) -> "SyntheticsTestApiStepRequestClientCertificateCert":
        '''cert block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#cert SyntheticsTest#cert}
        '''
        result = self._values.get("cert")
        assert result is not None, "Required property 'cert' is missing"
        return typing.cast("SyntheticsTestApiStepRequestClientCertificateCert", result)

    @builtins.property
    def key(self) -> "SyntheticsTestApiStepRequestClientCertificateKey":
        '''key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#key SyntheticsTest#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast("SyntheticsTestApiStepRequestClientCertificateKey", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepRequestClientCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestClientCertificateCert",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "filename": "filename"},
)
class SyntheticsTestApiStepRequestClientCertificateCert:
    def __init__(
        self,
        *,
        content: builtins.str,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: Content of the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        :param filename: File name for the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestClientCertificateCert.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if filename is not None:
            self._values["filename"] = filename

    @builtins.property
    def content(self) -> builtins.str:
        '''Content of the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''File name for the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepRequestClientCertificateCert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepRequestClientCertificateCertOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestClientCertificateCertOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestClientCertificateCertOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestClientCertificateCertOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestClientCertificateCertOutputReference, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestApiStepRequestClientCertificateCert]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRequestClientCertificateCert], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepRequestClientCertificateCert],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestClientCertificateCertOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestClientCertificateKey",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "filename": "filename"},
)
class SyntheticsTestApiStepRequestClientCertificateKey:
    def __init__(
        self,
        *,
        content: builtins.str,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: Content of the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        :param filename: File name for the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestClientCertificateKey.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if filename is not None:
            self._values["filename"] = filename

    @builtins.property
    def content(self) -> builtins.str:
        '''Content of the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''File name for the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepRequestClientCertificateKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepRequestClientCertificateKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestClientCertificateKeyOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestClientCertificateKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestClientCertificateKeyOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestClientCertificateKeyOutputReference, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestApiStepRequestClientCertificateKey]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRequestClientCertificateKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepRequestClientCertificateKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestClientCertificateKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestApiStepRequestClientCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestClientCertificateOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestClientCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCert")
    def put_cert(
        self,
        *,
        content: builtins.str,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: Content of the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        :param filename: File name for the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        value = SyntheticsTestApiStepRequestClientCertificateCert(
            content=content, filename=filename
        )

        return typing.cast(None, jsii.invoke(self, "putCert", [value]))

    @jsii.member(jsii_name="putKey")
    def put_key(
        self,
        *,
        content: builtins.str,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: Content of the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        :param filename: File name for the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        value = SyntheticsTestApiStepRequestClientCertificateKey(
            content=content, filename=filename
        )

        return typing.cast(None, jsii.invoke(self, "putKey", [value]))

    @builtins.property
    @jsii.member(jsii_name="cert")
    def cert(self) -> SyntheticsTestApiStepRequestClientCertificateCertOutputReference:
        return typing.cast(SyntheticsTestApiStepRequestClientCertificateCertOutputReference, jsii.get(self, "cert"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> SyntheticsTestApiStepRequestClientCertificateKeyOutputReference:
        return typing.cast(SyntheticsTestApiStepRequestClientCertificateKeyOutputReference, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="certInput")
    def cert_input(
        self,
    ) -> typing.Optional[SyntheticsTestApiStepRequestClientCertificateCert]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRequestClientCertificateCert], jsii.get(self, "certInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(
        self,
    ) -> typing.Optional[SyntheticsTestApiStepRequestClientCertificateKey]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRequestClientCertificateKey], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestApiStepRequestClientCertificate]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRequestClientCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepRequestClientCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestClientCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "allow_insecure": "allowInsecure",
        "body": "body",
        "certificate_domains": "certificateDomains",
        "dns_server": "dnsServer",
        "dns_server_port": "dnsServerPort",
        "follow_redirects": "followRedirects",
        "host": "host",
        "message": "message",
        "method": "method",
        "no_saving_response_body": "noSavingResponseBody",
        "number_of_packets": "numberOfPackets",
        "port": "port",
        "servername": "servername",
        "service": "service",
        "should_track_hops": "shouldTrackHops",
        "timeout": "timeout",
        "url": "url",
    },
)
class SyntheticsTestApiStepRequestDefinition:
    def __init__(
        self,
        *,
        allow_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        body: typing.Optional[builtins.str] = None,
        certificate_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_server: typing.Optional[builtins.str] = None,
        dns_server_port: typing.Optional[jsii.Number] = None,
        follow_redirects: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        method: typing.Optional[builtins.str] = None,
        no_saving_response_body: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        number_of_packets: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        servername: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        should_track_hops: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_insecure: Allows loading insecure content for an HTTP test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_insecure SyntheticsTest#allow_insecure}
        :param body: The request body. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#body SyntheticsTest#body}
        :param certificate_domains: By default, the client certificate is applied on the domain of the starting URL for browser tests. If you want your client certificate to be applied on other domains instead, add them in ``certificate_domains``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#certificate_domains SyntheticsTest#certificate_domains}
        :param dns_server: DNS server to use for DNS tests (``subtype = "dns"``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server SyntheticsTest#dns_server}
        :param dns_server_port: DNS server port to use for DNS tests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server_port SyntheticsTest#dns_server_port}
        :param follow_redirects: Determines whether or not the API HTTP test should follow redirects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#follow_redirects SyntheticsTest#follow_redirects}
        :param host: Host name to perform the test with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#host SyntheticsTest#host}
        :param message: For UDP and websocket tests, message to send with the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        :param method: The HTTP method. Valid values are ``GET``, ``POST``, ``PATCH``, ``PUT``, ``DELETE``, ``HEAD``, ``OPTIONS``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#method SyntheticsTest#method}
        :param no_saving_response_body: Determines whether or not to save the response body. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_saving_response_body SyntheticsTest#no_saving_response_body}
        :param number_of_packets: Number of pings to use per test for ICMP tests (``subtype = "icmp"``) between 0 and 10. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#number_of_packets SyntheticsTest#number_of_packets}
        :param port: Port to use when performing the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#port SyntheticsTest#port}
        :param servername: For SSL tests, it specifies on which server you want to initiate the TLS handshake, allowing the server to present one of multiple possible certificates on the same IP address and TCP port number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#servername SyntheticsTest#servername}
        :param service: For gRPC tests, service to target for healthcheck. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service SyntheticsTest#service}
        :param should_track_hops: This will turn on a traceroute probe to discover all gateways along the path to the host destination. For ICMP tests (``subtype = "icmp"``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#should_track_hops SyntheticsTest#should_track_hops}
        :param timeout: Timeout in seconds for the test. Defaults to ``60``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#timeout SyntheticsTest#timeout}
        :param url: The URL to send the request to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestDefinition.__init__)
            check_type(argname="argument allow_insecure", value=allow_insecure, expected_type=type_hints["allow_insecure"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument certificate_domains", value=certificate_domains, expected_type=type_hints["certificate_domains"])
            check_type(argname="argument dns_server", value=dns_server, expected_type=type_hints["dns_server"])
            check_type(argname="argument dns_server_port", value=dns_server_port, expected_type=type_hints["dns_server_port"])
            check_type(argname="argument follow_redirects", value=follow_redirects, expected_type=type_hints["follow_redirects"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument no_saving_response_body", value=no_saving_response_body, expected_type=type_hints["no_saving_response_body"])
            check_type(argname="argument number_of_packets", value=number_of_packets, expected_type=type_hints["number_of_packets"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument servername", value=servername, expected_type=type_hints["servername"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument should_track_hops", value=should_track_hops, expected_type=type_hints["should_track_hops"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_insecure is not None:
            self._values["allow_insecure"] = allow_insecure
        if body is not None:
            self._values["body"] = body
        if certificate_domains is not None:
            self._values["certificate_domains"] = certificate_domains
        if dns_server is not None:
            self._values["dns_server"] = dns_server
        if dns_server_port is not None:
            self._values["dns_server_port"] = dns_server_port
        if follow_redirects is not None:
            self._values["follow_redirects"] = follow_redirects
        if host is not None:
            self._values["host"] = host
        if message is not None:
            self._values["message"] = message
        if method is not None:
            self._values["method"] = method
        if no_saving_response_body is not None:
            self._values["no_saving_response_body"] = no_saving_response_body
        if number_of_packets is not None:
            self._values["number_of_packets"] = number_of_packets
        if port is not None:
            self._values["port"] = port
        if servername is not None:
            self._values["servername"] = servername
        if service is not None:
            self._values["service"] = service
        if should_track_hops is not None:
            self._values["should_track_hops"] = should_track_hops
        if timeout is not None:
            self._values["timeout"] = timeout
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def allow_insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allows loading insecure content for an HTTP test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_insecure SyntheticsTest#allow_insecure}
        '''
        result = self._values.get("allow_insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''The request body.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#body SyntheticsTest#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''By default, the client certificate is applied on the domain of the starting URL for browser tests.

        If you want your client certificate to be applied on other domains instead, add them in ``certificate_domains``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#certificate_domains SyntheticsTest#certificate_domains}
        '''
        result = self._values.get("certificate_domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dns_server(self) -> typing.Optional[builtins.str]:
        '''DNS server to use for DNS tests (``subtype = "dns"``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server SyntheticsTest#dns_server}
        '''
        result = self._values.get("dns_server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_server_port(self) -> typing.Optional[jsii.Number]:
        '''DNS server port to use for DNS tests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server_port SyntheticsTest#dns_server_port}
        '''
        result = self._values.get("dns_server_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def follow_redirects(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines whether or not the API HTTP test should follow redirects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#follow_redirects SyntheticsTest#follow_redirects}
        '''
        result = self._values.get("follow_redirects")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host name to perform the test with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#host SyntheticsTest#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''For UDP and websocket tests, message to send with the request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''The HTTP method. Valid values are ``GET``, ``POST``, ``PATCH``, ``PUT``, ``DELETE``, ``HEAD``, ``OPTIONS``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#method SyntheticsTest#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_saving_response_body(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines whether or not to save the response body.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_saving_response_body SyntheticsTest#no_saving_response_body}
        '''
        result = self._values.get("no_saving_response_body")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def number_of_packets(self) -> typing.Optional[jsii.Number]:
        '''Number of pings to use per test for ICMP tests (``subtype = "icmp"``) between 0 and 10.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#number_of_packets SyntheticsTest#number_of_packets}
        '''
        result = self._values.get("number_of_packets")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to use when performing the test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#port SyntheticsTest#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def servername(self) -> typing.Optional[builtins.str]:
        '''For SSL tests, it specifies on which server you want to initiate the TLS handshake, allowing the server to present one of multiple possible certificates on the same IP address and TCP port number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#servername SyntheticsTest#servername}
        '''
        result = self._values.get("servername")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''For gRPC tests, service to target for healthcheck.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service SyntheticsTest#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def should_track_hops(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''This will turn on a traceroute probe to discover all gateways along the path to the host destination.

        For ICMP tests (``subtype = "icmp"``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#should_track_hops SyntheticsTest#should_track_hops}
        '''
        result = self._values.get("should_track_hops")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Timeout in seconds for the test. Defaults to ``60``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#timeout SyntheticsTest#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''The URL to send the request to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepRequestDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepRequestDefinitionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestDefinitionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowInsecure")
    def reset_allow_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowInsecure", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetCertificateDomains")
    def reset_certificate_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateDomains", []))

    @jsii.member(jsii_name="resetDnsServer")
    def reset_dns_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServer", []))

    @jsii.member(jsii_name="resetDnsServerPort")
    def reset_dns_server_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServerPort", []))

    @jsii.member(jsii_name="resetFollowRedirects")
    def reset_follow_redirects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFollowRedirects", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetNoSavingResponseBody")
    def reset_no_saving_response_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoSavingResponseBody", []))

    @jsii.member(jsii_name="resetNumberOfPackets")
    def reset_number_of_packets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberOfPackets", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetServername")
    def reset_servername(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServername", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetShouldTrackHops")
    def reset_should_track_hops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShouldTrackHops", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="allowInsecureInput")
    def allow_insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowInsecureInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateDomainsInput")
    def certificate_domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServerInput")
    def dns_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsServerInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServerPortInput")
    def dns_server_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dnsServerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="followRedirectsInput")
    def follow_redirects_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "followRedirectsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="noSavingResponseBodyInput")
    def no_saving_response_body_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noSavingResponseBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfPacketsInput")
    def number_of_packets_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfPacketsInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="servernameInput")
    def servername_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servernameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldTrackHopsInput")
    def should_track_hops_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldTrackHopsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="allowInsecure")
    def allow_insecure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowInsecure"))

    @allow_insecure.setter
    def allow_insecure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "allow_insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowInsecure", value)

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="certificateDomains")
    def certificate_domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificateDomains"))

    @certificate_domains.setter
    def certificate_domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "certificate_domains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateDomains", value)

    @builtins.property
    @jsii.member(jsii_name="dnsServer")
    def dns_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsServer"))

    @dns_server.setter
    def dns_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "dns_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServer", value)

    @builtins.property
    @jsii.member(jsii_name="dnsServerPort")
    def dns_server_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dnsServerPort"))

    @dns_server_port.setter
    def dns_server_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "dns_server_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServerPort", value)

    @builtins.property
    @jsii.member(jsii_name="followRedirects")
    def follow_redirects(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "followRedirects"))

    @follow_redirects.setter
    def follow_redirects(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "follow_redirects").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "followRedirects", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="noSavingResponseBody")
    def no_saving_response_body(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noSavingResponseBody"))

    @no_saving_response_body.setter
    def no_saving_response_body(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "no_saving_response_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noSavingResponseBody", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfPackets")
    def number_of_packets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfPackets"))

    @number_of_packets.setter
    def number_of_packets(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "number_of_packets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfPackets", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="servername")
    def servername(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servername"))

    @servername.setter
    def servername(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "servername").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servername", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="shouldTrackHops")
    def should_track_hops(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldTrackHops"))

    @should_track_hops.setter
    def should_track_hops(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "should_track_hops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldTrackHops", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestApiStepRequestDefinition]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRequestDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepRequestDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestDefinitionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestProxy",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "headers": "headers"},
)
class SyntheticsTestApiStepRequestProxy:
    def __init__(
        self,
        *,
        url: builtins.str,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: URL of the proxy to perform the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        :param headers: Header name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#headers SyntheticsTest#headers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestProxy.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if headers is not None:
            self._values["headers"] = headers

    @builtins.property
    def url(self) -> builtins.str:
        '''URL of the proxy to perform the test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Header name and value map.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#headers SyntheticsTest#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepRequestProxy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepRequestProxyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRequestProxyOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRequestProxyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestProxyOutputReference, "headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestProxyOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestApiStepRequestProxy]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRequestProxy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepRequestProxy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRequestProxyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRetry",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "interval": "interval"},
)
class SyntheticsTestApiStepRetry:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: Number of retries needed to consider a location as failed before sending a notification alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#count SyntheticsTest#count}
        :param interval: Interval between a failed test and the next retry in milliseconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#interval SyntheticsTest#interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRetry.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if interval is not None:
            self._values["interval"] = interval

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Number of retries needed to consider a location as failed before sending a notification alert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#count SyntheticsTest#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Interval between a failed test and the next retry in milliseconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#interval SyntheticsTest#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestApiStepRetry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestApiStepRetryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestApiStepRetryOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestApiStepRetryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRetryOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRetryOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestApiStepRetry]:
        return typing.cast(typing.Optional[SyntheticsTestApiStepRetry], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestApiStepRetry],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestApiStepRetryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestAssertion",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "type": "type",
        "property": "property",
        "target": "target",
        "targetjsonpath": "targetjsonpath",
    },
)
class SyntheticsTestAssertion:
    def __init__(
        self,
        *,
        operator: builtins.str,
        type: builtins.str,
        property: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        targetjsonpath: typing.Optional[typing.Union["SyntheticsTestAssertionTargetjsonpath", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param operator: Assertion operator. **Note** Only some combinations of ``type`` and ``operator`` are valid (please refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        :param type: Type of assertion. **Note** Only some combinations of ``type`` and ``operator`` are valid (please refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_). Valid values are ``body``, ``header``, ``statusCode``, ``certificate``, ``responseTime``, ``property``, ``recordEvery``, ``recordSome``, ``tlsVersion``, ``minTlsVersion``, ``latency``, ``packetLossPercentage``, ``packetsReceived``, ``networkHop``, ``receivedMessage``, ``grpcHealthcheckStatus``, ``connection``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param property: If assertion type is ``header``, this is the header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#property SyntheticsTest#property}
        :param target: Expected value. Depends on the assertion type, refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_ for details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#target SyntheticsTest#target}
        :param targetjsonpath: targetjsonpath block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetjsonpath SyntheticsTest#targetjsonpath}
        '''
        if isinstance(targetjsonpath, dict):
            targetjsonpath = SyntheticsTestAssertionTargetjsonpath(**targetjsonpath)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestAssertion.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument property", value=property, expected_type=type_hints["property"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument targetjsonpath", value=targetjsonpath, expected_type=type_hints["targetjsonpath"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "type": type,
        }
        if property is not None:
            self._values["property"] = property
        if target is not None:
            self._values["target"] = target
        if targetjsonpath is not None:
            self._values["targetjsonpath"] = targetjsonpath

    @builtins.property
    def operator(self) -> builtins.str:
        '''Assertion operator. **Note** Only some combinations of ``type`` and ``operator`` are valid (please refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of assertion.

        **Note** Only some combinations of ``type`` and ``operator`` are valid (please refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_). Valid values are ``body``, ``header``, ``statusCode``, ``certificate``, ``responseTime``, ``property``, ``recordEvery``, ``recordSome``, ``tlsVersion``, ``minTlsVersion``, ``latency``, ``packetLossPercentage``, ``packetsReceived``, ``networkHop``, ``receivedMessage``, ``grpcHealthcheckStatus``, ``connection``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def property(self) -> typing.Optional[builtins.str]:
        '''If assertion type is ``header``, this is the header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#property SyntheticsTest#property}
        '''
        result = self._values.get("property")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Expected value. Depends on the assertion type, refer to `Datadog documentation <https://docs.datadoghq.com/api/latest/synthetics/#create-a-test>`_ for details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#target SyntheticsTest#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targetjsonpath(
        self,
    ) -> typing.Optional["SyntheticsTestAssertionTargetjsonpath"]:
        '''targetjsonpath block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetjsonpath SyntheticsTest#targetjsonpath}
        '''
        result = self._values.get("targetjsonpath")
        return typing.cast(typing.Optional["SyntheticsTestAssertionTargetjsonpath"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestAssertion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestAssertionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestAssertionList",
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
            type_hints = typing.get_type_hints(SyntheticsTestAssertionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SyntheticsTestAssertionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestAssertionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsTestAssertionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestAssertion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestAssertion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestAssertion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestAssertionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestAssertionOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestAssertionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTargetjsonpath")
    def put_targetjsonpath(
        self,
        *,
        jsonpath: builtins.str,
        operator: builtins.str,
        targetvalue: builtins.str,
    ) -> None:
        '''
        :param jsonpath: The JSON path to assert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#jsonpath SyntheticsTest#jsonpath}
        :param operator: The specific operator to use on the path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        :param targetvalue: Expected matching value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetvalue SyntheticsTest#targetvalue}
        '''
        value = SyntheticsTestAssertionTargetjsonpath(
            jsonpath=jsonpath, operator=operator, targetvalue=targetvalue
        )

        return typing.cast(None, jsii.invoke(self, "putTargetjsonpath", [value]))

    @jsii.member(jsii_name="resetProperty")
    def reset_property(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperty", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTargetjsonpath")
    def reset_targetjsonpath(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetjsonpath", []))

    @builtins.property
    @jsii.member(jsii_name="targetjsonpath")
    def targetjsonpath(self) -> "SyntheticsTestAssertionTargetjsonpathOutputReference":
        return typing.cast("SyntheticsTestAssertionTargetjsonpathOutputReference", jsii.get(self, "targetjsonpath"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyInput")
    def property_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propertyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetjsonpathInput")
    def targetjsonpath_input(
        self,
    ) -> typing.Optional["SyntheticsTestAssertionTargetjsonpath"]:
        return typing.cast(typing.Optional["SyntheticsTestAssertionTargetjsonpath"], jsii.get(self, "targetjsonpathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @property.setter
    def property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionOutputReference, "property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "property", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsTestAssertion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsTestAssertion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsTestAssertion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestAssertionTargetjsonpath",
    jsii_struct_bases=[],
    name_mapping={
        "jsonpath": "jsonpath",
        "operator": "operator",
        "targetvalue": "targetvalue",
    },
)
class SyntheticsTestAssertionTargetjsonpath:
    def __init__(
        self,
        *,
        jsonpath: builtins.str,
        operator: builtins.str,
        targetvalue: builtins.str,
    ) -> None:
        '''
        :param jsonpath: The JSON path to assert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#jsonpath SyntheticsTest#jsonpath}
        :param operator: The specific operator to use on the path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        :param targetvalue: Expected matching value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetvalue SyntheticsTest#targetvalue}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestAssertionTargetjsonpath.__init__)
            check_type(argname="argument jsonpath", value=jsonpath, expected_type=type_hints["jsonpath"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument targetvalue", value=targetvalue, expected_type=type_hints["targetvalue"])
        self._values: typing.Dict[str, typing.Any] = {
            "jsonpath": jsonpath,
            "operator": operator,
            "targetvalue": targetvalue,
        }

    @builtins.property
    def jsonpath(self) -> builtins.str:
        '''The JSON path to assert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#jsonpath SyntheticsTest#jsonpath}
        '''
        result = self._values.get("jsonpath")
        assert result is not None, "Required property 'jsonpath' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''The specific operator to use on the path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#operator SyntheticsTest#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targetvalue(self) -> builtins.str:
        '''Expected matching value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#targetvalue SyntheticsTest#targetvalue}
        '''
        result = self._values.get("targetvalue")
        assert result is not None, "Required property 'targetvalue' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestAssertionTargetjsonpath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestAssertionTargetjsonpathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestAssertionTargetjsonpathOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestAssertionTargetjsonpathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="jsonpathInput")
    def jsonpath_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonpathInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="targetvalueInput")
    def targetvalue_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetvalueInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonpath")
    def jsonpath(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonpath"))

    @jsonpath.setter
    def jsonpath(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionTargetjsonpathOutputReference, "jsonpath").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonpath", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionTargetjsonpathOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="targetvalue")
    def targetvalue(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetvalue"))

    @targetvalue.setter
    def targetvalue(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionTargetjsonpathOutputReference, "targetvalue").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetvalue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestAssertionTargetjsonpath]:
        return typing.cast(typing.Optional[SyntheticsTestAssertionTargetjsonpath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestAssertionTargetjsonpath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestAssertionTargetjsonpathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStep",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "params": "params",
        "type": "type",
        "allow_failure": "allowFailure",
        "force_element_update": "forceElementUpdate",
        "is_critical": "isCritical",
        "timeout": "timeout",
    },
)
class SyntheticsTestBrowserStep:
    def __init__(
        self,
        *,
        name: builtins.str,
        params: typing.Union["SyntheticsTestBrowserStepParams", typing.Dict[str, typing.Any]],
        type: builtins.str,
        allow_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_element_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_critical: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Name of the step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        :param params: params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#params SyntheticsTest#params}
        :param type: Type of the step. Valid values are ``assertCurrentUrl``, ``assertElementAttribute``, ``assertElementContent``, ``assertElementPresent``, ``assertEmail``, ``assertFileDownload``, ``assertFromJavascript``, ``assertPageContains``, ``assertPageLacks``, ``click``, ``extractFromJavascript``, ``extractVariable``, ``goToEmailLink``, ``goToUrl``, ``goToUrlAndMeasureTti``, ``hover``, ``playSubTest``, ``pressKey``, ``refresh``, ``runApiTest``, ``scroll``, ``selectOption``, ``typeText``, ``uploadFiles``, ``wait``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param allow_failure: Determines if the step should be allowed to fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_failure SyntheticsTest#allow_failure}
        :param force_element_update: Force update of the "element" parameter for the step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#force_element_update SyntheticsTest#force_element_update}
        :param is_critical: Determines whether or not to consider the entire test as failed if this step fails. Can be used only if ``allow_failure`` is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#is_critical SyntheticsTest#is_critical}
        :param timeout: Used to override the default timeout of a step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#timeout SyntheticsTest#timeout}
        '''
        if isinstance(params, dict):
            params = SyntheticsTestBrowserStepParams(**params)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStep.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument allow_failure", value=allow_failure, expected_type=type_hints["allow_failure"])
            check_type(argname="argument force_element_update", value=force_element_update, expected_type=type_hints["force_element_update"])
            check_type(argname="argument is_critical", value=is_critical, expected_type=type_hints["is_critical"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "params": params,
            "type": type,
        }
        if allow_failure is not None:
            self._values["allow_failure"] = allow_failure
        if force_element_update is not None:
            self._values["force_element_update"] = force_element_update
        if is_critical is not None:
            self._values["is_critical"] = is_critical
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def params(self) -> "SyntheticsTestBrowserStepParams":
        '''params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#params SyntheticsTest#params}
        '''
        result = self._values.get("params")
        assert result is not None, "Required property 'params' is missing"
        return typing.cast("SyntheticsTestBrowserStepParams", result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the step.

        Valid values are ``assertCurrentUrl``, ``assertElementAttribute``, ``assertElementContent``, ``assertElementPresent``, ``assertEmail``, ``assertFileDownload``, ``assertFromJavascript``, ``assertPageContains``, ``assertPageLacks``, ``click``, ``extractFromJavascript``, ``extractVariable``, ``goToEmailLink``, ``goToUrl``, ``goToUrlAndMeasureTti``, ``hover``, ``playSubTest``, ``pressKey``, ``refresh``, ``runApiTest``, ``scroll``, ``selectOption``, ``typeText``, ``uploadFiles``, ``wait``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines if the step should be allowed to fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_failure SyntheticsTest#allow_failure}
        '''
        result = self._values.get("allow_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def force_element_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Force update of the "element" parameter for the step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#force_element_update SyntheticsTest#force_element_update}
        '''
        result = self._values.get("force_element_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_critical(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines whether or not to consider the entire test as failed if this step fails.

        Can be used only if ``allow_failure`` is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#is_critical SyntheticsTest#is_critical}
        '''
        result = self._values.get("is_critical")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Used to override the default timeout of a step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#timeout SyntheticsTest#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestBrowserStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestBrowserStepList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepList",
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
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SyntheticsTestBrowserStepOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsTestBrowserStepOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserStep]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserStep]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserStep]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestBrowserStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParams")
    def put_params(
        self,
        *,
        attribute: typing.Optional[builtins.str] = None,
        check: typing.Optional[builtins.str] = None,
        click_type: typing.Optional[builtins.str] = None,
        code: typing.Optional[builtins.str] = None,
        delay: typing.Optional[jsii.Number] = None,
        element: typing.Optional[builtins.str] = None,
        element_user_locator: typing.Optional[typing.Union["SyntheticsTestBrowserStepParamsElementUserLocator", typing.Dict[str, typing.Any]]] = None,
        email: typing.Optional[builtins.str] = None,
        file: typing.Optional[builtins.str] = None,
        files: typing.Optional[builtins.str] = None,
        modifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        playing_tab_id: typing.Optional[builtins.str] = None,
        request: typing.Optional[builtins.str] = None,
        subtest_public_id: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
        variable: typing.Optional[typing.Union["SyntheticsTestBrowserStepParamsVariable", typing.Dict[str, typing.Any]]] = None,
        with_click: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        x: typing.Optional[jsii.Number] = None,
        y: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param attribute: Name of the attribute to use for an "assert attribute" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#attribute SyntheticsTest#attribute}
        :param check: Check type to use for an assertion step. Valid values are ``equals``, ``notEquals``, ``contains``, ``notContains``, ``startsWith``, ``notStartsWith``, ``greater``, ``lower``, ``greaterEquals``, ``lowerEquals``, ``matchRegex``, ``between``, ``isEmpty``, ``notIsEmpty``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#check SyntheticsTest#check}
        :param click_type: Type of click to use for a "click" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#click_type SyntheticsTest#click_type}
        :param code: Javascript code to use for the step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#code SyntheticsTest#code}
        :param delay: Delay between each key stroke for a "type test" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#delay SyntheticsTest#delay}
        :param element: Element to use for the step, json encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#element SyntheticsTest#element}
        :param element_user_locator: element_user_locator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#element_user_locator SyntheticsTest#element_user_locator}
        :param email: Details of the email for an "assert email" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#email SyntheticsTest#email}
        :param file: For an "assert download" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#file SyntheticsTest#file}
        :param files: Details of the files for an "upload files" step, json encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#files SyntheticsTest#files}
        :param modifiers: Modifier to use for a "press key" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#modifiers SyntheticsTest#modifiers}
        :param playing_tab_id: ID of the tab to play the subtest. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#playing_tab_id SyntheticsTest#playing_tab_id}
        :param request: Request for an API step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request SyntheticsTest#request}
        :param subtest_public_id: ID of the Synthetics test to use as subtest. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#subtest_public_id SyntheticsTest#subtest_public_id}
        :param value: Value of the step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        :param variable: variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#variable SyntheticsTest#variable}
        :param with_click: For "file upload" steps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#with_click SyntheticsTest#with_click}
        :param x: X coordinates for a "scroll step". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#x SyntheticsTest#x}
        :param y: Y coordinates for a "scroll step". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#y SyntheticsTest#y}
        '''
        value_ = SyntheticsTestBrowserStepParams(
            attribute=attribute,
            check=check,
            click_type=click_type,
            code=code,
            delay=delay,
            element=element,
            element_user_locator=element_user_locator,
            email=email,
            file=file,
            files=files,
            modifiers=modifiers,
            playing_tab_id=playing_tab_id,
            request=request,
            subtest_public_id=subtest_public_id,
            value=value,
            variable=variable,
            with_click=with_click,
            x=x,
            y=y,
        )

        return typing.cast(None, jsii.invoke(self, "putParams", [value_]))

    @jsii.member(jsii_name="resetAllowFailure")
    def reset_allow_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowFailure", []))

    @jsii.member(jsii_name="resetForceElementUpdate")
    def reset_force_element_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceElementUpdate", []))

    @jsii.member(jsii_name="resetIsCritical")
    def reset_is_critical(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsCritical", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="params")
    def params(self) -> "SyntheticsTestBrowserStepParamsOutputReference":
        return typing.cast("SyntheticsTestBrowserStepParamsOutputReference", jsii.get(self, "params"))

    @builtins.property
    @jsii.member(jsii_name="allowFailureInput")
    def allow_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="forceElementUpdateInput")
    def force_element_update_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceElementUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="isCriticalInput")
    def is_critical_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isCriticalInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="paramsInput")
    def params_input(self) -> typing.Optional["SyntheticsTestBrowserStepParams"]:
        return typing.cast(typing.Optional["SyntheticsTestBrowserStepParams"], jsii.get(self, "paramsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowFailure")
    def allow_failure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowFailure"))

    @allow_failure.setter
    def allow_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepOutputReference, "allow_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowFailure", value)

    @builtins.property
    @jsii.member(jsii_name="forceElementUpdate")
    def force_element_update(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceElementUpdate"))

    @force_element_update.setter
    def force_element_update(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepOutputReference, "force_element_update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceElementUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="isCritical")
    def is_critical(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isCritical"))

    @is_critical.setter
    def is_critical(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepOutputReference, "is_critical").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCritical", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsTestBrowserStep, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsTestBrowserStep, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsTestBrowserStep, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepParams",
    jsii_struct_bases=[],
    name_mapping={
        "attribute": "attribute",
        "check": "check",
        "click_type": "clickType",
        "code": "code",
        "delay": "delay",
        "element": "element",
        "element_user_locator": "elementUserLocator",
        "email": "email",
        "file": "file",
        "files": "files",
        "modifiers": "modifiers",
        "playing_tab_id": "playingTabId",
        "request": "request",
        "subtest_public_id": "subtestPublicId",
        "value": "value",
        "variable": "variable",
        "with_click": "withClick",
        "x": "x",
        "y": "y",
    },
)
class SyntheticsTestBrowserStepParams:
    def __init__(
        self,
        *,
        attribute: typing.Optional[builtins.str] = None,
        check: typing.Optional[builtins.str] = None,
        click_type: typing.Optional[builtins.str] = None,
        code: typing.Optional[builtins.str] = None,
        delay: typing.Optional[jsii.Number] = None,
        element: typing.Optional[builtins.str] = None,
        element_user_locator: typing.Optional[typing.Union["SyntheticsTestBrowserStepParamsElementUserLocator", typing.Dict[str, typing.Any]]] = None,
        email: typing.Optional[builtins.str] = None,
        file: typing.Optional[builtins.str] = None,
        files: typing.Optional[builtins.str] = None,
        modifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        playing_tab_id: typing.Optional[builtins.str] = None,
        request: typing.Optional[builtins.str] = None,
        subtest_public_id: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
        variable: typing.Optional[typing.Union["SyntheticsTestBrowserStepParamsVariable", typing.Dict[str, typing.Any]]] = None,
        with_click: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        x: typing.Optional[jsii.Number] = None,
        y: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param attribute: Name of the attribute to use for an "assert attribute" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#attribute SyntheticsTest#attribute}
        :param check: Check type to use for an assertion step. Valid values are ``equals``, ``notEquals``, ``contains``, ``notContains``, ``startsWith``, ``notStartsWith``, ``greater``, ``lower``, ``greaterEquals``, ``lowerEquals``, ``matchRegex``, ``between``, ``isEmpty``, ``notIsEmpty``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#check SyntheticsTest#check}
        :param click_type: Type of click to use for a "click" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#click_type SyntheticsTest#click_type}
        :param code: Javascript code to use for the step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#code SyntheticsTest#code}
        :param delay: Delay between each key stroke for a "type test" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#delay SyntheticsTest#delay}
        :param element: Element to use for the step, json encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#element SyntheticsTest#element}
        :param element_user_locator: element_user_locator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#element_user_locator SyntheticsTest#element_user_locator}
        :param email: Details of the email for an "assert email" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#email SyntheticsTest#email}
        :param file: For an "assert download" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#file SyntheticsTest#file}
        :param files: Details of the files for an "upload files" step, json encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#files SyntheticsTest#files}
        :param modifiers: Modifier to use for a "press key" step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#modifiers SyntheticsTest#modifiers}
        :param playing_tab_id: ID of the tab to play the subtest. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#playing_tab_id SyntheticsTest#playing_tab_id}
        :param request: Request for an API step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request SyntheticsTest#request}
        :param subtest_public_id: ID of the Synthetics test to use as subtest. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#subtest_public_id SyntheticsTest#subtest_public_id}
        :param value: Value of the step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        :param variable: variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#variable SyntheticsTest#variable}
        :param with_click: For "file upload" steps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#with_click SyntheticsTest#with_click}
        :param x: X coordinates for a "scroll step". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#x SyntheticsTest#x}
        :param y: Y coordinates for a "scroll step". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#y SyntheticsTest#y}
        '''
        if isinstance(element_user_locator, dict):
            element_user_locator = SyntheticsTestBrowserStepParamsElementUserLocator(**element_user_locator)
        if isinstance(variable, dict):
            variable = SyntheticsTestBrowserStepParamsVariable(**variable)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepParams.__init__)
            check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
            check_type(argname="argument check", value=check, expected_type=type_hints["check"])
            check_type(argname="argument click_type", value=click_type, expected_type=type_hints["click_type"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
            check_type(argname="argument element", value=element, expected_type=type_hints["element"])
            check_type(argname="argument element_user_locator", value=element_user_locator, expected_type=type_hints["element_user_locator"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument files", value=files, expected_type=type_hints["files"])
            check_type(argname="argument modifiers", value=modifiers, expected_type=type_hints["modifiers"])
            check_type(argname="argument playing_tab_id", value=playing_tab_id, expected_type=type_hints["playing_tab_id"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
            check_type(argname="argument subtest_public_id", value=subtest_public_id, expected_type=type_hints["subtest_public_id"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument with_click", value=with_click, expected_type=type_hints["with_click"])
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
            check_type(argname="argument y", value=y, expected_type=type_hints["y"])
        self._values: typing.Dict[str, typing.Any] = {}
        if attribute is not None:
            self._values["attribute"] = attribute
        if check is not None:
            self._values["check"] = check
        if click_type is not None:
            self._values["click_type"] = click_type
        if code is not None:
            self._values["code"] = code
        if delay is not None:
            self._values["delay"] = delay
        if element is not None:
            self._values["element"] = element
        if element_user_locator is not None:
            self._values["element_user_locator"] = element_user_locator
        if email is not None:
            self._values["email"] = email
        if file is not None:
            self._values["file"] = file
        if files is not None:
            self._values["files"] = files
        if modifiers is not None:
            self._values["modifiers"] = modifiers
        if playing_tab_id is not None:
            self._values["playing_tab_id"] = playing_tab_id
        if request is not None:
            self._values["request"] = request
        if subtest_public_id is not None:
            self._values["subtest_public_id"] = subtest_public_id
        if value is not None:
            self._values["value"] = value
        if variable is not None:
            self._values["variable"] = variable
        if with_click is not None:
            self._values["with_click"] = with_click
        if x is not None:
            self._values["x"] = x
        if y is not None:
            self._values["y"] = y

    @builtins.property
    def attribute(self) -> typing.Optional[builtins.str]:
        '''Name of the attribute to use for an "assert attribute" step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#attribute SyntheticsTest#attribute}
        '''
        result = self._values.get("attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def check(self) -> typing.Optional[builtins.str]:
        '''Check type to use for an assertion step.

        Valid values are ``equals``, ``notEquals``, ``contains``, ``notContains``, ``startsWith``, ``notStartsWith``, ``greater``, ``lower``, ``greaterEquals``, ``lowerEquals``, ``matchRegex``, ``between``, ``isEmpty``, ``notIsEmpty``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#check SyntheticsTest#check}
        '''
        result = self._values.get("check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def click_type(self) -> typing.Optional[builtins.str]:
        '''Type of click to use for a "click" step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#click_type SyntheticsTest#click_type}
        '''
        result = self._values.get("click_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''Javascript code to use for the step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#code SyntheticsTest#code}
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delay(self) -> typing.Optional[jsii.Number]:
        '''Delay between each key stroke for a "type test" step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#delay SyntheticsTest#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def element(self) -> typing.Optional[builtins.str]:
        '''Element to use for the step, json encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#element SyntheticsTest#element}
        '''
        result = self._values.get("element")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def element_user_locator(
        self,
    ) -> typing.Optional["SyntheticsTestBrowserStepParamsElementUserLocator"]:
        '''element_user_locator block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#element_user_locator SyntheticsTest#element_user_locator}
        '''
        result = self._values.get("element_user_locator")
        return typing.cast(typing.Optional["SyntheticsTestBrowserStepParamsElementUserLocator"], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Details of the email for an "assert email" step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#email SyntheticsTest#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file(self) -> typing.Optional[builtins.str]:
        '''For an "assert download" step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#file SyntheticsTest#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def files(self) -> typing.Optional[builtins.str]:
        '''Details of the files for an "upload files" step, json encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#files SyntheticsTest#files}
        '''
        result = self._values.get("files")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def modifiers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Modifier to use for a "press key" step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#modifiers SyntheticsTest#modifiers}
        '''
        result = self._values.get("modifiers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def playing_tab_id(self) -> typing.Optional[builtins.str]:
        '''ID of the tab to play the subtest.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#playing_tab_id SyntheticsTest#playing_tab_id}
        '''
        result = self._values.get("playing_tab_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request(self) -> typing.Optional[builtins.str]:
        '''Request for an API step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request SyntheticsTest#request}
        '''
        result = self._values.get("request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subtest_public_id(self) -> typing.Optional[builtins.str]:
        '''ID of the Synthetics test to use as subtest.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#subtest_public_id SyntheticsTest#subtest_public_id}
        '''
        result = self._values.get("subtest_public_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value of the step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variable(self) -> typing.Optional["SyntheticsTestBrowserStepParamsVariable"]:
        '''variable block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#variable SyntheticsTest#variable}
        '''
        result = self._values.get("variable")
        return typing.cast(typing.Optional["SyntheticsTestBrowserStepParamsVariable"], result)

    @builtins.property
    def with_click(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''For "file upload" steps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#with_click SyntheticsTest#with_click}
        '''
        result = self._values.get("with_click")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def x(self) -> typing.Optional[jsii.Number]:
        '''X coordinates for a "scroll step".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#x SyntheticsTest#x}
        '''
        result = self._values.get("x")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def y(self) -> typing.Optional[jsii.Number]:
        '''Y coordinates for a "scroll step".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#y SyntheticsTest#y}
        '''
        result = self._values.get("y")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestBrowserStepParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepParamsElementUserLocator",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "fail_test_on_cannot_locate": "failTestOnCannotLocate",
    },
)
class SyntheticsTestBrowserStepParamsElementUserLocator:
    def __init__(
        self,
        *,
        value: typing.Union["SyntheticsTestBrowserStepParamsElementUserLocatorValue", typing.Dict[str, typing.Any]],
        fail_test_on_cannot_locate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param value: value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        :param fail_test_on_cannot_locate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#fail_test_on_cannot_locate SyntheticsTest#fail_test_on_cannot_locate}.
        '''
        if isinstance(value, dict):
            value = SyntheticsTestBrowserStepParamsElementUserLocatorValue(**value)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepParamsElementUserLocator.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument fail_test_on_cannot_locate", value=fail_test_on_cannot_locate, expected_type=type_hints["fail_test_on_cannot_locate"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if fail_test_on_cannot_locate is not None:
            self._values["fail_test_on_cannot_locate"] = fail_test_on_cannot_locate

    @builtins.property
    def value(self) -> "SyntheticsTestBrowserStepParamsElementUserLocatorValue":
        '''value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast("SyntheticsTestBrowserStepParamsElementUserLocatorValue", result)

    @builtins.property
    def fail_test_on_cannot_locate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#fail_test_on_cannot_locate SyntheticsTest#fail_test_on_cannot_locate}.'''
        result = self._values.get("fail_test_on_cannot_locate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestBrowserStepParamsElementUserLocator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestBrowserStepParamsElementUserLocatorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepParamsElementUserLocatorOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepParamsElementUserLocatorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putValue")
    def put_value(
        self,
        *,
        value: builtins.str,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}.
        '''
        value_ = SyntheticsTestBrowserStepParamsElementUserLocatorValue(
            value=value, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putValue", [value_]))

    @jsii.member(jsii_name="resetFailTestOnCannotLocate")
    def reset_fail_test_on_cannot_locate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailTestOnCannotLocate", []))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(
        self,
    ) -> "SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference":
        return typing.cast("SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference", jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="failTestOnCannotLocateInput")
    def fail_test_on_cannot_locate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failTestOnCannotLocateInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(
        self,
    ) -> typing.Optional["SyntheticsTestBrowserStepParamsElementUserLocatorValue"]:
        return typing.cast(typing.Optional["SyntheticsTestBrowserStepParamsElementUserLocatorValue"], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="failTestOnCannotLocate")
    def fail_test_on_cannot_locate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failTestOnCannotLocate"))

    @fail_test_on_cannot_locate.setter
    def fail_test_on_cannot_locate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsElementUserLocatorOutputReference, "fail_test_on_cannot_locate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failTestOnCannotLocate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestBrowserStepParamsElementUserLocator]:
        return typing.cast(typing.Optional[SyntheticsTestBrowserStepParamsElementUserLocator], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestBrowserStepParamsElementUserLocator],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsElementUserLocatorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepParamsElementUserLocatorValue",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "type": "type"},
)
class SyntheticsTestBrowserStepParamsElementUserLocatorValue:
    def __init__(
        self,
        *,
        value: builtins.str,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepParamsElementUserLocatorValue.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestBrowserStepParamsElementUserLocatorValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestBrowserStepParamsElementUserLocatorValue]:
        return typing.cast(typing.Optional[SyntheticsTestBrowserStepParamsElementUserLocatorValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestBrowserStepParamsElementUserLocatorValue],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestBrowserStepParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepParamsOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepParamsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putElementUserLocator")
    def put_element_user_locator(
        self,
        *,
        value: typing.Union[SyntheticsTestBrowserStepParamsElementUserLocatorValue, typing.Dict[str, typing.Any]],
        fail_test_on_cannot_locate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param value: value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#value SyntheticsTest#value}
        :param fail_test_on_cannot_locate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#fail_test_on_cannot_locate SyntheticsTest#fail_test_on_cannot_locate}.
        '''
        value_ = SyntheticsTestBrowserStepParamsElementUserLocator(
            value=value, fail_test_on_cannot_locate=fail_test_on_cannot_locate
        )

        return typing.cast(None, jsii.invoke(self, "putElementUserLocator", [value_]))

    @jsii.member(jsii_name="putVariable")
    def put_variable(
        self,
        *,
        example: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param example: Example of the extracted variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#example SyntheticsTest#example}
        :param name: Name of the extracted variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        '''
        value = SyntheticsTestBrowserStepParamsVariable(example=example, name=name)

        return typing.cast(None, jsii.invoke(self, "putVariable", [value]))

    @jsii.member(jsii_name="resetAttribute")
    def reset_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttribute", []))

    @jsii.member(jsii_name="resetCheck")
    def reset_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheck", []))

    @jsii.member(jsii_name="resetClickType")
    def reset_click_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClickType", []))

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @jsii.member(jsii_name="resetElement")
    def reset_element(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElement", []))

    @jsii.member(jsii_name="resetElementUserLocator")
    def reset_element_user_locator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElementUserLocator", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetFiles")
    def reset_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFiles", []))

    @jsii.member(jsii_name="resetModifiers")
    def reset_modifiers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModifiers", []))

    @jsii.member(jsii_name="resetPlayingTabId")
    def reset_playing_tab_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlayingTabId", []))

    @jsii.member(jsii_name="resetRequest")
    def reset_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequest", []))

    @jsii.member(jsii_name="resetSubtestPublicId")
    def reset_subtest_public_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubtestPublicId", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetVariable")
    def reset_variable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariable", []))

    @jsii.member(jsii_name="resetWithClick")
    def reset_with_click(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithClick", []))

    @jsii.member(jsii_name="resetX")
    def reset_x(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetX", []))

    @jsii.member(jsii_name="resetY")
    def reset_y(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetY", []))

    @builtins.property
    @jsii.member(jsii_name="elementUserLocator")
    def element_user_locator(
        self,
    ) -> SyntheticsTestBrowserStepParamsElementUserLocatorOutputReference:
        return typing.cast(SyntheticsTestBrowserStepParamsElementUserLocatorOutputReference, jsii.get(self, "elementUserLocator"))

    @builtins.property
    @jsii.member(jsii_name="variable")
    def variable(self) -> "SyntheticsTestBrowserStepParamsVariableOutputReference":
        return typing.cast("SyntheticsTestBrowserStepParamsVariableOutputReference", jsii.get(self, "variable"))

    @builtins.property
    @jsii.member(jsii_name="attributeInput")
    def attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeInput"))

    @builtins.property
    @jsii.member(jsii_name="checkInput")
    def check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkInput"))

    @builtins.property
    @jsii.member(jsii_name="clickTypeInput")
    def click_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clickTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="elementInput")
    def element_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elementInput"))

    @builtins.property
    @jsii.member(jsii_name="elementUserLocatorInput")
    def element_user_locator_input(
        self,
    ) -> typing.Optional[SyntheticsTestBrowserStepParamsElementUserLocator]:
        return typing.cast(typing.Optional[SyntheticsTestBrowserStepParamsElementUserLocator], jsii.get(self, "elementUserLocatorInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="filesInput")
    def files_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filesInput"))

    @builtins.property
    @jsii.member(jsii_name="modifiersInput")
    def modifiers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "modifiersInput"))

    @builtins.property
    @jsii.member(jsii_name="playingTabIdInput")
    def playing_tab_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "playingTabIdInput"))

    @builtins.property
    @jsii.member(jsii_name="requestInput")
    def request_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestInput"))

    @builtins.property
    @jsii.member(jsii_name="subtestPublicIdInput")
    def subtest_public_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subtestPublicIdInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="variableInput")
    def variable_input(
        self,
    ) -> typing.Optional["SyntheticsTestBrowserStepParamsVariable"]:
        return typing.cast(typing.Optional["SyntheticsTestBrowserStepParamsVariable"], jsii.get(self, "variableInput"))

    @builtins.property
    @jsii.member(jsii_name="withClickInput")
    def with_click_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withClickInput"))

    @builtins.property
    @jsii.member(jsii_name="xInput")
    def x_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "xInput"))

    @builtins.property
    @jsii.member(jsii_name="yInput")
    def y_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "yInput"))

    @builtins.property
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attribute"))

    @attribute.setter
    def attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attribute", value)

    @builtins.property
    @jsii.member(jsii_name="check")
    def check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "check"))

    @check.setter
    def check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "check", value)

    @builtins.property
    @jsii.member(jsii_name="clickType")
    def click_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clickType"))

    @click_type.setter
    def click_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "click_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clickType", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "code"))

    @code.setter
    def code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "delay"))

    @delay.setter
    def delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delay", value)

    @builtins.property
    @jsii.member(jsii_name="element")
    def element(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "element"))

    @element.setter
    def element(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "element").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "element", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

    @builtins.property
    @jsii.member(jsii_name="files")
    def files(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "files"))

    @files.setter
    def files(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "files").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "files", value)

    @builtins.property
    @jsii.member(jsii_name="modifiers")
    def modifiers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "modifiers"))

    @modifiers.setter
    def modifiers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "modifiers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modifiers", value)

    @builtins.property
    @jsii.member(jsii_name="playingTabId")
    def playing_tab_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "playingTabId"))

    @playing_tab_id.setter
    def playing_tab_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "playing_tab_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "playingTabId", value)

    @builtins.property
    @jsii.member(jsii_name="request")
    def request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "request"))

    @request.setter
    def request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "request", value)

    @builtins.property
    @jsii.member(jsii_name="subtestPublicId")
    def subtest_public_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subtestPublicId"))

    @subtest_public_id.setter
    def subtest_public_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "subtest_public_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subtestPublicId", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="withClick")
    def with_click(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withClick"))

    @with_click.setter
    def with_click(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "with_click").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withClick", value)

    @builtins.property
    @jsii.member(jsii_name="x")
    def x(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "x"))

    @x.setter
    def x(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "x").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "x", value)

    @builtins.property
    @jsii.member(jsii_name="y")
    def y(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "y"))

    @y.setter
    def y(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "y").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "y", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestBrowserStepParams]:
        return typing.cast(typing.Optional[SyntheticsTestBrowserStepParams], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestBrowserStepParams],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepParamsVariable",
    jsii_struct_bases=[],
    name_mapping={"example": "example", "name": "name"},
)
class SyntheticsTestBrowserStepParamsVariable:
    def __init__(
        self,
        *,
        example: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param example: Example of the extracted variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#example SyntheticsTest#example}
        :param name: Name of the extracted variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepParamsVariable.__init__)
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if example is not None:
            self._values["example"] = example
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def example(self) -> typing.Optional[builtins.str]:
        '''Example of the extracted variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#example SyntheticsTest#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the extracted variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestBrowserStepParamsVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestBrowserStepParamsVariableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserStepParamsVariableOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestBrowserStepParamsVariableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "example"))

    @example.setter
    def example(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsVariableOutputReference, "example").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "example", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsVariableOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestBrowserStepParamsVariable]:
        return typing.cast(typing.Optional[SyntheticsTestBrowserStepParamsVariable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestBrowserStepParamsVariable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserStepParamsVariableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserVariable",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "example": "example",
        "id": "id",
        "pattern": "pattern",
    },
)
class SyntheticsTestBrowserVariable:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        example: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        pattern: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        :param type: Type of browser test variable. Valid values are ``element``, ``email``, ``global``, ``javascript``, ``text``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param example: Example for the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#example SyntheticsTest#example}
        :param id: ID of the global variable to use. This is actually only used (and required) in the case of using a variable of type ``global``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#id SyntheticsTest#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pattern: Pattern of the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#pattern SyntheticsTest#pattern}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestBrowserVariable.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if example is not None:
            self._values["example"] = example
        if id is not None:
            self._values["id"] = id
        if pattern is not None:
            self._values["pattern"] = pattern

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of browser test variable. Valid values are ``element``, ``email``, ``global``, ``javascript``, ``text``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def example(self) -> typing.Optional[builtins.str]:
        '''Example for the variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#example SyntheticsTest#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''ID of the global variable to use.

        This is actually only used (and required) in the case of using a variable of type ``global``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#id SyntheticsTest#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pattern(self) -> typing.Optional[builtins.str]:
        '''Pattern of the variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#pattern SyntheticsTest#pattern}
        '''
        result = self._values.get("pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestBrowserVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestBrowserVariableList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserVariableList",
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
            type_hints = typing.get_type_hints(SyntheticsTestBrowserVariableList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SyntheticsTestBrowserVariableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestBrowserVariableList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsTestBrowserVariableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserVariable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserVariable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserVariable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestBrowserVariableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestBrowserVariableOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestBrowserVariableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPattern")
    def reset_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPattern", []))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patternInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "example"))

    @example.setter
    def example(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableOutputReference, "example").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "example", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableOutputReference, "pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsTestBrowserVariable, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsTestBrowserVariable, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsTestBrowserVariable, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestBrowserVariableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "locations": "locations",
        "name": "name",
        "status": "status",
        "type": "type",
        "api_step": "apiStep",
        "assertion": "assertion",
        "browser_step": "browserStep",
        "browser_variable": "browserVariable",
        "config_variable": "configVariable",
        "device_ids": "deviceIds",
        "id": "id",
        "message": "message",
        "options_list": "optionsList",
        "request_basicauth": "requestBasicauth",
        "request_client_certificate": "requestClientCertificate",
        "request_definition": "requestDefinition",
        "request_headers": "requestHeaders",
        "request_proxy": "requestProxy",
        "request_query": "requestQuery",
        "set_cookie": "setCookie",
        "subtype": "subtype",
        "tags": "tags",
    },
)
class SyntheticsTestConfig(cdktf.TerraformMetaArguments):
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
        locations: typing.Sequence[builtins.str],
        name: builtins.str,
        status: builtins.str,
        type: builtins.str,
        api_step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsTestApiStep, typing.Dict[str, typing.Any]]]]] = None,
        assertion: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsTestAssertion, typing.Dict[str, typing.Any]]]]] = None,
        browser_step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsTestBrowserStep, typing.Dict[str, typing.Any]]]]] = None,
        browser_variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SyntheticsTestBrowserVariable, typing.Dict[str, typing.Any]]]]] = None,
        config_variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SyntheticsTestConfigVariable", typing.Dict[str, typing.Any]]]]] = None,
        device_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        options_list: typing.Optional[typing.Union["SyntheticsTestOptionsList", typing.Dict[str, typing.Any]]] = None,
        request_basicauth: typing.Optional[typing.Union["SyntheticsTestRequestBasicauth", typing.Dict[str, typing.Any]]] = None,
        request_client_certificate: typing.Optional[typing.Union["SyntheticsTestRequestClientCertificate", typing.Dict[str, typing.Any]]] = None,
        request_definition: typing.Optional[typing.Union["SyntheticsTestRequestDefinition", typing.Dict[str, typing.Any]]] = None,
        request_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_proxy: typing.Optional[typing.Union["SyntheticsTestRequestProxy", typing.Dict[str, typing.Any]]] = None,
        request_query: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        set_cookie: typing.Optional[builtins.str] = None,
        subtype: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param locations: Array of locations used to run the test. Refer to `the Datadog Synthetics location data source <https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/synthetics_locations>`_ to retrieve the list of locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#locations SyntheticsTest#locations}
        :param name: Name of Datadog synthetics test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        :param status: Define whether you want to start (``live``) or pause (``paused``) a Synthetic test. Valid values are ``live``, ``paused``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#status SyntheticsTest#status}
        :param type: Synthetics test type. Valid values are ``api``, ``browser``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param api_step: api_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#api_step SyntheticsTest#api_step}
        :param assertion: assertion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#assertion SyntheticsTest#assertion}
        :param browser_step: browser_step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#browser_step SyntheticsTest#browser_step}
        :param browser_variable: browser_variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#browser_variable SyntheticsTest#browser_variable}
        :param config_variable: config_variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#config_variable SyntheticsTest#config_variable}
        :param device_ids: Required if ``type = "browser"``. Array with the different device IDs used to run the test. Valid values are ``laptop_large``, ``tablet``, ``mobile_small``, ``chrome.laptop_large``, ``chrome.tablet``, ``chrome.mobile_small``, ``firefox.laptop_large``, ``firefox.tablet``, ``firefox.mobile_small``, ``edge.laptop_large``, ``edge.tablet``, ``edge.mobile_small``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#device_ids SyntheticsTest#device_ids}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#id SyntheticsTest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param message: A message to include with notifications for this synthetics test. Email notifications can be sent to specific users by using the same ``@username`` notation as events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        :param options_list: options_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#options_list SyntheticsTest#options_list}
        :param request_basicauth: request_basicauth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_basicauth SyntheticsTest#request_basicauth}
        :param request_client_certificate: request_client_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_client_certificate SyntheticsTest#request_client_certificate}
        :param request_definition: request_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_definition SyntheticsTest#request_definition}
        :param request_headers: Header name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_headers SyntheticsTest#request_headers}
        :param request_proxy: request_proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_proxy SyntheticsTest#request_proxy}
        :param request_query: Query arguments name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_query SyntheticsTest#request_query}
        :param set_cookie: Cookies to be used for a browser test request, using the `Set-Cookie <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie>`_ syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#set_cookie SyntheticsTest#set_cookie}
        :param subtype: The subtype of the Synthetic API test. Defaults to ``http``. Valid values are ``http``, ``ssl``, ``tcp``, ``dns``, ``multi``, ``icmp``, ``udp``, ``websocket``, ``grpc``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#subtype SyntheticsTest#subtype}
        :param tags: A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI. Default is an empty list (``[]``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#tags SyntheticsTest#tags}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(options_list, dict):
            options_list = SyntheticsTestOptionsList(**options_list)
        if isinstance(request_basicauth, dict):
            request_basicauth = SyntheticsTestRequestBasicauth(**request_basicauth)
        if isinstance(request_client_certificate, dict):
            request_client_certificate = SyntheticsTestRequestClientCertificate(**request_client_certificate)
        if isinstance(request_definition, dict):
            request_definition = SyntheticsTestRequestDefinition(**request_definition)
        if isinstance(request_proxy, dict):
            request_proxy = SyntheticsTestRequestProxy(**request_proxy)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument api_step", value=api_step, expected_type=type_hints["api_step"])
            check_type(argname="argument assertion", value=assertion, expected_type=type_hints["assertion"])
            check_type(argname="argument browser_step", value=browser_step, expected_type=type_hints["browser_step"])
            check_type(argname="argument browser_variable", value=browser_variable, expected_type=type_hints["browser_variable"])
            check_type(argname="argument config_variable", value=config_variable, expected_type=type_hints["config_variable"])
            check_type(argname="argument device_ids", value=device_ids, expected_type=type_hints["device_ids"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument options_list", value=options_list, expected_type=type_hints["options_list"])
            check_type(argname="argument request_basicauth", value=request_basicauth, expected_type=type_hints["request_basicauth"])
            check_type(argname="argument request_client_certificate", value=request_client_certificate, expected_type=type_hints["request_client_certificate"])
            check_type(argname="argument request_definition", value=request_definition, expected_type=type_hints["request_definition"])
            check_type(argname="argument request_headers", value=request_headers, expected_type=type_hints["request_headers"])
            check_type(argname="argument request_proxy", value=request_proxy, expected_type=type_hints["request_proxy"])
            check_type(argname="argument request_query", value=request_query, expected_type=type_hints["request_query"])
            check_type(argname="argument set_cookie", value=set_cookie, expected_type=type_hints["set_cookie"])
            check_type(argname="argument subtype", value=subtype, expected_type=type_hints["subtype"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "locations": locations,
            "name": name,
            "status": status,
            "type": type,
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
        if api_step is not None:
            self._values["api_step"] = api_step
        if assertion is not None:
            self._values["assertion"] = assertion
        if browser_step is not None:
            self._values["browser_step"] = browser_step
        if browser_variable is not None:
            self._values["browser_variable"] = browser_variable
        if config_variable is not None:
            self._values["config_variable"] = config_variable
        if device_ids is not None:
            self._values["device_ids"] = device_ids
        if id is not None:
            self._values["id"] = id
        if message is not None:
            self._values["message"] = message
        if options_list is not None:
            self._values["options_list"] = options_list
        if request_basicauth is not None:
            self._values["request_basicauth"] = request_basicauth
        if request_client_certificate is not None:
            self._values["request_client_certificate"] = request_client_certificate
        if request_definition is not None:
            self._values["request_definition"] = request_definition
        if request_headers is not None:
            self._values["request_headers"] = request_headers
        if request_proxy is not None:
            self._values["request_proxy"] = request_proxy
        if request_query is not None:
            self._values["request_query"] = request_query
        if set_cookie is not None:
            self._values["set_cookie"] = set_cookie
        if subtype is not None:
            self._values["subtype"] = subtype
        if tags is not None:
            self._values["tags"] = tags

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
    def locations(self) -> typing.List[builtins.str]:
        '''Array of locations used to run the test.

        Refer to `the Datadog Synthetics location data source <https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/synthetics_locations>`_ to retrieve the list of locations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#locations SyntheticsTest#locations}
        '''
        result = self._values.get("locations")
        assert result is not None, "Required property 'locations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of Datadog synthetics test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''Define whether you want to start (``live``) or pause (``paused``) a Synthetic test. Valid values are ``live``, ``paused``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#status SyntheticsTest#status}
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Synthetics test type. Valid values are ``api``, ``browser``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_step(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStep]]]:
        '''api_step block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#api_step SyntheticsTest#api_step}
        '''
        result = self._values.get("api_step")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestApiStep]]], result)

    @builtins.property
    def assertion(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestAssertion]]]:
        '''assertion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#assertion SyntheticsTest#assertion}
        '''
        result = self._values.get("assertion")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestAssertion]]], result)

    @builtins.property
    def browser_step(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserStep]]]:
        '''browser_step block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#browser_step SyntheticsTest#browser_step}
        '''
        result = self._values.get("browser_step")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserStep]]], result)

    @builtins.property
    def browser_variable(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserVariable]]]:
        '''browser_variable block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#browser_variable SyntheticsTest#browser_variable}
        '''
        result = self._values.get("browser_variable")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestBrowserVariable]]], result)

    @builtins.property
    def config_variable(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestConfigVariable"]]]:
        '''config_variable block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#config_variable SyntheticsTest#config_variable}
        '''
        result = self._values.get("config_variable")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SyntheticsTestConfigVariable"]]], result)

    @builtins.property
    def device_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Required if ``type = "browser"``.

        Array with the different device IDs used to run the test. Valid values are ``laptop_large``, ``tablet``, ``mobile_small``, ``chrome.laptop_large``, ``chrome.tablet``, ``chrome.mobile_small``, ``firefox.laptop_large``, ``firefox.tablet``, ``firefox.mobile_small``, ``edge.laptop_large``, ``edge.tablet``, ``edge.mobile_small``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#device_ids SyntheticsTest#device_ids}
        '''
        result = self._values.get("device_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#id SyntheticsTest#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''A message to include with notifications for this synthetics test.

        Email notifications can be sent to specific users by using the same ``@username`` notation as events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options_list(self) -> typing.Optional["SyntheticsTestOptionsList"]:
        '''options_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#options_list SyntheticsTest#options_list}
        '''
        result = self._values.get("options_list")
        return typing.cast(typing.Optional["SyntheticsTestOptionsList"], result)

    @builtins.property
    def request_basicauth(self) -> typing.Optional["SyntheticsTestRequestBasicauth"]:
        '''request_basicauth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_basicauth SyntheticsTest#request_basicauth}
        '''
        result = self._values.get("request_basicauth")
        return typing.cast(typing.Optional["SyntheticsTestRequestBasicauth"], result)

    @builtins.property
    def request_client_certificate(
        self,
    ) -> typing.Optional["SyntheticsTestRequestClientCertificate"]:
        '''request_client_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_client_certificate SyntheticsTest#request_client_certificate}
        '''
        result = self._values.get("request_client_certificate")
        return typing.cast(typing.Optional["SyntheticsTestRequestClientCertificate"], result)

    @builtins.property
    def request_definition(self) -> typing.Optional["SyntheticsTestRequestDefinition"]:
        '''request_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_definition SyntheticsTest#request_definition}
        '''
        result = self._values.get("request_definition")
        return typing.cast(typing.Optional["SyntheticsTestRequestDefinition"], result)

    @builtins.property
    def request_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Header name and value map.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_headers SyntheticsTest#request_headers}
        '''
        result = self._values.get("request_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def request_proxy(self) -> typing.Optional["SyntheticsTestRequestProxy"]:
        '''request_proxy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_proxy SyntheticsTest#request_proxy}
        '''
        result = self._values.get("request_proxy")
        return typing.cast(typing.Optional["SyntheticsTestRequestProxy"], result)

    @builtins.property
    def request_query(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Query arguments name and value map.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#request_query SyntheticsTest#request_query}
        '''
        result = self._values.get("request_query")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def set_cookie(self) -> typing.Optional[builtins.str]:
        '''Cookies to be used for a browser test request, using the `Set-Cookie <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie>`_ syntax.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#set_cookie SyntheticsTest#set_cookie}
        '''
        result = self._values.get("set_cookie")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subtype(self) -> typing.Optional[builtins.str]:
        '''The subtype of the Synthetic API test.

        Defaults to ``http``. Valid values are ``http``, ``ssl``, ``tcp``, ``dns``, ``multi``, ``icmp``, ``udp``, ``websocket``, ``grpc``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#subtype SyntheticsTest#subtype}
        '''
        result = self._values.get("subtype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tags to associate with your synthetics test.

        This can help you categorize and filter tests in the manage synthetics page of the UI. Default is an empty list (``[]``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#tags SyntheticsTest#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestConfigVariable",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "example": "example",
        "id": "id",
        "pattern": "pattern",
    },
)
class SyntheticsTestConfigVariable:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        example: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        pattern: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        :param type: Type of test configuration variable. Valid values are ``global``, ``text``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param example: Example for the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#example SyntheticsTest#example}
        :param id: When type = ``global``, ID of the global variable to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#id SyntheticsTest#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pattern: Pattern of the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#pattern SyntheticsTest#pattern}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestConfigVariable.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if example is not None:
            self._values["example"] = example
        if id is not None:
            self._values["id"] = id
        if pattern is not None:
            self._values["pattern"] = pattern

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#name SyntheticsTest#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of test configuration variable. Valid values are ``global``, ``text``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def example(self) -> typing.Optional[builtins.str]:
        '''Example for the variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#example SyntheticsTest#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''When type = ``global``, ID of the global variable to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#id SyntheticsTest#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pattern(self) -> typing.Optional[builtins.str]:
        '''Pattern of the variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#pattern SyntheticsTest#pattern}
        '''
        result = self._values.get("pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestConfigVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestConfigVariableList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestConfigVariableList",
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
            type_hints = typing.get_type_hints(SyntheticsTestConfigVariableList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SyntheticsTestConfigVariableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestConfigVariableList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsTestConfigVariableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestConfigVariable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestConfigVariable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SyntheticsTestConfigVariable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestConfigVariableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestConfigVariableOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestConfigVariableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPattern")
    def reset_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPattern", []))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patternInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "example"))

    @example.setter
    def example(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableOutputReference, "example").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "example", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableOutputReference, "pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticsTestConfigVariable, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticsTestConfigVariable, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticsTestConfigVariable, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestConfigVariableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsList",
    jsii_struct_bases=[],
    name_mapping={
        "tick_every": "tickEvery",
        "accept_self_signed": "acceptSelfSigned",
        "allow_insecure": "allowInsecure",
        "check_certificate_revocation": "checkCertificateRevocation",
        "ci": "ci",
        "disable_csp": "disableCsp",
        "follow_redirects": "followRedirects",
        "ignore_server_certificate_error": "ignoreServerCertificateError",
        "initial_navigation_timeout": "initialNavigationTimeout",
        "min_failure_duration": "minFailureDuration",
        "min_location_failed": "minLocationFailed",
        "monitor_name": "monitorName",
        "monitor_options": "monitorOptions",
        "monitor_priority": "monitorPriority",
        "no_screenshot": "noScreenshot",
        "restricted_roles": "restrictedRoles",
        "retry": "retry",
        "rum_settings": "rumSettings",
    },
)
class SyntheticsTestOptionsList:
    def __init__(
        self,
        *,
        tick_every: jsii.Number,
        accept_self_signed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_certificate_revocation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ci: typing.Optional[typing.Union["SyntheticsTestOptionsListCi", typing.Dict[str, typing.Any]]] = None,
        disable_csp: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        follow_redirects: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ignore_server_certificate_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        initial_navigation_timeout: typing.Optional[jsii.Number] = None,
        min_failure_duration: typing.Optional[jsii.Number] = None,
        min_location_failed: typing.Optional[jsii.Number] = None,
        monitor_name: typing.Optional[builtins.str] = None,
        monitor_options: typing.Optional[typing.Union["SyntheticsTestOptionsListMonitorOptions", typing.Dict[str, typing.Any]]] = None,
        monitor_priority: typing.Optional[jsii.Number] = None,
        no_screenshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restricted_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        retry: typing.Optional[typing.Union["SyntheticsTestOptionsListRetry", typing.Dict[str, typing.Any]]] = None,
        rum_settings: typing.Optional[typing.Union["SyntheticsTestOptionsListRumSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tick_every: How often the test should run (in seconds). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#tick_every SyntheticsTest#tick_every}
        :param accept_self_signed: For SSL test, whether or not the test should allow self signed certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#accept_self_signed SyntheticsTest#accept_self_signed}
        :param allow_insecure: Allows loading insecure content for an HTTP test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_insecure SyntheticsTest#allow_insecure}
        :param check_certificate_revocation: For SSL test, whether or not the test should fail on revoked certificate in stapled OCSP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#check_certificate_revocation SyntheticsTest#check_certificate_revocation}
        :param ci: ci block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#ci SyntheticsTest#ci}
        :param disable_csp: Disable Content Security Policy for browser tests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#disable_csp SyntheticsTest#disable_csp}
        :param follow_redirects: Determines whether or not the API HTTP test should follow redirects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#follow_redirects SyntheticsTest#follow_redirects}
        :param ignore_server_certificate_error: Ignore server certificate error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#ignore_server_certificate_error SyntheticsTest#ignore_server_certificate_error}
        :param initial_navigation_timeout: Timeout before declaring the initial step as failed (in seconds) for browser tests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#initial_navigation_timeout SyntheticsTest#initial_navigation_timeout}
        :param min_failure_duration: Minimum amount of time in failure required to trigger an alert. Default is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#min_failure_duration SyntheticsTest#min_failure_duration}
        :param min_location_failed: Minimum number of locations in failure required to trigger an alert. Default is ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#min_location_failed SyntheticsTest#min_location_failed}
        :param monitor_name: The monitor name is used for the alert title as well as for all monitor dashboard widgets and SLOs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_name SyntheticsTest#monitor_name}
        :param monitor_options: monitor_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_options SyntheticsTest#monitor_options}
        :param monitor_priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_priority SyntheticsTest#monitor_priority}.
        :param no_screenshot: Prevents saving screenshots of the steps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_screenshot SyntheticsTest#no_screenshot}
        :param restricted_roles: A list of role identifiers pulled from the Roles API to restrict read and write access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#restricted_roles SyntheticsTest#restricted_roles}
        :param retry: retry block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#retry SyntheticsTest#retry}
        :param rum_settings: rum_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#rum_settings SyntheticsTest#rum_settings}
        '''
        if isinstance(ci, dict):
            ci = SyntheticsTestOptionsListCi(**ci)
        if isinstance(monitor_options, dict):
            monitor_options = SyntheticsTestOptionsListMonitorOptions(**monitor_options)
        if isinstance(retry, dict):
            retry = SyntheticsTestOptionsListRetry(**retry)
        if isinstance(rum_settings, dict):
            rum_settings = SyntheticsTestOptionsListRumSettings(**rum_settings)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestOptionsList.__init__)
            check_type(argname="argument tick_every", value=tick_every, expected_type=type_hints["tick_every"])
            check_type(argname="argument accept_self_signed", value=accept_self_signed, expected_type=type_hints["accept_self_signed"])
            check_type(argname="argument allow_insecure", value=allow_insecure, expected_type=type_hints["allow_insecure"])
            check_type(argname="argument check_certificate_revocation", value=check_certificate_revocation, expected_type=type_hints["check_certificate_revocation"])
            check_type(argname="argument ci", value=ci, expected_type=type_hints["ci"])
            check_type(argname="argument disable_csp", value=disable_csp, expected_type=type_hints["disable_csp"])
            check_type(argname="argument follow_redirects", value=follow_redirects, expected_type=type_hints["follow_redirects"])
            check_type(argname="argument ignore_server_certificate_error", value=ignore_server_certificate_error, expected_type=type_hints["ignore_server_certificate_error"])
            check_type(argname="argument initial_navigation_timeout", value=initial_navigation_timeout, expected_type=type_hints["initial_navigation_timeout"])
            check_type(argname="argument min_failure_duration", value=min_failure_duration, expected_type=type_hints["min_failure_duration"])
            check_type(argname="argument min_location_failed", value=min_location_failed, expected_type=type_hints["min_location_failed"])
            check_type(argname="argument monitor_name", value=monitor_name, expected_type=type_hints["monitor_name"])
            check_type(argname="argument monitor_options", value=monitor_options, expected_type=type_hints["monitor_options"])
            check_type(argname="argument monitor_priority", value=monitor_priority, expected_type=type_hints["monitor_priority"])
            check_type(argname="argument no_screenshot", value=no_screenshot, expected_type=type_hints["no_screenshot"])
            check_type(argname="argument restricted_roles", value=restricted_roles, expected_type=type_hints["restricted_roles"])
            check_type(argname="argument retry", value=retry, expected_type=type_hints["retry"])
            check_type(argname="argument rum_settings", value=rum_settings, expected_type=type_hints["rum_settings"])
        self._values: typing.Dict[str, typing.Any] = {
            "tick_every": tick_every,
        }
        if accept_self_signed is not None:
            self._values["accept_self_signed"] = accept_self_signed
        if allow_insecure is not None:
            self._values["allow_insecure"] = allow_insecure
        if check_certificate_revocation is not None:
            self._values["check_certificate_revocation"] = check_certificate_revocation
        if ci is not None:
            self._values["ci"] = ci
        if disable_csp is not None:
            self._values["disable_csp"] = disable_csp
        if follow_redirects is not None:
            self._values["follow_redirects"] = follow_redirects
        if ignore_server_certificate_error is not None:
            self._values["ignore_server_certificate_error"] = ignore_server_certificate_error
        if initial_navigation_timeout is not None:
            self._values["initial_navigation_timeout"] = initial_navigation_timeout
        if min_failure_duration is not None:
            self._values["min_failure_duration"] = min_failure_duration
        if min_location_failed is not None:
            self._values["min_location_failed"] = min_location_failed
        if monitor_name is not None:
            self._values["monitor_name"] = monitor_name
        if monitor_options is not None:
            self._values["monitor_options"] = monitor_options
        if monitor_priority is not None:
            self._values["monitor_priority"] = monitor_priority
        if no_screenshot is not None:
            self._values["no_screenshot"] = no_screenshot
        if restricted_roles is not None:
            self._values["restricted_roles"] = restricted_roles
        if retry is not None:
            self._values["retry"] = retry
        if rum_settings is not None:
            self._values["rum_settings"] = rum_settings

    @builtins.property
    def tick_every(self) -> jsii.Number:
        '''How often the test should run (in seconds).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#tick_every SyntheticsTest#tick_every}
        '''
        result = self._values.get("tick_every")
        assert result is not None, "Required property 'tick_every' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def accept_self_signed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''For SSL test, whether or not the test should allow self signed certificates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#accept_self_signed SyntheticsTest#accept_self_signed}
        '''
        result = self._values.get("accept_self_signed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allows loading insecure content for an HTTP test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#allow_insecure SyntheticsTest#allow_insecure}
        '''
        result = self._values.get("allow_insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def check_certificate_revocation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''For SSL test, whether or not the test should fail on revoked certificate in stapled OCSP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#check_certificate_revocation SyntheticsTest#check_certificate_revocation}
        '''
        result = self._values.get("check_certificate_revocation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ci(self) -> typing.Optional["SyntheticsTestOptionsListCi"]:
        '''ci block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#ci SyntheticsTest#ci}
        '''
        result = self._values.get("ci")
        return typing.cast(typing.Optional["SyntheticsTestOptionsListCi"], result)

    @builtins.property
    def disable_csp(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable Content Security Policy for browser tests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#disable_csp SyntheticsTest#disable_csp}
        '''
        result = self._values.get("disable_csp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def follow_redirects(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines whether or not the API HTTP test should follow redirects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#follow_redirects SyntheticsTest#follow_redirects}
        '''
        result = self._values.get("follow_redirects")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ignore_server_certificate_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Ignore server certificate error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#ignore_server_certificate_error SyntheticsTest#ignore_server_certificate_error}
        '''
        result = self._values.get("ignore_server_certificate_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def initial_navigation_timeout(self) -> typing.Optional[jsii.Number]:
        '''Timeout before declaring the initial step as failed (in seconds) for browser tests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#initial_navigation_timeout SyntheticsTest#initial_navigation_timeout}
        '''
        result = self._values.get("initial_navigation_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_failure_duration(self) -> typing.Optional[jsii.Number]:
        '''Minimum amount of time in failure required to trigger an alert. Default is ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#min_failure_duration SyntheticsTest#min_failure_duration}
        '''
        result = self._values.get("min_failure_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_location_failed(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of locations in failure required to trigger an alert. Default is ``1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#min_location_failed SyntheticsTest#min_location_failed}
        '''
        result = self._values.get("min_location_failed")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitor_name(self) -> typing.Optional[builtins.str]:
        '''The monitor name is used for the alert title as well as for all monitor dashboard widgets and SLOs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_name SyntheticsTest#monitor_name}
        '''
        result = self._values.get("monitor_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitor_options(
        self,
    ) -> typing.Optional["SyntheticsTestOptionsListMonitorOptions"]:
        '''monitor_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_options SyntheticsTest#monitor_options}
        '''
        result = self._values.get("monitor_options")
        return typing.cast(typing.Optional["SyntheticsTestOptionsListMonitorOptions"], result)

    @builtins.property
    def monitor_priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#monitor_priority SyntheticsTest#monitor_priority}.'''
        result = self._values.get("monitor_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def no_screenshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Prevents saving screenshots of the steps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_screenshot SyntheticsTest#no_screenshot}
        '''
        result = self._values.get("no_screenshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def restricted_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of role identifiers pulled from the Roles API to restrict read and write access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#restricted_roles SyntheticsTest#restricted_roles}
        '''
        result = self._values.get("restricted_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def retry(self) -> typing.Optional["SyntheticsTestOptionsListRetry"]:
        '''retry block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#retry SyntheticsTest#retry}
        '''
        result = self._values.get("retry")
        return typing.cast(typing.Optional["SyntheticsTestOptionsListRetry"], result)

    @builtins.property
    def rum_settings(self) -> typing.Optional["SyntheticsTestOptionsListRumSettings"]:
        '''rum_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#rum_settings SyntheticsTest#rum_settings}
        '''
        result = self._values.get("rum_settings")
        return typing.cast(typing.Optional["SyntheticsTestOptionsListRumSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestOptionsList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListCi",
    jsii_struct_bases=[],
    name_mapping={"execution_rule": "executionRule"},
)
class SyntheticsTestOptionsListCi:
    def __init__(self, *, execution_rule: typing.Optional[builtins.str] = None) -> None:
        '''
        :param execution_rule: Execution rule for a Synthetics test. Valid values are ``blocking``, ``non_blocking``, ``skipped``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#execution_rule SyntheticsTest#execution_rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListCi.__init__)
            check_type(argname="argument execution_rule", value=execution_rule, expected_type=type_hints["execution_rule"])
        self._values: typing.Dict[str, typing.Any] = {}
        if execution_rule is not None:
            self._values["execution_rule"] = execution_rule

    @builtins.property
    def execution_rule(self) -> typing.Optional[builtins.str]:
        '''Execution rule for a Synthetics test. Valid values are ``blocking``, ``non_blocking``, ``skipped``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#execution_rule SyntheticsTest#execution_rule}
        '''
        result = self._values.get("execution_rule")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestOptionsListCi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestOptionsListCiOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListCiOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListCiOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExecutionRule")
    def reset_execution_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRule", []))

    @builtins.property
    @jsii.member(jsii_name="executionRuleInput")
    def execution_rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRule")
    def execution_rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRule"))

    @execution_rule.setter
    def execution_rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListCiOutputReference, "execution_rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestOptionsListCi]:
        return typing.cast(typing.Optional[SyntheticsTestOptionsListCi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestOptionsListCi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListCiOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListMonitorOptions",
    jsii_struct_bases=[],
    name_mapping={"renotify_interval": "renotifyInterval"},
)
class SyntheticsTestOptionsListMonitorOptions:
    def __init__(
        self,
        *,
        renotify_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param renotify_interval: Specify a renotification frequency. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#renotify_interval SyntheticsTest#renotify_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListMonitorOptions.__init__)
            check_type(argname="argument renotify_interval", value=renotify_interval, expected_type=type_hints["renotify_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if renotify_interval is not None:
            self._values["renotify_interval"] = renotify_interval

    @builtins.property
    def renotify_interval(self) -> typing.Optional[jsii.Number]:
        '''Specify a renotification frequency.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#renotify_interval SyntheticsTest#renotify_interval}
        '''
        result = self._values.get("renotify_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestOptionsListMonitorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestOptionsListMonitorOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListMonitorOptionsOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListMonitorOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRenotifyInterval")
    def reset_renotify_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenotifyInterval", []))

    @builtins.property
    @jsii.member(jsii_name="renotifyIntervalInput")
    def renotify_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "renotifyIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="renotifyInterval")
    def renotify_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "renotifyInterval"))

    @renotify_interval.setter
    def renotify_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListMonitorOptionsOutputReference, "renotify_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renotifyInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestOptionsListMonitorOptions]:
        return typing.cast(typing.Optional[SyntheticsTestOptionsListMonitorOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestOptionsListMonitorOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListMonitorOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestOptionsListOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCi")
    def put_ci(self, *, execution_rule: typing.Optional[builtins.str] = None) -> None:
        '''
        :param execution_rule: Execution rule for a Synthetics test. Valid values are ``blocking``, ``non_blocking``, ``skipped``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#execution_rule SyntheticsTest#execution_rule}
        '''
        value = SyntheticsTestOptionsListCi(execution_rule=execution_rule)

        return typing.cast(None, jsii.invoke(self, "putCi", [value]))

    @jsii.member(jsii_name="putMonitorOptions")
    def put_monitor_options(
        self,
        *,
        renotify_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param renotify_interval: Specify a renotification frequency. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#renotify_interval SyntheticsTest#renotify_interval}
        '''
        value = SyntheticsTestOptionsListMonitorOptions(
            renotify_interval=renotify_interval
        )

        return typing.cast(None, jsii.invoke(self, "putMonitorOptions", [value]))

    @jsii.member(jsii_name="putRetry")
    def put_retry(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: Number of retries needed to consider a location as failed before sending a notification alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#count SyntheticsTest#count}
        :param interval: Interval between a failed test and the next retry in milliseconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#interval SyntheticsTest#interval}
        '''
        value = SyntheticsTestOptionsListRetry(count=count, interval=interval)

        return typing.cast(None, jsii.invoke(self, "putRetry", [value]))

    @jsii.member(jsii_name="putRumSettings")
    def put_rum_settings(
        self,
        *,
        is_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        application_id: typing.Optional[builtins.str] = None,
        client_token_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param is_enabled: Determines whether RUM data is collected during test runs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#is_enabled SyntheticsTest#is_enabled}
        :param application_id: RUM application ID used to collect RUM data for the browser test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#application_id SyntheticsTest#application_id}
        :param client_token_id: RUM application API key ID used to collect RUM data for the browser test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#client_token_id SyntheticsTest#client_token_id}
        '''
        value = SyntheticsTestOptionsListRumSettings(
            is_enabled=is_enabled,
            application_id=application_id,
            client_token_id=client_token_id,
        )

        return typing.cast(None, jsii.invoke(self, "putRumSettings", [value]))

    @jsii.member(jsii_name="resetAcceptSelfSigned")
    def reset_accept_self_signed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceptSelfSigned", []))

    @jsii.member(jsii_name="resetAllowInsecure")
    def reset_allow_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowInsecure", []))

    @jsii.member(jsii_name="resetCheckCertificateRevocation")
    def reset_check_certificate_revocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckCertificateRevocation", []))

    @jsii.member(jsii_name="resetCi")
    def reset_ci(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCi", []))

    @jsii.member(jsii_name="resetDisableCsp")
    def reset_disable_csp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableCsp", []))

    @jsii.member(jsii_name="resetFollowRedirects")
    def reset_follow_redirects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFollowRedirects", []))

    @jsii.member(jsii_name="resetIgnoreServerCertificateError")
    def reset_ignore_server_certificate_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreServerCertificateError", []))

    @jsii.member(jsii_name="resetInitialNavigationTimeout")
    def reset_initial_navigation_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialNavigationTimeout", []))

    @jsii.member(jsii_name="resetMinFailureDuration")
    def reset_min_failure_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinFailureDuration", []))

    @jsii.member(jsii_name="resetMinLocationFailed")
    def reset_min_location_failed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinLocationFailed", []))

    @jsii.member(jsii_name="resetMonitorName")
    def reset_monitor_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorName", []))

    @jsii.member(jsii_name="resetMonitorOptions")
    def reset_monitor_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorOptions", []))

    @jsii.member(jsii_name="resetMonitorPriority")
    def reset_monitor_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorPriority", []))

    @jsii.member(jsii_name="resetNoScreenshot")
    def reset_no_screenshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoScreenshot", []))

    @jsii.member(jsii_name="resetRestrictedRoles")
    def reset_restricted_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictedRoles", []))

    @jsii.member(jsii_name="resetRetry")
    def reset_retry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetry", []))

    @jsii.member(jsii_name="resetRumSettings")
    def reset_rum_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRumSettings", []))

    @builtins.property
    @jsii.member(jsii_name="ci")
    def ci(self) -> SyntheticsTestOptionsListCiOutputReference:
        return typing.cast(SyntheticsTestOptionsListCiOutputReference, jsii.get(self, "ci"))

    @builtins.property
    @jsii.member(jsii_name="monitorOptions")
    def monitor_options(self) -> SyntheticsTestOptionsListMonitorOptionsOutputReference:
        return typing.cast(SyntheticsTestOptionsListMonitorOptionsOutputReference, jsii.get(self, "monitorOptions"))

    @builtins.property
    @jsii.member(jsii_name="retry")
    def retry(self) -> "SyntheticsTestOptionsListRetryOutputReference":
        return typing.cast("SyntheticsTestOptionsListRetryOutputReference", jsii.get(self, "retry"))

    @builtins.property
    @jsii.member(jsii_name="rumSettings")
    def rum_settings(self) -> "SyntheticsTestOptionsListRumSettingsOutputReference":
        return typing.cast("SyntheticsTestOptionsListRumSettingsOutputReference", jsii.get(self, "rumSettings"))

    @builtins.property
    @jsii.member(jsii_name="acceptSelfSignedInput")
    def accept_self_signed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "acceptSelfSignedInput"))

    @builtins.property
    @jsii.member(jsii_name="allowInsecureInput")
    def allow_insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowInsecureInput"))

    @builtins.property
    @jsii.member(jsii_name="checkCertificateRevocationInput")
    def check_certificate_revocation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "checkCertificateRevocationInput"))

    @builtins.property
    @jsii.member(jsii_name="ciInput")
    def ci_input(self) -> typing.Optional[SyntheticsTestOptionsListCi]:
        return typing.cast(typing.Optional[SyntheticsTestOptionsListCi], jsii.get(self, "ciInput"))

    @builtins.property
    @jsii.member(jsii_name="disableCspInput")
    def disable_csp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableCspInput"))

    @builtins.property
    @jsii.member(jsii_name="followRedirectsInput")
    def follow_redirects_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "followRedirectsInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreServerCertificateErrorInput")
    def ignore_server_certificate_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreServerCertificateErrorInput"))

    @builtins.property
    @jsii.member(jsii_name="initialNavigationTimeoutInput")
    def initial_navigation_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialNavigationTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="minFailureDurationInput")
    def min_failure_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minFailureDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="minLocationFailedInput")
    def min_location_failed_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLocationFailedInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorNameInput")
    def monitor_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitorNameInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorOptionsInput")
    def monitor_options_input(
        self,
    ) -> typing.Optional[SyntheticsTestOptionsListMonitorOptions]:
        return typing.cast(typing.Optional[SyntheticsTestOptionsListMonitorOptions], jsii.get(self, "monitorOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorPriorityInput")
    def monitor_priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monitorPriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="noScreenshotInput")
    def no_screenshot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noScreenshotInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictedRolesInput")
    def restricted_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "restrictedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="retryInput")
    def retry_input(self) -> typing.Optional["SyntheticsTestOptionsListRetry"]:
        return typing.cast(typing.Optional["SyntheticsTestOptionsListRetry"], jsii.get(self, "retryInput"))

    @builtins.property
    @jsii.member(jsii_name="rumSettingsInput")
    def rum_settings_input(
        self,
    ) -> typing.Optional["SyntheticsTestOptionsListRumSettings"]:
        return typing.cast(typing.Optional["SyntheticsTestOptionsListRumSettings"], jsii.get(self, "rumSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="tickEveryInput")
    def tick_every_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tickEveryInput"))

    @builtins.property
    @jsii.member(jsii_name="acceptSelfSigned")
    def accept_self_signed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "acceptSelfSigned"))

    @accept_self_signed.setter
    def accept_self_signed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "accept_self_signed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptSelfSigned", value)

    @builtins.property
    @jsii.member(jsii_name="allowInsecure")
    def allow_insecure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowInsecure"))

    @allow_insecure.setter
    def allow_insecure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "allow_insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowInsecure", value)

    @builtins.property
    @jsii.member(jsii_name="checkCertificateRevocation")
    def check_certificate_revocation(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "checkCertificateRevocation"))

    @check_certificate_revocation.setter
    def check_certificate_revocation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "check_certificate_revocation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkCertificateRevocation", value)

    @builtins.property
    @jsii.member(jsii_name="disableCsp")
    def disable_csp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableCsp"))

    @disable_csp.setter
    def disable_csp(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "disable_csp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableCsp", value)

    @builtins.property
    @jsii.member(jsii_name="followRedirects")
    def follow_redirects(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "followRedirects"))

    @follow_redirects.setter
    def follow_redirects(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "follow_redirects").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "followRedirects", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreServerCertificateError")
    def ignore_server_certificate_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreServerCertificateError"))

    @ignore_server_certificate_error.setter
    def ignore_server_certificate_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "ignore_server_certificate_error").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreServerCertificateError", value)

    @builtins.property
    @jsii.member(jsii_name="initialNavigationTimeout")
    def initial_navigation_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialNavigationTimeout"))

    @initial_navigation_timeout.setter
    def initial_navigation_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "initial_navigation_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialNavigationTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="minFailureDuration")
    def min_failure_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minFailureDuration"))

    @min_failure_duration.setter
    def min_failure_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "min_failure_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minFailureDuration", value)

    @builtins.property
    @jsii.member(jsii_name="minLocationFailed")
    def min_location_failed(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minLocationFailed"))

    @min_location_failed.setter
    def min_location_failed(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "min_location_failed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLocationFailed", value)

    @builtins.property
    @jsii.member(jsii_name="monitorName")
    def monitor_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitorName"))

    @monitor_name.setter
    def monitor_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "monitor_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorName", value)

    @builtins.property
    @jsii.member(jsii_name="monitorPriority")
    def monitor_priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monitorPriority"))

    @monitor_priority.setter
    def monitor_priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "monitor_priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorPriority", value)

    @builtins.property
    @jsii.member(jsii_name="noScreenshot")
    def no_screenshot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noScreenshot"))

    @no_screenshot.setter
    def no_screenshot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "no_screenshot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noScreenshot", value)

    @builtins.property
    @jsii.member(jsii_name="restrictedRoles")
    def restricted_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "restrictedRoles"))

    @restricted_roles.setter
    def restricted_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "restricted_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="tickEvery")
    def tick_every(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tickEvery"))

    @tick_every.setter
    def tick_every(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "tick_every").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tickEvery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestOptionsList]:
        return typing.cast(typing.Optional[SyntheticsTestOptionsList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SyntheticsTestOptionsList]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListRetry",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "interval": "interval"},
)
class SyntheticsTestOptionsListRetry:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: Number of retries needed to consider a location as failed before sending a notification alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#count SyntheticsTest#count}
        :param interval: Interval between a failed test and the next retry in milliseconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#interval SyntheticsTest#interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListRetry.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if interval is not None:
            self._values["interval"] = interval

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Number of retries needed to consider a location as failed before sending a notification alert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#count SyntheticsTest#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Interval between a failed test and the next retry in milliseconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#interval SyntheticsTest#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestOptionsListRetry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestOptionsListRetryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListRetryOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListRetryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListRetryOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListRetryOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestOptionsListRetry]:
        return typing.cast(typing.Optional[SyntheticsTestOptionsListRetry], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestOptionsListRetry],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListRetryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListRumSettings",
    jsii_struct_bases=[],
    name_mapping={
        "is_enabled": "isEnabled",
        "application_id": "applicationId",
        "client_token_id": "clientTokenId",
    },
)
class SyntheticsTestOptionsListRumSettings:
    def __init__(
        self,
        *,
        is_enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        application_id: typing.Optional[builtins.str] = None,
        client_token_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param is_enabled: Determines whether RUM data is collected during test runs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#is_enabled SyntheticsTest#is_enabled}
        :param application_id: RUM application ID used to collect RUM data for the browser test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#application_id SyntheticsTest#application_id}
        :param client_token_id: RUM application API key ID used to collect RUM data for the browser test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#client_token_id SyntheticsTest#client_token_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListRumSettings.__init__)
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument client_token_id", value=client_token_id, expected_type=type_hints["client_token_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "is_enabled": is_enabled,
        }
        if application_id is not None:
            self._values["application_id"] = application_id
        if client_token_id is not None:
            self._values["client_token_id"] = client_token_id

    @builtins.property
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Determines whether RUM data is collected during test runs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#is_enabled SyntheticsTest#is_enabled}
        '''
        result = self._values.get("is_enabled")
        assert result is not None, "Required property 'is_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def application_id(self) -> typing.Optional[builtins.str]:
        '''RUM application ID used to collect RUM data for the browser test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#application_id SyntheticsTest#application_id}
        '''
        result = self._values.get("application_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_token_id(self) -> typing.Optional[jsii.Number]:
        '''RUM application API key ID used to collect RUM data for the browser test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#client_token_id SyntheticsTest#client_token_id}
        '''
        result = self._values.get("client_token_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestOptionsListRumSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestOptionsListRumSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestOptionsListRumSettingsOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestOptionsListRumSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApplicationId")
    def reset_application_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationId", []))

    @jsii.member(jsii_name="resetClientTokenId")
    def reset_client_token_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTokenId", []))

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTokenIdInput")
    def client_token_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientTokenIdInput"))

    @builtins.property
    @jsii.member(jsii_name="isEnabledInput")
    def is_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListRumSettingsOutputReference, "application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="clientTokenId")
    def client_token_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientTokenId"))

    @client_token_id.setter
    def client_token_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListRumSettingsOutputReference, "client_token_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTokenId", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListRumSettingsOutputReference, "is_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestOptionsListRumSettings]:
        return typing.cast(typing.Optional[SyntheticsTestOptionsListRumSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestOptionsListRumSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestOptionsListRumSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestBasicauth",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "domain": "domain",
        "password": "password",
        "region": "region",
        "secret_key": "secretKey",
        "service_name": "serviceName",
        "session_token": "sessionToken",
        "type": "type",
        "username": "username",
        "workstation": "workstation",
    },
)
class SyntheticsTestRequestBasicauth:
    def __init__(
        self,
        *,
        access_key: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        service_name: typing.Optional[builtins.str] = None,
        session_token: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        workstation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_key: Access key for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#access_key SyntheticsTest#access_key}
        :param domain: Domain for ``ntlm`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#domain SyntheticsTest#domain}
        :param password: Password for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#password SyntheticsTest#password}
        :param region: Region for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#region SyntheticsTest#region}
        :param secret_key: Secret key for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#secret_key SyntheticsTest#secret_key}
        :param service_name: Service name for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service_name SyntheticsTest#service_name}
        :param session_token: Session token for ``SIGV4`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#session_token SyntheticsTest#session_token}
        :param type: Type of basic authentication to use when performing the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        :param username: Username for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#username SyntheticsTest#username}
        :param workstation: Workstation for ``ntlm`` authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#workstation SyntheticsTest#workstation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestRequestBasicauth.__init__)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument session_token", value=session_token, expected_type=type_hints["session_token"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument workstation", value=workstation, expected_type=type_hints["workstation"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_key is not None:
            self._values["access_key"] = access_key
        if domain is not None:
            self._values["domain"] = domain
        if password is not None:
            self._values["password"] = password
        if region is not None:
            self._values["region"] = region
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if service_name is not None:
            self._values["service_name"] = service_name
        if session_token is not None:
            self._values["session_token"] = session_token
        if type is not None:
            self._values["type"] = type
        if username is not None:
            self._values["username"] = username
        if workstation is not None:
            self._values["workstation"] = workstation

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''Access key for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#access_key SyntheticsTest#access_key}
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''Domain for ``ntlm`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#domain SyntheticsTest#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#password SyntheticsTest#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#region SyntheticsTest#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''Secret key for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#secret_key SyntheticsTest#secret_key}
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Service name for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service_name SyntheticsTest#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_token(self) -> typing.Optional[builtins.str]:
        '''Session token for ``SIGV4`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#session_token SyntheticsTest#session_token}
        '''
        result = self._values.get("session_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type of basic authentication to use when performing the test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#type SyntheticsTest#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#username SyntheticsTest#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workstation(self) -> typing.Optional[builtins.str]:
        '''Workstation for ``ntlm`` authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#workstation SyntheticsTest#workstation}
        '''
        result = self._values.get("workstation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestRequestBasicauth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestRequestBasicauthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestBasicauthOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestRequestBasicauthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSecretKey")
    def reset_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretKey", []))

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @jsii.member(jsii_name="resetSessionToken")
    def reset_session_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionToken", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetWorkstation")
    def reset_workstation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkstation", []))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTokenInput")
    def session_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="workstationInput")
    def workstation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workstationInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "secret_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="sessionToken")
    def session_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionToken"))

    @session_token.setter
    def session_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "session_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionToken", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="workstation")
    def workstation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workstation"))

    @workstation.setter
    def workstation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "workstation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workstation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestRequestBasicauth]:
        return typing.cast(typing.Optional[SyntheticsTestRequestBasicauth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestRequestBasicauth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestBasicauthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestClientCertificate",
    jsii_struct_bases=[],
    name_mapping={"cert": "cert", "key": "key"},
)
class SyntheticsTestRequestClientCertificate:
    def __init__(
        self,
        *,
        cert: typing.Union["SyntheticsTestRequestClientCertificateCert", typing.Dict[str, typing.Any]],
        key: typing.Union["SyntheticsTestRequestClientCertificateKey", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param cert: cert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#cert SyntheticsTest#cert}
        :param key: key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#key SyntheticsTest#key}
        '''
        if isinstance(cert, dict):
            cert = SyntheticsTestRequestClientCertificateCert(**cert)
        if isinstance(key, dict):
            key = SyntheticsTestRequestClientCertificateKey(**key)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestRequestClientCertificate.__init__)
            check_type(argname="argument cert", value=cert, expected_type=type_hints["cert"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "cert": cert,
            "key": key,
        }

    @builtins.property
    def cert(self) -> "SyntheticsTestRequestClientCertificateCert":
        '''cert block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#cert SyntheticsTest#cert}
        '''
        result = self._values.get("cert")
        assert result is not None, "Required property 'cert' is missing"
        return typing.cast("SyntheticsTestRequestClientCertificateCert", result)

    @builtins.property
    def key(self) -> "SyntheticsTestRequestClientCertificateKey":
        '''key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#key SyntheticsTest#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast("SyntheticsTestRequestClientCertificateKey", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestRequestClientCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestClientCertificateCert",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "filename": "filename"},
)
class SyntheticsTestRequestClientCertificateCert:
    def __init__(
        self,
        *,
        content: builtins.str,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: Content of the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        :param filename: File name for the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestRequestClientCertificateCert.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if filename is not None:
            self._values["filename"] = filename

    @builtins.property
    def content(self) -> builtins.str:
        '''Content of the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''File name for the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestRequestClientCertificateCert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestRequestClientCertificateCertOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestClientCertificateCertOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestRequestClientCertificateCertOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestClientCertificateCertOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestClientCertificateCertOutputReference, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestRequestClientCertificateCert]:
        return typing.cast(typing.Optional[SyntheticsTestRequestClientCertificateCert], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestRequestClientCertificateCert],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestClientCertificateCertOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestClientCertificateKey",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "filename": "filename"},
)
class SyntheticsTestRequestClientCertificateKey:
    def __init__(
        self,
        *,
        content: builtins.str,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: Content of the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        :param filename: File name for the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestRequestClientCertificateKey.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if filename is not None:
            self._values["filename"] = filename

    @builtins.property
    def content(self) -> builtins.str:
        '''Content of the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''File name for the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestRequestClientCertificateKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestRequestClientCertificateKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestClientCertificateKeyOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestRequestClientCertificateKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestClientCertificateKeyOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestClientCertificateKeyOutputReference, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsTestRequestClientCertificateKey]:
        return typing.cast(typing.Optional[SyntheticsTestRequestClientCertificateKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestRequestClientCertificateKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestClientCertificateKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticsTestRequestClientCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestClientCertificateOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestRequestClientCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCert")
    def put_cert(
        self,
        *,
        content: builtins.str,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: Content of the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        :param filename: File name for the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        value = SyntheticsTestRequestClientCertificateCert(
            content=content, filename=filename
        )

        return typing.cast(None, jsii.invoke(self, "putCert", [value]))

    @jsii.member(jsii_name="putKey")
    def put_key(
        self,
        *,
        content: builtins.str,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: Content of the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#content SyntheticsTest#content}
        :param filename: File name for the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#filename SyntheticsTest#filename}
        '''
        value = SyntheticsTestRequestClientCertificateKey(
            content=content, filename=filename
        )

        return typing.cast(None, jsii.invoke(self, "putKey", [value]))

    @builtins.property
    @jsii.member(jsii_name="cert")
    def cert(self) -> SyntheticsTestRequestClientCertificateCertOutputReference:
        return typing.cast(SyntheticsTestRequestClientCertificateCertOutputReference, jsii.get(self, "cert"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> SyntheticsTestRequestClientCertificateKeyOutputReference:
        return typing.cast(SyntheticsTestRequestClientCertificateKeyOutputReference, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="certInput")
    def cert_input(self) -> typing.Optional[SyntheticsTestRequestClientCertificateCert]:
        return typing.cast(typing.Optional[SyntheticsTestRequestClientCertificateCert], jsii.get(self, "certInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[SyntheticsTestRequestClientCertificateKey]:
        return typing.cast(typing.Optional[SyntheticsTestRequestClientCertificateKey], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestRequestClientCertificate]:
        return typing.cast(typing.Optional[SyntheticsTestRequestClientCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestRequestClientCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestClientCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "body": "body",
        "certificate_domains": "certificateDomains",
        "dns_server": "dnsServer",
        "dns_server_port": "dnsServerPort",
        "host": "host",
        "message": "message",
        "method": "method",
        "no_saving_response_body": "noSavingResponseBody",
        "number_of_packets": "numberOfPackets",
        "port": "port",
        "servername": "servername",
        "service": "service",
        "should_track_hops": "shouldTrackHops",
        "timeout": "timeout",
        "url": "url",
    },
)
class SyntheticsTestRequestDefinition:
    def __init__(
        self,
        *,
        body: typing.Optional[builtins.str] = None,
        certificate_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_server: typing.Optional[builtins.str] = None,
        dns_server_port: typing.Optional[jsii.Number] = None,
        host: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        method: typing.Optional[builtins.str] = None,
        no_saving_response_body: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        number_of_packets: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        servername: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        should_track_hops: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param body: The request body. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#body SyntheticsTest#body}
        :param certificate_domains: By default, the client certificate is applied on the domain of the starting URL for browser tests. If you want your client certificate to be applied on other domains instead, add them in ``certificate_domains``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#certificate_domains SyntheticsTest#certificate_domains}
        :param dns_server: DNS server to use for DNS tests (``subtype = "dns"``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server SyntheticsTest#dns_server}
        :param dns_server_port: DNS server port to use for DNS tests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server_port SyntheticsTest#dns_server_port}
        :param host: Host name to perform the test with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#host SyntheticsTest#host}
        :param message: For UDP and websocket tests, message to send with the request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        :param method: The HTTP method. Valid values are ``GET``, ``POST``, ``PATCH``, ``PUT``, ``DELETE``, ``HEAD``, ``OPTIONS``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#method SyntheticsTest#method}
        :param no_saving_response_body: Determines whether or not to save the response body. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_saving_response_body SyntheticsTest#no_saving_response_body}
        :param number_of_packets: Number of pings to use per test for ICMP tests (``subtype = "icmp"``) between 0 and 10. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#number_of_packets SyntheticsTest#number_of_packets}
        :param port: Port to use when performing the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#port SyntheticsTest#port}
        :param servername: For SSL tests, it specifies on which server you want to initiate the TLS handshake, allowing the server to present one of multiple possible certificates on the same IP address and TCP port number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#servername SyntheticsTest#servername}
        :param service: For gRPC tests, service to target for healthcheck. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service SyntheticsTest#service}
        :param should_track_hops: This will turn on a traceroute probe to discover all gateways along the path to the host destination. For ICMP tests (``subtype = "icmp"``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#should_track_hops SyntheticsTest#should_track_hops}
        :param timeout: Timeout in seconds for the test. Defaults to ``60``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#timeout SyntheticsTest#timeout}
        :param url: The URL to send the request to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestRequestDefinition.__init__)
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument certificate_domains", value=certificate_domains, expected_type=type_hints["certificate_domains"])
            check_type(argname="argument dns_server", value=dns_server, expected_type=type_hints["dns_server"])
            check_type(argname="argument dns_server_port", value=dns_server_port, expected_type=type_hints["dns_server_port"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument no_saving_response_body", value=no_saving_response_body, expected_type=type_hints["no_saving_response_body"])
            check_type(argname="argument number_of_packets", value=number_of_packets, expected_type=type_hints["number_of_packets"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument servername", value=servername, expected_type=type_hints["servername"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument should_track_hops", value=should_track_hops, expected_type=type_hints["should_track_hops"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body is not None:
            self._values["body"] = body
        if certificate_domains is not None:
            self._values["certificate_domains"] = certificate_domains
        if dns_server is not None:
            self._values["dns_server"] = dns_server
        if dns_server_port is not None:
            self._values["dns_server_port"] = dns_server_port
        if host is not None:
            self._values["host"] = host
        if message is not None:
            self._values["message"] = message
        if method is not None:
            self._values["method"] = method
        if no_saving_response_body is not None:
            self._values["no_saving_response_body"] = no_saving_response_body
        if number_of_packets is not None:
            self._values["number_of_packets"] = number_of_packets
        if port is not None:
            self._values["port"] = port
        if servername is not None:
            self._values["servername"] = servername
        if service is not None:
            self._values["service"] = service
        if should_track_hops is not None:
            self._values["should_track_hops"] = should_track_hops
        if timeout is not None:
            self._values["timeout"] = timeout
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''The request body.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#body SyntheticsTest#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''By default, the client certificate is applied on the domain of the starting URL for browser tests.

        If you want your client certificate to be applied on other domains instead, add them in ``certificate_domains``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#certificate_domains SyntheticsTest#certificate_domains}
        '''
        result = self._values.get("certificate_domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dns_server(self) -> typing.Optional[builtins.str]:
        '''DNS server to use for DNS tests (``subtype = "dns"``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server SyntheticsTest#dns_server}
        '''
        result = self._values.get("dns_server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_server_port(self) -> typing.Optional[jsii.Number]:
        '''DNS server port to use for DNS tests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#dns_server_port SyntheticsTest#dns_server_port}
        '''
        result = self._values.get("dns_server_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host name to perform the test with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#host SyntheticsTest#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''For UDP and websocket tests, message to send with the request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#message SyntheticsTest#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''The HTTP method. Valid values are ``GET``, ``POST``, ``PATCH``, ``PUT``, ``DELETE``, ``HEAD``, ``OPTIONS``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#method SyntheticsTest#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_saving_response_body(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines whether or not to save the response body.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#no_saving_response_body SyntheticsTest#no_saving_response_body}
        '''
        result = self._values.get("no_saving_response_body")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def number_of_packets(self) -> typing.Optional[jsii.Number]:
        '''Number of pings to use per test for ICMP tests (``subtype = "icmp"``) between 0 and 10.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#number_of_packets SyntheticsTest#number_of_packets}
        '''
        result = self._values.get("number_of_packets")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to use when performing the test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#port SyntheticsTest#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def servername(self) -> typing.Optional[builtins.str]:
        '''For SSL tests, it specifies on which server you want to initiate the TLS handshake, allowing the server to present one of multiple possible certificates on the same IP address and TCP port number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#servername SyntheticsTest#servername}
        '''
        result = self._values.get("servername")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''For gRPC tests, service to target for healthcheck.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#service SyntheticsTest#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def should_track_hops(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''This will turn on a traceroute probe to discover all gateways along the path to the host destination.

        For ICMP tests (``subtype = "icmp"``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#should_track_hops SyntheticsTest#should_track_hops}
        '''
        result = self._values.get("should_track_hops")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Timeout in seconds for the test. Defaults to ``60``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#timeout SyntheticsTest#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''The URL to send the request to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestRequestDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestRequestDefinitionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestRequestDefinitionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetCertificateDomains")
    def reset_certificate_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateDomains", []))

    @jsii.member(jsii_name="resetDnsServer")
    def reset_dns_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServer", []))

    @jsii.member(jsii_name="resetDnsServerPort")
    def reset_dns_server_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServerPort", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetNoSavingResponseBody")
    def reset_no_saving_response_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoSavingResponseBody", []))

    @jsii.member(jsii_name="resetNumberOfPackets")
    def reset_number_of_packets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberOfPackets", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetServername")
    def reset_servername(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServername", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetShouldTrackHops")
    def reset_should_track_hops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShouldTrackHops", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateDomainsInput")
    def certificate_domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServerInput")
    def dns_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsServerInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServerPortInput")
    def dns_server_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dnsServerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="noSavingResponseBodyInput")
    def no_saving_response_body_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noSavingResponseBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfPacketsInput")
    def number_of_packets_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfPacketsInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="servernameInput")
    def servername_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servernameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="shouldTrackHopsInput")
    def should_track_hops_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shouldTrackHopsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="certificateDomains")
    def certificate_domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificateDomains"))

    @certificate_domains.setter
    def certificate_domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "certificate_domains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateDomains", value)

    @builtins.property
    @jsii.member(jsii_name="dnsServer")
    def dns_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsServer"))

    @dns_server.setter
    def dns_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "dns_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServer", value)

    @builtins.property
    @jsii.member(jsii_name="dnsServerPort")
    def dns_server_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dnsServerPort"))

    @dns_server_port.setter
    def dns_server_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "dns_server_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServerPort", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="noSavingResponseBody")
    def no_saving_response_body(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noSavingResponseBody"))

    @no_saving_response_body.setter
    def no_saving_response_body(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "no_saving_response_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noSavingResponseBody", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfPackets")
    def number_of_packets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfPackets"))

    @number_of_packets.setter
    def number_of_packets(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "number_of_packets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfPackets", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="servername")
    def servername(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servername"))

    @servername.setter
    def servername(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "servername").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servername", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="shouldTrackHops")
    def should_track_hops(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shouldTrackHops"))

    @should_track_hops.setter
    def should_track_hops(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "should_track_hops").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shouldTrackHops", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestRequestDefinition]:
        return typing.cast(typing.Optional[SyntheticsTestRequestDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestRequestDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestDefinitionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestProxy",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "headers": "headers"},
)
class SyntheticsTestRequestProxy:
    def __init__(
        self,
        *,
        url: builtins.str,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: URL of the proxy to perform the test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        :param headers: Header name and value map. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#headers SyntheticsTest#headers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsTestRequestProxy.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if headers is not None:
            self._values["headers"] = headers

    @builtins.property
    def url(self) -> builtins.str:
        '''URL of the proxy to perform the test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#url SyntheticsTest#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Header name and value map.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_test#headers SyntheticsTest#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsTestRequestProxy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsTestRequestProxyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsTest.SyntheticsTestRequestProxyOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsTestRequestProxyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestProxyOutputReference, "headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestProxyOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsTestRequestProxy]:
        return typing.cast(typing.Optional[SyntheticsTestRequestProxy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsTestRequestProxy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsTestRequestProxyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SyntheticsTest",
    "SyntheticsTestApiStep",
    "SyntheticsTestApiStepAssertion",
    "SyntheticsTestApiStepAssertionList",
    "SyntheticsTestApiStepAssertionOutputReference",
    "SyntheticsTestApiStepAssertionTargetjsonpath",
    "SyntheticsTestApiStepAssertionTargetjsonpathOutputReference",
    "SyntheticsTestApiStepExtractedValue",
    "SyntheticsTestApiStepExtractedValueList",
    "SyntheticsTestApiStepExtractedValueOutputReference",
    "SyntheticsTestApiStepExtractedValueParser",
    "SyntheticsTestApiStepExtractedValueParserOutputReference",
    "SyntheticsTestApiStepList",
    "SyntheticsTestApiStepOutputReference",
    "SyntheticsTestApiStepRequestBasicauth",
    "SyntheticsTestApiStepRequestBasicauthOutputReference",
    "SyntheticsTestApiStepRequestClientCertificate",
    "SyntheticsTestApiStepRequestClientCertificateCert",
    "SyntheticsTestApiStepRequestClientCertificateCertOutputReference",
    "SyntheticsTestApiStepRequestClientCertificateKey",
    "SyntheticsTestApiStepRequestClientCertificateKeyOutputReference",
    "SyntheticsTestApiStepRequestClientCertificateOutputReference",
    "SyntheticsTestApiStepRequestDefinition",
    "SyntheticsTestApiStepRequestDefinitionOutputReference",
    "SyntheticsTestApiStepRequestProxy",
    "SyntheticsTestApiStepRequestProxyOutputReference",
    "SyntheticsTestApiStepRetry",
    "SyntheticsTestApiStepRetryOutputReference",
    "SyntheticsTestAssertion",
    "SyntheticsTestAssertionList",
    "SyntheticsTestAssertionOutputReference",
    "SyntheticsTestAssertionTargetjsonpath",
    "SyntheticsTestAssertionTargetjsonpathOutputReference",
    "SyntheticsTestBrowserStep",
    "SyntheticsTestBrowserStepList",
    "SyntheticsTestBrowserStepOutputReference",
    "SyntheticsTestBrowserStepParams",
    "SyntheticsTestBrowserStepParamsElementUserLocator",
    "SyntheticsTestBrowserStepParamsElementUserLocatorOutputReference",
    "SyntheticsTestBrowserStepParamsElementUserLocatorValue",
    "SyntheticsTestBrowserStepParamsElementUserLocatorValueOutputReference",
    "SyntheticsTestBrowserStepParamsOutputReference",
    "SyntheticsTestBrowserStepParamsVariable",
    "SyntheticsTestBrowserStepParamsVariableOutputReference",
    "SyntheticsTestBrowserVariable",
    "SyntheticsTestBrowserVariableList",
    "SyntheticsTestBrowserVariableOutputReference",
    "SyntheticsTestConfig",
    "SyntheticsTestConfigVariable",
    "SyntheticsTestConfigVariableList",
    "SyntheticsTestConfigVariableOutputReference",
    "SyntheticsTestOptionsList",
    "SyntheticsTestOptionsListCi",
    "SyntheticsTestOptionsListCiOutputReference",
    "SyntheticsTestOptionsListMonitorOptions",
    "SyntheticsTestOptionsListMonitorOptionsOutputReference",
    "SyntheticsTestOptionsListOutputReference",
    "SyntheticsTestOptionsListRetry",
    "SyntheticsTestOptionsListRetryOutputReference",
    "SyntheticsTestOptionsListRumSettings",
    "SyntheticsTestOptionsListRumSettingsOutputReference",
    "SyntheticsTestRequestBasicauth",
    "SyntheticsTestRequestBasicauthOutputReference",
    "SyntheticsTestRequestClientCertificate",
    "SyntheticsTestRequestClientCertificateCert",
    "SyntheticsTestRequestClientCertificateCertOutputReference",
    "SyntheticsTestRequestClientCertificateKey",
    "SyntheticsTestRequestClientCertificateKeyOutputReference",
    "SyntheticsTestRequestClientCertificateOutputReference",
    "SyntheticsTestRequestDefinition",
    "SyntheticsTestRequestDefinitionOutputReference",
    "SyntheticsTestRequestProxy",
    "SyntheticsTestRequestProxyOutputReference",
]

publication.publish()
