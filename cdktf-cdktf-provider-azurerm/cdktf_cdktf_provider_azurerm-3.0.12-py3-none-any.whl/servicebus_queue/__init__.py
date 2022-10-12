'''
# `azurerm_servicebus_queue`

Refer to the Terraform Registory for docs: [`azurerm_servicebus_queue`](https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue).
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


class ServicebusQueue(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.servicebusQueue.ServicebusQueue",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue azurerm_servicebus_queue}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        namespace_id: builtins.str,
        auto_delete_on_idle: typing.Optional[builtins.str] = None,
        dead_lettering_on_message_expiration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_message_ttl: typing.Optional[builtins.str] = None,
        duplicate_detection_history_time_window: typing.Optional[builtins.str] = None,
        enable_batched_operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_express: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_partitioning: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forward_dead_lettered_messages_to: typing.Optional[builtins.str] = None,
        forward_to: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        lock_duration: typing.Optional[builtins.str] = None,
        max_delivery_count: typing.Optional[jsii.Number] = None,
        max_message_size_in_kilobytes: typing.Optional[jsii.Number] = None,
        max_size_in_megabytes: typing.Optional[jsii.Number] = None,
        requires_duplicate_detection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        requires_session: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ServicebusQueueTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue azurerm_servicebus_queue} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#name ServicebusQueue#name}.
        :param namespace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#namespace_id ServicebusQueue#namespace_id}.
        :param auto_delete_on_idle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#auto_delete_on_idle ServicebusQueue#auto_delete_on_idle}.
        :param dead_lettering_on_message_expiration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#dead_lettering_on_message_expiration ServicebusQueue#dead_lettering_on_message_expiration}.
        :param default_message_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#default_message_ttl ServicebusQueue#default_message_ttl}.
        :param duplicate_detection_history_time_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#duplicate_detection_history_time_window ServicebusQueue#duplicate_detection_history_time_window}.
        :param enable_batched_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_batched_operations ServicebusQueue#enable_batched_operations}.
        :param enable_express: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_express ServicebusQueue#enable_express}.
        :param enable_partitioning: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_partitioning ServicebusQueue#enable_partitioning}.
        :param forward_dead_lettered_messages_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#forward_dead_lettered_messages_to ServicebusQueue#forward_dead_lettered_messages_to}.
        :param forward_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#forward_to ServicebusQueue#forward_to}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#id ServicebusQueue#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lock_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#lock_duration ServicebusQueue#lock_duration}.
        :param max_delivery_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_delivery_count ServicebusQueue#max_delivery_count}.
        :param max_message_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_message_size_in_kilobytes ServicebusQueue#max_message_size_in_kilobytes}.
        :param max_size_in_megabytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_size_in_megabytes ServicebusQueue#max_size_in_megabytes}.
        :param requires_duplicate_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#requires_duplicate_detection ServicebusQueue#requires_duplicate_detection}.
        :param requires_session: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#requires_session ServicebusQueue#requires_session}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#status ServicebusQueue#status}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#timeouts ServicebusQueue#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicebusQueue.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServicebusQueueConfig(
            name=name,
            namespace_id=namespace_id,
            auto_delete_on_idle=auto_delete_on_idle,
            dead_lettering_on_message_expiration=dead_lettering_on_message_expiration,
            default_message_ttl=default_message_ttl,
            duplicate_detection_history_time_window=duplicate_detection_history_time_window,
            enable_batched_operations=enable_batched_operations,
            enable_express=enable_express,
            enable_partitioning=enable_partitioning,
            forward_dead_lettered_messages_to=forward_dead_lettered_messages_to,
            forward_to=forward_to,
            id=id,
            lock_duration=lock_duration,
            max_delivery_count=max_delivery_count,
            max_message_size_in_kilobytes=max_message_size_in_kilobytes,
            max_size_in_megabytes=max_size_in_megabytes,
            requires_duplicate_detection=requires_duplicate_detection,
            requires_session=requires_session,
            status=status,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#create ServicebusQueue#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#delete ServicebusQueue#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#read ServicebusQueue#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#update ServicebusQueue#update}.
        '''
        value = ServicebusQueueTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoDeleteOnIdle")
    def reset_auto_delete_on_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDeleteOnIdle", []))

    @jsii.member(jsii_name="resetDeadLetteringOnMessageExpiration")
    def reset_dead_lettering_on_message_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadLetteringOnMessageExpiration", []))

    @jsii.member(jsii_name="resetDefaultMessageTtl")
    def reset_default_message_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultMessageTtl", []))

    @jsii.member(jsii_name="resetDuplicateDetectionHistoryTimeWindow")
    def reset_duplicate_detection_history_time_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuplicateDetectionHistoryTimeWindow", []))

    @jsii.member(jsii_name="resetEnableBatchedOperations")
    def reset_enable_batched_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBatchedOperations", []))

    @jsii.member(jsii_name="resetEnableExpress")
    def reset_enable_express(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableExpress", []))

    @jsii.member(jsii_name="resetEnablePartitioning")
    def reset_enable_partitioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePartitioning", []))

    @jsii.member(jsii_name="resetForwardDeadLetteredMessagesTo")
    def reset_forward_dead_lettered_messages_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardDeadLetteredMessagesTo", []))

    @jsii.member(jsii_name="resetForwardTo")
    def reset_forward_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardTo", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLockDuration")
    def reset_lock_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLockDuration", []))

    @jsii.member(jsii_name="resetMaxDeliveryCount")
    def reset_max_delivery_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDeliveryCount", []))

    @jsii.member(jsii_name="resetMaxMessageSizeInKilobytes")
    def reset_max_message_size_in_kilobytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxMessageSizeInKilobytes", []))

    @jsii.member(jsii_name="resetMaxSizeInMegabytes")
    def reset_max_size_in_megabytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSizeInMegabytes", []))

    @jsii.member(jsii_name="resetRequiresDuplicateDetection")
    def reset_requires_duplicate_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiresDuplicateDetection", []))

    @jsii.member(jsii_name="resetRequiresSession")
    def reset_requires_session(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiresSession", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ServicebusQueueTimeoutsOutputReference":
        return typing.cast("ServicebusQueueTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteOnIdleInput")
    def auto_delete_on_idle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoDeleteOnIdleInput"))

    @builtins.property
    @jsii.member(jsii_name="deadLetteringOnMessageExpirationInput")
    def dead_lettering_on_message_expiration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deadLetteringOnMessageExpirationInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultMessageTtlInput")
    def default_message_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultMessageTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="duplicateDetectionHistoryTimeWindowInput")
    def duplicate_detection_history_time_window_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "duplicateDetectionHistoryTimeWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBatchedOperationsInput")
    def enable_batched_operations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBatchedOperationsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableExpressInput")
    def enable_express_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableExpressInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePartitioningInput")
    def enable_partitioning_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePartitioningInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardDeadLetteredMessagesToInput")
    def forward_dead_lettered_messages_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardDeadLetteredMessagesToInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardToInput")
    def forward_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardToInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lockDurationInput")
    def lock_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lockDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDeliveryCountInput")
    def max_delivery_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDeliveryCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxMessageSizeInKilobytesInput")
    def max_message_size_in_kilobytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxMessageSizeInKilobytesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeInMegabytesInput")
    def max_size_in_megabytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInMegabytesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceIdInput")
    def namespace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="requiresDuplicateDetectionInput")
    def requires_duplicate_detection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiresDuplicateDetectionInput"))

    @builtins.property
    @jsii.member(jsii_name="requiresSessionInput")
    def requires_session_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiresSessionInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ServicebusQueueTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ServicebusQueueTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoDeleteOnIdle"))

    @auto_delete_on_idle.setter
    def auto_delete_on_idle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "auto_delete_on_idle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDeleteOnIdle", value)

    @builtins.property
    @jsii.member(jsii_name="deadLetteringOnMessageExpiration")
    def dead_lettering_on_message_expiration(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deadLetteringOnMessageExpiration"))

    @dead_lettering_on_message_expiration.setter
    def dead_lettering_on_message_expiration(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "dead_lettering_on_message_expiration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deadLetteringOnMessageExpiration", value)

    @builtins.property
    @jsii.member(jsii_name="defaultMessageTtl")
    def default_message_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultMessageTtl"))

    @default_message_ttl.setter
    def default_message_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "default_message_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultMessageTtl", value)

    @builtins.property
    @jsii.member(jsii_name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duplicateDetectionHistoryTimeWindow"))

    @duplicate_detection_history_time_window.setter
    def duplicate_detection_history_time_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "duplicate_detection_history_time_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duplicateDetectionHistoryTimeWindow", value)

    @builtins.property
    @jsii.member(jsii_name="enableBatchedOperations")
    def enable_batched_operations(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBatchedOperations"))

    @enable_batched_operations.setter
    def enable_batched_operations(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "enable_batched_operations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBatchedOperations", value)

    @builtins.property
    @jsii.member(jsii_name="enableExpress")
    def enable_express(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableExpress"))

    @enable_express.setter
    def enable_express(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "enable_express").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableExpress", value)

    @builtins.property
    @jsii.member(jsii_name="enablePartitioning")
    def enable_partitioning(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enablePartitioning"))

    @enable_partitioning.setter
    def enable_partitioning(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "enable_partitioning").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePartitioning", value)

    @builtins.property
    @jsii.member(jsii_name="forwardDeadLetteredMessagesTo")
    def forward_dead_lettered_messages_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardDeadLetteredMessagesTo"))

    @forward_dead_lettered_messages_to.setter
    def forward_dead_lettered_messages_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "forward_dead_lettered_messages_to").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardDeadLetteredMessagesTo", value)

    @builtins.property
    @jsii.member(jsii_name="forwardTo")
    def forward_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardTo"))

    @forward_to.setter
    def forward_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "forward_to").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardTo", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lockDuration")
    def lock_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lockDuration"))

    @lock_duration.setter
    def lock_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "lock_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockDuration", value)

    @builtins.property
    @jsii.member(jsii_name="maxDeliveryCount")
    def max_delivery_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDeliveryCount"))

    @max_delivery_count.setter
    def max_delivery_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "max_delivery_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDeliveryCount", value)

    @builtins.property
    @jsii.member(jsii_name="maxMessageSizeInKilobytes")
    def max_message_size_in_kilobytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxMessageSizeInKilobytes"))

    @max_message_size_in_kilobytes.setter
    def max_message_size_in_kilobytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "max_message_size_in_kilobytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxMessageSizeInKilobytes", value)

    @builtins.property
    @jsii.member(jsii_name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSizeInMegabytes"))

    @max_size_in_megabytes.setter
    def max_size_in_megabytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "max_size_in_megabytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSizeInMegabytes", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @namespace_id.setter
    def namespace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "namespace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceId", value)

    @builtins.property
    @jsii.member(jsii_name="requiresDuplicateDetection")
    def requires_duplicate_detection(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requiresDuplicateDetection"))

    @requires_duplicate_detection.setter
    def requires_duplicate_detection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "requires_duplicate_detection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiresDuplicateDetection", value)

    @builtins.property
    @jsii.member(jsii_name="requiresSession")
    def requires_session(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requiresSession"))

    @requires_session.setter
    def requires_session(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "requires_session").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiresSession", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueue, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.servicebusQueue.ServicebusQueueConfig",
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
        "namespace_id": "namespaceId",
        "auto_delete_on_idle": "autoDeleteOnIdle",
        "dead_lettering_on_message_expiration": "deadLetteringOnMessageExpiration",
        "default_message_ttl": "defaultMessageTtl",
        "duplicate_detection_history_time_window": "duplicateDetectionHistoryTimeWindow",
        "enable_batched_operations": "enableBatchedOperations",
        "enable_express": "enableExpress",
        "enable_partitioning": "enablePartitioning",
        "forward_dead_lettered_messages_to": "forwardDeadLetteredMessagesTo",
        "forward_to": "forwardTo",
        "id": "id",
        "lock_duration": "lockDuration",
        "max_delivery_count": "maxDeliveryCount",
        "max_message_size_in_kilobytes": "maxMessageSizeInKilobytes",
        "max_size_in_megabytes": "maxSizeInMegabytes",
        "requires_duplicate_detection": "requiresDuplicateDetection",
        "requires_session": "requiresSession",
        "status": "status",
        "timeouts": "timeouts",
    },
)
class ServicebusQueueConfig(cdktf.TerraformMetaArguments):
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
        namespace_id: builtins.str,
        auto_delete_on_idle: typing.Optional[builtins.str] = None,
        dead_lettering_on_message_expiration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_message_ttl: typing.Optional[builtins.str] = None,
        duplicate_detection_history_time_window: typing.Optional[builtins.str] = None,
        enable_batched_operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_express: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_partitioning: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forward_dead_lettered_messages_to: typing.Optional[builtins.str] = None,
        forward_to: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        lock_duration: typing.Optional[builtins.str] = None,
        max_delivery_count: typing.Optional[jsii.Number] = None,
        max_message_size_in_kilobytes: typing.Optional[jsii.Number] = None,
        max_size_in_megabytes: typing.Optional[jsii.Number] = None,
        requires_duplicate_detection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        requires_session: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ServicebusQueueTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#name ServicebusQueue#name}.
        :param namespace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#namespace_id ServicebusQueue#namespace_id}.
        :param auto_delete_on_idle: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#auto_delete_on_idle ServicebusQueue#auto_delete_on_idle}.
        :param dead_lettering_on_message_expiration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#dead_lettering_on_message_expiration ServicebusQueue#dead_lettering_on_message_expiration}.
        :param default_message_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#default_message_ttl ServicebusQueue#default_message_ttl}.
        :param duplicate_detection_history_time_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#duplicate_detection_history_time_window ServicebusQueue#duplicate_detection_history_time_window}.
        :param enable_batched_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_batched_operations ServicebusQueue#enable_batched_operations}.
        :param enable_express: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_express ServicebusQueue#enable_express}.
        :param enable_partitioning: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_partitioning ServicebusQueue#enable_partitioning}.
        :param forward_dead_lettered_messages_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#forward_dead_lettered_messages_to ServicebusQueue#forward_dead_lettered_messages_to}.
        :param forward_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#forward_to ServicebusQueue#forward_to}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#id ServicebusQueue#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lock_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#lock_duration ServicebusQueue#lock_duration}.
        :param max_delivery_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_delivery_count ServicebusQueue#max_delivery_count}.
        :param max_message_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_message_size_in_kilobytes ServicebusQueue#max_message_size_in_kilobytes}.
        :param max_size_in_megabytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_size_in_megabytes ServicebusQueue#max_size_in_megabytes}.
        :param requires_duplicate_detection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#requires_duplicate_detection ServicebusQueue#requires_duplicate_detection}.
        :param requires_session: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#requires_session ServicebusQueue#requires_session}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#status ServicebusQueue#status}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#timeouts ServicebusQueue#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ServicebusQueueTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ServicebusQueueConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_id", value=namespace_id, expected_type=type_hints["namespace_id"])
            check_type(argname="argument auto_delete_on_idle", value=auto_delete_on_idle, expected_type=type_hints["auto_delete_on_idle"])
            check_type(argname="argument dead_lettering_on_message_expiration", value=dead_lettering_on_message_expiration, expected_type=type_hints["dead_lettering_on_message_expiration"])
            check_type(argname="argument default_message_ttl", value=default_message_ttl, expected_type=type_hints["default_message_ttl"])
            check_type(argname="argument duplicate_detection_history_time_window", value=duplicate_detection_history_time_window, expected_type=type_hints["duplicate_detection_history_time_window"])
            check_type(argname="argument enable_batched_operations", value=enable_batched_operations, expected_type=type_hints["enable_batched_operations"])
            check_type(argname="argument enable_express", value=enable_express, expected_type=type_hints["enable_express"])
            check_type(argname="argument enable_partitioning", value=enable_partitioning, expected_type=type_hints["enable_partitioning"])
            check_type(argname="argument forward_dead_lettered_messages_to", value=forward_dead_lettered_messages_to, expected_type=type_hints["forward_dead_lettered_messages_to"])
            check_type(argname="argument forward_to", value=forward_to, expected_type=type_hints["forward_to"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lock_duration", value=lock_duration, expected_type=type_hints["lock_duration"])
            check_type(argname="argument max_delivery_count", value=max_delivery_count, expected_type=type_hints["max_delivery_count"])
            check_type(argname="argument max_message_size_in_kilobytes", value=max_message_size_in_kilobytes, expected_type=type_hints["max_message_size_in_kilobytes"])
            check_type(argname="argument max_size_in_megabytes", value=max_size_in_megabytes, expected_type=type_hints["max_size_in_megabytes"])
            check_type(argname="argument requires_duplicate_detection", value=requires_duplicate_detection, expected_type=type_hints["requires_duplicate_detection"])
            check_type(argname="argument requires_session", value=requires_session, expected_type=type_hints["requires_session"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "namespace_id": namespace_id,
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
        if auto_delete_on_idle is not None:
            self._values["auto_delete_on_idle"] = auto_delete_on_idle
        if dead_lettering_on_message_expiration is not None:
            self._values["dead_lettering_on_message_expiration"] = dead_lettering_on_message_expiration
        if default_message_ttl is not None:
            self._values["default_message_ttl"] = default_message_ttl
        if duplicate_detection_history_time_window is not None:
            self._values["duplicate_detection_history_time_window"] = duplicate_detection_history_time_window
        if enable_batched_operations is not None:
            self._values["enable_batched_operations"] = enable_batched_operations
        if enable_express is not None:
            self._values["enable_express"] = enable_express
        if enable_partitioning is not None:
            self._values["enable_partitioning"] = enable_partitioning
        if forward_dead_lettered_messages_to is not None:
            self._values["forward_dead_lettered_messages_to"] = forward_dead_lettered_messages_to
        if forward_to is not None:
            self._values["forward_to"] = forward_to
        if id is not None:
            self._values["id"] = id
        if lock_duration is not None:
            self._values["lock_duration"] = lock_duration
        if max_delivery_count is not None:
            self._values["max_delivery_count"] = max_delivery_count
        if max_message_size_in_kilobytes is not None:
            self._values["max_message_size_in_kilobytes"] = max_message_size_in_kilobytes
        if max_size_in_megabytes is not None:
            self._values["max_size_in_megabytes"] = max_size_in_megabytes
        if requires_duplicate_detection is not None:
            self._values["requires_duplicate_detection"] = requires_duplicate_detection
        if requires_session is not None:
            self._values["requires_session"] = requires_session
        if status is not None:
            self._values["status"] = status
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#name ServicebusQueue#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#namespace_id ServicebusQueue#namespace_id}.'''
        result = self._values.get("namespace_id")
        assert result is not None, "Required property 'namespace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_delete_on_idle(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#auto_delete_on_idle ServicebusQueue#auto_delete_on_idle}.'''
        result = self._values.get("auto_delete_on_idle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dead_lettering_on_message_expiration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#dead_lettering_on_message_expiration ServicebusQueue#dead_lettering_on_message_expiration}.'''
        result = self._values.get("dead_lettering_on_message_expiration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def default_message_ttl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#default_message_ttl ServicebusQueue#default_message_ttl}.'''
        result = self._values.get("default_message_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def duplicate_detection_history_time_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#duplicate_detection_history_time_window ServicebusQueue#duplicate_detection_history_time_window}.'''
        result = self._values.get("duplicate_detection_history_time_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_batched_operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_batched_operations ServicebusQueue#enable_batched_operations}.'''
        result = self._values.get("enable_batched_operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_express(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_express ServicebusQueue#enable_express}.'''
        result = self._values.get("enable_express")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_partitioning(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#enable_partitioning ServicebusQueue#enable_partitioning}.'''
        result = self._values.get("enable_partitioning")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forward_dead_lettered_messages_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#forward_dead_lettered_messages_to ServicebusQueue#forward_dead_lettered_messages_to}.'''
        result = self._values.get("forward_dead_lettered_messages_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forward_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#forward_to ServicebusQueue#forward_to}.'''
        result = self._values.get("forward_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#id ServicebusQueue#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#lock_duration ServicebusQueue#lock_duration}.'''
        result = self._values.get("lock_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_delivery_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_delivery_count ServicebusQueue#max_delivery_count}.'''
        result = self._values.get("max_delivery_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_message_size_in_kilobytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_message_size_in_kilobytes ServicebusQueue#max_message_size_in_kilobytes}.'''
        result = self._values.get("max_message_size_in_kilobytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_size_in_megabytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#max_size_in_megabytes ServicebusQueue#max_size_in_megabytes}.'''
        result = self._values.get("max_size_in_megabytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requires_duplicate_detection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#requires_duplicate_detection ServicebusQueue#requires_duplicate_detection}.'''
        result = self._values.get("requires_duplicate_detection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def requires_session(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#requires_session ServicebusQueue#requires_session}.'''
        result = self._values.get("requires_session")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#status ServicebusQueue#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ServicebusQueueTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#timeouts ServicebusQueue#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ServicebusQueueTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicebusQueueConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.servicebusQueue.ServicebusQueueTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ServicebusQueueTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#create ServicebusQueue#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#delete ServicebusQueue#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#read ServicebusQueue#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#update ServicebusQueue#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServicebusQueueTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#create ServicebusQueue#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#delete ServicebusQueue#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#read ServicebusQueue#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue#update ServicebusQueue#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicebusQueueTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServicebusQueueTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.servicebusQueue.ServicebusQueueTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ServicebusQueueTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ServicebusQueueTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueueTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueueTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueueTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServicebusQueueTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServicebusQueueTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServicebusQueueTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServicebusQueueTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServicebusQueue",
    "ServicebusQueueConfig",
    "ServicebusQueueTimeouts",
    "ServicebusQueueTimeoutsOutputReference",
]

publication.publish()
