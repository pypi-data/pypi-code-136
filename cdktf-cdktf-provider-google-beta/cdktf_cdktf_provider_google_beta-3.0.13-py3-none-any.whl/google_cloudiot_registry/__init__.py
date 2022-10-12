'''
# `google_cloudiot_registry`

Refer to the Terraform Registory for docs: [`google_cloudiot_registry`](https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry).
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


class GoogleCloudiotRegistry(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistry",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry google_cloudiot_registry}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        credentials: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudiotRegistryCredentials", typing.Dict[str, typing.Any]]]]] = None,
        event_notification_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudiotRegistryEventNotificationConfigs", typing.Dict[str, typing.Any]]]]] = None,
        http_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
        mqtt_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        state_notification_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleCloudiotRegistryTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry google_cloudiot_registry} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: A unique name for the resource, required by device registry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#name GoogleCloudiotRegistry#name}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#credentials GoogleCloudiotRegistry#credentials}
        :param event_notification_configs: event_notification_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#event_notification_configs GoogleCloudiotRegistry#event_notification_configs}
        :param http_config: Activate or deactivate HTTP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#http_config GoogleCloudiotRegistry#http_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#id GoogleCloudiotRegistry#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_level: The default logging verbosity for activity from devices in this registry. Specifies which events should be written to logs. For example, if the LogLevel is ERROR, only events that terminate in errors will be logged. LogLevel is inclusive; enabling INFO logging will also enable ERROR logging. Default value: "NONE" Possible values: ["NONE", "ERROR", "INFO", "DEBUG"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#log_level GoogleCloudiotRegistry#log_level}
        :param mqtt_config: Activate or deactivate MQTT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#mqtt_config GoogleCloudiotRegistry#mqtt_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#project GoogleCloudiotRegistry#project}.
        :param region: The region in which the created registry should reside. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#region GoogleCloudiotRegistry#region}
        :param state_notification_config: A PubSub topic to publish device state updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#state_notification_config GoogleCloudiotRegistry#state_notification_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#timeouts GoogleCloudiotRegistry#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistry.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleCloudiotRegistryConfig(
            name=name,
            credentials=credentials,
            event_notification_configs=event_notification_configs,
            http_config=http_config,
            id=id,
            log_level=log_level,
            mqtt_config=mqtt_config,
            project=project,
            region=region,
            state_notification_config=state_notification_config,
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

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudiotRegistryCredentials", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistry.put_credentials)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putEventNotificationConfigs")
    def put_event_notification_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudiotRegistryEventNotificationConfigs", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistry.put_event_notification_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEventNotificationConfigs", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#create GoogleCloudiotRegistry#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#delete GoogleCloudiotRegistry#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#update GoogleCloudiotRegistry#update}.
        '''
        value = GoogleCloudiotRegistryTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetEventNotificationConfigs")
    def reset_event_notification_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventNotificationConfigs", []))

    @jsii.member(jsii_name="resetHttpConfig")
    def reset_http_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @jsii.member(jsii_name="resetMqttConfig")
    def reset_mqtt_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMqttConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetStateNotificationConfig")
    def reset_state_notification_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStateNotificationConfig", []))

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
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "GoogleCloudiotRegistryCredentialsList":
        return typing.cast("GoogleCloudiotRegistryCredentialsList", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="eventNotificationConfigs")
    def event_notification_configs(
        self,
    ) -> "GoogleCloudiotRegistryEventNotificationConfigsList":
        return typing.cast("GoogleCloudiotRegistryEventNotificationConfigsList", jsii.get(self, "eventNotificationConfigs"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleCloudiotRegistryTimeoutsOutputReference":
        return typing.cast("GoogleCloudiotRegistryTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudiotRegistryCredentials"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudiotRegistryCredentials"]]], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="eventNotificationConfigsInput")
    def event_notification_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudiotRegistryEventNotificationConfigs"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudiotRegistryEventNotificationConfigs"]]], jsii.get(self, "eventNotificationConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpConfigInput")
    def http_config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "httpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="mqttConfigInput")
    def mqtt_config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "mqttConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="stateNotificationConfigInput")
    def state_notification_config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "stateNotificationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleCloudiotRegistryTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleCloudiotRegistryTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpConfig")
    def http_config(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "httpConfig"))

    @http_config.setter
    def http_config(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistry, "http_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpConfig", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistry, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistry, "log_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="mqttConfig")
    def mqtt_config(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "mqttConfig"))

    @mqtt_config.setter
    def mqtt_config(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistry, "mqtt_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mqttConfig", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistry, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistry, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistry, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="stateNotificationConfig")
    def state_notification_config(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "stateNotificationConfig"))

    @state_notification_config.setter
    def state_notification_config(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistry, "state_notification_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateNotificationConfig", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryConfig",
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
        "credentials": "credentials",
        "event_notification_configs": "eventNotificationConfigs",
        "http_config": "httpConfig",
        "id": "id",
        "log_level": "logLevel",
        "mqtt_config": "mqttConfig",
        "project": "project",
        "region": "region",
        "state_notification_config": "stateNotificationConfig",
        "timeouts": "timeouts",
    },
)
class GoogleCloudiotRegistryConfig(cdktf.TerraformMetaArguments):
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
        credentials: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudiotRegistryCredentials", typing.Dict[str, typing.Any]]]]] = None,
        event_notification_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudiotRegistryEventNotificationConfigs", typing.Dict[str, typing.Any]]]]] = None,
        http_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
        mqtt_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        state_notification_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleCloudiotRegistryTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: A unique name for the resource, required by device registry. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#name GoogleCloudiotRegistry#name}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#credentials GoogleCloudiotRegistry#credentials}
        :param event_notification_configs: event_notification_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#event_notification_configs GoogleCloudiotRegistry#event_notification_configs}
        :param http_config: Activate or deactivate HTTP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#http_config GoogleCloudiotRegistry#http_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#id GoogleCloudiotRegistry#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_level: The default logging verbosity for activity from devices in this registry. Specifies which events should be written to logs. For example, if the LogLevel is ERROR, only events that terminate in errors will be logged. LogLevel is inclusive; enabling INFO logging will also enable ERROR logging. Default value: "NONE" Possible values: ["NONE", "ERROR", "INFO", "DEBUG"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#log_level GoogleCloudiotRegistry#log_level}
        :param mqtt_config: Activate or deactivate MQTT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#mqtt_config GoogleCloudiotRegistry#mqtt_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#project GoogleCloudiotRegistry#project}.
        :param region: The region in which the created registry should reside. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#region GoogleCloudiotRegistry#region}
        :param state_notification_config: A PubSub topic to publish device state updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#state_notification_config GoogleCloudiotRegistry#state_notification_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#timeouts GoogleCloudiotRegistry#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleCloudiotRegistryTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument event_notification_configs", value=event_notification_configs, expected_type=type_hints["event_notification_configs"])
            check_type(argname="argument http_config", value=http_config, expected_type=type_hints["http_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument mqtt_config", value=mqtt_config, expected_type=type_hints["mqtt_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument state_notification_config", value=state_notification_config, expected_type=type_hints["state_notification_config"])
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
        if credentials is not None:
            self._values["credentials"] = credentials
        if event_notification_configs is not None:
            self._values["event_notification_configs"] = event_notification_configs
        if http_config is not None:
            self._values["http_config"] = http_config
        if id is not None:
            self._values["id"] = id
        if log_level is not None:
            self._values["log_level"] = log_level
        if mqtt_config is not None:
            self._values["mqtt_config"] = mqtt_config
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if state_notification_config is not None:
            self._values["state_notification_config"] = state_notification_config
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
        '''A unique name for the resource, required by device registry.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#name GoogleCloudiotRegistry#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudiotRegistryCredentials"]]]:
        '''credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#credentials GoogleCloudiotRegistry#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudiotRegistryCredentials"]]], result)

    @builtins.property
    def event_notification_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudiotRegistryEventNotificationConfigs"]]]:
        '''event_notification_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#event_notification_configs GoogleCloudiotRegistry#event_notification_configs}
        '''
        result = self._values.get("event_notification_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudiotRegistryEventNotificationConfigs"]]], result)

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Activate or deactivate HTTP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#http_config GoogleCloudiotRegistry#http_config}
        '''
        result = self._values.get("http_config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#id GoogleCloudiotRegistry#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''The default logging verbosity for activity from devices in this registry.

        Specifies which events should be written to logs. For
        example, if the LogLevel is ERROR, only events that terminate in
        errors will be logged. LogLevel is inclusive; enabling INFO logging
        will also enable ERROR logging. Default value: "NONE" Possible values: ["NONE", "ERROR", "INFO", "DEBUG"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#log_level GoogleCloudiotRegistry#log_level}
        '''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mqtt_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Activate or deactivate MQTT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#mqtt_config GoogleCloudiotRegistry#mqtt_config}
        '''
        result = self._values.get("mqtt_config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#project GoogleCloudiotRegistry#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region in which the created registry should reside. If it is not provided, the provider region is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#region GoogleCloudiotRegistry#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_notification_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A PubSub topic to publish device state updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#state_notification_config GoogleCloudiotRegistry#state_notification_config}
        '''
        result = self._values.get("state_notification_config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleCloudiotRegistryTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#timeouts GoogleCloudiotRegistry#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleCloudiotRegistryTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudiotRegistryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryCredentials",
    jsii_struct_bases=[],
    name_mapping={"public_key_certificate": "publicKeyCertificate"},
)
class GoogleCloudiotRegistryCredentials:
    def __init__(
        self,
        *,
        public_key_certificate: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param public_key_certificate: A public key certificate format and data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#public_key_certificate GoogleCloudiotRegistry#public_key_certificate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryCredentials.__init__)
            check_type(argname="argument public_key_certificate", value=public_key_certificate, expected_type=type_hints["public_key_certificate"])
        self._values: typing.Dict[str, typing.Any] = {
            "public_key_certificate": public_key_certificate,
        }

    @builtins.property
    def public_key_certificate(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A public key certificate format and data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#public_key_certificate GoogleCloudiotRegistry#public_key_certificate}
        '''
        result = self._values.get("public_key_certificate")
        assert result is not None, "Required property 'public_key_certificate' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudiotRegistryCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudiotRegistryCredentialsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryCredentialsList",
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
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryCredentialsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleCloudiotRegistryCredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryCredentialsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleCloudiotRegistryCredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryCredentialsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryCredentialsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryCredentialsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudiotRegistryCredentials]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudiotRegistryCredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudiotRegistryCredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryCredentialsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudiotRegistryCredentialsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryCredentialsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="publicKeyCertificateInput")
    def public_key_certificate_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "publicKeyCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyCertificate")
    def public_key_certificate(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "publicKeyCertificate"))

    @public_key_certificate.setter
    def public_key_certificate(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryCredentialsOutputReference, "public_key_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeyCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudiotRegistryCredentials, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudiotRegistryCredentials, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudiotRegistryCredentials, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryCredentialsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryEventNotificationConfigs",
    jsii_struct_bases=[],
    name_mapping={
        "pubsub_topic_name": "pubsubTopicName",
        "subfolder_matches": "subfolderMatches",
    },
)
class GoogleCloudiotRegistryEventNotificationConfigs:
    def __init__(
        self,
        *,
        pubsub_topic_name: builtins.str,
        subfolder_matches: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pubsub_topic_name: PubSub topic name to publish device events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#pubsub_topic_name GoogleCloudiotRegistry#pubsub_topic_name}
        :param subfolder_matches: If the subfolder name matches this string exactly, this configuration will be used. The string must not include the leading '/' character. If empty, all strings are matched. Empty value can only be used for the last 'event_notification_configs' item. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#subfolder_matches GoogleCloudiotRegistry#subfolder_matches}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryEventNotificationConfigs.__init__)
            check_type(argname="argument pubsub_topic_name", value=pubsub_topic_name, expected_type=type_hints["pubsub_topic_name"])
            check_type(argname="argument subfolder_matches", value=subfolder_matches, expected_type=type_hints["subfolder_matches"])
        self._values: typing.Dict[str, typing.Any] = {
            "pubsub_topic_name": pubsub_topic_name,
        }
        if subfolder_matches is not None:
            self._values["subfolder_matches"] = subfolder_matches

    @builtins.property
    def pubsub_topic_name(self) -> builtins.str:
        '''PubSub topic name to publish device events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#pubsub_topic_name GoogleCloudiotRegistry#pubsub_topic_name}
        '''
        result = self._values.get("pubsub_topic_name")
        assert result is not None, "Required property 'pubsub_topic_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subfolder_matches(self) -> typing.Optional[builtins.str]:
        '''If the subfolder name matches this string exactly, this configuration will be used.

        The string must not include the
        leading '/' character. If empty, all strings are matched. Empty
        value can only be used for the last 'event_notification_configs'
        item.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#subfolder_matches GoogleCloudiotRegistry#subfolder_matches}
        '''
        result = self._values.get("subfolder_matches")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudiotRegistryEventNotificationConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudiotRegistryEventNotificationConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryEventNotificationConfigsList",
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
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryEventNotificationConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleCloudiotRegistryEventNotificationConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryEventNotificationConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleCloudiotRegistryEventNotificationConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryEventNotificationConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryEventNotificationConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryEventNotificationConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudiotRegistryEventNotificationConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudiotRegistryEventNotificationConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudiotRegistryEventNotificationConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryEventNotificationConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudiotRegistryEventNotificationConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryEventNotificationConfigsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryEventNotificationConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSubfolderMatches")
    def reset_subfolder_matches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubfolderMatches", []))

    @builtins.property
    @jsii.member(jsii_name="pubsubTopicNameInput")
    def pubsub_topic_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pubsubTopicNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subfolderMatchesInput")
    def subfolder_matches_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subfolderMatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="pubsubTopicName")
    def pubsub_topic_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pubsubTopicName"))

    @pubsub_topic_name.setter
    def pubsub_topic_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryEventNotificationConfigsOutputReference, "pubsub_topic_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pubsubTopicName", value)

    @builtins.property
    @jsii.member(jsii_name="subfolderMatches")
    def subfolder_matches(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subfolderMatches"))

    @subfolder_matches.setter
    def subfolder_matches(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryEventNotificationConfigsOutputReference, "subfolder_matches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subfolderMatches", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudiotRegistryEventNotificationConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudiotRegistryEventNotificationConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudiotRegistryEventNotificationConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryEventNotificationConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleCloudiotRegistryTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#create GoogleCloudiotRegistry#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#delete GoogleCloudiotRegistry#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#update GoogleCloudiotRegistry#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#create GoogleCloudiotRegistry#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#delete GoogleCloudiotRegistry#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudiot_registry#update GoogleCloudiotRegistry#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudiotRegistryTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudiotRegistryTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudiotRegistry.GoogleCloudiotRegistryTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudiotRegistryTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudiotRegistryTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudiotRegistryTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudiotRegistryTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudiotRegistryTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleCloudiotRegistry",
    "GoogleCloudiotRegistryConfig",
    "GoogleCloudiotRegistryCredentials",
    "GoogleCloudiotRegistryCredentialsList",
    "GoogleCloudiotRegistryCredentialsOutputReference",
    "GoogleCloudiotRegistryEventNotificationConfigs",
    "GoogleCloudiotRegistryEventNotificationConfigsList",
    "GoogleCloudiotRegistryEventNotificationConfigsOutputReference",
    "GoogleCloudiotRegistryTimeouts",
    "GoogleCloudiotRegistryTimeoutsOutputReference",
]

publication.publish()
