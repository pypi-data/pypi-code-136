'''
# `azurerm_stream_analytics_output_eventhub`

Refer to the Terraform Registory for docs: [`azurerm_stream_analytics_output_eventhub`](https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub).
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


class StreamAnalyticsOutputEventhub(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputEventhub.StreamAnalyticsOutputEventhub",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub azurerm_stream_analytics_output_eventhub}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        eventhub_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        serialization: typing.Union["StreamAnalyticsOutputEventhubSerialization", typing.Dict[str, typing.Any]],
        servicebus_namespace: builtins.str,
        shared_access_policy_key: builtins.str,
        shared_access_policy_name: builtins.str,
        stream_analytics_job_name: builtins.str,
        authentication_mode: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        partition_key: typing.Optional[builtins.str] = None,
        property_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StreamAnalyticsOutputEventhubTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub azurerm_stream_analytics_output_eventhub} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param eventhub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#eventhub_name StreamAnalyticsOutputEventhub#eventhub_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#name StreamAnalyticsOutputEventhub#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#resource_group_name StreamAnalyticsOutputEventhub#resource_group_name}.
        :param serialization: serialization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#serialization StreamAnalyticsOutputEventhub#serialization}
        :param servicebus_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#servicebus_namespace StreamAnalyticsOutputEventhub#servicebus_namespace}.
        :param shared_access_policy_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#shared_access_policy_key StreamAnalyticsOutputEventhub#shared_access_policy_key}.
        :param shared_access_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#shared_access_policy_name StreamAnalyticsOutputEventhub#shared_access_policy_name}.
        :param stream_analytics_job_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#stream_analytics_job_name StreamAnalyticsOutputEventhub#stream_analytics_job_name}.
        :param authentication_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#authentication_mode StreamAnalyticsOutputEventhub#authentication_mode}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#id StreamAnalyticsOutputEventhub#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param partition_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#partition_key StreamAnalyticsOutputEventhub#partition_key}.
        :param property_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#property_columns StreamAnalyticsOutputEventhub#property_columns}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#timeouts StreamAnalyticsOutputEventhub#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsOutputEventhub.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StreamAnalyticsOutputEventhubConfig(
            eventhub_name=eventhub_name,
            name=name,
            resource_group_name=resource_group_name,
            serialization=serialization,
            servicebus_namespace=servicebus_namespace,
            shared_access_policy_key=shared_access_policy_key,
            shared_access_policy_name=shared_access_policy_name,
            stream_analytics_job_name=stream_analytics_job_name,
            authentication_mode=authentication_mode,
            id=id,
            partition_key=partition_key,
            property_columns=property_columns,
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

    @jsii.member(jsii_name="putSerialization")
    def put_serialization(
        self,
        *,
        type: builtins.str,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#type StreamAnalyticsOutputEventhub#type}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#encoding StreamAnalyticsOutputEventhub#encoding}.
        :param field_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#field_delimiter StreamAnalyticsOutputEventhub#field_delimiter}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#format StreamAnalyticsOutputEventhub#format}.
        '''
        value = StreamAnalyticsOutputEventhubSerialization(
            type=type,
            encoding=encoding,
            field_delimiter=field_delimiter,
            format=format,
        )

        return typing.cast(None, jsii.invoke(self, "putSerialization", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#create StreamAnalyticsOutputEventhub#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#delete StreamAnalyticsOutputEventhub#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#read StreamAnalyticsOutputEventhub#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#update StreamAnalyticsOutputEventhub#update}.
        '''
        value = StreamAnalyticsOutputEventhubTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuthenticationMode")
    def reset_authentication_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationMode", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPartitionKey")
    def reset_partition_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionKey", []))

    @jsii.member(jsii_name="resetPropertyColumns")
    def reset_property_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropertyColumns", []))

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
    @jsii.member(jsii_name="serialization")
    def serialization(
        self,
    ) -> "StreamAnalyticsOutputEventhubSerializationOutputReference":
        return typing.cast("StreamAnalyticsOutputEventhubSerializationOutputReference", jsii.get(self, "serialization"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StreamAnalyticsOutputEventhubTimeoutsOutputReference":
        return typing.cast("StreamAnalyticsOutputEventhubTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authenticationModeInput")
    def authentication_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationModeInput"))

    @builtins.property
    @jsii.member(jsii_name="eventhubNameInput")
    def eventhub_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventhubNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyInput")
    def partition_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyColumnsInput")
    def property_columns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "propertyColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serializationInput")
    def serialization_input(
        self,
    ) -> typing.Optional["StreamAnalyticsOutputEventhubSerialization"]:
        return typing.cast(typing.Optional["StreamAnalyticsOutputEventhubSerialization"], jsii.get(self, "serializationInput"))

    @builtins.property
    @jsii.member(jsii_name="servicebusNamespaceInput")
    def servicebus_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicebusNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedAccessPolicyKeyInput")
    def shared_access_policy_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedAccessPolicyKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedAccessPolicyNameInput")
    def shared_access_policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedAccessPolicyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="streamAnalyticsJobNameInput")
    def stream_analytics_job_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamAnalyticsJobNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StreamAnalyticsOutputEventhubTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StreamAnalyticsOutputEventhubTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationMode")
    def authentication_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationMode"))

    @authentication_mode.setter
    def authentication_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "authentication_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationMode", value)

    @builtins.property
    @jsii.member(jsii_name="eventhubName")
    def eventhub_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventhubName"))

    @eventhub_name.setter
    def eventhub_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "eventhub_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventhubName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="partitionKey")
    def partition_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partitionKey"))

    @partition_key.setter
    def partition_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "partition_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKey", value)

    @builtins.property
    @jsii.member(jsii_name="propertyColumns")
    def property_columns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "propertyColumns"))

    @property_columns.setter
    def property_columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "property_columns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertyColumns", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="servicebusNamespace")
    def servicebus_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicebusNamespace"))

    @servicebus_namespace.setter
    def servicebus_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "servicebus_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicebusNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedAccessPolicyKey"))

    @shared_access_policy_key.setter
    def shared_access_policy_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "shared_access_policy_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAccessPolicyKey", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedAccessPolicyName"))

    @shared_access_policy_name.setter
    def shared_access_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "shared_access_policy_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAccessPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="streamAnalyticsJobName")
    def stream_analytics_job_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamAnalyticsJobName"))

    @stream_analytics_job_name.setter
    def stream_analytics_job_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhub, "stream_analytics_job_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamAnalyticsJobName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputEventhub.StreamAnalyticsOutputEventhubConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "eventhub_name": "eventhubName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "serialization": "serialization",
        "servicebus_namespace": "servicebusNamespace",
        "shared_access_policy_key": "sharedAccessPolicyKey",
        "shared_access_policy_name": "sharedAccessPolicyName",
        "stream_analytics_job_name": "streamAnalyticsJobName",
        "authentication_mode": "authenticationMode",
        "id": "id",
        "partition_key": "partitionKey",
        "property_columns": "propertyColumns",
        "timeouts": "timeouts",
    },
)
class StreamAnalyticsOutputEventhubConfig(cdktf.TerraformMetaArguments):
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
        eventhub_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        serialization: typing.Union["StreamAnalyticsOutputEventhubSerialization", typing.Dict[str, typing.Any]],
        servicebus_namespace: builtins.str,
        shared_access_policy_key: builtins.str,
        shared_access_policy_name: builtins.str,
        stream_analytics_job_name: builtins.str,
        authentication_mode: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        partition_key: typing.Optional[builtins.str] = None,
        property_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StreamAnalyticsOutputEventhubTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param eventhub_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#eventhub_name StreamAnalyticsOutputEventhub#eventhub_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#name StreamAnalyticsOutputEventhub#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#resource_group_name StreamAnalyticsOutputEventhub#resource_group_name}.
        :param serialization: serialization block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#serialization StreamAnalyticsOutputEventhub#serialization}
        :param servicebus_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#servicebus_namespace StreamAnalyticsOutputEventhub#servicebus_namespace}.
        :param shared_access_policy_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#shared_access_policy_key StreamAnalyticsOutputEventhub#shared_access_policy_key}.
        :param shared_access_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#shared_access_policy_name StreamAnalyticsOutputEventhub#shared_access_policy_name}.
        :param stream_analytics_job_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#stream_analytics_job_name StreamAnalyticsOutputEventhub#stream_analytics_job_name}.
        :param authentication_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#authentication_mode StreamAnalyticsOutputEventhub#authentication_mode}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#id StreamAnalyticsOutputEventhub#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param partition_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#partition_key StreamAnalyticsOutputEventhub#partition_key}.
        :param property_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#property_columns StreamAnalyticsOutputEventhub#property_columns}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#timeouts StreamAnalyticsOutputEventhub#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(serialization, dict):
            serialization = StreamAnalyticsOutputEventhubSerialization(**serialization)
        if isinstance(timeouts, dict):
            timeouts = StreamAnalyticsOutputEventhubTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsOutputEventhubConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument eventhub_name", value=eventhub_name, expected_type=type_hints["eventhub_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument serialization", value=serialization, expected_type=type_hints["serialization"])
            check_type(argname="argument servicebus_namespace", value=servicebus_namespace, expected_type=type_hints["servicebus_namespace"])
            check_type(argname="argument shared_access_policy_key", value=shared_access_policy_key, expected_type=type_hints["shared_access_policy_key"])
            check_type(argname="argument shared_access_policy_name", value=shared_access_policy_name, expected_type=type_hints["shared_access_policy_name"])
            check_type(argname="argument stream_analytics_job_name", value=stream_analytics_job_name, expected_type=type_hints["stream_analytics_job_name"])
            check_type(argname="argument authentication_mode", value=authentication_mode, expected_type=type_hints["authentication_mode"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            check_type(argname="argument property_columns", value=property_columns, expected_type=type_hints["property_columns"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "eventhub_name": eventhub_name,
            "name": name,
            "resource_group_name": resource_group_name,
            "serialization": serialization,
            "servicebus_namespace": servicebus_namespace,
            "shared_access_policy_key": shared_access_policy_key,
            "shared_access_policy_name": shared_access_policy_name,
            "stream_analytics_job_name": stream_analytics_job_name,
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
        if authentication_mode is not None:
            self._values["authentication_mode"] = authentication_mode
        if id is not None:
            self._values["id"] = id
        if partition_key is not None:
            self._values["partition_key"] = partition_key
        if property_columns is not None:
            self._values["property_columns"] = property_columns
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
    def eventhub_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#eventhub_name StreamAnalyticsOutputEventhub#eventhub_name}.'''
        result = self._values.get("eventhub_name")
        assert result is not None, "Required property 'eventhub_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#name StreamAnalyticsOutputEventhub#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#resource_group_name StreamAnalyticsOutputEventhub#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def serialization(self) -> "StreamAnalyticsOutputEventhubSerialization":
        '''serialization block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#serialization StreamAnalyticsOutputEventhub#serialization}
        '''
        result = self._values.get("serialization")
        assert result is not None, "Required property 'serialization' is missing"
        return typing.cast("StreamAnalyticsOutputEventhubSerialization", result)

    @builtins.property
    def servicebus_namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#servicebus_namespace StreamAnalyticsOutputEventhub#servicebus_namespace}.'''
        result = self._values.get("servicebus_namespace")
        assert result is not None, "Required property 'servicebus_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shared_access_policy_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#shared_access_policy_key StreamAnalyticsOutputEventhub#shared_access_policy_key}.'''
        result = self._values.get("shared_access_policy_key")
        assert result is not None, "Required property 'shared_access_policy_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shared_access_policy_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#shared_access_policy_name StreamAnalyticsOutputEventhub#shared_access_policy_name}.'''
        result = self._values.get("shared_access_policy_name")
        assert result is not None, "Required property 'shared_access_policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_analytics_job_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#stream_analytics_job_name StreamAnalyticsOutputEventhub#stream_analytics_job_name}.'''
        result = self._values.get("stream_analytics_job_name")
        assert result is not None, "Required property 'stream_analytics_job_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#authentication_mode StreamAnalyticsOutputEventhub#authentication_mode}.'''
        result = self._values.get("authentication_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#id StreamAnalyticsOutputEventhub#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#partition_key StreamAnalyticsOutputEventhub#partition_key}.'''
        result = self._values.get("partition_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def property_columns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#property_columns StreamAnalyticsOutputEventhub#property_columns}.'''
        result = self._values.get("property_columns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StreamAnalyticsOutputEventhubTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#timeouts StreamAnalyticsOutputEventhub#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StreamAnalyticsOutputEventhubTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsOutputEventhubConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputEventhub.StreamAnalyticsOutputEventhubSerialization",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "encoding": "encoding",
        "field_delimiter": "fieldDelimiter",
        "format": "format",
    },
)
class StreamAnalyticsOutputEventhubSerialization:
    def __init__(
        self,
        *,
        type: builtins.str,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#type StreamAnalyticsOutputEventhub#type}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#encoding StreamAnalyticsOutputEventhub#encoding}.
        :param field_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#field_delimiter StreamAnalyticsOutputEventhub#field_delimiter}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#format StreamAnalyticsOutputEventhub#format}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsOutputEventhubSerialization.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if encoding is not None:
            self._values["encoding"] = encoding
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter
        if format is not None:
            self._values["format"] = format

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#type StreamAnalyticsOutputEventhub#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#encoding StreamAnalyticsOutputEventhub#encoding}.'''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#field_delimiter StreamAnalyticsOutputEventhub#field_delimiter}.'''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#format StreamAnalyticsOutputEventhub#format}.'''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsOutputEventhubSerialization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamAnalyticsOutputEventhubSerializationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputEventhub.StreamAnalyticsOutputEventhubSerializationOutputReference",
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
            type_hints = typing.get_type_hints(StreamAnalyticsOutputEventhubSerializationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @jsii.member(jsii_name="resetFieldDelimiter")
    def reset_field_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldDelimiter", []))

    @jsii.member(jsii_name="resetFormat")
    def reset_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormat", []))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiterInput")
    def field_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubSerializationOutputReference, "encoding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiter")
    def field_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldDelimiter"))

    @field_delimiter.setter
    def field_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubSerializationOutputReference, "field_delimiter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubSerializationOutputReference, "format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubSerializationOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StreamAnalyticsOutputEventhubSerialization]:
        return typing.cast(typing.Optional[StreamAnalyticsOutputEventhubSerialization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StreamAnalyticsOutputEventhubSerialization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubSerializationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputEventhub.StreamAnalyticsOutputEventhubTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StreamAnalyticsOutputEventhubTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#create StreamAnalyticsOutputEventhub#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#delete StreamAnalyticsOutputEventhub#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#read StreamAnalyticsOutputEventhub#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#update StreamAnalyticsOutputEventhub#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StreamAnalyticsOutputEventhubTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#create StreamAnalyticsOutputEventhub#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#delete StreamAnalyticsOutputEventhub#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#read StreamAnalyticsOutputEventhub#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/stream_analytics_output_eventhub#update StreamAnalyticsOutputEventhub#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamAnalyticsOutputEventhubTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamAnalyticsOutputEventhubTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.streamAnalyticsOutputEventhub.StreamAnalyticsOutputEventhubTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(StreamAnalyticsOutputEventhubTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StreamAnalyticsOutputEventhubTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StreamAnalyticsOutputEventhubTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StreamAnalyticsOutputEventhubTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StreamAnalyticsOutputEventhubTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StreamAnalyticsOutputEventhub",
    "StreamAnalyticsOutputEventhubConfig",
    "StreamAnalyticsOutputEventhubSerialization",
    "StreamAnalyticsOutputEventhubSerializationOutputReference",
    "StreamAnalyticsOutputEventhubTimeouts",
    "StreamAnalyticsOutputEventhubTimeoutsOutputReference",
]

publication.publish()
