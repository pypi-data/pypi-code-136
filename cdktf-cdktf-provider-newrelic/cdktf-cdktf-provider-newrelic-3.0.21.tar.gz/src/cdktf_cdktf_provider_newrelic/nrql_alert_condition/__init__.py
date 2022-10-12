'''
# `newrelic_nrql_alert_condition`

Refer to the Terraform Registory for docs: [`newrelic_nrql_alert_condition`](https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition).
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


class NrqlAlertCondition(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertCondition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition newrelic_nrql_alert_condition}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        nrql: typing.Union["NrqlAlertConditionNrql", typing.Dict[str, typing.Any]],
        policy_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        aggregation_delay: typing.Optional[builtins.str] = None,
        aggregation_method: typing.Optional[builtins.str] = None,
        aggregation_timer: typing.Optional[builtins.str] = None,
        aggregation_window: typing.Optional[jsii.Number] = None,
        baseline_direction: typing.Optional[builtins.str] = None,
        close_violations_on_expiration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        critical: typing.Optional[typing.Union["NrqlAlertConditionCritical", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expiration_duration: typing.Optional[jsii.Number] = None,
        fill_option: typing.Optional[builtins.str] = None,
        fill_value: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        open_violation_on_expiration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        runbook_url: typing.Optional[builtins.str] = None,
        slide_by: typing.Optional[jsii.Number] = None,
        term: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NrqlAlertConditionTerm", typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
        value_function: typing.Optional[builtins.str] = None,
        violation_time_limit: typing.Optional[builtins.str] = None,
        violation_time_limit_seconds: typing.Optional[jsii.Number] = None,
        warning: typing.Optional[typing.Union["NrqlAlertConditionWarning", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition newrelic_nrql_alert_condition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The title of the condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#name NrqlAlertCondition#name}
        :param nrql: nrql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#nrql NrqlAlertCondition#nrql}
        :param policy_id: The ID of the policy where this condition should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#policy_id NrqlAlertCondition#policy_id}
        :param account_id: The New Relic account ID for managing your NRQL alert conditions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#account_id NrqlAlertCondition#account_id}
        :param aggregation_delay: How long we wait for data that belongs in each aggregation window. Depending on your data, a longer delay may increase accuracy but delay notifications. Use aggregationDelay with the EVENT_FLOW and CADENCE aggregation methods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_delay NrqlAlertCondition#aggregation_delay}
        :param aggregation_method: The method that determines when we consider an aggregation window to be complete so that we can evaluate the signal for violations. Default is CADENCE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_method NrqlAlertCondition#aggregation_method}
        :param aggregation_timer: How long we wait after each data point arrives to make sure we've processed the whole batch. Use aggregationTimer with the EVENT_TIMER aggregation method. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_timer NrqlAlertCondition#aggregation_timer}
        :param aggregation_window: The duration of the time window used to evaluate the NRQL query, in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_window NrqlAlertCondition#aggregation_window}
        :param baseline_direction: The baseline direction of a baseline NRQL alert condition. Valid values are: 'LOWER_ONLY', 'UPPER_AND_LOWER', 'UPPER_ONLY' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#baseline_direction NrqlAlertCondition#baseline_direction}
        :param close_violations_on_expiration: Whether to close all open violations when the signal expires. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#close_violations_on_expiration NrqlAlertCondition#close_violations_on_expiration}
        :param critical: critical block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#critical NrqlAlertCondition#critical}
        :param description: The description of the NRQL alert condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#description NrqlAlertCondition#description}
        :param enabled: Whether or not to enable the alert condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#enabled NrqlAlertCondition#enabled}
        :param expiration_duration: The amount of time (in seconds) to wait before considering the signal expired. Must be in the range of 30 to 172800 (inclusive) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#expiration_duration NrqlAlertCondition#expiration_duration}
        :param fill_option: Which strategy to use when filling gaps in the signal. If static, the 'fill value' will be used for filling gaps in the signal. Valid values are: 'NONE', 'LAST_VALUE', or 'STATIC' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#fill_option NrqlAlertCondition#fill_option}
        :param fill_value: If using the 'static' fill option, this value will be used for filling gaps in the signal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#fill_value NrqlAlertCondition#fill_value}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#id NrqlAlertCondition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param open_violation_on_expiration: Whether to create a new violation to capture that the signal expired. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#open_violation_on_expiration NrqlAlertCondition#open_violation_on_expiration}
        :param runbook_url: Runbook URL to display in notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#runbook_url NrqlAlertCondition#runbook_url}
        :param slide_by: The duration of overlapping timewindows used to smooth the chart line, in seconds. Must be a factor of ``aggregation_window`` and less than the aggregation window. It should be greater or equal to 30 seconds if ``aggregation_window`` is less than or equal to 3600 seconds, or greater or equal to ``aggregation_window / 120`` if ``aggregation_window`` is greater than 3600 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#slide_by NrqlAlertCondition#slide_by}
        :param term: term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#term NrqlAlertCondition#term}
        :param type: The type of NRQL alert condition to create. Valid values are: 'static', 'baseline'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#type NrqlAlertCondition#type}
        :param value_function: Values are: 'single_value' (deprecated) or 'sum' (deprecated). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#value_function NrqlAlertCondition#value_function}
        :param violation_time_limit: Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are 'ONE_HOUR', 'TWO_HOURS', 'FOUR_HOURS', 'EIGHT_HOURS', 'TWELVE_HOURS', 'TWENTY_FOUR_HOURS', 'THIRTY_DAYS' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#violation_time_limit NrqlAlertCondition#violation_time_limit}
        :param violation_time_limit_seconds: Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Must be in the range of 300 to 2592000 (inclusive) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#violation_time_limit_seconds NrqlAlertCondition#violation_time_limit_seconds}
        :param warning: warning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#warning NrqlAlertCondition#warning}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NrqlAlertCondition.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NrqlAlertConditionConfig(
            name=name,
            nrql=nrql,
            policy_id=policy_id,
            account_id=account_id,
            aggregation_delay=aggregation_delay,
            aggregation_method=aggregation_method,
            aggregation_timer=aggregation_timer,
            aggregation_window=aggregation_window,
            baseline_direction=baseline_direction,
            close_violations_on_expiration=close_violations_on_expiration,
            critical=critical,
            description=description,
            enabled=enabled,
            expiration_duration=expiration_duration,
            fill_option=fill_option,
            fill_value=fill_value,
            id=id,
            open_violation_on_expiration=open_violation_on_expiration,
            runbook_url=runbook_url,
            slide_by=slide_by,
            term=term,
            type=type,
            value_function=value_function,
            violation_time_limit=violation_time_limit,
            violation_time_limit_seconds=violation_time_limit_seconds,
            warning=warning,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCritical")
    def put_critical(
        self,
        *,
        threshold: jsii.Number,
        duration: typing.Optional[jsii.Number] = None,
        operator: typing.Optional[builtins.str] = None,
        threshold_duration: typing.Optional[jsii.Number] = None,
        threshold_occurrences: typing.Optional[builtins.str] = None,
        time_function: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param threshold: For baseline conditions must be in range [1, 1000]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold NrqlAlertCondition#threshold}
        :param duration: In minutes, must be in the range of 1 to 120 (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#duration NrqlAlertCondition#duration}
        :param operator: One of (above, above_or_equals, below, below_or_equals, equals, not_equals). Defaults to 'equals'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#operator NrqlAlertCondition#operator}
        :param threshold_duration: The duration, in seconds, that the threshold must violate in order to create a violation. Value must be a multiple of the 'aggregation_window' (which has a default of 60 seconds). Value must be within 120-3600 seconds for baseline conditions, within 120-7200 seconds for static conditions with the sum value function, and within 60-7200 seconds for static conditions with the single_value value function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_duration NrqlAlertCondition#threshold_duration}
        :param threshold_occurrences: The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: 'ALL' or 'AT_LEAST_ONCE' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_occurrences NrqlAlertCondition#threshold_occurrences}
        :param time_function: Valid values are: 'all' or 'any'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#time_function NrqlAlertCondition#time_function}
        '''
        value = NrqlAlertConditionCritical(
            threshold=threshold,
            duration=duration,
            operator=operator,
            threshold_duration=threshold_duration,
            threshold_occurrences=threshold_occurrences,
            time_function=time_function,
        )

        return typing.cast(None, jsii.invoke(self, "putCritical", [value]))

    @jsii.member(jsii_name="putNrql")
    def put_nrql(
        self,
        *,
        query: builtins.str,
        evaluation_offset: typing.Optional[jsii.Number] = None,
        since_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#query NrqlAlertCondition#query}.
        :param evaluation_offset: NRQL queries are evaluated in one-minute time windows. The start time depends on the value you provide in the NRQL condition's ``evaluation_offset``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#evaluation_offset NrqlAlertCondition#evaluation_offset}
        :param since_value: NRQL queries are evaluated in one-minute time windows. The start time depends on the value you provide in the NRQL condition's ``since_value``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#since_value NrqlAlertCondition#since_value}
        '''
        value = NrqlAlertConditionNrql(
            query=query, evaluation_offset=evaluation_offset, since_value=since_value
        )

        return typing.cast(None, jsii.invoke(self, "putNrql", [value]))

    @jsii.member(jsii_name="putTerm")
    def put_term(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NrqlAlertConditionTerm", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NrqlAlertCondition.put_term)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTerm", [value]))

    @jsii.member(jsii_name="putWarning")
    def put_warning(
        self,
        *,
        threshold: jsii.Number,
        duration: typing.Optional[jsii.Number] = None,
        operator: typing.Optional[builtins.str] = None,
        threshold_duration: typing.Optional[jsii.Number] = None,
        threshold_occurrences: typing.Optional[builtins.str] = None,
        time_function: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param threshold: For baseline conditions must be in range [1, 1000]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold NrqlAlertCondition#threshold}
        :param duration: In minutes, must be in the range of 1 to 120 (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#duration NrqlAlertCondition#duration}
        :param operator: One of (above, above_or_equals, below, below_or_equals, equals, not_equals). Defaults to 'equals'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#operator NrqlAlertCondition#operator}
        :param threshold_duration: The duration, in seconds, that the threshold must violate in order to create a violation. Value must be a multiple of the 'aggregation_window' (which has a default of 60 seconds). Value must be within 120-3600 seconds for baseline conditions, within 120-7200 seconds for static conditions with the sum value function, and within 60-7200 seconds for static conditions with the single_value value function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_duration NrqlAlertCondition#threshold_duration}
        :param threshold_occurrences: The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: 'ALL' or 'AT_LEAST_ONCE' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_occurrences NrqlAlertCondition#threshold_occurrences}
        :param time_function: Valid values are: 'all' or 'any'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#time_function NrqlAlertCondition#time_function}
        '''
        value = NrqlAlertConditionWarning(
            threshold=threshold,
            duration=duration,
            operator=operator,
            threshold_duration=threshold_duration,
            threshold_occurrences=threshold_occurrences,
            time_function=time_function,
        )

        return typing.cast(None, jsii.invoke(self, "putWarning", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAggregationDelay")
    def reset_aggregation_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationDelay", []))

    @jsii.member(jsii_name="resetAggregationMethod")
    def reset_aggregation_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationMethod", []))

    @jsii.member(jsii_name="resetAggregationTimer")
    def reset_aggregation_timer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationTimer", []))

    @jsii.member(jsii_name="resetAggregationWindow")
    def reset_aggregation_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationWindow", []))

    @jsii.member(jsii_name="resetBaselineDirection")
    def reset_baseline_direction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaselineDirection", []))

    @jsii.member(jsii_name="resetCloseViolationsOnExpiration")
    def reset_close_violations_on_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloseViolationsOnExpiration", []))

    @jsii.member(jsii_name="resetCritical")
    def reset_critical(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCritical", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetExpirationDuration")
    def reset_expiration_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationDuration", []))

    @jsii.member(jsii_name="resetFillOption")
    def reset_fill_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFillOption", []))

    @jsii.member(jsii_name="resetFillValue")
    def reset_fill_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFillValue", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOpenViolationOnExpiration")
    def reset_open_violation_on_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenViolationOnExpiration", []))

    @jsii.member(jsii_name="resetRunbookUrl")
    def reset_runbook_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunbookUrl", []))

    @jsii.member(jsii_name="resetSlideBy")
    def reset_slide_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlideBy", []))

    @jsii.member(jsii_name="resetTerm")
    def reset_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerm", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValueFunction")
    def reset_value_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueFunction", []))

    @jsii.member(jsii_name="resetViolationTimeLimit")
    def reset_violation_time_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViolationTimeLimit", []))

    @jsii.member(jsii_name="resetViolationTimeLimitSeconds")
    def reset_violation_time_limit_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViolationTimeLimitSeconds", []))

    @jsii.member(jsii_name="resetWarning")
    def reset_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarning", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="critical")
    def critical(self) -> "NrqlAlertConditionCriticalOutputReference":
        return typing.cast("NrqlAlertConditionCriticalOutputReference", jsii.get(self, "critical"))

    @builtins.property
    @jsii.member(jsii_name="entityGuid")
    def entity_guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityGuid"))

    @builtins.property
    @jsii.member(jsii_name="nrql")
    def nrql(self) -> "NrqlAlertConditionNrqlOutputReference":
        return typing.cast("NrqlAlertConditionNrqlOutputReference", jsii.get(self, "nrql"))

    @builtins.property
    @jsii.member(jsii_name="term")
    def term(self) -> "NrqlAlertConditionTermList":
        return typing.cast("NrqlAlertConditionTermList", jsii.get(self, "term"))

    @builtins.property
    @jsii.member(jsii_name="warning")
    def warning(self) -> "NrqlAlertConditionWarningOutputReference":
        return typing.cast("NrqlAlertConditionWarningOutputReference", jsii.get(self, "warning"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationDelayInput")
    def aggregation_delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationMethodInput")
    def aggregation_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationTimerInput")
    def aggregation_timer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationTimerInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationWindowInput")
    def aggregation_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "aggregationWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="baselineDirectionInput")
    def baseline_direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baselineDirectionInput"))

    @builtins.property
    @jsii.member(jsii_name="closeViolationsOnExpirationInput")
    def close_violations_on_expiration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "closeViolationsOnExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="criticalInput")
    def critical_input(self) -> typing.Optional["NrqlAlertConditionCritical"]:
        return typing.cast(typing.Optional["NrqlAlertConditionCritical"], jsii.get(self, "criticalInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationDurationInput")
    def expiration_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="fillOptionInput")
    def fill_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fillOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="fillValueInput")
    def fill_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fillValueInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlInput")
    def nrql_input(self) -> typing.Optional["NrqlAlertConditionNrql"]:
        return typing.cast(typing.Optional["NrqlAlertConditionNrql"], jsii.get(self, "nrqlInput"))

    @builtins.property
    @jsii.member(jsii_name="openViolationOnExpirationInput")
    def open_violation_on_expiration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "openViolationOnExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="runbookUrlInput")
    def runbook_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runbookUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="slideByInput")
    def slide_by_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "slideByInput"))

    @builtins.property
    @jsii.member(jsii_name="termInput")
    def term_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NrqlAlertConditionTerm"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NrqlAlertConditionTerm"]]], jsii.get(self, "termInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueFunctionInput")
    def value_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="violationTimeLimitInput")
    def violation_time_limit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "violationTimeLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="violationTimeLimitSecondsInput")
    def violation_time_limit_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "violationTimeLimitSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="warningInput")
    def warning_input(self) -> typing.Optional["NrqlAlertConditionWarning"]:
        return typing.cast(typing.Optional["NrqlAlertConditionWarning"], jsii.get(self, "warningInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="aggregationDelay")
    def aggregation_delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationDelay"))

    @aggregation_delay.setter
    def aggregation_delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "aggregation_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationDelay", value)

    @builtins.property
    @jsii.member(jsii_name="aggregationMethod")
    def aggregation_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationMethod"))

    @aggregation_method.setter
    def aggregation_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "aggregation_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="aggregationTimer")
    def aggregation_timer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationTimer"))

    @aggregation_timer.setter
    def aggregation_timer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "aggregation_timer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationTimer", value)

    @builtins.property
    @jsii.member(jsii_name="aggregationWindow")
    def aggregation_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "aggregationWindow"))

    @aggregation_window.setter
    def aggregation_window(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "aggregation_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationWindow", value)

    @builtins.property
    @jsii.member(jsii_name="baselineDirection")
    def baseline_direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baselineDirection"))

    @baseline_direction.setter
    def baseline_direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "baseline_direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baselineDirection", value)

    @builtins.property
    @jsii.member(jsii_name="closeViolationsOnExpiration")
    def close_violations_on_expiration(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "closeViolationsOnExpiration"))

    @close_violations_on_expiration.setter
    def close_violations_on_expiration(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "close_violations_on_expiration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "closeViolationsOnExpiration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="expirationDuration")
    def expiration_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expirationDuration"))

    @expiration_duration.setter
    def expiration_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "expiration_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationDuration", value)

    @builtins.property
    @jsii.member(jsii_name="fillOption")
    def fill_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fillOption"))

    @fill_option.setter
    def fill_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "fill_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fillOption", value)

    @builtins.property
    @jsii.member(jsii_name="fillValue")
    def fill_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fillValue"))

    @fill_value.setter
    def fill_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "fill_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fillValue", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="openViolationOnExpiration")
    def open_violation_on_expiration(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "openViolationOnExpiration"))

    @open_violation_on_expiration.setter
    def open_violation_on_expiration(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "open_violation_on_expiration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openViolationOnExpiration", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="runbookUrl")
    def runbook_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runbookUrl"))

    @runbook_url.setter
    def runbook_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "runbook_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runbookUrl", value)

    @builtins.property
    @jsii.member(jsii_name="slideBy")
    def slide_by(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "slideBy"))

    @slide_by.setter
    def slide_by(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "slide_by").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slideBy", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="valueFunction")
    def value_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueFunction"))

    @value_function.setter
    def value_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "value_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueFunction", value)

    @builtins.property
    @jsii.member(jsii_name="violationTimeLimit")
    def violation_time_limit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "violationTimeLimit"))

    @violation_time_limit.setter
    def violation_time_limit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "violation_time_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "violationTimeLimit", value)

    @builtins.property
    @jsii.member(jsii_name="violationTimeLimitSeconds")
    def violation_time_limit_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "violationTimeLimitSeconds"))

    @violation_time_limit_seconds.setter
    def violation_time_limit_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertCondition, "violation_time_limit_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "violationTimeLimitSeconds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionConfig",
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
        "nrql": "nrql",
        "policy_id": "policyId",
        "account_id": "accountId",
        "aggregation_delay": "aggregationDelay",
        "aggregation_method": "aggregationMethod",
        "aggregation_timer": "aggregationTimer",
        "aggregation_window": "aggregationWindow",
        "baseline_direction": "baselineDirection",
        "close_violations_on_expiration": "closeViolationsOnExpiration",
        "critical": "critical",
        "description": "description",
        "enabled": "enabled",
        "expiration_duration": "expirationDuration",
        "fill_option": "fillOption",
        "fill_value": "fillValue",
        "id": "id",
        "open_violation_on_expiration": "openViolationOnExpiration",
        "runbook_url": "runbookUrl",
        "slide_by": "slideBy",
        "term": "term",
        "type": "type",
        "value_function": "valueFunction",
        "violation_time_limit": "violationTimeLimit",
        "violation_time_limit_seconds": "violationTimeLimitSeconds",
        "warning": "warning",
    },
)
class NrqlAlertConditionConfig(cdktf.TerraformMetaArguments):
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
        nrql: typing.Union["NrqlAlertConditionNrql", typing.Dict[str, typing.Any]],
        policy_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        aggregation_delay: typing.Optional[builtins.str] = None,
        aggregation_method: typing.Optional[builtins.str] = None,
        aggregation_timer: typing.Optional[builtins.str] = None,
        aggregation_window: typing.Optional[jsii.Number] = None,
        baseline_direction: typing.Optional[builtins.str] = None,
        close_violations_on_expiration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        critical: typing.Optional[typing.Union["NrqlAlertConditionCritical", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expiration_duration: typing.Optional[jsii.Number] = None,
        fill_option: typing.Optional[builtins.str] = None,
        fill_value: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        open_violation_on_expiration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        runbook_url: typing.Optional[builtins.str] = None,
        slide_by: typing.Optional[jsii.Number] = None,
        term: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NrqlAlertConditionTerm", typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
        value_function: typing.Optional[builtins.str] = None,
        violation_time_limit: typing.Optional[builtins.str] = None,
        violation_time_limit_seconds: typing.Optional[jsii.Number] = None,
        warning: typing.Optional[typing.Union["NrqlAlertConditionWarning", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The title of the condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#name NrqlAlertCondition#name}
        :param nrql: nrql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#nrql NrqlAlertCondition#nrql}
        :param policy_id: The ID of the policy where this condition should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#policy_id NrqlAlertCondition#policy_id}
        :param account_id: The New Relic account ID for managing your NRQL alert conditions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#account_id NrqlAlertCondition#account_id}
        :param aggregation_delay: How long we wait for data that belongs in each aggregation window. Depending on your data, a longer delay may increase accuracy but delay notifications. Use aggregationDelay with the EVENT_FLOW and CADENCE aggregation methods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_delay NrqlAlertCondition#aggregation_delay}
        :param aggregation_method: The method that determines when we consider an aggregation window to be complete so that we can evaluate the signal for violations. Default is CADENCE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_method NrqlAlertCondition#aggregation_method}
        :param aggregation_timer: How long we wait after each data point arrives to make sure we've processed the whole batch. Use aggregationTimer with the EVENT_TIMER aggregation method. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_timer NrqlAlertCondition#aggregation_timer}
        :param aggregation_window: The duration of the time window used to evaluate the NRQL query, in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_window NrqlAlertCondition#aggregation_window}
        :param baseline_direction: The baseline direction of a baseline NRQL alert condition. Valid values are: 'LOWER_ONLY', 'UPPER_AND_LOWER', 'UPPER_ONLY' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#baseline_direction NrqlAlertCondition#baseline_direction}
        :param close_violations_on_expiration: Whether to close all open violations when the signal expires. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#close_violations_on_expiration NrqlAlertCondition#close_violations_on_expiration}
        :param critical: critical block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#critical NrqlAlertCondition#critical}
        :param description: The description of the NRQL alert condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#description NrqlAlertCondition#description}
        :param enabled: Whether or not to enable the alert condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#enabled NrqlAlertCondition#enabled}
        :param expiration_duration: The amount of time (in seconds) to wait before considering the signal expired. Must be in the range of 30 to 172800 (inclusive) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#expiration_duration NrqlAlertCondition#expiration_duration}
        :param fill_option: Which strategy to use when filling gaps in the signal. If static, the 'fill value' will be used for filling gaps in the signal. Valid values are: 'NONE', 'LAST_VALUE', or 'STATIC' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#fill_option NrqlAlertCondition#fill_option}
        :param fill_value: If using the 'static' fill option, this value will be used for filling gaps in the signal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#fill_value NrqlAlertCondition#fill_value}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#id NrqlAlertCondition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param open_violation_on_expiration: Whether to create a new violation to capture that the signal expired. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#open_violation_on_expiration NrqlAlertCondition#open_violation_on_expiration}
        :param runbook_url: Runbook URL to display in notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#runbook_url NrqlAlertCondition#runbook_url}
        :param slide_by: The duration of overlapping timewindows used to smooth the chart line, in seconds. Must be a factor of ``aggregation_window`` and less than the aggregation window. It should be greater or equal to 30 seconds if ``aggregation_window`` is less than or equal to 3600 seconds, or greater or equal to ``aggregation_window / 120`` if ``aggregation_window`` is greater than 3600 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#slide_by NrqlAlertCondition#slide_by}
        :param term: term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#term NrqlAlertCondition#term}
        :param type: The type of NRQL alert condition to create. Valid values are: 'static', 'baseline'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#type NrqlAlertCondition#type}
        :param value_function: Values are: 'single_value' (deprecated) or 'sum' (deprecated). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#value_function NrqlAlertCondition#value_function}
        :param violation_time_limit: Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are 'ONE_HOUR', 'TWO_HOURS', 'FOUR_HOURS', 'EIGHT_HOURS', 'TWELVE_HOURS', 'TWENTY_FOUR_HOURS', 'THIRTY_DAYS' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#violation_time_limit NrqlAlertCondition#violation_time_limit}
        :param violation_time_limit_seconds: Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Must be in the range of 300 to 2592000 (inclusive) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#violation_time_limit_seconds NrqlAlertCondition#violation_time_limit_seconds}
        :param warning: warning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#warning NrqlAlertCondition#warning}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(nrql, dict):
            nrql = NrqlAlertConditionNrql(**nrql)
        if isinstance(critical, dict):
            critical = NrqlAlertConditionCritical(**critical)
        if isinstance(warning, dict):
            warning = NrqlAlertConditionWarning(**warning)
        if __debug__:
            type_hints = typing.get_type_hints(NrqlAlertConditionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument nrql", value=nrql, expected_type=type_hints["nrql"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument aggregation_delay", value=aggregation_delay, expected_type=type_hints["aggregation_delay"])
            check_type(argname="argument aggregation_method", value=aggregation_method, expected_type=type_hints["aggregation_method"])
            check_type(argname="argument aggregation_timer", value=aggregation_timer, expected_type=type_hints["aggregation_timer"])
            check_type(argname="argument aggregation_window", value=aggregation_window, expected_type=type_hints["aggregation_window"])
            check_type(argname="argument baseline_direction", value=baseline_direction, expected_type=type_hints["baseline_direction"])
            check_type(argname="argument close_violations_on_expiration", value=close_violations_on_expiration, expected_type=type_hints["close_violations_on_expiration"])
            check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument expiration_duration", value=expiration_duration, expected_type=type_hints["expiration_duration"])
            check_type(argname="argument fill_option", value=fill_option, expected_type=type_hints["fill_option"])
            check_type(argname="argument fill_value", value=fill_value, expected_type=type_hints["fill_value"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument open_violation_on_expiration", value=open_violation_on_expiration, expected_type=type_hints["open_violation_on_expiration"])
            check_type(argname="argument runbook_url", value=runbook_url, expected_type=type_hints["runbook_url"])
            check_type(argname="argument slide_by", value=slide_by, expected_type=type_hints["slide_by"])
            check_type(argname="argument term", value=term, expected_type=type_hints["term"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value_function", value=value_function, expected_type=type_hints["value_function"])
            check_type(argname="argument violation_time_limit", value=violation_time_limit, expected_type=type_hints["violation_time_limit"])
            check_type(argname="argument violation_time_limit_seconds", value=violation_time_limit_seconds, expected_type=type_hints["violation_time_limit_seconds"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "nrql": nrql,
            "policy_id": policy_id,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if aggregation_delay is not None:
            self._values["aggregation_delay"] = aggregation_delay
        if aggregation_method is not None:
            self._values["aggregation_method"] = aggregation_method
        if aggregation_timer is not None:
            self._values["aggregation_timer"] = aggregation_timer
        if aggregation_window is not None:
            self._values["aggregation_window"] = aggregation_window
        if baseline_direction is not None:
            self._values["baseline_direction"] = baseline_direction
        if close_violations_on_expiration is not None:
            self._values["close_violations_on_expiration"] = close_violations_on_expiration
        if critical is not None:
            self._values["critical"] = critical
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if expiration_duration is not None:
            self._values["expiration_duration"] = expiration_duration
        if fill_option is not None:
            self._values["fill_option"] = fill_option
        if fill_value is not None:
            self._values["fill_value"] = fill_value
        if id is not None:
            self._values["id"] = id
        if open_violation_on_expiration is not None:
            self._values["open_violation_on_expiration"] = open_violation_on_expiration
        if runbook_url is not None:
            self._values["runbook_url"] = runbook_url
        if slide_by is not None:
            self._values["slide_by"] = slide_by
        if term is not None:
            self._values["term"] = term
        if type is not None:
            self._values["type"] = type
        if value_function is not None:
            self._values["value_function"] = value_function
        if violation_time_limit is not None:
            self._values["violation_time_limit"] = violation_time_limit
        if violation_time_limit_seconds is not None:
            self._values["violation_time_limit_seconds"] = violation_time_limit_seconds
        if warning is not None:
            self._values["warning"] = warning

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
        '''The title of the condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#name NrqlAlertCondition#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nrql(self) -> "NrqlAlertConditionNrql":
        '''nrql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#nrql NrqlAlertCondition#nrql}
        '''
        result = self._values.get("nrql")
        assert result is not None, "Required property 'nrql' is missing"
        return typing.cast("NrqlAlertConditionNrql", result)

    @builtins.property
    def policy_id(self) -> jsii.Number:
        '''The ID of the policy where this condition should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#policy_id NrqlAlertCondition#policy_id}
        '''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The New Relic account ID for managing your NRQL alert conditions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#account_id NrqlAlertCondition#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def aggregation_delay(self) -> typing.Optional[builtins.str]:
        '''How long we wait for data that belongs in each aggregation window.

        Depending on your data, a longer delay may increase accuracy but delay notifications. Use aggregationDelay with the EVENT_FLOW and CADENCE aggregation methods.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_delay NrqlAlertCondition#aggregation_delay}
        '''
        result = self._values.get("aggregation_delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aggregation_method(self) -> typing.Optional[builtins.str]:
        '''The method that determines when we consider an aggregation window to be complete so that we can evaluate the signal for violations.

        Default is CADENCE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_method NrqlAlertCondition#aggregation_method}
        '''
        result = self._values.get("aggregation_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aggregation_timer(self) -> typing.Optional[builtins.str]:
        '''How long we wait after each data point arrives to make sure we've processed the whole batch.

        Use aggregationTimer with the EVENT_TIMER aggregation method.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_timer NrqlAlertCondition#aggregation_timer}
        '''
        result = self._values.get("aggregation_timer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aggregation_window(self) -> typing.Optional[jsii.Number]:
        '''The duration of the time window used to evaluate the NRQL query, in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#aggregation_window NrqlAlertCondition#aggregation_window}
        '''
        result = self._values.get("aggregation_window")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def baseline_direction(self) -> typing.Optional[builtins.str]:
        '''The baseline direction of a baseline NRQL alert condition. Valid values are: 'LOWER_ONLY', 'UPPER_AND_LOWER', 'UPPER_ONLY' (case insensitive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#baseline_direction NrqlAlertCondition#baseline_direction}
        '''
        result = self._values.get("baseline_direction")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def close_violations_on_expiration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to close all open violations when the signal expires.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#close_violations_on_expiration NrqlAlertCondition#close_violations_on_expiration}
        '''
        result = self._values.get("close_violations_on_expiration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def critical(self) -> typing.Optional["NrqlAlertConditionCritical"]:
        '''critical block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#critical NrqlAlertCondition#critical}
        '''
        result = self._values.get("critical")
        return typing.cast(typing.Optional["NrqlAlertConditionCritical"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the NRQL alert condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#description NrqlAlertCondition#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to enable the alert condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#enabled NrqlAlertCondition#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def expiration_duration(self) -> typing.Optional[jsii.Number]:
        '''The amount of time (in seconds) to wait before considering the signal expired.

        Must be in the range of 30 to 172800 (inclusive)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#expiration_duration NrqlAlertCondition#expiration_duration}
        '''
        result = self._values.get("expiration_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fill_option(self) -> typing.Optional[builtins.str]:
        '''Which strategy to use when filling gaps in the signal.

        If static, the 'fill value' will be used for filling gaps in the signal. Valid values are: 'NONE', 'LAST_VALUE', or 'STATIC' (case insensitive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#fill_option NrqlAlertCondition#fill_option}
        '''
        result = self._values.get("fill_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fill_value(self) -> typing.Optional[jsii.Number]:
        '''If using the 'static' fill option, this value will be used for filling gaps in the signal.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#fill_value NrqlAlertCondition#fill_value}
        '''
        result = self._values.get("fill_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#id NrqlAlertCondition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def open_violation_on_expiration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to create a new violation to capture that the signal expired.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#open_violation_on_expiration NrqlAlertCondition#open_violation_on_expiration}
        '''
        result = self._values.get("open_violation_on_expiration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def runbook_url(self) -> typing.Optional[builtins.str]:
        '''Runbook URL to display in notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#runbook_url NrqlAlertCondition#runbook_url}
        '''
        result = self._values.get("runbook_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slide_by(self) -> typing.Optional[jsii.Number]:
        '''The duration of overlapping timewindows used to smooth the chart line, in seconds.

        Must be a factor of ``aggregation_window`` and less than the aggregation window. It should be greater or equal to 30 seconds if ``aggregation_window`` is less than or equal to 3600 seconds, or greater or equal to ``aggregation_window / 120`` if ``aggregation_window`` is greater than 3600 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#slide_by NrqlAlertCondition#slide_by}
        '''
        result = self._values.get("slide_by")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def term(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NrqlAlertConditionTerm"]]]:
        '''term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#term NrqlAlertCondition#term}
        '''
        result = self._values.get("term")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NrqlAlertConditionTerm"]]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of NRQL alert condition to create. Valid values are: 'static', 'baseline'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#type NrqlAlertCondition#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_function(self) -> typing.Optional[builtins.str]:
        '''Values are: 'single_value' (deprecated) or 'sum' (deprecated).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#value_function NrqlAlertCondition#value_function}
        '''
        result = self._values.get("value_function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def violation_time_limit(self) -> typing.Optional[builtins.str]:
        '''Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select.

        Possible values are 'ONE_HOUR', 'TWO_HOURS', 'FOUR_HOURS', 'EIGHT_HOURS', 'TWELVE_HOURS', 'TWENTY_FOUR_HOURS', 'THIRTY_DAYS' (case insensitive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#violation_time_limit NrqlAlertCondition#violation_time_limit}
        '''
        result = self._values.get("violation_time_limit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def violation_time_limit_seconds(self) -> typing.Optional[jsii.Number]:
        '''Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select.

        Must be in the range of 300 to 2592000 (inclusive)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#violation_time_limit_seconds NrqlAlertCondition#violation_time_limit_seconds}
        '''
        result = self._values.get("violation_time_limit_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warning(self) -> typing.Optional["NrqlAlertConditionWarning"]:
        '''warning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#warning NrqlAlertCondition#warning}
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional["NrqlAlertConditionWarning"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NrqlAlertConditionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionCritical",
    jsii_struct_bases=[],
    name_mapping={
        "threshold": "threshold",
        "duration": "duration",
        "operator": "operator",
        "threshold_duration": "thresholdDuration",
        "threshold_occurrences": "thresholdOccurrences",
        "time_function": "timeFunction",
    },
)
class NrqlAlertConditionCritical:
    def __init__(
        self,
        *,
        threshold: jsii.Number,
        duration: typing.Optional[jsii.Number] = None,
        operator: typing.Optional[builtins.str] = None,
        threshold_duration: typing.Optional[jsii.Number] = None,
        threshold_occurrences: typing.Optional[builtins.str] = None,
        time_function: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param threshold: For baseline conditions must be in range [1, 1000]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold NrqlAlertCondition#threshold}
        :param duration: In minutes, must be in the range of 1 to 120 (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#duration NrqlAlertCondition#duration}
        :param operator: One of (above, above_or_equals, below, below_or_equals, equals, not_equals). Defaults to 'equals'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#operator NrqlAlertCondition#operator}
        :param threshold_duration: The duration, in seconds, that the threshold must violate in order to create a violation. Value must be a multiple of the 'aggregation_window' (which has a default of 60 seconds). Value must be within 120-3600 seconds for baseline conditions, within 120-7200 seconds for static conditions with the sum value function, and within 60-7200 seconds for static conditions with the single_value value function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_duration NrqlAlertCondition#threshold_duration}
        :param threshold_occurrences: The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: 'ALL' or 'AT_LEAST_ONCE' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_occurrences NrqlAlertCondition#threshold_occurrences}
        :param time_function: Valid values are: 'all' or 'any'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#time_function NrqlAlertCondition#time_function}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NrqlAlertConditionCritical.__init__)
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument threshold_duration", value=threshold_duration, expected_type=type_hints["threshold_duration"])
            check_type(argname="argument threshold_occurrences", value=threshold_occurrences, expected_type=type_hints["threshold_occurrences"])
            check_type(argname="argument time_function", value=time_function, expected_type=type_hints["time_function"])
        self._values: typing.Dict[str, typing.Any] = {
            "threshold": threshold,
        }
        if duration is not None:
            self._values["duration"] = duration
        if operator is not None:
            self._values["operator"] = operator
        if threshold_duration is not None:
            self._values["threshold_duration"] = threshold_duration
        if threshold_occurrences is not None:
            self._values["threshold_occurrences"] = threshold_occurrences
        if time_function is not None:
            self._values["time_function"] = time_function

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''For baseline conditions must be in range [1, 1000].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold NrqlAlertCondition#threshold}
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def duration(self) -> typing.Optional[jsii.Number]:
        '''In minutes, must be in the range of 1 to 120 (inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#duration NrqlAlertCondition#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''One of (above, above_or_equals, below, below_or_equals, equals, not_equals). Defaults to 'equals'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#operator NrqlAlertCondition#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_duration(self) -> typing.Optional[jsii.Number]:
        '''The duration, in seconds, that the threshold must violate in order to create a violation.

        Value must be a multiple of the 'aggregation_window' (which has a default of 60 seconds). Value must be within 120-3600 seconds for baseline conditions, within 120-7200 seconds for static conditions with the sum value function, and within 60-7200 seconds for static conditions with the single_value value function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_duration NrqlAlertCondition#threshold_duration}
        '''
        result = self._values.get("threshold_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def threshold_occurrences(self) -> typing.Optional[builtins.str]:
        '''The criteria for how many data points must be in violation for the specified threshold duration.

        Valid values are: 'ALL' or 'AT_LEAST_ONCE' (case insensitive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_occurrences NrqlAlertCondition#threshold_occurrences}
        '''
        result = self._values.get("threshold_occurrences")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_function(self) -> typing.Optional[builtins.str]:
        '''Valid values are: 'all' or 'any'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#time_function NrqlAlertCondition#time_function}
        '''
        result = self._values.get("time_function")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NrqlAlertConditionCritical(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NrqlAlertConditionCriticalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionCriticalOutputReference",
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
            type_hints = typing.get_type_hints(NrqlAlertConditionCriticalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetThresholdDuration")
    def reset_threshold_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdDuration", []))

    @jsii.member(jsii_name="resetThresholdOccurrences")
    def reset_threshold_occurrences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdOccurrences", []))

    @jsii.member(jsii_name="resetTimeFunction")
    def reset_time_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeFunction", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdDurationInput")
    def threshold_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdOccurrencesInput")
    def threshold_occurrences_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdOccurrencesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFunctionInput")
    def time_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionCriticalOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionCriticalOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionCriticalOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdDuration")
    def threshold_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdDuration"))

    @threshold_duration.setter
    def threshold_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionCriticalOutputReference, "threshold_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdDuration", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdOccurrences")
    def threshold_occurrences(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdOccurrences"))

    @threshold_occurrences.setter
    def threshold_occurrences(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionCriticalOutputReference, "threshold_occurrences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdOccurrences", value)

    @builtins.property
    @jsii.member(jsii_name="timeFunction")
    def time_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeFunction"))

    @time_function.setter
    def time_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionCriticalOutputReference, "time_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeFunction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NrqlAlertConditionCritical]:
        return typing.cast(typing.Optional[NrqlAlertConditionCritical], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NrqlAlertConditionCritical],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionCriticalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionNrql",
    jsii_struct_bases=[],
    name_mapping={
        "query": "query",
        "evaluation_offset": "evaluationOffset",
        "since_value": "sinceValue",
    },
)
class NrqlAlertConditionNrql:
    def __init__(
        self,
        *,
        query: builtins.str,
        evaluation_offset: typing.Optional[jsii.Number] = None,
        since_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#query NrqlAlertCondition#query}.
        :param evaluation_offset: NRQL queries are evaluated in one-minute time windows. The start time depends on the value you provide in the NRQL condition's ``evaluation_offset``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#evaluation_offset NrqlAlertCondition#evaluation_offset}
        :param since_value: NRQL queries are evaluated in one-minute time windows. The start time depends on the value you provide in the NRQL condition's ``since_value``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#since_value NrqlAlertCondition#since_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NrqlAlertConditionNrql.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument evaluation_offset", value=evaluation_offset, expected_type=type_hints["evaluation_offset"])
            check_type(argname="argument since_value", value=since_value, expected_type=type_hints["since_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if evaluation_offset is not None:
            self._values["evaluation_offset"] = evaluation_offset
        if since_value is not None:
            self._values["since_value"] = since_value

    @builtins.property
    def query(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#query NrqlAlertCondition#query}.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluation_offset(self) -> typing.Optional[jsii.Number]:
        '''NRQL queries are evaluated in one-minute time windows.

        The start time depends on the value you provide in the NRQL condition's ``evaluation_offset``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#evaluation_offset NrqlAlertCondition#evaluation_offset}
        '''
        result = self._values.get("evaluation_offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def since_value(self) -> typing.Optional[builtins.str]:
        '''NRQL queries are evaluated in one-minute time windows.

        The start time depends on the value you provide in the NRQL condition's ``since_value``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#since_value NrqlAlertCondition#since_value}
        '''
        result = self._values.get("since_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NrqlAlertConditionNrql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NrqlAlertConditionNrqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionNrqlOutputReference",
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
            type_hints = typing.get_type_hints(NrqlAlertConditionNrqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluationOffset")
    def reset_evaluation_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationOffset", []))

    @jsii.member(jsii_name="resetSinceValue")
    def reset_since_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSinceValue", []))

    @builtins.property
    @jsii.member(jsii_name="evaluationOffsetInput")
    def evaluation_offset_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="sinceValueInput")
    def since_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sinceValueInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationOffset")
    def evaluation_offset(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationOffset"))

    @evaluation_offset.setter
    def evaluation_offset(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionNrqlOutputReference, "evaluation_offset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationOffset", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionNrqlOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="sinceValue")
    def since_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sinceValue"))

    @since_value.setter
    def since_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionNrqlOutputReference, "since_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sinceValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NrqlAlertConditionNrql]:
        return typing.cast(typing.Optional[NrqlAlertConditionNrql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NrqlAlertConditionNrql]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionNrqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionTerm",
    jsii_struct_bases=[],
    name_mapping={
        "threshold": "threshold",
        "duration": "duration",
        "operator": "operator",
        "priority": "priority",
        "threshold_duration": "thresholdDuration",
        "threshold_occurrences": "thresholdOccurrences",
        "time_function": "timeFunction",
    },
)
class NrqlAlertConditionTerm:
    def __init__(
        self,
        *,
        threshold: jsii.Number,
        duration: typing.Optional[jsii.Number] = None,
        operator: typing.Optional[builtins.str] = None,
        priority: typing.Optional[builtins.str] = None,
        threshold_duration: typing.Optional[jsii.Number] = None,
        threshold_occurrences: typing.Optional[builtins.str] = None,
        time_function: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param threshold: For baseline conditions must be in range [1, 1000]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold NrqlAlertCondition#threshold}
        :param duration: In minutes, must be in the range of 1 to 120 (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#duration NrqlAlertCondition#duration}
        :param operator: One of (above, above_or_equals, below, below_or_equals, equals, not_equals). Defaults to 'equals'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#operator NrqlAlertCondition#operator}
        :param priority: One of (critical, warning). Defaults to 'critical'. At least one condition term must have priority set to 'critical'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#priority NrqlAlertCondition#priority}
        :param threshold_duration: The duration, in seconds, that the threshold must violate in order to create a violation. Value must be a multiple of the 'aggregation_window' (which has a default of 60 seconds). Value must be within 120-3600 seconds for baseline conditions, within 120-7200 seconds for static conditions with the sum value function, and within 60-7200 seconds for static conditions with the single_value value function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_duration NrqlAlertCondition#threshold_duration}
        :param threshold_occurrences: The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: 'ALL' or 'AT_LEAST_ONCE' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_occurrences NrqlAlertCondition#threshold_occurrences}
        :param time_function: Valid values are: 'all' or 'any'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#time_function NrqlAlertCondition#time_function}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NrqlAlertConditionTerm.__init__)
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument threshold_duration", value=threshold_duration, expected_type=type_hints["threshold_duration"])
            check_type(argname="argument threshold_occurrences", value=threshold_occurrences, expected_type=type_hints["threshold_occurrences"])
            check_type(argname="argument time_function", value=time_function, expected_type=type_hints["time_function"])
        self._values: typing.Dict[str, typing.Any] = {
            "threshold": threshold,
        }
        if duration is not None:
            self._values["duration"] = duration
        if operator is not None:
            self._values["operator"] = operator
        if priority is not None:
            self._values["priority"] = priority
        if threshold_duration is not None:
            self._values["threshold_duration"] = threshold_duration
        if threshold_occurrences is not None:
            self._values["threshold_occurrences"] = threshold_occurrences
        if time_function is not None:
            self._values["time_function"] = time_function

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''For baseline conditions must be in range [1, 1000].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold NrqlAlertCondition#threshold}
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def duration(self) -> typing.Optional[jsii.Number]:
        '''In minutes, must be in the range of 1 to 120 (inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#duration NrqlAlertCondition#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''One of (above, above_or_equals, below, below_or_equals, equals, not_equals). Defaults to 'equals'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#operator NrqlAlertCondition#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''One of (critical, warning). Defaults to 'critical'. At least one condition term must have priority set to 'critical'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#priority NrqlAlertCondition#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_duration(self) -> typing.Optional[jsii.Number]:
        '''The duration, in seconds, that the threshold must violate in order to create a violation.

        Value must be a multiple of the 'aggregation_window' (which has a default of 60 seconds). Value must be within 120-3600 seconds for baseline conditions, within 120-7200 seconds for static conditions with the sum value function, and within 60-7200 seconds for static conditions with the single_value value function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_duration NrqlAlertCondition#threshold_duration}
        '''
        result = self._values.get("threshold_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def threshold_occurrences(self) -> typing.Optional[builtins.str]:
        '''The criteria for how many data points must be in violation for the specified threshold duration.

        Valid values are: 'ALL' or 'AT_LEAST_ONCE' (case insensitive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_occurrences NrqlAlertCondition#threshold_occurrences}
        '''
        result = self._values.get("threshold_occurrences")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_function(self) -> typing.Optional[builtins.str]:
        '''Valid values are: 'all' or 'any'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#time_function NrqlAlertCondition#time_function}
        '''
        result = self._values.get("time_function")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NrqlAlertConditionTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NrqlAlertConditionTermList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionTermList",
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
            type_hints = typing.get_type_hints(NrqlAlertConditionTermList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NrqlAlertConditionTermOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NrqlAlertConditionTermList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NrqlAlertConditionTermOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NrqlAlertConditionTerm]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NrqlAlertConditionTerm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NrqlAlertConditionTerm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NrqlAlertConditionTermOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionTermOutputReference",
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
            type_hints = typing.get_type_hints(NrqlAlertConditionTermOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetThresholdDuration")
    def reset_threshold_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdDuration", []))

    @jsii.member(jsii_name="resetThresholdOccurrences")
    def reset_threshold_occurrences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdOccurrences", []))

    @jsii.member(jsii_name="resetTimeFunction")
    def reset_time_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeFunction", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdDurationInput")
    def threshold_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdOccurrencesInput")
    def threshold_occurrences_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdOccurrencesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFunctionInput")
    def time_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdDuration")
    def threshold_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdDuration"))

    @threshold_duration.setter
    def threshold_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermOutputReference, "threshold_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdDuration", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdOccurrences")
    def threshold_occurrences(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdOccurrences"))

    @threshold_occurrences.setter
    def threshold_occurrences(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermOutputReference, "threshold_occurrences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdOccurrences", value)

    @builtins.property
    @jsii.member(jsii_name="timeFunction")
    def time_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeFunction"))

    @time_function.setter
    def time_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermOutputReference, "time_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeFunction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NrqlAlertConditionTerm, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NrqlAlertConditionTerm, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NrqlAlertConditionTerm, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionTermOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionWarning",
    jsii_struct_bases=[],
    name_mapping={
        "threshold": "threshold",
        "duration": "duration",
        "operator": "operator",
        "threshold_duration": "thresholdDuration",
        "threshold_occurrences": "thresholdOccurrences",
        "time_function": "timeFunction",
    },
)
class NrqlAlertConditionWarning:
    def __init__(
        self,
        *,
        threshold: jsii.Number,
        duration: typing.Optional[jsii.Number] = None,
        operator: typing.Optional[builtins.str] = None,
        threshold_duration: typing.Optional[jsii.Number] = None,
        threshold_occurrences: typing.Optional[builtins.str] = None,
        time_function: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param threshold: For baseline conditions must be in range [1, 1000]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold NrqlAlertCondition#threshold}
        :param duration: In minutes, must be in the range of 1 to 120 (inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#duration NrqlAlertCondition#duration}
        :param operator: One of (above, above_or_equals, below, below_or_equals, equals, not_equals). Defaults to 'equals'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#operator NrqlAlertCondition#operator}
        :param threshold_duration: The duration, in seconds, that the threshold must violate in order to create a violation. Value must be a multiple of the 'aggregation_window' (which has a default of 60 seconds). Value must be within 120-3600 seconds for baseline conditions, within 120-7200 seconds for static conditions with the sum value function, and within 60-7200 seconds for static conditions with the single_value value function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_duration NrqlAlertCondition#threshold_duration}
        :param threshold_occurrences: The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: 'ALL' or 'AT_LEAST_ONCE' (case insensitive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_occurrences NrqlAlertCondition#threshold_occurrences}
        :param time_function: Valid values are: 'all' or 'any'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#time_function NrqlAlertCondition#time_function}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NrqlAlertConditionWarning.__init__)
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument threshold_duration", value=threshold_duration, expected_type=type_hints["threshold_duration"])
            check_type(argname="argument threshold_occurrences", value=threshold_occurrences, expected_type=type_hints["threshold_occurrences"])
            check_type(argname="argument time_function", value=time_function, expected_type=type_hints["time_function"])
        self._values: typing.Dict[str, typing.Any] = {
            "threshold": threshold,
        }
        if duration is not None:
            self._values["duration"] = duration
        if operator is not None:
            self._values["operator"] = operator
        if threshold_duration is not None:
            self._values["threshold_duration"] = threshold_duration
        if threshold_occurrences is not None:
            self._values["threshold_occurrences"] = threshold_occurrences
        if time_function is not None:
            self._values["time_function"] = time_function

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''For baseline conditions must be in range [1, 1000].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold NrqlAlertCondition#threshold}
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def duration(self) -> typing.Optional[jsii.Number]:
        '''In minutes, must be in the range of 1 to 120 (inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#duration NrqlAlertCondition#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''One of (above, above_or_equals, below, below_or_equals, equals, not_equals). Defaults to 'equals'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#operator NrqlAlertCondition#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_duration(self) -> typing.Optional[jsii.Number]:
        '''The duration, in seconds, that the threshold must violate in order to create a violation.

        Value must be a multiple of the 'aggregation_window' (which has a default of 60 seconds). Value must be within 120-3600 seconds for baseline conditions, within 120-7200 seconds for static conditions with the sum value function, and within 60-7200 seconds for static conditions with the single_value value function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_duration NrqlAlertCondition#threshold_duration}
        '''
        result = self._values.get("threshold_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def threshold_occurrences(self) -> typing.Optional[builtins.str]:
        '''The criteria for how many data points must be in violation for the specified threshold duration.

        Valid values are: 'ALL' or 'AT_LEAST_ONCE' (case insensitive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#threshold_occurrences NrqlAlertCondition#threshold_occurrences}
        '''
        result = self._values.get("threshold_occurrences")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_function(self) -> typing.Optional[builtins.str]:
        '''Valid values are: 'all' or 'any'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition#time_function NrqlAlertCondition#time_function}
        '''
        result = self._values.get("time_function")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NrqlAlertConditionWarning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NrqlAlertConditionWarningOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.nrqlAlertCondition.NrqlAlertConditionWarningOutputReference",
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
            type_hints = typing.get_type_hints(NrqlAlertConditionWarningOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetThresholdDuration")
    def reset_threshold_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdDuration", []))

    @jsii.member(jsii_name="resetThresholdOccurrences")
    def reset_threshold_occurrences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdOccurrences", []))

    @jsii.member(jsii_name="resetTimeFunction")
    def reset_time_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeFunction", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdDurationInput")
    def threshold_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdOccurrencesInput")
    def threshold_occurrences_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdOccurrencesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFunctionInput")
    def time_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionWarningOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionWarningOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionWarningOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdDuration")
    def threshold_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdDuration"))

    @threshold_duration.setter
    def threshold_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionWarningOutputReference, "threshold_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdDuration", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdOccurrences")
    def threshold_occurrences(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdOccurrences"))

    @threshold_occurrences.setter
    def threshold_occurrences(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionWarningOutputReference, "threshold_occurrences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdOccurrences", value)

    @builtins.property
    @jsii.member(jsii_name="timeFunction")
    def time_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeFunction"))

    @time_function.setter
    def time_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionWarningOutputReference, "time_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeFunction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NrqlAlertConditionWarning]:
        return typing.cast(typing.Optional[NrqlAlertConditionWarning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NrqlAlertConditionWarning]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NrqlAlertConditionWarningOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NrqlAlertCondition",
    "NrqlAlertConditionConfig",
    "NrqlAlertConditionCritical",
    "NrqlAlertConditionCriticalOutputReference",
    "NrqlAlertConditionNrql",
    "NrqlAlertConditionNrqlOutputReference",
    "NrqlAlertConditionTerm",
    "NrqlAlertConditionTermList",
    "NrqlAlertConditionTermOutputReference",
    "NrqlAlertConditionWarning",
    "NrqlAlertConditionWarningOutputReference",
]

publication.publish()
