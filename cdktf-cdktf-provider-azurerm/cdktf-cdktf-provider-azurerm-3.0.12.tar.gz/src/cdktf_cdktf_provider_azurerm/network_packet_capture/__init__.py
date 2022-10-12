'''
# `azurerm_network_packet_capture`

Refer to the Terraform Registory for docs: [`azurerm_network_packet_capture`](https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture).
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


class NetworkPacketCapture(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCapture",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture azurerm_network_packet_capture}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        network_watcher_name: builtins.str,
        resource_group_name: builtins.str,
        storage_location: typing.Union["NetworkPacketCaptureStorageLocation", typing.Dict[str, typing.Any]],
        target_resource_id: builtins.str,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkPacketCaptureFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_bytes_per_packet: typing.Optional[jsii.Number] = None,
        maximum_bytes_per_session: typing.Optional[jsii.Number] = None,
        maximum_capture_duration: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["NetworkPacketCaptureTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture azurerm_network_packet_capture} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#name NetworkPacketCapture#name}.
        :param network_watcher_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#network_watcher_name NetworkPacketCapture#network_watcher_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#resource_group_name NetworkPacketCapture#resource_group_name}.
        :param storage_location: storage_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#storage_location NetworkPacketCapture#storage_location}
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#target_resource_id NetworkPacketCapture#target_resource_id}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#filter NetworkPacketCapture#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#id NetworkPacketCapture#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_bytes_per_packet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_bytes_per_packet NetworkPacketCapture#maximum_bytes_per_packet}.
        :param maximum_bytes_per_session: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_bytes_per_session NetworkPacketCapture#maximum_bytes_per_session}.
        :param maximum_capture_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_capture_duration NetworkPacketCapture#maximum_capture_duration}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#timeouts NetworkPacketCapture#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPacketCapture.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkPacketCaptureConfig(
            name=name,
            network_watcher_name=network_watcher_name,
            resource_group_name=resource_group_name,
            storage_location=storage_location,
            target_resource_id=target_resource_id,
            filter=filter,
            id=id,
            maximum_bytes_per_packet=maximum_bytes_per_packet,
            maximum_bytes_per_session=maximum_bytes_per_session,
            maximum_capture_duration=maximum_capture_duration,
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

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkPacketCaptureFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPacketCapture.put_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putStorageLocation")
    def put_storage_location(
        self,
        *,
        file_path: typing.Optional[builtins.str] = None,
        storage_account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#file_path NetworkPacketCapture#file_path}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#storage_account_id NetworkPacketCapture#storage_account_id}.
        '''
        value = NetworkPacketCaptureStorageLocation(
            file_path=file_path, storage_account_id=storage_account_id
        )

        return typing.cast(None, jsii.invoke(self, "putStorageLocation", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#create NetworkPacketCapture#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#delete NetworkPacketCapture#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#read NetworkPacketCapture#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#update NetworkPacketCapture#update}.
        '''
        value = NetworkPacketCaptureTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaximumBytesPerPacket")
    def reset_maximum_bytes_per_packet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBytesPerPacket", []))

    @jsii.member(jsii_name="resetMaximumBytesPerSession")
    def reset_maximum_bytes_per_session(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBytesPerSession", []))

    @jsii.member(jsii_name="resetMaximumCaptureDuration")
    def reset_maximum_capture_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumCaptureDuration", []))

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
    @jsii.member(jsii_name="filter")
    def filter(self) -> "NetworkPacketCaptureFilterList":
        return typing.cast("NetworkPacketCaptureFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="storageLocation")
    def storage_location(self) -> "NetworkPacketCaptureStorageLocationOutputReference":
        return typing.cast("NetworkPacketCaptureStorageLocationOutputReference", jsii.get(self, "storageLocation"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "NetworkPacketCaptureTimeoutsOutputReference":
        return typing.cast("NetworkPacketCaptureTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkPacketCaptureFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkPacketCaptureFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBytesPerPacketInput")
    def maximum_bytes_per_packet_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBytesPerPacketInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBytesPerSessionInput")
    def maximum_bytes_per_session_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBytesPerSessionInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumCaptureDurationInput")
    def maximum_capture_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumCaptureDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkWatcherNameInput")
    def network_watcher_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkWatcherNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageLocationInput")
    def storage_location_input(
        self,
    ) -> typing.Optional["NetworkPacketCaptureStorageLocation"]:
        return typing.cast(typing.Optional["NetworkPacketCaptureStorageLocation"], jsii.get(self, "storageLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceIdInput")
    def target_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["NetworkPacketCaptureTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetworkPacketCaptureTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCapture, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maximumBytesPerPacket")
    def maximum_bytes_per_packet(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBytesPerPacket"))

    @maximum_bytes_per_packet.setter
    def maximum_bytes_per_packet(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCapture, "maximum_bytes_per_packet").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBytesPerPacket", value)

    @builtins.property
    @jsii.member(jsii_name="maximumBytesPerSession")
    def maximum_bytes_per_session(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBytesPerSession"))

    @maximum_bytes_per_session.setter
    def maximum_bytes_per_session(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCapture, "maximum_bytes_per_session").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBytesPerSession", value)

    @builtins.property
    @jsii.member(jsii_name="maximumCaptureDuration")
    def maximum_capture_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumCaptureDuration"))

    @maximum_capture_duration.setter
    def maximum_capture_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCapture, "maximum_capture_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCaptureDuration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCapture, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkWatcherName")
    def network_watcher_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkWatcherName"))

    @network_watcher_name.setter
    def network_watcher_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCapture, "network_watcher_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkWatcherName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCapture, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceId")
    def target_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetResourceId"))

    @target_resource_id.setter
    def target_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCapture, "target_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCaptureConfig",
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
        "network_watcher_name": "networkWatcherName",
        "resource_group_name": "resourceGroupName",
        "storage_location": "storageLocation",
        "target_resource_id": "targetResourceId",
        "filter": "filter",
        "id": "id",
        "maximum_bytes_per_packet": "maximumBytesPerPacket",
        "maximum_bytes_per_session": "maximumBytesPerSession",
        "maximum_capture_duration": "maximumCaptureDuration",
        "timeouts": "timeouts",
    },
)
class NetworkPacketCaptureConfig(cdktf.TerraformMetaArguments):
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
        network_watcher_name: builtins.str,
        resource_group_name: builtins.str,
        storage_location: typing.Union["NetworkPacketCaptureStorageLocation", typing.Dict[str, typing.Any]],
        target_resource_id: builtins.str,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkPacketCaptureFilter", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_bytes_per_packet: typing.Optional[jsii.Number] = None,
        maximum_bytes_per_session: typing.Optional[jsii.Number] = None,
        maximum_capture_duration: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["NetworkPacketCaptureTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#name NetworkPacketCapture#name}.
        :param network_watcher_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#network_watcher_name NetworkPacketCapture#network_watcher_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#resource_group_name NetworkPacketCapture#resource_group_name}.
        :param storage_location: storage_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#storage_location NetworkPacketCapture#storage_location}
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#target_resource_id NetworkPacketCapture#target_resource_id}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#filter NetworkPacketCapture#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#id NetworkPacketCapture#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_bytes_per_packet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_bytes_per_packet NetworkPacketCapture#maximum_bytes_per_packet}.
        :param maximum_bytes_per_session: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_bytes_per_session NetworkPacketCapture#maximum_bytes_per_session}.
        :param maximum_capture_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_capture_duration NetworkPacketCapture#maximum_capture_duration}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#timeouts NetworkPacketCapture#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage_location, dict):
            storage_location = NetworkPacketCaptureStorageLocation(**storage_location)
        if isinstance(timeouts, dict):
            timeouts = NetworkPacketCaptureTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPacketCaptureConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_watcher_name", value=network_watcher_name, expected_type=type_hints["network_watcher_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument storage_location", value=storage_location, expected_type=type_hints["storage_location"])
            check_type(argname="argument target_resource_id", value=target_resource_id, expected_type=type_hints["target_resource_id"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maximum_bytes_per_packet", value=maximum_bytes_per_packet, expected_type=type_hints["maximum_bytes_per_packet"])
            check_type(argname="argument maximum_bytes_per_session", value=maximum_bytes_per_session, expected_type=type_hints["maximum_bytes_per_session"])
            check_type(argname="argument maximum_capture_duration", value=maximum_capture_duration, expected_type=type_hints["maximum_capture_duration"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "network_watcher_name": network_watcher_name,
            "resource_group_name": resource_group_name,
            "storage_location": storage_location,
            "target_resource_id": target_resource_id,
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
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if maximum_bytes_per_packet is not None:
            self._values["maximum_bytes_per_packet"] = maximum_bytes_per_packet
        if maximum_bytes_per_session is not None:
            self._values["maximum_bytes_per_session"] = maximum_bytes_per_session
        if maximum_capture_duration is not None:
            self._values["maximum_capture_duration"] = maximum_capture_duration
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#name NetworkPacketCapture#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_watcher_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#network_watcher_name NetworkPacketCapture#network_watcher_name}.'''
        result = self._values.get("network_watcher_name")
        assert result is not None, "Required property 'network_watcher_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#resource_group_name NetworkPacketCapture#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_location(self) -> "NetworkPacketCaptureStorageLocation":
        '''storage_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#storage_location NetworkPacketCapture#storage_location}
        '''
        result = self._values.get("storage_location")
        assert result is not None, "Required property 'storage_location' is missing"
        return typing.cast("NetworkPacketCaptureStorageLocation", result)

    @builtins.property
    def target_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#target_resource_id NetworkPacketCapture#target_resource_id}.'''
        result = self._values.get("target_resource_id")
        assert result is not None, "Required property 'target_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkPacketCaptureFilter"]]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#filter NetworkPacketCapture#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkPacketCaptureFilter"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#id NetworkPacketCapture#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_bytes_per_packet(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_bytes_per_packet NetworkPacketCapture#maximum_bytes_per_packet}.'''
        result = self._values.get("maximum_bytes_per_packet")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_bytes_per_session(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_bytes_per_session NetworkPacketCapture#maximum_bytes_per_session}.'''
        result = self._values.get("maximum_bytes_per_session")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_capture_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#maximum_capture_duration NetworkPacketCapture#maximum_capture_duration}.'''
        result = self._values.get("maximum_capture_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetworkPacketCaptureTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#timeouts NetworkPacketCapture#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetworkPacketCaptureTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPacketCaptureConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCaptureFilter",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "local_ip_address": "localIpAddress",
        "local_port": "localPort",
        "remote_ip_address": "remoteIpAddress",
        "remote_port": "remotePort",
    },
)
class NetworkPacketCaptureFilter:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        local_ip_address: typing.Optional[builtins.str] = None,
        local_port: typing.Optional[builtins.str] = None,
        remote_ip_address: typing.Optional[builtins.str] = None,
        remote_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#protocol NetworkPacketCapture#protocol}.
        :param local_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#local_ip_address NetworkPacketCapture#local_ip_address}.
        :param local_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#local_port NetworkPacketCapture#local_port}.
        :param remote_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#remote_ip_address NetworkPacketCapture#remote_ip_address}.
        :param remote_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#remote_port NetworkPacketCapture#remote_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPacketCaptureFilter.__init__)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument local_ip_address", value=local_ip_address, expected_type=type_hints["local_ip_address"])
            check_type(argname="argument local_port", value=local_port, expected_type=type_hints["local_port"])
            check_type(argname="argument remote_ip_address", value=remote_ip_address, expected_type=type_hints["remote_ip_address"])
            check_type(argname="argument remote_port", value=remote_port, expected_type=type_hints["remote_port"])
        self._values: typing.Dict[str, typing.Any] = {
            "protocol": protocol,
        }
        if local_ip_address is not None:
            self._values["local_ip_address"] = local_ip_address
        if local_port is not None:
            self._values["local_port"] = local_port
        if remote_ip_address is not None:
            self._values["remote_ip_address"] = remote_ip_address
        if remote_port is not None:
            self._values["remote_port"] = remote_port

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#protocol NetworkPacketCapture#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def local_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#local_ip_address NetworkPacketCapture#local_ip_address}.'''
        result = self._values.get("local_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_port(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#local_port NetworkPacketCapture#local_port}.'''
        result = self._values.get("local_port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#remote_ip_address NetworkPacketCapture#remote_ip_address}.'''
        result = self._values.get("remote_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_port(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#remote_port NetworkPacketCapture#remote_port}.'''
        result = self._values.get("remote_port")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPacketCaptureFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPacketCaptureFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCaptureFilterList",
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
            type_hints = typing.get_type_hints(NetworkPacketCaptureFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkPacketCaptureFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPacketCaptureFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPacketCaptureFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkPacketCaptureFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkPacketCaptureFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkPacketCaptureFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPacketCaptureFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCaptureFilterOutputReference",
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
            type_hints = typing.get_type_hints(NetworkPacketCaptureFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetLocalIpAddress")
    def reset_local_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalIpAddress", []))

    @jsii.member(jsii_name="resetLocalPort")
    def reset_local_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalPort", []))

    @jsii.member(jsii_name="resetRemoteIpAddress")
    def reset_remote_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteIpAddress", []))

    @jsii.member(jsii_name="resetRemotePort")
    def reset_remote_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemotePort", []))

    @builtins.property
    @jsii.member(jsii_name="localIpAddressInput")
    def local_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="localPortInput")
    def local_port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localPortInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteIpAddressInput")
    def remote_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="remotePortInput")
    def remote_port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remotePortInput"))

    @builtins.property
    @jsii.member(jsii_name="localIpAddress")
    def local_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localIpAddress"))

    @local_ip_address.setter
    def local_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterOutputReference, "local_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="localPort")
    def local_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localPort"))

    @local_port.setter
    def local_port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterOutputReference, "local_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localPort", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="remoteIpAddress")
    def remote_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteIpAddress"))

    @remote_ip_address.setter
    def remote_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterOutputReference, "remote_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="remotePort")
    def remote_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remotePort"))

    @remote_port.setter
    def remote_port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterOutputReference, "remote_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remotePort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPacketCaptureFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPacketCaptureFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPacketCaptureFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCaptureStorageLocation",
    jsii_struct_bases=[],
    name_mapping={"file_path": "filePath", "storage_account_id": "storageAccountId"},
)
class NetworkPacketCaptureStorageLocation:
    def __init__(
        self,
        *,
        file_path: typing.Optional[builtins.str] = None,
        storage_account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#file_path NetworkPacketCapture#file_path}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#storage_account_id NetworkPacketCapture#storage_account_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPacketCaptureStorageLocation.__init__)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if file_path is not None:
            self._values["file_path"] = file_path
        if storage_account_id is not None:
            self._values["storage_account_id"] = storage_account_id

    @builtins.property
    def file_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#file_path NetworkPacketCapture#file_path}.'''
        result = self._values.get("file_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#storage_account_id NetworkPacketCapture#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPacketCaptureStorageLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPacketCaptureStorageLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCaptureStorageLocationOutputReference",
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
            type_hints = typing.get_type_hints(NetworkPacketCaptureStorageLocationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFilePath")
    def reset_file_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilePath", []))

    @jsii.member(jsii_name="resetStorageAccountId")
    def reset_storage_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="storagePath")
    def storage_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storagePath"))

    @builtins.property
    @jsii.member(jsii_name="filePathInput")
    def file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filePathInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="filePath")
    def file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filePath"))

    @file_path.setter
    def file_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureStorageLocationOutputReference, "file_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filePath", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureStorageLocationOutputReference, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkPacketCaptureStorageLocation]:
        return typing.cast(typing.Optional[NetworkPacketCaptureStorageLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkPacketCaptureStorageLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureStorageLocationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCaptureTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class NetworkPacketCaptureTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#create NetworkPacketCapture#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#delete NetworkPacketCapture#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#read NetworkPacketCapture#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#update NetworkPacketCapture#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkPacketCaptureTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#create NetworkPacketCapture#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#delete NetworkPacketCapture#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#read NetworkPacketCapture#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_packet_capture#update NetworkPacketCapture#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPacketCaptureTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPacketCaptureTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkPacketCapture.NetworkPacketCaptureTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkPacketCaptureTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPacketCaptureTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPacketCaptureTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPacketCaptureTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkPacketCaptureTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkPacketCapture",
    "NetworkPacketCaptureConfig",
    "NetworkPacketCaptureFilter",
    "NetworkPacketCaptureFilterList",
    "NetworkPacketCaptureFilterOutputReference",
    "NetworkPacketCaptureStorageLocation",
    "NetworkPacketCaptureStorageLocationOutputReference",
    "NetworkPacketCaptureTimeouts",
    "NetworkPacketCaptureTimeoutsOutputReference",
]

publication.publish()
