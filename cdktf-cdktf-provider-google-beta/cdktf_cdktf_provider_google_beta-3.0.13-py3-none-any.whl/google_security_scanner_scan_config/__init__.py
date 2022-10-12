'''
# `google_security_scanner_scan_config`

Refer to the Terraform Registory for docs: [`google_security_scanner_scan_config`](https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config).
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


class GoogleSecurityScannerScanConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config google_security_scanner_scan_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        starting_urls: typing.Sequence[builtins.str],
        authentication: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigAuthentication", typing.Dict[str, typing.Any]]] = None,
        blacklist_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        export_to_security_command_center: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_qps: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigSchedule", typing.Dict[str, typing.Any]]] = None,
        target_platforms: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_agent: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config google_security_scanner_scan_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The user provider display name of the ScanConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#display_name GoogleSecurityScannerScanConfig#display_name}
        :param starting_urls: The starting URLs from which the scanner finds site pages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#starting_urls GoogleSecurityScannerScanConfig#starting_urls}
        :param authentication: authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#authentication GoogleSecurityScannerScanConfig#authentication}
        :param blacklist_patterns: The blacklist URL patterns as described in https://cloud.google.com/security-scanner/docs/excluded-urls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#blacklist_patterns GoogleSecurityScannerScanConfig#blacklist_patterns}
        :param export_to_security_command_center: Controls export of scan configurations and results to Cloud Security Command Center. Default value: "ENABLED" Possible values: ["ENABLED", "DISABLED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#export_to_security_command_center GoogleSecurityScannerScanConfig#export_to_security_command_center}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#id GoogleSecurityScannerScanConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_qps: The maximum QPS during scanning. A valid value ranges from 5 to 20 inclusively. Defaults to 15. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#max_qps GoogleSecurityScannerScanConfig#max_qps}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#project GoogleSecurityScannerScanConfig#project}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#schedule GoogleSecurityScannerScanConfig#schedule}
        :param target_platforms: Set of Cloud Platforms targeted by the scan. If empty, APP_ENGINE will be used as a default. Possible values: ["APP_ENGINE", "COMPUTE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#target_platforms GoogleSecurityScannerScanConfig#target_platforms}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#timeouts GoogleSecurityScannerScanConfig#timeouts}
        :param user_agent: Type of the user agents used for scanning Default value: "CHROME_LINUX" Possible values: ["USER_AGENT_UNSPECIFIED", "CHROME_LINUX", "CHROME_ANDROID", "SAFARI_IPHONE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#user_agent GoogleSecurityScannerScanConfig#user_agent}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleSecurityScannerScanConfigConfig(
            display_name=display_name,
            starting_urls=starting_urls,
            authentication=authentication,
            blacklist_patterns=blacklist_patterns,
            export_to_security_command_center=export_to_security_command_center,
            id=id,
            max_qps=max_qps,
            project=project,
            schedule=schedule,
            target_platforms=target_platforms,
            timeouts=timeouts,
            user_agent=user_agent,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAuthentication")
    def put_authentication(
        self,
        *,
        custom_account: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigAuthenticationCustomAccount", typing.Dict[str, typing.Any]]] = None,
        google_account: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigAuthenticationGoogleAccount", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_account: custom_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#custom_account GoogleSecurityScannerScanConfig#custom_account}
        :param google_account: google_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#google_account GoogleSecurityScannerScanConfig#google_account}
        '''
        value = GoogleSecurityScannerScanConfigAuthentication(
            custom_account=custom_account, google_account=google_account
        )

        return typing.cast(None, jsii.invoke(self, "putAuthentication", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        interval_duration_days: jsii.Number,
        schedule_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_duration_days: The duration of time between executions in days. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#interval_duration_days GoogleSecurityScannerScanConfig#interval_duration_days}
        :param schedule_time: A timestamp indicates when the next run will be scheduled. The value is refreshed by the server after each run. If unspecified, it will default to current server time, which means the scan will be scheduled to start immediately. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#schedule_time GoogleSecurityScannerScanConfig#schedule_time}
        '''
        value = GoogleSecurityScannerScanConfigSchedule(
            interval_duration_days=interval_duration_days, schedule_time=schedule_time
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#create GoogleSecurityScannerScanConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#delete GoogleSecurityScannerScanConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#update GoogleSecurityScannerScanConfig#update}.
        '''
        value = GoogleSecurityScannerScanConfigTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuthentication")
    def reset_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthentication", []))

    @jsii.member(jsii_name="resetBlacklistPatterns")
    def reset_blacklist_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlacklistPatterns", []))

    @jsii.member(jsii_name="resetExportToSecurityCommandCenter")
    def reset_export_to_security_command_center(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExportToSecurityCommandCenter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxQps")
    def reset_max_qps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxQps", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetTargetPlatforms")
    def reset_target_platforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetPlatforms", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserAgent")
    def reset_user_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAgent", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authentication")
    def authentication(
        self,
    ) -> "GoogleSecurityScannerScanConfigAuthenticationOutputReference":
        return typing.cast("GoogleSecurityScannerScanConfigAuthenticationOutputReference", jsii.get(self, "authentication"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "GoogleSecurityScannerScanConfigScheduleOutputReference":
        return typing.cast("GoogleSecurityScannerScanConfigScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleSecurityScannerScanConfigTimeoutsOutputReference":
        return typing.cast("GoogleSecurityScannerScanConfigTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authenticationInput")
    def authentication_input(
        self,
    ) -> typing.Optional["GoogleSecurityScannerScanConfigAuthentication"]:
        return typing.cast(typing.Optional["GoogleSecurityScannerScanConfigAuthentication"], jsii.get(self, "authenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="blacklistPatternsInput")
    def blacklist_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "blacklistPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="exportToSecurityCommandCenterInput")
    def export_to_security_command_center_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exportToSecurityCommandCenterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxQpsInput")
    def max_qps_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxQpsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(
        self,
    ) -> typing.Optional["GoogleSecurityScannerScanConfigSchedule"]:
        return typing.cast(typing.Optional["GoogleSecurityScannerScanConfigSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="startingUrlsInput")
    def starting_urls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "startingUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPlatformsInput")
    def target_platforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetPlatformsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleSecurityScannerScanConfigTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleSecurityScannerScanConfigTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userAgentInput")
    def user_agent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="blacklistPatterns")
    def blacklist_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "blacklistPatterns"))

    @blacklist_patterns.setter
    def blacklist_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "blacklist_patterns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blacklistPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="exportToSecurityCommandCenter")
    def export_to_security_command_center(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exportToSecurityCommandCenter"))

    @export_to_security_command_center.setter
    def export_to_security_command_center(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "export_to_security_command_center").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exportToSecurityCommandCenter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxQps")
    def max_qps(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxQps"))

    @max_qps.setter
    def max_qps(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "max_qps").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxQps", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="startingUrls")
    def starting_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "startingUrls"))

    @starting_urls.setter
    def starting_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "starting_urls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startingUrls", value)

    @builtins.property
    @jsii.member(jsii_name="targetPlatforms")
    def target_platforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetPlatforms"))

    @target_platforms.setter
    def target_platforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "target_platforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPlatforms", value)

    @builtins.property
    @jsii.member(jsii_name="userAgent")
    def user_agent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAgent"))

    @user_agent.setter
    def user_agent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfig, "user_agent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAgent", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "custom_account": "customAccount",
        "google_account": "googleAccount",
    },
)
class GoogleSecurityScannerScanConfigAuthentication:
    def __init__(
        self,
        *,
        custom_account: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigAuthenticationCustomAccount", typing.Dict[str, typing.Any]]] = None,
        google_account: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigAuthenticationGoogleAccount", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_account: custom_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#custom_account GoogleSecurityScannerScanConfig#custom_account}
        :param google_account: google_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#google_account GoogleSecurityScannerScanConfig#google_account}
        '''
        if isinstance(custom_account, dict):
            custom_account = GoogleSecurityScannerScanConfigAuthenticationCustomAccount(**custom_account)
        if isinstance(google_account, dict):
            google_account = GoogleSecurityScannerScanConfigAuthenticationGoogleAccount(**google_account)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigAuthentication.__init__)
            check_type(argname="argument custom_account", value=custom_account, expected_type=type_hints["custom_account"])
            check_type(argname="argument google_account", value=google_account, expected_type=type_hints["google_account"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_account is not None:
            self._values["custom_account"] = custom_account
        if google_account is not None:
            self._values["google_account"] = google_account

    @builtins.property
    def custom_account(
        self,
    ) -> typing.Optional["GoogleSecurityScannerScanConfigAuthenticationCustomAccount"]:
        '''custom_account block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#custom_account GoogleSecurityScannerScanConfig#custom_account}
        '''
        result = self._values.get("custom_account")
        return typing.cast(typing.Optional["GoogleSecurityScannerScanConfigAuthenticationCustomAccount"], result)

    @builtins.property
    def google_account(
        self,
    ) -> typing.Optional["GoogleSecurityScannerScanConfigAuthenticationGoogleAccount"]:
        '''google_account block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#google_account GoogleSecurityScannerScanConfig#google_account}
        '''
        result = self._values.get("google_account")
        return typing.cast(typing.Optional["GoogleSecurityScannerScanConfigAuthenticationGoogleAccount"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecurityScannerScanConfigAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigAuthenticationCustomAccount",
    jsii_struct_bases=[],
    name_mapping={
        "login_url": "loginUrl",
        "password": "password",
        "username": "username",
    },
)
class GoogleSecurityScannerScanConfigAuthenticationCustomAccount:
    def __init__(
        self,
        *,
        login_url: builtins.str,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param login_url: The login form URL of the website. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#login_url GoogleSecurityScannerScanConfig#login_url}
        :param password: The password of the custom account. The credential is stored encrypted in GCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#password GoogleSecurityScannerScanConfig#password}
        :param username: The user name of the custom account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#username GoogleSecurityScannerScanConfig#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigAuthenticationCustomAccount.__init__)
            check_type(argname="argument login_url", value=login_url, expected_type=type_hints["login_url"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "login_url": login_url,
            "password": password,
            "username": username,
        }

    @builtins.property
    def login_url(self) -> builtins.str:
        '''The login form URL of the website.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#login_url GoogleSecurityScannerScanConfig#login_url}
        '''
        result = self._values.get("login_url")
        assert result is not None, "Required property 'login_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password of the custom account. The credential is stored encrypted in GCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#password GoogleSecurityScannerScanConfig#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The user name of the custom account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#username GoogleSecurityScannerScanConfig#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecurityScannerScanConfigAuthenticationCustomAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="loginUrlInput")
    def login_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="loginUrl")
    def login_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginUrl"))

    @login_url.setter
    def login_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference, "login_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginUrl", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSecurityScannerScanConfigAuthenticationCustomAccount]:
        return typing.cast(typing.Optional[GoogleSecurityScannerScanConfigAuthenticationCustomAccount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSecurityScannerScanConfigAuthenticationCustomAccount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigAuthenticationGoogleAccount",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class GoogleSecurityScannerScanConfigAuthenticationGoogleAccount:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: The password of the Google account. The credential is stored encrypted in GCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#password GoogleSecurityScannerScanConfig#password}
        :param username: The user name of the Google account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#username GoogleSecurityScannerScanConfig#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigAuthenticationGoogleAccount.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''The password of the Google account. The credential is stored encrypted in GCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#password GoogleSecurityScannerScanConfig#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The user name of the Google account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#username GoogleSecurityScannerScanConfig#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecurityScannerScanConfigAuthenticationGoogleAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSecurityScannerScanConfigAuthenticationGoogleAccount]:
        return typing.cast(typing.Optional[GoogleSecurityScannerScanConfigAuthenticationGoogleAccount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSecurityScannerScanConfigAuthenticationGoogleAccount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSecurityScannerScanConfigAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigAuthenticationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomAccount")
    def put_custom_account(
        self,
        *,
        login_url: builtins.str,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param login_url: The login form URL of the website. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#login_url GoogleSecurityScannerScanConfig#login_url}
        :param password: The password of the custom account. The credential is stored encrypted in GCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#password GoogleSecurityScannerScanConfig#password}
        :param username: The user name of the custom account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#username GoogleSecurityScannerScanConfig#username}
        '''
        value = GoogleSecurityScannerScanConfigAuthenticationCustomAccount(
            login_url=login_url, password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putCustomAccount", [value]))

    @jsii.member(jsii_name="putGoogleAccount")
    def put_google_account(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: The password of the Google account. The credential is stored encrypted in GCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#password GoogleSecurityScannerScanConfig#password}
        :param username: The user name of the Google account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#username GoogleSecurityScannerScanConfig#username}
        '''
        value = GoogleSecurityScannerScanConfigAuthenticationGoogleAccount(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putGoogleAccount", [value]))

    @jsii.member(jsii_name="resetCustomAccount")
    def reset_custom_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAccount", []))

    @jsii.member(jsii_name="resetGoogleAccount")
    def reset_google_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleAccount", []))

    @builtins.property
    @jsii.member(jsii_name="customAccount")
    def custom_account(
        self,
    ) -> GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference:
        return typing.cast(GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference, jsii.get(self, "customAccount"))

    @builtins.property
    @jsii.member(jsii_name="googleAccount")
    def google_account(
        self,
    ) -> GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference:
        return typing.cast(GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference, jsii.get(self, "googleAccount"))

    @builtins.property
    @jsii.member(jsii_name="customAccountInput")
    def custom_account_input(
        self,
    ) -> typing.Optional[GoogleSecurityScannerScanConfigAuthenticationCustomAccount]:
        return typing.cast(typing.Optional[GoogleSecurityScannerScanConfigAuthenticationCustomAccount], jsii.get(self, "customAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAccountInput")
    def google_account_input(
        self,
    ) -> typing.Optional[GoogleSecurityScannerScanConfigAuthenticationGoogleAccount]:
        return typing.cast(typing.Optional[GoogleSecurityScannerScanConfigAuthenticationGoogleAccount], jsii.get(self, "googleAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSecurityScannerScanConfigAuthentication]:
        return typing.cast(typing.Optional[GoogleSecurityScannerScanConfigAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSecurityScannerScanConfigAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigAuthenticationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigConfig",
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
        "starting_urls": "startingUrls",
        "authentication": "authentication",
        "blacklist_patterns": "blacklistPatterns",
        "export_to_security_command_center": "exportToSecurityCommandCenter",
        "id": "id",
        "max_qps": "maxQps",
        "project": "project",
        "schedule": "schedule",
        "target_platforms": "targetPlatforms",
        "timeouts": "timeouts",
        "user_agent": "userAgent",
    },
)
class GoogleSecurityScannerScanConfigConfig(cdktf.TerraformMetaArguments):
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
        starting_urls: typing.Sequence[builtins.str],
        authentication: typing.Optional[typing.Union[GoogleSecurityScannerScanConfigAuthentication, typing.Dict[str, typing.Any]]] = None,
        blacklist_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        export_to_security_command_center: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_qps: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigSchedule", typing.Dict[str, typing.Any]]] = None,
        target_platforms: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSecurityScannerScanConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_agent: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The user provider display name of the ScanConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#display_name GoogleSecurityScannerScanConfig#display_name}
        :param starting_urls: The starting URLs from which the scanner finds site pages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#starting_urls GoogleSecurityScannerScanConfig#starting_urls}
        :param authentication: authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#authentication GoogleSecurityScannerScanConfig#authentication}
        :param blacklist_patterns: The blacklist URL patterns as described in https://cloud.google.com/security-scanner/docs/excluded-urls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#blacklist_patterns GoogleSecurityScannerScanConfig#blacklist_patterns}
        :param export_to_security_command_center: Controls export of scan configurations and results to Cloud Security Command Center. Default value: "ENABLED" Possible values: ["ENABLED", "DISABLED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#export_to_security_command_center GoogleSecurityScannerScanConfig#export_to_security_command_center}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#id GoogleSecurityScannerScanConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_qps: The maximum QPS during scanning. A valid value ranges from 5 to 20 inclusively. Defaults to 15. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#max_qps GoogleSecurityScannerScanConfig#max_qps}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#project GoogleSecurityScannerScanConfig#project}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#schedule GoogleSecurityScannerScanConfig#schedule}
        :param target_platforms: Set of Cloud Platforms targeted by the scan. If empty, APP_ENGINE will be used as a default. Possible values: ["APP_ENGINE", "COMPUTE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#target_platforms GoogleSecurityScannerScanConfig#target_platforms}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#timeouts GoogleSecurityScannerScanConfig#timeouts}
        :param user_agent: Type of the user agents used for scanning Default value: "CHROME_LINUX" Possible values: ["USER_AGENT_UNSPECIFIED", "CHROME_LINUX", "CHROME_ANDROID", "SAFARI_IPHONE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#user_agent GoogleSecurityScannerScanConfig#user_agent}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(authentication, dict):
            authentication = GoogleSecurityScannerScanConfigAuthentication(**authentication)
        if isinstance(schedule, dict):
            schedule = GoogleSecurityScannerScanConfigSchedule(**schedule)
        if isinstance(timeouts, dict):
            timeouts = GoogleSecurityScannerScanConfigTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument starting_urls", value=starting_urls, expected_type=type_hints["starting_urls"])
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument blacklist_patterns", value=blacklist_patterns, expected_type=type_hints["blacklist_patterns"])
            check_type(argname="argument export_to_security_command_center", value=export_to_security_command_center, expected_type=type_hints["export_to_security_command_center"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_qps", value=max_qps, expected_type=type_hints["max_qps"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument target_platforms", value=target_platforms, expected_type=type_hints["target_platforms"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_agent", value=user_agent, expected_type=type_hints["user_agent"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "starting_urls": starting_urls,
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
        if authentication is not None:
            self._values["authentication"] = authentication
        if blacklist_patterns is not None:
            self._values["blacklist_patterns"] = blacklist_patterns
        if export_to_security_command_center is not None:
            self._values["export_to_security_command_center"] = export_to_security_command_center
        if id is not None:
            self._values["id"] = id
        if max_qps is not None:
            self._values["max_qps"] = max_qps
        if project is not None:
            self._values["project"] = project
        if schedule is not None:
            self._values["schedule"] = schedule
        if target_platforms is not None:
            self._values["target_platforms"] = target_platforms
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_agent is not None:
            self._values["user_agent"] = user_agent

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
        '''The user provider display name of the ScanConfig.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#display_name GoogleSecurityScannerScanConfig#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def starting_urls(self) -> typing.List[builtins.str]:
        '''The starting URLs from which the scanner finds site pages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#starting_urls GoogleSecurityScannerScanConfig#starting_urls}
        '''
        result = self._values.get("starting_urls")
        assert result is not None, "Required property 'starting_urls' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def authentication(
        self,
    ) -> typing.Optional[GoogleSecurityScannerScanConfigAuthentication]:
        '''authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#authentication GoogleSecurityScannerScanConfig#authentication}
        '''
        result = self._values.get("authentication")
        return typing.cast(typing.Optional[GoogleSecurityScannerScanConfigAuthentication], result)

    @builtins.property
    def blacklist_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The blacklist URL patterns as described in https://cloud.google.com/security-scanner/docs/excluded-urls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#blacklist_patterns GoogleSecurityScannerScanConfig#blacklist_patterns}
        '''
        result = self._values.get("blacklist_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def export_to_security_command_center(self) -> typing.Optional[builtins.str]:
        '''Controls export of scan configurations and results to Cloud Security Command Center. Default value: "ENABLED" Possible values: ["ENABLED", "DISABLED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#export_to_security_command_center GoogleSecurityScannerScanConfig#export_to_security_command_center}
        '''
        result = self._values.get("export_to_security_command_center")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#id GoogleSecurityScannerScanConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_qps(self) -> typing.Optional[jsii.Number]:
        '''The maximum QPS during scanning. A valid value ranges from 5 to 20 inclusively. Defaults to 15.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#max_qps GoogleSecurityScannerScanConfig#max_qps}
        '''
        result = self._values.get("max_qps")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#project GoogleSecurityScannerScanConfig#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional["GoogleSecurityScannerScanConfigSchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#schedule GoogleSecurityScannerScanConfig#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["GoogleSecurityScannerScanConfigSchedule"], result)

    @builtins.property
    def target_platforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of Cloud Platforms targeted by the scan.

        If empty, APP_ENGINE will be used as a default. Possible values: ["APP_ENGINE", "COMPUTE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#target_platforms GoogleSecurityScannerScanConfig#target_platforms}
        '''
        result = self._values.get("target_platforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleSecurityScannerScanConfigTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#timeouts GoogleSecurityScannerScanConfig#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleSecurityScannerScanConfigTimeouts"], result)

    @builtins.property
    def user_agent(self) -> typing.Optional[builtins.str]:
        '''Type of the user agents used for scanning Default value: "CHROME_LINUX" Possible values: ["USER_AGENT_UNSPECIFIED", "CHROME_LINUX", "CHROME_ANDROID", "SAFARI_IPHONE"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#user_agent GoogleSecurityScannerScanConfig#user_agent}
        '''
        result = self._values.get("user_agent")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecurityScannerScanConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "interval_duration_days": "intervalDurationDays",
        "schedule_time": "scheduleTime",
    },
)
class GoogleSecurityScannerScanConfigSchedule:
    def __init__(
        self,
        *,
        interval_duration_days: jsii.Number,
        schedule_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_duration_days: The duration of time between executions in days. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#interval_duration_days GoogleSecurityScannerScanConfig#interval_duration_days}
        :param schedule_time: A timestamp indicates when the next run will be scheduled. The value is refreshed by the server after each run. If unspecified, it will default to current server time, which means the scan will be scheduled to start immediately. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#schedule_time GoogleSecurityScannerScanConfig#schedule_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigSchedule.__init__)
            check_type(argname="argument interval_duration_days", value=interval_duration_days, expected_type=type_hints["interval_duration_days"])
            check_type(argname="argument schedule_time", value=schedule_time, expected_type=type_hints["schedule_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "interval_duration_days": interval_duration_days,
        }
        if schedule_time is not None:
            self._values["schedule_time"] = schedule_time

    @builtins.property
    def interval_duration_days(self) -> jsii.Number:
        '''The duration of time between executions in days.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#interval_duration_days GoogleSecurityScannerScanConfig#interval_duration_days}
        '''
        result = self._values.get("interval_duration_days")
        assert result is not None, "Required property 'interval_duration_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def schedule_time(self) -> typing.Optional[builtins.str]:
        '''A timestamp indicates when the next run will be scheduled.

        The value is refreshed
        by the server after each run. If unspecified, it will default to current server time,
        which means the scan will be scheduled to start immediately.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#schedule_time GoogleSecurityScannerScanConfig#schedule_time}
        '''
        result = self._values.get("schedule_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecurityScannerScanConfigSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecurityScannerScanConfigScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigScheduleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetScheduleTime")
    def reset_schedule_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleTime", []))

    @builtins.property
    @jsii.member(jsii_name="intervalDurationDaysInput")
    def interval_duration_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalDurationDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleTimeInput")
    def schedule_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalDurationDays")
    def interval_duration_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalDurationDays"))

    @interval_duration_days.setter
    def interval_duration_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigScheduleOutputReference, "interval_duration_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalDurationDays", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleTime")
    def schedule_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleTime"))

    @schedule_time.setter
    def schedule_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigScheduleOutputReference, "schedule_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSecurityScannerScanConfigSchedule]:
        return typing.cast(typing.Optional[GoogleSecurityScannerScanConfigSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSecurityScannerScanConfigSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleSecurityScannerScanConfigTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#create GoogleSecurityScannerScanConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#delete GoogleSecurityScannerScanConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#update GoogleSecurityScannerScanConfig#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#create GoogleSecurityScannerScanConfig#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#delete GoogleSecurityScannerScanConfig#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_security_scanner_scan_config#update GoogleSecurityScannerScanConfig#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSecurityScannerScanConfigTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSecurityScannerScanConfigTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSecurityScannerScanConfig.GoogleSecurityScannerScanConfigTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSecurityScannerScanConfigTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSecurityScannerScanConfigTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSecurityScannerScanConfigTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSecurityScannerScanConfigTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSecurityScannerScanConfigTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleSecurityScannerScanConfig",
    "GoogleSecurityScannerScanConfigAuthentication",
    "GoogleSecurityScannerScanConfigAuthenticationCustomAccount",
    "GoogleSecurityScannerScanConfigAuthenticationCustomAccountOutputReference",
    "GoogleSecurityScannerScanConfigAuthenticationGoogleAccount",
    "GoogleSecurityScannerScanConfigAuthenticationGoogleAccountOutputReference",
    "GoogleSecurityScannerScanConfigAuthenticationOutputReference",
    "GoogleSecurityScannerScanConfigConfig",
    "GoogleSecurityScannerScanConfigSchedule",
    "GoogleSecurityScannerScanConfigScheduleOutputReference",
    "GoogleSecurityScannerScanConfigTimeouts",
    "GoogleSecurityScannerScanConfigTimeoutsOutputReference",
]

publication.publish()
