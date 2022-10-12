'''
# `azurerm_container_connected_registry`

Refer to the Terraform Registory for docs: [`azurerm_container_connected_registry`](https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry).
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


class ContainerConnectedRegistry(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerConnectedRegistry.ContainerConnectedRegistry",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry azurerm_container_connected_registry}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container_registry_id: builtins.str,
        name: builtins.str,
        sync_token_id: builtins.str,
        audit_log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_token_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        notification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerConnectedRegistryNotification", typing.Dict[str, typing.Any]]]]] = None,
        parent_registry_id: typing.Optional[builtins.str] = None,
        sync_message_ttl: typing.Optional[builtins.str] = None,
        sync_schedule: typing.Optional[builtins.str] = None,
        sync_window: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ContainerConnectedRegistryTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry azurerm_container_connected_registry} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container_registry_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#container_registry_id ContainerConnectedRegistry#container_registry_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#name ContainerConnectedRegistry#name}.
        :param sync_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_token_id ContainerConnectedRegistry#sync_token_id}.
        :param audit_log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#audit_log_enabled ContainerConnectedRegistry#audit_log_enabled}.
        :param client_token_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#client_token_ids ContainerConnectedRegistry#client_token_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#id ContainerConnectedRegistry#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#log_level ContainerConnectedRegistry#log_level}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#mode ContainerConnectedRegistry#mode}.
        :param notification: notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#notification ContainerConnectedRegistry#notification}
        :param parent_registry_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#parent_registry_id ContainerConnectedRegistry#parent_registry_id}.
        :param sync_message_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_message_ttl ContainerConnectedRegistry#sync_message_ttl}.
        :param sync_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_schedule ContainerConnectedRegistry#sync_schedule}.
        :param sync_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_window ContainerConnectedRegistry#sync_window}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#timeouts ContainerConnectedRegistry#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerConnectedRegistry.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContainerConnectedRegistryConfig(
            container_registry_id=container_registry_id,
            name=name,
            sync_token_id=sync_token_id,
            audit_log_enabled=audit_log_enabled,
            client_token_ids=client_token_ids,
            id=id,
            log_level=log_level,
            mode=mode,
            notification=notification,
            parent_registry_id=parent_registry_id,
            sync_message_ttl=sync_message_ttl,
            sync_schedule=sync_schedule,
            sync_window=sync_window,
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

    @jsii.member(jsii_name="putNotification")
    def put_notification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerConnectedRegistryNotification", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerConnectedRegistry.put_notification)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNotification", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#create ContainerConnectedRegistry#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#delete ContainerConnectedRegistry#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#read ContainerConnectedRegistry#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#update ContainerConnectedRegistry#update}.
        '''
        value = ContainerConnectedRegistryTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuditLogEnabled")
    def reset_audit_log_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLogEnabled", []))

    @jsii.member(jsii_name="resetClientTokenIds")
    def reset_client_token_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTokenIds", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetNotification")
    def reset_notification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotification", []))

    @jsii.member(jsii_name="resetParentRegistryId")
    def reset_parent_registry_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentRegistryId", []))

    @jsii.member(jsii_name="resetSyncMessageTtl")
    def reset_sync_message_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncMessageTtl", []))

    @jsii.member(jsii_name="resetSyncSchedule")
    def reset_sync_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncSchedule", []))

    @jsii.member(jsii_name="resetSyncWindow")
    def reset_sync_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncWindow", []))

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
    @jsii.member(jsii_name="notification")
    def notification(self) -> "ContainerConnectedRegistryNotificationList":
        return typing.cast("ContainerConnectedRegistryNotificationList", jsii.get(self, "notification"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ContainerConnectedRegistryTimeoutsOutputReference":
        return typing.cast("ContainerConnectedRegistryTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="auditLogEnabledInput")
    def audit_log_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "auditLogEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTokenIdsInput")
    def client_token_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clientTokenIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryIdInput")
    def container_registry_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationInput")
    def notification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerConnectedRegistryNotification"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerConnectedRegistryNotification"]]], jsii.get(self, "notificationInput"))

    @builtins.property
    @jsii.member(jsii_name="parentRegistryIdInput")
    def parent_registry_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentRegistryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="syncMessageTtlInput")
    def sync_message_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncMessageTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="syncScheduleInput")
    def sync_schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="syncTokenIdInput")
    def sync_token_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncTokenIdInput"))

    @builtins.property
    @jsii.member(jsii_name="syncWindowInput")
    def sync_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ContainerConnectedRegistryTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ContainerConnectedRegistryTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="auditLogEnabled")
    def audit_log_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "auditLogEnabled"))

    @audit_log_enabled.setter
    def audit_log_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "audit_log_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditLogEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientTokenIds")
    def client_token_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clientTokenIds"))

    @client_token_ids.setter
    def client_token_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "client_token_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTokenIds", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryId")
    def container_registry_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerRegistryId"))

    @container_registry_id.setter
    def container_registry_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "container_registry_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "log_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentRegistryId")
    def parent_registry_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentRegistryId"))

    @parent_registry_id.setter
    def parent_registry_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "parent_registry_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentRegistryId", value)

    @builtins.property
    @jsii.member(jsii_name="syncMessageTtl")
    def sync_message_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syncMessageTtl"))

    @sync_message_ttl.setter
    def sync_message_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "sync_message_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncMessageTtl", value)

    @builtins.property
    @jsii.member(jsii_name="syncSchedule")
    def sync_schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syncSchedule"))

    @sync_schedule.setter
    def sync_schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "sync_schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncSchedule", value)

    @builtins.property
    @jsii.member(jsii_name="syncTokenId")
    def sync_token_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syncTokenId"))

    @sync_token_id.setter
    def sync_token_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "sync_token_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncTokenId", value)

    @builtins.property
    @jsii.member(jsii_name="syncWindow")
    def sync_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syncWindow"))

    @sync_window.setter
    def sync_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistry, "sync_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncWindow", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerConnectedRegistry.ContainerConnectedRegistryConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container_registry_id": "containerRegistryId",
        "name": "name",
        "sync_token_id": "syncTokenId",
        "audit_log_enabled": "auditLogEnabled",
        "client_token_ids": "clientTokenIds",
        "id": "id",
        "log_level": "logLevel",
        "mode": "mode",
        "notification": "notification",
        "parent_registry_id": "parentRegistryId",
        "sync_message_ttl": "syncMessageTtl",
        "sync_schedule": "syncSchedule",
        "sync_window": "syncWindow",
        "timeouts": "timeouts",
    },
)
class ContainerConnectedRegistryConfig(cdktf.TerraformMetaArguments):
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
        container_registry_id: builtins.str,
        name: builtins.str,
        sync_token_id: builtins.str,
        audit_log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_token_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        notification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerConnectedRegistryNotification", typing.Dict[str, typing.Any]]]]] = None,
        parent_registry_id: typing.Optional[builtins.str] = None,
        sync_message_ttl: typing.Optional[builtins.str] = None,
        sync_schedule: typing.Optional[builtins.str] = None,
        sync_window: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ContainerConnectedRegistryTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container_registry_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#container_registry_id ContainerConnectedRegistry#container_registry_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#name ContainerConnectedRegistry#name}.
        :param sync_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_token_id ContainerConnectedRegistry#sync_token_id}.
        :param audit_log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#audit_log_enabled ContainerConnectedRegistry#audit_log_enabled}.
        :param client_token_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#client_token_ids ContainerConnectedRegistry#client_token_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#id ContainerConnectedRegistry#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#log_level ContainerConnectedRegistry#log_level}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#mode ContainerConnectedRegistry#mode}.
        :param notification: notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#notification ContainerConnectedRegistry#notification}
        :param parent_registry_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#parent_registry_id ContainerConnectedRegistry#parent_registry_id}.
        :param sync_message_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_message_ttl ContainerConnectedRegistry#sync_message_ttl}.
        :param sync_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_schedule ContainerConnectedRegistry#sync_schedule}.
        :param sync_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_window ContainerConnectedRegistry#sync_window}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#timeouts ContainerConnectedRegistry#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ContainerConnectedRegistryTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerConnectedRegistryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container_registry_id", value=container_registry_id, expected_type=type_hints["container_registry_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sync_token_id", value=sync_token_id, expected_type=type_hints["sync_token_id"])
            check_type(argname="argument audit_log_enabled", value=audit_log_enabled, expected_type=type_hints["audit_log_enabled"])
            check_type(argname="argument client_token_ids", value=client_token_ids, expected_type=type_hints["client_token_ids"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument notification", value=notification, expected_type=type_hints["notification"])
            check_type(argname="argument parent_registry_id", value=parent_registry_id, expected_type=type_hints["parent_registry_id"])
            check_type(argname="argument sync_message_ttl", value=sync_message_ttl, expected_type=type_hints["sync_message_ttl"])
            check_type(argname="argument sync_schedule", value=sync_schedule, expected_type=type_hints["sync_schedule"])
            check_type(argname="argument sync_window", value=sync_window, expected_type=type_hints["sync_window"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_registry_id": container_registry_id,
            "name": name,
            "sync_token_id": sync_token_id,
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
        if audit_log_enabled is not None:
            self._values["audit_log_enabled"] = audit_log_enabled
        if client_token_ids is not None:
            self._values["client_token_ids"] = client_token_ids
        if id is not None:
            self._values["id"] = id
        if log_level is not None:
            self._values["log_level"] = log_level
        if mode is not None:
            self._values["mode"] = mode
        if notification is not None:
            self._values["notification"] = notification
        if parent_registry_id is not None:
            self._values["parent_registry_id"] = parent_registry_id
        if sync_message_ttl is not None:
            self._values["sync_message_ttl"] = sync_message_ttl
        if sync_schedule is not None:
            self._values["sync_schedule"] = sync_schedule
        if sync_window is not None:
            self._values["sync_window"] = sync_window
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
    def container_registry_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#container_registry_id ContainerConnectedRegistry#container_registry_id}.'''
        result = self._values.get("container_registry_id")
        assert result is not None, "Required property 'container_registry_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#name ContainerConnectedRegistry#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sync_token_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_token_id ContainerConnectedRegistry#sync_token_id}.'''
        result = self._values.get("sync_token_id")
        assert result is not None, "Required property 'sync_token_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#audit_log_enabled ContainerConnectedRegistry#audit_log_enabled}.'''
        result = self._values.get("audit_log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_token_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#client_token_ids ContainerConnectedRegistry#client_token_ids}.'''
        result = self._values.get("client_token_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#id ContainerConnectedRegistry#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#log_level ContainerConnectedRegistry#log_level}.'''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#mode ContainerConnectedRegistry#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerConnectedRegistryNotification"]]]:
        '''notification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#notification ContainerConnectedRegistry#notification}
        '''
        result = self._values.get("notification")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerConnectedRegistryNotification"]]], result)

    @builtins.property
    def parent_registry_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#parent_registry_id ContainerConnectedRegistry#parent_registry_id}.'''
        result = self._values.get("parent_registry_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_message_ttl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_message_ttl ContainerConnectedRegistry#sync_message_ttl}.'''
        result = self._values.get("sync_message_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_schedule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_schedule ContainerConnectedRegistry#sync_schedule}.'''
        result = self._values.get("sync_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#sync_window ContainerConnectedRegistry#sync_window}.'''
        result = self._values.get("sync_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ContainerConnectedRegistryTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#timeouts ContainerConnectedRegistry#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ContainerConnectedRegistryTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerConnectedRegistryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerConnectedRegistry.ContainerConnectedRegistryNotification",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "name": "name",
        "digest": "digest",
        "tag": "tag",
    },
)
class ContainerConnectedRegistryNotification:
    def __init__(
        self,
        *,
        action: builtins.str,
        name: builtins.str,
        digest: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#action ContainerConnectedRegistry#action}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#name ContainerConnectedRegistry#name}.
        :param digest: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#digest ContainerConnectedRegistry#digest}.
        :param tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#tag ContainerConnectedRegistry#tag}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerConnectedRegistryNotification.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument digest", value=digest, expected_type=type_hints["digest"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "name": name,
        }
        if digest is not None:
            self._values["digest"] = digest
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#action ContainerConnectedRegistry#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#name ContainerConnectedRegistry#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def digest(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#digest ContainerConnectedRegistry#digest}.'''
        result = self._values.get("digest")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#tag ContainerConnectedRegistry#tag}.'''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerConnectedRegistryNotification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerConnectedRegistryNotificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerConnectedRegistry.ContainerConnectedRegistryNotificationList",
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
            type_hints = typing.get_type_hints(ContainerConnectedRegistryNotificationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerConnectedRegistryNotificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerConnectedRegistryNotificationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerConnectedRegistryNotificationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerConnectedRegistryNotification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerConnectedRegistryNotification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerConnectedRegistryNotification]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerConnectedRegistryNotificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerConnectedRegistry.ContainerConnectedRegistryNotificationOutputReference",
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
            type_hints = typing.get_type_hints(ContainerConnectedRegistryNotificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDigest")
    def reset_digest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDigest", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="digestInput")
    def digest_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "digestInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="digest")
    def digest(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "digest"))

    @digest.setter
    def digest(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationOutputReference, "digest").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "digest", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerConnectedRegistryNotification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerConnectedRegistryNotification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerConnectedRegistryNotification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryNotificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.containerConnectedRegistry.ContainerConnectedRegistryTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ContainerConnectedRegistryTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#create ContainerConnectedRegistry#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#delete ContainerConnectedRegistry#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#read ContainerConnectedRegistry#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#update ContainerConnectedRegistry#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerConnectedRegistryTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#create ContainerConnectedRegistry#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#delete ContainerConnectedRegistry#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#read ContainerConnectedRegistry#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/container_connected_registry#update ContainerConnectedRegistry#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerConnectedRegistryTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerConnectedRegistryTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.containerConnectedRegistry.ContainerConnectedRegistryTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerConnectedRegistryTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerConnectedRegistryTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerConnectedRegistryTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerConnectedRegistryTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerConnectedRegistryTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ContainerConnectedRegistry",
    "ContainerConnectedRegistryConfig",
    "ContainerConnectedRegistryNotification",
    "ContainerConnectedRegistryNotificationList",
    "ContainerConnectedRegistryNotificationOutputReference",
    "ContainerConnectedRegistryTimeouts",
    "ContainerConnectedRegistryTimeoutsOutputReference",
]

publication.publish()
