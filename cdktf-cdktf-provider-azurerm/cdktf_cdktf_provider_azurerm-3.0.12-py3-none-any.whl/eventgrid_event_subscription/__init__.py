'''
# `azurerm_eventgrid_event_subscription`

Refer to the Terraform Registory for docs: [`azurerm_eventgrid_event_subscription`](https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription).
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


class EventgridEventSubscription(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription azurerm_eventgrid_event_subscription}.'''

    def __init__(
        self,
        scope_: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        scope: builtins.str,
        advanced_filter: typing.Optional[typing.Union["EventgridEventSubscriptionAdvancedFilter", typing.Dict[str, typing.Any]]] = None,
        advanced_filtering_on_arrays_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        azure_function_endpoint: typing.Optional[typing.Union["EventgridEventSubscriptionAzureFunctionEndpoint", typing.Dict[str, typing.Any]]] = None,
        dead_letter_identity: typing.Optional[typing.Union["EventgridEventSubscriptionDeadLetterIdentity", typing.Dict[str, typing.Any]]] = None,
        delivery_identity: typing.Optional[typing.Union["EventgridEventSubscriptionDeliveryIdentity", typing.Dict[str, typing.Any]]] = None,
        delivery_property: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionDeliveryProperty", typing.Dict[str, typing.Any]]]]] = None,
        event_delivery_schema: typing.Optional[builtins.str] = None,
        eventhub_endpoint_id: typing.Optional[builtins.str] = None,
        expiration_time_utc: typing.Optional[builtins.str] = None,
        hybrid_connection_endpoint_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        included_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        retry_policy: typing.Optional[typing.Union["EventgridEventSubscriptionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        service_bus_queue_endpoint_id: typing.Optional[builtins.str] = None,
        service_bus_topic_endpoint_id: typing.Optional[builtins.str] = None,
        storage_blob_dead_letter_destination: typing.Optional[typing.Union["EventgridEventSubscriptionStorageBlobDeadLetterDestination", typing.Dict[str, typing.Any]]] = None,
        storage_queue_endpoint: typing.Optional[typing.Union["EventgridEventSubscriptionStorageQueueEndpoint", typing.Dict[str, typing.Any]]] = None,
        subject_filter: typing.Optional[typing.Union["EventgridEventSubscriptionSubjectFilter", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["EventgridEventSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
        webhook_endpoint: typing.Optional[typing.Union["EventgridEventSubscriptionWebhookEndpoint", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription azurerm_eventgrid_event_subscription} Resource.

        :param scope_: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#name EventgridEventSubscription#name}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#scope EventgridEventSubscription#scope}.
        :param advanced_filter: advanced_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#advanced_filter EventgridEventSubscription#advanced_filter}
        :param advanced_filtering_on_arrays_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#advanced_filtering_on_arrays_enabled EventgridEventSubscription#advanced_filtering_on_arrays_enabled}.
        :param azure_function_endpoint: azure_function_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#azure_function_endpoint EventgridEventSubscription#azure_function_endpoint}
        :param dead_letter_identity: dead_letter_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#dead_letter_identity EventgridEventSubscription#dead_letter_identity}
        :param delivery_identity: delivery_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delivery_identity EventgridEventSubscription#delivery_identity}
        :param delivery_property: delivery_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delivery_property EventgridEventSubscription#delivery_property}
        :param event_delivery_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#event_delivery_schema EventgridEventSubscription#event_delivery_schema}.
        :param eventhub_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#eventhub_endpoint_id EventgridEventSubscription#eventhub_endpoint_id}.
        :param expiration_time_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#expiration_time_utc EventgridEventSubscription#expiration_time_utc}.
        :param hybrid_connection_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#hybrid_connection_endpoint_id EventgridEventSubscription#hybrid_connection_endpoint_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#id EventgridEventSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param included_event_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#included_event_types EventgridEventSubscription#included_event_types}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#labels EventgridEventSubscription#labels}.
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#retry_policy EventgridEventSubscription#retry_policy}
        :param service_bus_queue_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#service_bus_queue_endpoint_id EventgridEventSubscription#service_bus_queue_endpoint_id}.
        :param service_bus_topic_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#service_bus_topic_endpoint_id EventgridEventSubscription#service_bus_topic_endpoint_id}.
        :param storage_blob_dead_letter_destination: storage_blob_dead_letter_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_blob_dead_letter_destination EventgridEventSubscription#storage_blob_dead_letter_destination}
        :param storage_queue_endpoint: storage_queue_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_queue_endpoint EventgridEventSubscription#storage_queue_endpoint}
        :param subject_filter: subject_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_filter EventgridEventSubscription#subject_filter}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#timeouts EventgridEventSubscription#timeouts}
        :param webhook_endpoint: webhook_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#webhook_endpoint EventgridEventSubscription#webhook_endpoint}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscription.__init__)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EventgridEventSubscriptionConfig(
            name=name,
            scope=scope,
            advanced_filter=advanced_filter,
            advanced_filtering_on_arrays_enabled=advanced_filtering_on_arrays_enabled,
            azure_function_endpoint=azure_function_endpoint,
            dead_letter_identity=dead_letter_identity,
            delivery_identity=delivery_identity,
            delivery_property=delivery_property,
            event_delivery_schema=event_delivery_schema,
            eventhub_endpoint_id=eventhub_endpoint_id,
            expiration_time_utc=expiration_time_utc,
            hybrid_connection_endpoint_id=hybrid_connection_endpoint_id,
            id=id,
            included_event_types=included_event_types,
            labels=labels,
            retry_policy=retry_policy,
            service_bus_queue_endpoint_id=service_bus_queue_endpoint_id,
            service_bus_topic_endpoint_id=service_bus_topic_endpoint_id,
            storage_blob_dead_letter_destination=storage_blob_dead_letter_destination,
            storage_queue_endpoint=storage_queue_endpoint,
            subject_filter=subject_filter,
            timeouts=timeouts,
            webhook_endpoint=webhook_endpoint,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope_, id_, config])

    @jsii.member(jsii_name="putAdvancedFilter")
    def put_advanced_filter(
        self,
        *,
        bool_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterBoolEquals", typing.Dict[str, typing.Any]]]]] = None,
        is_not_null: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterIsNotNull", typing.Dict[str, typing.Any]]]]] = None,
        is_null_or_undefined: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined", typing.Dict[str, typing.Any]]]]] = None,
        number_greater_than: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberGreaterThan", typing.Dict[str, typing.Any]]]]] = None,
        number_greater_than_or_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals", typing.Dict[str, typing.Any]]]]] = None,
        number_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberIn", typing.Dict[str, typing.Any]]]]] = None,
        number_in_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberInRange", typing.Dict[str, typing.Any]]]]] = None,
        number_less_than: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberLessThan", typing.Dict[str, typing.Any]]]]] = None,
        number_less_than_or_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals", typing.Dict[str, typing.Any]]]]] = None,
        number_not_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberNotIn", typing.Dict[str, typing.Any]]]]] = None,
        number_not_in_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberNotInRange", typing.Dict[str, typing.Any]]]]] = None,
        string_begins_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringBeginsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_contains: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringContains", typing.Dict[str, typing.Any]]]]] = None,
        string_ends_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringEndsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringIn", typing.Dict[str, typing.Any]]]]] = None,
        string_not_begins_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_not_contains: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotContains", typing.Dict[str, typing.Any]]]]] = None,
        string_not_ends_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotEndsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_not_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotIn", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param bool_equals: bool_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#bool_equals EventgridEventSubscription#bool_equals}
        :param is_not_null: is_not_null block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#is_not_null EventgridEventSubscription#is_not_null}
        :param is_null_or_undefined: is_null_or_undefined block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#is_null_or_undefined EventgridEventSubscription#is_null_or_undefined}
        :param number_greater_than: number_greater_than block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_greater_than EventgridEventSubscription#number_greater_than}
        :param number_greater_than_or_equals: number_greater_than_or_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_greater_than_or_equals EventgridEventSubscription#number_greater_than_or_equals}
        :param number_in: number_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_in EventgridEventSubscription#number_in}
        :param number_in_range: number_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_in_range EventgridEventSubscription#number_in_range}
        :param number_less_than: number_less_than block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_less_than EventgridEventSubscription#number_less_than}
        :param number_less_than_or_equals: number_less_than_or_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_less_than_or_equals EventgridEventSubscription#number_less_than_or_equals}
        :param number_not_in: number_not_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_not_in EventgridEventSubscription#number_not_in}
        :param number_not_in_range: number_not_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_not_in_range EventgridEventSubscription#number_not_in_range}
        :param string_begins_with: string_begins_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_begins_with EventgridEventSubscription#string_begins_with}
        :param string_contains: string_contains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_contains EventgridEventSubscription#string_contains}
        :param string_ends_with: string_ends_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_ends_with EventgridEventSubscription#string_ends_with}
        :param string_in: string_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_in EventgridEventSubscription#string_in}
        :param string_not_begins_with: string_not_begins_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_begins_with EventgridEventSubscription#string_not_begins_with}
        :param string_not_contains: string_not_contains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_contains EventgridEventSubscription#string_not_contains}
        :param string_not_ends_with: string_not_ends_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_ends_with EventgridEventSubscription#string_not_ends_with}
        :param string_not_in: string_not_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_in EventgridEventSubscription#string_not_in}
        '''
        value = EventgridEventSubscriptionAdvancedFilter(
            bool_equals=bool_equals,
            is_not_null=is_not_null,
            is_null_or_undefined=is_null_or_undefined,
            number_greater_than=number_greater_than,
            number_greater_than_or_equals=number_greater_than_or_equals,
            number_in=number_in,
            number_in_range=number_in_range,
            number_less_than=number_less_than,
            number_less_than_or_equals=number_less_than_or_equals,
            number_not_in=number_not_in,
            number_not_in_range=number_not_in_range,
            string_begins_with=string_begins_with,
            string_contains=string_contains,
            string_ends_with=string_ends_with,
            string_in=string_in,
            string_not_begins_with=string_not_begins_with,
            string_not_contains=string_not_contains,
            string_not_ends_with=string_not_ends_with,
            string_not_in=string_not_in,
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedFilter", [value]))

    @jsii.member(jsii_name="putAzureFunctionEndpoint")
    def put_azure_function_endpoint(
        self,
        *,
        function_id: builtins.str,
        max_events_per_batch: typing.Optional[jsii.Number] = None,
        preferred_batch_size_in_kilobytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param function_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#function_id EventgridEventSubscription#function_id}.
        :param max_events_per_batch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_events_per_batch EventgridEventSubscription#max_events_per_batch}.
        :param preferred_batch_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#preferred_batch_size_in_kilobytes EventgridEventSubscription#preferred_batch_size_in_kilobytes}.
        '''
        value = EventgridEventSubscriptionAzureFunctionEndpoint(
            function_id=function_id,
            max_events_per_batch=max_events_per_batch,
            preferred_batch_size_in_kilobytes=preferred_batch_size_in_kilobytes,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureFunctionEndpoint", [value]))

    @jsii.member(jsii_name="putDeadLetterIdentity")
    def put_dead_letter_identity(
        self,
        *,
        type: builtins.str,
        user_assigned_identity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#type EventgridEventSubscription#type}.
        :param user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#user_assigned_identity EventgridEventSubscription#user_assigned_identity}.
        '''
        value = EventgridEventSubscriptionDeadLetterIdentity(
            type=type, user_assigned_identity=user_assigned_identity
        )

        return typing.cast(None, jsii.invoke(self, "putDeadLetterIdentity", [value]))

    @jsii.member(jsii_name="putDeliveryIdentity")
    def put_delivery_identity(
        self,
        *,
        type: builtins.str,
        user_assigned_identity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#type EventgridEventSubscription#type}.
        :param user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#user_assigned_identity EventgridEventSubscription#user_assigned_identity}.
        '''
        value = EventgridEventSubscriptionDeliveryIdentity(
            type=type, user_assigned_identity=user_assigned_identity
        )

        return typing.cast(None, jsii.invoke(self, "putDeliveryIdentity", [value]))

    @jsii.member(jsii_name="putDeliveryProperty")
    def put_delivery_property(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionDeliveryProperty", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscription.put_delivery_property)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeliveryProperty", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        event_time_to_live: jsii.Number,
        max_delivery_attempts: jsii.Number,
    ) -> None:
        '''
        :param event_time_to_live: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#event_time_to_live EventgridEventSubscription#event_time_to_live}.
        :param max_delivery_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_delivery_attempts EventgridEventSubscription#max_delivery_attempts}.
        '''
        value = EventgridEventSubscriptionRetryPolicy(
            event_time_to_live=event_time_to_live,
            max_delivery_attempts=max_delivery_attempts,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putStorageBlobDeadLetterDestination")
    def put_storage_blob_dead_letter_destination(
        self,
        *,
        storage_account_id: builtins.str,
        storage_blob_container_name: builtins.str,
    ) -> None:
        '''
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_account_id EventgridEventSubscription#storage_account_id}.
        :param storage_blob_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_blob_container_name EventgridEventSubscription#storage_blob_container_name}.
        '''
        value = EventgridEventSubscriptionStorageBlobDeadLetterDestination(
            storage_account_id=storage_account_id,
            storage_blob_container_name=storage_blob_container_name,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageBlobDeadLetterDestination", [value]))

    @jsii.member(jsii_name="putStorageQueueEndpoint")
    def put_storage_queue_endpoint(
        self,
        *,
        queue_name: builtins.str,
        storage_account_id: builtins.str,
        queue_message_time_to_live_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param queue_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#queue_name EventgridEventSubscription#queue_name}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_account_id EventgridEventSubscription#storage_account_id}.
        :param queue_message_time_to_live_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#queue_message_time_to_live_in_seconds EventgridEventSubscription#queue_message_time_to_live_in_seconds}.
        '''
        value = EventgridEventSubscriptionStorageQueueEndpoint(
            queue_name=queue_name,
            storage_account_id=storage_account_id,
            queue_message_time_to_live_in_seconds=queue_message_time_to_live_in_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageQueueEndpoint", [value]))

    @jsii.member(jsii_name="putSubjectFilter")
    def put_subject_filter(
        self,
        *,
        case_sensitive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subject_begins_with: typing.Optional[builtins.str] = None,
        subject_ends_with: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param case_sensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#case_sensitive EventgridEventSubscription#case_sensitive}.
        :param subject_begins_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_begins_with EventgridEventSubscription#subject_begins_with}.
        :param subject_ends_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_ends_with EventgridEventSubscription#subject_ends_with}.
        '''
        value = EventgridEventSubscriptionSubjectFilter(
            case_sensitive=case_sensitive,
            subject_begins_with=subject_begins_with,
            subject_ends_with=subject_ends_with,
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectFilter", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#create EventgridEventSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delete EventgridEventSubscription#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#read EventgridEventSubscription#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#update EventgridEventSubscription#update}.
        '''
        value = EventgridEventSubscriptionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWebhookEndpoint")
    def put_webhook_endpoint(
        self,
        *,
        url: builtins.str,
        active_directory_app_id_or_uri: typing.Optional[builtins.str] = None,
        active_directory_tenant_id: typing.Optional[builtins.str] = None,
        max_events_per_batch: typing.Optional[jsii.Number] = None,
        preferred_batch_size_in_kilobytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#url EventgridEventSubscription#url}.
        :param active_directory_app_id_or_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#active_directory_app_id_or_uri EventgridEventSubscription#active_directory_app_id_or_uri}.
        :param active_directory_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#active_directory_tenant_id EventgridEventSubscription#active_directory_tenant_id}.
        :param max_events_per_batch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_events_per_batch EventgridEventSubscription#max_events_per_batch}.
        :param preferred_batch_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#preferred_batch_size_in_kilobytes EventgridEventSubscription#preferred_batch_size_in_kilobytes}.
        '''
        value = EventgridEventSubscriptionWebhookEndpoint(
            url=url,
            active_directory_app_id_or_uri=active_directory_app_id_or_uri,
            active_directory_tenant_id=active_directory_tenant_id,
            max_events_per_batch=max_events_per_batch,
            preferred_batch_size_in_kilobytes=preferred_batch_size_in_kilobytes,
        )

        return typing.cast(None, jsii.invoke(self, "putWebhookEndpoint", [value]))

    @jsii.member(jsii_name="resetAdvancedFilter")
    def reset_advanced_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedFilter", []))

    @jsii.member(jsii_name="resetAdvancedFilteringOnArraysEnabled")
    def reset_advanced_filtering_on_arrays_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedFilteringOnArraysEnabled", []))

    @jsii.member(jsii_name="resetAzureFunctionEndpoint")
    def reset_azure_function_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureFunctionEndpoint", []))

    @jsii.member(jsii_name="resetDeadLetterIdentity")
    def reset_dead_letter_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadLetterIdentity", []))

    @jsii.member(jsii_name="resetDeliveryIdentity")
    def reset_delivery_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryIdentity", []))

    @jsii.member(jsii_name="resetDeliveryProperty")
    def reset_delivery_property(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryProperty", []))

    @jsii.member(jsii_name="resetEventDeliverySchema")
    def reset_event_delivery_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventDeliverySchema", []))

    @jsii.member(jsii_name="resetEventhubEndpointId")
    def reset_eventhub_endpoint_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventhubEndpointId", []))

    @jsii.member(jsii_name="resetExpirationTimeUtc")
    def reset_expiration_time_utc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationTimeUtc", []))

    @jsii.member(jsii_name="resetHybridConnectionEndpointId")
    def reset_hybrid_connection_endpoint_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHybridConnectionEndpointId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncludedEventTypes")
    def reset_included_event_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedEventTypes", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetServiceBusQueueEndpointId")
    def reset_service_bus_queue_endpoint_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceBusQueueEndpointId", []))

    @jsii.member(jsii_name="resetServiceBusTopicEndpointId")
    def reset_service_bus_topic_endpoint_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceBusTopicEndpointId", []))

    @jsii.member(jsii_name="resetStorageBlobDeadLetterDestination")
    def reset_storage_blob_dead_letter_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageBlobDeadLetterDestination", []))

    @jsii.member(jsii_name="resetStorageQueueEndpoint")
    def reset_storage_queue_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageQueueEndpoint", []))

    @jsii.member(jsii_name="resetSubjectFilter")
    def reset_subject_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectFilter", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWebhookEndpoint")
    def reset_webhook_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhookEndpoint", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="advancedFilter")
    def advanced_filter(
        self,
    ) -> "EventgridEventSubscriptionAdvancedFilterOutputReference":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterOutputReference", jsii.get(self, "advancedFilter"))

    @builtins.property
    @jsii.member(jsii_name="azureFunctionEndpoint")
    def azure_function_endpoint(
        self,
    ) -> "EventgridEventSubscriptionAzureFunctionEndpointOutputReference":
        return typing.cast("EventgridEventSubscriptionAzureFunctionEndpointOutputReference", jsii.get(self, "azureFunctionEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterIdentity")
    def dead_letter_identity(
        self,
    ) -> "EventgridEventSubscriptionDeadLetterIdentityOutputReference":
        return typing.cast("EventgridEventSubscriptionDeadLetterIdentityOutputReference", jsii.get(self, "deadLetterIdentity"))

    @builtins.property
    @jsii.member(jsii_name="deliveryIdentity")
    def delivery_identity(
        self,
    ) -> "EventgridEventSubscriptionDeliveryIdentityOutputReference":
        return typing.cast("EventgridEventSubscriptionDeliveryIdentityOutputReference", jsii.get(self, "deliveryIdentity"))

    @builtins.property
    @jsii.member(jsii_name="deliveryProperty")
    def delivery_property(self) -> "EventgridEventSubscriptionDeliveryPropertyList":
        return typing.cast("EventgridEventSubscriptionDeliveryPropertyList", jsii.get(self, "deliveryProperty"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(self) -> "EventgridEventSubscriptionRetryPolicyOutputReference":
        return typing.cast("EventgridEventSubscriptionRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="storageBlobDeadLetterDestination")
    def storage_blob_dead_letter_destination(
        self,
    ) -> "EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference":
        return typing.cast("EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference", jsii.get(self, "storageBlobDeadLetterDestination"))

    @builtins.property
    @jsii.member(jsii_name="storageQueueEndpoint")
    def storage_queue_endpoint(
        self,
    ) -> "EventgridEventSubscriptionStorageQueueEndpointOutputReference":
        return typing.cast("EventgridEventSubscriptionStorageQueueEndpointOutputReference", jsii.get(self, "storageQueueEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="subjectFilter")
    def subject_filter(
        self,
    ) -> "EventgridEventSubscriptionSubjectFilterOutputReference":
        return typing.cast("EventgridEventSubscriptionSubjectFilterOutputReference", jsii.get(self, "subjectFilter"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EventgridEventSubscriptionTimeoutsOutputReference":
        return typing.cast("EventgridEventSubscriptionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="webhookEndpoint")
    def webhook_endpoint(
        self,
    ) -> "EventgridEventSubscriptionWebhookEndpointOutputReference":
        return typing.cast("EventgridEventSubscriptionWebhookEndpointOutputReference", jsii.get(self, "webhookEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="advancedFilteringOnArraysEnabledInput")
    def advanced_filtering_on_arrays_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "advancedFilteringOnArraysEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedFilterInput")
    def advanced_filter_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionAdvancedFilter"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionAdvancedFilter"], jsii.get(self, "advancedFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFunctionEndpointInput")
    def azure_function_endpoint_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionAzureFunctionEndpoint"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionAzureFunctionEndpoint"], jsii.get(self, "azureFunctionEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterIdentityInput")
    def dead_letter_identity_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionDeadLetterIdentity"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionDeadLetterIdentity"], jsii.get(self, "deadLetterIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryIdentityInput")
    def delivery_identity_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionDeliveryIdentity"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionDeliveryIdentity"], jsii.get(self, "deliveryIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryPropertyInput")
    def delivery_property_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionDeliveryProperty"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionDeliveryProperty"]]], jsii.get(self, "deliveryPropertyInput"))

    @builtins.property
    @jsii.member(jsii_name="eventDeliverySchemaInput")
    def event_delivery_schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventDeliverySchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="eventhubEndpointIdInput")
    def eventhub_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventhubEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeUtcInput")
    def expiration_time_utc_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationTimeUtcInput"))

    @builtins.property
    @jsii.member(jsii_name="hybridConnectionEndpointIdInput")
    def hybrid_connection_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hybridConnectionEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includedEventTypesInput")
    def included_event_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedEventTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionRetryPolicy"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceBusQueueEndpointIdInput")
    def service_bus_queue_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceBusQueueEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceBusTopicEndpointIdInput")
    def service_bus_topic_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceBusTopicEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageBlobDeadLetterDestinationInput")
    def storage_blob_dead_letter_destination_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionStorageBlobDeadLetterDestination"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionStorageBlobDeadLetterDestination"], jsii.get(self, "storageBlobDeadLetterDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="storageQueueEndpointInput")
    def storage_queue_endpoint_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionStorageQueueEndpoint"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionStorageQueueEndpoint"], jsii.get(self, "storageQueueEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectFilterInput")
    def subject_filter_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionSubjectFilter"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionSubjectFilter"], jsii.get(self, "subjectFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["EventgridEventSubscriptionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["EventgridEventSubscriptionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookEndpointInput")
    def webhook_endpoint_input(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionWebhookEndpoint"]:
        return typing.cast(typing.Optional["EventgridEventSubscriptionWebhookEndpoint"], jsii.get(self, "webhookEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedFilteringOnArraysEnabled")
    def advanced_filtering_on_arrays_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "advancedFilteringOnArraysEnabled"))

    @advanced_filtering_on_arrays_enabled.setter
    def advanced_filtering_on_arrays_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "advanced_filtering_on_arrays_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedFilteringOnArraysEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventDeliverySchema")
    def event_delivery_schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventDeliverySchema"))

    @event_delivery_schema.setter
    def event_delivery_schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "event_delivery_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDeliverySchema", value)

    @builtins.property
    @jsii.member(jsii_name="eventhubEndpointId")
    def eventhub_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventhubEndpointId"))

    @eventhub_endpoint_id.setter
    def eventhub_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "eventhub_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventhubEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="expirationTimeUtc")
    def expiration_time_utc(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationTimeUtc"))

    @expiration_time_utc.setter
    def expiration_time_utc(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "expiration_time_utc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTimeUtc", value)

    @builtins.property
    @jsii.member(jsii_name="hybridConnectionEndpointId")
    def hybrid_connection_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hybridConnectionEndpointId"))

    @hybrid_connection_endpoint_id.setter
    def hybrid_connection_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "hybrid_connection_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hybridConnectionEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="includedEventTypes")
    def included_event_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedEventTypes"))

    @included_event_types.setter
    def included_event_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "included_event_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedEventTypes", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="serviceBusQueueEndpointId")
    def service_bus_queue_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceBusQueueEndpointId"))

    @service_bus_queue_endpoint_id.setter
    def service_bus_queue_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "service_bus_queue_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceBusQueueEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceBusTopicEndpointId")
    def service_bus_topic_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceBusTopicEndpointId"))

    @service_bus_topic_endpoint_id.setter
    def service_bus_topic_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscription, "service_bus_topic_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceBusTopicEndpointId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilter",
    jsii_struct_bases=[],
    name_mapping={
        "bool_equals": "boolEquals",
        "is_not_null": "isNotNull",
        "is_null_or_undefined": "isNullOrUndefined",
        "number_greater_than": "numberGreaterThan",
        "number_greater_than_or_equals": "numberGreaterThanOrEquals",
        "number_in": "numberIn",
        "number_in_range": "numberInRange",
        "number_less_than": "numberLessThan",
        "number_less_than_or_equals": "numberLessThanOrEquals",
        "number_not_in": "numberNotIn",
        "number_not_in_range": "numberNotInRange",
        "string_begins_with": "stringBeginsWith",
        "string_contains": "stringContains",
        "string_ends_with": "stringEndsWith",
        "string_in": "stringIn",
        "string_not_begins_with": "stringNotBeginsWith",
        "string_not_contains": "stringNotContains",
        "string_not_ends_with": "stringNotEndsWith",
        "string_not_in": "stringNotIn",
    },
)
class EventgridEventSubscriptionAdvancedFilter:
    def __init__(
        self,
        *,
        bool_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterBoolEquals", typing.Dict[str, typing.Any]]]]] = None,
        is_not_null: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterIsNotNull", typing.Dict[str, typing.Any]]]]] = None,
        is_null_or_undefined: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined", typing.Dict[str, typing.Any]]]]] = None,
        number_greater_than: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberGreaterThan", typing.Dict[str, typing.Any]]]]] = None,
        number_greater_than_or_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals", typing.Dict[str, typing.Any]]]]] = None,
        number_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberIn", typing.Dict[str, typing.Any]]]]] = None,
        number_in_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberInRange", typing.Dict[str, typing.Any]]]]] = None,
        number_less_than: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberLessThan", typing.Dict[str, typing.Any]]]]] = None,
        number_less_than_or_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals", typing.Dict[str, typing.Any]]]]] = None,
        number_not_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberNotIn", typing.Dict[str, typing.Any]]]]] = None,
        number_not_in_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterNumberNotInRange", typing.Dict[str, typing.Any]]]]] = None,
        string_begins_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringBeginsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_contains: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringContains", typing.Dict[str, typing.Any]]]]] = None,
        string_ends_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringEndsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringIn", typing.Dict[str, typing.Any]]]]] = None,
        string_not_begins_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_not_contains: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotContains", typing.Dict[str, typing.Any]]]]] = None,
        string_not_ends_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotEndsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_not_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotIn", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param bool_equals: bool_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#bool_equals EventgridEventSubscription#bool_equals}
        :param is_not_null: is_not_null block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#is_not_null EventgridEventSubscription#is_not_null}
        :param is_null_or_undefined: is_null_or_undefined block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#is_null_or_undefined EventgridEventSubscription#is_null_or_undefined}
        :param number_greater_than: number_greater_than block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_greater_than EventgridEventSubscription#number_greater_than}
        :param number_greater_than_or_equals: number_greater_than_or_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_greater_than_or_equals EventgridEventSubscription#number_greater_than_or_equals}
        :param number_in: number_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_in EventgridEventSubscription#number_in}
        :param number_in_range: number_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_in_range EventgridEventSubscription#number_in_range}
        :param number_less_than: number_less_than block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_less_than EventgridEventSubscription#number_less_than}
        :param number_less_than_or_equals: number_less_than_or_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_less_than_or_equals EventgridEventSubscription#number_less_than_or_equals}
        :param number_not_in: number_not_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_not_in EventgridEventSubscription#number_not_in}
        :param number_not_in_range: number_not_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_not_in_range EventgridEventSubscription#number_not_in_range}
        :param string_begins_with: string_begins_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_begins_with EventgridEventSubscription#string_begins_with}
        :param string_contains: string_contains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_contains EventgridEventSubscription#string_contains}
        :param string_ends_with: string_ends_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_ends_with EventgridEventSubscription#string_ends_with}
        :param string_in: string_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_in EventgridEventSubscription#string_in}
        :param string_not_begins_with: string_not_begins_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_begins_with EventgridEventSubscription#string_not_begins_with}
        :param string_not_contains: string_not_contains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_contains EventgridEventSubscription#string_not_contains}
        :param string_not_ends_with: string_not_ends_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_ends_with EventgridEventSubscription#string_not_ends_with}
        :param string_not_in: string_not_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_in EventgridEventSubscription#string_not_in}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilter.__init__)
            check_type(argname="argument bool_equals", value=bool_equals, expected_type=type_hints["bool_equals"])
            check_type(argname="argument is_not_null", value=is_not_null, expected_type=type_hints["is_not_null"])
            check_type(argname="argument is_null_or_undefined", value=is_null_or_undefined, expected_type=type_hints["is_null_or_undefined"])
            check_type(argname="argument number_greater_than", value=number_greater_than, expected_type=type_hints["number_greater_than"])
            check_type(argname="argument number_greater_than_or_equals", value=number_greater_than_or_equals, expected_type=type_hints["number_greater_than_or_equals"])
            check_type(argname="argument number_in", value=number_in, expected_type=type_hints["number_in"])
            check_type(argname="argument number_in_range", value=number_in_range, expected_type=type_hints["number_in_range"])
            check_type(argname="argument number_less_than", value=number_less_than, expected_type=type_hints["number_less_than"])
            check_type(argname="argument number_less_than_or_equals", value=number_less_than_or_equals, expected_type=type_hints["number_less_than_or_equals"])
            check_type(argname="argument number_not_in", value=number_not_in, expected_type=type_hints["number_not_in"])
            check_type(argname="argument number_not_in_range", value=number_not_in_range, expected_type=type_hints["number_not_in_range"])
            check_type(argname="argument string_begins_with", value=string_begins_with, expected_type=type_hints["string_begins_with"])
            check_type(argname="argument string_contains", value=string_contains, expected_type=type_hints["string_contains"])
            check_type(argname="argument string_ends_with", value=string_ends_with, expected_type=type_hints["string_ends_with"])
            check_type(argname="argument string_in", value=string_in, expected_type=type_hints["string_in"])
            check_type(argname="argument string_not_begins_with", value=string_not_begins_with, expected_type=type_hints["string_not_begins_with"])
            check_type(argname="argument string_not_contains", value=string_not_contains, expected_type=type_hints["string_not_contains"])
            check_type(argname="argument string_not_ends_with", value=string_not_ends_with, expected_type=type_hints["string_not_ends_with"])
            check_type(argname="argument string_not_in", value=string_not_in, expected_type=type_hints["string_not_in"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bool_equals is not None:
            self._values["bool_equals"] = bool_equals
        if is_not_null is not None:
            self._values["is_not_null"] = is_not_null
        if is_null_or_undefined is not None:
            self._values["is_null_or_undefined"] = is_null_or_undefined
        if number_greater_than is not None:
            self._values["number_greater_than"] = number_greater_than
        if number_greater_than_or_equals is not None:
            self._values["number_greater_than_or_equals"] = number_greater_than_or_equals
        if number_in is not None:
            self._values["number_in"] = number_in
        if number_in_range is not None:
            self._values["number_in_range"] = number_in_range
        if number_less_than is not None:
            self._values["number_less_than"] = number_less_than
        if number_less_than_or_equals is not None:
            self._values["number_less_than_or_equals"] = number_less_than_or_equals
        if number_not_in is not None:
            self._values["number_not_in"] = number_not_in
        if number_not_in_range is not None:
            self._values["number_not_in_range"] = number_not_in_range
        if string_begins_with is not None:
            self._values["string_begins_with"] = string_begins_with
        if string_contains is not None:
            self._values["string_contains"] = string_contains
        if string_ends_with is not None:
            self._values["string_ends_with"] = string_ends_with
        if string_in is not None:
            self._values["string_in"] = string_in
        if string_not_begins_with is not None:
            self._values["string_not_begins_with"] = string_not_begins_with
        if string_not_contains is not None:
            self._values["string_not_contains"] = string_not_contains
        if string_not_ends_with is not None:
            self._values["string_not_ends_with"] = string_not_ends_with
        if string_not_in is not None:
            self._values["string_not_in"] = string_not_in

    @builtins.property
    def bool_equals(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterBoolEquals"]]]:
        '''bool_equals block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#bool_equals EventgridEventSubscription#bool_equals}
        '''
        result = self._values.get("bool_equals")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterBoolEquals"]]], result)

    @builtins.property
    def is_not_null(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterIsNotNull"]]]:
        '''is_not_null block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#is_not_null EventgridEventSubscription#is_not_null}
        '''
        result = self._values.get("is_not_null")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterIsNotNull"]]], result)

    @builtins.property
    def is_null_or_undefined(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined"]]]:
        '''is_null_or_undefined block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#is_null_or_undefined EventgridEventSubscription#is_null_or_undefined}
        '''
        result = self._values.get("is_null_or_undefined")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined"]]], result)

    @builtins.property
    def number_greater_than(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberGreaterThan"]]]:
        '''number_greater_than block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_greater_than EventgridEventSubscription#number_greater_than}
        '''
        result = self._values.get("number_greater_than")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberGreaterThan"]]], result)

    @builtins.property
    def number_greater_than_or_equals(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals"]]]:
        '''number_greater_than_or_equals block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_greater_than_or_equals EventgridEventSubscription#number_greater_than_or_equals}
        '''
        result = self._values.get("number_greater_than_or_equals")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals"]]], result)

    @builtins.property
    def number_in(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberIn"]]]:
        '''number_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_in EventgridEventSubscription#number_in}
        '''
        result = self._values.get("number_in")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberIn"]]], result)

    @builtins.property
    def number_in_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberInRange"]]]:
        '''number_in_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_in_range EventgridEventSubscription#number_in_range}
        '''
        result = self._values.get("number_in_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberInRange"]]], result)

    @builtins.property
    def number_less_than(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberLessThan"]]]:
        '''number_less_than block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_less_than EventgridEventSubscription#number_less_than}
        '''
        result = self._values.get("number_less_than")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberLessThan"]]], result)

    @builtins.property
    def number_less_than_or_equals(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals"]]]:
        '''number_less_than_or_equals block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_less_than_or_equals EventgridEventSubscription#number_less_than_or_equals}
        '''
        result = self._values.get("number_less_than_or_equals")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals"]]], result)

    @builtins.property
    def number_not_in(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberNotIn"]]]:
        '''number_not_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_not_in EventgridEventSubscription#number_not_in}
        '''
        result = self._values.get("number_not_in")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberNotIn"]]], result)

    @builtins.property
    def number_not_in_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberNotInRange"]]]:
        '''number_not_in_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#number_not_in_range EventgridEventSubscription#number_not_in_range}
        '''
        result = self._values.get("number_not_in_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterNumberNotInRange"]]], result)

    @builtins.property
    def string_begins_with(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringBeginsWith"]]]:
        '''string_begins_with block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_begins_with EventgridEventSubscription#string_begins_with}
        '''
        result = self._values.get("string_begins_with")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringBeginsWith"]]], result)

    @builtins.property
    def string_contains(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringContains"]]]:
        '''string_contains block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_contains EventgridEventSubscription#string_contains}
        '''
        result = self._values.get("string_contains")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringContains"]]], result)

    @builtins.property
    def string_ends_with(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringEndsWith"]]]:
        '''string_ends_with block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_ends_with EventgridEventSubscription#string_ends_with}
        '''
        result = self._values.get("string_ends_with")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringEndsWith"]]], result)

    @builtins.property
    def string_in(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringIn"]]]:
        '''string_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_in EventgridEventSubscription#string_in}
        '''
        result = self._values.get("string_in")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringIn"]]], result)

    @builtins.property
    def string_not_begins_with(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith"]]]:
        '''string_not_begins_with block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_begins_with EventgridEventSubscription#string_not_begins_with}
        '''
        result = self._values.get("string_not_begins_with")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith"]]], result)

    @builtins.property
    def string_not_contains(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotContains"]]]:
        '''string_not_contains block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_contains EventgridEventSubscription#string_not_contains}
        '''
        result = self._values.get("string_not_contains")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotContains"]]], result)

    @builtins.property
    def string_not_ends_with(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotEndsWith"]]]:
        '''string_not_ends_with block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_ends_with EventgridEventSubscription#string_not_ends_with}
        '''
        result = self._values.get("string_not_ends_with")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotEndsWith"]]], result)

    @builtins.property
    def string_not_in(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotIn"]]]:
        '''string_not_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#string_not_in EventgridEventSubscription#string_not_in}
        '''
        result = self._values.get("string_not_in")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotIn"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterBoolEquals",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridEventSubscriptionAdvancedFilterBoolEquals:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterBoolEquals.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterBoolEquals(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterBoolEqualsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterBoolEqualsList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterBoolEqualsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterBoolEqualsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterBoolEqualsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterBoolEqualsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterBoolEqualsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterBoolEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterBoolEquals]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterBoolEquals]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterBoolEqualsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterBoolEquals, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterBoolEquals, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterBoolEquals, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterIsNotNull",
    jsii_struct_bases=[],
    name_mapping={"key": "key"},
)
class EventgridEventSubscriptionAdvancedFilterIsNotNull:
    def __init__(self, *, key: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterIsNotNull.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterIsNotNull(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterIsNotNullList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterIsNotNullList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterIsNotNullList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterIsNotNullOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterIsNotNullList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterIsNotNullOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNotNullList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNotNullList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNotNullList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNotNull]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNotNull]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNotNull]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNotNullList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterIsNotNullOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterIsNotNullOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterIsNotNullOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNotNullOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterIsNotNull, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterIsNotNull, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterIsNotNull, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNotNullOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined",
    jsii_struct_bases=[],
    name_mapping={"key": "key"},
)
class EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined:
    def __init__(self, *, key: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberGreaterThan",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridEventSubscriptionAdvancedFilterNumberGreaterThan:
    def __init__(self, *, key: builtins.str, value: jsii.Number) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberGreaterThan.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterNumberGreaterThan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals:
    def __init__(self, *, key: builtins.str, value: jsii.Number) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberIn",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterNumberIn:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberIn.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterNumberIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterNumberInList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberInList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberInList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterNumberInOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberInList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterNumberInOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberIn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberIn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterNumberInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberInOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberInOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberIn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberIn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberIn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberInRange",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterNumberInRange:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberInRange.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterNumberInRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterNumberInRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberInRangeList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberInRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberInRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberInRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberInRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberInRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberInRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberInRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberInRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberLessThan",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridEventSubscriptionAdvancedFilterNumberLessThan:
    def __init__(self, *, key: builtins.str, value: jsii.Number) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberLessThan.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterNumberLessThan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterNumberLessThanList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberLessThanList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberLessThanList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberLessThanList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThan]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals:
    def __init__(self, *, key: builtins.str, value: jsii.Number) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberLessThan, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberLessThan, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberLessThan, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberNotIn",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterNumberNotIn:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberNotIn.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterNumberNotIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterNumberNotInList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberNotInList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberNotInList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberNotInList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotIn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotIn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberNotIn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberNotIn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberNotIn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberNotInRange",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterNumberNotInRange:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberNotInRange.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterNumberNotInRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotInRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotInRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotInRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberNotInRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberNotInRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberNotInRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBoolEquals")
    def put_bool_equals(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterBoolEquals, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_bool_equals)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBoolEquals", [value]))

    @jsii.member(jsii_name="putIsNotNull")
    def put_is_not_null(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterIsNotNull, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_is_not_null)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIsNotNull", [value]))

    @jsii.member(jsii_name="putIsNullOrUndefined")
    def put_is_null_or_undefined(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_is_null_or_undefined)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIsNullOrUndefined", [value]))

    @jsii.member(jsii_name="putNumberGreaterThan")
    def put_number_greater_than(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_number_greater_than)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberGreaterThan", [value]))

    @jsii.member(jsii_name="putNumberGreaterThanOrEquals")
    def put_number_greater_than_or_equals(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_number_greater_than_or_equals)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberGreaterThanOrEquals", [value]))

    @jsii.member(jsii_name="putNumberIn")
    def put_number_in(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberIn, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_number_in)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberIn", [value]))

    @jsii.member(jsii_name="putNumberInRange")
    def put_number_in_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberInRange, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_number_in_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberInRange", [value]))

    @jsii.member(jsii_name="putNumberLessThan")
    def put_number_less_than(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberLessThan, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_number_less_than)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberLessThan", [value]))

    @jsii.member(jsii_name="putNumberLessThanOrEquals")
    def put_number_less_than_or_equals(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_number_less_than_or_equals)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberLessThanOrEquals", [value]))

    @jsii.member(jsii_name="putNumberNotIn")
    def put_number_not_in(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberNotIn, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_number_not_in)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberNotIn", [value]))

    @jsii.member(jsii_name="putNumberNotInRange")
    def put_number_not_in_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridEventSubscriptionAdvancedFilterNumberNotInRange, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_number_not_in_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberNotInRange", [value]))

    @jsii.member(jsii_name="putStringBeginsWith")
    def put_string_begins_with(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringBeginsWith", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_string_begins_with)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringBeginsWith", [value]))

    @jsii.member(jsii_name="putStringContains")
    def put_string_contains(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringContains", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_string_contains)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringContains", [value]))

    @jsii.member(jsii_name="putStringEndsWith")
    def put_string_ends_with(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringEndsWith", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_string_ends_with)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringEndsWith", [value]))

    @jsii.member(jsii_name="putStringIn")
    def put_string_in(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringIn", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_string_in)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringIn", [value]))

    @jsii.member(jsii_name="putStringNotBeginsWith")
    def put_string_not_begins_with(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_string_not_begins_with)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringNotBeginsWith", [value]))

    @jsii.member(jsii_name="putStringNotContains")
    def put_string_not_contains(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotContains", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_string_not_contains)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringNotContains", [value]))

    @jsii.member(jsii_name="putStringNotEndsWith")
    def put_string_not_ends_with(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotEndsWith", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_string_not_ends_with)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringNotEndsWith", [value]))

    @jsii.member(jsii_name="putStringNotIn")
    def put_string_not_in(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionAdvancedFilterStringNotIn", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterOutputReference.put_string_not_in)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringNotIn", [value]))

    @jsii.member(jsii_name="resetBoolEquals")
    def reset_bool_equals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoolEquals", []))

    @jsii.member(jsii_name="resetIsNotNull")
    def reset_is_not_null(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsNotNull", []))

    @jsii.member(jsii_name="resetIsNullOrUndefined")
    def reset_is_null_or_undefined(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsNullOrUndefined", []))

    @jsii.member(jsii_name="resetNumberGreaterThan")
    def reset_number_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberGreaterThan", []))

    @jsii.member(jsii_name="resetNumberGreaterThanOrEquals")
    def reset_number_greater_than_or_equals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberGreaterThanOrEquals", []))

    @jsii.member(jsii_name="resetNumberIn")
    def reset_number_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberIn", []))

    @jsii.member(jsii_name="resetNumberInRange")
    def reset_number_in_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberInRange", []))

    @jsii.member(jsii_name="resetNumberLessThan")
    def reset_number_less_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberLessThan", []))

    @jsii.member(jsii_name="resetNumberLessThanOrEquals")
    def reset_number_less_than_or_equals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberLessThanOrEquals", []))

    @jsii.member(jsii_name="resetNumberNotIn")
    def reset_number_not_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberNotIn", []))

    @jsii.member(jsii_name="resetNumberNotInRange")
    def reset_number_not_in_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberNotInRange", []))

    @jsii.member(jsii_name="resetStringBeginsWith")
    def reset_string_begins_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringBeginsWith", []))

    @jsii.member(jsii_name="resetStringContains")
    def reset_string_contains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringContains", []))

    @jsii.member(jsii_name="resetStringEndsWith")
    def reset_string_ends_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringEndsWith", []))

    @jsii.member(jsii_name="resetStringIn")
    def reset_string_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringIn", []))

    @jsii.member(jsii_name="resetStringNotBeginsWith")
    def reset_string_not_begins_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringNotBeginsWith", []))

    @jsii.member(jsii_name="resetStringNotContains")
    def reset_string_not_contains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringNotContains", []))

    @jsii.member(jsii_name="resetStringNotEndsWith")
    def reset_string_not_ends_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringNotEndsWith", []))

    @jsii.member(jsii_name="resetStringNotIn")
    def reset_string_not_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringNotIn", []))

    @builtins.property
    @jsii.member(jsii_name="boolEquals")
    def bool_equals(self) -> EventgridEventSubscriptionAdvancedFilterBoolEqualsList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterBoolEqualsList, jsii.get(self, "boolEquals"))

    @builtins.property
    @jsii.member(jsii_name="isNotNull")
    def is_not_null(self) -> EventgridEventSubscriptionAdvancedFilterIsNotNullList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterIsNotNullList, jsii.get(self, "isNotNull"))

    @builtins.property
    @jsii.member(jsii_name="isNullOrUndefined")
    def is_null_or_undefined(
        self,
    ) -> EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList, jsii.get(self, "isNullOrUndefined"))

    @builtins.property
    @jsii.member(jsii_name="numberGreaterThan")
    def number_greater_than(
        self,
    ) -> EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList, jsii.get(self, "numberGreaterThan"))

    @builtins.property
    @jsii.member(jsii_name="numberGreaterThanOrEquals")
    def number_greater_than_or_equals(
        self,
    ) -> EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, jsii.get(self, "numberGreaterThanOrEquals"))

    @builtins.property
    @jsii.member(jsii_name="numberIn")
    def number_in(self) -> EventgridEventSubscriptionAdvancedFilterNumberInList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterNumberInList, jsii.get(self, "numberIn"))

    @builtins.property
    @jsii.member(jsii_name="numberInRange")
    def number_in_range(
        self,
    ) -> EventgridEventSubscriptionAdvancedFilterNumberInRangeList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterNumberInRangeList, jsii.get(self, "numberInRange"))

    @builtins.property
    @jsii.member(jsii_name="numberLessThan")
    def number_less_than(
        self,
    ) -> EventgridEventSubscriptionAdvancedFilterNumberLessThanList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterNumberLessThanList, jsii.get(self, "numberLessThan"))

    @builtins.property
    @jsii.member(jsii_name="numberLessThanOrEquals")
    def number_less_than_or_equals(
        self,
    ) -> EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, jsii.get(self, "numberLessThanOrEquals"))

    @builtins.property
    @jsii.member(jsii_name="numberNotIn")
    def number_not_in(self) -> EventgridEventSubscriptionAdvancedFilterNumberNotInList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterNumberNotInList, jsii.get(self, "numberNotIn"))

    @builtins.property
    @jsii.member(jsii_name="numberNotInRange")
    def number_not_in_range(
        self,
    ) -> EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList:
        return typing.cast(EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList, jsii.get(self, "numberNotInRange"))

    @builtins.property
    @jsii.member(jsii_name="stringBeginsWith")
    def string_begins_with(
        self,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringBeginsWithList":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringBeginsWithList", jsii.get(self, "stringBeginsWith"))

    @builtins.property
    @jsii.member(jsii_name="stringContains")
    def string_contains(
        self,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringContainsList":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringContainsList", jsii.get(self, "stringContains"))

    @builtins.property
    @jsii.member(jsii_name="stringEndsWith")
    def string_ends_with(
        self,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringEndsWithList":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringEndsWithList", jsii.get(self, "stringEndsWith"))

    @builtins.property
    @jsii.member(jsii_name="stringIn")
    def string_in(self) -> "EventgridEventSubscriptionAdvancedFilterStringInList":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringInList", jsii.get(self, "stringIn"))

    @builtins.property
    @jsii.member(jsii_name="stringNotBeginsWith")
    def string_not_begins_with(
        self,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList", jsii.get(self, "stringNotBeginsWith"))

    @builtins.property
    @jsii.member(jsii_name="stringNotContains")
    def string_not_contains(
        self,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringNotContainsList":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringNotContainsList", jsii.get(self, "stringNotContains"))

    @builtins.property
    @jsii.member(jsii_name="stringNotEndsWith")
    def string_not_ends_with(
        self,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList", jsii.get(self, "stringNotEndsWith"))

    @builtins.property
    @jsii.member(jsii_name="stringNotIn")
    def string_not_in(
        self,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringNotInList":
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringNotInList", jsii.get(self, "stringNotIn"))

    @builtins.property
    @jsii.member(jsii_name="boolEqualsInput")
    def bool_equals_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterBoolEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterBoolEquals]]], jsii.get(self, "boolEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="isNotNullInput")
    def is_not_null_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNotNull]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNotNull]]], jsii.get(self, "isNotNullInput"))

    @builtins.property
    @jsii.member(jsii_name="isNullOrUndefinedInput")
    def is_null_or_undefined_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined]]], jsii.get(self, "isNullOrUndefinedInput"))

    @builtins.property
    @jsii.member(jsii_name="numberGreaterThanInput")
    def number_greater_than_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThan]]], jsii.get(self, "numberGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="numberGreaterThanOrEqualsInput")
    def number_greater_than_or_equals_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]], jsii.get(self, "numberGreaterThanOrEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInInput")
    def number_in_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberIn]]], jsii.get(self, "numberInInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInRangeInput")
    def number_in_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberInRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberInRange]]], jsii.get(self, "numberInRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="numberLessThanInput")
    def number_less_than_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThan]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThan]]], jsii.get(self, "numberLessThanInput"))

    @builtins.property
    @jsii.member(jsii_name="numberLessThanOrEqualsInput")
    def number_less_than_or_equals_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]], jsii.get(self, "numberLessThanOrEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="numberNotInInput")
    def number_not_in_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotIn]]], jsii.get(self, "numberNotInInput"))

    @builtins.property
    @jsii.member(jsii_name="numberNotInRangeInput")
    def number_not_in_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotInRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterNumberNotInRange]]], jsii.get(self, "numberNotInRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="stringBeginsWithInput")
    def string_begins_with_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringBeginsWith"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringBeginsWith"]]], jsii.get(self, "stringBeginsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="stringContainsInput")
    def string_contains_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringContains"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringContains"]]], jsii.get(self, "stringContainsInput"))

    @builtins.property
    @jsii.member(jsii_name="stringEndsWithInput")
    def string_ends_with_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringEndsWith"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringEndsWith"]]], jsii.get(self, "stringEndsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="stringInInput")
    def string_in_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringIn"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringIn"]]], jsii.get(self, "stringInInput"))

    @builtins.property
    @jsii.member(jsii_name="stringNotBeginsWithInput")
    def string_not_begins_with_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith"]]], jsii.get(self, "stringNotBeginsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="stringNotContainsInput")
    def string_not_contains_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotContains"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotContains"]]], jsii.get(self, "stringNotContainsInput"))

    @builtins.property
    @jsii.member(jsii_name="stringNotEndsWithInput")
    def string_not_ends_with_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotEndsWith"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotEndsWith"]]], jsii.get(self, "stringNotEndsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="stringNotInInput")
    def string_not_in_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotIn"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionAdvancedFilterStringNotIn"]]], jsii.get(self, "stringNotInInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionAdvancedFilter]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionAdvancedFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionAdvancedFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringBeginsWith",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterStringBeginsWith:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringBeginsWith.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterStringBeginsWith(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterStringBeginsWithList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringBeginsWithList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringBeginsWithList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringBeginsWithList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringBeginsWithList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringBeginsWithList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringBeginsWithList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringBeginsWith]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringBeginsWith]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringBeginsWith]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringBeginsWithList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringBeginsWith, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringBeginsWith, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringBeginsWith, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringContains",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterStringContains:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringContains.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterStringContains(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterStringContainsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringContainsList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringContainsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringContainsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringContainsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringContainsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringContainsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringContains]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringContains]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringContains]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringContainsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringContains, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringContains, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringContains, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringEndsWith",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterStringEndsWith:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringEndsWith.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterStringEndsWith(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterStringEndsWithList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringEndsWithList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringEndsWithList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringEndsWithList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringEndsWithList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringEndsWithList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringEndsWithList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringEndsWith]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringEndsWith]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringEndsWith]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringEndsWithList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringEndsWith, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringEndsWith, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringEndsWith, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringIn",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterStringIn:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringIn.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterStringIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterStringInList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringInList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringInList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringInOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringInList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringInOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringInList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringInList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringInList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringIn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringIn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringInList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterStringInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringInOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringInOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringInOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringInOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringIn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringIn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringIn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotContains",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterStringNotContains:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotContains.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterStringNotContains(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterStringNotContainsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotContainsList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotContainsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotContainsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotContainsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotContainsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotContainsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotContains]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotContains]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotContains]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotContainsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotContains, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotContains, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotContains, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotEndsWith",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterStringNotEndsWith:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotEndsWith.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterStringNotEndsWith(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotEndsWith]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotEndsWith]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotEndsWith]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotEndsWith, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotEndsWith, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotEndsWith, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotIn",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridEventSubscriptionAdvancedFilterStringNotIn:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotIn.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#key EventgridEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#values EventgridEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAdvancedFilterStringNotIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAdvancedFilterStringNotInList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotInList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotInList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotInList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotInList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotInList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotInList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotIn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionAdvancedFilterStringNotIn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotInList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotIn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotIn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilterStringNotIn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAzureFunctionEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "function_id": "functionId",
        "max_events_per_batch": "maxEventsPerBatch",
        "preferred_batch_size_in_kilobytes": "preferredBatchSizeInKilobytes",
    },
)
class EventgridEventSubscriptionAzureFunctionEndpoint:
    def __init__(
        self,
        *,
        function_id: builtins.str,
        max_events_per_batch: typing.Optional[jsii.Number] = None,
        preferred_batch_size_in_kilobytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param function_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#function_id EventgridEventSubscription#function_id}.
        :param max_events_per_batch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_events_per_batch EventgridEventSubscription#max_events_per_batch}.
        :param preferred_batch_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#preferred_batch_size_in_kilobytes EventgridEventSubscription#preferred_batch_size_in_kilobytes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAzureFunctionEndpoint.__init__)
            check_type(argname="argument function_id", value=function_id, expected_type=type_hints["function_id"])
            check_type(argname="argument max_events_per_batch", value=max_events_per_batch, expected_type=type_hints["max_events_per_batch"])
            check_type(argname="argument preferred_batch_size_in_kilobytes", value=preferred_batch_size_in_kilobytes, expected_type=type_hints["preferred_batch_size_in_kilobytes"])
        self._values: typing.Dict[str, typing.Any] = {
            "function_id": function_id,
        }
        if max_events_per_batch is not None:
            self._values["max_events_per_batch"] = max_events_per_batch
        if preferred_batch_size_in_kilobytes is not None:
            self._values["preferred_batch_size_in_kilobytes"] = preferred_batch_size_in_kilobytes

    @builtins.property
    def function_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#function_id EventgridEventSubscription#function_id}.'''
        result = self._values.get("function_id")
        assert result is not None, "Required property 'function_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_events_per_batch(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_events_per_batch EventgridEventSubscription#max_events_per_batch}.'''
        result = self._values.get("max_events_per_batch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_batch_size_in_kilobytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#preferred_batch_size_in_kilobytes EventgridEventSubscription#preferred_batch_size_in_kilobytes}.'''
        result = self._values.get("preferred_batch_size_in_kilobytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionAzureFunctionEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionAzureFunctionEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionAzureFunctionEndpointOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionAzureFunctionEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxEventsPerBatch")
    def reset_max_events_per_batch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxEventsPerBatch", []))

    @jsii.member(jsii_name="resetPreferredBatchSizeInKilobytes")
    def reset_preferred_batch_size_in_kilobytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredBatchSizeInKilobytes", []))

    @builtins.property
    @jsii.member(jsii_name="functionIdInput")
    def function_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="maxEventsPerBatchInput")
    def max_events_per_batch_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxEventsPerBatchInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredBatchSizeInKilobytesInput")
    def preferred_batch_size_in_kilobytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "preferredBatchSizeInKilobytesInput"))

    @builtins.property
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionId"))

    @function_id.setter
    def function_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAzureFunctionEndpointOutputReference, "function_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionId", value)

    @builtins.property
    @jsii.member(jsii_name="maxEventsPerBatch")
    def max_events_per_batch(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxEventsPerBatch"))

    @max_events_per_batch.setter
    def max_events_per_batch(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAzureFunctionEndpointOutputReference, "max_events_per_batch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxEventsPerBatch", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBatchSizeInKilobytes")
    def preferred_batch_size_in_kilobytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "preferredBatchSizeInKilobytes"))

    @preferred_batch_size_in_kilobytes.setter
    def preferred_batch_size_in_kilobytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAzureFunctionEndpointOutputReference, "preferred_batch_size_in_kilobytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBatchSizeInKilobytes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionAzureFunctionEndpoint]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionAzureFunctionEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionAzureFunctionEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionAzureFunctionEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionConfig",
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
        "scope": "scope",
        "advanced_filter": "advancedFilter",
        "advanced_filtering_on_arrays_enabled": "advancedFilteringOnArraysEnabled",
        "azure_function_endpoint": "azureFunctionEndpoint",
        "dead_letter_identity": "deadLetterIdentity",
        "delivery_identity": "deliveryIdentity",
        "delivery_property": "deliveryProperty",
        "event_delivery_schema": "eventDeliverySchema",
        "eventhub_endpoint_id": "eventhubEndpointId",
        "expiration_time_utc": "expirationTimeUtc",
        "hybrid_connection_endpoint_id": "hybridConnectionEndpointId",
        "id": "id",
        "included_event_types": "includedEventTypes",
        "labels": "labels",
        "retry_policy": "retryPolicy",
        "service_bus_queue_endpoint_id": "serviceBusQueueEndpointId",
        "service_bus_topic_endpoint_id": "serviceBusTopicEndpointId",
        "storage_blob_dead_letter_destination": "storageBlobDeadLetterDestination",
        "storage_queue_endpoint": "storageQueueEndpoint",
        "subject_filter": "subjectFilter",
        "timeouts": "timeouts",
        "webhook_endpoint": "webhookEndpoint",
    },
)
class EventgridEventSubscriptionConfig(cdktf.TerraformMetaArguments):
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
        scope: builtins.str,
        advanced_filter: typing.Optional[typing.Union[EventgridEventSubscriptionAdvancedFilter, typing.Dict[str, typing.Any]]] = None,
        advanced_filtering_on_arrays_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        azure_function_endpoint: typing.Optional[typing.Union[EventgridEventSubscriptionAzureFunctionEndpoint, typing.Dict[str, typing.Any]]] = None,
        dead_letter_identity: typing.Optional[typing.Union["EventgridEventSubscriptionDeadLetterIdentity", typing.Dict[str, typing.Any]]] = None,
        delivery_identity: typing.Optional[typing.Union["EventgridEventSubscriptionDeliveryIdentity", typing.Dict[str, typing.Any]]] = None,
        delivery_property: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridEventSubscriptionDeliveryProperty", typing.Dict[str, typing.Any]]]]] = None,
        event_delivery_schema: typing.Optional[builtins.str] = None,
        eventhub_endpoint_id: typing.Optional[builtins.str] = None,
        expiration_time_utc: typing.Optional[builtins.str] = None,
        hybrid_connection_endpoint_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        included_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        retry_policy: typing.Optional[typing.Union["EventgridEventSubscriptionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        service_bus_queue_endpoint_id: typing.Optional[builtins.str] = None,
        service_bus_topic_endpoint_id: typing.Optional[builtins.str] = None,
        storage_blob_dead_letter_destination: typing.Optional[typing.Union["EventgridEventSubscriptionStorageBlobDeadLetterDestination", typing.Dict[str, typing.Any]]] = None,
        storage_queue_endpoint: typing.Optional[typing.Union["EventgridEventSubscriptionStorageQueueEndpoint", typing.Dict[str, typing.Any]]] = None,
        subject_filter: typing.Optional[typing.Union["EventgridEventSubscriptionSubjectFilter", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["EventgridEventSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
        webhook_endpoint: typing.Optional[typing.Union["EventgridEventSubscriptionWebhookEndpoint", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#name EventgridEventSubscription#name}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#scope EventgridEventSubscription#scope}.
        :param advanced_filter: advanced_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#advanced_filter EventgridEventSubscription#advanced_filter}
        :param advanced_filtering_on_arrays_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#advanced_filtering_on_arrays_enabled EventgridEventSubscription#advanced_filtering_on_arrays_enabled}.
        :param azure_function_endpoint: azure_function_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#azure_function_endpoint EventgridEventSubscription#azure_function_endpoint}
        :param dead_letter_identity: dead_letter_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#dead_letter_identity EventgridEventSubscription#dead_letter_identity}
        :param delivery_identity: delivery_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delivery_identity EventgridEventSubscription#delivery_identity}
        :param delivery_property: delivery_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delivery_property EventgridEventSubscription#delivery_property}
        :param event_delivery_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#event_delivery_schema EventgridEventSubscription#event_delivery_schema}.
        :param eventhub_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#eventhub_endpoint_id EventgridEventSubscription#eventhub_endpoint_id}.
        :param expiration_time_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#expiration_time_utc EventgridEventSubscription#expiration_time_utc}.
        :param hybrid_connection_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#hybrid_connection_endpoint_id EventgridEventSubscription#hybrid_connection_endpoint_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#id EventgridEventSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param included_event_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#included_event_types EventgridEventSubscription#included_event_types}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#labels EventgridEventSubscription#labels}.
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#retry_policy EventgridEventSubscription#retry_policy}
        :param service_bus_queue_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#service_bus_queue_endpoint_id EventgridEventSubscription#service_bus_queue_endpoint_id}.
        :param service_bus_topic_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#service_bus_topic_endpoint_id EventgridEventSubscription#service_bus_topic_endpoint_id}.
        :param storage_blob_dead_letter_destination: storage_blob_dead_letter_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_blob_dead_letter_destination EventgridEventSubscription#storage_blob_dead_letter_destination}
        :param storage_queue_endpoint: storage_queue_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_queue_endpoint EventgridEventSubscription#storage_queue_endpoint}
        :param subject_filter: subject_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_filter EventgridEventSubscription#subject_filter}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#timeouts EventgridEventSubscription#timeouts}
        :param webhook_endpoint: webhook_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#webhook_endpoint EventgridEventSubscription#webhook_endpoint}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_filter, dict):
            advanced_filter = EventgridEventSubscriptionAdvancedFilter(**advanced_filter)
        if isinstance(azure_function_endpoint, dict):
            azure_function_endpoint = EventgridEventSubscriptionAzureFunctionEndpoint(**azure_function_endpoint)
        if isinstance(dead_letter_identity, dict):
            dead_letter_identity = EventgridEventSubscriptionDeadLetterIdentity(**dead_letter_identity)
        if isinstance(delivery_identity, dict):
            delivery_identity = EventgridEventSubscriptionDeliveryIdentity(**delivery_identity)
        if isinstance(retry_policy, dict):
            retry_policy = EventgridEventSubscriptionRetryPolicy(**retry_policy)
        if isinstance(storage_blob_dead_letter_destination, dict):
            storage_blob_dead_letter_destination = EventgridEventSubscriptionStorageBlobDeadLetterDestination(**storage_blob_dead_letter_destination)
        if isinstance(storage_queue_endpoint, dict):
            storage_queue_endpoint = EventgridEventSubscriptionStorageQueueEndpoint(**storage_queue_endpoint)
        if isinstance(subject_filter, dict):
            subject_filter = EventgridEventSubscriptionSubjectFilter(**subject_filter)
        if isinstance(timeouts, dict):
            timeouts = EventgridEventSubscriptionTimeouts(**timeouts)
        if isinstance(webhook_endpoint, dict):
            webhook_endpoint = EventgridEventSubscriptionWebhookEndpoint(**webhook_endpoint)
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument advanced_filter", value=advanced_filter, expected_type=type_hints["advanced_filter"])
            check_type(argname="argument advanced_filtering_on_arrays_enabled", value=advanced_filtering_on_arrays_enabled, expected_type=type_hints["advanced_filtering_on_arrays_enabled"])
            check_type(argname="argument azure_function_endpoint", value=azure_function_endpoint, expected_type=type_hints["azure_function_endpoint"])
            check_type(argname="argument dead_letter_identity", value=dead_letter_identity, expected_type=type_hints["dead_letter_identity"])
            check_type(argname="argument delivery_identity", value=delivery_identity, expected_type=type_hints["delivery_identity"])
            check_type(argname="argument delivery_property", value=delivery_property, expected_type=type_hints["delivery_property"])
            check_type(argname="argument event_delivery_schema", value=event_delivery_schema, expected_type=type_hints["event_delivery_schema"])
            check_type(argname="argument eventhub_endpoint_id", value=eventhub_endpoint_id, expected_type=type_hints["eventhub_endpoint_id"])
            check_type(argname="argument expiration_time_utc", value=expiration_time_utc, expected_type=type_hints["expiration_time_utc"])
            check_type(argname="argument hybrid_connection_endpoint_id", value=hybrid_connection_endpoint_id, expected_type=type_hints["hybrid_connection_endpoint_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument included_event_types", value=included_event_types, expected_type=type_hints["included_event_types"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument service_bus_queue_endpoint_id", value=service_bus_queue_endpoint_id, expected_type=type_hints["service_bus_queue_endpoint_id"])
            check_type(argname="argument service_bus_topic_endpoint_id", value=service_bus_topic_endpoint_id, expected_type=type_hints["service_bus_topic_endpoint_id"])
            check_type(argname="argument storage_blob_dead_letter_destination", value=storage_blob_dead_letter_destination, expected_type=type_hints["storage_blob_dead_letter_destination"])
            check_type(argname="argument storage_queue_endpoint", value=storage_queue_endpoint, expected_type=type_hints["storage_queue_endpoint"])
            check_type(argname="argument subject_filter", value=subject_filter, expected_type=type_hints["subject_filter"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument webhook_endpoint", value=webhook_endpoint, expected_type=type_hints["webhook_endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "scope": scope,
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
        if advanced_filter is not None:
            self._values["advanced_filter"] = advanced_filter
        if advanced_filtering_on_arrays_enabled is not None:
            self._values["advanced_filtering_on_arrays_enabled"] = advanced_filtering_on_arrays_enabled
        if azure_function_endpoint is not None:
            self._values["azure_function_endpoint"] = azure_function_endpoint
        if dead_letter_identity is not None:
            self._values["dead_letter_identity"] = dead_letter_identity
        if delivery_identity is not None:
            self._values["delivery_identity"] = delivery_identity
        if delivery_property is not None:
            self._values["delivery_property"] = delivery_property
        if event_delivery_schema is not None:
            self._values["event_delivery_schema"] = event_delivery_schema
        if eventhub_endpoint_id is not None:
            self._values["eventhub_endpoint_id"] = eventhub_endpoint_id
        if expiration_time_utc is not None:
            self._values["expiration_time_utc"] = expiration_time_utc
        if hybrid_connection_endpoint_id is not None:
            self._values["hybrid_connection_endpoint_id"] = hybrid_connection_endpoint_id
        if id is not None:
            self._values["id"] = id
        if included_event_types is not None:
            self._values["included_event_types"] = included_event_types
        if labels is not None:
            self._values["labels"] = labels
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if service_bus_queue_endpoint_id is not None:
            self._values["service_bus_queue_endpoint_id"] = service_bus_queue_endpoint_id
        if service_bus_topic_endpoint_id is not None:
            self._values["service_bus_topic_endpoint_id"] = service_bus_topic_endpoint_id
        if storage_blob_dead_letter_destination is not None:
            self._values["storage_blob_dead_letter_destination"] = storage_blob_dead_letter_destination
        if storage_queue_endpoint is not None:
            self._values["storage_queue_endpoint"] = storage_queue_endpoint
        if subject_filter is not None:
            self._values["subject_filter"] = subject_filter
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if webhook_endpoint is not None:
            self._values["webhook_endpoint"] = webhook_endpoint

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#name EventgridEventSubscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#scope EventgridEventSubscription#scope}.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_filter(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionAdvancedFilter]:
        '''advanced_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#advanced_filter EventgridEventSubscription#advanced_filter}
        '''
        result = self._values.get("advanced_filter")
        return typing.cast(typing.Optional[EventgridEventSubscriptionAdvancedFilter], result)

    @builtins.property
    def advanced_filtering_on_arrays_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#advanced_filtering_on_arrays_enabled EventgridEventSubscription#advanced_filtering_on_arrays_enabled}.'''
        result = self._values.get("advanced_filtering_on_arrays_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def azure_function_endpoint(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionAzureFunctionEndpoint]:
        '''azure_function_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#azure_function_endpoint EventgridEventSubscription#azure_function_endpoint}
        '''
        result = self._values.get("azure_function_endpoint")
        return typing.cast(typing.Optional[EventgridEventSubscriptionAzureFunctionEndpoint], result)

    @builtins.property
    def dead_letter_identity(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionDeadLetterIdentity"]:
        '''dead_letter_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#dead_letter_identity EventgridEventSubscription#dead_letter_identity}
        '''
        result = self._values.get("dead_letter_identity")
        return typing.cast(typing.Optional["EventgridEventSubscriptionDeadLetterIdentity"], result)

    @builtins.property
    def delivery_identity(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionDeliveryIdentity"]:
        '''delivery_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delivery_identity EventgridEventSubscription#delivery_identity}
        '''
        result = self._values.get("delivery_identity")
        return typing.cast(typing.Optional["EventgridEventSubscriptionDeliveryIdentity"], result)

    @builtins.property
    def delivery_property(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionDeliveryProperty"]]]:
        '''delivery_property block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delivery_property EventgridEventSubscription#delivery_property}
        '''
        result = self._values.get("delivery_property")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridEventSubscriptionDeliveryProperty"]]], result)

    @builtins.property
    def event_delivery_schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#event_delivery_schema EventgridEventSubscription#event_delivery_schema}.'''
        result = self._values.get("event_delivery_schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def eventhub_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#eventhub_endpoint_id EventgridEventSubscription#eventhub_endpoint_id}.'''
        result = self._values.get("eventhub_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_time_utc(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#expiration_time_utc EventgridEventSubscription#expiration_time_utc}.'''
        result = self._values.get("expiration_time_utc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hybrid_connection_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#hybrid_connection_endpoint_id EventgridEventSubscription#hybrid_connection_endpoint_id}.'''
        result = self._values.get("hybrid_connection_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#id EventgridEventSubscription#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def included_event_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#included_event_types EventgridEventSubscription#included_event_types}.'''
        result = self._values.get("included_event_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#labels EventgridEventSubscription#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def retry_policy(self) -> typing.Optional["EventgridEventSubscriptionRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#retry_policy EventgridEventSubscription#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["EventgridEventSubscriptionRetryPolicy"], result)

    @builtins.property
    def service_bus_queue_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#service_bus_queue_endpoint_id EventgridEventSubscription#service_bus_queue_endpoint_id}.'''
        result = self._values.get("service_bus_queue_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_bus_topic_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#service_bus_topic_endpoint_id EventgridEventSubscription#service_bus_topic_endpoint_id}.'''
        result = self._values.get("service_bus_topic_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_blob_dead_letter_destination(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionStorageBlobDeadLetterDestination"]:
        '''storage_blob_dead_letter_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_blob_dead_letter_destination EventgridEventSubscription#storage_blob_dead_letter_destination}
        '''
        result = self._values.get("storage_blob_dead_letter_destination")
        return typing.cast(typing.Optional["EventgridEventSubscriptionStorageBlobDeadLetterDestination"], result)

    @builtins.property
    def storage_queue_endpoint(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionStorageQueueEndpoint"]:
        '''storage_queue_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_queue_endpoint EventgridEventSubscription#storage_queue_endpoint}
        '''
        result = self._values.get("storage_queue_endpoint")
        return typing.cast(typing.Optional["EventgridEventSubscriptionStorageQueueEndpoint"], result)

    @builtins.property
    def subject_filter(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionSubjectFilter"]:
        '''subject_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_filter EventgridEventSubscription#subject_filter}
        '''
        result = self._values.get("subject_filter")
        return typing.cast(typing.Optional["EventgridEventSubscriptionSubjectFilter"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EventgridEventSubscriptionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#timeouts EventgridEventSubscription#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EventgridEventSubscriptionTimeouts"], result)

    @builtins.property
    def webhook_endpoint(
        self,
    ) -> typing.Optional["EventgridEventSubscriptionWebhookEndpoint"]:
        '''webhook_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#webhook_endpoint EventgridEventSubscription#webhook_endpoint}
        '''
        result = self._values.get("webhook_endpoint")
        return typing.cast(typing.Optional["EventgridEventSubscriptionWebhookEndpoint"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionDeadLetterIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "user_assigned_identity": "userAssignedIdentity"},
)
class EventgridEventSubscriptionDeadLetterIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        user_assigned_identity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#type EventgridEventSubscription#type}.
        :param user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#user_assigned_identity EventgridEventSubscription#user_assigned_identity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionDeadLetterIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user_assigned_identity", value=user_assigned_identity, expected_type=type_hints["user_assigned_identity"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if user_assigned_identity is not None:
            self._values["user_assigned_identity"] = user_assigned_identity

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#type EventgridEventSubscription#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_assigned_identity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#user_assigned_identity EventgridEventSubscription#user_assigned_identity}.'''
        result = self._values.get("user_assigned_identity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionDeadLetterIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionDeadLetterIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionDeadLetterIdentityOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionDeadLetterIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUserAssignedIdentity")
    def reset_user_assigned_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAssignedIdentity", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityInput")
    def user_assigned_identity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAssignedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeadLetterIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentity")
    def user_assigned_identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentity"))

    @user_assigned_identity.setter
    def user_assigned_identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeadLetterIdentityOutputReference, "user_assigned_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionDeadLetterIdentity]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionDeadLetterIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionDeadLetterIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeadLetterIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionDeliveryIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "user_assigned_identity": "userAssignedIdentity"},
)
class EventgridEventSubscriptionDeliveryIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        user_assigned_identity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#type EventgridEventSubscription#type}.
        :param user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#user_assigned_identity EventgridEventSubscription#user_assigned_identity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionDeliveryIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user_assigned_identity", value=user_assigned_identity, expected_type=type_hints["user_assigned_identity"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if user_assigned_identity is not None:
            self._values["user_assigned_identity"] = user_assigned_identity

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#type EventgridEventSubscription#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_assigned_identity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#user_assigned_identity EventgridEventSubscription#user_assigned_identity}.'''
        result = self._values.get("user_assigned_identity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionDeliveryIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionDeliveryIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionDeliveryIdentityOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionDeliveryIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUserAssignedIdentity")
    def reset_user_assigned_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAssignedIdentity", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityInput")
    def user_assigned_identity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAssignedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentity")
    def user_assigned_identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentity"))

    @user_assigned_identity.setter
    def user_assigned_identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryIdentityOutputReference, "user_assigned_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionDeliveryIdentity]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionDeliveryIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionDeliveryIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionDeliveryProperty",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "type": "type",
        "secret": "secret",
        "source_field": "sourceField",
        "value": "value",
    },
)
class EventgridEventSubscriptionDeliveryProperty:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        type: builtins.str,
        secret: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_field: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#header_name EventgridEventSubscription#header_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#type EventgridEventSubscription#type}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#secret EventgridEventSubscription#secret}.
        :param source_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#source_field EventgridEventSubscription#source_field}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionDeliveryProperty.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument source_field", value=source_field, expected_type=type_hints["source_field"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "type": type,
        }
        if secret is not None:
            self._values["secret"] = secret
        if source_field is not None:
            self._values["source_field"] = source_field
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#header_name EventgridEventSubscription#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#type EventgridEventSubscription#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#secret EventgridEventSubscription#secret}.'''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#source_field EventgridEventSubscription#source_field}.'''
        result = self._values.get("source_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#value EventgridEventSubscription#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionDeliveryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionDeliveryPropertyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionDeliveryPropertyList",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionDeliveryPropertyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridEventSubscriptionDeliveryPropertyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionDeliveryPropertyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridEventSubscriptionDeliveryPropertyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionDeliveryProperty]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionDeliveryProperty]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridEventSubscriptionDeliveryProperty]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridEventSubscriptionDeliveryPropertyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionDeliveryPropertyOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionDeliveryPropertyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @jsii.member(jsii_name="resetSourceField")
    def reset_source_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceField", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFieldInput")
    def source_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyOutputReference, "secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="sourceField")
    def source_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceField"))

    @source_field.setter
    def source_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyOutputReference, "source_field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceField", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionDeliveryProperty, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionDeliveryProperty, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionDeliveryProperty, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionDeliveryPropertyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "event_time_to_live": "eventTimeToLive",
        "max_delivery_attempts": "maxDeliveryAttempts",
    },
)
class EventgridEventSubscriptionRetryPolicy:
    def __init__(
        self,
        *,
        event_time_to_live: jsii.Number,
        max_delivery_attempts: jsii.Number,
    ) -> None:
        '''
        :param event_time_to_live: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#event_time_to_live EventgridEventSubscription#event_time_to_live}.
        :param max_delivery_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_delivery_attempts EventgridEventSubscription#max_delivery_attempts}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionRetryPolicy.__init__)
            check_type(argname="argument event_time_to_live", value=event_time_to_live, expected_type=type_hints["event_time_to_live"])
            check_type(argname="argument max_delivery_attempts", value=max_delivery_attempts, expected_type=type_hints["max_delivery_attempts"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_time_to_live": event_time_to_live,
            "max_delivery_attempts": max_delivery_attempts,
        }

    @builtins.property
    def event_time_to_live(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#event_time_to_live EventgridEventSubscription#event_time_to_live}.'''
        result = self._values.get("event_time_to_live")
        assert result is not None, "Required property 'event_time_to_live' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_delivery_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_delivery_attempts EventgridEventSubscription#max_delivery_attempts}.'''
        result = self._values.get("max_delivery_attempts")
        assert result is not None, "Required property 'max_delivery_attempts' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionRetryPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionRetryPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="eventTimeToLiveInput")
    def event_time_to_live_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "eventTimeToLiveInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDeliveryAttemptsInput")
    def max_delivery_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDeliveryAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="eventTimeToLive")
    def event_time_to_live(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "eventTimeToLive"))

    @event_time_to_live.setter
    def event_time_to_live(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionRetryPolicyOutputReference, "event_time_to_live").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTimeToLive", value)

    @builtins.property
    @jsii.member(jsii_name="maxDeliveryAttempts")
    def max_delivery_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDeliveryAttempts"))

    @max_delivery_attempts.setter
    def max_delivery_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionRetryPolicyOutputReference, "max_delivery_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDeliveryAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EventgridEventSubscriptionRetryPolicy]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionRetryPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionStorageBlobDeadLetterDestination",
    jsii_struct_bases=[],
    name_mapping={
        "storage_account_id": "storageAccountId",
        "storage_blob_container_name": "storageBlobContainerName",
    },
)
class EventgridEventSubscriptionStorageBlobDeadLetterDestination:
    def __init__(
        self,
        *,
        storage_account_id: builtins.str,
        storage_blob_container_name: builtins.str,
    ) -> None:
        '''
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_account_id EventgridEventSubscription#storage_account_id}.
        :param storage_blob_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_blob_container_name EventgridEventSubscription#storage_blob_container_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionStorageBlobDeadLetterDestination.__init__)
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument storage_blob_container_name", value=storage_blob_container_name, expected_type=type_hints["storage_blob_container_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage_account_id": storage_account_id,
            "storage_blob_container_name": storage_blob_container_name,
        }

    @builtins.property
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_account_id EventgridEventSubscription#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_blob_container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_blob_container_name EventgridEventSubscription#storage_blob_container_name}.'''
        result = self._values.get("storage_blob_container_name")
        assert result is not None, "Required property 'storage_blob_container_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionStorageBlobDeadLetterDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageBlobContainerNameInput")
    def storage_blob_container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageBlobContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="storageBlobContainerName")
    def storage_blob_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageBlobContainerName"))

    @storage_blob_container_name.setter
    def storage_blob_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference, "storage_blob_container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageBlobContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionStorageBlobDeadLetterDestination]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionStorageBlobDeadLetterDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionStorageBlobDeadLetterDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionStorageQueueEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "queue_name": "queueName",
        "storage_account_id": "storageAccountId",
        "queue_message_time_to_live_in_seconds": "queueMessageTimeToLiveInSeconds",
    },
)
class EventgridEventSubscriptionStorageQueueEndpoint:
    def __init__(
        self,
        *,
        queue_name: builtins.str,
        storage_account_id: builtins.str,
        queue_message_time_to_live_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param queue_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#queue_name EventgridEventSubscription#queue_name}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_account_id EventgridEventSubscription#storage_account_id}.
        :param queue_message_time_to_live_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#queue_message_time_to_live_in_seconds EventgridEventSubscription#queue_message_time_to_live_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionStorageQueueEndpoint.__init__)
            check_type(argname="argument queue_name", value=queue_name, expected_type=type_hints["queue_name"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument queue_message_time_to_live_in_seconds", value=queue_message_time_to_live_in_seconds, expected_type=type_hints["queue_message_time_to_live_in_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "queue_name": queue_name,
            "storage_account_id": storage_account_id,
        }
        if queue_message_time_to_live_in_seconds is not None:
            self._values["queue_message_time_to_live_in_seconds"] = queue_message_time_to_live_in_seconds

    @builtins.property
    def queue_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#queue_name EventgridEventSubscription#queue_name}.'''
        result = self._values.get("queue_name")
        assert result is not None, "Required property 'queue_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#storage_account_id EventgridEventSubscription#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_message_time_to_live_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#queue_message_time_to_live_in_seconds EventgridEventSubscription#queue_message_time_to_live_in_seconds}.'''
        result = self._values.get("queue_message_time_to_live_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionStorageQueueEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionStorageQueueEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionStorageQueueEndpointOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionStorageQueueEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetQueueMessageTimeToLiveInSeconds")
    def reset_queue_message_time_to_live_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueueMessageTimeToLiveInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="queueMessageTimeToLiveInSecondsInput")
    def queue_message_time_to_live_in_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queueMessageTimeToLiveInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="queueNameInput")
    def queue_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queueNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queueMessageTimeToLiveInSeconds")
    def queue_message_time_to_live_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queueMessageTimeToLiveInSeconds"))

    @queue_message_time_to_live_in_seconds.setter
    def queue_message_time_to_live_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionStorageQueueEndpointOutputReference, "queue_message_time_to_live_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueMessageTimeToLiveInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="queueName")
    def queue_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueName"))

    @queue_name.setter
    def queue_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionStorageQueueEndpointOutputReference, "queue_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionStorageQueueEndpointOutputReference, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionStorageQueueEndpoint]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionStorageQueueEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionStorageQueueEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionStorageQueueEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionSubjectFilter",
    jsii_struct_bases=[],
    name_mapping={
        "case_sensitive": "caseSensitive",
        "subject_begins_with": "subjectBeginsWith",
        "subject_ends_with": "subjectEndsWith",
    },
)
class EventgridEventSubscriptionSubjectFilter:
    def __init__(
        self,
        *,
        case_sensitive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subject_begins_with: typing.Optional[builtins.str] = None,
        subject_ends_with: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param case_sensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#case_sensitive EventgridEventSubscription#case_sensitive}.
        :param subject_begins_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_begins_with EventgridEventSubscription#subject_begins_with}.
        :param subject_ends_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_ends_with EventgridEventSubscription#subject_ends_with}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionSubjectFilter.__init__)
            check_type(argname="argument case_sensitive", value=case_sensitive, expected_type=type_hints["case_sensitive"])
            check_type(argname="argument subject_begins_with", value=subject_begins_with, expected_type=type_hints["subject_begins_with"])
            check_type(argname="argument subject_ends_with", value=subject_ends_with, expected_type=type_hints["subject_ends_with"])
        self._values: typing.Dict[str, typing.Any] = {}
        if case_sensitive is not None:
            self._values["case_sensitive"] = case_sensitive
        if subject_begins_with is not None:
            self._values["subject_begins_with"] = subject_begins_with
        if subject_ends_with is not None:
            self._values["subject_ends_with"] = subject_ends_with

    @builtins.property
    def case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#case_sensitive EventgridEventSubscription#case_sensitive}.'''
        result = self._values.get("case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subject_begins_with(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_begins_with EventgridEventSubscription#subject_begins_with}.'''
        result = self._values.get("subject_begins_with")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_ends_with(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#subject_ends_with EventgridEventSubscription#subject_ends_with}.'''
        result = self._values.get("subject_ends_with")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionSubjectFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionSubjectFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionSubjectFilterOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionSubjectFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaseSensitive")
    def reset_case_sensitive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaseSensitive", []))

    @jsii.member(jsii_name="resetSubjectBeginsWith")
    def reset_subject_begins_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectBeginsWith", []))

    @jsii.member(jsii_name="resetSubjectEndsWith")
    def reset_subject_ends_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectEndsWith", []))

    @builtins.property
    @jsii.member(jsii_name="caseSensitiveInput")
    def case_sensitive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "caseSensitiveInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectBeginsWithInput")
    def subject_begins_with_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectBeginsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectEndsWithInput")
    def subject_ends_with_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectEndsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="caseSensitive")
    def case_sensitive(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "caseSensitive"))

    @case_sensitive.setter
    def case_sensitive(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionSubjectFilterOutputReference, "case_sensitive").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="subjectBeginsWith")
    def subject_begins_with(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectBeginsWith"))

    @subject_begins_with.setter
    def subject_begins_with(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionSubjectFilterOutputReference, "subject_begins_with").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectBeginsWith", value)

    @builtins.property
    @jsii.member(jsii_name="subjectEndsWith")
    def subject_ends_with(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectEndsWith"))

    @subject_ends_with.setter
    def subject_ends_with(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionSubjectFilterOutputReference, "subject_ends_with").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectEndsWith", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionSubjectFilter]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionSubjectFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionSubjectFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionSubjectFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class EventgridEventSubscriptionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#create EventgridEventSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delete EventgridEventSubscription#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#read EventgridEventSubscription#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#update EventgridEventSubscription#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#create EventgridEventSubscription#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#delete EventgridEventSubscription#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#read EventgridEventSubscription#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#update EventgridEventSubscription#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridEventSubscriptionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridEventSubscriptionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridEventSubscriptionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionWebhookEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "active_directory_app_id_or_uri": "activeDirectoryAppIdOrUri",
        "active_directory_tenant_id": "activeDirectoryTenantId",
        "max_events_per_batch": "maxEventsPerBatch",
        "preferred_batch_size_in_kilobytes": "preferredBatchSizeInKilobytes",
    },
)
class EventgridEventSubscriptionWebhookEndpoint:
    def __init__(
        self,
        *,
        url: builtins.str,
        active_directory_app_id_or_uri: typing.Optional[builtins.str] = None,
        active_directory_tenant_id: typing.Optional[builtins.str] = None,
        max_events_per_batch: typing.Optional[jsii.Number] = None,
        preferred_batch_size_in_kilobytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#url EventgridEventSubscription#url}.
        :param active_directory_app_id_or_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#active_directory_app_id_or_uri EventgridEventSubscription#active_directory_app_id_or_uri}.
        :param active_directory_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#active_directory_tenant_id EventgridEventSubscription#active_directory_tenant_id}.
        :param max_events_per_batch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_events_per_batch EventgridEventSubscription#max_events_per_batch}.
        :param preferred_batch_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#preferred_batch_size_in_kilobytes EventgridEventSubscription#preferred_batch_size_in_kilobytes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridEventSubscriptionWebhookEndpoint.__init__)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument active_directory_app_id_or_uri", value=active_directory_app_id_or_uri, expected_type=type_hints["active_directory_app_id_or_uri"])
            check_type(argname="argument active_directory_tenant_id", value=active_directory_tenant_id, expected_type=type_hints["active_directory_tenant_id"])
            check_type(argname="argument max_events_per_batch", value=max_events_per_batch, expected_type=type_hints["max_events_per_batch"])
            check_type(argname="argument preferred_batch_size_in_kilobytes", value=preferred_batch_size_in_kilobytes, expected_type=type_hints["preferred_batch_size_in_kilobytes"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if active_directory_app_id_or_uri is not None:
            self._values["active_directory_app_id_or_uri"] = active_directory_app_id_or_uri
        if active_directory_tenant_id is not None:
            self._values["active_directory_tenant_id"] = active_directory_tenant_id
        if max_events_per_batch is not None:
            self._values["max_events_per_batch"] = max_events_per_batch
        if preferred_batch_size_in_kilobytes is not None:
            self._values["preferred_batch_size_in_kilobytes"] = preferred_batch_size_in_kilobytes

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#url EventgridEventSubscription#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_directory_app_id_or_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#active_directory_app_id_or_uri EventgridEventSubscription#active_directory_app_id_or_uri}.'''
        result = self._values.get("active_directory_app_id_or_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def active_directory_tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#active_directory_tenant_id EventgridEventSubscription#active_directory_tenant_id}.'''
        result = self._values.get("active_directory_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_events_per_batch(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#max_events_per_batch EventgridEventSubscription#max_events_per_batch}.'''
        result = self._values.get("max_events_per_batch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_batch_size_in_kilobytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_event_subscription#preferred_batch_size_in_kilobytes EventgridEventSubscription#preferred_batch_size_in_kilobytes}.'''
        result = self._values.get("preferred_batch_size_in_kilobytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridEventSubscriptionWebhookEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridEventSubscriptionWebhookEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridEventSubscription.EventgridEventSubscriptionWebhookEndpointOutputReference",
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
            type_hints = typing.get_type_hints(EventgridEventSubscriptionWebhookEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetActiveDirectoryAppIdOrUri")
    def reset_active_directory_app_id_or_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectoryAppIdOrUri", []))

    @jsii.member(jsii_name="resetActiveDirectoryTenantId")
    def reset_active_directory_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectoryTenantId", []))

    @jsii.member(jsii_name="resetMaxEventsPerBatch")
    def reset_max_events_per_batch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxEventsPerBatch", []))

    @jsii.member(jsii_name="resetPreferredBatchSizeInKilobytes")
    def reset_preferred_batch_size_in_kilobytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredBatchSizeInKilobytes", []))

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseUrl"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryAppIdOrUriInput")
    def active_directory_app_id_or_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activeDirectoryAppIdOrUriInput"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryTenantIdInput")
    def active_directory_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activeDirectoryTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="maxEventsPerBatchInput")
    def max_events_per_batch_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxEventsPerBatchInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredBatchSizeInKilobytesInput")
    def preferred_batch_size_in_kilobytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "preferredBatchSizeInKilobytesInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryAppIdOrUri")
    def active_directory_app_id_or_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activeDirectoryAppIdOrUri"))

    @active_directory_app_id_or_uri.setter
    def active_directory_app_id_or_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionWebhookEndpointOutputReference, "active_directory_app_id_or_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeDirectoryAppIdOrUri", value)

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryTenantId")
    def active_directory_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activeDirectoryTenantId"))

    @active_directory_tenant_id.setter
    def active_directory_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionWebhookEndpointOutputReference, "active_directory_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeDirectoryTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="maxEventsPerBatch")
    def max_events_per_batch(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxEventsPerBatch"))

    @max_events_per_batch.setter
    def max_events_per_batch(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionWebhookEndpointOutputReference, "max_events_per_batch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxEventsPerBatch", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBatchSizeInKilobytes")
    def preferred_batch_size_in_kilobytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "preferredBatchSizeInKilobytes"))

    @preferred_batch_size_in_kilobytes.setter
    def preferred_batch_size_in_kilobytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionWebhookEndpointOutputReference, "preferred_batch_size_in_kilobytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBatchSizeInKilobytes", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionWebhookEndpointOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridEventSubscriptionWebhookEndpoint]:
        return typing.cast(typing.Optional[EventgridEventSubscriptionWebhookEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridEventSubscriptionWebhookEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridEventSubscriptionWebhookEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EventgridEventSubscription",
    "EventgridEventSubscriptionAdvancedFilter",
    "EventgridEventSubscriptionAdvancedFilterBoolEquals",
    "EventgridEventSubscriptionAdvancedFilterBoolEqualsList",
    "EventgridEventSubscriptionAdvancedFilterBoolEqualsOutputReference",
    "EventgridEventSubscriptionAdvancedFilterIsNotNull",
    "EventgridEventSubscriptionAdvancedFilterIsNotNullList",
    "EventgridEventSubscriptionAdvancedFilterIsNotNullOutputReference",
    "EventgridEventSubscriptionAdvancedFilterIsNullOrUndefined",
    "EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedList",
    "EventgridEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference",
    "EventgridEventSubscriptionAdvancedFilterNumberGreaterThan",
    "EventgridEventSubscriptionAdvancedFilterNumberGreaterThanList",
    "EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals",
    "EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList",
    "EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference",
    "EventgridEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference",
    "EventgridEventSubscriptionAdvancedFilterNumberIn",
    "EventgridEventSubscriptionAdvancedFilterNumberInList",
    "EventgridEventSubscriptionAdvancedFilterNumberInOutputReference",
    "EventgridEventSubscriptionAdvancedFilterNumberInRange",
    "EventgridEventSubscriptionAdvancedFilterNumberInRangeList",
    "EventgridEventSubscriptionAdvancedFilterNumberInRangeOutputReference",
    "EventgridEventSubscriptionAdvancedFilterNumberLessThan",
    "EventgridEventSubscriptionAdvancedFilterNumberLessThanList",
    "EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEquals",
    "EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList",
    "EventgridEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference",
    "EventgridEventSubscriptionAdvancedFilterNumberLessThanOutputReference",
    "EventgridEventSubscriptionAdvancedFilterNumberNotIn",
    "EventgridEventSubscriptionAdvancedFilterNumberNotInList",
    "EventgridEventSubscriptionAdvancedFilterNumberNotInOutputReference",
    "EventgridEventSubscriptionAdvancedFilterNumberNotInRange",
    "EventgridEventSubscriptionAdvancedFilterNumberNotInRangeList",
    "EventgridEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference",
    "EventgridEventSubscriptionAdvancedFilterOutputReference",
    "EventgridEventSubscriptionAdvancedFilterStringBeginsWith",
    "EventgridEventSubscriptionAdvancedFilterStringBeginsWithList",
    "EventgridEventSubscriptionAdvancedFilterStringBeginsWithOutputReference",
    "EventgridEventSubscriptionAdvancedFilterStringContains",
    "EventgridEventSubscriptionAdvancedFilterStringContainsList",
    "EventgridEventSubscriptionAdvancedFilterStringContainsOutputReference",
    "EventgridEventSubscriptionAdvancedFilterStringEndsWith",
    "EventgridEventSubscriptionAdvancedFilterStringEndsWithList",
    "EventgridEventSubscriptionAdvancedFilterStringEndsWithOutputReference",
    "EventgridEventSubscriptionAdvancedFilterStringIn",
    "EventgridEventSubscriptionAdvancedFilterStringInList",
    "EventgridEventSubscriptionAdvancedFilterStringInOutputReference",
    "EventgridEventSubscriptionAdvancedFilterStringNotBeginsWith",
    "EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithList",
    "EventgridEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference",
    "EventgridEventSubscriptionAdvancedFilterStringNotContains",
    "EventgridEventSubscriptionAdvancedFilterStringNotContainsList",
    "EventgridEventSubscriptionAdvancedFilterStringNotContainsOutputReference",
    "EventgridEventSubscriptionAdvancedFilterStringNotEndsWith",
    "EventgridEventSubscriptionAdvancedFilterStringNotEndsWithList",
    "EventgridEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference",
    "EventgridEventSubscriptionAdvancedFilterStringNotIn",
    "EventgridEventSubscriptionAdvancedFilterStringNotInList",
    "EventgridEventSubscriptionAdvancedFilterStringNotInOutputReference",
    "EventgridEventSubscriptionAzureFunctionEndpoint",
    "EventgridEventSubscriptionAzureFunctionEndpointOutputReference",
    "EventgridEventSubscriptionConfig",
    "EventgridEventSubscriptionDeadLetterIdentity",
    "EventgridEventSubscriptionDeadLetterIdentityOutputReference",
    "EventgridEventSubscriptionDeliveryIdentity",
    "EventgridEventSubscriptionDeliveryIdentityOutputReference",
    "EventgridEventSubscriptionDeliveryProperty",
    "EventgridEventSubscriptionDeliveryPropertyList",
    "EventgridEventSubscriptionDeliveryPropertyOutputReference",
    "EventgridEventSubscriptionRetryPolicy",
    "EventgridEventSubscriptionRetryPolicyOutputReference",
    "EventgridEventSubscriptionStorageBlobDeadLetterDestination",
    "EventgridEventSubscriptionStorageBlobDeadLetterDestinationOutputReference",
    "EventgridEventSubscriptionStorageQueueEndpoint",
    "EventgridEventSubscriptionStorageQueueEndpointOutputReference",
    "EventgridEventSubscriptionSubjectFilter",
    "EventgridEventSubscriptionSubjectFilterOutputReference",
    "EventgridEventSubscriptionTimeouts",
    "EventgridEventSubscriptionTimeoutsOutputReference",
    "EventgridEventSubscriptionWebhookEndpoint",
    "EventgridEventSubscriptionWebhookEndpointOutputReference",
]

publication.publish()
