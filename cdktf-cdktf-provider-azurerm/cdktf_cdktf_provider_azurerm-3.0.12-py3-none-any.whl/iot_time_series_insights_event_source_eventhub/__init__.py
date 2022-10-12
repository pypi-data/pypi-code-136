'''
# `azurerm_iot_time_series_insights_event_source_eventhub`

Refer to the Terraform Registory for docs: [`azurerm_iot_time_series_insights_event_source_eventhub`](https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub).
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


class IotTimeSeriesInsightsEventSourceEventhub(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsEventSourceEventhub.IotTimeSeriesInsightsEventSourceEventhub",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub azurerm_iot_time_series_insights_event_source_eventhub}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        consumer_group_name: builtins.str,
        environment_id: builtins.str,
        eventhub_name: builtins.str,
        event_source_resource_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        namespace_name: builtins.str,
        shared_access_key: builtins.str,
        shared_access_key_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IotTimeSeriesInsightsEventSourceEventhubTimeouts", typing.Dict[str, typing.Any]]] = None,
        timestamp_property_name: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub azurerm_iot_time_series_insights_event_source_eventhub} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param consumer_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#consumer_group_name IotTimeSeriesInsightsEventSourceEventhub#consumer_group_name}.
        :param environment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#environment_id IotTimeSeriesInsightsEventSourceEventhub#environment_id}.
        :param eventhub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#eventhub_name IotTimeSeriesInsightsEventSourceEventhub#eventhub_name}.
        :param event_source_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#event_source_resource_id IotTimeSeriesInsightsEventSourceEventhub#event_source_resource_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#location IotTimeSeriesInsightsEventSourceEventhub#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#name IotTimeSeriesInsightsEventSourceEventhub#name}.
        :param namespace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#namespace_name IotTimeSeriesInsightsEventSourceEventhub#namespace_name}.
        :param shared_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#shared_access_key IotTimeSeriesInsightsEventSourceEventhub#shared_access_key}.
        :param shared_access_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#shared_access_key_name IotTimeSeriesInsightsEventSourceEventhub#shared_access_key_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#id IotTimeSeriesInsightsEventSourceEventhub#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#tags IotTimeSeriesInsightsEventSourceEventhub#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#timeouts IotTimeSeriesInsightsEventSourceEventhub#timeouts}
        :param timestamp_property_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#timestamp_property_name IotTimeSeriesInsightsEventSourceEventhub#timestamp_property_name}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsEventSourceEventhub.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IotTimeSeriesInsightsEventSourceEventhubConfig(
            consumer_group_name=consumer_group_name,
            environment_id=environment_id,
            eventhub_name=eventhub_name,
            event_source_resource_id=event_source_resource_id,
            location=location,
            name=name,
            namespace_name=namespace_name,
            shared_access_key=shared_access_key,
            shared_access_key_name=shared_access_key_name,
            id=id,
            tags=tags,
            timeouts=timeouts,
            timestamp_property_name=timestamp_property_name,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#create IotTimeSeriesInsightsEventSourceEventhub#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#delete IotTimeSeriesInsightsEventSourceEventhub#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#read IotTimeSeriesInsightsEventSourceEventhub#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#update IotTimeSeriesInsightsEventSourceEventhub#update}.
        '''
        value = IotTimeSeriesInsightsEventSourceEventhubTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimestampPropertyName")
    def reset_timestamp_property_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestampPropertyName", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference":
        return typing.cast("IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="consumerGroupNameInput")
    def consumer_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentIdInput")
    def environment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="eventhubNameInput")
    def eventhub_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventhubNameInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceResourceIdInput")
    def event_source_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventSourceResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceNameInput")
    def namespace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedAccessKeyInput")
    def shared_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedAccessKeyNameInput")
    def shared_access_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedAccessKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["IotTimeSeriesInsightsEventSourceEventhubTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IotTimeSeriesInsightsEventSourceEventhubTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampPropertyNameInput")
    def timestamp_property_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timestampPropertyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerGroupName")
    def consumer_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerGroupName"))

    @consumer_group_name.setter
    def consumer_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "consumer_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentId"))

    @environment_id.setter
    def environment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "environment_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentId", value)

    @builtins.property
    @jsii.member(jsii_name="eventhubName")
    def eventhub_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventhubName"))

    @eventhub_name.setter
    def eventhub_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "eventhub_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventhubName", value)

    @builtins.property
    @jsii.member(jsii_name="eventSourceResourceId")
    def event_source_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventSourceResourceId"))

    @event_source_resource_id.setter
    def event_source_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "event_source_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSourceResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "namespace_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAccessKey")
    def shared_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedAccessKey"))

    @shared_access_key.setter
    def shared_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "shared_access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAccessKeyName")
    def shared_access_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedAccessKeyName"))

    @shared_access_key_name.setter
    def shared_access_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "shared_access_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAccessKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timestampPropertyName")
    def timestamp_property_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timestampPropertyName"))

    @timestamp_property_name.setter
    def timestamp_property_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhub, "timestamp_property_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timestampPropertyName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsEventSourceEventhub.IotTimeSeriesInsightsEventSourceEventhubConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "consumer_group_name": "consumerGroupName",
        "environment_id": "environmentId",
        "eventhub_name": "eventhubName",
        "event_source_resource_id": "eventSourceResourceId",
        "location": "location",
        "name": "name",
        "namespace_name": "namespaceName",
        "shared_access_key": "sharedAccessKey",
        "shared_access_key_name": "sharedAccessKeyName",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
        "timestamp_property_name": "timestampPropertyName",
    },
)
class IotTimeSeriesInsightsEventSourceEventhubConfig(cdktf.TerraformMetaArguments):
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
        consumer_group_name: builtins.str,
        environment_id: builtins.str,
        eventhub_name: builtins.str,
        event_source_resource_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        namespace_name: builtins.str,
        shared_access_key: builtins.str,
        shared_access_key_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["IotTimeSeriesInsightsEventSourceEventhubTimeouts", typing.Dict[str, typing.Any]]] = None,
        timestamp_property_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param consumer_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#consumer_group_name IotTimeSeriesInsightsEventSourceEventhub#consumer_group_name}.
        :param environment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#environment_id IotTimeSeriesInsightsEventSourceEventhub#environment_id}.
        :param eventhub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#eventhub_name IotTimeSeriesInsightsEventSourceEventhub#eventhub_name}.
        :param event_source_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#event_source_resource_id IotTimeSeriesInsightsEventSourceEventhub#event_source_resource_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#location IotTimeSeriesInsightsEventSourceEventhub#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#name IotTimeSeriesInsightsEventSourceEventhub#name}.
        :param namespace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#namespace_name IotTimeSeriesInsightsEventSourceEventhub#namespace_name}.
        :param shared_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#shared_access_key IotTimeSeriesInsightsEventSourceEventhub#shared_access_key}.
        :param shared_access_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#shared_access_key_name IotTimeSeriesInsightsEventSourceEventhub#shared_access_key_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#id IotTimeSeriesInsightsEventSourceEventhub#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#tags IotTimeSeriesInsightsEventSourceEventhub#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#timeouts IotTimeSeriesInsightsEventSourceEventhub#timeouts}
        :param timestamp_property_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#timestamp_property_name IotTimeSeriesInsightsEventSourceEventhub#timestamp_property_name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = IotTimeSeriesInsightsEventSourceEventhubTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsEventSourceEventhubConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument consumer_group_name", value=consumer_group_name, expected_type=type_hints["consumer_group_name"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
            check_type(argname="argument eventhub_name", value=eventhub_name, expected_type=type_hints["eventhub_name"])
            check_type(argname="argument event_source_resource_id", value=event_source_resource_id, expected_type=type_hints["event_source_resource_id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument shared_access_key", value=shared_access_key, expected_type=type_hints["shared_access_key"])
            check_type(argname="argument shared_access_key_name", value=shared_access_key_name, expected_type=type_hints["shared_access_key_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timestamp_property_name", value=timestamp_property_name, expected_type=type_hints["timestamp_property_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "consumer_group_name": consumer_group_name,
            "environment_id": environment_id,
            "eventhub_name": eventhub_name,
            "event_source_resource_id": event_source_resource_id,
            "location": location,
            "name": name,
            "namespace_name": namespace_name,
            "shared_access_key": shared_access_key,
            "shared_access_key_name": shared_access_key_name,
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
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timestamp_property_name is not None:
            self._values["timestamp_property_name"] = timestamp_property_name

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
    def consumer_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#consumer_group_name IotTimeSeriesInsightsEventSourceEventhub#consumer_group_name}.'''
        result = self._values.get("consumer_group_name")
        assert result is not None, "Required property 'consumer_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#environment_id IotTimeSeriesInsightsEventSourceEventhub#environment_id}.'''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def eventhub_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#eventhub_name IotTimeSeriesInsightsEventSourceEventhub#eventhub_name}.'''
        result = self._values.get("eventhub_name")
        assert result is not None, "Required property 'eventhub_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_source_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#event_source_resource_id IotTimeSeriesInsightsEventSourceEventhub#event_source_resource_id}.'''
        result = self._values.get("event_source_resource_id")
        assert result is not None, "Required property 'event_source_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#location IotTimeSeriesInsightsEventSourceEventhub#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#name IotTimeSeriesInsightsEventSourceEventhub#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#namespace_name IotTimeSeriesInsightsEventSourceEventhub#namespace_name}.'''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shared_access_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#shared_access_key IotTimeSeriesInsightsEventSourceEventhub#shared_access_key}.'''
        result = self._values.get("shared_access_key")
        assert result is not None, "Required property 'shared_access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shared_access_key_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#shared_access_key_name IotTimeSeriesInsightsEventSourceEventhub#shared_access_key_name}.'''
        result = self._values.get("shared_access_key_name")
        assert result is not None, "Required property 'shared_access_key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#id IotTimeSeriesInsightsEventSourceEventhub#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#tags IotTimeSeriesInsightsEventSourceEventhub#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["IotTimeSeriesInsightsEventSourceEventhubTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#timeouts IotTimeSeriesInsightsEventSourceEventhub#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IotTimeSeriesInsightsEventSourceEventhubTimeouts"], result)

    @builtins.property
    def timestamp_property_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#timestamp_property_name IotTimeSeriesInsightsEventSourceEventhub#timestamp_property_name}.'''
        result = self._values.get("timestamp_property_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTimeSeriesInsightsEventSourceEventhubConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsEventSourceEventhub.IotTimeSeriesInsightsEventSourceEventhubTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class IotTimeSeriesInsightsEventSourceEventhubTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#create IotTimeSeriesInsightsEventSourceEventhub#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#delete IotTimeSeriesInsightsEventSourceEventhub#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#read IotTimeSeriesInsightsEventSourceEventhub#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#update IotTimeSeriesInsightsEventSourceEventhub#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsEventSourceEventhubTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#create IotTimeSeriesInsightsEventSourceEventhub#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#delete IotTimeSeriesInsightsEventSourceEventhub#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#read IotTimeSeriesInsightsEventSourceEventhub#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/iot_time_series_insights_event_source_eventhub#update IotTimeSeriesInsightsEventSourceEventhub#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTimeSeriesInsightsEventSourceEventhubTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.iotTimeSeriesInsightsEventSourceEventhub.IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTimeSeriesInsightsEventSourceEventhubTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTimeSeriesInsightsEventSourceEventhubTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTimeSeriesInsightsEventSourceEventhubTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IotTimeSeriesInsightsEventSourceEventhub",
    "IotTimeSeriesInsightsEventSourceEventhubConfig",
    "IotTimeSeriesInsightsEventSourceEventhubTimeouts",
    "IotTimeSeriesInsightsEventSourceEventhubTimeoutsOutputReference",
]

publication.publish()
