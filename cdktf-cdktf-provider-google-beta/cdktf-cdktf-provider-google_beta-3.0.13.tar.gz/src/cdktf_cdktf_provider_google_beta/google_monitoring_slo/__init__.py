'''
# `google_monitoring_slo`

Refer to the Terraform Registory for docs: [`google_monitoring_slo`](https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo).
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


class GoogleMonitoringSlo(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSlo",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo google_monitoring_slo}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        goal: jsii.Number,
        service: builtins.str,
        basic_sli: typing.Optional[typing.Union["GoogleMonitoringSloBasicSli", typing.Dict[str, typing.Any]]] = None,
        calendar_period: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        request_based_sli: typing.Optional[typing.Union["GoogleMonitoringSloRequestBasedSli", typing.Dict[str, typing.Any]]] = None,
        rolling_period_days: typing.Optional[jsii.Number] = None,
        slo_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringSloTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        windows_based_sli: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSli", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo google_monitoring_slo} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param goal: The fraction of service that must be good in order for this objective to be met. 0 < goal <= 0.999 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#goal GoogleMonitoringSlo#goal}
        :param service: ID of the service to which this SLO belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#service GoogleMonitoringSlo#service}
        :param basic_sli: basic_sli block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#basic_sli GoogleMonitoringSlo#basic_sli}
        :param calendar_period: A calendar period, semantically "since the start of the current ". Possible values: ["DAY", "WEEK", "FORTNIGHT", "MONTH"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#calendar_period GoogleMonitoringSlo#calendar_period}
        :param display_name: Name used for UI elements listing this SLO. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#display_name GoogleMonitoringSlo#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#id GoogleMonitoringSlo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#project GoogleMonitoringSlo#project}.
        :param request_based_sli: request_based_sli block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#request_based_sli GoogleMonitoringSlo#request_based_sli}
        :param rolling_period_days: A rolling time period, semantically "in the past X days". Must be between 1 to 30 days, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#rolling_period_days GoogleMonitoringSlo#rolling_period_days}
        :param slo_id: The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#slo_id GoogleMonitoringSlo#slo_id}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#timeouts GoogleMonitoringSlo#timeouts}
        :param user_labels: This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#user_labels GoogleMonitoringSlo#user_labels}
        :param windows_based_sli: windows_based_sli block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#windows_based_sli GoogleMonitoringSlo#windows_based_sli}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSlo.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleMonitoringSloConfig(
            goal=goal,
            service=service,
            basic_sli=basic_sli,
            calendar_period=calendar_period,
            display_name=display_name,
            id=id,
            project=project,
            request_based_sli=request_based_sli,
            rolling_period_days=rolling_period_days,
            slo_id=slo_id,
            timeouts=timeouts,
            user_labels=user_labels,
            windows_based_sli=windows_based_sli,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBasicSli")
    def put_basic_sli(
        self,
        *,
        availability: typing.Optional[typing.Union["GoogleMonitoringSloBasicSliAvailability", typing.Dict[str, typing.Any]]] = None,
        latency: typing.Optional[typing.Union["GoogleMonitoringSloBasicSliLatency", typing.Dict[str, typing.Any]]] = None,
        location: typing.Optional[typing.Sequence[builtins.str]] = None,
        method: typing.Optional[typing.Sequence[builtins.str]] = None,
        version: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param availability: availability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#availability GoogleMonitoringSlo#availability}
        :param latency: latency block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#latency GoogleMonitoringSlo#latency}
        :param location: An optional set of locations to which this SLI is relevant. Telemetry from other locations will not be used to calculate performance for this SLI. If omitted, this SLI applies to all locations in which the Service has activity. For service types that don't support breaking down by location, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#location GoogleMonitoringSlo#location}
        :param method: An optional set of RPCs to which this SLI is relevant. Telemetry from other methods will not be used to calculate performance for this SLI. If omitted, this SLI applies to all the Service's methods. For service types that don't support breaking down by method, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#method GoogleMonitoringSlo#method}
        :param version: The set of API versions to which this SLI is relevant. Telemetry from other API versions will not be used to calculate performance for this SLI. If omitted, this SLI applies to all API versions. For service types that don't support breaking down by version, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#version GoogleMonitoringSlo#version}
        '''
        value = GoogleMonitoringSloBasicSli(
            availability=availability,
            latency=latency,
            location=location,
            method=method,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putBasicSli", [value]))

    @jsii.member(jsii_name="putRequestBasedSli")
    def put_request_based_sli(
        self,
        *,
        distribution_cut: typing.Optional[typing.Union["GoogleMonitoringSloRequestBasedSliDistributionCut", typing.Dict[str, typing.Any]]] = None,
        good_total_ratio: typing.Optional[typing.Union["GoogleMonitoringSloRequestBasedSliGoodTotalRatio", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param distribution_cut: distribution_cut block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_cut GoogleMonitoringSlo#distribution_cut}
        :param good_total_ratio: good_total_ratio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio GoogleMonitoringSlo#good_total_ratio}
        '''
        value = GoogleMonitoringSloRequestBasedSli(
            distribution_cut=distribution_cut, good_total_ratio=good_total_ratio
        )

        return typing.cast(None, jsii.invoke(self, "putRequestBasedSli", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#create GoogleMonitoringSlo#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#delete GoogleMonitoringSlo#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#update GoogleMonitoringSlo#update}.
        '''
        value = GoogleMonitoringSloTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWindowsBasedSli")
    def put_windows_based_sli(
        self,
        *,
        good_bad_metric_filter: typing.Optional[builtins.str] = None,
        good_total_ratio_threshold: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold", typing.Dict[str, typing.Any]]] = None,
        metric_mean_in_range: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliMetricMeanInRange", typing.Dict[str, typing.Any]]] = None,
        metric_sum_in_range: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliMetricSumInRange", typing.Dict[str, typing.Any]]] = None,
        window_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param good_bad_metric_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ with ValueType = BOOL. The window is good if any true values appear in the window. One of 'good_bad_metric_filter', 'good_total_ratio_threshold', 'metric_mean_in_range', 'metric_sum_in_range' must be set for 'windows_based_sli'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_bad_metric_filter GoogleMonitoringSlo#good_bad_metric_filter}
        :param good_total_ratio_threshold: good_total_ratio_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio_threshold GoogleMonitoringSlo#good_total_ratio_threshold}
        :param metric_mean_in_range: metric_mean_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#metric_mean_in_range GoogleMonitoringSlo#metric_mean_in_range}
        :param metric_sum_in_range: metric_sum_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#metric_sum_in_range GoogleMonitoringSlo#metric_sum_in_range}
        :param window_period: Duration over which window quality is evaluated, given as a duration string "{X}s" representing X seconds. Must be an integer fraction of a day and at least 60s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#window_period GoogleMonitoringSlo#window_period}
        '''
        value = GoogleMonitoringSloWindowsBasedSli(
            good_bad_metric_filter=good_bad_metric_filter,
            good_total_ratio_threshold=good_total_ratio_threshold,
            metric_mean_in_range=metric_mean_in_range,
            metric_sum_in_range=metric_sum_in_range,
            window_period=window_period,
        )

        return typing.cast(None, jsii.invoke(self, "putWindowsBasedSli", [value]))

    @jsii.member(jsii_name="resetBasicSli")
    def reset_basic_sli(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicSli", []))

    @jsii.member(jsii_name="resetCalendarPeriod")
    def reset_calendar_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCalendarPeriod", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRequestBasedSli")
    def reset_request_based_sli(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestBasedSli", []))

    @jsii.member(jsii_name="resetRollingPeriodDays")
    def reset_rolling_period_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollingPeriodDays", []))

    @jsii.member(jsii_name="resetSloId")
    def reset_slo_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSloId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserLabels")
    def reset_user_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserLabels", []))

    @jsii.member(jsii_name="resetWindowsBasedSli")
    def reset_windows_based_sli(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsBasedSli", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="basicSli")
    def basic_sli(self) -> "GoogleMonitoringSloBasicSliOutputReference":
        return typing.cast("GoogleMonitoringSloBasicSliOutputReference", jsii.get(self, "basicSli"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="requestBasedSli")
    def request_based_sli(self) -> "GoogleMonitoringSloRequestBasedSliOutputReference":
        return typing.cast("GoogleMonitoringSloRequestBasedSliOutputReference", jsii.get(self, "requestBasedSli"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleMonitoringSloTimeoutsOutputReference":
        return typing.cast("GoogleMonitoringSloTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="windowsBasedSli")
    def windows_based_sli(self) -> "GoogleMonitoringSloWindowsBasedSliOutputReference":
        return typing.cast("GoogleMonitoringSloWindowsBasedSliOutputReference", jsii.get(self, "windowsBasedSli"))

    @builtins.property
    @jsii.member(jsii_name="basicSliInput")
    def basic_sli_input(self) -> typing.Optional["GoogleMonitoringSloBasicSli"]:
        return typing.cast(typing.Optional["GoogleMonitoringSloBasicSli"], jsii.get(self, "basicSliInput"))

    @builtins.property
    @jsii.member(jsii_name="calendarPeriodInput")
    def calendar_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "calendarPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="goalInput")
    def goal_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "goalInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="requestBasedSliInput")
    def request_based_sli_input(
        self,
    ) -> typing.Optional["GoogleMonitoringSloRequestBasedSli"]:
        return typing.cast(typing.Optional["GoogleMonitoringSloRequestBasedSli"], jsii.get(self, "requestBasedSliInput"))

    @builtins.property
    @jsii.member(jsii_name="rollingPeriodDaysInput")
    def rolling_period_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rollingPeriodDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="sloIdInput")
    def slo_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sloIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleMonitoringSloTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleMonitoringSloTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userLabelsInput")
    def user_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "userLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsBasedSliInput")
    def windows_based_sli_input(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSli"]:
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSli"], jsii.get(self, "windowsBasedSliInput"))

    @builtins.property
    @jsii.member(jsii_name="calendarPeriod")
    def calendar_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "calendarPeriod"))

    @calendar_period.setter
    def calendar_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "calendar_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "calendarPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="goal")
    def goal(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "goal"))

    @goal.setter
    def goal(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "goal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "goal", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="rollingPeriodDays")
    def rolling_period_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rollingPeriodDays"))

    @rolling_period_days.setter
    def rolling_period_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "rolling_period_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollingPeriodDays", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="sloId")
    def slo_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sloId"))

    @slo_id.setter
    def slo_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "slo_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sloId", value)

    @builtins.property
    @jsii.member(jsii_name="userLabels")
    def user_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "userLabels"))

    @user_labels.setter
    def user_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSlo, "user_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userLabels", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloBasicSli",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "latency": "latency",
        "location": "location",
        "method": "method",
        "version": "version",
    },
)
class GoogleMonitoringSloBasicSli:
    def __init__(
        self,
        *,
        availability: typing.Optional[typing.Union["GoogleMonitoringSloBasicSliAvailability", typing.Dict[str, typing.Any]]] = None,
        latency: typing.Optional[typing.Union["GoogleMonitoringSloBasicSliLatency", typing.Dict[str, typing.Any]]] = None,
        location: typing.Optional[typing.Sequence[builtins.str]] = None,
        method: typing.Optional[typing.Sequence[builtins.str]] = None,
        version: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param availability: availability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#availability GoogleMonitoringSlo#availability}
        :param latency: latency block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#latency GoogleMonitoringSlo#latency}
        :param location: An optional set of locations to which this SLI is relevant. Telemetry from other locations will not be used to calculate performance for this SLI. If omitted, this SLI applies to all locations in which the Service has activity. For service types that don't support breaking down by location, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#location GoogleMonitoringSlo#location}
        :param method: An optional set of RPCs to which this SLI is relevant. Telemetry from other methods will not be used to calculate performance for this SLI. If omitted, this SLI applies to all the Service's methods. For service types that don't support breaking down by method, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#method GoogleMonitoringSlo#method}
        :param version: The set of API versions to which this SLI is relevant. Telemetry from other API versions will not be used to calculate performance for this SLI. If omitted, this SLI applies to all API versions. For service types that don't support breaking down by version, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#version GoogleMonitoringSlo#version}
        '''
        if isinstance(availability, dict):
            availability = GoogleMonitoringSloBasicSliAvailability(**availability)
        if isinstance(latency, dict):
            latency = GoogleMonitoringSloBasicSliLatency(**latency)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloBasicSli.__init__)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument latency", value=latency, expected_type=type_hints["latency"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if latency is not None:
            self._values["latency"] = latency
        if location is not None:
            self._values["location"] = location
        if method is not None:
            self._values["method"] = method
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def availability(
        self,
    ) -> typing.Optional["GoogleMonitoringSloBasicSliAvailability"]:
        '''availability block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#availability GoogleMonitoringSlo#availability}
        '''
        result = self._values.get("availability")
        return typing.cast(typing.Optional["GoogleMonitoringSloBasicSliAvailability"], result)

    @builtins.property
    def latency(self) -> typing.Optional["GoogleMonitoringSloBasicSliLatency"]:
        '''latency block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#latency GoogleMonitoringSlo#latency}
        '''
        result = self._values.get("latency")
        return typing.cast(typing.Optional["GoogleMonitoringSloBasicSliLatency"], result)

    @builtins.property
    def location(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional set of locations to which this SLI is relevant.

        Telemetry from other locations will not be used to calculate
        performance for this SLI. If omitted, this SLI applies to all
        locations in which the Service has activity. For service types
        that don't support breaking down by location, setting this
        field will result in an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#location GoogleMonitoringSlo#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional set of RPCs to which this SLI is relevant.

        Telemetry from other methods will not be used to calculate
        performance for this SLI. If omitted, this SLI applies to all
        the Service's methods. For service types that don't support
        breaking down by method, setting this field will result in an
        error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#method GoogleMonitoringSlo#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def version(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of API versions to which this SLI is relevant.

        Telemetry from other API versions will not be used to
        calculate performance for this SLI. If omitted,
        this SLI applies to all API versions. For service types
        that don't support breaking down by version, setting this
        field will result in an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#version GoogleMonitoringSlo#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloBasicSli(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloBasicSliAvailability",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class GoogleMonitoringSloBasicSliAvailability:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Whether an availability SLI is enabled or not. Must be set to true. Defaults to 'true'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#enabled GoogleMonitoringSlo#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloBasicSliAvailability.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether an availability SLI is enabled or not. Must be set to true. Defaults to 'true'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#enabled GoogleMonitoringSlo#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloBasicSliAvailability(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloBasicSliAvailabilityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloBasicSliAvailabilityOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloBasicSliAvailabilityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloBasicSliAvailabilityOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloBasicSliAvailability]:
        return typing.cast(typing.Optional[GoogleMonitoringSloBasicSliAvailability], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloBasicSliAvailability],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloBasicSliAvailabilityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloBasicSliLatency",
    jsii_struct_bases=[],
    name_mapping={"threshold": "threshold"},
)
class GoogleMonitoringSloBasicSliLatency:
    def __init__(self, *, threshold: builtins.str) -> None:
        '''
        :param threshold: A duration string, e.g. 10s. Good service is defined to be the count of requests made to this service that return in no more than threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloBasicSliLatency.__init__)
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "threshold": threshold,
        }

    @builtins.property
    def threshold(self) -> builtins.str:
        '''A duration string, e.g. 10s. Good service is defined to be the count of requests made to this service that return in no more than threshold.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloBasicSliLatency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloBasicSliLatencyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloBasicSliLatencyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloBasicSliLatencyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloBasicSliLatencyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleMonitoringSloBasicSliLatency]:
        return typing.cast(typing.Optional[GoogleMonitoringSloBasicSliLatency], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloBasicSliLatency],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloBasicSliLatencyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringSloBasicSliOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloBasicSliOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloBasicSliOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAvailability")
    def put_availability(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Whether an availability SLI is enabled or not. Must be set to true. Defaults to 'true'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#enabled GoogleMonitoringSlo#enabled}
        '''
        value = GoogleMonitoringSloBasicSliAvailability(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putAvailability", [value]))

    @jsii.member(jsii_name="putLatency")
    def put_latency(self, *, threshold: builtins.str) -> None:
        '''
        :param threshold: A duration string, e.g. 10s. Good service is defined to be the count of requests made to this service that return in no more than threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        value = GoogleMonitoringSloBasicSliLatency(threshold=threshold)

        return typing.cast(None, jsii.invoke(self, "putLatency", [value]))

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetLatency")
    def reset_latency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatency", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> GoogleMonitoringSloBasicSliAvailabilityOutputReference:
        return typing.cast(GoogleMonitoringSloBasicSliAvailabilityOutputReference, jsii.get(self, "availability"))

    @builtins.property
    @jsii.member(jsii_name="latency")
    def latency(self) -> GoogleMonitoringSloBasicSliLatencyOutputReference:
        return typing.cast(GoogleMonitoringSloBasicSliLatencyOutputReference, jsii.get(self, "latency"))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloBasicSliAvailability]:
        return typing.cast(typing.Optional[GoogleMonitoringSloBasicSliAvailability], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="latencyInput")
    def latency_input(self) -> typing.Optional[GoogleMonitoringSloBasicSliLatency]:
        return typing.cast(typing.Optional[GoogleMonitoringSloBasicSliLatency], jsii.get(self, "latencyInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "location"))

    @location.setter
    def location(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloBasicSliOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "method"))

    @method.setter
    def method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloBasicSliOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloBasicSliOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleMonitoringSloBasicSli]:
        return typing.cast(typing.Optional[GoogleMonitoringSloBasicSli], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloBasicSli],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloBasicSliOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "goal": "goal",
        "service": "service",
        "basic_sli": "basicSli",
        "calendar_period": "calendarPeriod",
        "display_name": "displayName",
        "id": "id",
        "project": "project",
        "request_based_sli": "requestBasedSli",
        "rolling_period_days": "rollingPeriodDays",
        "slo_id": "sloId",
        "timeouts": "timeouts",
        "user_labels": "userLabels",
        "windows_based_sli": "windowsBasedSli",
    },
)
class GoogleMonitoringSloConfig(cdktf.TerraformMetaArguments):
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
        goal: jsii.Number,
        service: builtins.str,
        basic_sli: typing.Optional[typing.Union[GoogleMonitoringSloBasicSli, typing.Dict[str, typing.Any]]] = None,
        calendar_period: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        request_based_sli: typing.Optional[typing.Union["GoogleMonitoringSloRequestBasedSli", typing.Dict[str, typing.Any]]] = None,
        rolling_period_days: typing.Optional[jsii.Number] = None,
        slo_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringSloTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        windows_based_sli: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSli", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param goal: The fraction of service that must be good in order for this objective to be met. 0 < goal <= 0.999 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#goal GoogleMonitoringSlo#goal}
        :param service: ID of the service to which this SLO belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#service GoogleMonitoringSlo#service}
        :param basic_sli: basic_sli block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#basic_sli GoogleMonitoringSlo#basic_sli}
        :param calendar_period: A calendar period, semantically "since the start of the current ". Possible values: ["DAY", "WEEK", "FORTNIGHT", "MONTH"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#calendar_period GoogleMonitoringSlo#calendar_period}
        :param display_name: Name used for UI elements listing this SLO. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#display_name GoogleMonitoringSlo#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#id GoogleMonitoringSlo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#project GoogleMonitoringSlo#project}.
        :param request_based_sli: request_based_sli block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#request_based_sli GoogleMonitoringSlo#request_based_sli}
        :param rolling_period_days: A rolling time period, semantically "in the past X days". Must be between 1 to 30 days, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#rolling_period_days GoogleMonitoringSlo#rolling_period_days}
        :param slo_id: The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#slo_id GoogleMonitoringSlo#slo_id}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#timeouts GoogleMonitoringSlo#timeouts}
        :param user_labels: This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#user_labels GoogleMonitoringSlo#user_labels}
        :param windows_based_sli: windows_based_sli block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#windows_based_sli GoogleMonitoringSlo#windows_based_sli}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(basic_sli, dict):
            basic_sli = GoogleMonitoringSloBasicSli(**basic_sli)
        if isinstance(request_based_sli, dict):
            request_based_sli = GoogleMonitoringSloRequestBasedSli(**request_based_sli)
        if isinstance(timeouts, dict):
            timeouts = GoogleMonitoringSloTimeouts(**timeouts)
        if isinstance(windows_based_sli, dict):
            windows_based_sli = GoogleMonitoringSloWindowsBasedSli(**windows_based_sli)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument goal", value=goal, expected_type=type_hints["goal"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument basic_sli", value=basic_sli, expected_type=type_hints["basic_sli"])
            check_type(argname="argument calendar_period", value=calendar_period, expected_type=type_hints["calendar_period"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument request_based_sli", value=request_based_sli, expected_type=type_hints["request_based_sli"])
            check_type(argname="argument rolling_period_days", value=rolling_period_days, expected_type=type_hints["rolling_period_days"])
            check_type(argname="argument slo_id", value=slo_id, expected_type=type_hints["slo_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_labels", value=user_labels, expected_type=type_hints["user_labels"])
            check_type(argname="argument windows_based_sli", value=windows_based_sli, expected_type=type_hints["windows_based_sli"])
        self._values: typing.Dict[str, typing.Any] = {
            "goal": goal,
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
        if basic_sli is not None:
            self._values["basic_sli"] = basic_sli
        if calendar_period is not None:
            self._values["calendar_period"] = calendar_period
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if request_based_sli is not None:
            self._values["request_based_sli"] = request_based_sli
        if rolling_period_days is not None:
            self._values["rolling_period_days"] = rolling_period_days
        if slo_id is not None:
            self._values["slo_id"] = slo_id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_labels is not None:
            self._values["user_labels"] = user_labels
        if windows_based_sli is not None:
            self._values["windows_based_sli"] = windows_based_sli

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
    def goal(self) -> jsii.Number:
        '''The fraction of service that must be good in order for this objective to be met.

        0 < goal <= 0.999

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#goal GoogleMonitoringSlo#goal}
        '''
        result = self._values.get("goal")
        assert result is not None, "Required property 'goal' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''ID of the service to which this SLO belongs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#service GoogleMonitoringSlo#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_sli(self) -> typing.Optional[GoogleMonitoringSloBasicSli]:
        '''basic_sli block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#basic_sli GoogleMonitoringSlo#basic_sli}
        '''
        result = self._values.get("basic_sli")
        return typing.cast(typing.Optional[GoogleMonitoringSloBasicSli], result)

    @builtins.property
    def calendar_period(self) -> typing.Optional[builtins.str]:
        '''A calendar period, semantically "since the start of the current ". Possible values: ["DAY", "WEEK", "FORTNIGHT", "MONTH"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#calendar_period GoogleMonitoringSlo#calendar_period}
        '''
        result = self._values.get("calendar_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Name used for UI elements listing this SLO.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#display_name GoogleMonitoringSlo#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#id GoogleMonitoringSlo#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#project GoogleMonitoringSlo#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_based_sli(
        self,
    ) -> typing.Optional["GoogleMonitoringSloRequestBasedSli"]:
        '''request_based_sli block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#request_based_sli GoogleMonitoringSlo#request_based_sli}
        '''
        result = self._values.get("request_based_sli")
        return typing.cast(typing.Optional["GoogleMonitoringSloRequestBasedSli"], result)

    @builtins.property
    def rolling_period_days(self) -> typing.Optional[jsii.Number]:
        '''A rolling time period, semantically "in the past X days". Must be between 1 to 30 days, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#rolling_period_days GoogleMonitoringSlo#rolling_period_days}
        '''
        result = self._values.get("rolling_period_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def slo_id(self) -> typing.Optional[builtins.str]:
        '''The id to use for this ServiceLevelObjective. If omitted, an id will be generated instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#slo_id GoogleMonitoringSlo#slo_id}
        '''
        result = self._values.get("slo_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleMonitoringSloTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#timeouts GoogleMonitoringSlo#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleMonitoringSloTimeouts"], result)

    @builtins.property
    def user_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#user_labels GoogleMonitoringSlo#user_labels}
        '''
        result = self._values.get("user_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def windows_based_sli(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSli"]:
        '''windows_based_sli block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#windows_based_sli GoogleMonitoringSlo#windows_based_sli}
        '''
        result = self._values.get("windows_based_sli")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSli"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloRequestBasedSli",
    jsii_struct_bases=[],
    name_mapping={
        "distribution_cut": "distributionCut",
        "good_total_ratio": "goodTotalRatio",
    },
)
class GoogleMonitoringSloRequestBasedSli:
    def __init__(
        self,
        *,
        distribution_cut: typing.Optional[typing.Union["GoogleMonitoringSloRequestBasedSliDistributionCut", typing.Dict[str, typing.Any]]] = None,
        good_total_ratio: typing.Optional[typing.Union["GoogleMonitoringSloRequestBasedSliGoodTotalRatio", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param distribution_cut: distribution_cut block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_cut GoogleMonitoringSlo#distribution_cut}
        :param good_total_ratio: good_total_ratio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio GoogleMonitoringSlo#good_total_ratio}
        '''
        if isinstance(distribution_cut, dict):
            distribution_cut = GoogleMonitoringSloRequestBasedSliDistributionCut(**distribution_cut)
        if isinstance(good_total_ratio, dict):
            good_total_ratio = GoogleMonitoringSloRequestBasedSliGoodTotalRatio(**good_total_ratio)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloRequestBasedSli.__init__)
            check_type(argname="argument distribution_cut", value=distribution_cut, expected_type=type_hints["distribution_cut"])
            check_type(argname="argument good_total_ratio", value=good_total_ratio, expected_type=type_hints["good_total_ratio"])
        self._values: typing.Dict[str, typing.Any] = {}
        if distribution_cut is not None:
            self._values["distribution_cut"] = distribution_cut
        if good_total_ratio is not None:
            self._values["good_total_ratio"] = good_total_ratio

    @builtins.property
    def distribution_cut(
        self,
    ) -> typing.Optional["GoogleMonitoringSloRequestBasedSliDistributionCut"]:
        '''distribution_cut block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_cut GoogleMonitoringSlo#distribution_cut}
        '''
        result = self._values.get("distribution_cut")
        return typing.cast(typing.Optional["GoogleMonitoringSloRequestBasedSliDistributionCut"], result)

    @builtins.property
    def good_total_ratio(
        self,
    ) -> typing.Optional["GoogleMonitoringSloRequestBasedSliGoodTotalRatio"]:
        '''good_total_ratio block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio GoogleMonitoringSlo#good_total_ratio}
        '''
        result = self._values.get("good_total_ratio")
        return typing.cast(typing.Optional["GoogleMonitoringSloRequestBasedSliGoodTotalRatio"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloRequestBasedSli(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloRequestBasedSliDistributionCut",
    jsii_struct_bases=[],
    name_mapping={"distribution_filter": "distributionFilter", "range": "range"},
)
class GoogleMonitoringSloRequestBasedSliDistributionCut:
    def __init__(
        self,
        *,
        distribution_filter: builtins.str,
        range: typing.Union["GoogleMonitoringSloRequestBasedSliDistributionCutRange", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param distribution_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ aggregating values to quantify the good service provided. Must have ValueType = DISTRIBUTION and MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_filter GoogleMonitoringSlo#distribution_filter}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        '''
        if isinstance(range, dict):
            range = GoogleMonitoringSloRequestBasedSliDistributionCutRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloRequestBasedSliDistributionCut.__init__)
            check_type(argname="argument distribution_filter", value=distribution_filter, expected_type=type_hints["distribution_filter"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[str, typing.Any] = {
            "distribution_filter": distribution_filter,
            "range": range,
        }

    @builtins.property
    def distribution_filter(self) -> builtins.str:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ aggregating values to quantify the good service provided.

        Must have ValueType = DISTRIBUTION and
        MetricKind = DELTA or MetricKind = CUMULATIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_filter GoogleMonitoringSlo#distribution_filter}
        '''
        result = self._values.get("distribution_filter")
        assert result is not None, "Required property 'distribution_filter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(self) -> "GoogleMonitoringSloRequestBasedSliDistributionCutRange":
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        '''
        result = self._values.get("range")
        assert result is not None, "Required property 'range' is missing"
        return typing.cast("GoogleMonitoringSloRequestBasedSliDistributionCutRange", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloRequestBasedSliDistributionCut(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloRequestBasedSliDistributionCutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloRequestBasedSliDistributionCutOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloRequestBasedSliDistributionCutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        :param min: Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        value = GoogleMonitoringSloRequestBasedSliDistributionCutRange(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(
        self,
    ) -> "GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference":
        return typing.cast("GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="distributionFilterInput")
    def distribution_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["GoogleMonitoringSloRequestBasedSliDistributionCutRange"]:
        return typing.cast(typing.Optional["GoogleMonitoringSloRequestBasedSliDistributionCutRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="distributionFilter")
    def distribution_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distributionFilter"))

    @distribution_filter.setter
    def distribution_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliDistributionCutOutputReference, "distribution_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributionFilter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloRequestBasedSliDistributionCut]:
        return typing.cast(typing.Optional[GoogleMonitoringSloRequestBasedSliDistributionCut], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloRequestBasedSliDistributionCut],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliDistributionCutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloRequestBasedSliDistributionCutRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class GoogleMonitoringSloRequestBasedSliDistributionCutRange:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        :param min: Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloRequestBasedSliDistributionCutRange.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        '''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloRequestBasedSliDistributionCutRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloRequestBasedSliDistributionCutRange]:
        return typing.cast(typing.Optional[GoogleMonitoringSloRequestBasedSliDistributionCutRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloRequestBasedSliDistributionCutRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloRequestBasedSliGoodTotalRatio",
    jsii_struct_bases=[],
    name_mapping={
        "bad_service_filter": "badServiceFilter",
        "good_service_filter": "goodServiceFilter",
        "total_service_filter": "totalServiceFilter",
    },
)
class GoogleMonitoringSloRequestBasedSliGoodTotalRatio:
    def __init__(
        self,
        *,
        bad_service_filter: typing.Optional[builtins.str] = None,
        good_service_filter: typing.Optional[builtins.str] = None,
        total_service_filter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bad_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying bad service provided, either demanded service that was not provided or demanded service that was of inadequate quality. Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Exactly two of 'good_service_filter','bad_service_filter','total_service_filter' must be set (good + bad = total is assumed). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#bad_service_filter GoogleMonitoringSlo#bad_service_filter}
        :param good_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying good service provided. Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Exactly two of 'good_service_filter','bad_service_filter','total_service_filter' must be set (good + bad = total is assumed). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_service_filter GoogleMonitoringSlo#good_service_filter}
        :param total_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying total demanded service. Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Exactly two of 'good_service_filter','bad_service_filter','total_service_filter' must be set (good + bad = total is assumed). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#total_service_filter GoogleMonitoringSlo#total_service_filter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloRequestBasedSliGoodTotalRatio.__init__)
            check_type(argname="argument bad_service_filter", value=bad_service_filter, expected_type=type_hints["bad_service_filter"])
            check_type(argname="argument good_service_filter", value=good_service_filter, expected_type=type_hints["good_service_filter"])
            check_type(argname="argument total_service_filter", value=total_service_filter, expected_type=type_hints["total_service_filter"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bad_service_filter is not None:
            self._values["bad_service_filter"] = bad_service_filter
        if good_service_filter is not None:
            self._values["good_service_filter"] = good_service_filter
        if total_service_filter is not None:
            self._values["total_service_filter"] = total_service_filter

    @builtins.property
    def bad_service_filter(self) -> typing.Optional[builtins.str]:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying bad service provided, either demanded service that was not provided or demanded service that was of inadequate quality.

        Must have ValueType = DOUBLE or ValueType = INT64 and
        must have MetricKind = DELTA or MetricKind = CUMULATIVE.

        Exactly two of 'good_service_filter','bad_service_filter','total_service_filter'
        must be set (good + bad = total is assumed).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#bad_service_filter GoogleMonitoringSlo#bad_service_filter}
        '''
        result = self._values.get("bad_service_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def good_service_filter(self) -> typing.Optional[builtins.str]:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying good service provided. Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE.

        Exactly two of 'good_service_filter','bad_service_filter','total_service_filter'
        must be set (good + bad = total is assumed).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_service_filter GoogleMonitoringSlo#good_service_filter}
        '''
        result = self._values.get("good_service_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def total_service_filter(self) -> typing.Optional[builtins.str]:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying total demanded service.

        Must have ValueType = DOUBLE or ValueType = INT64 and
        must have MetricKind = DELTA or MetricKind = CUMULATIVE.

        Exactly two of 'good_service_filter','bad_service_filter','total_service_filter'
        must be set (good + bad = total is assumed).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#total_service_filter GoogleMonitoringSlo#total_service_filter}
        '''
        result = self._values.get("total_service_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloRequestBasedSliGoodTotalRatio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBadServiceFilter")
    def reset_bad_service_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBadServiceFilter", []))

    @jsii.member(jsii_name="resetGoodServiceFilter")
    def reset_good_service_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoodServiceFilter", []))

    @jsii.member(jsii_name="resetTotalServiceFilter")
    def reset_total_service_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTotalServiceFilter", []))

    @builtins.property
    @jsii.member(jsii_name="badServiceFilterInput")
    def bad_service_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "badServiceFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="goodServiceFilterInput")
    def good_service_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "goodServiceFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="totalServiceFilterInput")
    def total_service_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "totalServiceFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="badServiceFilter")
    def bad_service_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "badServiceFilter"))

    @bad_service_filter.setter
    def bad_service_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference, "bad_service_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "badServiceFilter", value)

    @builtins.property
    @jsii.member(jsii_name="goodServiceFilter")
    def good_service_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "goodServiceFilter"))

    @good_service_filter.setter
    def good_service_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference, "good_service_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "goodServiceFilter", value)

    @builtins.property
    @jsii.member(jsii_name="totalServiceFilter")
    def total_service_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "totalServiceFilter"))

    @total_service_filter.setter
    def total_service_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference, "total_service_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalServiceFilter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloRequestBasedSliGoodTotalRatio]:
        return typing.cast(typing.Optional[GoogleMonitoringSloRequestBasedSliGoodTotalRatio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloRequestBasedSliGoodTotalRatio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringSloRequestBasedSliOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloRequestBasedSliOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloRequestBasedSliOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDistributionCut")
    def put_distribution_cut(
        self,
        *,
        distribution_filter: builtins.str,
        range: typing.Union[GoogleMonitoringSloRequestBasedSliDistributionCutRange, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param distribution_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ aggregating values to quantify the good service provided. Must have ValueType = DISTRIBUTION and MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_filter GoogleMonitoringSlo#distribution_filter}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        '''
        value = GoogleMonitoringSloRequestBasedSliDistributionCut(
            distribution_filter=distribution_filter, range=range
        )

        return typing.cast(None, jsii.invoke(self, "putDistributionCut", [value]))

    @jsii.member(jsii_name="putGoodTotalRatio")
    def put_good_total_ratio(
        self,
        *,
        bad_service_filter: typing.Optional[builtins.str] = None,
        good_service_filter: typing.Optional[builtins.str] = None,
        total_service_filter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bad_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying bad service provided, either demanded service that was not provided or demanded service that was of inadequate quality. Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Exactly two of 'good_service_filter','bad_service_filter','total_service_filter' must be set (good + bad = total is assumed). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#bad_service_filter GoogleMonitoringSlo#bad_service_filter}
        :param good_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying good service provided. Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Exactly two of 'good_service_filter','bad_service_filter','total_service_filter' must be set (good + bad = total is assumed). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_service_filter GoogleMonitoringSlo#good_service_filter}
        :param total_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying total demanded service. Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Exactly two of 'good_service_filter','bad_service_filter','total_service_filter' must be set (good + bad = total is assumed). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#total_service_filter GoogleMonitoringSlo#total_service_filter}
        '''
        value = GoogleMonitoringSloRequestBasedSliGoodTotalRatio(
            bad_service_filter=bad_service_filter,
            good_service_filter=good_service_filter,
            total_service_filter=total_service_filter,
        )

        return typing.cast(None, jsii.invoke(self, "putGoodTotalRatio", [value]))

    @jsii.member(jsii_name="resetDistributionCut")
    def reset_distribution_cut(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDistributionCut", []))

    @jsii.member(jsii_name="resetGoodTotalRatio")
    def reset_good_total_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoodTotalRatio", []))

    @builtins.property
    @jsii.member(jsii_name="distributionCut")
    def distribution_cut(
        self,
    ) -> GoogleMonitoringSloRequestBasedSliDistributionCutOutputReference:
        return typing.cast(GoogleMonitoringSloRequestBasedSliDistributionCutOutputReference, jsii.get(self, "distributionCut"))

    @builtins.property
    @jsii.member(jsii_name="goodTotalRatio")
    def good_total_ratio(
        self,
    ) -> GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference:
        return typing.cast(GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference, jsii.get(self, "goodTotalRatio"))

    @builtins.property
    @jsii.member(jsii_name="distributionCutInput")
    def distribution_cut_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloRequestBasedSliDistributionCut]:
        return typing.cast(typing.Optional[GoogleMonitoringSloRequestBasedSliDistributionCut], jsii.get(self, "distributionCutInput"))

    @builtins.property
    @jsii.member(jsii_name="goodTotalRatioInput")
    def good_total_ratio_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloRequestBasedSliGoodTotalRatio]:
        return typing.cast(typing.Optional[GoogleMonitoringSloRequestBasedSliGoodTotalRatio], jsii.get(self, "goodTotalRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleMonitoringSloRequestBasedSli]:
        return typing.cast(typing.Optional[GoogleMonitoringSloRequestBasedSli], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloRequestBasedSli],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloRequestBasedSliOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleMonitoringSloTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#create GoogleMonitoringSlo#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#delete GoogleMonitoringSlo#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#update GoogleMonitoringSlo#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#create GoogleMonitoringSlo#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#delete GoogleMonitoringSlo#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#update GoogleMonitoringSlo#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringSloTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringSloTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringSloTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSli",
    jsii_struct_bases=[],
    name_mapping={
        "good_bad_metric_filter": "goodBadMetricFilter",
        "good_total_ratio_threshold": "goodTotalRatioThreshold",
        "metric_mean_in_range": "metricMeanInRange",
        "metric_sum_in_range": "metricSumInRange",
        "window_period": "windowPeriod",
    },
)
class GoogleMonitoringSloWindowsBasedSli:
    def __init__(
        self,
        *,
        good_bad_metric_filter: typing.Optional[builtins.str] = None,
        good_total_ratio_threshold: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold", typing.Dict[str, typing.Any]]] = None,
        metric_mean_in_range: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliMetricMeanInRange", typing.Dict[str, typing.Any]]] = None,
        metric_sum_in_range: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliMetricSumInRange", typing.Dict[str, typing.Any]]] = None,
        window_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param good_bad_metric_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ with ValueType = BOOL. The window is good if any true values appear in the window. One of 'good_bad_metric_filter', 'good_total_ratio_threshold', 'metric_mean_in_range', 'metric_sum_in_range' must be set for 'windows_based_sli'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_bad_metric_filter GoogleMonitoringSlo#good_bad_metric_filter}
        :param good_total_ratio_threshold: good_total_ratio_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio_threshold GoogleMonitoringSlo#good_total_ratio_threshold}
        :param metric_mean_in_range: metric_mean_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#metric_mean_in_range GoogleMonitoringSlo#metric_mean_in_range}
        :param metric_sum_in_range: metric_sum_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#metric_sum_in_range GoogleMonitoringSlo#metric_sum_in_range}
        :param window_period: Duration over which window quality is evaluated, given as a duration string "{X}s" representing X seconds. Must be an integer fraction of a day and at least 60s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#window_period GoogleMonitoringSlo#window_period}
        '''
        if isinstance(good_total_ratio_threshold, dict):
            good_total_ratio_threshold = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold(**good_total_ratio_threshold)
        if isinstance(metric_mean_in_range, dict):
            metric_mean_in_range = GoogleMonitoringSloWindowsBasedSliMetricMeanInRange(**metric_mean_in_range)
        if isinstance(metric_sum_in_range, dict):
            metric_sum_in_range = GoogleMonitoringSloWindowsBasedSliMetricSumInRange(**metric_sum_in_range)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSli.__init__)
            check_type(argname="argument good_bad_metric_filter", value=good_bad_metric_filter, expected_type=type_hints["good_bad_metric_filter"])
            check_type(argname="argument good_total_ratio_threshold", value=good_total_ratio_threshold, expected_type=type_hints["good_total_ratio_threshold"])
            check_type(argname="argument metric_mean_in_range", value=metric_mean_in_range, expected_type=type_hints["metric_mean_in_range"])
            check_type(argname="argument metric_sum_in_range", value=metric_sum_in_range, expected_type=type_hints["metric_sum_in_range"])
            check_type(argname="argument window_period", value=window_period, expected_type=type_hints["window_period"])
        self._values: typing.Dict[str, typing.Any] = {}
        if good_bad_metric_filter is not None:
            self._values["good_bad_metric_filter"] = good_bad_metric_filter
        if good_total_ratio_threshold is not None:
            self._values["good_total_ratio_threshold"] = good_total_ratio_threshold
        if metric_mean_in_range is not None:
            self._values["metric_mean_in_range"] = metric_mean_in_range
        if metric_sum_in_range is not None:
            self._values["metric_sum_in_range"] = metric_sum_in_range
        if window_period is not None:
            self._values["window_period"] = window_period

    @builtins.property
    def good_bad_metric_filter(self) -> typing.Optional[builtins.str]:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ with ValueType = BOOL. The window is good if any true values appear in the window. One of 'good_bad_metric_filter', 'good_total_ratio_threshold', 'metric_mean_in_range', 'metric_sum_in_range' must be set for 'windows_based_sli'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_bad_metric_filter GoogleMonitoringSlo#good_bad_metric_filter}
        '''
        result = self._values.get("good_bad_metric_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def good_total_ratio_threshold(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold"]:
        '''good_total_ratio_threshold block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio_threshold GoogleMonitoringSlo#good_total_ratio_threshold}
        '''
        result = self._values.get("good_total_ratio_threshold")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold"], result)

    @builtins.property
    def metric_mean_in_range(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliMetricMeanInRange"]:
        '''metric_mean_in_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#metric_mean_in_range GoogleMonitoringSlo#metric_mean_in_range}
        '''
        result = self._values.get("metric_mean_in_range")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliMetricMeanInRange"], result)

    @builtins.property
    def metric_sum_in_range(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliMetricSumInRange"]:
        '''metric_sum_in_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#metric_sum_in_range GoogleMonitoringSlo#metric_sum_in_range}
        '''
        result = self._values.get("metric_sum_in_range")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliMetricSumInRange"], result)

    @builtins.property
    def window_period(self) -> typing.Optional[builtins.str]:
        '''Duration over which window quality is evaluated, given as a duration string "{X}s" representing X seconds.

        Must be an
        integer fraction of a day and at least 60s.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#window_period GoogleMonitoringSlo#window_period}
        '''
        result = self._values.get("window_period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSli(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold",
    jsii_struct_bases=[],
    name_mapping={
        "basic_sli_performance": "basicSliPerformance",
        "performance": "performance",
        "threshold": "threshold",
    },
)
class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold:
    def __init__(
        self,
        *,
        basic_sli_performance: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance", typing.Dict[str, typing.Any]]] = None,
        performance: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance", typing.Dict[str, typing.Any]]] = None,
        threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param basic_sli_performance: basic_sli_performance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#basic_sli_performance GoogleMonitoringSlo#basic_sli_performance}
        :param performance: performance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#performance GoogleMonitoringSlo#performance}
        :param threshold: If window performance >= threshold, the window is counted as good. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        if isinstance(basic_sli_performance, dict):
            basic_sli_performance = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance(**basic_sli_performance)
        if isinstance(performance, dict):
            performance = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance(**performance)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold.__init__)
            check_type(argname="argument basic_sli_performance", value=basic_sli_performance, expected_type=type_hints["basic_sli_performance"])
            check_type(argname="argument performance", value=performance, expected_type=type_hints["performance"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
        self._values: typing.Dict[str, typing.Any] = {}
        if basic_sli_performance is not None:
            self._values["basic_sli_performance"] = basic_sli_performance
        if performance is not None:
            self._values["performance"] = performance
        if threshold is not None:
            self._values["threshold"] = threshold

    @builtins.property
    def basic_sli_performance(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance"]:
        '''basic_sli_performance block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#basic_sli_performance GoogleMonitoringSlo#basic_sli_performance}
        '''
        result = self._values.get("basic_sli_performance")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance"], result)

    @builtins.property
    def performance(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance"]:
        '''performance block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#performance GoogleMonitoringSlo#performance}
        '''
        result = self._values.get("performance")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance"], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''If window performance >= threshold, the window is counted as good.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "latency": "latency",
        "location": "location",
        "method": "method",
        "version": "version",
    },
)
class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance:
    def __init__(
        self,
        *,
        availability: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability", typing.Dict[str, typing.Any]]] = None,
        latency: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency", typing.Dict[str, typing.Any]]] = None,
        location: typing.Optional[typing.Sequence[builtins.str]] = None,
        method: typing.Optional[typing.Sequence[builtins.str]] = None,
        version: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param availability: availability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#availability GoogleMonitoringSlo#availability}
        :param latency: latency block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#latency GoogleMonitoringSlo#latency}
        :param location: An optional set of locations to which this SLI is relevant. Telemetry from other locations will not be used to calculate performance for this SLI. If omitted, this SLI applies to all locations in which the Service has activity. For service types that don't support breaking down by location, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#location GoogleMonitoringSlo#location}
        :param method: An optional set of RPCs to which this SLI is relevant. Telemetry from other methods will not be used to calculate performance for this SLI. If omitted, this SLI applies to all the Service's methods. For service types that don't support breaking down by method, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#method GoogleMonitoringSlo#method}
        :param version: The set of API versions to which this SLI is relevant. Telemetry from other API versions will not be used to calculate performance for this SLI. If omitted, this SLI applies to all API versions. For service types that don't support breaking down by version, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#version GoogleMonitoringSlo#version}
        '''
        if isinstance(availability, dict):
            availability = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability(**availability)
        if isinstance(latency, dict):
            latency = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency(**latency)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance.__init__)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument latency", value=latency, expected_type=type_hints["latency"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if latency is not None:
            self._values["latency"] = latency
        if location is not None:
            self._values["location"] = location
        if method is not None:
            self._values["method"] = method
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def availability(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability"]:
        '''availability block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#availability GoogleMonitoringSlo#availability}
        '''
        result = self._values.get("availability")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability"], result)

    @builtins.property
    def latency(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency"]:
        '''latency block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#latency GoogleMonitoringSlo#latency}
        '''
        result = self._values.get("latency")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency"], result)

    @builtins.property
    def location(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional set of locations to which this SLI is relevant.

        Telemetry from other locations will not be used to calculate
        performance for this SLI. If omitted, this SLI applies to all
        locations in which the Service has activity. For service types
        that don't support breaking down by location, setting this
        field will result in an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#location GoogleMonitoringSlo#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional set of RPCs to which this SLI is relevant.

        Telemetry from other methods will not be used to calculate
        performance for this SLI. If omitted, this SLI applies to all
        the Service's methods. For service types that don't support
        breaking down by method, setting this field will result in an
        error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#method GoogleMonitoringSlo#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def version(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of API versions to which this SLI is relevant.

        Telemetry from other API versions will not be used to
        calculate performance for this SLI. If omitted,
        this SLI applies to all API versions. For service types
        that don't support breaking down by version, setting this
        field will result in an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#version GoogleMonitoringSlo#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Whether an availability SLI is enabled or not. Must be set to 'true. Defaults to 'true'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#enabled GoogleMonitoringSlo#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether an availability SLI is enabled or not. Must be set to 'true. Defaults to 'true'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#enabled GoogleMonitoringSlo#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency",
    jsii_struct_bases=[],
    name_mapping={"threshold": "threshold"},
)
class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency:
    def __init__(self, *, threshold: builtins.str) -> None:
        '''
        :param threshold: A duration string, e.g. 10s. Good service is defined to be the count of requests made to this service that return in no more than threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency.__init__)
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "threshold": threshold,
        }

    @builtins.property
    def threshold(self) -> builtins.str:
        '''A duration string, e.g. 10s. Good service is defined to be the count of requests made to this service that return in no more than threshold.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAvailability")
    def put_availability(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Whether an availability SLI is enabled or not. Must be set to 'true. Defaults to 'true'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#enabled GoogleMonitoringSlo#enabled}
        '''
        value = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAvailability", [value]))

    @jsii.member(jsii_name="putLatency")
    def put_latency(self, *, threshold: builtins.str) -> None:
        '''
        :param threshold: A duration string, e.g. 10s. Good service is defined to be the count of requests made to this service that return in no more than threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        value = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency(
            threshold=threshold
        )

        return typing.cast(None, jsii.invoke(self, "putLatency", [value]))

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetLatency")
    def reset_latency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatency", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(
        self,
    ) -> GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityOutputReference:
        return typing.cast(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityOutputReference, jsii.get(self, "availability"))

    @builtins.property
    @jsii.member(jsii_name="latency")
    def latency(
        self,
    ) -> GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyOutputReference:
        return typing.cast(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyOutputReference, jsii.get(self, "latency"))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="latencyInput")
    def latency_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency], jsii.get(self, "latencyInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "location"))

    @location.setter
    def location(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "method"))

    @method.setter
    def method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBasicSliPerformance")
    def put_basic_sli_performance(
        self,
        *,
        availability: typing.Optional[typing.Union[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability, typing.Dict[str, typing.Any]]] = None,
        latency: typing.Optional[typing.Union[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency, typing.Dict[str, typing.Any]]] = None,
        location: typing.Optional[typing.Sequence[builtins.str]] = None,
        method: typing.Optional[typing.Sequence[builtins.str]] = None,
        version: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param availability: availability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#availability GoogleMonitoringSlo#availability}
        :param latency: latency block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#latency GoogleMonitoringSlo#latency}
        :param location: An optional set of locations to which this SLI is relevant. Telemetry from other locations will not be used to calculate performance for this SLI. If omitted, this SLI applies to all locations in which the Service has activity. For service types that don't support breaking down by location, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#location GoogleMonitoringSlo#location}
        :param method: An optional set of RPCs to which this SLI is relevant. Telemetry from other methods will not be used to calculate performance for this SLI. If omitted, this SLI applies to all the Service's methods. For service types that don't support breaking down by method, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#method GoogleMonitoringSlo#method}
        :param version: The set of API versions to which this SLI is relevant. Telemetry from other API versions will not be used to calculate performance for this SLI. If omitted, this SLI applies to all API versions. For service types that don't support breaking down by version, setting this field will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#version GoogleMonitoringSlo#version}
        '''
        value = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance(
            availability=availability,
            latency=latency,
            location=location,
            method=method,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putBasicSliPerformance", [value]))

    @jsii.member(jsii_name="putPerformance")
    def put_performance(
        self,
        *,
        distribution_cut: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut", typing.Dict[str, typing.Any]]] = None,
        good_total_ratio: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param distribution_cut: distribution_cut block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_cut GoogleMonitoringSlo#distribution_cut}
        :param good_total_ratio: good_total_ratio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio GoogleMonitoringSlo#good_total_ratio}
        '''
        value = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance(
            distribution_cut=distribution_cut, good_total_ratio=good_total_ratio
        )

        return typing.cast(None, jsii.invoke(self, "putPerformance", [value]))

    @jsii.member(jsii_name="resetBasicSliPerformance")
    def reset_basic_sli_performance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicSliPerformance", []))

    @jsii.member(jsii_name="resetPerformance")
    def reset_performance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformance", []))

    @jsii.member(jsii_name="resetThreshold")
    def reset_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="basicSliPerformance")
    def basic_sli_performance(
        self,
    ) -> GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference:
        return typing.cast(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference, jsii.get(self, "basicSliPerformance"))

    @builtins.property
    @jsii.member(jsii_name="performance")
    def performance(
        self,
    ) -> "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceOutputReference":
        return typing.cast("GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceOutputReference", jsii.get(self, "performance"))

    @builtins.property
    @jsii.member(jsii_name="basicSliPerformanceInput")
    def basic_sli_performance_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance], jsii.get(self, "basicSliPerformanceInput"))

    @builtins.property
    @jsii.member(jsii_name="performanceInput")
    def performance_input(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance"]:
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance"], jsii.get(self, "performanceInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance",
    jsii_struct_bases=[],
    name_mapping={
        "distribution_cut": "distributionCut",
        "good_total_ratio": "goodTotalRatio",
    },
)
class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance:
    def __init__(
        self,
        *,
        distribution_cut: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut", typing.Dict[str, typing.Any]]] = None,
        good_total_ratio: typing.Optional[typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param distribution_cut: distribution_cut block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_cut GoogleMonitoringSlo#distribution_cut}
        :param good_total_ratio: good_total_ratio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio GoogleMonitoringSlo#good_total_ratio}
        '''
        if isinstance(distribution_cut, dict):
            distribution_cut = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut(**distribution_cut)
        if isinstance(good_total_ratio, dict):
            good_total_ratio = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio(**good_total_ratio)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance.__init__)
            check_type(argname="argument distribution_cut", value=distribution_cut, expected_type=type_hints["distribution_cut"])
            check_type(argname="argument good_total_ratio", value=good_total_ratio, expected_type=type_hints["good_total_ratio"])
        self._values: typing.Dict[str, typing.Any] = {}
        if distribution_cut is not None:
            self._values["distribution_cut"] = distribution_cut
        if good_total_ratio is not None:
            self._values["good_total_ratio"] = good_total_ratio

    @builtins.property
    def distribution_cut(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut"]:
        '''distribution_cut block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_cut GoogleMonitoringSlo#distribution_cut}
        '''
        result = self._values.get("distribution_cut")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut"], result)

    @builtins.property
    def good_total_ratio(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio"]:
        '''good_total_ratio block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_total_ratio GoogleMonitoringSlo#good_total_ratio}
        '''
        result = self._values.get("good_total_ratio")
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut",
    jsii_struct_bases=[],
    name_mapping={"distribution_filter": "distributionFilter", "range": "range"},
)
class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut:
    def __init__(
        self,
        *,
        distribution_filter: builtins.str,
        range: typing.Union["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param distribution_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ aggregating values to quantify the good service provided. Must have ValueType = DISTRIBUTION and MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_filter GoogleMonitoringSlo#distribution_filter}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        '''
        if isinstance(range, dict):
            range = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut.__init__)
            check_type(argname="argument distribution_filter", value=distribution_filter, expected_type=type_hints["distribution_filter"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[str, typing.Any] = {
            "distribution_filter": distribution_filter,
            "range": range,
        }

    @builtins.property
    def distribution_filter(self) -> builtins.str:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ aggregating values to quantify the good service provided.

        Must have ValueType = DISTRIBUTION and
        MetricKind = DELTA or MetricKind = CUMULATIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_filter GoogleMonitoringSlo#distribution_filter}
        '''
        result = self._values.get("distribution_filter")
        assert result is not None, "Required property 'distribution_filter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange":
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        '''
        result = self._values.get("range")
        assert result is not None, "Required property 'range' is missing"
        return typing.cast("GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        :param min: Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        value = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(
        self,
    ) -> "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference":
        return typing.cast("GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="distributionFilterInput")
    def distribution_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange"]:
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="distributionFilter")
    def distribution_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distributionFilter"))

    @distribution_filter.setter
    def distribution_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutOutputReference, "distribution_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributionFilter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        :param min: Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        '''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio",
    jsii_struct_bases=[],
    name_mapping={
        "bad_service_filter": "badServiceFilter",
        "good_service_filter": "goodServiceFilter",
        "total_service_filter": "totalServiceFilter",
    },
)
class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio:
    def __init__(
        self,
        *,
        bad_service_filter: typing.Optional[builtins.str] = None,
        good_service_filter: typing.Optional[builtins.str] = None,
        total_service_filter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bad_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying bad service provided, either demanded service that was not provided or demanded service that was of inadequate quality. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed). Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#bad_service_filter GoogleMonitoringSlo#bad_service_filter}
        :param good_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying good service provided. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed). Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_service_filter GoogleMonitoringSlo#good_service_filter}
        :param total_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying total demanded service. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed). Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#total_service_filter GoogleMonitoringSlo#total_service_filter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio.__init__)
            check_type(argname="argument bad_service_filter", value=bad_service_filter, expected_type=type_hints["bad_service_filter"])
            check_type(argname="argument good_service_filter", value=good_service_filter, expected_type=type_hints["good_service_filter"])
            check_type(argname="argument total_service_filter", value=total_service_filter, expected_type=type_hints["total_service_filter"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bad_service_filter is not None:
            self._values["bad_service_filter"] = bad_service_filter
        if good_service_filter is not None:
            self._values["good_service_filter"] = good_service_filter
        if total_service_filter is not None:
            self._values["total_service_filter"] = total_service_filter

    @builtins.property
    def bad_service_filter(self) -> typing.Optional[builtins.str]:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying bad service provided, either demanded service that was not provided or demanded service that was of inadequate quality. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed).

        Must have ValueType = DOUBLE or ValueType = INT64 and
        must have MetricKind = DELTA or MetricKind = CUMULATIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#bad_service_filter GoogleMonitoringSlo#bad_service_filter}
        '''
        result = self._values.get("bad_service_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def good_service_filter(self) -> typing.Optional[builtins.str]:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying good service provided. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed).

        Must have ValueType = DOUBLE or ValueType = INT64 and
        must have MetricKind = DELTA or MetricKind = CUMULATIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_service_filter GoogleMonitoringSlo#good_service_filter}
        '''
        result = self._values.get("good_service_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def total_service_filter(self) -> typing.Optional[builtins.str]:
        '''A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying total demanded service. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed).

        Must have ValueType = DOUBLE or ValueType = INT64 and
        must have MetricKind = DELTA or MetricKind = CUMULATIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#total_service_filter GoogleMonitoringSlo#total_service_filter}
        '''
        result = self._values.get("total_service_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBadServiceFilter")
    def reset_bad_service_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBadServiceFilter", []))

    @jsii.member(jsii_name="resetGoodServiceFilter")
    def reset_good_service_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoodServiceFilter", []))

    @jsii.member(jsii_name="resetTotalServiceFilter")
    def reset_total_service_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTotalServiceFilter", []))

    @builtins.property
    @jsii.member(jsii_name="badServiceFilterInput")
    def bad_service_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "badServiceFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="goodServiceFilterInput")
    def good_service_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "goodServiceFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="totalServiceFilterInput")
    def total_service_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "totalServiceFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="badServiceFilter")
    def bad_service_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "badServiceFilter"))

    @bad_service_filter.setter
    def bad_service_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference, "bad_service_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "badServiceFilter", value)

    @builtins.property
    @jsii.member(jsii_name="goodServiceFilter")
    def good_service_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "goodServiceFilter"))

    @good_service_filter.setter
    def good_service_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference, "good_service_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "goodServiceFilter", value)

    @builtins.property
    @jsii.member(jsii_name="totalServiceFilter")
    def total_service_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "totalServiceFilter"))

    @total_service_filter.setter
    def total_service_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference, "total_service_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalServiceFilter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDistributionCut")
    def put_distribution_cut(
        self,
        *,
        distribution_filter: builtins.str,
        range: typing.Union[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param distribution_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ aggregating values to quantify the good service provided. Must have ValueType = DISTRIBUTION and MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#distribution_filter GoogleMonitoringSlo#distribution_filter}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        '''
        value = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut(
            distribution_filter=distribution_filter, range=range
        )

        return typing.cast(None, jsii.invoke(self, "putDistributionCut", [value]))

    @jsii.member(jsii_name="putGoodTotalRatio")
    def put_good_total_ratio(
        self,
        *,
        bad_service_filter: typing.Optional[builtins.str] = None,
        good_service_filter: typing.Optional[builtins.str] = None,
        total_service_filter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bad_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying bad service provided, either demanded service that was not provided or demanded service that was of inadequate quality. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed). Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#bad_service_filter GoogleMonitoringSlo#bad_service_filter}
        :param good_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying good service provided. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed). Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#good_service_filter GoogleMonitoringSlo#good_service_filter}
        :param total_service_filter: A TimeSeries `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ quantifying total demanded service. Exactly two of good, bad, or total service filter must be defined (where good + bad = total is assumed). Must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#total_service_filter GoogleMonitoringSlo#total_service_filter}
        '''
        value = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio(
            bad_service_filter=bad_service_filter,
            good_service_filter=good_service_filter,
            total_service_filter=total_service_filter,
        )

        return typing.cast(None, jsii.invoke(self, "putGoodTotalRatio", [value]))

    @jsii.member(jsii_name="resetDistributionCut")
    def reset_distribution_cut(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDistributionCut", []))

    @jsii.member(jsii_name="resetGoodTotalRatio")
    def reset_good_total_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoodTotalRatio", []))

    @builtins.property
    @jsii.member(jsii_name="distributionCut")
    def distribution_cut(
        self,
    ) -> GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutOutputReference:
        return typing.cast(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutOutputReference, jsii.get(self, "distributionCut"))

    @builtins.property
    @jsii.member(jsii_name="goodTotalRatio")
    def good_total_ratio(
        self,
    ) -> GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference:
        return typing.cast(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference, jsii.get(self, "goodTotalRatio"))

    @builtins.property
    @jsii.member(jsii_name="distributionCutInput")
    def distribution_cut_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut], jsii.get(self, "distributionCutInput"))

    @builtins.property
    @jsii.member(jsii_name="goodTotalRatioInput")
    def good_total_ratio_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio], jsii.get(self, "goodTotalRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliMetricMeanInRange",
    jsii_struct_bases=[],
    name_mapping={"range": "range", "time_series": "timeSeries"},
)
class GoogleMonitoringSloWindowsBasedSliMetricMeanInRange:
    def __init__(
        self,
        *,
        range: typing.Union["GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange", typing.Dict[str, typing.Any]],
        time_series: builtins.str,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        :param time_series: A `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ specifying the TimeSeries to use for evaluating window The provided TimeSeries must have ValueType = INT64 or ValueType = DOUBLE and MetricKind = GAUGE. Mean value 'X' should satisfy 'range.min <= X <= range.max' under good service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#time_series GoogleMonitoringSlo#time_series}
        '''
        if isinstance(range, dict):
            range = GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliMetricMeanInRange.__init__)
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument time_series", value=time_series, expected_type=type_hints["time_series"])
        self._values: typing.Dict[str, typing.Any] = {
            "range": range,
            "time_series": time_series,
        }

    @builtins.property
    def range(self) -> "GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange":
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        '''
        result = self._values.get("range")
        assert result is not None, "Required property 'range' is missing"
        return typing.cast("GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange", result)

    @builtins.property
    def time_series(self) -> builtins.str:
        '''A `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ specifying the TimeSeries to use for evaluating window The provided TimeSeries must have ValueType = INT64 or ValueType = DOUBLE and MetricKind = GAUGE. Mean value 'X' should satisfy 'range.min <= X <= range.max' under good service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#time_series GoogleMonitoringSlo#time_series}
        '''
        result = self._values.get("time_series")
        assert result is not None, "Required property 'time_series' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliMetricMeanInRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        :param min: Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        value = GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(
        self,
    ) -> "GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference":
        return typing.cast("GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange"]:
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeSeriesInput")
    def time_series_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeSeriesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeSeries")
    def time_series(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeSeries"))

    @time_series.setter
    def time_series(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeOutputReference, "time_series").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeSeries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricMeanInRange]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricMeanInRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricMeanInRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        :param min: Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        '''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliMetricSumInRange",
    jsii_struct_bases=[],
    name_mapping={"range": "range", "time_series": "timeSeries"},
)
class GoogleMonitoringSloWindowsBasedSliMetricSumInRange:
    def __init__(
        self,
        *,
        range: typing.Union["GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange", typing.Dict[str, typing.Any]],
        time_series: builtins.str,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        :param time_series: A `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ specifying the TimeSeries to use for evaluating window quality. The provided TimeSeries must have ValueType = INT64 or ValueType = DOUBLE and MetricKind = GAUGE. Summed value 'X' should satisfy 'range.min <= X <= range.max' for a good window. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#time_series GoogleMonitoringSlo#time_series}
        '''
        if isinstance(range, dict):
            range = GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliMetricSumInRange.__init__)
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument time_series", value=time_series, expected_type=type_hints["time_series"])
        self._values: typing.Dict[str, typing.Any] = {
            "range": range,
            "time_series": time_series,
        }

    @builtins.property
    def range(self) -> "GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange":
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        '''
        result = self._values.get("range")
        assert result is not None, "Required property 'range' is missing"
        return typing.cast("GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange", result)

    @builtins.property
    def time_series(self) -> builtins.str:
        '''A `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ specifying the TimeSeries to use for evaluating window quality. The provided TimeSeries must have ValueType = INT64 or ValueType = DOUBLE and MetricKind = GAUGE.

        Summed value 'X' should satisfy
        'range.min <= X <= range.max' for a good window.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#time_series GoogleMonitoringSlo#time_series}
        '''
        result = self._values.get("time_series")
        assert result is not None, "Required property 'time_series' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliMetricSumInRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliMetricSumInRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliMetricSumInRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        :param min: Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        value = GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(
        self,
    ) -> "GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference":
        return typing.cast("GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange"]:
        return typing.cast(typing.Optional["GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeSeriesInput")
    def time_series_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeSeriesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeSeries")
    def time_series(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeSeries"))

    @time_series.setter
    def time_series(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeOutputReference, "time_series").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeSeries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricSumInRange]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricSumInRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricSumInRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        :param min: Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''max value for the range (inclusive). If not given, will be set to "infinity", defining an open range ">= range.min".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#max GoogleMonitoringSlo#max}
        '''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Min value for the range (inclusive). If not given, will be set to "-infinity", defining an open range "< range.max".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#min GoogleMonitoringSlo#min}
        '''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringSloWindowsBasedSliOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringSlo.GoogleMonitoringSloWindowsBasedSliOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringSloWindowsBasedSliOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGoodTotalRatioThreshold")
    def put_good_total_ratio_threshold(
        self,
        *,
        basic_sli_performance: typing.Optional[typing.Union[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance, typing.Dict[str, typing.Any]]] = None,
        performance: typing.Optional[typing.Union[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance, typing.Dict[str, typing.Any]]] = None,
        threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param basic_sli_performance: basic_sli_performance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#basic_sli_performance GoogleMonitoringSlo#basic_sli_performance}
        :param performance: performance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#performance GoogleMonitoringSlo#performance}
        :param threshold: If window performance >= threshold, the window is counted as good. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#threshold GoogleMonitoringSlo#threshold}
        '''
        value = GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold(
            basic_sli_performance=basic_sli_performance,
            performance=performance,
            threshold=threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putGoodTotalRatioThreshold", [value]))

    @jsii.member(jsii_name="putMetricMeanInRange")
    def put_metric_mean_in_range(
        self,
        *,
        range: typing.Union[GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange, typing.Dict[str, typing.Any]],
        time_series: builtins.str,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        :param time_series: A `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ specifying the TimeSeries to use for evaluating window The provided TimeSeries must have ValueType = INT64 or ValueType = DOUBLE and MetricKind = GAUGE. Mean value 'X' should satisfy 'range.min <= X <= range.max' under good service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#time_series GoogleMonitoringSlo#time_series}
        '''
        value = GoogleMonitoringSloWindowsBasedSliMetricMeanInRange(
            range=range, time_series=time_series
        )

        return typing.cast(None, jsii.invoke(self, "putMetricMeanInRange", [value]))

    @jsii.member(jsii_name="putMetricSumInRange")
    def put_metric_sum_in_range(
        self,
        *,
        range: typing.Union[GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange, typing.Dict[str, typing.Any]],
        time_series: builtins.str,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#range GoogleMonitoringSlo#range}
        :param time_series: A `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`_ specifying the TimeSeries to use for evaluating window quality. The provided TimeSeries must have ValueType = INT64 or ValueType = DOUBLE and MetricKind = GAUGE. Summed value 'X' should satisfy 'range.min <= X <= range.max' for a good window. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_slo#time_series GoogleMonitoringSlo#time_series}
        '''
        value = GoogleMonitoringSloWindowsBasedSliMetricSumInRange(
            range=range, time_series=time_series
        )

        return typing.cast(None, jsii.invoke(self, "putMetricSumInRange", [value]))

    @jsii.member(jsii_name="resetGoodBadMetricFilter")
    def reset_good_bad_metric_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoodBadMetricFilter", []))

    @jsii.member(jsii_name="resetGoodTotalRatioThreshold")
    def reset_good_total_ratio_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoodTotalRatioThreshold", []))

    @jsii.member(jsii_name="resetMetricMeanInRange")
    def reset_metric_mean_in_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricMeanInRange", []))

    @jsii.member(jsii_name="resetMetricSumInRange")
    def reset_metric_sum_in_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricSumInRange", []))

    @jsii.member(jsii_name="resetWindowPeriod")
    def reset_window_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowPeriod", []))

    @builtins.property
    @jsii.member(jsii_name="goodTotalRatioThreshold")
    def good_total_ratio_threshold(
        self,
    ) -> GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdOutputReference:
        return typing.cast(GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdOutputReference, jsii.get(self, "goodTotalRatioThreshold"))

    @builtins.property
    @jsii.member(jsii_name="metricMeanInRange")
    def metric_mean_in_range(
        self,
    ) -> GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeOutputReference:
        return typing.cast(GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeOutputReference, jsii.get(self, "metricMeanInRange"))

    @builtins.property
    @jsii.member(jsii_name="metricSumInRange")
    def metric_sum_in_range(
        self,
    ) -> GoogleMonitoringSloWindowsBasedSliMetricSumInRangeOutputReference:
        return typing.cast(GoogleMonitoringSloWindowsBasedSliMetricSumInRangeOutputReference, jsii.get(self, "metricSumInRange"))

    @builtins.property
    @jsii.member(jsii_name="goodBadMetricFilterInput")
    def good_bad_metric_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "goodBadMetricFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="goodTotalRatioThresholdInput")
    def good_total_ratio_threshold_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold], jsii.get(self, "goodTotalRatioThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="metricMeanInRangeInput")
    def metric_mean_in_range_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricMeanInRange]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricMeanInRange], jsii.get(self, "metricMeanInRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="metricSumInRangeInput")
    def metric_sum_in_range_input(
        self,
    ) -> typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricSumInRange]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSliMetricSumInRange], jsii.get(self, "metricSumInRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="windowPeriodInput")
    def window_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="goodBadMetricFilter")
    def good_bad_metric_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "goodBadMetricFilter"))

    @good_bad_metric_filter.setter
    def good_bad_metric_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliOutputReference, "good_bad_metric_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "goodBadMetricFilter", value)

    @builtins.property
    @jsii.member(jsii_name="windowPeriod")
    def window_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowPeriod"))

    @window_period.setter
    def window_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliOutputReference, "window_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleMonitoringSloWindowsBasedSli]:
        return typing.cast(typing.Optional[GoogleMonitoringSloWindowsBasedSli], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringSloWindowsBasedSli],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringSloWindowsBasedSliOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleMonitoringSlo",
    "GoogleMonitoringSloBasicSli",
    "GoogleMonitoringSloBasicSliAvailability",
    "GoogleMonitoringSloBasicSliAvailabilityOutputReference",
    "GoogleMonitoringSloBasicSliLatency",
    "GoogleMonitoringSloBasicSliLatencyOutputReference",
    "GoogleMonitoringSloBasicSliOutputReference",
    "GoogleMonitoringSloConfig",
    "GoogleMonitoringSloRequestBasedSli",
    "GoogleMonitoringSloRequestBasedSliDistributionCut",
    "GoogleMonitoringSloRequestBasedSliDistributionCutOutputReference",
    "GoogleMonitoringSloRequestBasedSliDistributionCutRange",
    "GoogleMonitoringSloRequestBasedSliDistributionCutRangeOutputReference",
    "GoogleMonitoringSloRequestBasedSliGoodTotalRatio",
    "GoogleMonitoringSloRequestBasedSliGoodTotalRatioOutputReference",
    "GoogleMonitoringSloRequestBasedSliOutputReference",
    "GoogleMonitoringSloTimeouts",
    "GoogleMonitoringSloTimeoutsOutputReference",
    "GoogleMonitoringSloWindowsBasedSli",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThreshold",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityOutputReference",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyOutputReference",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceOutputReference",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdOutputReference",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformance",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutOutputReference",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeOutputReference",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioOutputReference",
    "GoogleMonitoringSloWindowsBasedSliGoodTotalRatioThresholdPerformanceOutputReference",
    "GoogleMonitoringSloWindowsBasedSliMetricMeanInRange",
    "GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeOutputReference",
    "GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRange",
    "GoogleMonitoringSloWindowsBasedSliMetricMeanInRangeRangeOutputReference",
    "GoogleMonitoringSloWindowsBasedSliMetricSumInRange",
    "GoogleMonitoringSloWindowsBasedSliMetricSumInRangeOutputReference",
    "GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRange",
    "GoogleMonitoringSloWindowsBasedSliMetricSumInRangeRangeOutputReference",
    "GoogleMonitoringSloWindowsBasedSliOutputReference",
]

publication.publish()
