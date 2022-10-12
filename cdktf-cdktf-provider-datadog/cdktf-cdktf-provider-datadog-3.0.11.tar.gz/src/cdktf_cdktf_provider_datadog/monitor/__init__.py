'''
# `datadog_monitor`

Refer to the Terraform Registory for docs: [`datadog_monitor`](https://www.terraform.io/docs/providers/datadog/r/monitor).
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


class Monitor(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.Monitor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/monitor datadog_monitor}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        message: builtins.str,
        name: builtins.str,
        query: builtins.str,
        type: builtins.str,
        enable_logs_sample: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        escalation_message: typing.Optional[builtins.str] = None,
        evaluation_delay: typing.Optional[jsii.Number] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        groupby_simple_monitor: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        group_retention_duration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        include_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        locked: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        monitor_thresholds: typing.Optional[typing.Union["MonitorMonitorThresholds", typing.Dict[str, typing.Any]]] = None,
        monitor_threshold_windows: typing.Optional[typing.Union["MonitorMonitorThresholdWindows", typing.Dict[str, typing.Any]]] = None,
        new_group_delay: typing.Optional[jsii.Number] = None,
        new_host_delay: typing.Optional[jsii.Number] = None,
        no_data_timeframe: typing.Optional[jsii.Number] = None,
        notify_audit: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notify_no_data: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        on_missing_data: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        renotify_interval: typing.Optional[jsii.Number] = None,
        renotify_occurrences: typing.Optional[jsii.Number] = None,
        renotify_statuses: typing.Optional[typing.Sequence[builtins.str]] = None,
        require_full_window: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restricted_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeout_h: typing.Optional[jsii.Number] = None,
        validate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        variables: typing.Optional[typing.Union["MonitorVariables", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/monitor datadog_monitor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param message: A message to include with notifications for this monitor. Email notifications can be sent to specific users by using the same ``@username`` notation as events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#message Monitor#message}
        :param name: Name of Datadog monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#name Monitor#name}
        :param query: The monitor query to notify on. Note this is not the same query you see in the UI and the syntax is different depending on the monitor type, please see the `API Reference <https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor>`_ for details. ``terraform plan`` will validate query contents unless ``validate`` is set to ``false``. *Note:** APM latency data is now available as Distribution Metrics. Existing monitors have been migrated automatically but all terraformed monitors can still use the existing metrics. We strongly recommend updating monitor definitions to query the new metrics. To learn more, or to see examples of how to update your terraform definitions to utilize the new distribution metrics, see the `detailed doc <https://docs.datadoghq.com/tracing/guide/ddsketch_trace_metrics/>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#query Monitor#query}
        :param type: The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API `documentation page <https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor>`_. Note: The monitor type cannot be changed after a monitor is created. Valid values are ``composite``, ``event alert``, ``log alert``, ``metric alert``, ``process alert``, ``query alert``, ``rum alert``, ``service check``, ``synthetics alert``, ``trace-analytics alert``, ``slo alert``, ``event-v2 alert``, ``audit alert``, ``ci-pipelines alert``, ``ci-tests alert``, ``error-tracking alert``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#type Monitor#type}
        :param enable_logs_sample: A boolean indicating whether or not to include a list of log values which triggered the alert. This is only used by log monitors. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#enable_logs_sample Monitor#enable_logs_sample}
        :param escalation_message: A message to include with a re-notification. Supports the ``@username`` notification allowed elsewhere. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#escalation_message Monitor#escalation_message}
        :param evaluation_delay: (Only applies to metric alert) Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to ``300`` (5min), the ``timeframe`` is set to ``last_5m`` and the time is 7:00, the monitor will evaluate data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor will always have data during evaluation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#evaluation_delay Monitor#evaluation_delay}
        :param force_delete: A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO, composite monitor). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#force_delete Monitor#force_delete}
        :param groupby_simple_monitor: Whether or not to trigger one alert if any source breaches a threshold. This is only used by log monitors. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#groupby_simple_monitor Monitor#groupby_simple_monitor}
        :param group_retention_duration: The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: 60m, 1h, and 2d. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#group_retention_duration Monitor#group_retention_duration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#id Monitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_tags: A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#include_tags Monitor#include_tags}
        :param locked: A boolean indicating whether changes to this monitor should be restricted to the creator or admins. Defaults to ``false``. **Deprecated.** Use ``restricted_roles``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#locked Monitor#locked}
        :param monitor_thresholds: monitor_thresholds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#monitor_thresholds Monitor#monitor_thresholds}
        :param monitor_threshold_windows: monitor_threshold_windows block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#monitor_threshold_windows Monitor#monitor_threshold_windows}
        :param new_group_delay: The time (in seconds) to skip evaluations for new groups. ``new_group_delay`` overrides ``new_host_delay`` if it is set to a nonzero value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#new_group_delay Monitor#new_group_delay}
        :param new_host_delay: **Deprecated**. See ``new_group_delay``. Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non-negative integer. This value is ignored for simple monitors and monitors not grouped by host. Defaults to ``300``. The only case when this should be used is to override the default and set ``new_host_delay`` to zero for monitors grouped by host. **Deprecated.** Use ``new_group_delay`` except when setting ``new_host_delay`` to zero. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#new_host_delay Monitor#new_host_delay}
        :param no_data_timeframe: The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes. We recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#no_data_timeframe Monitor#no_data_timeframe}
        :param notify_audit: A boolean indicating whether tagged users will be notified on changes to this monitor. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#notify_audit Monitor#notify_audit}
        :param notify_no_data: A boolean indicating whether this monitor will notify when data stops reporting. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#notify_no_data Monitor#notify_no_data}
        :param on_missing_data: Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using ``Count`` queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than ``Count``, for example ``Gauge``, ``Measure``, or ``Rate``, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Valid values are: ``show_no_data``, ``show_and_notify_no_data``, ``resolve``, and ``default``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#on_missing_data Monitor#on_missing_data}
        :param priority: Integer from 1 (high) to 5 (low) indicating alert severity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#priority Monitor#priority}
        :param renotify_interval: The number of minutes after the last notification before a monitor will re-notify on the current status. It will only re-notify if it's not resolved. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_interval Monitor#renotify_interval}
        :param renotify_occurrences: The number of re-notification messages that should be sent on the current status. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_occurrences Monitor#renotify_occurrences}
        :param renotify_statuses: The types of statuses for which re-notification messages should be sent. Valid values are ``alert``, ``warn``, ``no data``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_statuses Monitor#renotify_statuses}
        :param require_full_window: A boolean indicating whether this monitor needs a full window of data before it's evaluated. We highly recommend you set this to ``false`` for sparse metrics, otherwise some evaluations will be skipped. Default: ``true`` for ``on average``, ``at all times`` and ``in total`` aggregation. ``false`` otherwise. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#require_full_window Monitor#require_full_window}
        :param restricted_roles: A list of unique role identifiers to define which roles are allowed to edit the monitor. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. Roles unique identifiers can be pulled from the `Roles API <https://docs.datadoghq.com/api/latest/roles/#list-roles>`_ in the ``data.id`` field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#restricted_roles Monitor#restricted_roles}
        :param tags: A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it's not currently possible to filter by these tags when querying via the API Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#tags Monitor#tags}
        :param timeout_h: The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#timeout_h Monitor#timeout_h}
        :param validate: If set to ``false``, skip the validation call done during plan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#validate Monitor#validate}
        :param variables: variables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#variables Monitor#variables}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Monitor.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorConfig(
            message=message,
            name=name,
            query=query,
            type=type,
            enable_logs_sample=enable_logs_sample,
            escalation_message=escalation_message,
            evaluation_delay=evaluation_delay,
            force_delete=force_delete,
            groupby_simple_monitor=groupby_simple_monitor,
            group_retention_duration=group_retention_duration,
            id=id,
            include_tags=include_tags,
            locked=locked,
            monitor_thresholds=monitor_thresholds,
            monitor_threshold_windows=monitor_threshold_windows,
            new_group_delay=new_group_delay,
            new_host_delay=new_host_delay,
            no_data_timeframe=no_data_timeframe,
            notify_audit=notify_audit,
            notify_no_data=notify_no_data,
            on_missing_data=on_missing_data,
            priority=priority,
            renotify_interval=renotify_interval,
            renotify_occurrences=renotify_occurrences,
            renotify_statuses=renotify_statuses,
            require_full_window=require_full_window,
            restricted_roles=restricted_roles,
            tags=tags,
            timeout_h=timeout_h,
            validate=validate,
            variables=variables,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMonitorThresholds")
    def put_monitor_thresholds(
        self,
        *,
        critical: typing.Optional[builtins.str] = None,
        critical_recovery: typing.Optional[builtins.str] = None,
        ok: typing.Optional[builtins.str] = None,
        unknown: typing.Optional[builtins.str] = None,
        warning: typing.Optional[builtins.str] = None,
        warning_recovery: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param critical: The monitor ``CRITICAL`` threshold. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#critical Monitor#critical}
        :param critical_recovery: The monitor ``CRITICAL`` recovery threshold. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#critical_recovery Monitor#critical_recovery}
        :param ok: The monitor ``OK`` threshold. Only supported in monitor type ``service check``. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#ok Monitor#ok}
        :param unknown: The monitor ``UNKNOWN`` threshold. Only supported in monitor type ``service check``. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#unknown Monitor#unknown}
        :param warning: The monitor ``WARNING`` threshold. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#warning Monitor#warning}
        :param warning_recovery: The monitor ``WARNING`` recovery threshold. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#warning_recovery Monitor#warning_recovery}
        '''
        value = MonitorMonitorThresholds(
            critical=critical,
            critical_recovery=critical_recovery,
            ok=ok,
            unknown=unknown,
            warning=warning,
            warning_recovery=warning_recovery,
        )

        return typing.cast(None, jsii.invoke(self, "putMonitorThresholds", [value]))

    @jsii.member(jsii_name="putMonitorThresholdWindows")
    def put_monitor_threshold_windows(
        self,
        *,
        recovery_window: typing.Optional[builtins.str] = None,
        trigger_window: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recovery_window: Describes how long an anomalous metric must be normal before the alert recovers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#recovery_window Monitor#recovery_window}
        :param trigger_window: Describes how long a metric must be anomalous before an alert triggers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#trigger_window Monitor#trigger_window}
        '''
        value = MonitorMonitorThresholdWindows(
            recovery_window=recovery_window, trigger_window=trigger_window
        )

        return typing.cast(None, jsii.invoke(self, "putMonitorThresholdWindows", [value]))

    @jsii.member(jsii_name="putVariables")
    def put_variables(
        self,
        *,
        event_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorVariablesEventQuery", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param event_query: event_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#event_query Monitor#event_query}
        '''
        value = MonitorVariables(event_query=event_query)

        return typing.cast(None, jsii.invoke(self, "putVariables", [value]))

    @jsii.member(jsii_name="resetEnableLogsSample")
    def reset_enable_logs_sample(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLogsSample", []))

    @jsii.member(jsii_name="resetEscalationMessage")
    def reset_escalation_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEscalationMessage", []))

    @jsii.member(jsii_name="resetEvaluationDelay")
    def reset_evaluation_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationDelay", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetGroupbySimpleMonitor")
    def reset_groupby_simple_monitor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupbySimpleMonitor", []))

    @jsii.member(jsii_name="resetGroupRetentionDuration")
    def reset_group_retention_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupRetentionDuration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncludeTags")
    def reset_include_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTags", []))

    @jsii.member(jsii_name="resetLocked")
    def reset_locked(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocked", []))

    @jsii.member(jsii_name="resetMonitorThresholds")
    def reset_monitor_thresholds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorThresholds", []))

    @jsii.member(jsii_name="resetMonitorThresholdWindows")
    def reset_monitor_threshold_windows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorThresholdWindows", []))

    @jsii.member(jsii_name="resetNewGroupDelay")
    def reset_new_group_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewGroupDelay", []))

    @jsii.member(jsii_name="resetNewHostDelay")
    def reset_new_host_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewHostDelay", []))

    @jsii.member(jsii_name="resetNoDataTimeframe")
    def reset_no_data_timeframe(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoDataTimeframe", []))

    @jsii.member(jsii_name="resetNotifyAudit")
    def reset_notify_audit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyAudit", []))

    @jsii.member(jsii_name="resetNotifyNoData")
    def reset_notify_no_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyNoData", []))

    @jsii.member(jsii_name="resetOnMissingData")
    def reset_on_missing_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnMissingData", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetRenotifyInterval")
    def reset_renotify_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenotifyInterval", []))

    @jsii.member(jsii_name="resetRenotifyOccurrences")
    def reset_renotify_occurrences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenotifyOccurrences", []))

    @jsii.member(jsii_name="resetRenotifyStatuses")
    def reset_renotify_statuses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenotifyStatuses", []))

    @jsii.member(jsii_name="resetRequireFullWindow")
    def reset_require_full_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireFullWindow", []))

    @jsii.member(jsii_name="resetRestrictedRoles")
    def reset_restricted_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictedRoles", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeoutH")
    def reset_timeout_h(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutH", []))

    @jsii.member(jsii_name="resetValidate")
    def reset_validate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidate", []))

    @jsii.member(jsii_name="resetVariables")
    def reset_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariables", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="monitorThresholds")
    def monitor_thresholds(self) -> "MonitorMonitorThresholdsOutputReference":
        return typing.cast("MonitorMonitorThresholdsOutputReference", jsii.get(self, "monitorThresholds"))

    @builtins.property
    @jsii.member(jsii_name="monitorThresholdWindows")
    def monitor_threshold_windows(
        self,
    ) -> "MonitorMonitorThresholdWindowsOutputReference":
        return typing.cast("MonitorMonitorThresholdWindowsOutputReference", jsii.get(self, "monitorThresholdWindows"))

    @builtins.property
    @jsii.member(jsii_name="variables")
    def variables(self) -> "MonitorVariablesOutputReference":
        return typing.cast("MonitorVariablesOutputReference", jsii.get(self, "variables"))

    @builtins.property
    @jsii.member(jsii_name="enableLogsSampleInput")
    def enable_logs_sample_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLogsSampleInput"))

    @builtins.property
    @jsii.member(jsii_name="escalationMessageInput")
    def escalation_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "escalationMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationDelayInput")
    def evaluation_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="groupbySimpleMonitorInput")
    def groupby_simple_monitor_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "groupbySimpleMonitorInput"))

    @builtins.property
    @jsii.member(jsii_name="groupRetentionDurationInput")
    def group_retention_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupRetentionDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTagsInput")
    def include_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="lockedInput")
    def locked_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "lockedInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorThresholdsInput")
    def monitor_thresholds_input(self) -> typing.Optional["MonitorMonitorThresholds"]:
        return typing.cast(typing.Optional["MonitorMonitorThresholds"], jsii.get(self, "monitorThresholdsInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorThresholdWindowsInput")
    def monitor_threshold_windows_input(
        self,
    ) -> typing.Optional["MonitorMonitorThresholdWindows"]:
        return typing.cast(typing.Optional["MonitorMonitorThresholdWindows"], jsii.get(self, "monitorThresholdWindowsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="newGroupDelayInput")
    def new_group_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "newGroupDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="newHostDelayInput")
    def new_host_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "newHostDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="noDataTimeframeInput")
    def no_data_timeframe_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "noDataTimeframeInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyAuditInput")
    def notify_audit_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifyAuditInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyNoDataInput")
    def notify_no_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifyNoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="onMissingDataInput")
    def on_missing_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onMissingDataInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="renotifyIntervalInput")
    def renotify_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "renotifyIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="renotifyOccurrencesInput")
    def renotify_occurrences_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "renotifyOccurrencesInput"))

    @builtins.property
    @jsii.member(jsii_name="renotifyStatusesInput")
    def renotify_statuses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "renotifyStatusesInput"))

    @builtins.property
    @jsii.member(jsii_name="requireFullWindowInput")
    def require_full_window_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireFullWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictedRolesInput")
    def restricted_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "restrictedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutHInput")
    def timeout_h_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutHInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="validateInput")
    def validate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "validateInput"))

    @builtins.property
    @jsii.member(jsii_name="variablesInput")
    def variables_input(self) -> typing.Optional["MonitorVariables"]:
        return typing.cast(typing.Optional["MonitorVariables"], jsii.get(self, "variablesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLogsSample")
    def enable_logs_sample(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLogsSample"))

    @enable_logs_sample.setter
    def enable_logs_sample(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "enable_logs_sample").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogsSample", value)

    @builtins.property
    @jsii.member(jsii_name="escalationMessage")
    def escalation_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "escalationMessage"))

    @escalation_message.setter
    def escalation_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "escalation_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "escalationMessage", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationDelay")
    def evaluation_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationDelay"))

    @evaluation_delay.setter
    def evaluation_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "evaluation_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationDelay", value)

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "force_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="groupbySimpleMonitor")
    def groupby_simple_monitor(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "groupbySimpleMonitor"))

    @groupby_simple_monitor.setter
    def groupby_simple_monitor(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "groupby_simple_monitor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupbySimpleMonitor", value)

    @builtins.property
    @jsii.member(jsii_name="groupRetentionDuration")
    def group_retention_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupRetentionDuration"))

    @group_retention_duration.setter
    def group_retention_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "group_retention_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupRetentionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="includeTags")
    def include_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeTags"))

    @include_tags.setter
    def include_tags(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "include_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTags", value)

    @builtins.property
    @jsii.member(jsii_name="locked")
    def locked(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "locked"))

    @locked.setter
    def locked(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "locked").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locked", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="newGroupDelay")
    def new_group_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "newGroupDelay"))

    @new_group_delay.setter
    def new_group_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "new_group_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newGroupDelay", value)

    @builtins.property
    @jsii.member(jsii_name="newHostDelay")
    def new_host_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "newHostDelay"))

    @new_host_delay.setter
    def new_host_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "new_host_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newHostDelay", value)

    @builtins.property
    @jsii.member(jsii_name="noDataTimeframe")
    def no_data_timeframe(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "noDataTimeframe"))

    @no_data_timeframe.setter
    def no_data_timeframe(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "no_data_timeframe").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDataTimeframe", value)

    @builtins.property
    @jsii.member(jsii_name="notifyAudit")
    def notify_audit(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notifyAudit"))

    @notify_audit.setter
    def notify_audit(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "notify_audit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyAudit", value)

    @builtins.property
    @jsii.member(jsii_name="notifyNoData")
    def notify_no_data(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notifyNoData"))

    @notify_no_data.setter
    def notify_no_data(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "notify_no_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyNoData", value)

    @builtins.property
    @jsii.member(jsii_name="onMissingData")
    def on_missing_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onMissingData"))

    @on_missing_data.setter
    def on_missing_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "on_missing_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onMissingData", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="renotifyInterval")
    def renotify_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "renotifyInterval"))

    @renotify_interval.setter
    def renotify_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "renotify_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renotifyInterval", value)

    @builtins.property
    @jsii.member(jsii_name="renotifyOccurrences")
    def renotify_occurrences(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "renotifyOccurrences"))

    @renotify_occurrences.setter
    def renotify_occurrences(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "renotify_occurrences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renotifyOccurrences", value)

    @builtins.property
    @jsii.member(jsii_name="renotifyStatuses")
    def renotify_statuses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "renotifyStatuses"))

    @renotify_statuses.setter
    def renotify_statuses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "renotify_statuses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renotifyStatuses", value)

    @builtins.property
    @jsii.member(jsii_name="requireFullWindow")
    def require_full_window(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireFullWindow"))

    @require_full_window.setter
    def require_full_window(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "require_full_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireFullWindow", value)

    @builtins.property
    @jsii.member(jsii_name="restrictedRoles")
    def restricted_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "restrictedRoles"))

    @restricted_roles.setter
    def restricted_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "restricted_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutH")
    def timeout_h(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutH"))

    @timeout_h.setter
    def timeout_h(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "timeout_h").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutH", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="validate")
    def validate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "validate"))

    @validate.setter
    def validate(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Monitor, "validate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validate", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "message": "message",
        "name": "name",
        "query": "query",
        "type": "type",
        "enable_logs_sample": "enableLogsSample",
        "escalation_message": "escalationMessage",
        "evaluation_delay": "evaluationDelay",
        "force_delete": "forceDelete",
        "groupby_simple_monitor": "groupbySimpleMonitor",
        "group_retention_duration": "groupRetentionDuration",
        "id": "id",
        "include_tags": "includeTags",
        "locked": "locked",
        "monitor_thresholds": "monitorThresholds",
        "monitor_threshold_windows": "monitorThresholdWindows",
        "new_group_delay": "newGroupDelay",
        "new_host_delay": "newHostDelay",
        "no_data_timeframe": "noDataTimeframe",
        "notify_audit": "notifyAudit",
        "notify_no_data": "notifyNoData",
        "on_missing_data": "onMissingData",
        "priority": "priority",
        "renotify_interval": "renotifyInterval",
        "renotify_occurrences": "renotifyOccurrences",
        "renotify_statuses": "renotifyStatuses",
        "require_full_window": "requireFullWindow",
        "restricted_roles": "restrictedRoles",
        "tags": "tags",
        "timeout_h": "timeoutH",
        "validate": "validate",
        "variables": "variables",
    },
)
class MonitorConfig(cdktf.TerraformMetaArguments):
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
        message: builtins.str,
        name: builtins.str,
        query: builtins.str,
        type: builtins.str,
        enable_logs_sample: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        escalation_message: typing.Optional[builtins.str] = None,
        evaluation_delay: typing.Optional[jsii.Number] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        groupby_simple_monitor: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        group_retention_duration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        include_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        locked: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        monitor_thresholds: typing.Optional[typing.Union["MonitorMonitorThresholds", typing.Dict[str, typing.Any]]] = None,
        monitor_threshold_windows: typing.Optional[typing.Union["MonitorMonitorThresholdWindows", typing.Dict[str, typing.Any]]] = None,
        new_group_delay: typing.Optional[jsii.Number] = None,
        new_host_delay: typing.Optional[jsii.Number] = None,
        no_data_timeframe: typing.Optional[jsii.Number] = None,
        notify_audit: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notify_no_data: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        on_missing_data: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        renotify_interval: typing.Optional[jsii.Number] = None,
        renotify_occurrences: typing.Optional[jsii.Number] = None,
        renotify_statuses: typing.Optional[typing.Sequence[builtins.str]] = None,
        require_full_window: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restricted_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeout_h: typing.Optional[jsii.Number] = None,
        validate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        variables: typing.Optional[typing.Union["MonitorVariables", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param message: A message to include with notifications for this monitor. Email notifications can be sent to specific users by using the same ``@username`` notation as events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#message Monitor#message}
        :param name: Name of Datadog monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#name Monitor#name}
        :param query: The monitor query to notify on. Note this is not the same query you see in the UI and the syntax is different depending on the monitor type, please see the `API Reference <https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor>`_ for details. ``terraform plan`` will validate query contents unless ``validate`` is set to ``false``. *Note:** APM latency data is now available as Distribution Metrics. Existing monitors have been migrated automatically but all terraformed monitors can still use the existing metrics. We strongly recommend updating monitor definitions to query the new metrics. To learn more, or to see examples of how to update your terraform definitions to utilize the new distribution metrics, see the `detailed doc <https://docs.datadoghq.com/tracing/guide/ddsketch_trace_metrics/>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#query Monitor#query}
        :param type: The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API `documentation page <https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor>`_. Note: The monitor type cannot be changed after a monitor is created. Valid values are ``composite``, ``event alert``, ``log alert``, ``metric alert``, ``process alert``, ``query alert``, ``rum alert``, ``service check``, ``synthetics alert``, ``trace-analytics alert``, ``slo alert``, ``event-v2 alert``, ``audit alert``, ``ci-pipelines alert``, ``ci-tests alert``, ``error-tracking alert``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#type Monitor#type}
        :param enable_logs_sample: A boolean indicating whether or not to include a list of log values which triggered the alert. This is only used by log monitors. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#enable_logs_sample Monitor#enable_logs_sample}
        :param escalation_message: A message to include with a re-notification. Supports the ``@username`` notification allowed elsewhere. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#escalation_message Monitor#escalation_message}
        :param evaluation_delay: (Only applies to metric alert) Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to ``300`` (5min), the ``timeframe`` is set to ``last_5m`` and the time is 7:00, the monitor will evaluate data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor will always have data during evaluation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#evaluation_delay Monitor#evaluation_delay}
        :param force_delete: A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO, composite monitor). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#force_delete Monitor#force_delete}
        :param groupby_simple_monitor: Whether or not to trigger one alert if any source breaches a threshold. This is only used by log monitors. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#groupby_simple_monitor Monitor#groupby_simple_monitor}
        :param group_retention_duration: The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: 60m, 1h, and 2d. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#group_retention_duration Monitor#group_retention_duration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#id Monitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_tags: A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#include_tags Monitor#include_tags}
        :param locked: A boolean indicating whether changes to this monitor should be restricted to the creator or admins. Defaults to ``false``. **Deprecated.** Use ``restricted_roles``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#locked Monitor#locked}
        :param monitor_thresholds: monitor_thresholds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#monitor_thresholds Monitor#monitor_thresholds}
        :param monitor_threshold_windows: monitor_threshold_windows block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#monitor_threshold_windows Monitor#monitor_threshold_windows}
        :param new_group_delay: The time (in seconds) to skip evaluations for new groups. ``new_group_delay`` overrides ``new_host_delay`` if it is set to a nonzero value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#new_group_delay Monitor#new_group_delay}
        :param new_host_delay: **Deprecated**. See ``new_group_delay``. Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non-negative integer. This value is ignored for simple monitors and monitors not grouped by host. Defaults to ``300``. The only case when this should be used is to override the default and set ``new_host_delay`` to zero for monitors grouped by host. **Deprecated.** Use ``new_group_delay`` except when setting ``new_host_delay`` to zero. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#new_host_delay Monitor#new_host_delay}
        :param no_data_timeframe: The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes. We recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#no_data_timeframe Monitor#no_data_timeframe}
        :param notify_audit: A boolean indicating whether tagged users will be notified on changes to this monitor. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#notify_audit Monitor#notify_audit}
        :param notify_no_data: A boolean indicating whether this monitor will notify when data stops reporting. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#notify_no_data Monitor#notify_no_data}
        :param on_missing_data: Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using ``Count`` queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than ``Count``, for example ``Gauge``, ``Measure``, or ``Rate``, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Valid values are: ``show_no_data``, ``show_and_notify_no_data``, ``resolve``, and ``default``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#on_missing_data Monitor#on_missing_data}
        :param priority: Integer from 1 (high) to 5 (low) indicating alert severity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#priority Monitor#priority}
        :param renotify_interval: The number of minutes after the last notification before a monitor will re-notify on the current status. It will only re-notify if it's not resolved. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_interval Monitor#renotify_interval}
        :param renotify_occurrences: The number of re-notification messages that should be sent on the current status. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_occurrences Monitor#renotify_occurrences}
        :param renotify_statuses: The types of statuses for which re-notification messages should be sent. Valid values are ``alert``, ``warn``, ``no data``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_statuses Monitor#renotify_statuses}
        :param require_full_window: A boolean indicating whether this monitor needs a full window of data before it's evaluated. We highly recommend you set this to ``false`` for sparse metrics, otherwise some evaluations will be skipped. Default: ``true`` for ``on average``, ``at all times`` and ``in total`` aggregation. ``false`` otherwise. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#require_full_window Monitor#require_full_window}
        :param restricted_roles: A list of unique role identifiers to define which roles are allowed to edit the monitor. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. Roles unique identifiers can be pulled from the `Roles API <https://docs.datadoghq.com/api/latest/roles/#list-roles>`_ in the ``data.id`` field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#restricted_roles Monitor#restricted_roles}
        :param tags: A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it's not currently possible to filter by these tags when querying via the API Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#tags Monitor#tags}
        :param timeout_h: The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#timeout_h Monitor#timeout_h}
        :param validate: If set to ``false``, skip the validation call done during plan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#validate Monitor#validate}
        :param variables: variables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#variables Monitor#variables}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(monitor_thresholds, dict):
            monitor_thresholds = MonitorMonitorThresholds(**monitor_thresholds)
        if isinstance(monitor_threshold_windows, dict):
            monitor_threshold_windows = MonitorMonitorThresholdWindows(**monitor_threshold_windows)
        if isinstance(variables, dict):
            variables = MonitorVariables(**variables)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument enable_logs_sample", value=enable_logs_sample, expected_type=type_hints["enable_logs_sample"])
            check_type(argname="argument escalation_message", value=escalation_message, expected_type=type_hints["escalation_message"])
            check_type(argname="argument evaluation_delay", value=evaluation_delay, expected_type=type_hints["evaluation_delay"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument groupby_simple_monitor", value=groupby_simple_monitor, expected_type=type_hints["groupby_simple_monitor"])
            check_type(argname="argument group_retention_duration", value=group_retention_duration, expected_type=type_hints["group_retention_duration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument include_tags", value=include_tags, expected_type=type_hints["include_tags"])
            check_type(argname="argument locked", value=locked, expected_type=type_hints["locked"])
            check_type(argname="argument monitor_thresholds", value=monitor_thresholds, expected_type=type_hints["monitor_thresholds"])
            check_type(argname="argument monitor_threshold_windows", value=monitor_threshold_windows, expected_type=type_hints["monitor_threshold_windows"])
            check_type(argname="argument new_group_delay", value=new_group_delay, expected_type=type_hints["new_group_delay"])
            check_type(argname="argument new_host_delay", value=new_host_delay, expected_type=type_hints["new_host_delay"])
            check_type(argname="argument no_data_timeframe", value=no_data_timeframe, expected_type=type_hints["no_data_timeframe"])
            check_type(argname="argument notify_audit", value=notify_audit, expected_type=type_hints["notify_audit"])
            check_type(argname="argument notify_no_data", value=notify_no_data, expected_type=type_hints["notify_no_data"])
            check_type(argname="argument on_missing_data", value=on_missing_data, expected_type=type_hints["on_missing_data"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument renotify_interval", value=renotify_interval, expected_type=type_hints["renotify_interval"])
            check_type(argname="argument renotify_occurrences", value=renotify_occurrences, expected_type=type_hints["renotify_occurrences"])
            check_type(argname="argument renotify_statuses", value=renotify_statuses, expected_type=type_hints["renotify_statuses"])
            check_type(argname="argument require_full_window", value=require_full_window, expected_type=type_hints["require_full_window"])
            check_type(argname="argument restricted_roles", value=restricted_roles, expected_type=type_hints["restricted_roles"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout_h", value=timeout_h, expected_type=type_hints["timeout_h"])
            check_type(argname="argument validate", value=validate, expected_type=type_hints["validate"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
            "name": name,
            "query": query,
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
        if enable_logs_sample is not None:
            self._values["enable_logs_sample"] = enable_logs_sample
        if escalation_message is not None:
            self._values["escalation_message"] = escalation_message
        if evaluation_delay is not None:
            self._values["evaluation_delay"] = evaluation_delay
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if groupby_simple_monitor is not None:
            self._values["groupby_simple_monitor"] = groupby_simple_monitor
        if group_retention_duration is not None:
            self._values["group_retention_duration"] = group_retention_duration
        if id is not None:
            self._values["id"] = id
        if include_tags is not None:
            self._values["include_tags"] = include_tags
        if locked is not None:
            self._values["locked"] = locked
        if monitor_thresholds is not None:
            self._values["monitor_thresholds"] = monitor_thresholds
        if monitor_threshold_windows is not None:
            self._values["monitor_threshold_windows"] = monitor_threshold_windows
        if new_group_delay is not None:
            self._values["new_group_delay"] = new_group_delay
        if new_host_delay is not None:
            self._values["new_host_delay"] = new_host_delay
        if no_data_timeframe is not None:
            self._values["no_data_timeframe"] = no_data_timeframe
        if notify_audit is not None:
            self._values["notify_audit"] = notify_audit
        if notify_no_data is not None:
            self._values["notify_no_data"] = notify_no_data
        if on_missing_data is not None:
            self._values["on_missing_data"] = on_missing_data
        if priority is not None:
            self._values["priority"] = priority
        if renotify_interval is not None:
            self._values["renotify_interval"] = renotify_interval
        if renotify_occurrences is not None:
            self._values["renotify_occurrences"] = renotify_occurrences
        if renotify_statuses is not None:
            self._values["renotify_statuses"] = renotify_statuses
        if require_full_window is not None:
            self._values["require_full_window"] = require_full_window
        if restricted_roles is not None:
            self._values["restricted_roles"] = restricted_roles
        if tags is not None:
            self._values["tags"] = tags
        if timeout_h is not None:
            self._values["timeout_h"] = timeout_h
        if validate is not None:
            self._values["validate"] = validate
        if variables is not None:
            self._values["variables"] = variables

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
    def message(self) -> builtins.str:
        '''A message to include with notifications for this monitor.

        Email notifications can be sent to specific users by using the same ``@username`` notation as events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#message Monitor#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of Datadog monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#name Monitor#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''The monitor query to notify on.

        Note this is not the same query you see in the UI and the syntax is different depending on the monitor type, please see the `API Reference <https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor>`_ for details. ``terraform plan`` will validate query contents unless ``validate`` is set to ``false``.

        *Note:** APM latency data is now available as Distribution Metrics. Existing monitors have been migrated automatically but all terraformed monitors can still use the existing metrics. We strongly recommend updating monitor definitions to query the new metrics. To learn more, or to see examples of how to update your terraform definitions to utilize the new distribution metrics, see the `detailed doc <https://docs.datadoghq.com/tracing/guide/ddsketch_trace_metrics/>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#query Monitor#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the monitor.

        The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API `documentation page <https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor>`_. Note: The monitor type cannot be changed after a monitor is created. Valid values are ``composite``, ``event alert``, ``log alert``, ``metric alert``, ``process alert``, ``query alert``, ``rum alert``, ``service check``, ``synthetics alert``, ``trace-analytics alert``, ``slo alert``, ``event-v2 alert``, ``audit alert``, ``ci-pipelines alert``, ``ci-tests alert``, ``error-tracking alert``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#type Monitor#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_logs_sample(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean indicating whether or not to include a list of log values which triggered the alert.

        This is only used by log monitors. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#enable_logs_sample Monitor#enable_logs_sample}
        '''
        result = self._values.get("enable_logs_sample")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def escalation_message(self) -> typing.Optional[builtins.str]:
        '''A message to include with a re-notification. Supports the ``@username`` notification allowed elsewhere.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#escalation_message Monitor#escalation_message}
        '''
        result = self._values.get("escalation_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_delay(self) -> typing.Optional[jsii.Number]:
        '''(Only applies to metric alert) Time (in seconds) to delay evaluation, as a non-negative integer.

        For example, if the value is set to ``300`` (5min), the ``timeframe`` is set to ``last_5m`` and the time is 7:00, the monitor will evaluate data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor will always have data during evaluation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#evaluation_delay Monitor#evaluation_delay}
        '''
        result = self._values.get("evaluation_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO, composite monitor).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#force_delete Monitor#force_delete}
        '''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def groupby_simple_monitor(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to trigger one alert if any source breaches a threshold.

        This is only used by log monitors. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#groupby_simple_monitor Monitor#groupby_simple_monitor}
        '''
        result = self._values.get("groupby_simple_monitor")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def group_retention_duration(self) -> typing.Optional[builtins.str]:
        '''The time span after which groups with missing data are dropped from the monitor state.

        The minimum value is one hour, and the maximum value is 72 hours. Example values are: 60m, 1h, and 2d. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#group_retention_duration Monitor#group_retention_duration}
        '''
        result = self._values.get("group_retention_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#id Monitor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#include_tags Monitor#include_tags}
        '''
        result = self._values.get("include_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def locked(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean indicating whether changes to this monitor should be restricted to the creator or admins.

        Defaults to ``false``. **Deprecated.** Use ``restricted_roles``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#locked Monitor#locked}
        '''
        result = self._values.get("locked")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def monitor_thresholds(self) -> typing.Optional["MonitorMonitorThresholds"]:
        '''monitor_thresholds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#monitor_thresholds Monitor#monitor_thresholds}
        '''
        result = self._values.get("monitor_thresholds")
        return typing.cast(typing.Optional["MonitorMonitorThresholds"], result)

    @builtins.property
    def monitor_threshold_windows(
        self,
    ) -> typing.Optional["MonitorMonitorThresholdWindows"]:
        '''monitor_threshold_windows block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#monitor_threshold_windows Monitor#monitor_threshold_windows}
        '''
        result = self._values.get("monitor_threshold_windows")
        return typing.cast(typing.Optional["MonitorMonitorThresholdWindows"], result)

    @builtins.property
    def new_group_delay(self) -> typing.Optional[jsii.Number]:
        '''The time (in seconds) to skip evaluations for new groups.

        ``new_group_delay`` overrides ``new_host_delay`` if it is set to a nonzero value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#new_group_delay Monitor#new_group_delay}
        '''
        result = self._values.get("new_group_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def new_host_delay(self) -> typing.Optional[jsii.Number]:
        '''**Deprecated**.

        See ``new_group_delay``. Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non-negative integer. This value is ignored for simple monitors and monitors not grouped by host. Defaults to ``300``. The only case when this should be used is to override the default and set ``new_host_delay`` to zero for monitors grouped by host. **Deprecated.** Use ``new_group_delay`` except when setting ``new_host_delay`` to zero.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#new_host_delay Monitor#new_host_delay}
        '''
        result = self._values.get("new_host_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def no_data_timeframe(self) -> typing.Optional[jsii.Number]:
        '''The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes.

        We recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#no_data_timeframe Monitor#no_data_timeframe}
        '''
        result = self._values.get("no_data_timeframe")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def notify_audit(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean indicating whether tagged users will be notified on changes to this monitor. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#notify_audit Monitor#notify_audit}
        '''
        result = self._values.get("notify_audit")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def notify_no_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean indicating whether this monitor will notify when data stops reporting. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#notify_no_data Monitor#notify_no_data}
        '''
        result = self._values.get("notify_no_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def on_missing_data(self) -> typing.Optional[builtins.str]:
        '''Controls how groups or monitors are treated if an evaluation does not return any data points.

        The default option results in different behavior depending on the monitor query type. For monitors using ``Count`` queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than ``Count``, for example ``Gauge``, ``Measure``, or ``Rate``, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Valid values are: ``show_no_data``, ``show_and_notify_no_data``, ``resolve``, and ``default``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#on_missing_data Monitor#on_missing_data}
        '''
        result = self._values.get("on_missing_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Integer from 1 (high) to 5 (low) indicating alert severity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#priority Monitor#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def renotify_interval(self) -> typing.Optional[jsii.Number]:
        '''The number of minutes after the last notification before a monitor will re-notify on the current status.

        It will only re-notify if it's not resolved.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_interval Monitor#renotify_interval}
        '''
        result = self._values.get("renotify_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def renotify_occurrences(self) -> typing.Optional[jsii.Number]:
        '''The number of re-notification messages that should be sent on the current status.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_occurrences Monitor#renotify_occurrences}
        '''
        result = self._values.get("renotify_occurrences")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def renotify_statuses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The types of statuses for which re-notification messages should be sent. Valid values are ``alert``, ``warn``, ``no data``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#renotify_statuses Monitor#renotify_statuses}
        '''
        result = self._values.get("renotify_statuses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def require_full_window(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''A boolean indicating whether this monitor needs a full window of data before it's evaluated.

        We highly recommend you set this to ``false`` for sparse metrics, otherwise some evaluations will be skipped. Default: ``true`` for ``on average``, ``at all times`` and ``in total`` aggregation. ``false`` otherwise.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#require_full_window Monitor#require_full_window}
        '''
        result = self._values.get("require_full_window")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def restricted_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of unique role identifiers to define which roles are allowed to edit the monitor.

        Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. Roles unique identifiers can be pulled from the `Roles API <https://docs.datadoghq.com/api/latest/roles/#list-roles>`_ in the ``data.id`` field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#restricted_roles Monitor#restricted_roles}
        '''
        result = self._values.get("restricted_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tags to associate with your monitor.

        This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it's not currently possible to filter by these tags when querying via the API

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#tags Monitor#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeout_h(self) -> typing.Optional[jsii.Number]:
        '''The number of hours of the monitor not reporting data before it automatically resolves from a triggered state.

        The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#timeout_h Monitor#timeout_h}
        '''
        result = self._values.get("timeout_h")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def validate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to ``false``, skip the validation call done during plan.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#validate Monitor#validate}
        '''
        result = self._values.get("validate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def variables(self) -> typing.Optional["MonitorVariables"]:
        '''variables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#variables Monitor#variables}
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Optional["MonitorVariables"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorMonitorThresholdWindows",
    jsii_struct_bases=[],
    name_mapping={
        "recovery_window": "recoveryWindow",
        "trigger_window": "triggerWindow",
    },
)
class MonitorMonitorThresholdWindows:
    def __init__(
        self,
        *,
        recovery_window: typing.Optional[builtins.str] = None,
        trigger_window: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recovery_window: Describes how long an anomalous metric must be normal before the alert recovers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#recovery_window Monitor#recovery_window}
        :param trigger_window: Describes how long a metric must be anomalous before an alert triggers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#trigger_window Monitor#trigger_window}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorMonitorThresholdWindows.__init__)
            check_type(argname="argument recovery_window", value=recovery_window, expected_type=type_hints["recovery_window"])
            check_type(argname="argument trigger_window", value=trigger_window, expected_type=type_hints["trigger_window"])
        self._values: typing.Dict[str, typing.Any] = {}
        if recovery_window is not None:
            self._values["recovery_window"] = recovery_window
        if trigger_window is not None:
            self._values["trigger_window"] = trigger_window

    @builtins.property
    def recovery_window(self) -> typing.Optional[builtins.str]:
        '''Describes how long an anomalous metric must be normal before the alert recovers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#recovery_window Monitor#recovery_window}
        '''
        result = self._values.get("recovery_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_window(self) -> typing.Optional[builtins.str]:
        '''Describes how long a metric must be anomalous before an alert triggers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#trigger_window Monitor#trigger_window}
        '''
        result = self._values.get("trigger_window")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorMonitorThresholdWindows(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorMonitorThresholdWindowsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorMonitorThresholdWindowsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorMonitorThresholdWindowsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRecoveryWindow")
    def reset_recovery_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryWindow", []))

    @jsii.member(jsii_name="resetTriggerWindow")
    def reset_trigger_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerWindow", []))

    @builtins.property
    @jsii.member(jsii_name="recoveryWindowInput")
    def recovery_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerWindowInput")
    def trigger_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryWindow")
    def recovery_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryWindow"))

    @recovery_window.setter
    def recovery_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdWindowsOutputReference, "recovery_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryWindow", value)

    @builtins.property
    @jsii.member(jsii_name="triggerWindow")
    def trigger_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerWindow"))

    @trigger_window.setter
    def trigger_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdWindowsOutputReference, "trigger_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerWindow", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorMonitorThresholdWindows]:
        return typing.cast(typing.Optional[MonitorMonitorThresholdWindows], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorMonitorThresholdWindows],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdWindowsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorMonitorThresholds",
    jsii_struct_bases=[],
    name_mapping={
        "critical": "critical",
        "critical_recovery": "criticalRecovery",
        "ok": "ok",
        "unknown": "unknown",
        "warning": "warning",
        "warning_recovery": "warningRecovery",
    },
)
class MonitorMonitorThresholds:
    def __init__(
        self,
        *,
        critical: typing.Optional[builtins.str] = None,
        critical_recovery: typing.Optional[builtins.str] = None,
        ok: typing.Optional[builtins.str] = None,
        unknown: typing.Optional[builtins.str] = None,
        warning: typing.Optional[builtins.str] = None,
        warning_recovery: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param critical: The monitor ``CRITICAL`` threshold. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#critical Monitor#critical}
        :param critical_recovery: The monitor ``CRITICAL`` recovery threshold. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#critical_recovery Monitor#critical_recovery}
        :param ok: The monitor ``OK`` threshold. Only supported in monitor type ``service check``. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#ok Monitor#ok}
        :param unknown: The monitor ``UNKNOWN`` threshold. Only supported in monitor type ``service check``. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#unknown Monitor#unknown}
        :param warning: The monitor ``WARNING`` threshold. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#warning Monitor#warning}
        :param warning_recovery: The monitor ``WARNING`` recovery threshold. Must be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#warning_recovery Monitor#warning_recovery}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorMonitorThresholds.__init__)
            check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            check_type(argname="argument critical_recovery", value=critical_recovery, expected_type=type_hints["critical_recovery"])
            check_type(argname="argument ok", value=ok, expected_type=type_hints["ok"])
            check_type(argname="argument unknown", value=unknown, expected_type=type_hints["unknown"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
            check_type(argname="argument warning_recovery", value=warning_recovery, expected_type=type_hints["warning_recovery"])
        self._values: typing.Dict[str, typing.Any] = {}
        if critical is not None:
            self._values["critical"] = critical
        if critical_recovery is not None:
            self._values["critical_recovery"] = critical_recovery
        if ok is not None:
            self._values["ok"] = ok
        if unknown is not None:
            self._values["unknown"] = unknown
        if warning is not None:
            self._values["warning"] = warning
        if warning_recovery is not None:
            self._values["warning_recovery"] = warning_recovery

    @builtins.property
    def critical(self) -> typing.Optional[builtins.str]:
        '''The monitor ``CRITICAL`` threshold. Must be a number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#critical Monitor#critical}
        '''
        result = self._values.get("critical")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def critical_recovery(self) -> typing.Optional[builtins.str]:
        '''The monitor ``CRITICAL`` recovery threshold. Must be a number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#critical_recovery Monitor#critical_recovery}
        '''
        result = self._values.get("critical_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ok(self) -> typing.Optional[builtins.str]:
        '''The monitor ``OK`` threshold. Only supported in monitor type ``service check``. Must be a number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#ok Monitor#ok}
        '''
        result = self._values.get("ok")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unknown(self) -> typing.Optional[builtins.str]:
        '''The monitor ``UNKNOWN`` threshold. Only supported in monitor type ``service check``. Must be a number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#unknown Monitor#unknown}
        '''
        result = self._values.get("unknown")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warning(self) -> typing.Optional[builtins.str]:
        '''The monitor ``WARNING`` threshold. Must be a number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#warning Monitor#warning}
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warning_recovery(self) -> typing.Optional[builtins.str]:
        '''The monitor ``WARNING`` recovery threshold. Must be a number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#warning_recovery Monitor#warning_recovery}
        '''
        result = self._values.get("warning_recovery")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorMonitorThresholds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorMonitorThresholdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorMonitorThresholdsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorMonitorThresholdsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCritical")
    def reset_critical(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCritical", []))

    @jsii.member(jsii_name="resetCriticalRecovery")
    def reset_critical_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCriticalRecovery", []))

    @jsii.member(jsii_name="resetOk")
    def reset_ok(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOk", []))

    @jsii.member(jsii_name="resetUnknown")
    def reset_unknown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnknown", []))

    @jsii.member(jsii_name="resetWarning")
    def reset_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarning", []))

    @jsii.member(jsii_name="resetWarningRecovery")
    def reset_warning_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarningRecovery", []))

    @builtins.property
    @jsii.member(jsii_name="criticalInput")
    def critical_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "criticalInput"))

    @builtins.property
    @jsii.member(jsii_name="criticalRecoveryInput")
    def critical_recovery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "criticalRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="okInput")
    def ok_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "okInput"))

    @builtins.property
    @jsii.member(jsii_name="unknownInput")
    def unknown_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unknownInput"))

    @builtins.property
    @jsii.member(jsii_name="warningInput")
    def warning_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warningInput"))

    @builtins.property
    @jsii.member(jsii_name="warningRecoveryInput")
    def warning_recovery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warningRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="critical")
    def critical(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "critical"))

    @critical.setter
    def critical(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdsOutputReference, "critical").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "critical", value)

    @builtins.property
    @jsii.member(jsii_name="criticalRecovery")
    def critical_recovery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "criticalRecovery"))

    @critical_recovery.setter
    def critical_recovery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdsOutputReference, "critical_recovery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "criticalRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="ok")
    def ok(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ok"))

    @ok.setter
    def ok(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdsOutputReference, "ok").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ok", value)

    @builtins.property
    @jsii.member(jsii_name="unknown")
    def unknown(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unknown"))

    @unknown.setter
    def unknown(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdsOutputReference, "unknown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unknown", value)

    @builtins.property
    @jsii.member(jsii_name="warning")
    def warning(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warning"))

    @warning.setter
    def warning(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdsOutputReference, "warning").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warning", value)

    @builtins.property
    @jsii.member(jsii_name="warningRecovery")
    def warning_recovery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warningRecovery"))

    @warning_recovery.setter
    def warning_recovery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdsOutputReference, "warning_recovery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warningRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorMonitorThresholds]:
        return typing.cast(typing.Optional[MonitorMonitorThresholds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MonitorMonitorThresholds]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorMonitorThresholdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariables",
    jsii_struct_bases=[],
    name_mapping={"event_query": "eventQuery"},
)
class MonitorVariables:
    def __init__(
        self,
        *,
        event_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorVariablesEventQuery", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param event_query: event_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#event_query Monitor#event_query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariables.__init__)
            check_type(argname="argument event_query", value=event_query, expected_type=type_hints["event_query"])
        self._values: typing.Dict[str, typing.Any] = {}
        if event_query is not None:
            self._values["event_query"] = event_query

    @builtins.property
    def event_query(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorVariablesEventQuery"]]]:
        '''event_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#event_query Monitor#event_query}
        '''
        result = self._values.get("event_query")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorVariablesEventQuery"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQuery",
    jsii_struct_bases=[],
    name_mapping={
        "compute": "compute",
        "data_source": "dataSource",
        "name": "name",
        "group_by": "groupBy",
        "indexes": "indexes",
        "search": "search",
    },
)
class MonitorVariablesEventQuery:
    def __init__(
        self,
        *,
        compute: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorVariablesEventQueryCompute", typing.Dict[str, typing.Any]]]],
        data_source: builtins.str,
        name: builtins.str,
        group_by: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorVariablesEventQueryGroupBy", typing.Dict[str, typing.Any]]]]] = None,
        indexes: typing.Optional[typing.Sequence[builtins.str]] = None,
        search: typing.Optional[typing.Union["MonitorVariablesEventQuerySearch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param compute: compute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#compute Monitor#compute}
        :param data_source: The data source for event platform-based queries. Valid values are ``rum``, ``ci_pipelines``, ``ci_tests``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#data_source Monitor#data_source}
        :param name: The name of query for use in formulas. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#name Monitor#name}
        :param group_by: group_by block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#group_by Monitor#group_by}
        :param indexes: An array of index names to query in the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#indexes Monitor#indexes}
        :param search: search block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#search Monitor#search}
        '''
        if isinstance(search, dict):
            search = MonitorVariablesEventQuerySearch(**search)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQuery.__init__)
            check_type(argname="argument compute", value=compute, expected_type=type_hints["compute"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument group_by", value=group_by, expected_type=type_hints["group_by"])
            check_type(argname="argument indexes", value=indexes, expected_type=type_hints["indexes"])
            check_type(argname="argument search", value=search, expected_type=type_hints["search"])
        self._values: typing.Dict[str, typing.Any] = {
            "compute": compute,
            "data_source": data_source,
            "name": name,
        }
        if group_by is not None:
            self._values["group_by"] = group_by
        if indexes is not None:
            self._values["indexes"] = indexes
        if search is not None:
            self._values["search"] = search

    @builtins.property
    def compute(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["MonitorVariablesEventQueryCompute"]]:
        '''compute block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#compute Monitor#compute}
        '''
        result = self._values.get("compute")
        assert result is not None, "Required property 'compute' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["MonitorVariablesEventQueryCompute"]], result)

    @builtins.property
    def data_source(self) -> builtins.str:
        '''The data source for event platform-based queries. Valid values are ``rum``, ``ci_pipelines``, ``ci_tests``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#data_source Monitor#data_source}
        '''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of query for use in formulas.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#name Monitor#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_by(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorVariablesEventQueryGroupBy"]]]:
        '''group_by block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#group_by Monitor#group_by}
        '''
        result = self._values.get("group_by")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorVariablesEventQueryGroupBy"]]], result)

    @builtins.property
    def indexes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of index names to query in the stream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#indexes Monitor#indexes}
        '''
        result = self._values.get("indexes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def search(self) -> typing.Optional["MonitorVariablesEventQuerySearch"]:
        '''search block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#search Monitor#search}
        '''
        result = self._values.get("search")
        return typing.cast(typing.Optional["MonitorVariablesEventQuerySearch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorVariablesEventQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryCompute",
    jsii_struct_bases=[],
    name_mapping={
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
    },
)
class MonitorVariablesEventQueryCompute:
    def __init__(
        self,
        *,
        aggregation: builtins.str,
        interval: typing.Optional[jsii.Number] = None,
        metric: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation: The aggregation methods for event platform queries. Valid values are ``count``, ``cardinality``, ``median``, ``pc75``, ``pc90``, ``pc95``, ``pc98``, ``pc99``, ``sum``, ``min``, ``max``, ``avg``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#aggregation Monitor#aggregation}
        :param interval: A time interval in milliseconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#interval Monitor#interval}
        :param metric: The measurable attribute to compute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#metric Monitor#metric}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryCompute.__init__)
            check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
        self._values: typing.Dict[str, typing.Any] = {
            "aggregation": aggregation,
        }
        if interval is not None:
            self._values["interval"] = interval
        if metric is not None:
            self._values["metric"] = metric

    @builtins.property
    def aggregation(self) -> builtins.str:
        '''The aggregation methods for event platform queries.

        Valid values are ``count``, ``cardinality``, ``median``, ``pc75``, ``pc90``, ``pc95``, ``pc98``, ``pc99``, ``sum``, ``min``, ``max``, ``avg``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#aggregation Monitor#aggregation}
        '''
        result = self._values.get("aggregation")
        assert result is not None, "Required property 'aggregation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''A time interval in milliseconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#interval Monitor#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric(self) -> typing.Optional[builtins.str]:
        '''The measurable attribute to compute.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#metric Monitor#metric}
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorVariablesEventQueryCompute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorVariablesEventQueryComputeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryComputeList",
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
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryComputeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorVariablesEventQueryComputeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryComputeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorVariablesEventQueryComputeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryComputeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryComputeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryComputeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryCompute]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryCompute]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryCompute]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryComputeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorVariablesEventQueryComputeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryComputeOutputReference",
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
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryComputeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetMetric")
    def reset_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetric", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationInput")
    def aggregation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregation")
    def aggregation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregation"))

    @aggregation.setter
    def aggregation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryComputeOutputReference, "aggregation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregation", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryComputeOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metric"))

    @metric.setter
    def metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryComputeOutputReference, "metric").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metric", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorVariablesEventQueryCompute, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorVariablesEventQueryCompute, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorVariablesEventQueryCompute, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryComputeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryGroupBy",
    jsii_struct_bases=[],
    name_mapping={"facet": "facet", "limit": "limit", "sort": "sort"},
)
class MonitorVariablesEventQueryGroupBy:
    def __init__(
        self,
        *,
        facet: builtins.str,
        limit: typing.Optional[jsii.Number] = None,
        sort: typing.Optional[typing.Union["MonitorVariablesEventQueryGroupBySort", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param facet: The event facet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#facet Monitor#facet}
        :param limit: The number of groups to return. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#limit Monitor#limit}
        :param sort: sort block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#sort Monitor#sort}
        '''
        if isinstance(sort, dict):
            sort = MonitorVariablesEventQueryGroupBySort(**sort)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryGroupBy.__init__)
            check_type(argname="argument facet", value=facet, expected_type=type_hints["facet"])
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument sort", value=sort, expected_type=type_hints["sort"])
        self._values: typing.Dict[str, typing.Any] = {
            "facet": facet,
        }
        if limit is not None:
            self._values["limit"] = limit
        if sort is not None:
            self._values["sort"] = sort

    @builtins.property
    def facet(self) -> builtins.str:
        '''The event facet.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#facet Monitor#facet}
        '''
        result = self._values.get("facet")
        assert result is not None, "Required property 'facet' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def limit(self) -> typing.Optional[jsii.Number]:
        '''The number of groups to return.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#limit Monitor#limit}
        '''
        result = self._values.get("limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sort(self) -> typing.Optional["MonitorVariablesEventQueryGroupBySort"]:
        '''sort block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#sort Monitor#sort}
        '''
        result = self._values.get("sort")
        return typing.cast(typing.Optional["MonitorVariablesEventQueryGroupBySort"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorVariablesEventQueryGroupBy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorVariablesEventQueryGroupByList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryGroupByList",
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
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryGroupByList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorVariablesEventQueryGroupByOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryGroupByList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorVariablesEventQueryGroupByOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupByList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupByList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupByList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryGroupBy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryGroupBy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryGroupBy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupByList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorVariablesEventQueryGroupByOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryGroupByOutputReference",
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
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryGroupByOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSort")
    def put_sort(
        self,
        *,
        aggregation: builtins.str,
        metric: typing.Optional[builtins.str] = None,
        order: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation: The aggregation methods for the event platform queries. Valid values are ``count``, ``cardinality``, ``median``, ``pc75``, ``pc90``, ``pc95``, ``pc98``, ``pc99``, ``sum``, ``min``, ``max``, ``avg``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#aggregation Monitor#aggregation}
        :param metric: The metric used for sorting group by results. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#metric Monitor#metric}
        :param order: Direction of sort. Valid values are ``asc``, ``desc``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#order Monitor#order}
        '''
        value = MonitorVariablesEventQueryGroupBySort(
            aggregation=aggregation, metric=metric, order=order
        )

        return typing.cast(None, jsii.invoke(self, "putSort", [value]))

    @jsii.member(jsii_name="resetLimit")
    def reset_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLimit", []))

    @jsii.member(jsii_name="resetSort")
    def reset_sort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSort", []))

    @builtins.property
    @jsii.member(jsii_name="sort")
    def sort(self) -> "MonitorVariablesEventQueryGroupBySortOutputReference":
        return typing.cast("MonitorVariablesEventQueryGroupBySortOutputReference", jsii.get(self, "sort"))

    @builtins.property
    @jsii.member(jsii_name="facetInput")
    def facet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "facetInput"))

    @builtins.property
    @jsii.member(jsii_name="limitInput")
    def limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "limitInput"))

    @builtins.property
    @jsii.member(jsii_name="sortInput")
    def sort_input(self) -> typing.Optional["MonitorVariablesEventQueryGroupBySort"]:
        return typing.cast(typing.Optional["MonitorVariablesEventQueryGroupBySort"], jsii.get(self, "sortInput"))

    @builtins.property
    @jsii.member(jsii_name="facet")
    def facet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "facet"))

    @facet.setter
    def facet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupByOutputReference, "facet").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "facet", value)

    @builtins.property
    @jsii.member(jsii_name="limit")
    def limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "limit"))

    @limit.setter
    def limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupByOutputReference, "limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorVariablesEventQueryGroupBy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorVariablesEventQueryGroupBy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorVariablesEventQueryGroupBy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupByOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryGroupBySort",
    jsii_struct_bases=[],
    name_mapping={"aggregation": "aggregation", "metric": "metric", "order": "order"},
)
class MonitorVariablesEventQueryGroupBySort:
    def __init__(
        self,
        *,
        aggregation: builtins.str,
        metric: typing.Optional[builtins.str] = None,
        order: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation: The aggregation methods for the event platform queries. Valid values are ``count``, ``cardinality``, ``median``, ``pc75``, ``pc90``, ``pc95``, ``pc98``, ``pc99``, ``sum``, ``min``, ``max``, ``avg``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#aggregation Monitor#aggregation}
        :param metric: The metric used for sorting group by results. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#metric Monitor#metric}
        :param order: Direction of sort. Valid values are ``asc``, ``desc``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#order Monitor#order}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryGroupBySort.__init__)
            check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
        self._values: typing.Dict[str, typing.Any] = {
            "aggregation": aggregation,
        }
        if metric is not None:
            self._values["metric"] = metric
        if order is not None:
            self._values["order"] = order

    @builtins.property
    def aggregation(self) -> builtins.str:
        '''The aggregation methods for the event platform queries.

        Valid values are ``count``, ``cardinality``, ``median``, ``pc75``, ``pc90``, ``pc95``, ``pc98``, ``pc99``, ``sum``, ``min``, ``max``, ``avg``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#aggregation Monitor#aggregation}
        '''
        result = self._values.get("aggregation")
        assert result is not None, "Required property 'aggregation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric(self) -> typing.Optional[builtins.str]:
        '''The metric used for sorting group by results.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#metric Monitor#metric}
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def order(self) -> typing.Optional[builtins.str]:
        '''Direction of sort. Valid values are ``asc``, ``desc``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#order Monitor#order}
        '''
        result = self._values.get("order")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorVariablesEventQueryGroupBySort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorVariablesEventQueryGroupBySortOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryGroupBySortOutputReference",
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
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryGroupBySortOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetric")
    def reset_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetric", []))

    @jsii.member(jsii_name="resetOrder")
    def reset_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrder", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationInput")
    def aggregation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregation")
    def aggregation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregation"))

    @aggregation.setter
    def aggregation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupBySortOutputReference, "aggregation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregation", value)

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metric"))

    @metric.setter
    def metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupBySortOutputReference, "metric").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metric", value)

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "order"))

    @order.setter
    def order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupBySortOutputReference, "order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorVariablesEventQueryGroupBySort]:
        return typing.cast(typing.Optional[MonitorVariablesEventQueryGroupBySort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorVariablesEventQueryGroupBySort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryGroupBySortOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorVariablesEventQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryList",
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
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MonitorVariablesEventQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorVariablesEventQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorVariablesEventQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQueryOutputReference",
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
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCompute")
    def put_compute(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorVariablesEventQueryCompute, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryOutputReference.put_compute)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCompute", [value]))

    @jsii.member(jsii_name="putGroupBy")
    def put_group_by(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorVariablesEventQueryGroupBy, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQueryOutputReference.put_group_by)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGroupBy", [value]))

    @jsii.member(jsii_name="putSearch")
    def put_search(self, *, query: builtins.str) -> None:
        '''
        :param query: The events search string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#query Monitor#query}
        '''
        value = MonitorVariablesEventQuerySearch(query=query)

        return typing.cast(None, jsii.invoke(self, "putSearch", [value]))

    @jsii.member(jsii_name="resetGroupBy")
    def reset_group_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupBy", []))

    @jsii.member(jsii_name="resetIndexes")
    def reset_indexes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexes", []))

    @jsii.member(jsii_name="resetSearch")
    def reset_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearch", []))

    @builtins.property
    @jsii.member(jsii_name="compute")
    def compute(self) -> MonitorVariablesEventQueryComputeList:
        return typing.cast(MonitorVariablesEventQueryComputeList, jsii.get(self, "compute"))

    @builtins.property
    @jsii.member(jsii_name="groupBy")
    def group_by(self) -> MonitorVariablesEventQueryGroupByList:
        return typing.cast(MonitorVariablesEventQueryGroupByList, jsii.get(self, "groupBy"))

    @builtins.property
    @jsii.member(jsii_name="search")
    def search(self) -> "MonitorVariablesEventQuerySearchOutputReference":
        return typing.cast("MonitorVariablesEventQuerySearchOutputReference", jsii.get(self, "search"))

    @builtins.property
    @jsii.member(jsii_name="computeInput")
    def compute_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryCompute]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryCompute]]], jsii.get(self, "computeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceInput")
    def data_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByInput")
    def group_by_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryGroupBy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQueryGroupBy]]], jsii.get(self, "groupByInput"))

    @builtins.property
    @jsii.member(jsii_name="indexesInput")
    def indexes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "indexesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="searchInput")
    def search_input(self) -> typing.Optional["MonitorVariablesEventQuerySearch"]:
        return typing.cast(typing.Optional["MonitorVariablesEventQuerySearch"], jsii.get(self, "searchInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryOutputReference, "data_source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSource", value)

    @builtins.property
    @jsii.member(jsii_name="indexes")
    def indexes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "indexes"))

    @indexes.setter
    def indexes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryOutputReference, "indexes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexes", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorVariablesEventQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorVariablesEventQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorVariablesEventQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQuerySearch",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class MonitorVariablesEventQuerySearch:
    def __init__(self, *, query: builtins.str) -> None:
        '''
        :param query: The events search string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#query Monitor#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesEventQuerySearch.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }

    @builtins.property
    def query(self) -> builtins.str:
        '''The events search string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/monitor#query Monitor#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorVariablesEventQuerySearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorVariablesEventQuerySearchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesEventQuerySearchOutputReference",
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
            type_hints = typing.get_type_hints(MonitorVariablesEventQuerySearchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQuerySearchOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorVariablesEventQuerySearch]:
        return typing.cast(typing.Optional[MonitorVariablesEventQuerySearch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorVariablesEventQuerySearch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesEventQuerySearchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorVariablesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.monitor.MonitorVariablesOutputReference",
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
            type_hints = typing.get_type_hints(MonitorVariablesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEventQuery")
    def put_event_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorVariablesEventQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorVariablesOutputReference.put_event_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEventQuery", [value]))

    @jsii.member(jsii_name="resetEventQuery")
    def reset_event_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventQuery", []))

    @builtins.property
    @jsii.member(jsii_name="eventQuery")
    def event_query(self) -> MonitorVariablesEventQueryList:
        return typing.cast(MonitorVariablesEventQueryList, jsii.get(self, "eventQuery"))

    @builtins.property
    @jsii.member(jsii_name="eventQueryInput")
    def event_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorVariablesEventQuery]]], jsii.get(self, "eventQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorVariables]:
        return typing.cast(typing.Optional[MonitorVariables], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MonitorVariables]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorVariablesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Monitor",
    "MonitorConfig",
    "MonitorMonitorThresholdWindows",
    "MonitorMonitorThresholdWindowsOutputReference",
    "MonitorMonitorThresholds",
    "MonitorMonitorThresholdsOutputReference",
    "MonitorVariables",
    "MonitorVariablesEventQuery",
    "MonitorVariablesEventQueryCompute",
    "MonitorVariablesEventQueryComputeList",
    "MonitorVariablesEventQueryComputeOutputReference",
    "MonitorVariablesEventQueryGroupBy",
    "MonitorVariablesEventQueryGroupByList",
    "MonitorVariablesEventQueryGroupByOutputReference",
    "MonitorVariablesEventQueryGroupBySort",
    "MonitorVariablesEventQueryGroupBySortOutputReference",
    "MonitorVariablesEventQueryList",
    "MonitorVariablesEventQueryOutputReference",
    "MonitorVariablesEventQuerySearch",
    "MonitorVariablesEventQuerySearchOutputReference",
    "MonitorVariablesOutputReference",
]

publication.publish()
