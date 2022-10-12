'''
# `google_app_engine_flexible_app_version`

Refer to the Terraform Registory for docs: [`google_app_engine_flexible_app_version`](https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version).
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


class GoogleAppEngineFlexibleAppVersion(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersion",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version google_app_engine_flexible_app_version}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        liveness_check: typing.Union["GoogleAppEngineFlexibleAppVersionLivenessCheck", typing.Dict[str, typing.Any]],
        readiness_check: typing.Union["GoogleAppEngineFlexibleAppVersionReadinessCheck", typing.Dict[str, typing.Any]],
        runtime: builtins.str,
        service: builtins.str,
        api_config: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionApiConfig", typing.Dict[str, typing.Any]]] = None,
        automatic_scaling: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScaling", typing.Dict[str, typing.Any]]] = None,
        beta_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_expiration: typing.Optional[builtins.str] = None,
        delete_service_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        deployment: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionDeployment", typing.Dict[str, typing.Any]]] = None,
        endpoints_api_service: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionEndpointsApiService", typing.Dict[str, typing.Any]]] = None,
        entrypoint: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionEntrypoint", typing.Dict[str, typing.Any]]] = None,
        env_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        handlers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAppEngineFlexibleAppVersionHandlers", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        inbound_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_class: typing.Optional[builtins.str] = None,
        manual_scaling: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionManualScaling", typing.Dict[str, typing.Any]]] = None,
        network: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionNetwork", typing.Dict[str, typing.Any]]] = None,
        nobuild_files_regex: typing.Optional[builtins.str] = None,
        noop_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project: typing.Optional[builtins.str] = None,
        resources: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionResources", typing.Dict[str, typing.Any]]] = None,
        runtime_api_version: typing.Optional[builtins.str] = None,
        runtime_channel: typing.Optional[builtins.str] = None,
        runtime_main_executable_path: typing.Optional[builtins.str] = None,
        service_account: typing.Optional[builtins.str] = None,
        serving_status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionTimeouts", typing.Dict[str, typing.Any]]] = None,
        version_id: typing.Optional[builtins.str] = None,
        vpc_access_connector: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionVpcAccessConnector", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version google_app_engine_flexible_app_version} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param liveness_check: liveness_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#liveness_check GoogleAppEngineFlexibleAppVersion#liveness_check}
        :param readiness_check: readiness_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#readiness_check GoogleAppEngineFlexibleAppVersion#readiness_check}
        :param runtime: Desired runtime. Example python27. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime GoogleAppEngineFlexibleAppVersion#runtime}
        :param service: AppEngine service resource. Can contain numbers, letters, and hyphens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#service GoogleAppEngineFlexibleAppVersion#service}
        :param api_config: api_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#api_config GoogleAppEngineFlexibleAppVersion#api_config}
        :param automatic_scaling: automatic_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#automatic_scaling GoogleAppEngineFlexibleAppVersion#automatic_scaling}
        :param beta_settings: Metadata settings that are supplied to this version to enable beta runtime features. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#beta_settings GoogleAppEngineFlexibleAppVersion#beta_settings}
        :param default_expiration: Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#default_expiration GoogleAppEngineFlexibleAppVersion#default_expiration}
        :param delete_service_on_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#delete_service_on_destroy GoogleAppEngineFlexibleAppVersion#delete_service_on_destroy}.
        :param deployment: deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#deployment GoogleAppEngineFlexibleAppVersion#deployment}
        :param endpoints_api_service: endpoints_api_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#endpoints_api_service GoogleAppEngineFlexibleAppVersion#endpoints_api_service}
        :param entrypoint: entrypoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#entrypoint GoogleAppEngineFlexibleAppVersion#entrypoint}
        :param env_variables: Environment variables available to the application. As these are not returned in the API request, Terraform will not detect any changes made outside of the Terraform config. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#env_variables GoogleAppEngineFlexibleAppVersion#env_variables}
        :param handlers: handlers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#handlers GoogleAppEngineFlexibleAppVersion#handlers}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#id GoogleAppEngineFlexibleAppVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inbound_services: A list of the types of messages that this application is able to receive. Possible values: ["INBOUND_SERVICE_MAIL", "INBOUND_SERVICE_MAIL_BOUNCE", "INBOUND_SERVICE_XMPP_ERROR", "INBOUND_SERVICE_XMPP_MESSAGE", "INBOUND_SERVICE_XMPP_SUBSCRIBE", "INBOUND_SERVICE_XMPP_PRESENCE", "INBOUND_SERVICE_CHANNEL_PRESENCE", "INBOUND_SERVICE_WARMUP"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#inbound_services GoogleAppEngineFlexibleAppVersion#inbound_services}
        :param instance_class: Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1, B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instance_class GoogleAppEngineFlexibleAppVersion#instance_class}
        :param manual_scaling: manual_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#manual_scaling GoogleAppEngineFlexibleAppVersion#manual_scaling}
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#network GoogleAppEngineFlexibleAppVersion#network}
        :param nobuild_files_regex: Files that match this pattern will not be built into this version. Only applicable for Go runtimes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#nobuild_files_regex GoogleAppEngineFlexibleAppVersion#nobuild_files_regex}
        :param noop_on_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#noop_on_destroy GoogleAppEngineFlexibleAppVersion#noop_on_destroy}.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#project GoogleAppEngineFlexibleAppVersion#project}.
        :param resources: resources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#resources GoogleAppEngineFlexibleAppVersion#resources}
        :param runtime_api_version: The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at 'https://cloud.google.com/appengine/docs/standard//config/appref' Substitute '' with 'python', 'java', 'php', 'ruby', 'go' or 'nodejs'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_api_version GoogleAppEngineFlexibleAppVersion#runtime_api_version}
        :param runtime_channel: The channel of the runtime to use. Only available for some runtimes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_channel GoogleAppEngineFlexibleAppVersion#runtime_channel}
        :param runtime_main_executable_path: The path or name of the app's main executable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_main_executable_path GoogleAppEngineFlexibleAppVersion#runtime_main_executable_path}
        :param service_account: The identity that the deployed version will run as. Admin API will use the App Engine Appspot service account as default if this field is neither provided in app.yaml file nor through CLI flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#service_account GoogleAppEngineFlexibleAppVersion#service_account}
        :param serving_status: Current serving status of this version. Only the versions with a SERVING status create instances and can be billed. Default value: "SERVING" Possible values: ["SERVING", "STOPPED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#serving_status GoogleAppEngineFlexibleAppVersion#serving_status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeouts GoogleAppEngineFlexibleAppVersion#timeouts}
        :param version_id: Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#version_id GoogleAppEngineFlexibleAppVersion#version_id}
        :param vpc_access_connector: vpc_access_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#vpc_access_connector GoogleAppEngineFlexibleAppVersion#vpc_access_connector}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersion.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleAppEngineFlexibleAppVersionConfig(
            liveness_check=liveness_check,
            readiness_check=readiness_check,
            runtime=runtime,
            service=service,
            api_config=api_config,
            automatic_scaling=automatic_scaling,
            beta_settings=beta_settings,
            default_expiration=default_expiration,
            delete_service_on_destroy=delete_service_on_destroy,
            deployment=deployment,
            endpoints_api_service=endpoints_api_service,
            entrypoint=entrypoint,
            env_variables=env_variables,
            handlers=handlers,
            id=id,
            inbound_services=inbound_services,
            instance_class=instance_class,
            manual_scaling=manual_scaling,
            network=network,
            nobuild_files_regex=nobuild_files_regex,
            noop_on_destroy=noop_on_destroy,
            project=project,
            resources=resources,
            runtime_api_version=runtime_api_version,
            runtime_channel=runtime_channel,
            runtime_main_executable_path=runtime_main_executable_path,
            service_account=service_account,
            serving_status=serving_status,
            timeouts=timeouts,
            version_id=version_id,
            vpc_access_connector=vpc_access_connector,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApiConfig")
    def put_api_config(
        self,
        *,
        script: builtins.str,
        auth_fail_action: typing.Optional[builtins.str] = None,
        login: typing.Optional[builtins.str] = None,
        security_level: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param script: Path to the script from the application root directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#script GoogleAppEngineFlexibleAppVersion#script}
        :param auth_fail_action: Action to take when users access resources that require authentication. Default value: "AUTH_FAIL_ACTION_REDIRECT" Possible values: ["AUTH_FAIL_ACTION_REDIRECT", "AUTH_FAIL_ACTION_UNAUTHORIZED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#auth_fail_action GoogleAppEngineFlexibleAppVersion#auth_fail_action}
        :param login: Level of login required to access this resource. Default value: "LOGIN_OPTIONAL" Possible values: ["LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#login GoogleAppEngineFlexibleAppVersion#login}
        :param security_level: Security (HTTPS) enforcement for this URL. Possible values: ["SECURE_DEFAULT", "SECURE_NEVER", "SECURE_OPTIONAL", "SECURE_ALWAYS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#security_level GoogleAppEngineFlexibleAppVersion#security_level}
        :param url: URL to serve the endpoint at. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#url GoogleAppEngineFlexibleAppVersion#url}
        '''
        value = GoogleAppEngineFlexibleAppVersionApiConfig(
            script=script,
            auth_fail_action=auth_fail_action,
            login=login,
            security_level=security_level,
            url=url,
        )

        return typing.cast(None, jsii.invoke(self, "putApiConfig", [value]))

    @jsii.member(jsii_name="putAutomaticScaling")
    def put_automatic_scaling(
        self,
        *,
        cpu_utilization: typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization", typing.Dict[str, typing.Any]],
        cool_down_period: typing.Optional[builtins.str] = None,
        disk_utilization: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization", typing.Dict[str, typing.Any]]] = None,
        max_concurrent_requests: typing.Optional[jsii.Number] = None,
        max_idle_instances: typing.Optional[jsii.Number] = None,
        max_pending_latency: typing.Optional[builtins.str] = None,
        max_total_instances: typing.Optional[jsii.Number] = None,
        min_idle_instances: typing.Optional[jsii.Number] = None,
        min_pending_latency: typing.Optional[builtins.str] = None,
        min_total_instances: typing.Optional[jsii.Number] = None,
        network_utilization: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization", typing.Dict[str, typing.Any]]] = None,
        request_utilization: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cpu_utilization: cpu_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cpu_utilization GoogleAppEngineFlexibleAppVersion#cpu_utilization}
        :param cool_down_period: The time period that the Autoscaler should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. Default: 120s Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cool_down_period GoogleAppEngineFlexibleAppVersion#cool_down_period}
        :param disk_utilization: disk_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disk_utilization GoogleAppEngineFlexibleAppVersion#disk_utilization}
        :param max_concurrent_requests: Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance. Defaults to a runtime-specific value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_concurrent_requests GoogleAppEngineFlexibleAppVersion#max_concurrent_requests}
        :param max_idle_instances: Maximum number of idle instances that should be maintained for this version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_idle_instances GoogleAppEngineFlexibleAppVersion#max_idle_instances}
        :param max_pending_latency: Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_pending_latency GoogleAppEngineFlexibleAppVersion#max_pending_latency}
        :param max_total_instances: Maximum number of instances that should be started to handle requests for this version. Default: 20. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_total_instances GoogleAppEngineFlexibleAppVersion#max_total_instances}
        :param min_idle_instances: Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_idle_instances GoogleAppEngineFlexibleAppVersion#min_idle_instances}
        :param min_pending_latency: Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_pending_latency GoogleAppEngineFlexibleAppVersion#min_pending_latency}
        :param min_total_instances: Minimum number of running instances that should be maintained for this version. Default: 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_total_instances GoogleAppEngineFlexibleAppVersion#min_total_instances}
        :param network_utilization: network_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#network_utilization GoogleAppEngineFlexibleAppVersion#network_utilization}
        :param request_utilization: request_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#request_utilization GoogleAppEngineFlexibleAppVersion#request_utilization}
        '''
        value = GoogleAppEngineFlexibleAppVersionAutomaticScaling(
            cpu_utilization=cpu_utilization,
            cool_down_period=cool_down_period,
            disk_utilization=disk_utilization,
            max_concurrent_requests=max_concurrent_requests,
            max_idle_instances=max_idle_instances,
            max_pending_latency=max_pending_latency,
            max_total_instances=max_total_instances,
            min_idle_instances=min_idle_instances,
            min_pending_latency=min_pending_latency,
            min_total_instances=min_total_instances,
            network_utilization=network_utilization,
            request_utilization=request_utilization,
        )

        return typing.cast(None, jsii.invoke(self, "putAutomaticScaling", [value]))

    @jsii.member(jsii_name="putDeployment")
    def put_deployment(
        self,
        *,
        cloud_build_options: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions", typing.Dict[str, typing.Any]]] = None,
        container: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionDeploymentContainer", typing.Dict[str, typing.Any]]] = None,
        files: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAppEngineFlexibleAppVersionDeploymentFiles", typing.Dict[str, typing.Any]]]]] = None,
        zip: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionDeploymentZip", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_build_options: cloud_build_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cloud_build_options GoogleAppEngineFlexibleAppVersion#cloud_build_options}
        :param container: container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#container GoogleAppEngineFlexibleAppVersion#container}
        :param files: files block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#files GoogleAppEngineFlexibleAppVersion#files}
        :param zip: zip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#zip GoogleAppEngineFlexibleAppVersion#zip}
        '''
        value = GoogleAppEngineFlexibleAppVersionDeployment(
            cloud_build_options=cloud_build_options,
            container=container,
            files=files,
            zip=zip,
        )

        return typing.cast(None, jsii.invoke(self, "putDeployment", [value]))

    @jsii.member(jsii_name="putEndpointsApiService")
    def put_endpoints_api_service(
        self,
        *,
        name: builtins.str,
        config_id: typing.Optional[builtins.str] = None,
        disable_trace_sampling: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rollout_strategy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Endpoints service name which is the name of the "service" resource in the Service Management API. For example "myapi.endpoints.myproject.cloud.goog". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        :param config_id: Endpoints service configuration ID as specified by the Service Management API. For example "2016-09-19r1". By default, the rollout strategy for Endpoints is "FIXED". This means that Endpoints starts up with a particular configuration ID. When a new configuration is rolled out, Endpoints must be given the new configuration ID. The configId field is used to give the configuration ID and is required in this case. Endpoints also has a rollout strategy called "MANAGED". When using this, Endpoints fetches the latest configuration and does not need the configuration ID. In this case, configId must be omitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#config_id GoogleAppEngineFlexibleAppVersion#config_id}
        :param disable_trace_sampling: Enable or disable trace sampling. By default, this is set to false for enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disable_trace_sampling GoogleAppEngineFlexibleAppVersion#disable_trace_sampling}
        :param rollout_strategy: Endpoints rollout strategy. If FIXED, configId must be specified. If MANAGED, configId must be omitted. Default value: "FIXED" Possible values: ["FIXED", "MANAGED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#rollout_strategy GoogleAppEngineFlexibleAppVersion#rollout_strategy}
        '''
        value = GoogleAppEngineFlexibleAppVersionEndpointsApiService(
            name=name,
            config_id=config_id,
            disable_trace_sampling=disable_trace_sampling,
            rollout_strategy=rollout_strategy,
        )

        return typing.cast(None, jsii.invoke(self, "putEndpointsApiService", [value]))

    @jsii.member(jsii_name="putEntrypoint")
    def put_entrypoint(self, *, shell: builtins.str) -> None:
        '''
        :param shell: The format should be a shell command that can be fed to bash -c. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#shell GoogleAppEngineFlexibleAppVersion#shell}
        '''
        value = GoogleAppEngineFlexibleAppVersionEntrypoint(shell=shell)

        return typing.cast(None, jsii.invoke(self, "putEntrypoint", [value]))

    @jsii.member(jsii_name="putHandlers")
    def put_handlers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAppEngineFlexibleAppVersionHandlers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersion.put_handlers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHandlers", [value]))

    @jsii.member(jsii_name="putLivenessCheck")
    def put_liveness_check(
        self,
        *,
        path: builtins.str,
        check_interval: typing.Optional[builtins.str] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        host: typing.Optional[builtins.str] = None,
        initial_delay: typing.Optional[builtins.str] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: The request path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        :param check_interval: Interval between health checks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#check_interval GoogleAppEngineFlexibleAppVersion#check_interval}
        :param failure_threshold: Number of consecutive failed checks required before considering the VM unhealthy. Default: 4. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#failure_threshold GoogleAppEngineFlexibleAppVersion#failure_threshold}
        :param host: Host header to send when performing a HTTP Readiness check. Example: "myapp.appspot.com". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#host GoogleAppEngineFlexibleAppVersion#host}
        :param initial_delay: The initial delay before starting to execute the checks. Default: "300s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#initial_delay GoogleAppEngineFlexibleAppVersion#initial_delay}
        :param success_threshold: Number of consecutive successful checks required before considering the VM healthy. Default: 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#success_threshold GoogleAppEngineFlexibleAppVersion#success_threshold}
        :param timeout: Time before the check is considered failed. Default: "4s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeout GoogleAppEngineFlexibleAppVersion#timeout}
        '''
        value = GoogleAppEngineFlexibleAppVersionLivenessCheck(
            path=path,
            check_interval=check_interval,
            failure_threshold=failure_threshold,
            host=host,
            initial_delay=initial_delay,
            success_threshold=success_threshold,
            timeout=timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putLivenessCheck", [value]))

    @jsii.member(jsii_name="putManualScaling")
    def put_manual_scaling(self, *, instances: jsii.Number) -> None:
        '''
        :param instances: Number of instances to assign to the service at the start. *Note:** When managing the number of instances at runtime through the App Engine Admin API or the (now deprecated) Python 2 Modules API set_num_instances() you must use 'lifecycle.ignore_changes = ["manual_scaling"[0].instances]' to prevent drift detection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instances GoogleAppEngineFlexibleAppVersion#instances}
        '''
        value = GoogleAppEngineFlexibleAppVersionManualScaling(instances=instances)

        return typing.cast(None, jsii.invoke(self, "putManualScaling", [value]))

    @jsii.member(jsii_name="putNetwork")
    def put_network(
        self,
        *,
        name: builtins.str,
        forwarded_ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_tag: typing.Optional[builtins.str] = None,
        session_affinity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Google Compute Engine network where the virtual machines are created. Specify the short name, not the resource path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        :param forwarded_ports: List of ports, or port pairs, to forward from the virtual machine to the application container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#forwarded_ports GoogleAppEngineFlexibleAppVersion#forwarded_ports}
        :param instance_tag: Tag to apply to the instance during creation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instance_tag GoogleAppEngineFlexibleAppVersion#instance_tag}
        :param session_affinity: Enable session affinity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#session_affinity GoogleAppEngineFlexibleAppVersion#session_affinity}
        :param subnetwork: Google Cloud Platform sub-network where the virtual machines are created. Specify the short name, not the resource path. If the network that the instance is being created in is a Legacy network, then the IP address is allocated from the IPv4Range. If the network that the instance is being created in is an auto Subnet Mode Network, then only network name should be specified (not the subnetworkName) and the IP address is created from the IPCidrRange of the subnetwork that exists in that zone for that network. If the network that the instance is being created in is a custom Subnet Mode Network, then the subnetworkName must be specified and the IP address is created from the IPCidrRange of the subnetwork. If specified, the subnetwork must exist in the same region as the App Engine flexible environment application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#subnetwork GoogleAppEngineFlexibleAppVersion#subnetwork}
        '''
        value = GoogleAppEngineFlexibleAppVersionNetwork(
            name=name,
            forwarded_ports=forwarded_ports,
            instance_tag=instance_tag,
            session_affinity=session_affinity,
            subnetwork=subnetwork,
        )

        return typing.cast(None, jsii.invoke(self, "putNetwork", [value]))

    @jsii.member(jsii_name="putReadinessCheck")
    def put_readiness_check(
        self,
        *,
        path: builtins.str,
        app_start_timeout: typing.Optional[builtins.str] = None,
        check_interval: typing.Optional[builtins.str] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        host: typing.Optional[builtins.str] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: The request path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        :param app_start_timeout: A maximum time limit on application initialization, measured from moment the application successfully replies to a healthcheck until it is ready to serve traffic. Default: "300s" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#app_start_timeout GoogleAppEngineFlexibleAppVersion#app_start_timeout}
        :param check_interval: Interval between health checks. Default: "5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#check_interval GoogleAppEngineFlexibleAppVersion#check_interval}
        :param failure_threshold: Number of consecutive failed checks required before removing traffic. Default: 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#failure_threshold GoogleAppEngineFlexibleAppVersion#failure_threshold}
        :param host: Host header to send when performing a HTTP Readiness check. Example: "myapp.appspot.com". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#host GoogleAppEngineFlexibleAppVersion#host}
        :param success_threshold: Number of consecutive successful checks required before receiving traffic. Default: 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#success_threshold GoogleAppEngineFlexibleAppVersion#success_threshold}
        :param timeout: Time before the check is considered failed. Default: "4s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeout GoogleAppEngineFlexibleAppVersion#timeout}
        '''
        value = GoogleAppEngineFlexibleAppVersionReadinessCheck(
            path=path,
            app_start_timeout=app_start_timeout,
            check_interval=check_interval,
            failure_threshold=failure_threshold,
            host=host,
            success_threshold=success_threshold,
            timeout=timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putReadinessCheck", [value]))

    @jsii.member(jsii_name="putResources")
    def put_resources(
        self,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        disk_gb: typing.Optional[jsii.Number] = None,
        memory_gb: typing.Optional[jsii.Number] = None,
        volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAppEngineFlexibleAppVersionResourcesVolumes", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cpu: Number of CPU cores needed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cpu GoogleAppEngineFlexibleAppVersion#cpu}
        :param disk_gb: Disk size (GB) needed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disk_gb GoogleAppEngineFlexibleAppVersion#disk_gb}
        :param memory_gb: Memory (GB) needed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#memory_gb GoogleAppEngineFlexibleAppVersion#memory_gb}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#volumes GoogleAppEngineFlexibleAppVersion#volumes}
        '''
        value = GoogleAppEngineFlexibleAppVersionResources(
            cpu=cpu, disk_gb=disk_gb, memory_gb=memory_gb, volumes=volumes
        )

        return typing.cast(None, jsii.invoke(self, "putResources", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#create GoogleAppEngineFlexibleAppVersion#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#delete GoogleAppEngineFlexibleAppVersion#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#update GoogleAppEngineFlexibleAppVersion#update}.
        '''
        value = GoogleAppEngineFlexibleAppVersionTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpcAccessConnector")
    def put_vpc_access_connector(self, *, name: builtins.str) -> None:
        '''
        :param name: Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        '''
        value = GoogleAppEngineFlexibleAppVersionVpcAccessConnector(name=name)

        return typing.cast(None, jsii.invoke(self, "putVpcAccessConnector", [value]))

    @jsii.member(jsii_name="resetApiConfig")
    def reset_api_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiConfig", []))

    @jsii.member(jsii_name="resetAutomaticScaling")
    def reset_automatic_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticScaling", []))

    @jsii.member(jsii_name="resetBetaSettings")
    def reset_beta_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBetaSettings", []))

    @jsii.member(jsii_name="resetDefaultExpiration")
    def reset_default_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultExpiration", []))

    @jsii.member(jsii_name="resetDeleteServiceOnDestroy")
    def reset_delete_service_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteServiceOnDestroy", []))

    @jsii.member(jsii_name="resetDeployment")
    def reset_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployment", []))

    @jsii.member(jsii_name="resetEndpointsApiService")
    def reset_endpoints_api_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointsApiService", []))

    @jsii.member(jsii_name="resetEntrypoint")
    def reset_entrypoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntrypoint", []))

    @jsii.member(jsii_name="resetEnvVariables")
    def reset_env_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvVariables", []))

    @jsii.member(jsii_name="resetHandlers")
    def reset_handlers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHandlers", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInboundServices")
    def reset_inbound_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInboundServices", []))

    @jsii.member(jsii_name="resetInstanceClass")
    def reset_instance_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceClass", []))

    @jsii.member(jsii_name="resetManualScaling")
    def reset_manual_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManualScaling", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetNobuildFilesRegex")
    def reset_nobuild_files_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNobuildFilesRegex", []))

    @jsii.member(jsii_name="resetNoopOnDestroy")
    def reset_noop_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoopOnDestroy", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

    @jsii.member(jsii_name="resetRuntimeApiVersion")
    def reset_runtime_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeApiVersion", []))

    @jsii.member(jsii_name="resetRuntimeChannel")
    def reset_runtime_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeChannel", []))

    @jsii.member(jsii_name="resetRuntimeMainExecutablePath")
    def reset_runtime_main_executable_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeMainExecutablePath", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetServingStatus")
    def reset_serving_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServingStatus", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersionId")
    def reset_version_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionId", []))

    @jsii.member(jsii_name="resetVpcAccessConnector")
    def reset_vpc_access_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcAccessConnector", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="apiConfig")
    def api_config(self) -> "GoogleAppEngineFlexibleAppVersionApiConfigOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionApiConfigOutputReference", jsii.get(self, "apiConfig"))

    @builtins.property
    @jsii.member(jsii_name="automaticScaling")
    def automatic_scaling(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference", jsii.get(self, "automaticScaling"))

    @builtins.property
    @jsii.member(jsii_name="deployment")
    def deployment(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionDeploymentOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionDeploymentOutputReference", jsii.get(self, "deployment"))

    @builtins.property
    @jsii.member(jsii_name="endpointsApiService")
    def endpoints_api_service(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference", jsii.get(self, "endpointsApiService"))

    @builtins.property
    @jsii.member(jsii_name="entrypoint")
    def entrypoint(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionEntrypointOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionEntrypointOutputReference", jsii.get(self, "entrypoint"))

    @builtins.property
    @jsii.member(jsii_name="handlers")
    def handlers(self) -> "GoogleAppEngineFlexibleAppVersionHandlersList":
        return typing.cast("GoogleAppEngineFlexibleAppVersionHandlersList", jsii.get(self, "handlers"))

    @builtins.property
    @jsii.member(jsii_name="livenessCheck")
    def liveness_check(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference", jsii.get(self, "livenessCheck"))

    @builtins.property
    @jsii.member(jsii_name="manualScaling")
    def manual_scaling(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionManualScalingOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionManualScalingOutputReference", jsii.get(self, "manualScaling"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> "GoogleAppEngineFlexibleAppVersionNetworkOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionNetworkOutputReference", jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="readinessCheck")
    def readiness_check(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference", jsii.get(self, "readinessCheck"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> "GoogleAppEngineFlexibleAppVersionResourcesOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionResourcesOutputReference", jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcAccessConnector")
    def vpc_access_connector(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionVpcAccessConnectorOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionVpcAccessConnectorOutputReference", jsii.get(self, "vpcAccessConnector"))

    @builtins.property
    @jsii.member(jsii_name="apiConfigInput")
    def api_config_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionApiConfig"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionApiConfig"], jsii.get(self, "apiConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticScalingInput")
    def automatic_scaling_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScaling"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScaling"], jsii.get(self, "automaticScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="betaSettingsInput")
    def beta_settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "betaSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultExpirationInput")
    def default_expiration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteServiceOnDestroyInput")
    def delete_service_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteServiceOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentInput")
    def deployment_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionDeployment"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionDeployment"], jsii.get(self, "deploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointsApiServiceInput")
    def endpoints_api_service_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionEndpointsApiService"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionEndpointsApiService"], jsii.get(self, "endpointsApiServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="entrypointInput")
    def entrypoint_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionEntrypoint"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionEntrypoint"], jsii.get(self, "entrypointInput"))

    @builtins.property
    @jsii.member(jsii_name="envVariablesInput")
    def env_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "envVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="handlersInput")
    def handlers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionHandlers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionHandlers"]]], jsii.get(self, "handlersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inboundServicesInput")
    def inbound_services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inboundServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceClassInput")
    def instance_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceClassInput"))

    @builtins.property
    @jsii.member(jsii_name="livenessCheckInput")
    def liveness_check_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionLivenessCheck"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionLivenessCheck"], jsii.get(self, "livenessCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="manualScalingInput")
    def manual_scaling_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionManualScaling"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionManualScaling"], jsii.get(self, "manualScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionNetwork"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionNetwork"], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="nobuildFilesRegexInput")
    def nobuild_files_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nobuildFilesRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="noopOnDestroyInput")
    def noop_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noopOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="readinessCheckInput")
    def readiness_check_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionReadinessCheck"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionReadinessCheck"], jsii.get(self, "readinessCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionResources"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionResources"], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeApiVersionInput")
    def runtime_api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeApiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeChannelInput")
    def runtime_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeMainExecutablePathInput")
    def runtime_main_executable_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeMainExecutablePathInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="servingStatusInput")
    def serving_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servingStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionIdInput")
    def version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcAccessConnectorInput")
    def vpc_access_connector_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionVpcAccessConnector"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionVpcAccessConnector"], jsii.get(self, "vpcAccessConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="betaSettings")
    def beta_settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "betaSettings"))

    @beta_settings.setter
    def beta_settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "beta_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "betaSettings", value)

    @builtins.property
    @jsii.member(jsii_name="defaultExpiration")
    def default_expiration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultExpiration"))

    @default_expiration.setter
    def default_expiration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "default_expiration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultExpiration", value)

    @builtins.property
    @jsii.member(jsii_name="deleteServiceOnDestroy")
    def delete_service_on_destroy(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deleteServiceOnDestroy"))

    @delete_service_on_destroy.setter
    def delete_service_on_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "delete_service_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteServiceOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="envVariables")
    def env_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "envVariables"))

    @env_variables.setter
    def env_variables(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "env_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "envVariables", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="inboundServices")
    def inbound_services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inboundServices"))

    @inbound_services.setter
    def inbound_services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "inbound_services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inboundServices", value)

    @builtins.property
    @jsii.member(jsii_name="instanceClass")
    def instance_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceClass"))

    @instance_class.setter
    def instance_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "instance_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceClass", value)

    @builtins.property
    @jsii.member(jsii_name="nobuildFilesRegex")
    def nobuild_files_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nobuildFilesRegex"))

    @nobuild_files_regex.setter
    def nobuild_files_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "nobuild_files_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nobuildFilesRegex", value)

    @builtins.property
    @jsii.member(jsii_name="noopOnDestroy")
    def noop_on_destroy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noopOnDestroy"))

    @noop_on_destroy.setter
    def noop_on_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "noop_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noopOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "runtime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeApiVersion")
    def runtime_api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeApiVersion"))

    @runtime_api_version.setter
    def runtime_api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "runtime_api_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeApiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeChannel")
    def runtime_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeChannel"))

    @runtime_channel.setter
    def runtime_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "runtime_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeChannel", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeMainExecutablePath")
    def runtime_main_executable_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeMainExecutablePath"))

    @runtime_main_executable_path.setter
    def runtime_main_executable_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "runtime_main_executable_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeMainExecutablePath", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="servingStatus")
    def serving_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servingStatus"))

    @serving_status.setter
    def serving_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "serving_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servingStatus", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersion, "version_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionApiConfig",
    jsii_struct_bases=[],
    name_mapping={
        "script": "script",
        "auth_fail_action": "authFailAction",
        "login": "login",
        "security_level": "securityLevel",
        "url": "url",
    },
)
class GoogleAppEngineFlexibleAppVersionApiConfig:
    def __init__(
        self,
        *,
        script: builtins.str,
        auth_fail_action: typing.Optional[builtins.str] = None,
        login: typing.Optional[builtins.str] = None,
        security_level: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param script: Path to the script from the application root directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#script GoogleAppEngineFlexibleAppVersion#script}
        :param auth_fail_action: Action to take when users access resources that require authentication. Default value: "AUTH_FAIL_ACTION_REDIRECT" Possible values: ["AUTH_FAIL_ACTION_REDIRECT", "AUTH_FAIL_ACTION_UNAUTHORIZED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#auth_fail_action GoogleAppEngineFlexibleAppVersion#auth_fail_action}
        :param login: Level of login required to access this resource. Default value: "LOGIN_OPTIONAL" Possible values: ["LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#login GoogleAppEngineFlexibleAppVersion#login}
        :param security_level: Security (HTTPS) enforcement for this URL. Possible values: ["SECURE_DEFAULT", "SECURE_NEVER", "SECURE_OPTIONAL", "SECURE_ALWAYS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#security_level GoogleAppEngineFlexibleAppVersion#security_level}
        :param url: URL to serve the endpoint at. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#url GoogleAppEngineFlexibleAppVersion#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionApiConfig.__init__)
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument auth_fail_action", value=auth_fail_action, expected_type=type_hints["auth_fail_action"])
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument security_level", value=security_level, expected_type=type_hints["security_level"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "script": script,
        }
        if auth_fail_action is not None:
            self._values["auth_fail_action"] = auth_fail_action
        if login is not None:
            self._values["login"] = login
        if security_level is not None:
            self._values["security_level"] = security_level
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def script(self) -> builtins.str:
        '''Path to the script from the application root directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#script GoogleAppEngineFlexibleAppVersion#script}
        '''
        result = self._values.get("script")
        assert result is not None, "Required property 'script' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_fail_action(self) -> typing.Optional[builtins.str]:
        '''Action to take when users access resources that require authentication. Default value: "AUTH_FAIL_ACTION_REDIRECT" Possible values: ["AUTH_FAIL_ACTION_REDIRECT", "AUTH_FAIL_ACTION_UNAUTHORIZED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#auth_fail_action GoogleAppEngineFlexibleAppVersion#auth_fail_action}
        '''
        result = self._values.get("auth_fail_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login(self) -> typing.Optional[builtins.str]:
        '''Level of login required to access this resource. Default value: "LOGIN_OPTIONAL" Possible values: ["LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#login GoogleAppEngineFlexibleAppVersion#login}
        '''
        result = self._values.get("login")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_level(self) -> typing.Optional[builtins.str]:
        '''Security (HTTPS) enforcement for this URL. Possible values: ["SECURE_DEFAULT", "SECURE_NEVER", "SECURE_OPTIONAL", "SECURE_ALWAYS"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#security_level GoogleAppEngineFlexibleAppVersion#security_level}
        '''
        result = self._values.get("security_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''URL to serve the endpoint at.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#url GoogleAppEngineFlexibleAppVersion#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionApiConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionApiConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionApiConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionApiConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthFailAction")
    def reset_auth_fail_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthFailAction", []))

    @jsii.member(jsii_name="resetLogin")
    def reset_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogin", []))

    @jsii.member(jsii_name="resetSecurityLevel")
    def reset_security_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityLevel", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="authFailActionInput")
    def auth_fail_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authFailActionInput"))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptInput")
    def script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptInput"))

    @builtins.property
    @jsii.member(jsii_name="securityLevelInput")
    def security_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="authFailAction")
    def auth_fail_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authFailAction"))

    @auth_fail_action.setter
    def auth_fail_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionApiConfigOutputReference, "auth_fail_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authFailAction", value)

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "login"))

    @login.setter
    def login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionApiConfigOutputReference, "login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "login", value)

    @builtins.property
    @jsii.member(jsii_name="script")
    def script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "script"))

    @script.setter
    def script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionApiConfigOutputReference, "script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "script", value)

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityLevel"))

    @security_level.setter
    def security_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionApiConfigOutputReference, "security_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionApiConfigOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionApiConfig]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionApiConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionApiConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionApiConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScaling",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_utilization": "cpuUtilization",
        "cool_down_period": "coolDownPeriod",
        "disk_utilization": "diskUtilization",
        "max_concurrent_requests": "maxConcurrentRequests",
        "max_idle_instances": "maxIdleInstances",
        "max_pending_latency": "maxPendingLatency",
        "max_total_instances": "maxTotalInstances",
        "min_idle_instances": "minIdleInstances",
        "min_pending_latency": "minPendingLatency",
        "min_total_instances": "minTotalInstances",
        "network_utilization": "networkUtilization",
        "request_utilization": "requestUtilization",
    },
)
class GoogleAppEngineFlexibleAppVersionAutomaticScaling:
    def __init__(
        self,
        *,
        cpu_utilization: typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization", typing.Dict[str, typing.Any]],
        cool_down_period: typing.Optional[builtins.str] = None,
        disk_utilization: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization", typing.Dict[str, typing.Any]]] = None,
        max_concurrent_requests: typing.Optional[jsii.Number] = None,
        max_idle_instances: typing.Optional[jsii.Number] = None,
        max_pending_latency: typing.Optional[builtins.str] = None,
        max_total_instances: typing.Optional[jsii.Number] = None,
        min_idle_instances: typing.Optional[jsii.Number] = None,
        min_pending_latency: typing.Optional[builtins.str] = None,
        min_total_instances: typing.Optional[jsii.Number] = None,
        network_utilization: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization", typing.Dict[str, typing.Any]]] = None,
        request_utilization: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cpu_utilization: cpu_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cpu_utilization GoogleAppEngineFlexibleAppVersion#cpu_utilization}
        :param cool_down_period: The time period that the Autoscaler should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. Default: 120s Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cool_down_period GoogleAppEngineFlexibleAppVersion#cool_down_period}
        :param disk_utilization: disk_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disk_utilization GoogleAppEngineFlexibleAppVersion#disk_utilization}
        :param max_concurrent_requests: Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance. Defaults to a runtime-specific value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_concurrent_requests GoogleAppEngineFlexibleAppVersion#max_concurrent_requests}
        :param max_idle_instances: Maximum number of idle instances that should be maintained for this version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_idle_instances GoogleAppEngineFlexibleAppVersion#max_idle_instances}
        :param max_pending_latency: Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_pending_latency GoogleAppEngineFlexibleAppVersion#max_pending_latency}
        :param max_total_instances: Maximum number of instances that should be started to handle requests for this version. Default: 20. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_total_instances GoogleAppEngineFlexibleAppVersion#max_total_instances}
        :param min_idle_instances: Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_idle_instances GoogleAppEngineFlexibleAppVersion#min_idle_instances}
        :param min_pending_latency: Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_pending_latency GoogleAppEngineFlexibleAppVersion#min_pending_latency}
        :param min_total_instances: Minimum number of running instances that should be maintained for this version. Default: 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_total_instances GoogleAppEngineFlexibleAppVersion#min_total_instances}
        :param network_utilization: network_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#network_utilization GoogleAppEngineFlexibleAppVersion#network_utilization}
        :param request_utilization: request_utilization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#request_utilization GoogleAppEngineFlexibleAppVersion#request_utilization}
        '''
        if isinstance(cpu_utilization, dict):
            cpu_utilization = GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization(**cpu_utilization)
        if isinstance(disk_utilization, dict):
            disk_utilization = GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization(**disk_utilization)
        if isinstance(network_utilization, dict):
            network_utilization = GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization(**network_utilization)
        if isinstance(request_utilization, dict):
            request_utilization = GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization(**request_utilization)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScaling.__init__)
            check_type(argname="argument cpu_utilization", value=cpu_utilization, expected_type=type_hints["cpu_utilization"])
            check_type(argname="argument cool_down_period", value=cool_down_period, expected_type=type_hints["cool_down_period"])
            check_type(argname="argument disk_utilization", value=disk_utilization, expected_type=type_hints["disk_utilization"])
            check_type(argname="argument max_concurrent_requests", value=max_concurrent_requests, expected_type=type_hints["max_concurrent_requests"])
            check_type(argname="argument max_idle_instances", value=max_idle_instances, expected_type=type_hints["max_idle_instances"])
            check_type(argname="argument max_pending_latency", value=max_pending_latency, expected_type=type_hints["max_pending_latency"])
            check_type(argname="argument max_total_instances", value=max_total_instances, expected_type=type_hints["max_total_instances"])
            check_type(argname="argument min_idle_instances", value=min_idle_instances, expected_type=type_hints["min_idle_instances"])
            check_type(argname="argument min_pending_latency", value=min_pending_latency, expected_type=type_hints["min_pending_latency"])
            check_type(argname="argument min_total_instances", value=min_total_instances, expected_type=type_hints["min_total_instances"])
            check_type(argname="argument network_utilization", value=network_utilization, expected_type=type_hints["network_utilization"])
            check_type(argname="argument request_utilization", value=request_utilization, expected_type=type_hints["request_utilization"])
        self._values: typing.Dict[str, typing.Any] = {
            "cpu_utilization": cpu_utilization,
        }
        if cool_down_period is not None:
            self._values["cool_down_period"] = cool_down_period
        if disk_utilization is not None:
            self._values["disk_utilization"] = disk_utilization
        if max_concurrent_requests is not None:
            self._values["max_concurrent_requests"] = max_concurrent_requests
        if max_idle_instances is not None:
            self._values["max_idle_instances"] = max_idle_instances
        if max_pending_latency is not None:
            self._values["max_pending_latency"] = max_pending_latency
        if max_total_instances is not None:
            self._values["max_total_instances"] = max_total_instances
        if min_idle_instances is not None:
            self._values["min_idle_instances"] = min_idle_instances
        if min_pending_latency is not None:
            self._values["min_pending_latency"] = min_pending_latency
        if min_total_instances is not None:
            self._values["min_total_instances"] = min_total_instances
        if network_utilization is not None:
            self._values["network_utilization"] = network_utilization
        if request_utilization is not None:
            self._values["request_utilization"] = request_utilization

    @builtins.property
    def cpu_utilization(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization":
        '''cpu_utilization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cpu_utilization GoogleAppEngineFlexibleAppVersion#cpu_utilization}
        '''
        result = self._values.get("cpu_utilization")
        assert result is not None, "Required property 'cpu_utilization' is missing"
        return typing.cast("GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization", result)

    @builtins.property
    def cool_down_period(self) -> typing.Optional[builtins.str]:
        '''The time period that the Autoscaler should wait before it starts collecting information from a new instance.

        This prevents the autoscaler from collecting information when the instance is initializing,
        during which the collected usage would not be reliable. Default: 120s

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cool_down_period GoogleAppEngineFlexibleAppVersion#cool_down_period}
        '''
        result = self._values.get("cool_down_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_utilization(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization"]:
        '''disk_utilization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disk_utilization GoogleAppEngineFlexibleAppVersion#disk_utilization}
        '''
        result = self._values.get("disk_utilization")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization"], result)

    @builtins.property
    def max_concurrent_requests(self) -> typing.Optional[jsii.Number]:
        '''Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.

        Defaults to a runtime-specific value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_concurrent_requests GoogleAppEngineFlexibleAppVersion#max_concurrent_requests}
        '''
        result = self._values.get("max_concurrent_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_instances(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of idle instances that should be maintained for this version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_idle_instances GoogleAppEngineFlexibleAppVersion#max_idle_instances}
        '''
        result = self._values.get("max_idle_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_pending_latency(self) -> typing.Optional[builtins.str]:
        '''Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_pending_latency GoogleAppEngineFlexibleAppVersion#max_pending_latency}
        '''
        result = self._values.get("max_pending_latency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_total_instances(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of instances that should be started to handle requests for this version. Default: 20.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#max_total_instances GoogleAppEngineFlexibleAppVersion#max_total_instances}
        '''
        result = self._values.get("max_total_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_idle_instances(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of idle instances that should be maintained for this version.

        Only applicable for the default version of a service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_idle_instances GoogleAppEngineFlexibleAppVersion#min_idle_instances}
        '''
        result = self._values.get("min_idle_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_pending_latency(self) -> typing.Optional[builtins.str]:
        '''Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_pending_latency GoogleAppEngineFlexibleAppVersion#min_pending_latency}
        '''
        result = self._values.get("min_pending_latency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_total_instances(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of running instances that should be maintained for this version. Default: 2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#min_total_instances GoogleAppEngineFlexibleAppVersion#min_total_instances}
        '''
        result = self._values.get("min_total_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_utilization(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization"]:
        '''network_utilization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#network_utilization GoogleAppEngineFlexibleAppVersion#network_utilization}
        '''
        result = self._values.get("network_utilization")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization"], result)

    @builtins.property
    def request_utilization(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization"]:
        '''request_utilization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#request_utilization GoogleAppEngineFlexibleAppVersion#request_utilization}
        '''
        result = self._values.get("request_utilization")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionAutomaticScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization",
    jsii_struct_bases=[],
    name_mapping={
        "target_utilization": "targetUtilization",
        "aggregation_window_length": "aggregationWindowLength",
    },
)
class GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization:
    def __init__(
        self,
        *,
        target_utilization: jsii.Number,
        aggregation_window_length: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_utilization: Target CPU utilization ratio to maintain when scaling. Must be between 0 and 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_utilization GoogleAppEngineFlexibleAppVersion#target_utilization}
        :param aggregation_window_length: Period of time over which CPU utilization is calculated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#aggregation_window_length GoogleAppEngineFlexibleAppVersion#aggregation_window_length}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization.__init__)
            check_type(argname="argument target_utilization", value=target_utilization, expected_type=type_hints["target_utilization"])
            check_type(argname="argument aggregation_window_length", value=aggregation_window_length, expected_type=type_hints["aggregation_window_length"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_utilization": target_utilization,
        }
        if aggregation_window_length is not None:
            self._values["aggregation_window_length"] = aggregation_window_length

    @builtins.property
    def target_utilization(self) -> jsii.Number:
        '''Target CPU utilization ratio to maintain when scaling. Must be between 0 and 1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_utilization GoogleAppEngineFlexibleAppVersion#target_utilization}
        '''
        result = self._values.get("target_utilization")
        assert result is not None, "Required property 'target_utilization' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def aggregation_window_length(self) -> typing.Optional[builtins.str]:
        '''Period of time over which CPU utilization is calculated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#aggregation_window_length GoogleAppEngineFlexibleAppVersion#aggregation_window_length}
        '''
        result = self._values.get("aggregation_window_length")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAggregationWindowLength")
    def reset_aggregation_window_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationWindowLength", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationWindowLengthInput")
    def aggregation_window_length_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationWindowLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="targetUtilizationInput")
    def target_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationWindowLength")
    def aggregation_window_length(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationWindowLength"))

    @aggregation_window_length.setter
    def aggregation_window_length(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference, "aggregation_window_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationWindowLength", value)

    @builtins.property
    @jsii.member(jsii_name="targetUtilization")
    def target_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetUtilization"))

    @target_utilization.setter
    def target_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference, "target_utilization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization",
    jsii_struct_bases=[],
    name_mapping={
        "target_read_bytes_per_second": "targetReadBytesPerSecond",
        "target_read_ops_per_second": "targetReadOpsPerSecond",
        "target_write_bytes_per_second": "targetWriteBytesPerSecond",
        "target_write_ops_per_second": "targetWriteOpsPerSecond",
    },
)
class GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization:
    def __init__(
        self,
        *,
        target_read_bytes_per_second: typing.Optional[jsii.Number] = None,
        target_read_ops_per_second: typing.Optional[jsii.Number] = None,
        target_write_bytes_per_second: typing.Optional[jsii.Number] = None,
        target_write_ops_per_second: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_read_bytes_per_second: Target bytes read per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_read_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_read_bytes_per_second}
        :param target_read_ops_per_second: Target ops read per seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_read_ops_per_second GoogleAppEngineFlexibleAppVersion#target_read_ops_per_second}
        :param target_write_bytes_per_second: Target bytes written per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_write_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_write_bytes_per_second}
        :param target_write_ops_per_second: Target ops written per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_write_ops_per_second GoogleAppEngineFlexibleAppVersion#target_write_ops_per_second}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization.__init__)
            check_type(argname="argument target_read_bytes_per_second", value=target_read_bytes_per_second, expected_type=type_hints["target_read_bytes_per_second"])
            check_type(argname="argument target_read_ops_per_second", value=target_read_ops_per_second, expected_type=type_hints["target_read_ops_per_second"])
            check_type(argname="argument target_write_bytes_per_second", value=target_write_bytes_per_second, expected_type=type_hints["target_write_bytes_per_second"])
            check_type(argname="argument target_write_ops_per_second", value=target_write_ops_per_second, expected_type=type_hints["target_write_ops_per_second"])
        self._values: typing.Dict[str, typing.Any] = {}
        if target_read_bytes_per_second is not None:
            self._values["target_read_bytes_per_second"] = target_read_bytes_per_second
        if target_read_ops_per_second is not None:
            self._values["target_read_ops_per_second"] = target_read_ops_per_second
        if target_write_bytes_per_second is not None:
            self._values["target_write_bytes_per_second"] = target_write_bytes_per_second
        if target_write_ops_per_second is not None:
            self._values["target_write_ops_per_second"] = target_write_ops_per_second

    @builtins.property
    def target_read_bytes_per_second(self) -> typing.Optional[jsii.Number]:
        '''Target bytes read per second.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_read_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_read_bytes_per_second}
        '''
        result = self._values.get("target_read_bytes_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_read_ops_per_second(self) -> typing.Optional[jsii.Number]:
        '''Target ops read per seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_read_ops_per_second GoogleAppEngineFlexibleAppVersion#target_read_ops_per_second}
        '''
        result = self._values.get("target_read_ops_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_write_bytes_per_second(self) -> typing.Optional[jsii.Number]:
        '''Target bytes written per second.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_write_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_write_bytes_per_second}
        '''
        result = self._values.get("target_write_bytes_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_write_ops_per_second(self) -> typing.Optional[jsii.Number]:
        '''Target ops written per second.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_write_ops_per_second GoogleAppEngineFlexibleAppVersion#target_write_ops_per_second}
        '''
        result = self._values.get("target_write_ops_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTargetReadBytesPerSecond")
    def reset_target_read_bytes_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetReadBytesPerSecond", []))

    @jsii.member(jsii_name="resetTargetReadOpsPerSecond")
    def reset_target_read_ops_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetReadOpsPerSecond", []))

    @jsii.member(jsii_name="resetTargetWriteBytesPerSecond")
    def reset_target_write_bytes_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetWriteBytesPerSecond", []))

    @jsii.member(jsii_name="resetTargetWriteOpsPerSecond")
    def reset_target_write_ops_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetWriteOpsPerSecond", []))

    @builtins.property
    @jsii.member(jsii_name="targetReadBytesPerSecondInput")
    def target_read_bytes_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetReadBytesPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetReadOpsPerSecondInput")
    def target_read_ops_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetReadOpsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetWriteBytesPerSecondInput")
    def target_write_bytes_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetWriteBytesPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetWriteOpsPerSecondInput")
    def target_write_ops_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetWriteOpsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetReadBytesPerSecond")
    def target_read_bytes_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetReadBytesPerSecond"))

    @target_read_bytes_per_second.setter
    def target_read_bytes_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference, "target_read_bytes_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetReadBytesPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="targetReadOpsPerSecond")
    def target_read_ops_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetReadOpsPerSecond"))

    @target_read_ops_per_second.setter
    def target_read_ops_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference, "target_read_ops_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetReadOpsPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="targetWriteBytesPerSecond")
    def target_write_bytes_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetWriteBytesPerSecond"))

    @target_write_bytes_per_second.setter
    def target_write_bytes_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference, "target_write_bytes_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetWriteBytesPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="targetWriteOpsPerSecond")
    def target_write_ops_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetWriteOpsPerSecond"))

    @target_write_ops_per_second.setter
    def target_write_ops_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference, "target_write_ops_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetWriteOpsPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization",
    jsii_struct_bases=[],
    name_mapping={
        "target_received_bytes_per_second": "targetReceivedBytesPerSecond",
        "target_received_packets_per_second": "targetReceivedPacketsPerSecond",
        "target_sent_bytes_per_second": "targetSentBytesPerSecond",
        "target_sent_packets_per_second": "targetSentPacketsPerSecond",
    },
)
class GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization:
    def __init__(
        self,
        *,
        target_received_bytes_per_second: typing.Optional[jsii.Number] = None,
        target_received_packets_per_second: typing.Optional[jsii.Number] = None,
        target_sent_bytes_per_second: typing.Optional[jsii.Number] = None,
        target_sent_packets_per_second: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_received_bytes_per_second: Target bytes received per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_received_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_received_bytes_per_second}
        :param target_received_packets_per_second: Target packets received per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_received_packets_per_second GoogleAppEngineFlexibleAppVersion#target_received_packets_per_second}
        :param target_sent_bytes_per_second: Target bytes sent per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_sent_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_sent_bytes_per_second}
        :param target_sent_packets_per_second: Target packets sent per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_sent_packets_per_second GoogleAppEngineFlexibleAppVersion#target_sent_packets_per_second}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization.__init__)
            check_type(argname="argument target_received_bytes_per_second", value=target_received_bytes_per_second, expected_type=type_hints["target_received_bytes_per_second"])
            check_type(argname="argument target_received_packets_per_second", value=target_received_packets_per_second, expected_type=type_hints["target_received_packets_per_second"])
            check_type(argname="argument target_sent_bytes_per_second", value=target_sent_bytes_per_second, expected_type=type_hints["target_sent_bytes_per_second"])
            check_type(argname="argument target_sent_packets_per_second", value=target_sent_packets_per_second, expected_type=type_hints["target_sent_packets_per_second"])
        self._values: typing.Dict[str, typing.Any] = {}
        if target_received_bytes_per_second is not None:
            self._values["target_received_bytes_per_second"] = target_received_bytes_per_second
        if target_received_packets_per_second is not None:
            self._values["target_received_packets_per_second"] = target_received_packets_per_second
        if target_sent_bytes_per_second is not None:
            self._values["target_sent_bytes_per_second"] = target_sent_bytes_per_second
        if target_sent_packets_per_second is not None:
            self._values["target_sent_packets_per_second"] = target_sent_packets_per_second

    @builtins.property
    def target_received_bytes_per_second(self) -> typing.Optional[jsii.Number]:
        '''Target bytes received per second.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_received_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_received_bytes_per_second}
        '''
        result = self._values.get("target_received_bytes_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_received_packets_per_second(self) -> typing.Optional[jsii.Number]:
        '''Target packets received per second.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_received_packets_per_second GoogleAppEngineFlexibleAppVersion#target_received_packets_per_second}
        '''
        result = self._values.get("target_received_packets_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_sent_bytes_per_second(self) -> typing.Optional[jsii.Number]:
        '''Target bytes sent per second.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_sent_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_sent_bytes_per_second}
        '''
        result = self._values.get("target_sent_bytes_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_sent_packets_per_second(self) -> typing.Optional[jsii.Number]:
        '''Target packets sent per second.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_sent_packets_per_second GoogleAppEngineFlexibleAppVersion#target_sent_packets_per_second}
        '''
        result = self._values.get("target_sent_packets_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTargetReceivedBytesPerSecond")
    def reset_target_received_bytes_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetReceivedBytesPerSecond", []))

    @jsii.member(jsii_name="resetTargetReceivedPacketsPerSecond")
    def reset_target_received_packets_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetReceivedPacketsPerSecond", []))

    @jsii.member(jsii_name="resetTargetSentBytesPerSecond")
    def reset_target_sent_bytes_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSentBytesPerSecond", []))

    @jsii.member(jsii_name="resetTargetSentPacketsPerSecond")
    def reset_target_sent_packets_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSentPacketsPerSecond", []))

    @builtins.property
    @jsii.member(jsii_name="targetReceivedBytesPerSecondInput")
    def target_received_bytes_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetReceivedBytesPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetReceivedPacketsPerSecondInput")
    def target_received_packets_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetReceivedPacketsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSentBytesPerSecondInput")
    def target_sent_bytes_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetSentBytesPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSentPacketsPerSecondInput")
    def target_sent_packets_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetSentPacketsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetReceivedBytesPerSecond")
    def target_received_bytes_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetReceivedBytesPerSecond"))

    @target_received_bytes_per_second.setter
    def target_received_bytes_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference, "target_received_bytes_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetReceivedBytesPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="targetReceivedPacketsPerSecond")
    def target_received_packets_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetReceivedPacketsPerSecond"))

    @target_received_packets_per_second.setter
    def target_received_packets_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference, "target_received_packets_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetReceivedPacketsPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="targetSentBytesPerSecond")
    def target_sent_bytes_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetSentBytesPerSecond"))

    @target_sent_bytes_per_second.setter
    def target_sent_bytes_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference, "target_sent_bytes_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSentBytesPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="targetSentPacketsPerSecond")
    def target_sent_packets_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetSentPacketsPerSecond"))

    @target_sent_packets_per_second.setter
    def target_sent_packets_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference, "target_sent_packets_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSentPacketsPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCpuUtilization")
    def put_cpu_utilization(
        self,
        *,
        target_utilization: jsii.Number,
        aggregation_window_length: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_utilization: Target CPU utilization ratio to maintain when scaling. Must be between 0 and 1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_utilization GoogleAppEngineFlexibleAppVersion#target_utilization}
        :param aggregation_window_length: Period of time over which CPU utilization is calculated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#aggregation_window_length GoogleAppEngineFlexibleAppVersion#aggregation_window_length}
        '''
        value = GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization(
            target_utilization=target_utilization,
            aggregation_window_length=aggregation_window_length,
        )

        return typing.cast(None, jsii.invoke(self, "putCpuUtilization", [value]))

    @jsii.member(jsii_name="putDiskUtilization")
    def put_disk_utilization(
        self,
        *,
        target_read_bytes_per_second: typing.Optional[jsii.Number] = None,
        target_read_ops_per_second: typing.Optional[jsii.Number] = None,
        target_write_bytes_per_second: typing.Optional[jsii.Number] = None,
        target_write_ops_per_second: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_read_bytes_per_second: Target bytes read per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_read_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_read_bytes_per_second}
        :param target_read_ops_per_second: Target ops read per seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_read_ops_per_second GoogleAppEngineFlexibleAppVersion#target_read_ops_per_second}
        :param target_write_bytes_per_second: Target bytes written per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_write_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_write_bytes_per_second}
        :param target_write_ops_per_second: Target ops written per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_write_ops_per_second GoogleAppEngineFlexibleAppVersion#target_write_ops_per_second}
        '''
        value = GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization(
            target_read_bytes_per_second=target_read_bytes_per_second,
            target_read_ops_per_second=target_read_ops_per_second,
            target_write_bytes_per_second=target_write_bytes_per_second,
            target_write_ops_per_second=target_write_ops_per_second,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskUtilization", [value]))

    @jsii.member(jsii_name="putNetworkUtilization")
    def put_network_utilization(
        self,
        *,
        target_received_bytes_per_second: typing.Optional[jsii.Number] = None,
        target_received_packets_per_second: typing.Optional[jsii.Number] = None,
        target_sent_bytes_per_second: typing.Optional[jsii.Number] = None,
        target_sent_packets_per_second: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_received_bytes_per_second: Target bytes received per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_received_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_received_bytes_per_second}
        :param target_received_packets_per_second: Target packets received per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_received_packets_per_second GoogleAppEngineFlexibleAppVersion#target_received_packets_per_second}
        :param target_sent_bytes_per_second: Target bytes sent per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_sent_bytes_per_second GoogleAppEngineFlexibleAppVersion#target_sent_bytes_per_second}
        :param target_sent_packets_per_second: Target packets sent per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_sent_packets_per_second GoogleAppEngineFlexibleAppVersion#target_sent_packets_per_second}
        '''
        value = GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization(
            target_received_bytes_per_second=target_received_bytes_per_second,
            target_received_packets_per_second=target_received_packets_per_second,
            target_sent_bytes_per_second=target_sent_bytes_per_second,
            target_sent_packets_per_second=target_sent_packets_per_second,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkUtilization", [value]))

    @jsii.member(jsii_name="putRequestUtilization")
    def put_request_utilization(
        self,
        *,
        target_concurrent_requests: typing.Optional[jsii.Number] = None,
        target_request_count_per_second: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_concurrent_requests: Target number of concurrent requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_concurrent_requests GoogleAppEngineFlexibleAppVersion#target_concurrent_requests}
        :param target_request_count_per_second: Target requests per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_request_count_per_second GoogleAppEngineFlexibleAppVersion#target_request_count_per_second}
        '''
        value = GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization(
            target_concurrent_requests=target_concurrent_requests,
            target_request_count_per_second=target_request_count_per_second,
        )

        return typing.cast(None, jsii.invoke(self, "putRequestUtilization", [value]))

    @jsii.member(jsii_name="resetCoolDownPeriod")
    def reset_cool_down_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoolDownPeriod", []))

    @jsii.member(jsii_name="resetDiskUtilization")
    def reset_disk_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskUtilization", []))

    @jsii.member(jsii_name="resetMaxConcurrentRequests")
    def reset_max_concurrent_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentRequests", []))

    @jsii.member(jsii_name="resetMaxIdleInstances")
    def reset_max_idle_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleInstances", []))

    @jsii.member(jsii_name="resetMaxPendingLatency")
    def reset_max_pending_latency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPendingLatency", []))

    @jsii.member(jsii_name="resetMaxTotalInstances")
    def reset_max_total_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTotalInstances", []))

    @jsii.member(jsii_name="resetMinIdleInstances")
    def reset_min_idle_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinIdleInstances", []))

    @jsii.member(jsii_name="resetMinPendingLatency")
    def reset_min_pending_latency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinPendingLatency", []))

    @jsii.member(jsii_name="resetMinTotalInstances")
    def reset_min_total_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTotalInstances", []))

    @jsii.member(jsii_name="resetNetworkUtilization")
    def reset_network_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkUtilization", []))

    @jsii.member(jsii_name="resetRequestUtilization")
    def reset_request_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestUtilization", []))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilization")
    def cpu_utilization(
        self,
    ) -> GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference:
        return typing.cast(GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference, jsii.get(self, "cpuUtilization"))

    @builtins.property
    @jsii.member(jsii_name="diskUtilization")
    def disk_utilization(
        self,
    ) -> GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference:
        return typing.cast(GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference, jsii.get(self, "diskUtilization"))

    @builtins.property
    @jsii.member(jsii_name="networkUtilization")
    def network_utilization(
        self,
    ) -> GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference:
        return typing.cast(GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference, jsii.get(self, "networkUtilization"))

    @builtins.property
    @jsii.member(jsii_name="requestUtilization")
    def request_utilization(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference", jsii.get(self, "requestUtilization"))

    @builtins.property
    @jsii.member(jsii_name="coolDownPeriodInput")
    def cool_down_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coolDownPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationInput")
    def cpu_utilization_input(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization], jsii.get(self, "cpuUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="diskUtilizationInput")
    def disk_utilization_input(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization], jsii.get(self, "diskUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentRequestsInput")
    def max_concurrent_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleInstancesInput")
    def max_idle_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPendingLatencyInput")
    def max_pending_latency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxPendingLatencyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTotalInstancesInput")
    def max_total_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTotalInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="minIdleInstancesInput")
    def min_idle_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minIdleInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="minPendingLatencyInput")
    def min_pending_latency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minPendingLatencyInput"))

    @builtins.property
    @jsii.member(jsii_name="minTotalInstancesInput")
    def min_total_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minTotalInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="networkUtilizationInput")
    def network_utilization_input(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization], jsii.get(self, "networkUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="requestUtilizationInput")
    def request_utilization_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization"], jsii.get(self, "requestUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="coolDownPeriod")
    def cool_down_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coolDownPeriod"))

    @cool_down_period.setter
    def cool_down_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "cool_down_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coolDownPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentRequests")
    def max_concurrent_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentRequests"))

    @max_concurrent_requests.setter
    def max_concurrent_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "max_concurrent_requests").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentRequests", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleInstances")
    def max_idle_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleInstances"))

    @max_idle_instances.setter
    def max_idle_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "max_idle_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleInstances", value)

    @builtins.property
    @jsii.member(jsii_name="maxPendingLatency")
    def max_pending_latency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxPendingLatency"))

    @max_pending_latency.setter
    def max_pending_latency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "max_pending_latency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPendingLatency", value)

    @builtins.property
    @jsii.member(jsii_name="maxTotalInstances")
    def max_total_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTotalInstances"))

    @max_total_instances.setter
    def max_total_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "max_total_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTotalInstances", value)

    @builtins.property
    @jsii.member(jsii_name="minIdleInstances")
    def min_idle_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minIdleInstances"))

    @min_idle_instances.setter
    def min_idle_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "min_idle_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minIdleInstances", value)

    @builtins.property
    @jsii.member(jsii_name="minPendingLatency")
    def min_pending_latency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minPendingLatency"))

    @min_pending_latency.setter
    def min_pending_latency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "min_pending_latency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minPendingLatency", value)

    @builtins.property
    @jsii.member(jsii_name="minTotalInstances")
    def min_total_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minTotalInstances"))

    @min_total_instances.setter
    def min_total_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "min_total_instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTotalInstances", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScaling]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization",
    jsii_struct_bases=[],
    name_mapping={
        "target_concurrent_requests": "targetConcurrentRequests",
        "target_request_count_per_second": "targetRequestCountPerSecond",
    },
)
class GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization:
    def __init__(
        self,
        *,
        target_concurrent_requests: typing.Optional[jsii.Number] = None,
        target_request_count_per_second: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_concurrent_requests: Target number of concurrent requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_concurrent_requests GoogleAppEngineFlexibleAppVersion#target_concurrent_requests}
        :param target_request_count_per_second: Target requests per second. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_request_count_per_second GoogleAppEngineFlexibleAppVersion#target_request_count_per_second}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization.__init__)
            check_type(argname="argument target_concurrent_requests", value=target_concurrent_requests, expected_type=type_hints["target_concurrent_requests"])
            check_type(argname="argument target_request_count_per_second", value=target_request_count_per_second, expected_type=type_hints["target_request_count_per_second"])
        self._values: typing.Dict[str, typing.Any] = {}
        if target_concurrent_requests is not None:
            self._values["target_concurrent_requests"] = target_concurrent_requests
        if target_request_count_per_second is not None:
            self._values["target_request_count_per_second"] = target_request_count_per_second

    @builtins.property
    def target_concurrent_requests(self) -> typing.Optional[jsii.Number]:
        '''Target number of concurrent requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_concurrent_requests GoogleAppEngineFlexibleAppVersion#target_concurrent_requests}
        '''
        result = self._values.get("target_concurrent_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_request_count_per_second(self) -> typing.Optional[builtins.str]:
        '''Target requests per second.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#target_request_count_per_second GoogleAppEngineFlexibleAppVersion#target_request_count_per_second}
        '''
        result = self._values.get("target_request_count_per_second")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTargetConcurrentRequests")
    def reset_target_concurrent_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetConcurrentRequests", []))

    @jsii.member(jsii_name="resetTargetRequestCountPerSecond")
    def reset_target_request_count_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetRequestCountPerSecond", []))

    @builtins.property
    @jsii.member(jsii_name="targetConcurrentRequestsInput")
    def target_concurrent_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetConcurrentRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetRequestCountPerSecondInput")
    def target_request_count_per_second_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetRequestCountPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="targetConcurrentRequests")
    def target_concurrent_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetConcurrentRequests"))

    @target_concurrent_requests.setter
    def target_concurrent_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference, "target_concurrent_requests").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetConcurrentRequests", value)

    @builtins.property
    @jsii.member(jsii_name="targetRequestCountPerSecond")
    def target_request_count_per_second(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetRequestCountPerSecond"))

    @target_request_count_per_second.setter
    def target_request_count_per_second(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference, "target_request_count_per_second").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetRequestCountPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "liveness_check": "livenessCheck",
        "readiness_check": "readinessCheck",
        "runtime": "runtime",
        "service": "service",
        "api_config": "apiConfig",
        "automatic_scaling": "automaticScaling",
        "beta_settings": "betaSettings",
        "default_expiration": "defaultExpiration",
        "delete_service_on_destroy": "deleteServiceOnDestroy",
        "deployment": "deployment",
        "endpoints_api_service": "endpointsApiService",
        "entrypoint": "entrypoint",
        "env_variables": "envVariables",
        "handlers": "handlers",
        "id": "id",
        "inbound_services": "inboundServices",
        "instance_class": "instanceClass",
        "manual_scaling": "manualScaling",
        "network": "network",
        "nobuild_files_regex": "nobuildFilesRegex",
        "noop_on_destroy": "noopOnDestroy",
        "project": "project",
        "resources": "resources",
        "runtime_api_version": "runtimeApiVersion",
        "runtime_channel": "runtimeChannel",
        "runtime_main_executable_path": "runtimeMainExecutablePath",
        "service_account": "serviceAccount",
        "serving_status": "servingStatus",
        "timeouts": "timeouts",
        "version_id": "versionId",
        "vpc_access_connector": "vpcAccessConnector",
    },
)
class GoogleAppEngineFlexibleAppVersionConfig(cdktf.TerraformMetaArguments):
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
        liveness_check: typing.Union["GoogleAppEngineFlexibleAppVersionLivenessCheck", typing.Dict[str, typing.Any]],
        readiness_check: typing.Union["GoogleAppEngineFlexibleAppVersionReadinessCheck", typing.Dict[str, typing.Any]],
        runtime: builtins.str,
        service: builtins.str,
        api_config: typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionApiConfig, typing.Dict[str, typing.Any]]] = None,
        automatic_scaling: typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionAutomaticScaling, typing.Dict[str, typing.Any]]] = None,
        beta_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_expiration: typing.Optional[builtins.str] = None,
        delete_service_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        deployment: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionDeployment", typing.Dict[str, typing.Any]]] = None,
        endpoints_api_service: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionEndpointsApiService", typing.Dict[str, typing.Any]]] = None,
        entrypoint: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionEntrypoint", typing.Dict[str, typing.Any]]] = None,
        env_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        handlers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAppEngineFlexibleAppVersionHandlers", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        inbound_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_class: typing.Optional[builtins.str] = None,
        manual_scaling: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionManualScaling", typing.Dict[str, typing.Any]]] = None,
        network: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionNetwork", typing.Dict[str, typing.Any]]] = None,
        nobuild_files_regex: typing.Optional[builtins.str] = None,
        noop_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project: typing.Optional[builtins.str] = None,
        resources: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionResources", typing.Dict[str, typing.Any]]] = None,
        runtime_api_version: typing.Optional[builtins.str] = None,
        runtime_channel: typing.Optional[builtins.str] = None,
        runtime_main_executable_path: typing.Optional[builtins.str] = None,
        service_account: typing.Optional[builtins.str] = None,
        serving_status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionTimeouts", typing.Dict[str, typing.Any]]] = None,
        version_id: typing.Optional[builtins.str] = None,
        vpc_access_connector: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionVpcAccessConnector", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param liveness_check: liveness_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#liveness_check GoogleAppEngineFlexibleAppVersion#liveness_check}
        :param readiness_check: readiness_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#readiness_check GoogleAppEngineFlexibleAppVersion#readiness_check}
        :param runtime: Desired runtime. Example python27. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime GoogleAppEngineFlexibleAppVersion#runtime}
        :param service: AppEngine service resource. Can contain numbers, letters, and hyphens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#service GoogleAppEngineFlexibleAppVersion#service}
        :param api_config: api_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#api_config GoogleAppEngineFlexibleAppVersion#api_config}
        :param automatic_scaling: automatic_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#automatic_scaling GoogleAppEngineFlexibleAppVersion#automatic_scaling}
        :param beta_settings: Metadata settings that are supplied to this version to enable beta runtime features. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#beta_settings GoogleAppEngineFlexibleAppVersion#beta_settings}
        :param default_expiration: Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#default_expiration GoogleAppEngineFlexibleAppVersion#default_expiration}
        :param delete_service_on_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#delete_service_on_destroy GoogleAppEngineFlexibleAppVersion#delete_service_on_destroy}.
        :param deployment: deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#deployment GoogleAppEngineFlexibleAppVersion#deployment}
        :param endpoints_api_service: endpoints_api_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#endpoints_api_service GoogleAppEngineFlexibleAppVersion#endpoints_api_service}
        :param entrypoint: entrypoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#entrypoint GoogleAppEngineFlexibleAppVersion#entrypoint}
        :param env_variables: Environment variables available to the application. As these are not returned in the API request, Terraform will not detect any changes made outside of the Terraform config. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#env_variables GoogleAppEngineFlexibleAppVersion#env_variables}
        :param handlers: handlers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#handlers GoogleAppEngineFlexibleAppVersion#handlers}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#id GoogleAppEngineFlexibleAppVersion#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inbound_services: A list of the types of messages that this application is able to receive. Possible values: ["INBOUND_SERVICE_MAIL", "INBOUND_SERVICE_MAIL_BOUNCE", "INBOUND_SERVICE_XMPP_ERROR", "INBOUND_SERVICE_XMPP_MESSAGE", "INBOUND_SERVICE_XMPP_SUBSCRIBE", "INBOUND_SERVICE_XMPP_PRESENCE", "INBOUND_SERVICE_CHANNEL_PRESENCE", "INBOUND_SERVICE_WARMUP"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#inbound_services GoogleAppEngineFlexibleAppVersion#inbound_services}
        :param instance_class: Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1, B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instance_class GoogleAppEngineFlexibleAppVersion#instance_class}
        :param manual_scaling: manual_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#manual_scaling GoogleAppEngineFlexibleAppVersion#manual_scaling}
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#network GoogleAppEngineFlexibleAppVersion#network}
        :param nobuild_files_regex: Files that match this pattern will not be built into this version. Only applicable for Go runtimes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#nobuild_files_regex GoogleAppEngineFlexibleAppVersion#nobuild_files_regex}
        :param noop_on_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#noop_on_destroy GoogleAppEngineFlexibleAppVersion#noop_on_destroy}.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#project GoogleAppEngineFlexibleAppVersion#project}.
        :param resources: resources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#resources GoogleAppEngineFlexibleAppVersion#resources}
        :param runtime_api_version: The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at 'https://cloud.google.com/appengine/docs/standard//config/appref' Substitute '' with 'python', 'java', 'php', 'ruby', 'go' or 'nodejs'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_api_version GoogleAppEngineFlexibleAppVersion#runtime_api_version}
        :param runtime_channel: The channel of the runtime to use. Only available for some runtimes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_channel GoogleAppEngineFlexibleAppVersion#runtime_channel}
        :param runtime_main_executable_path: The path or name of the app's main executable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_main_executable_path GoogleAppEngineFlexibleAppVersion#runtime_main_executable_path}
        :param service_account: The identity that the deployed version will run as. Admin API will use the App Engine Appspot service account as default if this field is neither provided in app.yaml file nor through CLI flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#service_account GoogleAppEngineFlexibleAppVersion#service_account}
        :param serving_status: Current serving status of this version. Only the versions with a SERVING status create instances and can be billed. Default value: "SERVING" Possible values: ["SERVING", "STOPPED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#serving_status GoogleAppEngineFlexibleAppVersion#serving_status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeouts GoogleAppEngineFlexibleAppVersion#timeouts}
        :param version_id: Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#version_id GoogleAppEngineFlexibleAppVersion#version_id}
        :param vpc_access_connector: vpc_access_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#vpc_access_connector GoogleAppEngineFlexibleAppVersion#vpc_access_connector}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(liveness_check, dict):
            liveness_check = GoogleAppEngineFlexibleAppVersionLivenessCheck(**liveness_check)
        if isinstance(readiness_check, dict):
            readiness_check = GoogleAppEngineFlexibleAppVersionReadinessCheck(**readiness_check)
        if isinstance(api_config, dict):
            api_config = GoogleAppEngineFlexibleAppVersionApiConfig(**api_config)
        if isinstance(automatic_scaling, dict):
            automatic_scaling = GoogleAppEngineFlexibleAppVersionAutomaticScaling(**automatic_scaling)
        if isinstance(deployment, dict):
            deployment = GoogleAppEngineFlexibleAppVersionDeployment(**deployment)
        if isinstance(endpoints_api_service, dict):
            endpoints_api_service = GoogleAppEngineFlexibleAppVersionEndpointsApiService(**endpoints_api_service)
        if isinstance(entrypoint, dict):
            entrypoint = GoogleAppEngineFlexibleAppVersionEntrypoint(**entrypoint)
        if isinstance(manual_scaling, dict):
            manual_scaling = GoogleAppEngineFlexibleAppVersionManualScaling(**manual_scaling)
        if isinstance(network, dict):
            network = GoogleAppEngineFlexibleAppVersionNetwork(**network)
        if isinstance(resources, dict):
            resources = GoogleAppEngineFlexibleAppVersionResources(**resources)
        if isinstance(timeouts, dict):
            timeouts = GoogleAppEngineFlexibleAppVersionTimeouts(**timeouts)
        if isinstance(vpc_access_connector, dict):
            vpc_access_connector = GoogleAppEngineFlexibleAppVersionVpcAccessConnector(**vpc_access_connector)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument liveness_check", value=liveness_check, expected_type=type_hints["liveness_check"])
            check_type(argname="argument readiness_check", value=readiness_check, expected_type=type_hints["readiness_check"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument api_config", value=api_config, expected_type=type_hints["api_config"])
            check_type(argname="argument automatic_scaling", value=automatic_scaling, expected_type=type_hints["automatic_scaling"])
            check_type(argname="argument beta_settings", value=beta_settings, expected_type=type_hints["beta_settings"])
            check_type(argname="argument default_expiration", value=default_expiration, expected_type=type_hints["default_expiration"])
            check_type(argname="argument delete_service_on_destroy", value=delete_service_on_destroy, expected_type=type_hints["delete_service_on_destroy"])
            check_type(argname="argument deployment", value=deployment, expected_type=type_hints["deployment"])
            check_type(argname="argument endpoints_api_service", value=endpoints_api_service, expected_type=type_hints["endpoints_api_service"])
            check_type(argname="argument entrypoint", value=entrypoint, expected_type=type_hints["entrypoint"])
            check_type(argname="argument env_variables", value=env_variables, expected_type=type_hints["env_variables"])
            check_type(argname="argument handlers", value=handlers, expected_type=type_hints["handlers"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inbound_services", value=inbound_services, expected_type=type_hints["inbound_services"])
            check_type(argname="argument instance_class", value=instance_class, expected_type=type_hints["instance_class"])
            check_type(argname="argument manual_scaling", value=manual_scaling, expected_type=type_hints["manual_scaling"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument nobuild_files_regex", value=nobuild_files_regex, expected_type=type_hints["nobuild_files_regex"])
            check_type(argname="argument noop_on_destroy", value=noop_on_destroy, expected_type=type_hints["noop_on_destroy"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument runtime_api_version", value=runtime_api_version, expected_type=type_hints["runtime_api_version"])
            check_type(argname="argument runtime_channel", value=runtime_channel, expected_type=type_hints["runtime_channel"])
            check_type(argname="argument runtime_main_executable_path", value=runtime_main_executable_path, expected_type=type_hints["runtime_main_executable_path"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument serving_status", value=serving_status, expected_type=type_hints["serving_status"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
            check_type(argname="argument vpc_access_connector", value=vpc_access_connector, expected_type=type_hints["vpc_access_connector"])
        self._values: typing.Dict[str, typing.Any] = {
            "liveness_check": liveness_check,
            "readiness_check": readiness_check,
            "runtime": runtime,
            "service": service,
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
        if api_config is not None:
            self._values["api_config"] = api_config
        if automatic_scaling is not None:
            self._values["automatic_scaling"] = automatic_scaling
        if beta_settings is not None:
            self._values["beta_settings"] = beta_settings
        if default_expiration is not None:
            self._values["default_expiration"] = default_expiration
        if delete_service_on_destroy is not None:
            self._values["delete_service_on_destroy"] = delete_service_on_destroy
        if deployment is not None:
            self._values["deployment"] = deployment
        if endpoints_api_service is not None:
            self._values["endpoints_api_service"] = endpoints_api_service
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if env_variables is not None:
            self._values["env_variables"] = env_variables
        if handlers is not None:
            self._values["handlers"] = handlers
        if id is not None:
            self._values["id"] = id
        if inbound_services is not None:
            self._values["inbound_services"] = inbound_services
        if instance_class is not None:
            self._values["instance_class"] = instance_class
        if manual_scaling is not None:
            self._values["manual_scaling"] = manual_scaling
        if network is not None:
            self._values["network"] = network
        if nobuild_files_regex is not None:
            self._values["nobuild_files_regex"] = nobuild_files_regex
        if noop_on_destroy is not None:
            self._values["noop_on_destroy"] = noop_on_destroy
        if project is not None:
            self._values["project"] = project
        if resources is not None:
            self._values["resources"] = resources
        if runtime_api_version is not None:
            self._values["runtime_api_version"] = runtime_api_version
        if runtime_channel is not None:
            self._values["runtime_channel"] = runtime_channel
        if runtime_main_executable_path is not None:
            self._values["runtime_main_executable_path"] = runtime_main_executable_path
        if service_account is not None:
            self._values["service_account"] = service_account
        if serving_status is not None:
            self._values["serving_status"] = serving_status
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version_id is not None:
            self._values["version_id"] = version_id
        if vpc_access_connector is not None:
            self._values["vpc_access_connector"] = vpc_access_connector

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
    def liveness_check(self) -> "GoogleAppEngineFlexibleAppVersionLivenessCheck":
        '''liveness_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#liveness_check GoogleAppEngineFlexibleAppVersion#liveness_check}
        '''
        result = self._values.get("liveness_check")
        assert result is not None, "Required property 'liveness_check' is missing"
        return typing.cast("GoogleAppEngineFlexibleAppVersionLivenessCheck", result)

    @builtins.property
    def readiness_check(self) -> "GoogleAppEngineFlexibleAppVersionReadinessCheck":
        '''readiness_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#readiness_check GoogleAppEngineFlexibleAppVersion#readiness_check}
        '''
        result = self._values.get("readiness_check")
        assert result is not None, "Required property 'readiness_check' is missing"
        return typing.cast("GoogleAppEngineFlexibleAppVersionReadinessCheck", result)

    @builtins.property
    def runtime(self) -> builtins.str:
        '''Desired runtime. Example python27.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime GoogleAppEngineFlexibleAppVersion#runtime}
        '''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''AppEngine service resource. Can contain numbers, letters, and hyphens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#service GoogleAppEngineFlexibleAppVersion#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_config(self) -> typing.Optional[GoogleAppEngineFlexibleAppVersionApiConfig]:
        '''api_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#api_config GoogleAppEngineFlexibleAppVersion#api_config}
        '''
        result = self._values.get("api_config")
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionApiConfig], result)

    @builtins.property
    def automatic_scaling(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScaling]:
        '''automatic_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#automatic_scaling GoogleAppEngineFlexibleAppVersion#automatic_scaling}
        '''
        result = self._values.get("automatic_scaling")
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionAutomaticScaling], result)

    @builtins.property
    def beta_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata settings that are supplied to this version to enable beta runtime features.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#beta_settings GoogleAppEngineFlexibleAppVersion#beta_settings}
        '''
        result = self._values.get("beta_settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def default_expiration(self) -> typing.Optional[builtins.str]:
        '''Duration that static files should be cached by web proxies and browsers.

        Only applicable if the corresponding StaticFilesHandler does not specify its own expiration time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#default_expiration GoogleAppEngineFlexibleAppVersion#default_expiration}
        '''
        result = self._values.get("default_expiration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_service_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#delete_service_on_destroy GoogleAppEngineFlexibleAppVersion#delete_service_on_destroy}.'''
        result = self._values.get("delete_service_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def deployment(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionDeployment"]:
        '''deployment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#deployment GoogleAppEngineFlexibleAppVersion#deployment}
        '''
        result = self._values.get("deployment")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionDeployment"], result)

    @builtins.property
    def endpoints_api_service(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionEndpointsApiService"]:
        '''endpoints_api_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#endpoints_api_service GoogleAppEngineFlexibleAppVersion#endpoints_api_service}
        '''
        result = self._values.get("endpoints_api_service")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionEndpointsApiService"], result)

    @builtins.property
    def entrypoint(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionEntrypoint"]:
        '''entrypoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#entrypoint GoogleAppEngineFlexibleAppVersion#entrypoint}
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionEntrypoint"], result)

    @builtins.property
    def env_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Environment variables available to the application.

        As these are not returned in the API request, Terraform will not detect any changes made outside of the Terraform config.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#env_variables GoogleAppEngineFlexibleAppVersion#env_variables}
        '''
        result = self._values.get("env_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def handlers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionHandlers"]]]:
        '''handlers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#handlers GoogleAppEngineFlexibleAppVersion#handlers}
        '''
        result = self._values.get("handlers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionHandlers"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#id GoogleAppEngineFlexibleAppVersion#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inbound_services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the types of messages that this application is able to receive.

        Possible values: ["INBOUND_SERVICE_MAIL", "INBOUND_SERVICE_MAIL_BOUNCE", "INBOUND_SERVICE_XMPP_ERROR", "INBOUND_SERVICE_XMPP_MESSAGE", "INBOUND_SERVICE_XMPP_SUBSCRIBE", "INBOUND_SERVICE_XMPP_PRESENCE", "INBOUND_SERVICE_CHANNEL_PRESENCE", "INBOUND_SERVICE_WARMUP"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#inbound_services GoogleAppEngineFlexibleAppVersion#inbound_services}
        '''
        result = self._values.get("inbound_services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def instance_class(self) -> typing.Optional[builtins.str]:
        '''Instance class that is used to run this version.

        Valid values are
        AutomaticScaling: F1, F2, F4, F4_1G
        ManualScaling: B1, B2, B4, B8, B4_1G
        Defaults to F1 for AutomaticScaling and B1 for ManualScaling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instance_class GoogleAppEngineFlexibleAppVersion#instance_class}
        '''
        result = self._values.get("instance_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manual_scaling(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionManualScaling"]:
        '''manual_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#manual_scaling GoogleAppEngineFlexibleAppVersion#manual_scaling}
        '''
        result = self._values.get("manual_scaling")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionManualScaling"], result)

    @builtins.property
    def network(self) -> typing.Optional["GoogleAppEngineFlexibleAppVersionNetwork"]:
        '''network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#network GoogleAppEngineFlexibleAppVersion#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionNetwork"], result)

    @builtins.property
    def nobuild_files_regex(self) -> typing.Optional[builtins.str]:
        '''Files that match this pattern will not be built into this version. Only applicable for Go runtimes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#nobuild_files_regex GoogleAppEngineFlexibleAppVersion#nobuild_files_regex}
        '''
        result = self._values.get("nobuild_files_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def noop_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#noop_on_destroy GoogleAppEngineFlexibleAppVersion#noop_on_destroy}.'''
        result = self._values.get("noop_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#project GoogleAppEngineFlexibleAppVersion#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resources(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionResources"]:
        '''resources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#resources GoogleAppEngineFlexibleAppVersion#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionResources"], result)

    @builtins.property
    def runtime_api_version(self) -> typing.Optional[builtins.str]:
        '''The version of the API in the given runtime environment.

        Please see the app.yaml reference for valid values at 'https://cloud.google.com/appengine/docs/standard//config/appref'
        Substitute '' with 'python', 'java', 'php', 'ruby', 'go' or 'nodejs'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_api_version GoogleAppEngineFlexibleAppVersion#runtime_api_version}
        '''
        result = self._values.get("runtime_api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_channel(self) -> typing.Optional[builtins.str]:
        '''The channel of the runtime to use. Only available for some runtimes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_channel GoogleAppEngineFlexibleAppVersion#runtime_channel}
        '''
        result = self._values.get("runtime_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_main_executable_path(self) -> typing.Optional[builtins.str]:
        '''The path or name of the app's main executable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#runtime_main_executable_path GoogleAppEngineFlexibleAppVersion#runtime_main_executable_path}
        '''
        result = self._values.get("runtime_main_executable_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The identity that the deployed version will run as.

        Admin API will use the App Engine Appspot service account as
        default if this field is neither provided in app.yaml file nor through CLI flag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#service_account GoogleAppEngineFlexibleAppVersion#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serving_status(self) -> typing.Optional[builtins.str]:
        '''Current serving status of this version.

        Only the versions with a SERVING status create instances and can be billed. Default value: "SERVING" Possible values: ["SERVING", "STOPPED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#serving_status GoogleAppEngineFlexibleAppVersion#serving_status}
        '''
        result = self._values.get("serving_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleAppEngineFlexibleAppVersionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeouts GoogleAppEngineFlexibleAppVersion#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionTimeouts"], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''Relative name of the version within the service.

        For example, 'v1'. Version names can contain only lowercase letters, numbers, or hyphens.
        Reserved names,"default", "latest", and any name with the prefix "ah-".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#version_id GoogleAppEngineFlexibleAppVersion#version_id}
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_access_connector(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionVpcAccessConnector"]:
        '''vpc_access_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#vpc_access_connector GoogleAppEngineFlexibleAppVersion#vpc_access_connector}
        '''
        result = self._values.get("vpc_access_connector")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionVpcAccessConnector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeployment",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_build_options": "cloudBuildOptions",
        "container": "container",
        "files": "files",
        "zip": "zip",
    },
)
class GoogleAppEngineFlexibleAppVersionDeployment:
    def __init__(
        self,
        *,
        cloud_build_options: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions", typing.Dict[str, typing.Any]]] = None,
        container: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionDeploymentContainer", typing.Dict[str, typing.Any]]] = None,
        files: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAppEngineFlexibleAppVersionDeploymentFiles", typing.Dict[str, typing.Any]]]]] = None,
        zip: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionDeploymentZip", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_build_options: cloud_build_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cloud_build_options GoogleAppEngineFlexibleAppVersion#cloud_build_options}
        :param container: container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#container GoogleAppEngineFlexibleAppVersion#container}
        :param files: files block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#files GoogleAppEngineFlexibleAppVersion#files}
        :param zip: zip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#zip GoogleAppEngineFlexibleAppVersion#zip}
        '''
        if isinstance(cloud_build_options, dict):
            cloud_build_options = GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions(**cloud_build_options)
        if isinstance(container, dict):
            container = GoogleAppEngineFlexibleAppVersionDeploymentContainer(**container)
        if isinstance(zip, dict):
            zip = GoogleAppEngineFlexibleAppVersionDeploymentZip(**zip)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeployment.__init__)
            check_type(argname="argument cloud_build_options", value=cloud_build_options, expected_type=type_hints["cloud_build_options"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument files", value=files, expected_type=type_hints["files"])
            check_type(argname="argument zip", value=zip, expected_type=type_hints["zip"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud_build_options is not None:
            self._values["cloud_build_options"] = cloud_build_options
        if container is not None:
            self._values["container"] = container
        if files is not None:
            self._values["files"] = files
        if zip is not None:
            self._values["zip"] = zip

    @builtins.property
    def cloud_build_options(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions"]:
        '''cloud_build_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cloud_build_options GoogleAppEngineFlexibleAppVersion#cloud_build_options}
        '''
        result = self._values.get("cloud_build_options")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions"], result)

    @builtins.property
    def container(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionDeploymentContainer"]:
        '''container block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#container GoogleAppEngineFlexibleAppVersion#container}
        '''
        result = self._values.get("container")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionDeploymentContainer"], result)

    @builtins.property
    def files(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionDeploymentFiles"]]]:
        '''files block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#files GoogleAppEngineFlexibleAppVersion#files}
        '''
        result = self._values.get("files")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionDeploymentFiles"]]], result)

    @builtins.property
    def zip(self) -> typing.Optional["GoogleAppEngineFlexibleAppVersionDeploymentZip"]:
        '''zip block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#zip GoogleAppEngineFlexibleAppVersion#zip}
        '''
        result = self._values.get("zip")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionDeploymentZip"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionDeployment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions",
    jsii_struct_bases=[],
    name_mapping={
        "app_yaml_path": "appYamlPath",
        "cloud_build_timeout": "cloudBuildTimeout",
    },
)
class GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions:
    def __init__(
        self,
        *,
        app_yaml_path: builtins.str,
        cloud_build_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param app_yaml_path: Path to the yaml file used in deployment, used to determine runtime configuration details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#app_yaml_path GoogleAppEngineFlexibleAppVersion#app_yaml_path}
        :param cloud_build_timeout: The Cloud Build timeout used as part of any dependent builds performed by version creation. Defaults to 10 minutes. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cloud_build_timeout GoogleAppEngineFlexibleAppVersion#cloud_build_timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions.__init__)
            check_type(argname="argument app_yaml_path", value=app_yaml_path, expected_type=type_hints["app_yaml_path"])
            check_type(argname="argument cloud_build_timeout", value=cloud_build_timeout, expected_type=type_hints["cloud_build_timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_yaml_path": app_yaml_path,
        }
        if cloud_build_timeout is not None:
            self._values["cloud_build_timeout"] = cloud_build_timeout

    @builtins.property
    def app_yaml_path(self) -> builtins.str:
        '''Path to the yaml file used in deployment, used to determine runtime configuration details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#app_yaml_path GoogleAppEngineFlexibleAppVersion#app_yaml_path}
        '''
        result = self._values.get("app_yaml_path")
        assert result is not None, "Required property 'app_yaml_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_build_timeout(self) -> typing.Optional[builtins.str]:
        '''The Cloud Build timeout used as part of any dependent builds performed by version creation. Defaults to 10 minutes.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cloud_build_timeout GoogleAppEngineFlexibleAppVersion#cloud_build_timeout}
        '''
        result = self._values.get("cloud_build_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudBuildTimeout")
    def reset_cloud_build_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudBuildTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="appYamlPathInput")
    def app_yaml_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appYamlPathInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudBuildTimeoutInput")
    def cloud_build_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudBuildTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="appYamlPath")
    def app_yaml_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appYamlPath"))

    @app_yaml_path.setter
    def app_yaml_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference, "app_yaml_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appYamlPath", value)

    @builtins.property
    @jsii.member(jsii_name="cloudBuildTimeout")
    def cloud_build_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudBuildTimeout"))

    @cloud_build_timeout.setter
    def cloud_build_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference, "cloud_build_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudBuildTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentContainer",
    jsii_struct_bases=[],
    name_mapping={"image": "image"},
)
class GoogleAppEngineFlexibleAppVersionDeploymentContainer:
    def __init__(self, *, image: builtins.str) -> None:
        '''
        :param image: URI to the hosted container image in Google Container Registry. The URI must be fully qualified and include a tag or digest. Examples: "gcr.io/my-project/image:tag" or "gcr.io/my-project/image@digest" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#image GoogleAppEngineFlexibleAppVersion#image}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentContainer.__init__)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
        }

    @builtins.property
    def image(self) -> builtins.str:
        '''URI to the hosted container image in Google Container Registry.

        The URI must be fully qualified and include a tag or digest.
        Examples: "gcr.io/my-project/image:tag" or "gcr.io/my-project/image@digest"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#image GoogleAppEngineFlexibleAppVersion#image}
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionDeploymentContainer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionDeploymentContainerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentContainerOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentContainerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentContainerOutputReference, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentContainer]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentContainer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentContainer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentContainerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentFiles",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "source_url": "sourceUrl", "sha1_sum": "sha1Sum"},
)
class GoogleAppEngineFlexibleAppVersionDeploymentFiles:
    def __init__(
        self,
        *,
        name: builtins.str,
        source_url: builtins.str,
        sha1_sum: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}.
        :param source_url: Source URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#source_url GoogleAppEngineFlexibleAppVersion#source_url}
        :param sha1_sum: SHA1 checksum of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#sha1_sum GoogleAppEngineFlexibleAppVersion#sha1_sum}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentFiles.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_url", value=source_url, expected_type=type_hints["source_url"])
            check_type(argname="argument sha1_sum", value=sha1_sum, expected_type=type_hints["sha1_sum"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "source_url": source_url,
        }
        if sha1_sum is not None:
            self._values["sha1_sum"] = sha1_sum

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_url(self) -> builtins.str:
        '''Source URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#source_url GoogleAppEngineFlexibleAppVersion#source_url}
        '''
        result = self._values.get("source_url")
        assert result is not None, "Required property 'source_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sha1_sum(self) -> typing.Optional[builtins.str]:
        '''SHA1 checksum of the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#sha1_sum GoogleAppEngineFlexibleAppVersion#sha1_sum}
        '''
        result = self._values.get("sha1_sum")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionDeploymentFiles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionDeploymentFilesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentFilesList",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentFilesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentFilesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentFilesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentFilesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentFilesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionDeploymentFiles]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionDeploymentFiles]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionDeploymentFiles]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentFilesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSha1Sum")
    def reset_sha1_sum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSha1Sum", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sha1SumInput")
    def sha1_sum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sha1SumInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUrlInput")
    def source_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sha1Sum")
    def sha1_sum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha1Sum"))

    @sha1_sum.setter
    def sha1_sum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference, "sha1_sum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sha1Sum", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUrl")
    def source_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceUrl"))

    @source_url.setter
    def source_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference, "source_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionDeploymentFiles, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionDeploymentFiles, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionDeploymentFiles, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAppEngineFlexibleAppVersionDeploymentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudBuildOptions")
    def put_cloud_build_options(
        self,
        *,
        app_yaml_path: builtins.str,
        cloud_build_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param app_yaml_path: Path to the yaml file used in deployment, used to determine runtime configuration details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#app_yaml_path GoogleAppEngineFlexibleAppVersion#app_yaml_path}
        :param cloud_build_timeout: The Cloud Build timeout used as part of any dependent builds performed by version creation. Defaults to 10 minutes. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cloud_build_timeout GoogleAppEngineFlexibleAppVersion#cloud_build_timeout}
        '''
        value = GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions(
            app_yaml_path=app_yaml_path, cloud_build_timeout=cloud_build_timeout
        )

        return typing.cast(None, jsii.invoke(self, "putCloudBuildOptions", [value]))

    @jsii.member(jsii_name="putContainer")
    def put_container(self, *, image: builtins.str) -> None:
        '''
        :param image: URI to the hosted container image in Google Container Registry. The URI must be fully qualified and include a tag or digest. Examples: "gcr.io/my-project/image:tag" or "gcr.io/my-project/image@digest" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#image GoogleAppEngineFlexibleAppVersion#image}
        '''
        value = GoogleAppEngineFlexibleAppVersionDeploymentContainer(image=image)

        return typing.cast(None, jsii.invoke(self, "putContainer", [value]))

    @jsii.member(jsii_name="putFiles")
    def put_files(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAppEngineFlexibleAppVersionDeploymentFiles, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentOutputReference.put_files)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFiles", [value]))

    @jsii.member(jsii_name="putZip")
    def put_zip(
        self,
        *,
        source_url: builtins.str,
        files_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param source_url: Source URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#source_url GoogleAppEngineFlexibleAppVersion#source_url}
        :param files_count: files count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#files_count GoogleAppEngineFlexibleAppVersion#files_count}
        '''
        value = GoogleAppEngineFlexibleAppVersionDeploymentZip(
            source_url=source_url, files_count=files_count
        )

        return typing.cast(None, jsii.invoke(self, "putZip", [value]))

    @jsii.member(jsii_name="resetCloudBuildOptions")
    def reset_cloud_build_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudBuildOptions", []))

    @jsii.member(jsii_name="resetContainer")
    def reset_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainer", []))

    @jsii.member(jsii_name="resetFiles")
    def reset_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFiles", []))

    @jsii.member(jsii_name="resetZip")
    def reset_zip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZip", []))

    @builtins.property
    @jsii.member(jsii_name="cloudBuildOptions")
    def cloud_build_options(
        self,
    ) -> GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference:
        return typing.cast(GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference, jsii.get(self, "cloudBuildOptions"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(
        self,
    ) -> GoogleAppEngineFlexibleAppVersionDeploymentContainerOutputReference:
        return typing.cast(GoogleAppEngineFlexibleAppVersionDeploymentContainerOutputReference, jsii.get(self, "container"))

    @builtins.property
    @jsii.member(jsii_name="files")
    def files(self) -> GoogleAppEngineFlexibleAppVersionDeploymentFilesList:
        return typing.cast(GoogleAppEngineFlexibleAppVersionDeploymentFilesList, jsii.get(self, "files"))

    @builtins.property
    @jsii.member(jsii_name="zip")
    def zip(self) -> "GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference", jsii.get(self, "zip"))

    @builtins.property
    @jsii.member(jsii_name="cloudBuildOptionsInput")
    def cloud_build_options_input(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions], jsii.get(self, "cloudBuildOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentContainer]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentContainer], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="filesInput")
    def files_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionDeploymentFiles]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionDeploymentFiles]]], jsii.get(self, "filesInput"))

    @builtins.property
    @jsii.member(jsii_name="zipInput")
    def zip_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionDeploymentZip"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionDeploymentZip"], jsii.get(self, "zipInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionDeployment]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionDeployment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionDeployment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentZip",
    jsii_struct_bases=[],
    name_mapping={"source_url": "sourceUrl", "files_count": "filesCount"},
)
class GoogleAppEngineFlexibleAppVersionDeploymentZip:
    def __init__(
        self,
        *,
        source_url: builtins.str,
        files_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param source_url: Source URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#source_url GoogleAppEngineFlexibleAppVersion#source_url}
        :param files_count: files count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#files_count GoogleAppEngineFlexibleAppVersion#files_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentZip.__init__)
            check_type(argname="argument source_url", value=source_url, expected_type=type_hints["source_url"])
            check_type(argname="argument files_count", value=files_count, expected_type=type_hints["files_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_url": source_url,
        }
        if files_count is not None:
            self._values["files_count"] = files_count

    @builtins.property
    def source_url(self) -> builtins.str:
        '''Source URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#source_url GoogleAppEngineFlexibleAppVersion#source_url}
        '''
        result = self._values.get("source_url")
        assert result is not None, "Required property 'source_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def files_count(self) -> typing.Optional[jsii.Number]:
        '''files count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#files_count GoogleAppEngineFlexibleAppVersion#files_count}
        '''
        result = self._values.get("files_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionDeploymentZip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFilesCount")
    def reset_files_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesCount", []))

    @builtins.property
    @jsii.member(jsii_name="filesCountInput")
    def files_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "filesCountInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUrlInput")
    def source_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="filesCount")
    def files_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "filesCount"))

    @files_count.setter
    def files_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference, "files_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filesCount", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUrl")
    def source_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceUrl"))

    @source_url.setter
    def source_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference, "source_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentZip]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentZip], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionDeploymentZip],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionEndpointsApiService",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "config_id": "configId",
        "disable_trace_sampling": "disableTraceSampling",
        "rollout_strategy": "rolloutStrategy",
    },
)
class GoogleAppEngineFlexibleAppVersionEndpointsApiService:
    def __init__(
        self,
        *,
        name: builtins.str,
        config_id: typing.Optional[builtins.str] = None,
        disable_trace_sampling: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rollout_strategy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Endpoints service name which is the name of the "service" resource in the Service Management API. For example "myapi.endpoints.myproject.cloud.goog". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        :param config_id: Endpoints service configuration ID as specified by the Service Management API. For example "2016-09-19r1". By default, the rollout strategy for Endpoints is "FIXED". This means that Endpoints starts up with a particular configuration ID. When a new configuration is rolled out, Endpoints must be given the new configuration ID. The configId field is used to give the configuration ID and is required in this case. Endpoints also has a rollout strategy called "MANAGED". When using this, Endpoints fetches the latest configuration and does not need the configuration ID. In this case, configId must be omitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#config_id GoogleAppEngineFlexibleAppVersion#config_id}
        :param disable_trace_sampling: Enable or disable trace sampling. By default, this is set to false for enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disable_trace_sampling GoogleAppEngineFlexibleAppVersion#disable_trace_sampling}
        :param rollout_strategy: Endpoints rollout strategy. If FIXED, configId must be specified. If MANAGED, configId must be omitted. Default value: "FIXED" Possible values: ["FIXED", "MANAGED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#rollout_strategy GoogleAppEngineFlexibleAppVersion#rollout_strategy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionEndpointsApiService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument disable_trace_sampling", value=disable_trace_sampling, expected_type=type_hints["disable_trace_sampling"])
            check_type(argname="argument rollout_strategy", value=rollout_strategy, expected_type=type_hints["rollout_strategy"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if config_id is not None:
            self._values["config_id"] = config_id
        if disable_trace_sampling is not None:
            self._values["disable_trace_sampling"] = disable_trace_sampling
        if rollout_strategy is not None:
            self._values["rollout_strategy"] = rollout_strategy

    @builtins.property
    def name(self) -> builtins.str:
        '''Endpoints service name which is the name of the "service" resource in the Service Management API. For example "myapi.endpoints.myproject.cloud.goog".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config_id(self) -> typing.Optional[builtins.str]:
        '''Endpoints service configuration ID as specified by the Service Management API. For example "2016-09-19r1".

        By default, the rollout strategy for Endpoints is "FIXED". This means that Endpoints starts up with a particular configuration ID.
        When a new configuration is rolled out, Endpoints must be given the new configuration ID. The configId field is used to give the configuration ID
        and is required in this case.

        Endpoints also has a rollout strategy called "MANAGED". When using this, Endpoints fetches the latest configuration and does not need
        the configuration ID. In this case, configId must be omitted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#config_id GoogleAppEngineFlexibleAppVersion#config_id}
        '''
        result = self._values.get("config_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_trace_sampling(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable or disable trace sampling. By default, this is set to false for enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disable_trace_sampling GoogleAppEngineFlexibleAppVersion#disable_trace_sampling}
        '''
        result = self._values.get("disable_trace_sampling")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rollout_strategy(self) -> typing.Optional[builtins.str]:
        '''Endpoints rollout strategy.

        If FIXED, configId must be specified. If MANAGED, configId must be omitted. Default value: "FIXED" Possible values: ["FIXED", "MANAGED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#rollout_strategy GoogleAppEngineFlexibleAppVersion#rollout_strategy}
        '''
        result = self._values.get("rollout_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionEndpointsApiService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConfigId")
    def reset_config_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigId", []))

    @jsii.member(jsii_name="resetDisableTraceSampling")
    def reset_disable_trace_sampling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableTraceSampling", []))

    @jsii.member(jsii_name="resetRolloutStrategy")
    def reset_rollout_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRolloutStrategy", []))

    @builtins.property
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="disableTraceSamplingInput")
    def disable_trace_sampling_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableTraceSamplingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rolloutStrategyInput")
    def rollout_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rolloutStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference, "config_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="disableTraceSampling")
    def disable_trace_sampling(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableTraceSampling"))

    @disable_trace_sampling.setter
    def disable_trace_sampling(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference, "disable_trace_sampling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableTraceSampling", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rolloutStrategy")
    def rollout_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rolloutStrategy"))

    @rollout_strategy.setter
    def rollout_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference, "rollout_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rolloutStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionEndpointsApiService]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionEndpointsApiService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionEndpointsApiService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionEntrypoint",
    jsii_struct_bases=[],
    name_mapping={"shell": "shell"},
)
class GoogleAppEngineFlexibleAppVersionEntrypoint:
    def __init__(self, *, shell: builtins.str) -> None:
        '''
        :param shell: The format should be a shell command that can be fed to bash -c. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#shell GoogleAppEngineFlexibleAppVersion#shell}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionEntrypoint.__init__)
            check_type(argname="argument shell", value=shell, expected_type=type_hints["shell"])
        self._values: typing.Dict[str, typing.Any] = {
            "shell": shell,
        }

    @builtins.property
    def shell(self) -> builtins.str:
        '''The format should be a shell command that can be fed to bash -c.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#shell GoogleAppEngineFlexibleAppVersion#shell}
        '''
        result = self._values.get("shell")
        assert result is not None, "Required property 'shell' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionEntrypoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionEntrypointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionEntrypointOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionEntrypointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="shellInput")
    def shell_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shellInput"))

    @builtins.property
    @jsii.member(jsii_name="shell")
    def shell(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shell"))

    @shell.setter
    def shell(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionEntrypointOutputReference, "shell").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shell", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionEntrypoint]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionEntrypoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionEntrypoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionEntrypointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionHandlers",
    jsii_struct_bases=[],
    name_mapping={
        "auth_fail_action": "authFailAction",
        "login": "login",
        "redirect_http_response_code": "redirectHttpResponseCode",
        "script": "script",
        "security_level": "securityLevel",
        "static_files": "staticFiles",
        "url_regex": "urlRegex",
    },
)
class GoogleAppEngineFlexibleAppVersionHandlers:
    def __init__(
        self,
        *,
        auth_fail_action: typing.Optional[builtins.str] = None,
        login: typing.Optional[builtins.str] = None,
        redirect_http_response_code: typing.Optional[builtins.str] = None,
        script: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionHandlersScript", typing.Dict[str, typing.Any]]] = None,
        security_level: typing.Optional[builtins.str] = None,
        static_files: typing.Optional[typing.Union["GoogleAppEngineFlexibleAppVersionHandlersStaticFiles", typing.Dict[str, typing.Any]]] = None,
        url_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_fail_action: Actions to take when the user is not logged in. Possible values: ["AUTH_FAIL_ACTION_REDIRECT", "AUTH_FAIL_ACTION_UNAUTHORIZED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#auth_fail_action GoogleAppEngineFlexibleAppVersion#auth_fail_action}
        :param login: Methods to restrict access to a URL based on login status. Possible values: ["LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#login GoogleAppEngineFlexibleAppVersion#login}
        :param redirect_http_response_code: 30x code to use when performing redirects for the secure field. Possible values: ["REDIRECT_HTTP_RESPONSE_CODE_301", "REDIRECT_HTTP_RESPONSE_CODE_302", "REDIRECT_HTTP_RESPONSE_CODE_303", "REDIRECT_HTTP_RESPONSE_CODE_307"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#redirect_http_response_code GoogleAppEngineFlexibleAppVersion#redirect_http_response_code}
        :param script: script block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#script GoogleAppEngineFlexibleAppVersion#script}
        :param security_level: Security (HTTPS) enforcement for this URL. Possible values: ["SECURE_DEFAULT", "SECURE_NEVER", "SECURE_OPTIONAL", "SECURE_ALWAYS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#security_level GoogleAppEngineFlexibleAppVersion#security_level}
        :param static_files: static_files block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#static_files GoogleAppEngineFlexibleAppVersion#static_files}
        :param url_regex: URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings. All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#url_regex GoogleAppEngineFlexibleAppVersion#url_regex}
        '''
        if isinstance(script, dict):
            script = GoogleAppEngineFlexibleAppVersionHandlersScript(**script)
        if isinstance(static_files, dict):
            static_files = GoogleAppEngineFlexibleAppVersionHandlersStaticFiles(**static_files)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionHandlers.__init__)
            check_type(argname="argument auth_fail_action", value=auth_fail_action, expected_type=type_hints["auth_fail_action"])
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument redirect_http_response_code", value=redirect_http_response_code, expected_type=type_hints["redirect_http_response_code"])
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument security_level", value=security_level, expected_type=type_hints["security_level"])
            check_type(argname="argument static_files", value=static_files, expected_type=type_hints["static_files"])
            check_type(argname="argument url_regex", value=url_regex, expected_type=type_hints["url_regex"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_fail_action is not None:
            self._values["auth_fail_action"] = auth_fail_action
        if login is not None:
            self._values["login"] = login
        if redirect_http_response_code is not None:
            self._values["redirect_http_response_code"] = redirect_http_response_code
        if script is not None:
            self._values["script"] = script
        if security_level is not None:
            self._values["security_level"] = security_level
        if static_files is not None:
            self._values["static_files"] = static_files
        if url_regex is not None:
            self._values["url_regex"] = url_regex

    @builtins.property
    def auth_fail_action(self) -> typing.Optional[builtins.str]:
        '''Actions to take when the user is not logged in. Possible values: ["AUTH_FAIL_ACTION_REDIRECT", "AUTH_FAIL_ACTION_UNAUTHORIZED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#auth_fail_action GoogleAppEngineFlexibleAppVersion#auth_fail_action}
        '''
        result = self._values.get("auth_fail_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login(self) -> typing.Optional[builtins.str]:
        '''Methods to restrict access to a URL based on login status. Possible values: ["LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#login GoogleAppEngineFlexibleAppVersion#login}
        '''
        result = self._values.get("login")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_http_response_code(self) -> typing.Optional[builtins.str]:
        '''30x code to use when performing redirects for the secure field. Possible values: ["REDIRECT_HTTP_RESPONSE_CODE_301", "REDIRECT_HTTP_RESPONSE_CODE_302", "REDIRECT_HTTP_RESPONSE_CODE_303", "REDIRECT_HTTP_RESPONSE_CODE_307"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#redirect_http_response_code GoogleAppEngineFlexibleAppVersion#redirect_http_response_code}
        '''
        result = self._values.get("redirect_http_response_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def script(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionHandlersScript"]:
        '''script block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#script GoogleAppEngineFlexibleAppVersion#script}
        '''
        result = self._values.get("script")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionHandlersScript"], result)

    @builtins.property
    def security_level(self) -> typing.Optional[builtins.str]:
        '''Security (HTTPS) enforcement for this URL. Possible values: ["SECURE_DEFAULT", "SECURE_NEVER", "SECURE_OPTIONAL", "SECURE_ALWAYS"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#security_level GoogleAppEngineFlexibleAppVersion#security_level}
        '''
        result = self._values.get("security_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def static_files(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionHandlersStaticFiles"]:
        '''static_files block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#static_files GoogleAppEngineFlexibleAppVersion#static_files}
        '''
        result = self._values.get("static_files")
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionHandlersStaticFiles"], result)

    @builtins.property
    def url_regex(self) -> typing.Optional[builtins.str]:
        '''URL prefix.

        Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings.
        All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#url_regex GoogleAppEngineFlexibleAppVersion#url_regex}
        '''
        result = self._values.get("url_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionHandlers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionHandlersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionHandlersList",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionHandlersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAppEngineFlexibleAppVersionHandlersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionHandlersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAppEngineFlexibleAppVersionHandlersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionHandlers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionHandlers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionHandlers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAppEngineFlexibleAppVersionHandlersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionHandlersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionHandlersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putScript")
    def put_script(self, *, script_path: builtins.str) -> None:
        '''
        :param script_path: Path to the script from the application root directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#script_path GoogleAppEngineFlexibleAppVersion#script_path}
        '''
        value = GoogleAppEngineFlexibleAppVersionHandlersScript(
            script_path=script_path
        )

        return typing.cast(None, jsii.invoke(self, "putScript", [value]))

    @jsii.member(jsii_name="putStaticFiles")
    def put_static_files(
        self,
        *,
        application_readable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expiration: typing.Optional[builtins.str] = None,
        http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        mime_type: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        require_matching_file: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        upload_path_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_readable: Whether files should also be uploaded as code data. By default, files declared in static file handlers are uploaded as static data and are only served to end users; they cannot be read by the application. If enabled, uploads are charged against both your code and static data storage resource quotas. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#application_readable GoogleAppEngineFlexibleAppVersion#application_readable}
        :param expiration: Time a static file served by this handler should be cached by web proxies and browsers. A duration in seconds with up to nine fractional digits, terminated by 's'. Example "3.5s". Default is '0s' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#expiration GoogleAppEngineFlexibleAppVersion#expiration}
        :param http_headers: HTTP headers to use for all responses from these URLs. An object containing a list of "key:value" value pairs.". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#http_headers GoogleAppEngineFlexibleAppVersion#http_headers}
        :param mime_type: MIME type used to serve all files served by this handler. Defaults to file-specific MIME types, which are derived from each file's filename extension. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#mime_type GoogleAppEngineFlexibleAppVersion#mime_type}
        :param path: Path to the static files matched by the URL pattern, from the application root directory. The path can refer to text matched in groupings in the URL pattern. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        :param require_matching_file: Whether this handler should match the request if the file referenced by the handler does not exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#require_matching_file GoogleAppEngineFlexibleAppVersion#require_matching_file}
        :param upload_path_regex: Regular expression that matches the file paths for all files that should be referenced by this handler. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#upload_path_regex GoogleAppEngineFlexibleAppVersion#upload_path_regex}
        '''
        value = GoogleAppEngineFlexibleAppVersionHandlersStaticFiles(
            application_readable=application_readable,
            expiration=expiration,
            http_headers=http_headers,
            mime_type=mime_type,
            path=path,
            require_matching_file=require_matching_file,
            upload_path_regex=upload_path_regex,
        )

        return typing.cast(None, jsii.invoke(self, "putStaticFiles", [value]))

    @jsii.member(jsii_name="resetAuthFailAction")
    def reset_auth_fail_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthFailAction", []))

    @jsii.member(jsii_name="resetLogin")
    def reset_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogin", []))

    @jsii.member(jsii_name="resetRedirectHttpResponseCode")
    def reset_redirect_http_response_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectHttpResponseCode", []))

    @jsii.member(jsii_name="resetScript")
    def reset_script(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScript", []))

    @jsii.member(jsii_name="resetSecurityLevel")
    def reset_security_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityLevel", []))

    @jsii.member(jsii_name="resetStaticFiles")
    def reset_static_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticFiles", []))

    @jsii.member(jsii_name="resetUrlRegex")
    def reset_url_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRegex", []))

    @builtins.property
    @jsii.member(jsii_name="script")
    def script(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionHandlersScriptOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionHandlersScriptOutputReference", jsii.get(self, "script"))

    @builtins.property
    @jsii.member(jsii_name="staticFiles")
    def static_files(
        self,
    ) -> "GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference":
        return typing.cast("GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference", jsii.get(self, "staticFiles"))

    @builtins.property
    @jsii.member(jsii_name="authFailActionInput")
    def auth_fail_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authFailActionInput"))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectHttpResponseCodeInput")
    def redirect_http_response_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectHttpResponseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptInput")
    def script_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionHandlersScript"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionHandlersScript"], jsii.get(self, "scriptInput"))

    @builtins.property
    @jsii.member(jsii_name="securityLevelInput")
    def security_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="staticFilesInput")
    def static_files_input(
        self,
    ) -> typing.Optional["GoogleAppEngineFlexibleAppVersionHandlersStaticFiles"]:
        return typing.cast(typing.Optional["GoogleAppEngineFlexibleAppVersionHandlersStaticFiles"], jsii.get(self, "staticFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRegexInput")
    def url_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="authFailAction")
    def auth_fail_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authFailAction"))

    @auth_fail_action.setter
    def auth_fail_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersOutputReference, "auth_fail_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authFailAction", value)

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "login"))

    @login.setter
    def login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersOutputReference, "login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "login", value)

    @builtins.property
    @jsii.member(jsii_name="redirectHttpResponseCode")
    def redirect_http_response_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectHttpResponseCode"))

    @redirect_http_response_code.setter
    def redirect_http_response_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersOutputReference, "redirect_http_response_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectHttpResponseCode", value)

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityLevel"))

    @security_level.setter
    def security_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersOutputReference, "security_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="urlRegex")
    def url_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlRegex"))

    @url_regex.setter
    def url_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersOutputReference, "url_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlRegex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionHandlers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionHandlers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionHandlers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionHandlersScript",
    jsii_struct_bases=[],
    name_mapping={"script_path": "scriptPath"},
)
class GoogleAppEngineFlexibleAppVersionHandlersScript:
    def __init__(self, *, script_path: builtins.str) -> None:
        '''
        :param script_path: Path to the script from the application root directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#script_path GoogleAppEngineFlexibleAppVersion#script_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionHandlersScript.__init__)
            check_type(argname="argument script_path", value=script_path, expected_type=type_hints["script_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "script_path": script_path,
        }

    @builtins.property
    def script_path(self) -> builtins.str:
        '''Path to the script from the application root directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#script_path GoogleAppEngineFlexibleAppVersion#script_path}
        '''
        result = self._values.get("script_path")
        assert result is not None, "Required property 'script_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionHandlersScript(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionHandlersScriptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionHandlersScriptOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionHandlersScriptOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="scriptPathInput")
    def script_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptPathInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptPath")
    def script_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scriptPath"))

    @script_path.setter
    def script_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersScriptOutputReference, "script_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionHandlersScript]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionHandlersScript], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionHandlersScript],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersScriptOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionHandlersStaticFiles",
    jsii_struct_bases=[],
    name_mapping={
        "application_readable": "applicationReadable",
        "expiration": "expiration",
        "http_headers": "httpHeaders",
        "mime_type": "mimeType",
        "path": "path",
        "require_matching_file": "requireMatchingFile",
        "upload_path_regex": "uploadPathRegex",
    },
)
class GoogleAppEngineFlexibleAppVersionHandlersStaticFiles:
    def __init__(
        self,
        *,
        application_readable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expiration: typing.Optional[builtins.str] = None,
        http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        mime_type: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        require_matching_file: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        upload_path_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_readable: Whether files should also be uploaded as code data. By default, files declared in static file handlers are uploaded as static data and are only served to end users; they cannot be read by the application. If enabled, uploads are charged against both your code and static data storage resource quotas. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#application_readable GoogleAppEngineFlexibleAppVersion#application_readable}
        :param expiration: Time a static file served by this handler should be cached by web proxies and browsers. A duration in seconds with up to nine fractional digits, terminated by 's'. Example "3.5s". Default is '0s' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#expiration GoogleAppEngineFlexibleAppVersion#expiration}
        :param http_headers: HTTP headers to use for all responses from these URLs. An object containing a list of "key:value" value pairs.". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#http_headers GoogleAppEngineFlexibleAppVersion#http_headers}
        :param mime_type: MIME type used to serve all files served by this handler. Defaults to file-specific MIME types, which are derived from each file's filename extension. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#mime_type GoogleAppEngineFlexibleAppVersion#mime_type}
        :param path: Path to the static files matched by the URL pattern, from the application root directory. The path can refer to text matched in groupings in the URL pattern. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        :param require_matching_file: Whether this handler should match the request if the file referenced by the handler does not exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#require_matching_file GoogleAppEngineFlexibleAppVersion#require_matching_file}
        :param upload_path_regex: Regular expression that matches the file paths for all files that should be referenced by this handler. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#upload_path_regex GoogleAppEngineFlexibleAppVersion#upload_path_regex}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionHandlersStaticFiles.__init__)
            check_type(argname="argument application_readable", value=application_readable, expected_type=type_hints["application_readable"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument http_headers", value=http_headers, expected_type=type_hints["http_headers"])
            check_type(argname="argument mime_type", value=mime_type, expected_type=type_hints["mime_type"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument require_matching_file", value=require_matching_file, expected_type=type_hints["require_matching_file"])
            check_type(argname="argument upload_path_regex", value=upload_path_regex, expected_type=type_hints["upload_path_regex"])
        self._values: typing.Dict[str, typing.Any] = {}
        if application_readable is not None:
            self._values["application_readable"] = application_readable
        if expiration is not None:
            self._values["expiration"] = expiration
        if http_headers is not None:
            self._values["http_headers"] = http_headers
        if mime_type is not None:
            self._values["mime_type"] = mime_type
        if path is not None:
            self._values["path"] = path
        if require_matching_file is not None:
            self._values["require_matching_file"] = require_matching_file
        if upload_path_regex is not None:
            self._values["upload_path_regex"] = upload_path_regex

    @builtins.property
    def application_readable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether files should also be uploaded as code data.

        By default, files declared in static file handlers are
        uploaded as static data and are only served to end users; they cannot be read by the application. If enabled,
        uploads are charged against both your code and static data storage resource quotas.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#application_readable GoogleAppEngineFlexibleAppVersion#application_readable}
        '''
        result = self._values.get("application_readable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def expiration(self) -> typing.Optional[builtins.str]:
        '''Time a static file served by this handler should be cached by web proxies and browsers.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example "3.5s".
        Default is '0s'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#expiration GoogleAppEngineFlexibleAppVersion#expiration}
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''HTTP headers to use for all responses from these URLs. An object containing a list of "key:value" value pairs.".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#http_headers GoogleAppEngineFlexibleAppVersion#http_headers}
        '''
        result = self._values.get("http_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def mime_type(self) -> typing.Optional[builtins.str]:
        '''MIME type used to serve all files served by this handler.

        Defaults to file-specific MIME types, which are derived from each file's filename extension.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#mime_type GoogleAppEngineFlexibleAppVersion#mime_type}
        '''
        result = self._values.get("mime_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path to the static files matched by the URL pattern, from the application root directory.

        The path can refer to text matched in groupings in the URL pattern.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_matching_file(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this handler should match the request if the file referenced by the handler does not exist.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#require_matching_file GoogleAppEngineFlexibleAppVersion#require_matching_file}
        '''
        result = self._values.get("require_matching_file")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def upload_path_regex(self) -> typing.Optional[builtins.str]:
        '''Regular expression that matches the file paths for all files that should be referenced by this handler.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#upload_path_regex GoogleAppEngineFlexibleAppVersion#upload_path_regex}
        '''
        result = self._values.get("upload_path_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionHandlersStaticFiles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApplicationReadable")
    def reset_application_readable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationReadable", []))

    @jsii.member(jsii_name="resetExpiration")
    def reset_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiration", []))

    @jsii.member(jsii_name="resetHttpHeaders")
    def reset_http_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeaders", []))

    @jsii.member(jsii_name="resetMimeType")
    def reset_mime_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMimeType", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetRequireMatchingFile")
    def reset_require_matching_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireMatchingFile", []))

    @jsii.member(jsii_name="resetUploadPathRegex")
    def reset_upload_path_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUploadPathRegex", []))

    @builtins.property
    @jsii.member(jsii_name="applicationReadableInput")
    def application_readable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "applicationReadableInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationInput")
    def expiration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeadersInput")
    def http_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "httpHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="mimeTypeInput")
    def mime_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mimeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="requireMatchingFileInput")
    def require_matching_file_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireMatchingFileInput"))

    @builtins.property
    @jsii.member(jsii_name="uploadPathRegexInput")
    def upload_path_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uploadPathRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationReadable")
    def application_readable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "applicationReadable"))

    @application_readable.setter
    def application_readable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference, "application_readable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationReadable", value)

    @builtins.property
    @jsii.member(jsii_name="expiration")
    def expiration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiration"))

    @expiration.setter
    def expiration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference, "expiration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiration", value)

    @builtins.property
    @jsii.member(jsii_name="httpHeaders")
    def http_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "httpHeaders"))

    @http_headers.setter
    def http_headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference, "http_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="mimeType")
    def mime_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mimeType"))

    @mime_type.setter
    def mime_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference, "mime_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mimeType", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="requireMatchingFile")
    def require_matching_file(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireMatchingFile"))

    @require_matching_file.setter
    def require_matching_file(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference, "require_matching_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireMatchingFile", value)

    @builtins.property
    @jsii.member(jsii_name="uploadPathRegex")
    def upload_path_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uploadPathRegex"))

    @upload_path_regex.setter
    def upload_path_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference, "upload_path_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uploadPathRegex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionHandlersStaticFiles]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionHandlersStaticFiles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionHandlersStaticFiles],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionLivenessCheck",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "check_interval": "checkInterval",
        "failure_threshold": "failureThreshold",
        "host": "host",
        "initial_delay": "initialDelay",
        "success_threshold": "successThreshold",
        "timeout": "timeout",
    },
)
class GoogleAppEngineFlexibleAppVersionLivenessCheck:
    def __init__(
        self,
        *,
        path: builtins.str,
        check_interval: typing.Optional[builtins.str] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        host: typing.Optional[builtins.str] = None,
        initial_delay: typing.Optional[builtins.str] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: The request path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        :param check_interval: Interval between health checks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#check_interval GoogleAppEngineFlexibleAppVersion#check_interval}
        :param failure_threshold: Number of consecutive failed checks required before considering the VM unhealthy. Default: 4. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#failure_threshold GoogleAppEngineFlexibleAppVersion#failure_threshold}
        :param host: Host header to send when performing a HTTP Readiness check. Example: "myapp.appspot.com". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#host GoogleAppEngineFlexibleAppVersion#host}
        :param initial_delay: The initial delay before starting to execute the checks. Default: "300s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#initial_delay GoogleAppEngineFlexibleAppVersion#initial_delay}
        :param success_threshold: Number of consecutive successful checks required before considering the VM healthy. Default: 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#success_threshold GoogleAppEngineFlexibleAppVersion#success_threshold}
        :param timeout: Time before the check is considered failed. Default: "4s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeout GoogleAppEngineFlexibleAppVersion#timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionLivenessCheck.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument check_interval", value=check_interval, expected_type=type_hints["check_interval"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument initial_delay", value=initial_delay, expected_type=type_hints["initial_delay"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if check_interval is not None:
            self._values["check_interval"] = check_interval
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if host is not None:
            self._values["host"] = host
        if initial_delay is not None:
            self._values["initial_delay"] = initial_delay
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def path(self) -> builtins.str:
        '''The request path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def check_interval(self) -> typing.Optional[builtins.str]:
        '''Interval between health checks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#check_interval GoogleAppEngineFlexibleAppVersion#check_interval}
        '''
        result = self._values.get("check_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Number of consecutive failed checks required before considering the VM unhealthy. Default: 4.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#failure_threshold GoogleAppEngineFlexibleAppVersion#failure_threshold}
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host header to send when performing a HTTP Readiness check. Example: "myapp.appspot.com".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#host GoogleAppEngineFlexibleAppVersion#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_delay(self) -> typing.Optional[builtins.str]:
        '''The initial delay before starting to execute the checks. Default: "300s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#initial_delay GoogleAppEngineFlexibleAppVersion#initial_delay}
        '''
        result = self._values.get("initial_delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Number of consecutive successful checks required before considering the VM healthy. Default: 2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#success_threshold GoogleAppEngineFlexibleAppVersion#success_threshold}
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Time before the check is considered failed. Default: "4s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeout GoogleAppEngineFlexibleAppVersion#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionLivenessCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckInterval")
    def reset_check_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckInterval", []))

    @jsii.member(jsii_name="resetFailureThreshold")
    def reset_failure_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureThreshold", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetInitialDelay")
    def reset_initial_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialDelay", []))

    @jsii.member(jsii_name="resetSuccessThreshold")
    def reset_success_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessThreshold", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="checkIntervalInput")
    def check_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="failureThresholdInput")
    def failure_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="initialDelayInput")
    def initial_delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initialDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="successThresholdInput")
    def success_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="checkInterval")
    def check_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkInterval"))

    @check_interval.setter
    def check_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference, "check_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkInterval", value)

    @builtins.property
    @jsii.member(jsii_name="failureThreshold")
    def failure_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureThreshold"))

    @failure_threshold.setter
    def failure_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference, "failure_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="initialDelay")
    def initial_delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialDelay"))

    @initial_delay.setter
    def initial_delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference, "initial_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialDelay", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="successThreshold")
    def success_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successThreshold"))

    @success_threshold.setter
    def success_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference, "success_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionLivenessCheck]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionLivenessCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionLivenessCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionManualScaling",
    jsii_struct_bases=[],
    name_mapping={"instances": "instances"},
)
class GoogleAppEngineFlexibleAppVersionManualScaling:
    def __init__(self, *, instances: jsii.Number) -> None:
        '''
        :param instances: Number of instances to assign to the service at the start. *Note:** When managing the number of instances at runtime through the App Engine Admin API or the (now deprecated) Python 2 Modules API set_num_instances() you must use 'lifecycle.ignore_changes = ["manual_scaling"[0].instances]' to prevent drift detection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instances GoogleAppEngineFlexibleAppVersion#instances}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionManualScaling.__init__)
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
        self._values: typing.Dict[str, typing.Any] = {
            "instances": instances,
        }

    @builtins.property
    def instances(self) -> jsii.Number:
        '''Number of instances to assign to the service at the start.

        *Note:** When managing the number of instances at runtime through the App Engine Admin API or the (now deprecated) Python 2
        Modules API set_num_instances() you must use 'lifecycle.ignore_changes = ["manual_scaling"[0].instances]' to prevent drift detection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instances GoogleAppEngineFlexibleAppVersion#instances}
        '''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionManualScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionManualScalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionManualScalingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionManualScalingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionManualScalingOutputReference, "instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionManualScaling]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionManualScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionManualScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionManualScalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionNetwork",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "forwarded_ports": "forwardedPorts",
        "instance_tag": "instanceTag",
        "session_affinity": "sessionAffinity",
        "subnetwork": "subnetwork",
    },
)
class GoogleAppEngineFlexibleAppVersionNetwork:
    def __init__(
        self,
        *,
        name: builtins.str,
        forwarded_ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_tag: typing.Optional[builtins.str] = None,
        session_affinity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subnetwork: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Google Compute Engine network where the virtual machines are created. Specify the short name, not the resource path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        :param forwarded_ports: List of ports, or port pairs, to forward from the virtual machine to the application container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#forwarded_ports GoogleAppEngineFlexibleAppVersion#forwarded_ports}
        :param instance_tag: Tag to apply to the instance during creation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instance_tag GoogleAppEngineFlexibleAppVersion#instance_tag}
        :param session_affinity: Enable session affinity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#session_affinity GoogleAppEngineFlexibleAppVersion#session_affinity}
        :param subnetwork: Google Cloud Platform sub-network where the virtual machines are created. Specify the short name, not the resource path. If the network that the instance is being created in is a Legacy network, then the IP address is allocated from the IPv4Range. If the network that the instance is being created in is an auto Subnet Mode Network, then only network name should be specified (not the subnetworkName) and the IP address is created from the IPCidrRange of the subnetwork that exists in that zone for that network. If the network that the instance is being created in is a custom Subnet Mode Network, then the subnetworkName must be specified and the IP address is created from the IPCidrRange of the subnetwork. If specified, the subnetwork must exist in the same region as the App Engine flexible environment application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#subnetwork GoogleAppEngineFlexibleAppVersion#subnetwork}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionNetwork.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument forwarded_ports", value=forwarded_ports, expected_type=type_hints["forwarded_ports"])
            check_type(argname="argument instance_tag", value=instance_tag, expected_type=type_hints["instance_tag"])
            check_type(argname="argument session_affinity", value=session_affinity, expected_type=type_hints["session_affinity"])
            check_type(argname="argument subnetwork", value=subnetwork, expected_type=type_hints["subnetwork"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if forwarded_ports is not None:
            self._values["forwarded_ports"] = forwarded_ports
        if instance_tag is not None:
            self._values["instance_tag"] = instance_tag
        if session_affinity is not None:
            self._values["session_affinity"] = session_affinity
        if subnetwork is not None:
            self._values["subnetwork"] = subnetwork

    @builtins.property
    def name(self) -> builtins.str:
        '''Google Compute Engine network where the virtual machines are created. Specify the short name, not the resource path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def forwarded_ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of ports, or port pairs, to forward from the virtual machine to the application container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#forwarded_ports GoogleAppEngineFlexibleAppVersion#forwarded_ports}
        '''
        result = self._values.get("forwarded_ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def instance_tag(self) -> typing.Optional[builtins.str]:
        '''Tag to apply to the instance during creation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#instance_tag GoogleAppEngineFlexibleAppVersion#instance_tag}
        '''
        result = self._values.get("instance_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_affinity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable session affinity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#session_affinity GoogleAppEngineFlexibleAppVersion#session_affinity}
        '''
        result = self._values.get("session_affinity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subnetwork(self) -> typing.Optional[builtins.str]:
        '''Google Cloud Platform sub-network where the virtual machines are created. Specify the short name, not the resource path.

        If the network that the instance is being created in is a Legacy network, then the IP address is allocated from the IPv4Range.
        If the network that the instance is being created in is an auto Subnet Mode Network, then only network name should be specified (not the subnetworkName) and the IP address is created from the IPCidrRange of the subnetwork that exists in that zone for that network.
        If the network that the instance is being created in is a custom Subnet Mode Network, then the subnetworkName must be specified and the IP address is created from the IPCidrRange of the subnetwork.
        If specified, the subnetwork must exist in the same region as the App Engine flexible environment application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#subnetwork GoogleAppEngineFlexibleAppVersion#subnetwork}
        '''
        result = self._values.get("subnetwork")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionNetworkOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetForwardedPorts")
    def reset_forwarded_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardedPorts", []))

    @jsii.member(jsii_name="resetInstanceTag")
    def reset_instance_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTag", []))

    @jsii.member(jsii_name="resetSessionAffinity")
    def reset_session_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinity", []))

    @jsii.member(jsii_name="resetSubnetwork")
    def reset_subnetwork(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetwork", []))

    @builtins.property
    @jsii.member(jsii_name="forwardedPortsInput")
    def forwarded_ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "forwardedPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTagInput")
    def instance_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTagInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityInput")
    def session_affinity_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sessionAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetworkInput")
    def subnetwork_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardedPorts")
    def forwarded_ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "forwardedPorts"))

    @forwarded_ports.setter
    def forwarded_ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionNetworkOutputReference, "forwarded_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardedPorts", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTag")
    def instance_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceTag"))

    @instance_tag.setter
    def instance_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionNetworkOutputReference, "instance_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTag", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionNetworkOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinity")
    def session_affinity(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sessionAffinity"))

    @session_affinity.setter
    def session_affinity(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionNetworkOutputReference, "session_affinity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinity", value)

    @builtins.property
    @jsii.member(jsii_name="subnetwork")
    def subnetwork(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetwork"))

    @subnetwork.setter
    def subnetwork(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionNetworkOutputReference, "subnetwork").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetwork", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionNetwork]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionNetwork],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionReadinessCheck",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "app_start_timeout": "appStartTimeout",
        "check_interval": "checkInterval",
        "failure_threshold": "failureThreshold",
        "host": "host",
        "success_threshold": "successThreshold",
        "timeout": "timeout",
    },
)
class GoogleAppEngineFlexibleAppVersionReadinessCheck:
    def __init__(
        self,
        *,
        path: builtins.str,
        app_start_timeout: typing.Optional[builtins.str] = None,
        check_interval: typing.Optional[builtins.str] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        host: typing.Optional[builtins.str] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: The request path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        :param app_start_timeout: A maximum time limit on application initialization, measured from moment the application successfully replies to a healthcheck until it is ready to serve traffic. Default: "300s" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#app_start_timeout GoogleAppEngineFlexibleAppVersion#app_start_timeout}
        :param check_interval: Interval between health checks. Default: "5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#check_interval GoogleAppEngineFlexibleAppVersion#check_interval}
        :param failure_threshold: Number of consecutive failed checks required before removing traffic. Default: 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#failure_threshold GoogleAppEngineFlexibleAppVersion#failure_threshold}
        :param host: Host header to send when performing a HTTP Readiness check. Example: "myapp.appspot.com". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#host GoogleAppEngineFlexibleAppVersion#host}
        :param success_threshold: Number of consecutive successful checks required before receiving traffic. Default: 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#success_threshold GoogleAppEngineFlexibleAppVersion#success_threshold}
        :param timeout: Time before the check is considered failed. Default: "4s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeout GoogleAppEngineFlexibleAppVersion#timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionReadinessCheck.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument app_start_timeout", value=app_start_timeout, expected_type=type_hints["app_start_timeout"])
            check_type(argname="argument check_interval", value=check_interval, expected_type=type_hints["check_interval"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if app_start_timeout is not None:
            self._values["app_start_timeout"] = app_start_timeout
        if check_interval is not None:
            self._values["check_interval"] = check_interval
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if host is not None:
            self._values["host"] = host
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def path(self) -> builtins.str:
        '''The request path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#path GoogleAppEngineFlexibleAppVersion#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_start_timeout(self) -> typing.Optional[builtins.str]:
        '''A maximum time limit on application initialization, measured from moment the application successfully replies to a healthcheck until it is ready to serve traffic.

        Default: "300s"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#app_start_timeout GoogleAppEngineFlexibleAppVersion#app_start_timeout}
        '''
        result = self._values.get("app_start_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def check_interval(self) -> typing.Optional[builtins.str]:
        '''Interval between health checks.  Default: "5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#check_interval GoogleAppEngineFlexibleAppVersion#check_interval}
        '''
        result = self._values.get("check_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Number of consecutive failed checks required before removing traffic. Default: 2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#failure_threshold GoogleAppEngineFlexibleAppVersion#failure_threshold}
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host header to send when performing a HTTP Readiness check. Example: "myapp.appspot.com".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#host GoogleAppEngineFlexibleAppVersion#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Number of consecutive successful checks required before receiving traffic. Default: 2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#success_threshold GoogleAppEngineFlexibleAppVersion#success_threshold}
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Time before the check is considered failed. Default: "4s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#timeout GoogleAppEngineFlexibleAppVersion#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionReadinessCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppStartTimeout")
    def reset_app_start_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppStartTimeout", []))

    @jsii.member(jsii_name="resetCheckInterval")
    def reset_check_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckInterval", []))

    @jsii.member(jsii_name="resetFailureThreshold")
    def reset_failure_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureThreshold", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetSuccessThreshold")
    def reset_success_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessThreshold", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="appStartTimeoutInput")
    def app_start_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appStartTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="checkIntervalInput")
    def check_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="failureThresholdInput")
    def failure_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="successThresholdInput")
    def success_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="appStartTimeout")
    def app_start_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appStartTimeout"))

    @app_start_timeout.setter
    def app_start_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference, "app_start_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appStartTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="checkInterval")
    def check_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkInterval"))

    @check_interval.setter
    def check_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference, "check_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkInterval", value)

    @builtins.property
    @jsii.member(jsii_name="failureThreshold")
    def failure_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureThreshold"))

    @failure_threshold.setter
    def failure_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference, "failure_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="successThreshold")
    def success_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successThreshold"))

    @success_threshold.setter
    def success_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference, "success_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionReadinessCheck]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionReadinessCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionReadinessCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionResources",
    jsii_struct_bases=[],
    name_mapping={
        "cpu": "cpu",
        "disk_gb": "diskGb",
        "memory_gb": "memoryGb",
        "volumes": "volumes",
    },
)
class GoogleAppEngineFlexibleAppVersionResources:
    def __init__(
        self,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        disk_gb: typing.Optional[jsii.Number] = None,
        memory_gb: typing.Optional[jsii.Number] = None,
        volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAppEngineFlexibleAppVersionResourcesVolumes", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cpu: Number of CPU cores needed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cpu GoogleAppEngineFlexibleAppVersion#cpu}
        :param disk_gb: Disk size (GB) needed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disk_gb GoogleAppEngineFlexibleAppVersion#disk_gb}
        :param memory_gb: Memory (GB) needed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#memory_gb GoogleAppEngineFlexibleAppVersion#memory_gb}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#volumes GoogleAppEngineFlexibleAppVersion#volumes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionResources.__init__)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument disk_gb", value=disk_gb, expected_type=type_hints["disk_gb"])
            check_type(argname="argument memory_gb", value=memory_gb, expected_type=type_hints["memory_gb"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if disk_gb is not None:
            self._values["disk_gb"] = disk_gb
        if memory_gb is not None:
            self._values["memory_gb"] = memory_gb
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''Number of CPU cores needed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#cpu GoogleAppEngineFlexibleAppVersion#cpu}
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_gb(self) -> typing.Optional[jsii.Number]:
        '''Disk size (GB) needed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#disk_gb GoogleAppEngineFlexibleAppVersion#disk_gb}
        '''
        result = self._values.get("disk_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_gb(self) -> typing.Optional[jsii.Number]:
        '''Memory (GB) needed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#memory_gb GoogleAppEngineFlexibleAppVersion#memory_gb}
        '''
        result = self._values.get("memory_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionResourcesVolumes"]]]:
        '''volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#volumes GoogleAppEngineFlexibleAppVersion#volumes}
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionResourcesVolumes"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionResourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionResourcesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionResourcesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVolumes")
    def put_volumes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAppEngineFlexibleAppVersionResourcesVolumes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionResourcesOutputReference.put_volumes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolumes", [value]))

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetDiskGb")
    def reset_disk_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskGb", []))

    @jsii.member(jsii_name="resetMemoryGb")
    def reset_memory_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryGb", []))

    @jsii.member(jsii_name="resetVolumes")
    def reset_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumes", []))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> "GoogleAppEngineFlexibleAppVersionResourcesVolumesList":
        return typing.cast("GoogleAppEngineFlexibleAppVersionResourcesVolumesList", jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="diskGbInput")
    def disk_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskGbInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryGbInput")
    def memory_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryGbInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesInput")
    def volumes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionResourcesVolumes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAppEngineFlexibleAppVersionResourcesVolumes"]]], jsii.get(self, "volumesInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesOutputReference, "cpu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="diskGb")
    def disk_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskGb"))

    @disk_gb.setter
    def disk_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesOutputReference, "disk_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskGb", value)

    @builtins.property
    @jsii.member(jsii_name="memoryGb")
    def memory_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryGb"))

    @memory_gb.setter
    def memory_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesOutputReference, "memory_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionResources]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionResources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionResources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionResourcesVolumes",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "size_gb": "sizeGb", "volume_type": "volumeType"},
)
class GoogleAppEngineFlexibleAppVersionResourcesVolumes:
    def __init__(
        self,
        *,
        name: builtins.str,
        size_gb: jsii.Number,
        volume_type: builtins.str,
    ) -> None:
        '''
        :param name: Unique name for the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        :param size_gb: Volume size in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#size_gb GoogleAppEngineFlexibleAppVersion#size_gb}
        :param volume_type: Underlying volume type, e.g. 'tmpfs'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#volume_type GoogleAppEngineFlexibleAppVersion#volume_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionResourcesVolumes.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument size_gb", value=size_gb, expected_type=type_hints["size_gb"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "size_gb": size_gb,
            "volume_type": volume_type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Unique name for the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size_gb(self) -> jsii.Number:
        '''Volume size in gigabytes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#size_gb GoogleAppEngineFlexibleAppVersion#size_gb}
        '''
        result = self._values.get("size_gb")
        assert result is not None, "Required property 'size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def volume_type(self) -> builtins.str:
        '''Underlying volume type, e.g. 'tmpfs'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#volume_type GoogleAppEngineFlexibleAppVersion#volume_type}
        '''
        result = self._values.get("volume_type")
        assert result is not None, "Required property 'volume_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionResourcesVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionResourcesVolumesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionResourcesVolumesList",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionResourcesVolumesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionResourcesVolumesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesVolumesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesVolumesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesVolumesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionResourcesVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionResourcesVolumes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAppEngineFlexibleAppVersionResourcesVolumes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesVolumesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference.__init__)
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
    @jsii.member(jsii_name="sizeGbInput")
    def size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sizeGb")
    def size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeGb"))

    @size_gb.setter
    def size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference, "size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference, "volume_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionResourcesVolumes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionResourcesVolumes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionResourcesVolumes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleAppEngineFlexibleAppVersionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#create GoogleAppEngineFlexibleAppVersion#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#delete GoogleAppEngineFlexibleAppVersion#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#update GoogleAppEngineFlexibleAppVersion#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#create GoogleAppEngineFlexibleAppVersion#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#delete GoogleAppEngineFlexibleAppVersion#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#update GoogleAppEngineFlexibleAppVersion#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAppEngineFlexibleAppVersionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionVpcAccessConnector",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleAppEngineFlexibleAppVersionVpcAccessConnector:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionVpcAccessConnector.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_flexible_app_version#name GoogleAppEngineFlexibleAppVersion#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineFlexibleAppVersionVpcAccessConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineFlexibleAppVersionVpcAccessConnectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineFlexibleAppVersion.GoogleAppEngineFlexibleAppVersionVpcAccessConnectorOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineFlexibleAppVersionVpcAccessConnectorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionVpcAccessConnectorOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineFlexibleAppVersionVpcAccessConnector]:
        return typing.cast(typing.Optional[GoogleAppEngineFlexibleAppVersionVpcAccessConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineFlexibleAppVersionVpcAccessConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineFlexibleAppVersionVpcAccessConnectorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleAppEngineFlexibleAppVersion",
    "GoogleAppEngineFlexibleAppVersionApiConfig",
    "GoogleAppEngineFlexibleAppVersionApiConfigOutputReference",
    "GoogleAppEngineFlexibleAppVersionAutomaticScaling",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilization",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingCpuUtilizationOutputReference",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilization",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingDiskUtilizationOutputReference",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilization",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingNetworkUtilizationOutputReference",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingOutputReference",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilization",
    "GoogleAppEngineFlexibleAppVersionAutomaticScalingRequestUtilizationOutputReference",
    "GoogleAppEngineFlexibleAppVersionConfig",
    "GoogleAppEngineFlexibleAppVersionDeployment",
    "GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptions",
    "GoogleAppEngineFlexibleAppVersionDeploymentCloudBuildOptionsOutputReference",
    "GoogleAppEngineFlexibleAppVersionDeploymentContainer",
    "GoogleAppEngineFlexibleAppVersionDeploymentContainerOutputReference",
    "GoogleAppEngineFlexibleAppVersionDeploymentFiles",
    "GoogleAppEngineFlexibleAppVersionDeploymentFilesList",
    "GoogleAppEngineFlexibleAppVersionDeploymentFilesOutputReference",
    "GoogleAppEngineFlexibleAppVersionDeploymentOutputReference",
    "GoogleAppEngineFlexibleAppVersionDeploymentZip",
    "GoogleAppEngineFlexibleAppVersionDeploymentZipOutputReference",
    "GoogleAppEngineFlexibleAppVersionEndpointsApiService",
    "GoogleAppEngineFlexibleAppVersionEndpointsApiServiceOutputReference",
    "GoogleAppEngineFlexibleAppVersionEntrypoint",
    "GoogleAppEngineFlexibleAppVersionEntrypointOutputReference",
    "GoogleAppEngineFlexibleAppVersionHandlers",
    "GoogleAppEngineFlexibleAppVersionHandlersList",
    "GoogleAppEngineFlexibleAppVersionHandlersOutputReference",
    "GoogleAppEngineFlexibleAppVersionHandlersScript",
    "GoogleAppEngineFlexibleAppVersionHandlersScriptOutputReference",
    "GoogleAppEngineFlexibleAppVersionHandlersStaticFiles",
    "GoogleAppEngineFlexibleAppVersionHandlersStaticFilesOutputReference",
    "GoogleAppEngineFlexibleAppVersionLivenessCheck",
    "GoogleAppEngineFlexibleAppVersionLivenessCheckOutputReference",
    "GoogleAppEngineFlexibleAppVersionManualScaling",
    "GoogleAppEngineFlexibleAppVersionManualScalingOutputReference",
    "GoogleAppEngineFlexibleAppVersionNetwork",
    "GoogleAppEngineFlexibleAppVersionNetworkOutputReference",
    "GoogleAppEngineFlexibleAppVersionReadinessCheck",
    "GoogleAppEngineFlexibleAppVersionReadinessCheckOutputReference",
    "GoogleAppEngineFlexibleAppVersionResources",
    "GoogleAppEngineFlexibleAppVersionResourcesOutputReference",
    "GoogleAppEngineFlexibleAppVersionResourcesVolumes",
    "GoogleAppEngineFlexibleAppVersionResourcesVolumesList",
    "GoogleAppEngineFlexibleAppVersionResourcesVolumesOutputReference",
    "GoogleAppEngineFlexibleAppVersionTimeouts",
    "GoogleAppEngineFlexibleAppVersionTimeoutsOutputReference",
    "GoogleAppEngineFlexibleAppVersionVpcAccessConnector",
    "GoogleAppEngineFlexibleAppVersionVpcAccessConnectorOutputReference",
]

publication.publish()
