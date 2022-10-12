'''
# `google_monitoring_notification_channel`

Refer to the Terraform Registory for docs: [`google_monitoring_notification_channel`](https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel).
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


class GoogleMonitoringNotificationChannel(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringNotificationChannel.GoogleMonitoringNotificationChannel",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel google_monitoring_notification_channel}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        sensitive_labels: typing.Optional[typing.Union["GoogleMonitoringNotificationChannelSensitiveLabels", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringNotificationChannelTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel google_monitoring_notification_channel} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param type: The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of valid values such as "email", "slack", etc... Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#type GoogleMonitoringNotificationChannel#type}
        :param description: An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#description GoogleMonitoringNotificationChannel#description}
        :param display_name: An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#display_name GoogleMonitoringNotificationChannel#display_name}
        :param enabled: Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#enabled GoogleMonitoringNotificationChannel#enabled}
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#force_delete GoogleMonitoringNotificationChannel#force_delete}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#id GoogleMonitoringNotificationChannel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the sensitive_labels block, but cannot be configured in both places. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#labels GoogleMonitoringNotificationChannel#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#project GoogleMonitoringNotificationChannel#project}.
        :param sensitive_labels: sensitive_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#sensitive_labels GoogleMonitoringNotificationChannel#sensitive_labels}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#timeouts GoogleMonitoringNotificationChannel#timeouts}
        :param user_labels: User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema, unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#user_labels GoogleMonitoringNotificationChannel#user_labels}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringNotificationChannel.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleMonitoringNotificationChannelConfig(
            type=type,
            description=description,
            display_name=display_name,
            enabled=enabled,
            force_delete=force_delete,
            id=id,
            labels=labels,
            project=project,
            sensitive_labels=sensitive_labels,
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

    @jsii.member(jsii_name="putSensitiveLabels")
    def put_sensitive_labels(
        self,
        *,
        auth_token: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        service_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_token: An authorization token for a notification channel. Channel types that support this field include: slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#auth_token GoogleMonitoringNotificationChannel#auth_token}
        :param password: An password for a notification channel. Channel types that support this field include: webhook_basicauth. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#password GoogleMonitoringNotificationChannel#password}
        :param service_key: An servicekey token for a notification channel. Channel types that support this field include: pagerduty. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#service_key GoogleMonitoringNotificationChannel#service_key}
        '''
        value = GoogleMonitoringNotificationChannelSensitiveLabels(
            auth_token=auth_token, password=password, service_key=service_key
        )

        return typing.cast(None, jsii.invoke(self, "putSensitiveLabels", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#create GoogleMonitoringNotificationChannel#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#delete GoogleMonitoringNotificationChannel#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#update GoogleMonitoringNotificationChannel#update}.
        '''
        value = GoogleMonitoringNotificationChannelTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSensitiveLabels")
    def reset_sensitive_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitiveLabels", []))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="sensitiveLabels")
    def sensitive_labels(
        self,
    ) -> "GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference":
        return typing.cast("GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference", jsii.get(self, "sensitiveLabels"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleMonitoringNotificationChannelTimeoutsOutputReference":
        return typing.cast("GoogleMonitoringNotificationChannelTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="verificationStatus")
    def verification_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verificationStatus"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="sensitiveLabelsInput")
    def sensitive_labels_input(
        self,
    ) -> typing.Optional["GoogleMonitoringNotificationChannelSensitiveLabels"]:
        return typing.cast(typing.Optional["GoogleMonitoringNotificationChannelSensitiveLabels"], jsii.get(self, "sensitiveLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleMonitoringNotificationChannelTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleMonitoringNotificationChannelTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userLabelsInput")
    def user_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "userLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "force_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="userLabels")
    def user_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "userLabels"))

    @user_labels.setter
    def user_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannel, "user_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userLabels", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringNotificationChannel.GoogleMonitoringNotificationChannelConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "type": "type",
        "description": "description",
        "display_name": "displayName",
        "enabled": "enabled",
        "force_delete": "forceDelete",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "sensitive_labels": "sensitiveLabels",
        "timeouts": "timeouts",
        "user_labels": "userLabels",
    },
)
class GoogleMonitoringNotificationChannelConfig(cdktf.TerraformMetaArguments):
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
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        sensitive_labels: typing.Optional[typing.Union["GoogleMonitoringNotificationChannelSensitiveLabels", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleMonitoringNotificationChannelTimeouts", typing.Dict[str, typing.Any]]] = None,
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
        :param type: The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of valid values such as "email", "slack", etc... Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#type GoogleMonitoringNotificationChannel#type}
        :param description: An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#description GoogleMonitoringNotificationChannel#description}
        :param display_name: An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#display_name GoogleMonitoringNotificationChannel#display_name}
        :param enabled: Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#enabled GoogleMonitoringNotificationChannel#enabled}
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#force_delete GoogleMonitoringNotificationChannel#force_delete}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#id GoogleMonitoringNotificationChannel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the sensitive_labels block, but cannot be configured in both places. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#labels GoogleMonitoringNotificationChannel#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#project GoogleMonitoringNotificationChannel#project}.
        :param sensitive_labels: sensitive_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#sensitive_labels GoogleMonitoringNotificationChannel#sensitive_labels}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#timeouts GoogleMonitoringNotificationChannel#timeouts}
        :param user_labels: User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema, unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#user_labels GoogleMonitoringNotificationChannel#user_labels}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(sensitive_labels, dict):
            sensitive_labels = GoogleMonitoringNotificationChannelSensitiveLabels(**sensitive_labels)
        if isinstance(timeouts, dict):
            timeouts = GoogleMonitoringNotificationChannelTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringNotificationChannelConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument sensitive_labels", value=sensitive_labels, expected_type=type_hints["sensitive_labels"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_labels", value=user_labels, expected_type=type_hints["user_labels"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if project is not None:
            self._values["project"] = project
        if sensitive_labels is not None:
            self._values["sensitive_labels"] = sensitive_labels
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
    def type(self) -> builtins.str:
        '''The type of the notification channel.

        This field matches the value of the NotificationChannelDescriptor.type field. See https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of valid values such as "email", "slack", etc...

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#type GoogleMonitoringNotificationChannel#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional human-readable description of this notification channel.

        This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#description GoogleMonitoringNotificationChannel#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''An optional human-readable name for this notification channel.

        It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#display_name GoogleMonitoringNotificationChannel#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether notifications are forwarded to the described channel.

        This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#enabled GoogleMonitoringNotificationChannel#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#force_delete GoogleMonitoringNotificationChannel#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#id GoogleMonitoringNotificationChannel#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Configuration fields that define the channel and its behavior.

        The
        permissible and required labels are specified in the
        NotificationChannelDescriptor corresponding to the type field.

        Labels with sensitive data are obfuscated by the API and therefore Terraform cannot
        determine if there are upstream changes to these fields. They can also be configured via
        the sensitive_labels block, but cannot be configured in both places.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#labels GoogleMonitoringNotificationChannel#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#project GoogleMonitoringNotificationChannel#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive_labels(
        self,
    ) -> typing.Optional["GoogleMonitoringNotificationChannelSensitiveLabels"]:
        '''sensitive_labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#sensitive_labels GoogleMonitoringNotificationChannel#sensitive_labels}
        '''
        result = self._values.get("sensitive_labels")
        return typing.cast(typing.Optional["GoogleMonitoringNotificationChannelSensitiveLabels"], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleMonitoringNotificationChannelTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#timeouts GoogleMonitoringNotificationChannel#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleMonitoringNotificationChannelTimeouts"], result)

    @builtins.property
    def user_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema, unlike the labels field.

        This field is intended to be used for organizing and identifying the NotificationChannel objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#user_labels GoogleMonitoringNotificationChannel#user_labels}
        '''
        result = self._values.get("user_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringNotificationChannelConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringNotificationChannel.GoogleMonitoringNotificationChannelSensitiveLabels",
    jsii_struct_bases=[],
    name_mapping={
        "auth_token": "authToken",
        "password": "password",
        "service_key": "serviceKey",
    },
)
class GoogleMonitoringNotificationChannelSensitiveLabels:
    def __init__(
        self,
        *,
        auth_token: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        service_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_token: An authorization token for a notification channel. Channel types that support this field include: slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#auth_token GoogleMonitoringNotificationChannel#auth_token}
        :param password: An password for a notification channel. Channel types that support this field include: webhook_basicauth. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#password GoogleMonitoringNotificationChannel#password}
        :param service_key: An servicekey token for a notification channel. Channel types that support this field include: pagerduty. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#service_key GoogleMonitoringNotificationChannel#service_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringNotificationChannelSensitiveLabels.__init__)
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument service_key", value=service_key, expected_type=type_hints["service_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_token is not None:
            self._values["auth_token"] = auth_token
        if password is not None:
            self._values["password"] = password
        if service_key is not None:
            self._values["service_key"] = service_key

    @builtins.property
    def auth_token(self) -> typing.Optional[builtins.str]:
        '''An authorization token for a notification channel. Channel types that support this field include: slack.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#auth_token GoogleMonitoringNotificationChannel#auth_token}
        '''
        result = self._values.get("auth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''An password for a notification channel. Channel types that support this field include: webhook_basicauth.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#password GoogleMonitoringNotificationChannel#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_key(self) -> typing.Optional[builtins.str]:
        '''An servicekey token for a notification channel. Channel types that support this field include: pagerduty.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#service_key GoogleMonitoringNotificationChannel#service_key}
        '''
        result = self._values.get("service_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringNotificationChannelSensitiveLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringNotificationChannel.GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthToken")
    def reset_auth_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthToken", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetServiceKey")
    def reset_service_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceKey", []))

    @builtins.property
    @jsii.member(jsii_name="authTokenInput")
    def auth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceKeyInput")
    def service_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference, "auth_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authToken", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="serviceKey")
    def service_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceKey"))

    @service_key.setter
    def service_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference, "service_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleMonitoringNotificationChannelSensitiveLabels]:
        return typing.cast(typing.Optional[GoogleMonitoringNotificationChannelSensitiveLabels], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleMonitoringNotificationChannelSensitiveLabels],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleMonitoringNotificationChannel.GoogleMonitoringNotificationChannelTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleMonitoringNotificationChannelTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#create GoogleMonitoringNotificationChannel#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#delete GoogleMonitoringNotificationChannel#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#update GoogleMonitoringNotificationChannel#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleMonitoringNotificationChannelTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#create GoogleMonitoringNotificationChannel#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#delete GoogleMonitoringNotificationChannel#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_monitoring_notification_channel#update GoogleMonitoringNotificationChannel#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleMonitoringNotificationChannelTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleMonitoringNotificationChannelTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleMonitoringNotificationChannel.GoogleMonitoringNotificationChannelTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleMonitoringNotificationChannelTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannelTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannelTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannelTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleMonitoringNotificationChannelTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleMonitoringNotificationChannelTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleMonitoringNotificationChannelTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleMonitoringNotificationChannelTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleMonitoringNotificationChannel",
    "GoogleMonitoringNotificationChannelConfig",
    "GoogleMonitoringNotificationChannelSensitiveLabels",
    "GoogleMonitoringNotificationChannelSensitiveLabelsOutputReference",
    "GoogleMonitoringNotificationChannelTimeouts",
    "GoogleMonitoringNotificationChannelTimeoutsOutputReference",
]

publication.publish()
