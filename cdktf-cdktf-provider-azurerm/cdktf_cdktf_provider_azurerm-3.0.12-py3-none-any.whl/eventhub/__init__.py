'''
# `azurerm_eventhub`

Refer to the Terraform Registory for docs: [`azurerm_eventhub`](https://www.terraform.io/docs/providers/azurerm/r/eventhub).
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


class Eventhub(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhub.Eventhub",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub azurerm_eventhub}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        message_retention: jsii.Number,
        name: builtins.str,
        namespace_name: builtins.str,
        partition_count: jsii.Number,
        resource_group_name: builtins.str,
        capture_description: typing.Optional[typing.Union["EventhubCaptureDescription", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EventhubTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub azurerm_eventhub} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param message_retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#message_retention Eventhub#message_retention}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#name Eventhub#name}.
        :param namespace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#namespace_name Eventhub#namespace_name}.
        :param partition_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#partition_count Eventhub#partition_count}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#resource_group_name Eventhub#resource_group_name}.
        :param capture_description: capture_description block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#capture_description Eventhub#capture_description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#id Eventhub#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#status Eventhub#status}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#timeouts Eventhub#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Eventhub.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EventhubConfig(
            message_retention=message_retention,
            name=name,
            namespace_name=namespace_name,
            partition_count=partition_count,
            resource_group_name=resource_group_name,
            capture_description=capture_description,
            id=id,
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

    @jsii.member(jsii_name="putCaptureDescription")
    def put_capture_description(
        self,
        *,
        destination: typing.Union["EventhubCaptureDescriptionDestination", typing.Dict[str, typing.Any]],
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        encoding: builtins.str,
        interval_in_seconds: typing.Optional[jsii.Number] = None,
        size_limit_in_bytes: typing.Optional[jsii.Number] = None,
        skip_empty_archives: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#destination Eventhub#destination}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#enabled Eventhub#enabled}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#encoding Eventhub#encoding}.
        :param interval_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#interval_in_seconds Eventhub#interval_in_seconds}.
        :param size_limit_in_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#size_limit_in_bytes Eventhub#size_limit_in_bytes}.
        :param skip_empty_archives: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#skip_empty_archives Eventhub#skip_empty_archives}.
        '''
        value = EventhubCaptureDescription(
            destination=destination,
            enabled=enabled,
            encoding=encoding,
            interval_in_seconds=interval_in_seconds,
            size_limit_in_bytes=size_limit_in_bytes,
            skip_empty_archives=skip_empty_archives,
        )

        return typing.cast(None, jsii.invoke(self, "putCaptureDescription", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#create Eventhub#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#delete Eventhub#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#read Eventhub#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#update Eventhub#update}.
        '''
        value = EventhubTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCaptureDescription")
    def reset_capture_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaptureDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="captureDescription")
    def capture_description(self) -> "EventhubCaptureDescriptionOutputReference":
        return typing.cast("EventhubCaptureDescriptionOutputReference", jsii.get(self, "captureDescription"))

    @builtins.property
    @jsii.member(jsii_name="partitionIds")
    def partition_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "partitionIds"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EventhubTimeoutsOutputReference":
        return typing.cast("EventhubTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="captureDescriptionInput")
    def capture_description_input(
        self,
    ) -> typing.Optional["EventhubCaptureDescription"]:
        return typing.cast(typing.Optional["EventhubCaptureDescription"], jsii.get(self, "captureDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="messageRetentionInput")
    def message_retention_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "messageRetentionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceNameInput")
    def namespace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionCountInput")
    def partition_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionCountInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["EventhubTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["EventhubTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Eventhub, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="messageRetention")
    def message_retention(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "messageRetention"))

    @message_retention.setter
    def message_retention(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Eventhub, "message_retention").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageRetention", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Eventhub, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Eventhub, "namespace_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property
    @jsii.member(jsii_name="partitionCount")
    def partition_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partitionCount"))

    @partition_count.setter
    def partition_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Eventhub, "partition_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionCount", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Eventhub, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Eventhub, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhub.EventhubCaptureDescription",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "enabled": "enabled",
        "encoding": "encoding",
        "interval_in_seconds": "intervalInSeconds",
        "size_limit_in_bytes": "sizeLimitInBytes",
        "skip_empty_archives": "skipEmptyArchives",
    },
)
class EventhubCaptureDescription:
    def __init__(
        self,
        *,
        destination: typing.Union["EventhubCaptureDescriptionDestination", typing.Dict[str, typing.Any]],
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        encoding: builtins.str,
        interval_in_seconds: typing.Optional[jsii.Number] = None,
        size_limit_in_bytes: typing.Optional[jsii.Number] = None,
        skip_empty_archives: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#destination Eventhub#destination}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#enabled Eventhub#enabled}.
        :param encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#encoding Eventhub#encoding}.
        :param interval_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#interval_in_seconds Eventhub#interval_in_seconds}.
        :param size_limit_in_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#size_limit_in_bytes Eventhub#size_limit_in_bytes}.
        :param skip_empty_archives: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#skip_empty_archives Eventhub#skip_empty_archives}.
        '''
        if isinstance(destination, dict):
            destination = EventhubCaptureDescriptionDestination(**destination)
        if __debug__:
            type_hints = typing.get_type_hints(EventhubCaptureDescription.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
            check_type(argname="argument size_limit_in_bytes", value=size_limit_in_bytes, expected_type=type_hints["size_limit_in_bytes"])
            check_type(argname="argument skip_empty_archives", value=skip_empty_archives, expected_type=type_hints["skip_empty_archives"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
            "enabled": enabled,
            "encoding": encoding,
        }
        if interval_in_seconds is not None:
            self._values["interval_in_seconds"] = interval_in_seconds
        if size_limit_in_bytes is not None:
            self._values["size_limit_in_bytes"] = size_limit_in_bytes
        if skip_empty_archives is not None:
            self._values["skip_empty_archives"] = skip_empty_archives

    @builtins.property
    def destination(self) -> "EventhubCaptureDescriptionDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#destination Eventhub#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("EventhubCaptureDescriptionDestination", result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#enabled Eventhub#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def encoding(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#encoding Eventhub#encoding}.'''
        result = self._values.get("encoding")
        assert result is not None, "Required property 'encoding' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#interval_in_seconds Eventhub#interval_in_seconds}.'''
        result = self._values.get("interval_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def size_limit_in_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#size_limit_in_bytes Eventhub#size_limit_in_bytes}.'''
        result = self._values.get("size_limit_in_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def skip_empty_archives(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#skip_empty_archives Eventhub#skip_empty_archives}.'''
        result = self._values.get("skip_empty_archives")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubCaptureDescription(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhub.EventhubCaptureDescriptionDestination",
    jsii_struct_bases=[],
    name_mapping={
        "archive_name_format": "archiveNameFormat",
        "blob_container_name": "blobContainerName",
        "name": "name",
        "storage_account_id": "storageAccountId",
    },
)
class EventhubCaptureDescriptionDestination:
    def __init__(
        self,
        *,
        archive_name_format: builtins.str,
        blob_container_name: builtins.str,
        name: builtins.str,
        storage_account_id: builtins.str,
    ) -> None:
        '''
        :param archive_name_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#archive_name_format Eventhub#archive_name_format}.
        :param blob_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#blob_container_name Eventhub#blob_container_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#name Eventhub#name}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#storage_account_id Eventhub#storage_account_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubCaptureDescriptionDestination.__init__)
            check_type(argname="argument archive_name_format", value=archive_name_format, expected_type=type_hints["archive_name_format"])
            check_type(argname="argument blob_container_name", value=blob_container_name, expected_type=type_hints["blob_container_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "archive_name_format": archive_name_format,
            "blob_container_name": blob_container_name,
            "name": name,
            "storage_account_id": storage_account_id,
        }

    @builtins.property
    def archive_name_format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#archive_name_format Eventhub#archive_name_format}.'''
        result = self._values.get("archive_name_format")
        assert result is not None, "Required property 'archive_name_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def blob_container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#blob_container_name Eventhub#blob_container_name}.'''
        result = self._values.get("blob_container_name")
        assert result is not None, "Required property 'blob_container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#name Eventhub#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#storage_account_id Eventhub#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubCaptureDescriptionDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventhubCaptureDescriptionDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhub.EventhubCaptureDescriptionDestinationOutputReference",
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
            type_hints = typing.get_type_hints(EventhubCaptureDescriptionDestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="archiveNameFormatInput")
    def archive_name_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "archiveNameFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="blobContainerNameInput")
    def blob_container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blobContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveNameFormat")
    def archive_name_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "archiveNameFormat"))

    @archive_name_format.setter
    def archive_name_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionDestinationOutputReference, "archive_name_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveNameFormat", value)

    @builtins.property
    @jsii.member(jsii_name="blobContainerName")
    def blob_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobContainerName"))

    @blob_container_name.setter
    def blob_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionDestinationOutputReference, "blob_container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionDestinationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionDestinationOutputReference, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EventhubCaptureDescriptionDestination]:
        return typing.cast(typing.Optional[EventhubCaptureDescriptionDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventhubCaptureDescriptionDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventhubCaptureDescriptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhub.EventhubCaptureDescriptionOutputReference",
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
            type_hints = typing.get_type_hints(EventhubCaptureDescriptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        archive_name_format: builtins.str,
        blob_container_name: builtins.str,
        name: builtins.str,
        storage_account_id: builtins.str,
    ) -> None:
        '''
        :param archive_name_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#archive_name_format Eventhub#archive_name_format}.
        :param blob_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#blob_container_name Eventhub#blob_container_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#name Eventhub#name}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#storage_account_id Eventhub#storage_account_id}.
        '''
        value = EventhubCaptureDescriptionDestination(
            archive_name_format=archive_name_format,
            blob_container_name=blob_container_name,
            name=name,
            storage_account_id=storage_account_id,
        )

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="resetIntervalInSeconds")
    def reset_interval_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntervalInSeconds", []))

    @jsii.member(jsii_name="resetSizeLimitInBytes")
    def reset_size_limit_in_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeLimitInBytes", []))

    @jsii.member(jsii_name="resetSkipEmptyArchives")
    def reset_skip_empty_archives(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipEmptyArchives", []))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> EventhubCaptureDescriptionDestinationOutputReference:
        return typing.cast(EventhubCaptureDescriptionDestinationOutputReference, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(
        self,
    ) -> typing.Optional[EventhubCaptureDescriptionDestination]:
        return typing.cast(typing.Optional[EventhubCaptureDescriptionDestination], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInSecondsInput")
    def interval_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeLimitInBytesInput")
    def size_limit_in_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeLimitInBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="skipEmptyArchivesInput")
    def skip_empty_archives_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipEmptyArchivesInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionOutputReference, "encoding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="intervalInSeconds")
    def interval_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalInSeconds"))

    @interval_in_seconds.setter
    def interval_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionOutputReference, "interval_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="sizeLimitInBytes")
    def size_limit_in_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeLimitInBytes"))

    @size_limit_in_bytes.setter
    def size_limit_in_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionOutputReference, "size_limit_in_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeLimitInBytes", value)

    @builtins.property
    @jsii.member(jsii_name="skipEmptyArchives")
    def skip_empty_archives(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipEmptyArchives"))

    @skip_empty_archives.setter
    def skip_empty_archives(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionOutputReference, "skip_empty_archives").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipEmptyArchives", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EventhubCaptureDescription]:
        return typing.cast(typing.Optional[EventhubCaptureDescription], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventhubCaptureDescription],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubCaptureDescriptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhub.EventhubConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "message_retention": "messageRetention",
        "name": "name",
        "namespace_name": "namespaceName",
        "partition_count": "partitionCount",
        "resource_group_name": "resourceGroupName",
        "capture_description": "captureDescription",
        "id": "id",
        "status": "status",
        "timeouts": "timeouts",
    },
)
class EventhubConfig(cdktf.TerraformMetaArguments):
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
        message_retention: jsii.Number,
        name: builtins.str,
        namespace_name: builtins.str,
        partition_count: jsii.Number,
        resource_group_name: builtins.str,
        capture_description: typing.Optional[typing.Union[EventhubCaptureDescription, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EventhubTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param message_retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#message_retention Eventhub#message_retention}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#name Eventhub#name}.
        :param namespace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#namespace_name Eventhub#namespace_name}.
        :param partition_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#partition_count Eventhub#partition_count}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#resource_group_name Eventhub#resource_group_name}.
        :param capture_description: capture_description block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#capture_description Eventhub#capture_description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#id Eventhub#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#status Eventhub#status}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#timeouts Eventhub#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capture_description, dict):
            capture_description = EventhubCaptureDescription(**capture_description)
        if isinstance(timeouts, dict):
            timeouts = EventhubTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(EventhubConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument message_retention", value=message_retention, expected_type=type_hints["message_retention"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument partition_count", value=partition_count, expected_type=type_hints["partition_count"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument capture_description", value=capture_description, expected_type=type_hints["capture_description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "message_retention": message_retention,
            "name": name,
            "namespace_name": namespace_name,
            "partition_count": partition_count,
            "resource_group_name": resource_group_name,
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
        if capture_description is not None:
            self._values["capture_description"] = capture_description
        if id is not None:
            self._values["id"] = id
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
    def message_retention(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#message_retention Eventhub#message_retention}.'''
        result = self._values.get("message_retention")
        assert result is not None, "Required property 'message_retention' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#name Eventhub#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#namespace_name Eventhub#namespace_name}.'''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#partition_count Eventhub#partition_count}.'''
        result = self._values.get("partition_count")
        assert result is not None, "Required property 'partition_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#resource_group_name Eventhub#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capture_description(self) -> typing.Optional[EventhubCaptureDescription]:
        '''capture_description block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#capture_description Eventhub#capture_description}
        '''
        result = self._values.get("capture_description")
        return typing.cast(typing.Optional[EventhubCaptureDescription], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#id Eventhub#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#status Eventhub#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EventhubTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#timeouts Eventhub#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EventhubTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.eventhub.EventhubTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class EventhubTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#create Eventhub#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#delete Eventhub#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#read Eventhub#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#update Eventhub#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventhubTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#create Eventhub#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#delete Eventhub#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#read Eventhub#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/eventhub#update Eventhub#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventhubTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventhubTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.eventhub.EventhubTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(EventhubTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventhubTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventhubTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventhubTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventhubTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventhubTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Eventhub",
    "EventhubCaptureDescription",
    "EventhubCaptureDescriptionDestination",
    "EventhubCaptureDescriptionDestinationOutputReference",
    "EventhubCaptureDescriptionOutputReference",
    "EventhubConfig",
    "EventhubTimeouts",
    "EventhubTimeoutsOutputReference",
]

publication.publish()
