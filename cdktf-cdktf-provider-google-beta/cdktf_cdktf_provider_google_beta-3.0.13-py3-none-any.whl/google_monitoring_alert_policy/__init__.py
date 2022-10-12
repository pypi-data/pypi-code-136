'''
# `google_monitoring_alert_policy`

Refer to the Terraform Registory for docs: [`google_monitoring_alert_policy`](https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy).
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


class GoogleMonitoringAlertPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy google_monitoring_alert_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        combiner: builtins.str,
        conditions: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditions", typing.Dict[str, typing.Any]]]],
        display_name: builtins.str,
        alert_strategy: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyAlertStrategy", typing.Dict[str, typing.Any]]] = None,
        documentation: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyDocumentation", typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy google_monitoring_alert_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param combiner: How to combine the results of multiple conditions to determine if an incident should be opened. Possible values: ["AND", "OR", "AND_WITH_MATCHING_RESOURCE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#combiner GoogleMonitoringAlertPolicy#combiner}
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#conditions GoogleMonitoringAlertPolicy#conditions}
        :param display_name: A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        :param alert_strategy: alert_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alert_strategy GoogleMonitoringAlertPolicy#alert_strategy}
        :param documentation: documentation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#documentation GoogleMonitoringAlertPolicy#documentation}
        :param enabled: Whether or not the policy is enabled. The default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#enabled GoogleMonitoringAlertPolicy#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#id GoogleMonitoringAlertPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_channels: Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_channels GoogleMonitoringAlertPolicy#notification_channels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#project GoogleMonitoringAlertPolicy#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#timeouts GoogleMonitoringAlertPolicy#timeouts}
        :param user_labels: This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#user_labels GoogleMonitoringAlertPolicy#user_labels}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleMonitoringAlertPolicyConfig(
            combiner=combiner,
            conditions=conditions,
            display_name=display_name,
            alert_strategy=alert_strategy,
            documentation=documentation,
            enabled=enabled,
            id=id,
            notification_channels=notification_channels,
            project=project,
            timeouts=timeouts,
            user_labels=user_labels,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlertStrategy")
    def put_alert_strategy(
        self,
        *,
        auto_close: typing.Optional[builtins.str] = None,
        notification_rate_limit: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_close: If an alert policy that was active has no data for this long, any open incidents will close. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#auto_close GoogleMonitoringAlertPolicy#auto_close}
        :param notification_rate_limit: notification_rate_limit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_rate_limit GoogleMonitoringAlertPolicy#notification_rate_limit}
        '''
        value = GoogleMonitoringAlertPolicyAlertStrategy(
            auto_close=auto_close, notification_rate_limit=notification_rate_limit
        )

        return typing.cast(None, jsii.invoke(self, "putAlertStrategy", [value]))

    @jsii.member(jsii_name="putConditions")
    def put_conditions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicy.put_conditions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditions", [value]))

    @jsii.member(jsii_name="putDocumentation")
    def put_documentation(
        self,
        *,
        content: typing.Optional[builtins.str] = None,
        mime_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: The text of the documentation, interpreted according to mimeType. The content may not exceed 8,192 Unicode characters and may not exceed more than 10,240 bytes when encoded in UTF-8 format, whichever is smaller. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#content GoogleMonitoringAlertPolicy#content}
        :param mime_type: The format of the content field. Presently, only the value "text/markdown" is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#mime_type GoogleMonitoringAlertPolicy#mime_type}
        '''
        value = GoogleMonitoringAlertPolicyDocumentation(
            content=content, mime_type=mime_type
        )

        return typing.cast(None, jsii.invoke(self, "putDocumentation", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#create GoogleMonitoringAlertPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#delete GoogleMonitoringAlertPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#update GoogleMonitoringAlertPolicy#update}.
        '''
        value = GoogleMonitoringAlertPolicyTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAlertStrategy")
    def reset_alert_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertStrategy", []))

    @jsii.member(jsii_name="resetDocumentation")
    def reset_documentation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentation", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotificationChannels")
    def reset_notification_channels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationChannels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserLabels")
    def reset_user_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserLabels", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alertStrategy")
    def alert_strategy(
        self,
    ) -> "GoogleMonitoringAlertPolicyAlertStrategyOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyAlertStrategyOutputReference", jsii.get(self, "alertStrategy"))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> "GoogleMonitoringAlertPolicyConditionsList":
        return typing.cast("GoogleMonitoringAlertPolicyConditionsList", jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="creationRecord")
    def creation_record(self) -> "GoogleMonitoringAlertPolicyCreationRecordList":
        return typing.cast("GoogleMonitoringAlertPolicyCreationRecordList", jsii.get(self, "creationRecord"))

    @builtins.property
    @jsii.member(jsii_name="documentation")
    def documentation(
        self,
    ) -> "GoogleMonitoringAlertPolicyDocumentationOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyDocumentationOutputReference", jsii.get(self, "documentation"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleMonitoringAlertPolicyTimeoutsOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="alertStrategyInput")
    def alert_strategy_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyAlertStrategy"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyAlertStrategy"], jsii.get(self, "alertStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="combinerInput")
    def combiner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "combinerInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionsInput")
    def conditions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditions"]]], jsii.get(self, "conditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="documentationInput")
    def documentation_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyDocumentation"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyDocumentation"], jsii.get(self, "documentationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationChannelsInput")
    def notification_channels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationChannelsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleMonitoringAlertPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleMonitoringAlertPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userLabelsInput")
    def user_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "userLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="combiner")
    def combiner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "combiner"))

    @combiner.setter
    def combiner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicy, "combiner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "combiner", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicy, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicy, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="notificationChannels")
    def notification_channels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationChannels"))

    @notification_channels.setter
    def notification_channels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicy, "notification_channels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationChannels", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicy, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="userLabels")
    def user_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "userLabels"))

    @user_labels.setter
    def user_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicy, "user_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userLabels", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyAlertStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "auto_close": "autoClose",
        "notification_rate_limit": "notificationRateLimit",
    },
)
class GoogleMonitoringAlertPolicyAlertStrategy:
    def __init__(
        self,
        *,
        auto_close: typing.Optional[builtins.str] = None,
        notification_rate_limit: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_close: If an alert policy that was active has no data for this long, any open incidents will close. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#auto_close GoogleMonitoringAlertPolicy#auto_close}
        :param notification_rate_limit: notification_rate_limit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_rate_limit GoogleMonitoringAlertPolicy#notification_rate_limit}
        '''
        if isinstance(notification_rate_limit, dict):
            notification_rate_limit = GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit(**notification_rate_limit)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyAlertStrategy.__init__)
            check_type(argname="argument auto_close", value=auto_close, expected_type=type_hints["auto_close"])
            check_type(argname="argument notification_rate_limit", value=notification_rate_limit, expected_type=type_hints["notification_rate_limit"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_close is not None:
            self._values["auto_close"] = auto_close
        if notification_rate_limit is not None:
            self._values["notification_rate_limit"] = notification_rate_limit

    @builtins.property
    def auto_close(self) -> typing.Optional[builtins.str]:
        '''If an alert policy that was active has no data for this long, any open incidents will close.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#auto_close GoogleMonitoringAlertPolicy#auto_close}
        '''
        result = self._values.get("auto_close")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_rate_limit(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit"]:
        '''notification_rate_limit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_rate_limit GoogleMonitoringAlertPolicy#notification_rate_limit}
        '''
        result = self._values.get("notification_rate_limit")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyAlertStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit",
    jsii_struct_bases=[],
    name_mapping={"period": "period"},
)
class GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit:
    def __init__(self, *, period: typing.Optional[builtins.str] = None) -> None:
        '''
        :param period: Not more than one notification per period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#period GoogleMonitoringAlertPolicy#period}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit.__init__)
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
        self._values: typing.Dict[str, typing.Any] = {}
        if period is not None:
            self._values["period"] = period

    @builtins.property
    def period(self) -> typing.Optional[builtins.str]:
        '''Not more than one notification per period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#period GoogleMonitoringAlertPolicy#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "period"))

    @period.setter
    def period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyAlertStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyAlertStrategyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyAlertStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNotificationRateLimit")
    def put_notification_rate_limit(
        self,
        *,
        period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param period: Not more than one notification per period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#period GoogleMonitoringAlertPolicy#period}
        '''
        value = GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit(
            period=period
        )

        return typing.cast(None, jsii.invoke(self, "putNotificationRateLimit", [value]))

    @jsii.member(jsii_name="resetAutoClose")
    def reset_auto_close(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoClose", []))

    @jsii.member(jsii_name="resetNotificationRateLimit")
    def reset_notification_rate_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationRateLimit", []))

    @builtins.property
    @jsii.member(jsii_name="notificationRateLimit")
    def notification_rate_limit(
        self,
    ) -> GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference, jsii.get(self, "notificationRateLimit"))

    @builtins.property
    @jsii.member(jsii_name="autoCloseInput")
    def auto_close_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoCloseInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationRateLimitInput")
    def notification_rate_limit_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit], jsii.get(self, "notificationRateLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="autoClose")
    def auto_close(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoClose"))

    @auto_close.setter
    def auto_close(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyAlertStrategyOutputReference, "auto_close").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoClose", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyAlertStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditions",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "condition_absent": "conditionAbsent",
        "condition_matched_log": "conditionMatchedLog",
        "condition_monitoring_query_language": "conditionMonitoringQueryLanguage",
        "condition_threshold": "conditionThreshold",
    },
)
class GoogleMonitoringAlertPolicyConditions:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        condition_absent: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionAbsent", typing.Dict[str, typing.Any]]] = None,
        condition_matched_log: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionMatchedLog", typing.Dict[str, typing.Any]]] = None,
        condition_monitoring_query_language: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage", typing.Dict[str, typing.Any]]] = None,
        condition_threshold: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionThreshold", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param display_name: A short name or phrase used to identify the condition in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple conditions in the same policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        :param condition_absent: condition_absent block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_absent GoogleMonitoringAlertPolicy#condition_absent}
        :param condition_matched_log: condition_matched_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_matched_log GoogleMonitoringAlertPolicy#condition_matched_log}
        :param condition_monitoring_query_language: condition_monitoring_query_language block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_monitoring_query_language GoogleMonitoringAlertPolicy#condition_monitoring_query_language}
        :param condition_threshold: condition_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_threshold GoogleMonitoringAlertPolicy#condition_threshold}
        '''
        if isinstance(condition_absent, dict):
            condition_absent = GoogleMonitoringAlertPolicyConditionsConditionAbsent(**condition_absent)
        if isinstance(condition_matched_log, dict):
            condition_matched_log = GoogleMonitoringAlertPolicyConditionsConditionMatchedLog(**condition_matched_log)
        if isinstance(condition_monitoring_query_language, dict):
            condition_monitoring_query_language = GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage(**condition_monitoring_query_language)
        if isinstance(condition_threshold, dict):
            condition_threshold = GoogleMonitoringAlertPolicyConditionsConditionThreshold(**condition_threshold)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditions.__init__)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument condition_absent", value=condition_absent, expected_type=type_hints["condition_absent"])
            check_type(argname="argument condition_matched_log", value=condition_matched_log, expected_type=type_hints["condition_matched_log"])
            check_type(argname="argument condition_monitoring_query_language", value=condition_monitoring_query_language, expected_type=type_hints["condition_monitoring_query_language"])
            check_type(argname="argument condition_threshold", value=condition_threshold, expected_type=type_hints["condition_threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
        }
        if condition_absent is not None:
            self._values["condition_absent"] = condition_absent
        if condition_matched_log is not None:
            self._values["condition_matched_log"] = condition_matched_log
        if condition_monitoring_query_language is not None:
            self._values["condition_monitoring_query_language"] = condition_monitoring_query_language
        if condition_threshold is not None:
            self._values["condition_threshold"] = condition_threshold

    @builtins.property
    def display_name(self) -> builtins.str:
        '''A short name or phrase used to identify the condition in dashboards, notifications, and incidents.

        To avoid confusion, don't use the same
        display name for multiple conditions in the same
        policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_absent(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsent"]:
        '''condition_absent block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_absent GoogleMonitoringAlertPolicy#condition_absent}
        '''
        result = self._values.get("condition_absent")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsent"], result)

    @builtins.property
    def condition_matched_log(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMatchedLog"]:
        '''condition_matched_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_matched_log GoogleMonitoringAlertPolicy#condition_matched_log}
        '''
        result = self._values.get("condition_matched_log")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMatchedLog"], result)

    @builtins.property
    def condition_monitoring_query_language(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage"]:
        '''condition_monitoring_query_language block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_monitoring_query_language GoogleMonitoringAlertPolicy#condition_monitoring_query_language}
        '''
        result = self._values.get("condition_monitoring_query_language")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage"], result)

    @builtins.property
    def condition_threshold(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThreshold"]:
        '''condition_threshold block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#condition_threshold GoogleMonitoringAlertPolicy#condition_threshold}
        '''
        result = self._values.get("condition_threshold")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThreshold"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsent",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "aggregations": "aggregations",
        "filter": "filter",
        "trigger": "trigger",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionAbsent:
    def __init__(
        self,
        *,
        duration: builtins.str,
        aggregations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations", typing.Dict[str, typing.Any]]]]] = None,
        filter: typing.Optional[builtins.str] = None,
        trigger: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param duration: The amount of time that a time series must fail to report new data to be considered failing. Currently, only values that are a multiple of a minute--e.g. 60s, 120s, or 300s --are supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param aggregations: aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        :param filter: A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        if isinstance(trigger, dict):
            trigger = GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsent.__init__)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument aggregations", value=aggregations, expected_type=type_hints["aggregations"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[str, typing.Any] = {
            "duration": duration,
        }
        if aggregations is not None:
            self._values["aggregations"] = aggregations
        if filter is not None:
            self._values["filter"] = filter
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def duration(self) -> builtins.str:
        '''The amount of time that a time series must fail to report new data to be considered failing.

        Currently, only values that are a
        multiple of a minute--e.g. 60s, 120s, or 300s
        --are supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aggregations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations"]]]:
        '''aggregations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        '''
        result = self._values.get("aggregations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations"]]], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger"]:
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionAbsent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations",
    jsii_struct_bases=[],
    name_mapping={
        "alignment_period": "alignmentPeriod",
        "cross_series_reducer": "crossSeriesReducer",
        "group_by_fields": "groupByFields",
        "per_series_aligner": "perSeriesAligner",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations:
    def __init__(
        self,
        *,
        alignment_period: typing.Optional[builtins.str] = None,
        cross_series_reducer: typing.Optional[builtins.str] = None,
        group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        per_series_aligner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alignment_period: The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        :param cross_series_reducer: The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        :param group_by_fields: The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        :param per_series_aligner: The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations.__init__)
            check_type(argname="argument alignment_period", value=alignment_period, expected_type=type_hints["alignment_period"])
            check_type(argname="argument cross_series_reducer", value=cross_series_reducer, expected_type=type_hints["cross_series_reducer"])
            check_type(argname="argument group_by_fields", value=group_by_fields, expected_type=type_hints["group_by_fields"])
            check_type(argname="argument per_series_aligner", value=per_series_aligner, expected_type=type_hints["per_series_aligner"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alignment_period is not None:
            self._values["alignment_period"] = alignment_period
        if cross_series_reducer is not None:
            self._values["cross_series_reducer"] = cross_series_reducer
        if group_by_fields is not None:
            self._values["group_by_fields"] = group_by_fields
        if per_series_aligner is not None:
            self._values["per_series_aligner"] = per_series_aligner

    @builtins.property
    def alignment_period(self) -> typing.Optional[builtins.str]:
        '''The alignment period for per-time series alignment.

        If present,
        alignmentPeriod must be at least
        60 seconds. After per-time series
        alignment, each time series will
        contain data points only on the
        period boundaries. If
        perSeriesAligner is not specified
        or equals ALIGN_NONE, then this
        field is ignored. If
        perSeriesAligner is specified and
        does not equal ALIGN_NONE, then
        this field must be defined;
        otherwise an error is returned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        '''
        result = self._values.get("alignment_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_series_reducer(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to combine time series.

        Not all reducer
        functions may be applied to all
        time series, depending on the
        metric type and the value type of
        the original time series.
        Reduction may change the metric
        type of value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        '''
        result = self._values.get("cross_series_reducer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of fields to preserve when crossSeriesReducer is specified.

        The groupByFields determine how
        the time series are partitioned
        into subsets prior to applying the
        aggregation function. Each subset
        contains time series that have the
        same value for each of the
        grouping fields. Each individual
        time series is a member of exactly
        one subset. The crossSeriesReducer
        is applied to each subset of time
        series. It is not possible to
        reduce across different resource
        types, so this field implicitly
        contains resource.type. Fields not
        specified in groupByFields are
        aggregated away. If groupByFields
        is not specified and all the time
        series have the same resource
        type, then the time series are
        aggregated into a single output
        time series. If crossSeriesReducer
        is not defined, this field is
        ignored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        '''
        result = self._values.get("group_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def per_series_aligner(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to align individual time series.

        Not all
        alignment functions may be applied
        to all time series, depending on
        the metric type and value type of
        the original time series.
        Alignment may change the metric
        type or the value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        result = self._values.get("per_series_aligner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAlignmentPeriod")
    def reset_alignment_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlignmentPeriod", []))

    @jsii.member(jsii_name="resetCrossSeriesReducer")
    def reset_cross_series_reducer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossSeriesReducer", []))

    @jsii.member(jsii_name="resetGroupByFields")
    def reset_group_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByFields", []))

    @jsii.member(jsii_name="resetPerSeriesAligner")
    def reset_per_series_aligner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerSeriesAligner", []))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriodInput")
    def alignment_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alignmentPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducerInput")
    def cross_series_reducer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossSeriesReducerInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByFieldsInput")
    def group_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="perSeriesAlignerInput")
    def per_series_aligner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perSeriesAlignerInput"))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriod")
    def alignment_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alignmentPeriod"))

    @alignment_period.setter
    def alignment_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference, "alignment_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alignmentPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducer")
    def cross_series_reducer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossSeriesReducer"))

    @cross_series_reducer.setter
    def cross_series_reducer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference, "cross_series_reducer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossSeriesReducer", value)

    @builtins.property
    @jsii.member(jsii_name="groupByFields")
    def group_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByFields"))

    @group_by_fields.setter
    def group_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference, "group_by_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByFields", value)

    @builtins.property
    @jsii.member(jsii_name="perSeriesAligner")
    def per_series_aligner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perSeriesAligner"))

    @per_series_aligner.setter
    def per_series_aligner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference, "per_series_aligner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perSeriesAligner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAggregations")
    def put_aggregations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference.put_aggregations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAggregations", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger(
            count=count, percent=percent
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="resetAggregations")
    def reset_aggregations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregations", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetTrigger")
    def reset_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrigger", []))

    @builtins.property
    @jsii.member(jsii_name="aggregations")
    def aggregations(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList, jsii.get(self, "aggregations"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="aggregationsInput")
    def aggregations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations]]], jsii.get(self, "aggregationsInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "percent": "percent"},
)
class GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if percent is not None:
            self._values["percent"] = percent

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The absolute number of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetPercent")
    def reset_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercent", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference, "percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMatchedLog",
    jsii_struct_bases=[],
    name_mapping={"filter": "filter", "label_extractors": "labelExtractors"},
)
class GoogleMonitoringAlertPolicyConditionsConditionMatchedLog:
    def __init__(
        self,
        *,
        filter: builtins.str,
        label_extractors: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param filter: A logs-based filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param label_extractors: A map from a label key to an extractor expression, which is used to extract the value for this label key. Each entry in this map is a specification for how data should be extracted from log entries that match filter. Each combination of extracted values is treated as a separate rule for the purposes of triggering notifications. Label keys and corresponding values can be used in notifications generated by this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#label_extractors GoogleMonitoringAlertPolicy#label_extractors}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionMatchedLog.__init__)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument label_extractors", value=label_extractors, expected_type=type_hints["label_extractors"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
        }
        if label_extractors is not None:
            self._values["label_extractors"] = label_extractors

    @builtins.property
    def filter(self) -> builtins.str:
        '''A logs-based filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_extractors(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map from a label key to an extractor expression, which is used to extract the value for this label key.

        Each entry in this map is
        a specification for how data should be extracted from log entries that
        match filter. Each combination of extracted values is treated as
        a separate rule for the purposes of triggering notifications.
        Label keys and corresponding values can be used in notifications
        generated by this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#label_extractors GoogleMonitoringAlertPolicy#label_extractors}
        '''
        result = self._values.get("label_extractors")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionMatchedLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLabelExtractors")
    def reset_label_extractors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelExtractors", []))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="labelExtractorsInput")
    def label_extractors_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelExtractorsInput"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="labelExtractors")
    def label_extractors(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labelExtractors"))

    @label_extractors.setter
    def label_extractors(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference, "label_extractors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelExtractors", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "query": "query",
        "evaluation_missing_data": "evaluationMissingData",
        "trigger": "trigger",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage:
    def __init__(
        self,
        *,
        duration: builtins.str,
        query: builtins.str,
        evaluation_missing_data: typing.Optional[builtins.str] = None,
        trigger: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param duration: The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param query: Monitoring Query Language query that outputs a boolean stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#query GoogleMonitoringAlertPolicy#query}
        :param evaluation_missing_data: A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        if isinstance(trigger, dict):
            trigger = GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage.__init__)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument evaluation_missing_data", value=evaluation_missing_data, expected_type=type_hints["evaluation_missing_data"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[str, typing.Any] = {
            "duration": duration,
            "query": query,
        }
        if evaluation_missing_data is not None:
            self._values["evaluation_missing_data"] = evaluation_missing_data
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def duration(self) -> builtins.str:
        '''The amount of time that a time series must violate the threshold to be considered failing.

        Currently, only values that are a
        multiple of a minute--e.g., 0, 60, 120, or
        300 seconds--are supported. If an invalid
        value is given, an error will be returned.
        When choosing a duration, it is useful to
        keep in mind the frequency of the underlying
        time series data (which may also be affected
        by any alignments specified in the
        aggregations field); a good duration is long
        enough so that a single outlier does not
        generate spurious alerts, but short enough
        that unhealthy states are detected and
        alerted on quickly.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Monitoring Query Language query that outputs a boolean stream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#query GoogleMonitoringAlertPolicy#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluation_missing_data(self) -> typing.Optional[builtins.str]:
        '''A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        '''
        result = self._values.get("evaluation_missing_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger"]:
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger(
            count=count, percent=percent
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="resetEvaluationMissingData")
    def reset_evaluation_missing_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationMissingData", []))

    @jsii.member(jsii_name="resetTrigger")
    def reset_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrigger", []))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationMissingDataInput")
    def evaluation_missing_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationMissingDataInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationMissingData")
    def evaluation_missing_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluationMissingData"))

    @evaluation_missing_data.setter
    def evaluation_missing_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference, "evaluation_missing_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationMissingData", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "percent": "percent"},
)
class GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if percent is not None:
            self._values["percent"] = percent

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The absolute number of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetPercent")
    def reset_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercent", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference, "percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThreshold",
    jsii_struct_bases=[],
    name_mapping={
        "comparison": "comparison",
        "duration": "duration",
        "aggregations": "aggregations",
        "denominator_aggregations": "denominatorAggregations",
        "denominator_filter": "denominatorFilter",
        "evaluation_missing_data": "evaluationMissingData",
        "filter": "filter",
        "threshold_value": "thresholdValue",
        "trigger": "trigger",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionThreshold:
    def __init__(
        self,
        *,
        comparison: builtins.str,
        duration: builtins.str,
        aggregations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations", typing.Dict[str, typing.Any]]]]] = None,
        denominator_aggregations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations", typing.Dict[str, typing.Any]]]]] = None,
        denominator_filter: typing.Optional[builtins.str] = None,
        evaluation_missing_data: typing.Optional[builtins.str] = None,
        filter: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
        trigger: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param comparison: The comparison to apply between the time series (indicated by filter and aggregation) and the threshold (indicated by threshold_value). The comparison is applied on each time series, with the time series on the left-hand side and the threshold on the right-hand side. Only COMPARISON_LT and COMPARISON_GT are supported currently. Possible values: ["COMPARISON_GT", "COMPARISON_GE", "COMPARISON_LT", "COMPARISON_LE", "COMPARISON_EQ", "COMPARISON_NE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#comparison GoogleMonitoringAlertPolicy#comparison}
        :param duration: The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param aggregations: aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        :param denominator_aggregations: denominator_aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_aggregations GoogleMonitoringAlertPolicy#denominator_aggregations}
        :param denominator_filter: A filter that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold. If a denominator_filter is specified, the time series specified by the filter field will be used as the numerator.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_filter GoogleMonitoringAlertPolicy#denominator_filter}
        :param evaluation_missing_data: A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        :param filter: A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param threshold_value: A value against which to compare the time series. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#threshold_value GoogleMonitoringAlertPolicy#threshold_value}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        if isinstance(trigger, dict):
            trigger = GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThreshold.__init__)
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument aggregations", value=aggregations, expected_type=type_hints["aggregations"])
            check_type(argname="argument denominator_aggregations", value=denominator_aggregations, expected_type=type_hints["denominator_aggregations"])
            check_type(argname="argument denominator_filter", value=denominator_filter, expected_type=type_hints["denominator_filter"])
            check_type(argname="argument evaluation_missing_data", value=evaluation_missing_data, expected_type=type_hints["evaluation_missing_data"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument threshold_value", value=threshold_value, expected_type=type_hints["threshold_value"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[str, typing.Any] = {
            "comparison": comparison,
            "duration": duration,
        }
        if aggregations is not None:
            self._values["aggregations"] = aggregations
        if denominator_aggregations is not None:
            self._values["denominator_aggregations"] = denominator_aggregations
        if denominator_filter is not None:
            self._values["denominator_filter"] = denominator_filter
        if evaluation_missing_data is not None:
            self._values["evaluation_missing_data"] = evaluation_missing_data
        if filter is not None:
            self._values["filter"] = filter
        if threshold_value is not None:
            self._values["threshold_value"] = threshold_value
        if trigger is not None:
            self._values["trigger"] = trigger

    @builtins.property
    def comparison(self) -> builtins.str:
        '''The comparison to apply between the time series (indicated by filter and aggregation) and the threshold (indicated by threshold_value).

        The comparison is applied
        on each time series, with the time series on
        the left-hand side and the threshold on the
        right-hand side. Only COMPARISON_LT and
        COMPARISON_GT are supported currently. Possible values: ["COMPARISON_GT", "COMPARISON_GE", "COMPARISON_LT", "COMPARISON_LE", "COMPARISON_EQ", "COMPARISON_NE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#comparison GoogleMonitoringAlertPolicy#comparison}
        '''
        result = self._values.get("comparison")
        assert result is not None, "Required property 'comparison' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration(self) -> builtins.str:
        '''The amount of time that a time series must violate the threshold to be considered failing.

        Currently, only values that are a
        multiple of a minute--e.g., 0, 60, 120, or
        300 seconds--are supported. If an invalid
        value is given, an error will be returned.
        When choosing a duration, it is useful to
        keep in mind the frequency of the underlying
        time series data (which may also be affected
        by any alignments specified in the
        aggregations field); a good duration is long
        enough so that a single outlier does not
        generate spurious alerts, but short enough
        that unhealthy states are detected and
        alerted on quickly.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aggregations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations"]]]:
        '''aggregations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        '''
        result = self._values.get("aggregations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations"]]], result)

    @builtins.property
    def denominator_aggregations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations"]]]:
        '''denominator_aggregations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_aggregations GoogleMonitoringAlertPolicy#denominator_aggregations}
        '''
        result = self._values.get("denominator_aggregations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations"]]], result)

    @builtins.property
    def denominator_filter(self) -> typing.Optional[builtins.str]:
        '''A filter that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold.

        If
        a denominator_filter is specified, the time
        series specified by the filter field will be
        used as the numerator.The filter is similar
        to the one that is specified in the
        MetricService.ListTimeSeries request (that
        call is useful to verify the time series
        that will be retrieved / processed) and must
        specify the metric type and optionally may
        contain restrictions on resource type,
        resource labels, and metric labels. This
        field may not exceed 2048 Unicode characters
        in length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_filter GoogleMonitoringAlertPolicy#denominator_filter}
        '''
        result = self._values.get("denominator_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_missing_data(self) -> typing.Optional[builtins.str]:
        '''A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        '''
        result = self._values.get("evaluation_missing_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_value(self) -> typing.Optional[jsii.Number]:
        '''A value against which to compare the time series.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#threshold_value GoogleMonitoringAlertPolicy#threshold_value}
        '''
        result = self._values.get("threshold_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def trigger(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger"]:
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        result = self._values.get("trigger")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionThreshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations",
    jsii_struct_bases=[],
    name_mapping={
        "alignment_period": "alignmentPeriod",
        "cross_series_reducer": "crossSeriesReducer",
        "group_by_fields": "groupByFields",
        "per_series_aligner": "perSeriesAligner",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations:
    def __init__(
        self,
        *,
        alignment_period: typing.Optional[builtins.str] = None,
        cross_series_reducer: typing.Optional[builtins.str] = None,
        group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        per_series_aligner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alignment_period: The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        :param cross_series_reducer: The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        :param group_by_fields: The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        :param per_series_aligner: The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations.__init__)
            check_type(argname="argument alignment_period", value=alignment_period, expected_type=type_hints["alignment_period"])
            check_type(argname="argument cross_series_reducer", value=cross_series_reducer, expected_type=type_hints["cross_series_reducer"])
            check_type(argname="argument group_by_fields", value=group_by_fields, expected_type=type_hints["group_by_fields"])
            check_type(argname="argument per_series_aligner", value=per_series_aligner, expected_type=type_hints["per_series_aligner"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alignment_period is not None:
            self._values["alignment_period"] = alignment_period
        if cross_series_reducer is not None:
            self._values["cross_series_reducer"] = cross_series_reducer
        if group_by_fields is not None:
            self._values["group_by_fields"] = group_by_fields
        if per_series_aligner is not None:
            self._values["per_series_aligner"] = per_series_aligner

    @builtins.property
    def alignment_period(self) -> typing.Optional[builtins.str]:
        '''The alignment period for per-time series alignment.

        If present,
        alignmentPeriod must be at least
        60 seconds. After per-time series
        alignment, each time series will
        contain data points only on the
        period boundaries. If
        perSeriesAligner is not specified
        or equals ALIGN_NONE, then this
        field is ignored. If
        perSeriesAligner is specified and
        does not equal ALIGN_NONE, then
        this field must be defined;
        otherwise an error is returned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        '''
        result = self._values.get("alignment_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_series_reducer(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to combine time series.

        Not all reducer
        functions may be applied to all
        time series, depending on the
        metric type and the value type of
        the original time series.
        Reduction may change the metric
        type of value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        '''
        result = self._values.get("cross_series_reducer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of fields to preserve when crossSeriesReducer is specified.

        The groupByFields determine how
        the time series are partitioned
        into subsets prior to applying the
        aggregation function. Each subset
        contains time series that have the
        same value for each of the
        grouping fields. Each individual
        time series is a member of exactly
        one subset. The crossSeriesReducer
        is applied to each subset of time
        series. It is not possible to
        reduce across different resource
        types, so this field implicitly
        contains resource.type. Fields not
        specified in groupByFields are
        aggregated away. If groupByFields
        is not specified and all the time
        series have the same resource
        type, then the time series are
        aggregated into a single output
        time series. If crossSeriesReducer
        is not defined, this field is
        ignored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        '''
        result = self._values.get("group_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def per_series_aligner(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to align individual time series.

        Not all
        alignment functions may be applied
        to all time series, depending on
        the metric type and value type of
        the original time series.
        Alignment may change the metric
        type or the value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        result = self._values.get("per_series_aligner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAlignmentPeriod")
    def reset_alignment_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlignmentPeriod", []))

    @jsii.member(jsii_name="resetCrossSeriesReducer")
    def reset_cross_series_reducer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossSeriesReducer", []))

    @jsii.member(jsii_name="resetGroupByFields")
    def reset_group_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByFields", []))

    @jsii.member(jsii_name="resetPerSeriesAligner")
    def reset_per_series_aligner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerSeriesAligner", []))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriodInput")
    def alignment_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alignmentPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducerInput")
    def cross_series_reducer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossSeriesReducerInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByFieldsInput")
    def group_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="perSeriesAlignerInput")
    def per_series_aligner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perSeriesAlignerInput"))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriod")
    def alignment_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alignmentPeriod"))

    @alignment_period.setter
    def alignment_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference, "alignment_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alignmentPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducer")
    def cross_series_reducer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossSeriesReducer"))

    @cross_series_reducer.setter
    def cross_series_reducer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference, "cross_series_reducer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossSeriesReducer", value)

    @builtins.property
    @jsii.member(jsii_name="groupByFields")
    def group_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByFields"))

    @group_by_fields.setter
    def group_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference, "group_by_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByFields", value)

    @builtins.property
    @jsii.member(jsii_name="perSeriesAligner")
    def per_series_aligner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perSeriesAligner"))

    @per_series_aligner.setter
    def per_series_aligner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference, "per_series_aligner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perSeriesAligner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations",
    jsii_struct_bases=[],
    name_mapping={
        "alignment_period": "alignmentPeriod",
        "cross_series_reducer": "crossSeriesReducer",
        "group_by_fields": "groupByFields",
        "per_series_aligner": "perSeriesAligner",
    },
)
class GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations:
    def __init__(
        self,
        *,
        alignment_period: typing.Optional[builtins.str] = None,
        cross_series_reducer: typing.Optional[builtins.str] = None,
        group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        per_series_aligner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alignment_period: The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        :param cross_series_reducer: The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        :param group_by_fields: The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        :param per_series_aligner: The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations.__init__)
            check_type(argname="argument alignment_period", value=alignment_period, expected_type=type_hints["alignment_period"])
            check_type(argname="argument cross_series_reducer", value=cross_series_reducer, expected_type=type_hints["cross_series_reducer"])
            check_type(argname="argument group_by_fields", value=group_by_fields, expected_type=type_hints["group_by_fields"])
            check_type(argname="argument per_series_aligner", value=per_series_aligner, expected_type=type_hints["per_series_aligner"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alignment_period is not None:
            self._values["alignment_period"] = alignment_period
        if cross_series_reducer is not None:
            self._values["cross_series_reducer"] = cross_series_reducer
        if group_by_fields is not None:
            self._values["group_by_fields"] = group_by_fields
        if per_series_aligner is not None:
            self._values["per_series_aligner"] = per_series_aligner

    @builtins.property
    def alignment_period(self) -> typing.Optional[builtins.str]:
        '''The alignment period for per-time series alignment.

        If present,
        alignmentPeriod must be at least
        60 seconds. After per-time series
        alignment, each time series will
        contain data points only on the
        period boundaries. If
        perSeriesAligner is not specified
        or equals ALIGN_NONE, then this
        field is ignored. If
        perSeriesAligner is specified and
        does not equal ALIGN_NONE, then
        this field must be defined;
        otherwise an error is returned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alignment_period GoogleMonitoringAlertPolicy#alignment_period}
        '''
        result = self._values.get("alignment_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_series_reducer(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to combine time series.

        Not all reducer
        functions may be applied to all
        time series, depending on the
        metric type and the value type of
        the original time series.
        Reduction may change the metric
        type of value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#cross_series_reducer GoogleMonitoringAlertPolicy#cross_series_reducer}
        '''
        result = self._values.get("cross_series_reducer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of fields to preserve when crossSeriesReducer is specified.

        The groupByFields determine how
        the time series are partitioned
        into subsets prior to applying the
        aggregation function. Each subset
        contains time series that have the
        same value for each of the
        grouping fields. Each individual
        time series is a member of exactly
        one subset. The crossSeriesReducer
        is applied to each subset of time
        series. It is not possible to
        reduce across different resource
        types, so this field implicitly
        contains resource.type. Fields not
        specified in groupByFields are
        aggregated away. If groupByFields
        is not specified and all the time
        series have the same resource
        type, then the time series are
        aggregated into a single output
        time series. If crossSeriesReducer
        is not defined, this field is
        ignored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#group_by_fields GoogleMonitoringAlertPolicy#group_by_fields}
        '''
        result = self._values.get("group_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def per_series_aligner(self) -> typing.Optional[builtins.str]:
        '''The approach to be used to align individual time series.

        Not all
        alignment functions may be applied
        to all time series, depending on
        the metric type and value type of
        the original time series.
        Alignment may change the metric
        type or the value type of the time
        series.Time series data must be
        aligned in order to perform cross-
        time series reduction. If
        crossSeriesReducer is specified,
        then perSeriesAligner must be
        specified and not equal ALIGN_NONE
        and alignmentPeriod must be
        specified; otherwise, an error is
        returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#per_series_aligner GoogleMonitoringAlertPolicy#per_series_aligner}
        '''
        result = self._values.get("per_series_aligner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAlignmentPeriod")
    def reset_alignment_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlignmentPeriod", []))

    @jsii.member(jsii_name="resetCrossSeriesReducer")
    def reset_cross_series_reducer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossSeriesReducer", []))

    @jsii.member(jsii_name="resetGroupByFields")
    def reset_group_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByFields", []))

    @jsii.member(jsii_name="resetPerSeriesAligner")
    def reset_per_series_aligner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerSeriesAligner", []))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriodInput")
    def alignment_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alignmentPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducerInput")
    def cross_series_reducer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossSeriesReducerInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByFieldsInput")
    def group_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="perSeriesAlignerInput")
    def per_series_aligner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perSeriesAlignerInput"))

    @builtins.property
    @jsii.member(jsii_name="alignmentPeriod")
    def alignment_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alignmentPeriod"))

    @alignment_period.setter
    def alignment_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference, "alignment_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alignmentPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="crossSeriesReducer")
    def cross_series_reducer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossSeriesReducer"))

    @cross_series_reducer.setter
    def cross_series_reducer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference, "cross_series_reducer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossSeriesReducer", value)

    @builtins.property
    @jsii.member(jsii_name="groupByFields")
    def group_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByFields"))

    @group_by_fields.setter
    def group_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference, "group_by_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByFields", value)

    @builtins.property
    @jsii.member(jsii_name="perSeriesAligner")
    def per_series_aligner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perSeriesAligner"))

    @per_series_aligner.setter
    def per_series_aligner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference, "per_series_aligner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perSeriesAligner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAggregations")
    def put_aggregations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference.put_aggregations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAggregations", [value]))

    @jsii.member(jsii_name="putDenominatorAggregations")
    def put_denominator_aggregations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference.put_denominator_aggregations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDenominatorAggregations", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger(
            count=count, percent=percent
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="resetAggregations")
    def reset_aggregations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregations", []))

    @jsii.member(jsii_name="resetDenominatorAggregations")
    def reset_denominator_aggregations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDenominatorAggregations", []))

    @jsii.member(jsii_name="resetDenominatorFilter")
    def reset_denominator_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDenominatorFilter", []))

    @jsii.member(jsii_name="resetEvaluationMissingData")
    def reset_evaluation_missing_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationMissingData", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetThresholdValue")
    def reset_threshold_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdValue", []))

    @jsii.member(jsii_name="resetTrigger")
    def reset_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrigger", []))

    @builtins.property
    @jsii.member(jsii_name="aggregations")
    def aggregations(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList, jsii.get(self, "aggregations"))

    @builtins.property
    @jsii.member(jsii_name="denominatorAggregations")
    def denominator_aggregations(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList, jsii.get(self, "denominatorAggregations"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference":
        return typing.cast("GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="aggregationsInput")
    def aggregations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations]]], jsii.get(self, "aggregationsInput"))

    @builtins.property
    @jsii.member(jsii_name="comparisonInput")
    def comparison_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparisonInput"))

    @builtins.property
    @jsii.member(jsii_name="denominatorAggregationsInput")
    def denominator_aggregations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations]]], jsii.get(self, "denominatorAggregationsInput"))

    @builtins.property
    @jsii.member(jsii_name="denominatorFilterInput")
    def denominator_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "denominatorFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationMissingDataInput")
    def evaluation_missing_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationMissingDataInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdValueInput")
    def threshold_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdValueInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger"]:
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="comparison")
    def comparison(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparison"))

    @comparison.setter
    def comparison(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, "comparison").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparison", value)

    @builtins.property
    @jsii.member(jsii_name="denominatorFilter")
    def denominator_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "denominatorFilter"))

    @denominator_filter.setter
    def denominator_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, "denominator_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "denominatorFilter", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationMissingData")
    def evaluation_missing_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluationMissingData"))

    @evaluation_missing_data.setter
    def evaluation_missing_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, "evaluation_missing_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationMissingData", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdValue")
    def threshold_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdValue"))

    @threshold_value.setter
    def threshold_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, "threshold_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "percent": "percent"},
)
class GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: The absolute number of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        :param percent: The percentage of time series that must fail the predicate for the condition to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if percent is not None:
            self._values["percent"] = percent

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The absolute number of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#count GoogleMonitoringAlertPolicy#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of time series that must fail the predicate for the condition to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#percent GoogleMonitoringAlertPolicy#percent}
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetPercent")
    def reset_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercent", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference, "percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsList",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyConditionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyConditionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleMonitoringAlertPolicyConditionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConditionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConditionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putConditionAbsent")
    def put_condition_absent(
        self,
        *,
        duration: builtins.str,
        aggregations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations, typing.Dict[str, typing.Any]]]]] = None,
        filter: typing.Optional[builtins.str] = None,
        trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param duration: The amount of time that a time series must fail to report new data to be considered failing. Currently, only values that are a multiple of a minute--e.g. 60s, 120s, or 300s --are supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param aggregations: aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        :param filter: A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionAbsent(
            duration=duration,
            aggregations=aggregations,
            filter=filter,
            trigger=trigger,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionAbsent", [value]))

    @jsii.member(jsii_name="putConditionMatchedLog")
    def put_condition_matched_log(
        self,
        *,
        filter: builtins.str,
        label_extractors: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param filter: A logs-based filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param label_extractors: A map from a label key to an extractor expression, which is used to extract the value for this label key. Each entry in this map is a specification for how data should be extracted from log entries that match filter. Each combination of extracted values is treated as a separate rule for the purposes of triggering notifications. Label keys and corresponding values can be used in notifications generated by this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#label_extractors GoogleMonitoringAlertPolicy#label_extractors}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionMatchedLog(
            filter=filter, label_extractors=label_extractors
        )

        return typing.cast(None, jsii.invoke(self, "putConditionMatchedLog", [value]))

    @jsii.member(jsii_name="putConditionMonitoringQueryLanguage")
    def put_condition_monitoring_query_language(
        self,
        *,
        duration: builtins.str,
        query: builtins.str,
        evaluation_missing_data: typing.Optional[builtins.str] = None,
        trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param duration: The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param query: Monitoring Query Language query that outputs a boolean stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#query GoogleMonitoringAlertPolicy#query}
        :param evaluation_missing_data: A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage(
            duration=duration,
            query=query,
            evaluation_missing_data=evaluation_missing_data,
            trigger=trigger,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionMonitoringQueryLanguage", [value]))

    @jsii.member(jsii_name="putConditionThreshold")
    def put_condition_threshold(
        self,
        *,
        comparison: builtins.str,
        duration: builtins.str,
        aggregations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations, typing.Dict[str, typing.Any]]]]] = None,
        denominator_aggregations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations, typing.Dict[str, typing.Any]]]]] = None,
        denominator_filter: typing.Optional[builtins.str] = None,
        evaluation_missing_data: typing.Optional[builtins.str] = None,
        filter: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
        trigger: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param comparison: The comparison to apply between the time series (indicated by filter and aggregation) and the threshold (indicated by threshold_value). The comparison is applied on each time series, with the time series on the left-hand side and the threshold on the right-hand side. Only COMPARISON_LT and COMPARISON_GT are supported currently. Possible values: ["COMPARISON_GT", "COMPARISON_GE", "COMPARISON_LT", "COMPARISON_LE", "COMPARISON_EQ", "COMPARISON_NE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#comparison GoogleMonitoringAlertPolicy#comparison}
        :param duration: The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#duration GoogleMonitoringAlertPolicy#duration}
        :param aggregations: aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#aggregations GoogleMonitoringAlertPolicy#aggregations}
        :param denominator_aggregations: denominator_aggregations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_aggregations GoogleMonitoringAlertPolicy#denominator_aggregations}
        :param denominator_filter: A filter that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold. If a denominator_filter is specified, the time series specified by the filter field will be used as the numerator.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#denominator_filter GoogleMonitoringAlertPolicy#denominator_filter}
        :param evaluation_missing_data: A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#evaluation_missing_data GoogleMonitoringAlertPolicy#evaluation_missing_data}
        :param filter: A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#filter GoogleMonitoringAlertPolicy#filter}
        :param threshold_value: A value against which to compare the time series. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#threshold_value GoogleMonitoringAlertPolicy#threshold_value}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#trigger GoogleMonitoringAlertPolicy#trigger}
        '''
        value = GoogleMonitoringAlertPolicyConditionsConditionThreshold(
            comparison=comparison,
            duration=duration,
            aggregations=aggregations,
            denominator_aggregations=denominator_aggregations,
            denominator_filter=denominator_filter,
            evaluation_missing_data=evaluation_missing_data,
            filter=filter,
            threshold_value=threshold_value,
            trigger=trigger,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionThreshold", [value]))

    @jsii.member(jsii_name="resetConditionAbsent")
    def reset_condition_absent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionAbsent", []))

    @jsii.member(jsii_name="resetConditionMatchedLog")
    def reset_condition_matched_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionMatchedLog", []))

    @jsii.member(jsii_name="resetConditionMonitoringQueryLanguage")
    def reset_condition_monitoring_query_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionMonitoringQueryLanguage", []))

    @jsii.member(jsii_name="resetConditionThreshold")
    def reset_condition_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="conditionAbsent")
    def condition_absent(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference, jsii.get(self, "conditionAbsent"))

    @builtins.property
    @jsii.member(jsii_name="conditionMatchedLog")
    def condition_matched_log(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference, jsii.get(self, "conditionMatchedLog"))

    @builtins.property
    @jsii.member(jsii_name="conditionMonitoringQueryLanguage")
    def condition_monitoring_query_language(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference, jsii.get(self, "conditionMonitoringQueryLanguage"))

    @builtins.property
    @jsii.member(jsii_name="conditionThreshold")
    def condition_threshold(
        self,
    ) -> GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference:
        return typing.cast(GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference, jsii.get(self, "conditionThreshold"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="conditionAbsentInput")
    def condition_absent_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionAbsent], jsii.get(self, "conditionAbsentInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionMatchedLogInput")
    def condition_matched_log_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMatchedLog], jsii.get(self, "conditionMatchedLogInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionMonitoringQueryLanguageInput")
    def condition_monitoring_query_language_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage], jsii.get(self, "conditionMonitoringQueryLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionThresholdInput")
    def condition_threshold_input(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyConditionsConditionThreshold], jsii.get(self, "conditionThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsOutputReference, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyConditions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyConditionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "combiner": "combiner",
        "conditions": "conditions",
        "display_name": "displayName",
        "alert_strategy": "alertStrategy",
        "documentation": "documentation",
        "enabled": "enabled",
        "id": "id",
        "notification_channels": "notificationChannels",
        "project": "project",
        "timeouts": "timeouts",
        "user_labels": "userLabels",
    },
)
class GoogleMonitoringAlertPolicyConfig(cdktf.TerraformMetaArguments):
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
        combiner: builtins.str,
        conditions: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleMonitoringAlertPolicyConditions, typing.Dict[str, typing.Any]]]],
        display_name: builtins.str,
        alert_strategy: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyAlertStrategy, typing.Dict[str, typing.Any]]] = None,
        documentation: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyDocumentation", typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        notification_channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringAlertPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param combiner: How to combine the results of multiple conditions to determine if an incident should be opened. Possible values: ["AND", "OR", "AND_WITH_MATCHING_RESOURCE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#combiner GoogleMonitoringAlertPolicy#combiner}
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#conditions GoogleMonitoringAlertPolicy#conditions}
        :param display_name: A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        :param alert_strategy: alert_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alert_strategy GoogleMonitoringAlertPolicy#alert_strategy}
        :param documentation: documentation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#documentation GoogleMonitoringAlertPolicy#documentation}
        :param enabled: Whether or not the policy is enabled. The default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#enabled GoogleMonitoringAlertPolicy#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#id GoogleMonitoringAlertPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_channels: Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_channels GoogleMonitoringAlertPolicy#notification_channels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#project GoogleMonitoringAlertPolicy#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#timeouts GoogleMonitoringAlertPolicy#timeouts}
        :param user_labels: This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#user_labels GoogleMonitoringAlertPolicy#user_labels}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alert_strategy, dict):
            alert_strategy = GoogleMonitoringAlertPolicyAlertStrategy(**alert_strategy)
        if isinstance(documentation, dict):
            documentation = GoogleMonitoringAlertPolicyDocumentation(**documentation)
        if isinstance(timeouts, dict):
            timeouts = GoogleMonitoringAlertPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument combiner", value=combiner, expected_type=type_hints["combiner"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument alert_strategy", value=alert_strategy, expected_type=type_hints["alert_strategy"])
            check_type(argname="argument documentation", value=documentation, expected_type=type_hints["documentation"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_channels", value=notification_channels, expected_type=type_hints["notification_channels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_labels", value=user_labels, expected_type=type_hints["user_labels"])
        self._values: typing.Dict[str, typing.Any] = {
            "combiner": combiner,
            "conditions": conditions,
            "display_name": display_name,
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
        if alert_strategy is not None:
            self._values["alert_strategy"] = alert_strategy
        if documentation is not None:
            self._values["documentation"] = documentation
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if notification_channels is not None:
            self._values["notification_channels"] = notification_channels
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_labels is not None:
            self._values["user_labels"] = user_labels

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
    def combiner(self) -> builtins.str:
        '''How to combine the results of multiple conditions to determine if an incident should be opened.

        Possible values: ["AND", "OR", "AND_WITH_MATCHING_RESOURCE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#combiner GoogleMonitoringAlertPolicy#combiner}
        '''
        result = self._values.get("combiner")
        assert result is not None, "Required property 'combiner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]]:
        '''conditions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#conditions GoogleMonitoringAlertPolicy#conditions}
        '''
        result = self._values.get("conditions")
        assert result is not None, "Required property 'conditions' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[GoogleMonitoringAlertPolicyConditions]], result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''A short name or phrase used to identify the policy in dashboards, notifications, and incidents.

        To avoid confusion, don't use
        the same display name for multiple policies in the same project. The
        name is limited to 512 Unicode characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#display_name GoogleMonitoringAlertPolicy#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert_strategy(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy]:
        '''alert_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#alert_strategy GoogleMonitoringAlertPolicy#alert_strategy}
        '''
        result = self._values.get("alert_strategy")
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyAlertStrategy], result)

    @builtins.property
    def documentation(
        self,
    ) -> typing.Optional["GoogleMonitoringAlertPolicyDocumentation"]:
        '''documentation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#documentation GoogleMonitoringAlertPolicy#documentation}
        '''
        result = self._values.get("documentation")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyDocumentation"], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not the policy is enabled. The default is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#enabled GoogleMonitoringAlertPolicy#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#id GoogleMonitoringAlertPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_channels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident.

        Each element of this array corresponds
        to the name field in each of the NotificationChannel objects that are
        returned from the notificationChannels.list method. The syntax of the
        entries in this field is
        'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#notification_channels GoogleMonitoringAlertPolicy#notification_channels}
        '''
        result = self._values.get("notification_channels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#project GoogleMonitoringAlertPolicy#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleMonitoringAlertPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#timeouts GoogleMonitoringAlertPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleMonitoringAlertPolicyTimeouts"], result)

    @builtins.property
    def user_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#user_labels GoogleMonitoringAlertPolicy#user_labels}
        '''
        result = self._values.get("user_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyCreationRecord",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleMonitoringAlertPolicyCreationRecord:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyCreationRecord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyCreationRecordList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyCreationRecordList",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyCreationRecordList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleMonitoringAlertPolicyCreationRecordOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyCreationRecordList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleMonitoringAlertPolicyCreationRecordOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyCreationRecordList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyCreationRecordList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyCreationRecordList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleMonitoringAlertPolicyCreationRecordOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyCreationRecordOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyCreationRecordOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="mutatedBy")
    def mutated_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mutatedBy"))

    @builtins.property
    @jsii.member(jsii_name="mutateTime")
    def mutate_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mutateTime"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyCreationRecord]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyCreationRecord], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyCreationRecord],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyCreationRecordOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyDocumentation",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "mime_type": "mimeType"},
)
class GoogleMonitoringAlertPolicyDocumentation:
    def __init__(
        self,
        *,
        content: typing.Optional[builtins.str] = None,
        mime_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content: The text of the documentation, interpreted according to mimeType. The content may not exceed 8,192 Unicode characters and may not exceed more than 10,240 bytes when encoded in UTF-8 format, whichever is smaller. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#content GoogleMonitoringAlertPolicy#content}
        :param mime_type: The format of the content field. Presently, only the value "text/markdown" is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#mime_type GoogleMonitoringAlertPolicy#mime_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyDocumentation.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument mime_type", value=mime_type, expected_type=type_hints["mime_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if content is not None:
            self._values["content"] = content
        if mime_type is not None:
            self._values["mime_type"] = mime_type

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''The text of the documentation, interpreted according to mimeType.

        The content may not exceed 8,192 Unicode characters and may not
        exceed more than 10,240 bytes when encoded in UTF-8 format,
        whichever is smaller.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#content GoogleMonitoringAlertPolicy#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mime_type(self) -> typing.Optional[builtins.str]:
        '''The format of the content field. Presently, only the value "text/markdown" is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#mime_type GoogleMonitoringAlertPolicy#mime_type}
        '''
        result = self._values.get("mime_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyDocumentation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyDocumentationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyDocumentationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyDocumentationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetMimeType")
    def reset_mime_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMimeType", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="mimeTypeInput")
    def mime_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mimeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyDocumentationOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="mimeType")
    def mime_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mimeType"))

    @mime_type.setter
    def mime_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyDocumentationOutputReference, "mime_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mimeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringAlertPolicyDocumentation]:
        return typing.cast(typing.Optional[GoogleMonitoringAlertPolicyDocumentation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringAlertPolicyDocumentation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyDocumentationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleMonitoringAlertPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#create GoogleMonitoringAlertPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#delete GoogleMonitoringAlertPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#update GoogleMonitoringAlertPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#create GoogleMonitoringAlertPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#delete GoogleMonitoringAlertPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_alert_policy#update GoogleMonitoringAlertPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringAlertPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringAlertPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringAlertPolicy.GoogleMonitoringAlertPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringAlertPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringAlertPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringAlertPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleMonitoringAlertPolicy",
    "GoogleMonitoringAlertPolicyAlertStrategy",
    "GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimit",
    "GoogleMonitoringAlertPolicyAlertStrategyNotificationRateLimitOutputReference",
    "GoogleMonitoringAlertPolicyAlertStrategyOutputReference",
    "GoogleMonitoringAlertPolicyConditions",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsent",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregations",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsList",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentAggregationsOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentTrigger",
    "GoogleMonitoringAlertPolicyConditionsConditionAbsentTriggerOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionMatchedLog",
    "GoogleMonitoringAlertPolicyConditionsConditionMatchedLogOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguage",
    "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTrigger",
    "GoogleMonitoringAlertPolicyConditionsConditionMonitoringQueryLanguageTriggerOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionThreshold",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregations",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsList",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdAggregationsOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregations",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsList",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdDenominatorAggregationsOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdOutputReference",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdTrigger",
    "GoogleMonitoringAlertPolicyConditionsConditionThresholdTriggerOutputReference",
    "GoogleMonitoringAlertPolicyConditionsList",
    "GoogleMonitoringAlertPolicyConditionsOutputReference",
    "GoogleMonitoringAlertPolicyConfig",
    "GoogleMonitoringAlertPolicyCreationRecord",
    "GoogleMonitoringAlertPolicyCreationRecordList",
    "GoogleMonitoringAlertPolicyCreationRecordOutputReference",
    "GoogleMonitoringAlertPolicyDocumentation",
    "GoogleMonitoringAlertPolicyDocumentationOutputReference",
    "GoogleMonitoringAlertPolicyTimeouts",
    "GoogleMonitoringAlertPolicyTimeoutsOutputReference",
]

publication.publish()
