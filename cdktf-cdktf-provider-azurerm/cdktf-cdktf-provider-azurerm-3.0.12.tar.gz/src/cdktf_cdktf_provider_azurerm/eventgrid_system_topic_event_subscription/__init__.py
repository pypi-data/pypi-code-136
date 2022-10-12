'''
# `azurerm_eventgrid_system_topic_event_subscription`

Refer to the Terraform Registory for docs: [`azurerm_eventgrid_system_topic_event_subscription`](https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription).
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


class EventgridSystemTopicEventSubscription(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription azurerm_eventgrid_system_topic_event_subscription}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
        system_topic: builtins.str,
        advanced_filter: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilter", typing.Dict[str, typing.Any]]] = None,
        advanced_filtering_on_arrays_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        azure_function_endpoint: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint", typing.Dict[str, typing.Any]]] = None,
        dead_letter_identity: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionDeadLetterIdentity", typing.Dict[str, typing.Any]]] = None,
        delivery_identity: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionDeliveryIdentity", typing.Dict[str, typing.Any]]] = None,
        delivery_property: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionDeliveryProperty", typing.Dict[str, typing.Any]]]]] = None,
        event_delivery_schema: typing.Optional[builtins.str] = None,
        eventhub_endpoint_id: typing.Optional[builtins.str] = None,
        expiration_time_utc: typing.Optional[builtins.str] = None,
        hybrid_connection_endpoint_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        included_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        retry_policy: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        service_bus_queue_endpoint_id: typing.Optional[builtins.str] = None,
        service_bus_topic_endpoint_id: typing.Optional[builtins.str] = None,
        storage_blob_dead_letter_destination: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination", typing.Dict[str, typing.Any]]] = None,
        storage_queue_endpoint: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionStorageQueueEndpoint", typing.Dict[str, typing.Any]]] = None,
        subject_filter: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionSubjectFilter", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
        webhook_endpoint: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionWebhookEndpoint", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription azurerm_eventgrid_system_topic_event_subscription} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#name EventgridSystemTopicEventSubscription#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#resource_group_name EventgridSystemTopicEventSubscription#resource_group_name}.
        :param system_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#system_topic EventgridSystemTopicEventSubscription#system_topic}.
        :param advanced_filter: advanced_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#advanced_filter EventgridSystemTopicEventSubscription#advanced_filter}
        :param advanced_filtering_on_arrays_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#advanced_filtering_on_arrays_enabled EventgridSystemTopicEventSubscription#advanced_filtering_on_arrays_enabled}.
        :param azure_function_endpoint: azure_function_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#azure_function_endpoint EventgridSystemTopicEventSubscription#azure_function_endpoint}
        :param dead_letter_identity: dead_letter_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#dead_letter_identity EventgridSystemTopicEventSubscription#dead_letter_identity}
        :param delivery_identity: delivery_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delivery_identity EventgridSystemTopicEventSubscription#delivery_identity}
        :param delivery_property: delivery_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delivery_property EventgridSystemTopicEventSubscription#delivery_property}
        :param event_delivery_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#event_delivery_schema EventgridSystemTopicEventSubscription#event_delivery_schema}.
        :param eventhub_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#eventhub_endpoint_id EventgridSystemTopicEventSubscription#eventhub_endpoint_id}.
        :param expiration_time_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#expiration_time_utc EventgridSystemTopicEventSubscription#expiration_time_utc}.
        :param hybrid_connection_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#hybrid_connection_endpoint_id EventgridSystemTopicEventSubscription#hybrid_connection_endpoint_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#id EventgridSystemTopicEventSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param included_event_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#included_event_types EventgridSystemTopicEventSubscription#included_event_types}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#labels EventgridSystemTopicEventSubscription#labels}.
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#retry_policy EventgridSystemTopicEventSubscription#retry_policy}
        :param service_bus_queue_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#service_bus_queue_endpoint_id EventgridSystemTopicEventSubscription#service_bus_queue_endpoint_id}.
        :param service_bus_topic_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#service_bus_topic_endpoint_id EventgridSystemTopicEventSubscription#service_bus_topic_endpoint_id}.
        :param storage_blob_dead_letter_destination: storage_blob_dead_letter_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_blob_dead_letter_destination EventgridSystemTopicEventSubscription#storage_blob_dead_letter_destination}
        :param storage_queue_endpoint: storage_queue_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_queue_endpoint EventgridSystemTopicEventSubscription#storage_queue_endpoint}
        :param subject_filter: subject_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_filter EventgridSystemTopicEventSubscription#subject_filter}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#timeouts EventgridSystemTopicEventSubscription#timeouts}
        :param webhook_endpoint: webhook_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#webhook_endpoint EventgridSystemTopicEventSubscription#webhook_endpoint}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscription.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EventgridSystemTopicEventSubscriptionConfig(
            name=name,
            resource_group_name=resource_group_name,
            system_topic=system_topic,
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

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdvancedFilter")
    def put_advanced_filter(
        self,
        *,
        bool_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals", typing.Dict[str, typing.Any]]]]] = None,
        is_not_null: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull", typing.Dict[str, typing.Any]]]]] = None,
        is_null_or_undefined: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined", typing.Dict[str, typing.Any]]]]] = None,
        number_greater_than: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan", typing.Dict[str, typing.Any]]]]] = None,
        number_greater_than_or_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals", typing.Dict[str, typing.Any]]]]] = None,
        number_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn", typing.Dict[str, typing.Any]]]]] = None,
        number_in_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange", typing.Dict[str, typing.Any]]]]] = None,
        number_less_than: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan", typing.Dict[str, typing.Any]]]]] = None,
        number_less_than_or_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals", typing.Dict[str, typing.Any]]]]] = None,
        number_not_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn", typing.Dict[str, typing.Any]]]]] = None,
        number_not_in_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange", typing.Dict[str, typing.Any]]]]] = None,
        string_begins_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_contains: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains", typing.Dict[str, typing.Any]]]]] = None,
        string_ends_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn", typing.Dict[str, typing.Any]]]]] = None,
        string_not_begins_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_not_contains: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains", typing.Dict[str, typing.Any]]]]] = None,
        string_not_ends_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_not_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param bool_equals: bool_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#bool_equals EventgridSystemTopicEventSubscription#bool_equals}
        :param is_not_null: is_not_null block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#is_not_null EventgridSystemTopicEventSubscription#is_not_null}
        :param is_null_or_undefined: is_null_or_undefined block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#is_null_or_undefined EventgridSystemTopicEventSubscription#is_null_or_undefined}
        :param number_greater_than: number_greater_than block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_greater_than EventgridSystemTopicEventSubscription#number_greater_than}
        :param number_greater_than_or_equals: number_greater_than_or_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_greater_than_or_equals EventgridSystemTopicEventSubscription#number_greater_than_or_equals}
        :param number_in: number_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_in EventgridSystemTopicEventSubscription#number_in}
        :param number_in_range: number_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_in_range EventgridSystemTopicEventSubscription#number_in_range}
        :param number_less_than: number_less_than block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_less_than EventgridSystemTopicEventSubscription#number_less_than}
        :param number_less_than_or_equals: number_less_than_or_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_less_than_or_equals EventgridSystemTopicEventSubscription#number_less_than_or_equals}
        :param number_not_in: number_not_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_not_in EventgridSystemTopicEventSubscription#number_not_in}
        :param number_not_in_range: number_not_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_not_in_range EventgridSystemTopicEventSubscription#number_not_in_range}
        :param string_begins_with: string_begins_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_begins_with EventgridSystemTopicEventSubscription#string_begins_with}
        :param string_contains: string_contains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_contains EventgridSystemTopicEventSubscription#string_contains}
        :param string_ends_with: string_ends_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_ends_with EventgridSystemTopicEventSubscription#string_ends_with}
        :param string_in: string_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_in EventgridSystemTopicEventSubscription#string_in}
        :param string_not_begins_with: string_not_begins_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_begins_with EventgridSystemTopicEventSubscription#string_not_begins_with}
        :param string_not_contains: string_not_contains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_contains EventgridSystemTopicEventSubscription#string_not_contains}
        :param string_not_ends_with: string_not_ends_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_ends_with EventgridSystemTopicEventSubscription#string_not_ends_with}
        :param string_not_in: string_not_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_in EventgridSystemTopicEventSubscription#string_not_in}
        '''
        value = EventgridSystemTopicEventSubscriptionAdvancedFilter(
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
        :param function_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#function_id EventgridSystemTopicEventSubscription#function_id}.
        :param max_events_per_batch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_events_per_batch EventgridSystemTopicEventSubscription#max_events_per_batch}.
        :param preferred_batch_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#preferred_batch_size_in_kilobytes EventgridSystemTopicEventSubscription#preferred_batch_size_in_kilobytes}.
        '''
        value = EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint(
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
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#type EventgridSystemTopicEventSubscription#type}.
        :param user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#user_assigned_identity EventgridSystemTopicEventSubscription#user_assigned_identity}.
        '''
        value = EventgridSystemTopicEventSubscriptionDeadLetterIdentity(
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
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#type EventgridSystemTopicEventSubscription#type}.
        :param user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#user_assigned_identity EventgridSystemTopicEventSubscription#user_assigned_identity}.
        '''
        value = EventgridSystemTopicEventSubscriptionDeliveryIdentity(
            type=type, user_assigned_identity=user_assigned_identity
        )

        return typing.cast(None, jsii.invoke(self, "putDeliveryIdentity", [value]))

    @jsii.member(jsii_name="putDeliveryProperty")
    def put_delivery_property(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionDeliveryProperty", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscription.put_delivery_property)
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
        :param event_time_to_live: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#event_time_to_live EventgridSystemTopicEventSubscription#event_time_to_live}.
        :param max_delivery_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_delivery_attempts EventgridSystemTopicEventSubscription#max_delivery_attempts}.
        '''
        value = EventgridSystemTopicEventSubscriptionRetryPolicy(
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
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_account_id EventgridSystemTopicEventSubscription#storage_account_id}.
        :param storage_blob_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_blob_container_name EventgridSystemTopicEventSubscription#storage_blob_container_name}.
        '''
        value = EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination(
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
        :param queue_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#queue_name EventgridSystemTopicEventSubscription#queue_name}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_account_id EventgridSystemTopicEventSubscription#storage_account_id}.
        :param queue_message_time_to_live_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#queue_message_time_to_live_in_seconds EventgridSystemTopicEventSubscription#queue_message_time_to_live_in_seconds}.
        '''
        value = EventgridSystemTopicEventSubscriptionStorageQueueEndpoint(
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
        :param case_sensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#case_sensitive EventgridSystemTopicEventSubscription#case_sensitive}.
        :param subject_begins_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_begins_with EventgridSystemTopicEventSubscription#subject_begins_with}.
        :param subject_ends_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_ends_with EventgridSystemTopicEventSubscription#subject_ends_with}.
        '''
        value = EventgridSystemTopicEventSubscriptionSubjectFilter(
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#create EventgridSystemTopicEventSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delete EventgridSystemTopicEventSubscription#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#read EventgridSystemTopicEventSubscription#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#update EventgridSystemTopicEventSubscription#update}.
        '''
        value = EventgridSystemTopicEventSubscriptionTimeouts(
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
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#url EventgridSystemTopicEventSubscription#url}.
        :param active_directory_app_id_or_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#active_directory_app_id_or_uri EventgridSystemTopicEventSubscription#active_directory_app_id_or_uri}.
        :param active_directory_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#active_directory_tenant_id EventgridSystemTopicEventSubscription#active_directory_tenant_id}.
        :param max_events_per_batch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_events_per_batch EventgridSystemTopicEventSubscription#max_events_per_batch}.
        :param preferred_batch_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#preferred_batch_size_in_kilobytes EventgridSystemTopicEventSubscription#preferred_batch_size_in_kilobytes}.
        '''
        value = EventgridSystemTopicEventSubscriptionWebhookEndpoint(
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
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference", jsii.get(self, "advancedFilter"))

    @builtins.property
    @jsii.member(jsii_name="azureFunctionEndpoint")
    def azure_function_endpoint(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference", jsii.get(self, "azureFunctionEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterIdentity")
    def dead_letter_identity(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference", jsii.get(self, "deadLetterIdentity"))

    @builtins.property
    @jsii.member(jsii_name="deliveryIdentity")
    def delivery_identity(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference", jsii.get(self, "deliveryIdentity"))

    @builtins.property
    @jsii.member(jsii_name="deliveryProperty")
    def delivery_property(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionDeliveryPropertyList":
        return typing.cast("EventgridSystemTopicEventSubscriptionDeliveryPropertyList", jsii.get(self, "deliveryProperty"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="storageBlobDeadLetterDestination")
    def storage_blob_dead_letter_destination(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference", jsii.get(self, "storageBlobDeadLetterDestination"))

    @builtins.property
    @jsii.member(jsii_name="storageQueueEndpoint")
    def storage_queue_endpoint(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference", jsii.get(self, "storageQueueEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="subjectFilter")
    def subject_filter(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference", jsii.get(self, "subjectFilter"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionTimeoutsOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="webhookEndpoint")
    def webhook_endpoint(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference":
        return typing.cast("EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference", jsii.get(self, "webhookEndpoint"))

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
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionAdvancedFilter"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionAdvancedFilter"], jsii.get(self, "advancedFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFunctionEndpointInput")
    def azure_function_endpoint_input(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint"], jsii.get(self, "azureFunctionEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterIdentityInput")
    def dead_letter_identity_input(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionDeadLetterIdentity"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionDeadLetterIdentity"], jsii.get(self, "deadLetterIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryIdentityInput")
    def delivery_identity_input(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionDeliveryIdentity"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionDeliveryIdentity"], jsii.get(self, "deliveryIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryPropertyInput")
    def delivery_property_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionDeliveryProperty"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionDeliveryProperty"]]], jsii.get(self, "deliveryPropertyInput"))

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
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionRetryPolicy"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionRetryPolicy"], jsii.get(self, "retryPolicyInput"))

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
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination"], jsii.get(self, "storageBlobDeadLetterDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="storageQueueEndpointInput")
    def storage_queue_endpoint_input(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionStorageQueueEndpoint"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionStorageQueueEndpoint"], jsii.get(self, "storageQueueEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectFilterInput")
    def subject_filter_input(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionSubjectFilter"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionSubjectFilter"], jsii.get(self, "subjectFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="systemTopicInput")
    def system_topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "systemTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookEndpointInput")
    def webhook_endpoint_input(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionWebhookEndpoint"]:
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionWebhookEndpoint"], jsii.get(self, "webhookEndpointInput"))

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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "advanced_filtering_on_arrays_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedFilteringOnArraysEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventDeliverySchema")
    def event_delivery_schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventDeliverySchema"))

    @event_delivery_schema.setter
    def event_delivery_schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "event_delivery_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDeliverySchema", value)

    @builtins.property
    @jsii.member(jsii_name="eventhubEndpointId")
    def eventhub_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventhubEndpointId"))

    @eventhub_endpoint_id.setter
    def eventhub_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "eventhub_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventhubEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="expirationTimeUtc")
    def expiration_time_utc(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationTimeUtc"))

    @expiration_time_utc.setter
    def expiration_time_utc(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "expiration_time_utc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTimeUtc", value)

    @builtins.property
    @jsii.member(jsii_name="hybridConnectionEndpointId")
    def hybrid_connection_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hybridConnectionEndpointId"))

    @hybrid_connection_endpoint_id.setter
    def hybrid_connection_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "hybrid_connection_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hybridConnectionEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="includedEventTypes")
    def included_event_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedEventTypes"))

    @included_event_types.setter
    def included_event_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "included_event_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedEventTypes", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceBusQueueEndpointId")
    def service_bus_queue_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceBusQueueEndpointId"))

    @service_bus_queue_endpoint_id.setter
    def service_bus_queue_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "service_bus_queue_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceBusQueueEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceBusTopicEndpointId")
    def service_bus_topic_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceBusTopicEndpointId"))

    @service_bus_topic_endpoint_id.setter
    def service_bus_topic_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "service_bus_topic_endpoint_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceBusTopicEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="systemTopic")
    def system_topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "systemTopic"))

    @system_topic.setter
    def system_topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscription, "system_topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemTopic", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilter",
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
class EventgridSystemTopicEventSubscriptionAdvancedFilter:
    def __init__(
        self,
        *,
        bool_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals", typing.Dict[str, typing.Any]]]]] = None,
        is_not_null: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull", typing.Dict[str, typing.Any]]]]] = None,
        is_null_or_undefined: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined", typing.Dict[str, typing.Any]]]]] = None,
        number_greater_than: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan", typing.Dict[str, typing.Any]]]]] = None,
        number_greater_than_or_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals", typing.Dict[str, typing.Any]]]]] = None,
        number_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn", typing.Dict[str, typing.Any]]]]] = None,
        number_in_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange", typing.Dict[str, typing.Any]]]]] = None,
        number_less_than: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan", typing.Dict[str, typing.Any]]]]] = None,
        number_less_than_or_equals: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals", typing.Dict[str, typing.Any]]]]] = None,
        number_not_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn", typing.Dict[str, typing.Any]]]]] = None,
        number_not_in_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange", typing.Dict[str, typing.Any]]]]] = None,
        string_begins_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_contains: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains", typing.Dict[str, typing.Any]]]]] = None,
        string_ends_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn", typing.Dict[str, typing.Any]]]]] = None,
        string_not_begins_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_not_contains: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains", typing.Dict[str, typing.Any]]]]] = None,
        string_not_ends_with: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith", typing.Dict[str, typing.Any]]]]] = None,
        string_not_in: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param bool_equals: bool_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#bool_equals EventgridSystemTopicEventSubscription#bool_equals}
        :param is_not_null: is_not_null block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#is_not_null EventgridSystemTopicEventSubscription#is_not_null}
        :param is_null_or_undefined: is_null_or_undefined block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#is_null_or_undefined EventgridSystemTopicEventSubscription#is_null_or_undefined}
        :param number_greater_than: number_greater_than block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_greater_than EventgridSystemTopicEventSubscription#number_greater_than}
        :param number_greater_than_or_equals: number_greater_than_or_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_greater_than_or_equals EventgridSystemTopicEventSubscription#number_greater_than_or_equals}
        :param number_in: number_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_in EventgridSystemTopicEventSubscription#number_in}
        :param number_in_range: number_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_in_range EventgridSystemTopicEventSubscription#number_in_range}
        :param number_less_than: number_less_than block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_less_than EventgridSystemTopicEventSubscription#number_less_than}
        :param number_less_than_or_equals: number_less_than_or_equals block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_less_than_or_equals EventgridSystemTopicEventSubscription#number_less_than_or_equals}
        :param number_not_in: number_not_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_not_in EventgridSystemTopicEventSubscription#number_not_in}
        :param number_not_in_range: number_not_in_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_not_in_range EventgridSystemTopicEventSubscription#number_not_in_range}
        :param string_begins_with: string_begins_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_begins_with EventgridSystemTopicEventSubscription#string_begins_with}
        :param string_contains: string_contains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_contains EventgridSystemTopicEventSubscription#string_contains}
        :param string_ends_with: string_ends_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_ends_with EventgridSystemTopicEventSubscription#string_ends_with}
        :param string_in: string_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_in EventgridSystemTopicEventSubscription#string_in}
        :param string_not_begins_with: string_not_begins_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_begins_with EventgridSystemTopicEventSubscription#string_not_begins_with}
        :param string_not_contains: string_not_contains block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_contains EventgridSystemTopicEventSubscription#string_not_contains}
        :param string_not_ends_with: string_not_ends_with block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_ends_with EventgridSystemTopicEventSubscription#string_not_ends_with}
        :param string_not_in: string_not_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_in EventgridSystemTopicEventSubscription#string_not_in}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilter.__init__)
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals"]]]:
        '''bool_equals block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#bool_equals EventgridSystemTopicEventSubscription#bool_equals}
        '''
        result = self._values.get("bool_equals")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals"]]], result)

    @builtins.property
    def is_not_null(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull"]]]:
        '''is_not_null block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#is_not_null EventgridSystemTopicEventSubscription#is_not_null}
        '''
        result = self._values.get("is_not_null")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull"]]], result)

    @builtins.property
    def is_null_or_undefined(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined"]]]:
        '''is_null_or_undefined block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#is_null_or_undefined EventgridSystemTopicEventSubscription#is_null_or_undefined}
        '''
        result = self._values.get("is_null_or_undefined")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined"]]], result)

    @builtins.property
    def number_greater_than(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan"]]]:
        '''number_greater_than block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_greater_than EventgridSystemTopicEventSubscription#number_greater_than}
        '''
        result = self._values.get("number_greater_than")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan"]]], result)

    @builtins.property
    def number_greater_than_or_equals(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals"]]]:
        '''number_greater_than_or_equals block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_greater_than_or_equals EventgridSystemTopicEventSubscription#number_greater_than_or_equals}
        '''
        result = self._values.get("number_greater_than_or_equals")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals"]]], result)

    @builtins.property
    def number_in(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn"]]]:
        '''number_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_in EventgridSystemTopicEventSubscription#number_in}
        '''
        result = self._values.get("number_in")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn"]]], result)

    @builtins.property
    def number_in_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange"]]]:
        '''number_in_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_in_range EventgridSystemTopicEventSubscription#number_in_range}
        '''
        result = self._values.get("number_in_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange"]]], result)

    @builtins.property
    def number_less_than(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan"]]]:
        '''number_less_than block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_less_than EventgridSystemTopicEventSubscription#number_less_than}
        '''
        result = self._values.get("number_less_than")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan"]]], result)

    @builtins.property
    def number_less_than_or_equals(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals"]]]:
        '''number_less_than_or_equals block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_less_than_or_equals EventgridSystemTopicEventSubscription#number_less_than_or_equals}
        '''
        result = self._values.get("number_less_than_or_equals")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals"]]], result)

    @builtins.property
    def number_not_in(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn"]]]:
        '''number_not_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_not_in EventgridSystemTopicEventSubscription#number_not_in}
        '''
        result = self._values.get("number_not_in")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn"]]], result)

    @builtins.property
    def number_not_in_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange"]]]:
        '''number_not_in_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#number_not_in_range EventgridSystemTopicEventSubscription#number_not_in_range}
        '''
        result = self._values.get("number_not_in_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange"]]], result)

    @builtins.property
    def string_begins_with(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith"]]]:
        '''string_begins_with block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_begins_with EventgridSystemTopicEventSubscription#string_begins_with}
        '''
        result = self._values.get("string_begins_with")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith"]]], result)

    @builtins.property
    def string_contains(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains"]]]:
        '''string_contains block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_contains EventgridSystemTopicEventSubscription#string_contains}
        '''
        result = self._values.get("string_contains")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains"]]], result)

    @builtins.property
    def string_ends_with(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith"]]]:
        '''string_ends_with block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_ends_with EventgridSystemTopicEventSubscription#string_ends_with}
        '''
        result = self._values.get("string_ends_with")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith"]]], result)

    @builtins.property
    def string_in(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn"]]]:
        '''string_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_in EventgridSystemTopicEventSubscription#string_in}
        '''
        result = self._values.get("string_in")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn"]]], result)

    @builtins.property
    def string_not_begins_with(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith"]]]:
        '''string_not_begins_with block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_begins_with EventgridSystemTopicEventSubscription#string_not_begins_with}
        '''
        result = self._values.get("string_not_begins_with")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith"]]], result)

    @builtins.property
    def string_not_contains(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains"]]]:
        '''string_not_contains block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_contains EventgridSystemTopicEventSubscription#string_not_contains}
        '''
        result = self._values.get("string_not_contains")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains"]]], result)

    @builtins.property
    def string_not_ends_with(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith"]]]:
        '''string_not_ends_with block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_ends_with EventgridSystemTopicEventSubscription#string_not_ends_with}
        '''
        result = self._values.get("string_not_ends_with")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith"]]], result)

    @builtins.property
    def string_not_in(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn"]]]:
        '''string_not_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#string_not_in EventgridSystemTopicEventSubscription#string_not_in}
        '''
        result = self._values.get("string_not_in")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull",
    jsii_struct_bases=[],
    name_mapping={"key": "key"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull:
    def __init__(self, *, key: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined",
    jsii_struct_bases=[],
    name_mapping={"key": "key"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined:
    def __init__(self, *, key: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan:
    def __init__(self, *, key: builtins.str, value: jsii.Number) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals:
    def __init__(self, *, key: builtins.str, value: jsii.Number) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan:
    def __init__(self, *, key: builtins.str, value: jsii.Number) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals:
    def __init__(self, *, key: builtins.str, value: jsii.Number) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[jsii.Number],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBoolEquals")
    def put_bool_equals(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_bool_equals)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBoolEquals", [value]))

    @jsii.member(jsii_name="putIsNotNull")
    def put_is_not_null(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_is_not_null)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIsNotNull", [value]))

    @jsii.member(jsii_name="putIsNullOrUndefined")
    def put_is_null_or_undefined(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_is_null_or_undefined)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIsNullOrUndefined", [value]))

    @jsii.member(jsii_name="putNumberGreaterThan")
    def put_number_greater_than(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_number_greater_than)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberGreaterThan", [value]))

    @jsii.member(jsii_name="putNumberGreaterThanOrEquals")
    def put_number_greater_than_or_equals(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_number_greater_than_or_equals)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberGreaterThanOrEquals", [value]))

    @jsii.member(jsii_name="putNumberIn")
    def put_number_in(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_number_in)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberIn", [value]))

    @jsii.member(jsii_name="putNumberInRange")
    def put_number_in_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_number_in_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberInRange", [value]))

    @jsii.member(jsii_name="putNumberLessThan")
    def put_number_less_than(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_number_less_than)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberLessThan", [value]))

    @jsii.member(jsii_name="putNumberLessThanOrEquals")
    def put_number_less_than_or_equals(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_number_less_than_or_equals)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberLessThanOrEquals", [value]))

    @jsii.member(jsii_name="putNumberNotIn")
    def put_number_not_in(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_number_not_in)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberNotIn", [value]))

    @jsii.member(jsii_name="putNumberNotInRange")
    def put_number_not_in_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_number_not_in_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumberNotInRange", [value]))

    @jsii.member(jsii_name="putStringBeginsWith")
    def put_string_begins_with(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_string_begins_with)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringBeginsWith", [value]))

    @jsii.member(jsii_name="putStringContains")
    def put_string_contains(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_string_contains)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringContains", [value]))

    @jsii.member(jsii_name="putStringEndsWith")
    def put_string_ends_with(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_string_ends_with)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringEndsWith", [value]))

    @jsii.member(jsii_name="putStringIn")
    def put_string_in(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_string_in)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringIn", [value]))

    @jsii.member(jsii_name="putStringNotBeginsWith")
    def put_string_not_begins_with(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_string_not_begins_with)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringNotBeginsWith", [value]))

    @jsii.member(jsii_name="putStringNotContains")
    def put_string_not_contains(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_string_not_contains)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringNotContains", [value]))

    @jsii.member(jsii_name="putStringNotEndsWith")
    def put_string_not_ends_with(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_string_not_ends_with)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStringNotEndsWith", [value]))

    @jsii.member(jsii_name="putStringNotIn")
    def put_string_not_in(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference.put_string_not_in)
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
    def bool_equals(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList, jsii.get(self, "boolEquals"))

    @builtins.property
    @jsii.member(jsii_name="isNotNull")
    def is_not_null(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList, jsii.get(self, "isNotNull"))

    @builtins.property
    @jsii.member(jsii_name="isNullOrUndefined")
    def is_null_or_undefined(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList, jsii.get(self, "isNullOrUndefined"))

    @builtins.property
    @jsii.member(jsii_name="numberGreaterThan")
    def number_greater_than(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList, jsii.get(self, "numberGreaterThan"))

    @builtins.property
    @jsii.member(jsii_name="numberGreaterThanOrEquals")
    def number_greater_than_or_equals(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList, jsii.get(self, "numberGreaterThanOrEquals"))

    @builtins.property
    @jsii.member(jsii_name="numberIn")
    def number_in(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList, jsii.get(self, "numberIn"))

    @builtins.property
    @jsii.member(jsii_name="numberInRange")
    def number_in_range(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList, jsii.get(self, "numberInRange"))

    @builtins.property
    @jsii.member(jsii_name="numberLessThan")
    def number_less_than(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList, jsii.get(self, "numberLessThan"))

    @builtins.property
    @jsii.member(jsii_name="numberLessThanOrEquals")
    def number_less_than_or_equals(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList, jsii.get(self, "numberLessThanOrEquals"))

    @builtins.property
    @jsii.member(jsii_name="numberNotIn")
    def number_not_in(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList, jsii.get(self, "numberNotIn"))

    @builtins.property
    @jsii.member(jsii_name="numberNotInRange")
    def number_not_in_range(
        self,
    ) -> EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList:
        return typing.cast(EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList, jsii.get(self, "numberNotInRange"))

    @builtins.property
    @jsii.member(jsii_name="stringBeginsWith")
    def string_begins_with(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList", jsii.get(self, "stringBeginsWith"))

    @builtins.property
    @jsii.member(jsii_name="stringContains")
    def string_contains(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList", jsii.get(self, "stringContains"))

    @builtins.property
    @jsii.member(jsii_name="stringEndsWith")
    def string_ends_with(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList", jsii.get(self, "stringEndsWith"))

    @builtins.property
    @jsii.member(jsii_name="stringIn")
    def string_in(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList", jsii.get(self, "stringIn"))

    @builtins.property
    @jsii.member(jsii_name="stringNotBeginsWith")
    def string_not_begins_with(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList", jsii.get(self, "stringNotBeginsWith"))

    @builtins.property
    @jsii.member(jsii_name="stringNotContains")
    def string_not_contains(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList", jsii.get(self, "stringNotContains"))

    @builtins.property
    @jsii.member(jsii_name="stringNotEndsWith")
    def string_not_ends_with(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList", jsii.get(self, "stringNotEndsWith"))

    @builtins.property
    @jsii.member(jsii_name="stringNotIn")
    def string_not_in(
        self,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList":
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList", jsii.get(self, "stringNotIn"))

    @builtins.property
    @jsii.member(jsii_name="boolEqualsInput")
    def bool_equals_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals]]], jsii.get(self, "boolEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="isNotNullInput")
    def is_not_null_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull]]], jsii.get(self, "isNotNullInput"))

    @builtins.property
    @jsii.member(jsii_name="isNullOrUndefinedInput")
    def is_null_or_undefined_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined]]], jsii.get(self, "isNullOrUndefinedInput"))

    @builtins.property
    @jsii.member(jsii_name="numberGreaterThanInput")
    def number_greater_than_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan]]], jsii.get(self, "numberGreaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="numberGreaterThanOrEqualsInput")
    def number_greater_than_or_equals_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals]]], jsii.get(self, "numberGreaterThanOrEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInInput")
    def number_in_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn]]], jsii.get(self, "numberInInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInRangeInput")
    def number_in_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange]]], jsii.get(self, "numberInRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="numberLessThanInput")
    def number_less_than_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan]]], jsii.get(self, "numberLessThanInput"))

    @builtins.property
    @jsii.member(jsii_name="numberLessThanOrEqualsInput")
    def number_less_than_or_equals_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals]]], jsii.get(self, "numberLessThanOrEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="numberNotInInput")
    def number_not_in_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn]]], jsii.get(self, "numberNotInInput"))

    @builtins.property
    @jsii.member(jsii_name="numberNotInRangeInput")
    def number_not_in_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange]]], jsii.get(self, "numberNotInRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="stringBeginsWithInput")
    def string_begins_with_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith"]]], jsii.get(self, "stringBeginsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="stringContainsInput")
    def string_contains_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains"]]], jsii.get(self, "stringContainsInput"))

    @builtins.property
    @jsii.member(jsii_name="stringEndsWithInput")
    def string_ends_with_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith"]]], jsii.get(self, "stringEndsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="stringInInput")
    def string_in_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn"]]], jsii.get(self, "stringInInput"))

    @builtins.property
    @jsii.member(jsii_name="stringNotBeginsWithInput")
    def string_not_begins_with_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith"]]], jsii.get(self, "stringNotBeginsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="stringNotContainsInput")
    def string_not_contains_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains"]]], jsii.get(self, "stringNotContainsInput"))

    @builtins.property
    @jsii.member(jsii_name="stringNotEndsWithInput")
    def string_not_ends_with_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith"]]], jsii.get(self, "stringNotEndsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="stringNotInInput")
    def string_not_in_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn"]]], jsii.get(self, "stringNotInInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionAdvancedFilter]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionAdvancedFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionAdvancedFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#key EventgridSystemTopicEventSubscription#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#values EventgridSystemTopicEventSubscription#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "function_id": "functionId",
        "max_events_per_batch": "maxEventsPerBatch",
        "preferred_batch_size_in_kilobytes": "preferredBatchSizeInKilobytes",
    },
)
class EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint:
    def __init__(
        self,
        *,
        function_id: builtins.str,
        max_events_per_batch: typing.Optional[jsii.Number] = None,
        preferred_batch_size_in_kilobytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param function_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#function_id EventgridSystemTopicEventSubscription#function_id}.
        :param max_events_per_batch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_events_per_batch EventgridSystemTopicEventSubscription#max_events_per_batch}.
        :param preferred_batch_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#preferred_batch_size_in_kilobytes EventgridSystemTopicEventSubscription#preferred_batch_size_in_kilobytes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#function_id EventgridSystemTopicEventSubscription#function_id}.'''
        result = self._values.get("function_id")
        assert result is not None, "Required property 'function_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_events_per_batch(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_events_per_batch EventgridSystemTopicEventSubscription#max_events_per_batch}.'''
        result = self._values.get("max_events_per_batch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_batch_size_in_kilobytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#preferred_batch_size_in_kilobytes EventgridSystemTopicEventSubscription#preferred_batch_size_in_kilobytes}.'''
        result = self._values.get("preferred_batch_size_in_kilobytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference, "function_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionId", value)

    @builtins.property
    @jsii.member(jsii_name="maxEventsPerBatch")
    def max_events_per_batch(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxEventsPerBatch"))

    @max_events_per_batch.setter
    def max_events_per_batch(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference, "max_events_per_batch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxEventsPerBatch", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBatchSizeInKilobytes")
    def preferred_batch_size_in_kilobytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "preferredBatchSizeInKilobytes"))

    @preferred_batch_size_in_kilobytes.setter
    def preferred_batch_size_in_kilobytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference, "preferred_batch_size_in_kilobytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBatchSizeInKilobytes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionConfig",
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
        "resource_group_name": "resourceGroupName",
        "system_topic": "systemTopic",
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
class EventgridSystemTopicEventSubscriptionConfig(cdktf.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        system_topic: builtins.str,
        advanced_filter: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAdvancedFilter, typing.Dict[str, typing.Any]]] = None,
        advanced_filtering_on_arrays_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        azure_function_endpoint: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint, typing.Dict[str, typing.Any]]] = None,
        dead_letter_identity: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionDeadLetterIdentity", typing.Dict[str, typing.Any]]] = None,
        delivery_identity: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionDeliveryIdentity", typing.Dict[str, typing.Any]]] = None,
        delivery_property: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventgridSystemTopicEventSubscriptionDeliveryProperty", typing.Dict[str, typing.Any]]]]] = None,
        event_delivery_schema: typing.Optional[builtins.str] = None,
        eventhub_endpoint_id: typing.Optional[builtins.str] = None,
        expiration_time_utc: typing.Optional[builtins.str] = None,
        hybrid_connection_endpoint_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        included_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        retry_policy: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        service_bus_queue_endpoint_id: typing.Optional[builtins.str] = None,
        service_bus_topic_endpoint_id: typing.Optional[builtins.str] = None,
        storage_blob_dead_letter_destination: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination", typing.Dict[str, typing.Any]]] = None,
        storage_queue_endpoint: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionStorageQueueEndpoint", typing.Dict[str, typing.Any]]] = None,
        subject_filter: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionSubjectFilter", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
        webhook_endpoint: typing.Optional[typing.Union["EventgridSystemTopicEventSubscriptionWebhookEndpoint", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#name EventgridSystemTopicEventSubscription#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#resource_group_name EventgridSystemTopicEventSubscription#resource_group_name}.
        :param system_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#system_topic EventgridSystemTopicEventSubscription#system_topic}.
        :param advanced_filter: advanced_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#advanced_filter EventgridSystemTopicEventSubscription#advanced_filter}
        :param advanced_filtering_on_arrays_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#advanced_filtering_on_arrays_enabled EventgridSystemTopicEventSubscription#advanced_filtering_on_arrays_enabled}.
        :param azure_function_endpoint: azure_function_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#azure_function_endpoint EventgridSystemTopicEventSubscription#azure_function_endpoint}
        :param dead_letter_identity: dead_letter_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#dead_letter_identity EventgridSystemTopicEventSubscription#dead_letter_identity}
        :param delivery_identity: delivery_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delivery_identity EventgridSystemTopicEventSubscription#delivery_identity}
        :param delivery_property: delivery_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delivery_property EventgridSystemTopicEventSubscription#delivery_property}
        :param event_delivery_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#event_delivery_schema EventgridSystemTopicEventSubscription#event_delivery_schema}.
        :param eventhub_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#eventhub_endpoint_id EventgridSystemTopicEventSubscription#eventhub_endpoint_id}.
        :param expiration_time_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#expiration_time_utc EventgridSystemTopicEventSubscription#expiration_time_utc}.
        :param hybrid_connection_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#hybrid_connection_endpoint_id EventgridSystemTopicEventSubscription#hybrid_connection_endpoint_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#id EventgridSystemTopicEventSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param included_event_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#included_event_types EventgridSystemTopicEventSubscription#included_event_types}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#labels EventgridSystemTopicEventSubscription#labels}.
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#retry_policy EventgridSystemTopicEventSubscription#retry_policy}
        :param service_bus_queue_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#service_bus_queue_endpoint_id EventgridSystemTopicEventSubscription#service_bus_queue_endpoint_id}.
        :param service_bus_topic_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#service_bus_topic_endpoint_id EventgridSystemTopicEventSubscription#service_bus_topic_endpoint_id}.
        :param storage_blob_dead_letter_destination: storage_blob_dead_letter_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_blob_dead_letter_destination EventgridSystemTopicEventSubscription#storage_blob_dead_letter_destination}
        :param storage_queue_endpoint: storage_queue_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_queue_endpoint EventgridSystemTopicEventSubscription#storage_queue_endpoint}
        :param subject_filter: subject_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_filter EventgridSystemTopicEventSubscription#subject_filter}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#timeouts EventgridSystemTopicEventSubscription#timeouts}
        :param webhook_endpoint: webhook_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#webhook_endpoint EventgridSystemTopicEventSubscription#webhook_endpoint}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_filter, dict):
            advanced_filter = EventgridSystemTopicEventSubscriptionAdvancedFilter(**advanced_filter)
        if isinstance(azure_function_endpoint, dict):
            azure_function_endpoint = EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint(**azure_function_endpoint)
        if isinstance(dead_letter_identity, dict):
            dead_letter_identity = EventgridSystemTopicEventSubscriptionDeadLetterIdentity(**dead_letter_identity)
        if isinstance(delivery_identity, dict):
            delivery_identity = EventgridSystemTopicEventSubscriptionDeliveryIdentity(**delivery_identity)
        if isinstance(retry_policy, dict):
            retry_policy = EventgridSystemTopicEventSubscriptionRetryPolicy(**retry_policy)
        if isinstance(storage_blob_dead_letter_destination, dict):
            storage_blob_dead_letter_destination = EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination(**storage_blob_dead_letter_destination)
        if isinstance(storage_queue_endpoint, dict):
            storage_queue_endpoint = EventgridSystemTopicEventSubscriptionStorageQueueEndpoint(**storage_queue_endpoint)
        if isinstance(subject_filter, dict):
            subject_filter = EventgridSystemTopicEventSubscriptionSubjectFilter(**subject_filter)
        if isinstance(timeouts, dict):
            timeouts = EventgridSystemTopicEventSubscriptionTimeouts(**timeouts)
        if isinstance(webhook_endpoint, dict):
            webhook_endpoint = EventgridSystemTopicEventSubscriptionWebhookEndpoint(**webhook_endpoint)
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument system_topic", value=system_topic, expected_type=type_hints["system_topic"])
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
            "resource_group_name": resource_group_name,
            "system_topic": system_topic,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#name EventgridSystemTopicEventSubscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#resource_group_name EventgridSystemTopicEventSubscription#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def system_topic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#system_topic EventgridSystemTopicEventSubscription#system_topic}.'''
        result = self._values.get("system_topic")
        assert result is not None, "Required property 'system_topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_filter(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionAdvancedFilter]:
        '''advanced_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#advanced_filter EventgridSystemTopicEventSubscription#advanced_filter}
        '''
        result = self._values.get("advanced_filter")
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionAdvancedFilter], result)

    @builtins.property
    def advanced_filtering_on_arrays_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#advanced_filtering_on_arrays_enabled EventgridSystemTopicEventSubscription#advanced_filtering_on_arrays_enabled}.'''
        result = self._values.get("advanced_filtering_on_arrays_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def azure_function_endpoint(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint]:
        '''azure_function_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#azure_function_endpoint EventgridSystemTopicEventSubscription#azure_function_endpoint}
        '''
        result = self._values.get("azure_function_endpoint")
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint], result)

    @builtins.property
    def dead_letter_identity(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionDeadLetterIdentity"]:
        '''dead_letter_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#dead_letter_identity EventgridSystemTopicEventSubscription#dead_letter_identity}
        '''
        result = self._values.get("dead_letter_identity")
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionDeadLetterIdentity"], result)

    @builtins.property
    def delivery_identity(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionDeliveryIdentity"]:
        '''delivery_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delivery_identity EventgridSystemTopicEventSubscription#delivery_identity}
        '''
        result = self._values.get("delivery_identity")
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionDeliveryIdentity"], result)

    @builtins.property
    def delivery_property(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionDeliveryProperty"]]]:
        '''delivery_property block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delivery_property EventgridSystemTopicEventSubscription#delivery_property}
        '''
        result = self._values.get("delivery_property")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventgridSystemTopicEventSubscriptionDeliveryProperty"]]], result)

    @builtins.property
    def event_delivery_schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#event_delivery_schema EventgridSystemTopicEventSubscription#event_delivery_schema}.'''
        result = self._values.get("event_delivery_schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def eventhub_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#eventhub_endpoint_id EventgridSystemTopicEventSubscription#eventhub_endpoint_id}.'''
        result = self._values.get("eventhub_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_time_utc(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#expiration_time_utc EventgridSystemTopicEventSubscription#expiration_time_utc}.'''
        result = self._values.get("expiration_time_utc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hybrid_connection_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#hybrid_connection_endpoint_id EventgridSystemTopicEventSubscription#hybrid_connection_endpoint_id}.'''
        result = self._values.get("hybrid_connection_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#id EventgridSystemTopicEventSubscription#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def included_event_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#included_event_types EventgridSystemTopicEventSubscription#included_event_types}.'''
        result = self._values.get("included_event_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#labels EventgridSystemTopicEventSubscription#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def retry_policy(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#retry_policy EventgridSystemTopicEventSubscription#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionRetryPolicy"], result)

    @builtins.property
    def service_bus_queue_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#service_bus_queue_endpoint_id EventgridSystemTopicEventSubscription#service_bus_queue_endpoint_id}.'''
        result = self._values.get("service_bus_queue_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_bus_topic_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#service_bus_topic_endpoint_id EventgridSystemTopicEventSubscription#service_bus_topic_endpoint_id}.'''
        result = self._values.get("service_bus_topic_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_blob_dead_letter_destination(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination"]:
        '''storage_blob_dead_letter_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_blob_dead_letter_destination EventgridSystemTopicEventSubscription#storage_blob_dead_letter_destination}
        '''
        result = self._values.get("storage_blob_dead_letter_destination")
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination"], result)

    @builtins.property
    def storage_queue_endpoint(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionStorageQueueEndpoint"]:
        '''storage_queue_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_queue_endpoint EventgridSystemTopicEventSubscription#storage_queue_endpoint}
        '''
        result = self._values.get("storage_queue_endpoint")
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionStorageQueueEndpoint"], result)

    @builtins.property
    def subject_filter(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionSubjectFilter"]:
        '''subject_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_filter EventgridSystemTopicEventSubscription#subject_filter}
        '''
        result = self._values.get("subject_filter")
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionSubjectFilter"], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#timeouts EventgridSystemTopicEventSubscription#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionTimeouts"], result)

    @builtins.property
    def webhook_endpoint(
        self,
    ) -> typing.Optional["EventgridSystemTopicEventSubscriptionWebhookEndpoint"]:
        '''webhook_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#webhook_endpoint EventgridSystemTopicEventSubscription#webhook_endpoint}
        '''
        result = self._values.get("webhook_endpoint")
        return typing.cast(typing.Optional["EventgridSystemTopicEventSubscriptionWebhookEndpoint"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionDeadLetterIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "user_assigned_identity": "userAssignedIdentity"},
)
class EventgridSystemTopicEventSubscriptionDeadLetterIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        user_assigned_identity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#type EventgridSystemTopicEventSubscription#type}.
        :param user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#user_assigned_identity EventgridSystemTopicEventSubscription#user_assigned_identity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionDeadLetterIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user_assigned_identity", value=user_assigned_identity, expected_type=type_hints["user_assigned_identity"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if user_assigned_identity is not None:
            self._values["user_assigned_identity"] = user_assigned_identity

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#type EventgridSystemTopicEventSubscription#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_assigned_identity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#user_assigned_identity EventgridSystemTopicEventSubscription#user_assigned_identity}.'''
        result = self._values.get("user_assigned_identity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionDeadLetterIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentity")
    def user_assigned_identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentity"))

    @user_assigned_identity.setter
    def user_assigned_identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference, "user_assigned_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionDeadLetterIdentity]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionDeadLetterIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionDeadLetterIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionDeliveryIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "user_assigned_identity": "userAssignedIdentity"},
)
class EventgridSystemTopicEventSubscriptionDeliveryIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        user_assigned_identity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#type EventgridSystemTopicEventSubscription#type}.
        :param user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#user_assigned_identity EventgridSystemTopicEventSubscription#user_assigned_identity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionDeliveryIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user_assigned_identity", value=user_assigned_identity, expected_type=type_hints["user_assigned_identity"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if user_assigned_identity is not None:
            self._values["user_assigned_identity"] = user_assigned_identity

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#type EventgridSystemTopicEventSubscription#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_assigned_identity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#user_assigned_identity EventgridSystemTopicEventSubscription#user_assigned_identity}.'''
        result = self._values.get("user_assigned_identity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionDeliveryIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentity")
    def user_assigned_identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentity"))

    @user_assigned_identity.setter
    def user_assigned_identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference, "user_assigned_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionDeliveryIdentity]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionDeliveryIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionDeliveryIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionDeliveryProperty",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "type": "type",
        "secret": "secret",
        "source_field": "sourceField",
        "value": "value",
    },
)
class EventgridSystemTopicEventSubscriptionDeliveryProperty:
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
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#header_name EventgridSystemTopicEventSubscription#header_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#type EventgridSystemTopicEventSubscription#type}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#secret EventgridSystemTopicEventSubscription#secret}.
        :param source_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#source_field EventgridSystemTopicEventSubscription#source_field}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionDeliveryProperty.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#header_name EventgridSystemTopicEventSubscription#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#type EventgridSystemTopicEventSubscription#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#secret EventgridSystemTopicEventSubscription#secret}.'''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#source_field EventgridSystemTopicEventSubscription#source_field}.'''
        result = self._values.get("source_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#value EventgridSystemTopicEventSubscription#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionDeliveryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionDeliveryPropertyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionDeliveryPropertyList",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionDeliveryPropertyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionDeliveryPropertyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionDeliveryProperty]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionDeliveryProperty]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventgridSystemTopicEventSubscriptionDeliveryProperty]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference, "secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="sourceField")
    def source_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceField"))

    @source_field.setter
    def source_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference, "source_field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceField", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionDeliveryProperty, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionDeliveryProperty, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionDeliveryProperty, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "event_time_to_live": "eventTimeToLive",
        "max_delivery_attempts": "maxDeliveryAttempts",
    },
)
class EventgridSystemTopicEventSubscriptionRetryPolicy:
    def __init__(
        self,
        *,
        event_time_to_live: jsii.Number,
        max_delivery_attempts: jsii.Number,
    ) -> None:
        '''
        :param event_time_to_live: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#event_time_to_live EventgridSystemTopicEventSubscription#event_time_to_live}.
        :param max_delivery_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_delivery_attempts EventgridSystemTopicEventSubscription#max_delivery_attempts}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionRetryPolicy.__init__)
            check_type(argname="argument event_time_to_live", value=event_time_to_live, expected_type=type_hints["event_time_to_live"])
            check_type(argname="argument max_delivery_attempts", value=max_delivery_attempts, expected_type=type_hints["max_delivery_attempts"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_time_to_live": event_time_to_live,
            "max_delivery_attempts": max_delivery_attempts,
        }

    @builtins.property
    def event_time_to_live(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#event_time_to_live EventgridSystemTopicEventSubscription#event_time_to_live}.'''
        result = self._values.get("event_time_to_live")
        assert result is not None, "Required property 'event_time_to_live' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_delivery_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_delivery_attempts EventgridSystemTopicEventSubscription#max_delivery_attempts}.'''
        result = self._values.get("max_delivery_attempts")
        assert result is not None, "Required property 'max_delivery_attempts' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference, "event_time_to_live").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTimeToLive", value)

    @builtins.property
    @jsii.member(jsii_name="maxDeliveryAttempts")
    def max_delivery_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDeliveryAttempts"))

    @max_delivery_attempts.setter
    def max_delivery_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference, "max_delivery_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDeliveryAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionRetryPolicy]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination",
    jsii_struct_bases=[],
    name_mapping={
        "storage_account_id": "storageAccountId",
        "storage_blob_container_name": "storageBlobContainerName",
    },
)
class EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination:
    def __init__(
        self,
        *,
        storage_account_id: builtins.str,
        storage_blob_container_name: builtins.str,
    ) -> None:
        '''
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_account_id EventgridSystemTopicEventSubscription#storage_account_id}.
        :param storage_blob_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_blob_container_name EventgridSystemTopicEventSubscription#storage_blob_container_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination.__init__)
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument storage_blob_container_name", value=storage_blob_container_name, expected_type=type_hints["storage_blob_container_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage_account_id": storage_account_id,
            "storage_blob_container_name": storage_blob_container_name,
        }

    @builtins.property
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_account_id EventgridSystemTopicEventSubscription#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_blob_container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_blob_container_name EventgridSystemTopicEventSubscription#storage_blob_container_name}.'''
        result = self._values.get("storage_blob_container_name")
        assert result is not None, "Required property 'storage_blob_container_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="storageBlobContainerName")
    def storage_blob_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageBlobContainerName"))

    @storage_blob_container_name.setter
    def storage_blob_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference, "storage_blob_container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageBlobContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionStorageQueueEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "queue_name": "queueName",
        "storage_account_id": "storageAccountId",
        "queue_message_time_to_live_in_seconds": "queueMessageTimeToLiveInSeconds",
    },
)
class EventgridSystemTopicEventSubscriptionStorageQueueEndpoint:
    def __init__(
        self,
        *,
        queue_name: builtins.str,
        storage_account_id: builtins.str,
        queue_message_time_to_live_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param queue_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#queue_name EventgridSystemTopicEventSubscription#queue_name}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_account_id EventgridSystemTopicEventSubscription#storage_account_id}.
        :param queue_message_time_to_live_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#queue_message_time_to_live_in_seconds EventgridSystemTopicEventSubscription#queue_message_time_to_live_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionStorageQueueEndpoint.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#queue_name EventgridSystemTopicEventSubscription#queue_name}.'''
        result = self._values.get("queue_name")
        assert result is not None, "Required property 'queue_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#storage_account_id EventgridSystemTopicEventSubscription#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_message_time_to_live_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#queue_message_time_to_live_in_seconds EventgridSystemTopicEventSubscription#queue_message_time_to_live_in_seconds}.'''
        result = self._values.get("queue_message_time_to_live_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionStorageQueueEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference, "queue_message_time_to_live_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueMessageTimeToLiveInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="queueName")
    def queue_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueName"))

    @queue_name.setter
    def queue_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference, "queue_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionStorageQueueEndpoint]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionStorageQueueEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionStorageQueueEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionSubjectFilter",
    jsii_struct_bases=[],
    name_mapping={
        "case_sensitive": "caseSensitive",
        "subject_begins_with": "subjectBeginsWith",
        "subject_ends_with": "subjectEndsWith",
    },
)
class EventgridSystemTopicEventSubscriptionSubjectFilter:
    def __init__(
        self,
        *,
        case_sensitive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subject_begins_with: typing.Optional[builtins.str] = None,
        subject_ends_with: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param case_sensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#case_sensitive EventgridSystemTopicEventSubscription#case_sensitive}.
        :param subject_begins_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_begins_with EventgridSystemTopicEventSubscription#subject_begins_with}.
        :param subject_ends_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_ends_with EventgridSystemTopicEventSubscription#subject_ends_with}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionSubjectFilter.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#case_sensitive EventgridSystemTopicEventSubscription#case_sensitive}.'''
        result = self._values.get("case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subject_begins_with(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_begins_with EventgridSystemTopicEventSubscription#subject_begins_with}.'''
        result = self._values.get("subject_begins_with")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_ends_with(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#subject_ends_with EventgridSystemTopicEventSubscription#subject_ends_with}.'''
        result = self._values.get("subject_ends_with")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionSubjectFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference, "case_sensitive").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="subjectBeginsWith")
    def subject_begins_with(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectBeginsWith"))

    @subject_begins_with.setter
    def subject_begins_with(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference, "subject_begins_with").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectBeginsWith", value)

    @builtins.property
    @jsii.member(jsii_name="subjectEndsWith")
    def subject_ends_with(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectEndsWith"))

    @subject_ends_with.setter
    def subject_ends_with(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference, "subject_ends_with").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectEndsWith", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionSubjectFilter]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionSubjectFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionSubjectFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class EventgridSystemTopicEventSubscriptionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#create EventgridSystemTopicEventSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delete EventgridSystemTopicEventSubscription#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#read EventgridSystemTopicEventSubscription#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#update EventgridSystemTopicEventSubscription#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#create EventgridSystemTopicEventSubscription#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#delete EventgridSystemTopicEventSubscription#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#read EventgridSystemTopicEventSubscription#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#update EventgridSystemTopicEventSubscription#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventgridSystemTopicEventSubscriptionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionWebhookEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "active_directory_app_id_or_uri": "activeDirectoryAppIdOrUri",
        "active_directory_tenant_id": "activeDirectoryTenantId",
        "max_events_per_batch": "maxEventsPerBatch",
        "preferred_batch_size_in_kilobytes": "preferredBatchSizeInKilobytes",
    },
)
class EventgridSystemTopicEventSubscriptionWebhookEndpoint:
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
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#url EventgridSystemTopicEventSubscription#url}.
        :param active_directory_app_id_or_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#active_directory_app_id_or_uri EventgridSystemTopicEventSubscription#active_directory_app_id_or_uri}.
        :param active_directory_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#active_directory_tenant_id EventgridSystemTopicEventSubscription#active_directory_tenant_id}.
        :param max_events_per_batch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_events_per_batch EventgridSystemTopicEventSubscription#max_events_per_batch}.
        :param preferred_batch_size_in_kilobytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#preferred_batch_size_in_kilobytes EventgridSystemTopicEventSubscription#preferred_batch_size_in_kilobytes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionWebhookEndpoint.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#url EventgridSystemTopicEventSubscription#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_directory_app_id_or_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#active_directory_app_id_or_uri EventgridSystemTopicEventSubscription#active_directory_app_id_or_uri}.'''
        result = self._values.get("active_directory_app_id_or_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def active_directory_tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#active_directory_tenant_id EventgridSystemTopicEventSubscription#active_directory_tenant_id}.'''
        result = self._values.get("active_directory_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_events_per_batch(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#max_events_per_batch EventgridSystemTopicEventSubscription#max_events_per_batch}.'''
        result = self._values.get("max_events_per_batch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_batch_size_in_kilobytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventgrid_system_topic_event_subscription#preferred_batch_size_in_kilobytes EventgridSystemTopicEventSubscription#preferred_batch_size_in_kilobytes}.'''
        result = self._values.get("preferred_batch_size_in_kilobytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventgridSystemTopicEventSubscriptionWebhookEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventgridSystemTopicEventSubscription.EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference",
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
            type_hints = typing.get_type_hints(EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference, "active_directory_app_id_or_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeDirectoryAppIdOrUri", value)

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryTenantId")
    def active_directory_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activeDirectoryTenantId"))

    @active_directory_tenant_id.setter
    def active_directory_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference, "active_directory_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeDirectoryTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="maxEventsPerBatch")
    def max_events_per_batch(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxEventsPerBatch"))

    @max_events_per_batch.setter
    def max_events_per_batch(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference, "max_events_per_batch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxEventsPerBatch", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBatchSizeInKilobytes")
    def preferred_batch_size_in_kilobytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "preferredBatchSizeInKilobytes"))

    @preferred_batch_size_in_kilobytes.setter
    def preferred_batch_size_in_kilobytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference, "preferred_batch_size_in_kilobytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBatchSizeInKilobytes", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventgridSystemTopicEventSubscriptionWebhookEndpoint]:
        return typing.cast(typing.Optional[EventgridSystemTopicEventSubscriptionWebhookEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventgridSystemTopicEventSubscriptionWebhookEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EventgridSystemTopicEventSubscription",
    "EventgridSystemTopicEventSubscriptionAdvancedFilter",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEquals",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterBoolEqualsOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNull",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNotNullOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefined",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterIsNullOrUndefinedOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThan",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEquals",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOrEqualsOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberGreaterThanOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberIn",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRange",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberInRangeOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThan",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEquals",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOrEqualsOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberLessThanOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotIn",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRange",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterNumberNotInRangeOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWith",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringBeginsWithOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringContains",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringContainsOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWith",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringEndsWithOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringIn",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringInList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringInOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWith",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotBeginsWithOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContains",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotContainsOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWith",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotEndsWithOutputReference",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotIn",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInList",
    "EventgridSystemTopicEventSubscriptionAdvancedFilterStringNotInOutputReference",
    "EventgridSystemTopicEventSubscriptionAzureFunctionEndpoint",
    "EventgridSystemTopicEventSubscriptionAzureFunctionEndpointOutputReference",
    "EventgridSystemTopicEventSubscriptionConfig",
    "EventgridSystemTopicEventSubscriptionDeadLetterIdentity",
    "EventgridSystemTopicEventSubscriptionDeadLetterIdentityOutputReference",
    "EventgridSystemTopicEventSubscriptionDeliveryIdentity",
    "EventgridSystemTopicEventSubscriptionDeliveryIdentityOutputReference",
    "EventgridSystemTopicEventSubscriptionDeliveryProperty",
    "EventgridSystemTopicEventSubscriptionDeliveryPropertyList",
    "EventgridSystemTopicEventSubscriptionDeliveryPropertyOutputReference",
    "EventgridSystemTopicEventSubscriptionRetryPolicy",
    "EventgridSystemTopicEventSubscriptionRetryPolicyOutputReference",
    "EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestination",
    "EventgridSystemTopicEventSubscriptionStorageBlobDeadLetterDestinationOutputReference",
    "EventgridSystemTopicEventSubscriptionStorageQueueEndpoint",
    "EventgridSystemTopicEventSubscriptionStorageQueueEndpointOutputReference",
    "EventgridSystemTopicEventSubscriptionSubjectFilter",
    "EventgridSystemTopicEventSubscriptionSubjectFilterOutputReference",
    "EventgridSystemTopicEventSubscriptionTimeouts",
    "EventgridSystemTopicEventSubscriptionTimeoutsOutputReference",
    "EventgridSystemTopicEventSubscriptionWebhookEndpoint",
    "EventgridSystemTopicEventSubscriptionWebhookEndpointOutputReference",
]

publication.publish()
