'''
# `azurerm_network_connection_monitor`

Refer to the Terraform Registory for docs: [`azurerm_network_connection_monitor`](https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor).
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


class NetworkConnectionMonitor(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor azurerm_network_connection_monitor}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        endpoint: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorEndpoint", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        network_watcher_id: builtins.str,
        test_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorTestConfiguration", typing.Dict[str, typing.Any]]]],
        test_group: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorTestGroup", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        output_workspace_resource_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetworkConnectionMonitorTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor azurerm_network_connection_monitor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#endpoint NetworkConnectionMonitor#endpoint}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#location NetworkConnectionMonitor#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.
        :param network_watcher_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#network_watcher_id NetworkConnectionMonitor#network_watcher_id}.
        :param test_configuration: test_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_configuration NetworkConnectionMonitor#test_configuration}
        :param test_group: test_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_group NetworkConnectionMonitor#test_group}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#id NetworkConnectionMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#notes NetworkConnectionMonitor#notes}.
        :param output_workspace_resource_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#output_workspace_resource_ids NetworkConnectionMonitor#output_workspace_resource_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#tags NetworkConnectionMonitor#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#timeouts NetworkConnectionMonitor#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitor.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkConnectionMonitorConfig(
            endpoint=endpoint,
            location=location,
            name=name,
            network_watcher_id=network_watcher_id,
            test_configuration=test_configuration,
            test_group=test_group,
            id=id,
            notes=notes,
            output_workspace_resource_ids=output_workspace_resource_ids,
            tags=tags,
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

    @jsii.member(jsii_name="putEndpoint")
    def put_endpoint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorEndpoint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitor.put_endpoint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEndpoint", [value]))

    @jsii.member(jsii_name="putTestConfiguration")
    def put_test_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorTestConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitor.put_test_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTestConfiguration", [value]))

    @jsii.member(jsii_name="putTestGroup")
    def put_test_group(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorTestGroup", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitor.put_test_group)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTestGroup", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#create NetworkConnectionMonitor#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#delete NetworkConnectionMonitor#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#read NetworkConnectionMonitor#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#update NetworkConnectionMonitor#update}.
        '''
        value = NetworkConnectionMonitorTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotes")
    def reset_notes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotes", []))

    @jsii.member(jsii_name="resetOutputWorkspaceResourceIds")
    def reset_output_workspace_resource_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputWorkspaceResourceIds", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> "NetworkConnectionMonitorEndpointList":
        return typing.cast("NetworkConnectionMonitorEndpointList", jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="testConfiguration")
    def test_configuration(self) -> "NetworkConnectionMonitorTestConfigurationList":
        return typing.cast("NetworkConnectionMonitorTestConfigurationList", jsii.get(self, "testConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="testGroup")
    def test_group(self) -> "NetworkConnectionMonitorTestGroupList":
        return typing.cast("NetworkConnectionMonitorTestGroupList", jsii.get(self, "testGroup"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "NetworkConnectionMonitorTimeoutsOutputReference":
        return typing.cast("NetworkConnectionMonitorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorEndpoint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorEndpoint"]]], jsii.get(self, "endpointInput"))

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
    @jsii.member(jsii_name="networkWatcherIdInput")
    def network_watcher_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkWatcherIdInput"))

    @builtins.property
    @jsii.member(jsii_name="notesInput")
    def notes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notesInput"))

    @builtins.property
    @jsii.member(jsii_name="outputWorkspaceResourceIdsInput")
    def output_workspace_resource_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "outputWorkspaceResourceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="testConfigurationInput")
    def test_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestConfiguration"]]], jsii.get(self, "testConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="testGroupInput")
    def test_group_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestGroup"]]], jsii.get(self, "testGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["NetworkConnectionMonitorTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetworkConnectionMonitorTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitor, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitor, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitor, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkWatcherId")
    def network_watcher_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkWatcherId"))

    @network_watcher_id.setter
    def network_watcher_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitor, "network_watcher_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkWatcherId", value)

    @builtins.property
    @jsii.member(jsii_name="notes")
    def notes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notes"))

    @notes.setter
    def notes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitor, "notes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notes", value)

    @builtins.property
    @jsii.member(jsii_name="outputWorkspaceResourceIds")
    def output_workspace_resource_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "outputWorkspaceResourceIds"))

    @output_workspace_resource_ids.setter
    def output_workspace_resource_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitor, "output_workspace_resource_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputWorkspaceResourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitor, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "endpoint": "endpoint",
        "location": "location",
        "name": "name",
        "network_watcher_id": "networkWatcherId",
        "test_configuration": "testConfiguration",
        "test_group": "testGroup",
        "id": "id",
        "notes": "notes",
        "output_workspace_resource_ids": "outputWorkspaceResourceIds",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class NetworkConnectionMonitorConfig(cdktf.TerraformMetaArguments):
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
        endpoint: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorEndpoint", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        network_watcher_id: builtins.str,
        test_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorTestConfiguration", typing.Dict[str, typing.Any]]]],
        test_group: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorTestGroup", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        output_workspace_resource_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetworkConnectionMonitorTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#endpoint NetworkConnectionMonitor#endpoint}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#location NetworkConnectionMonitor#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.
        :param network_watcher_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#network_watcher_id NetworkConnectionMonitor#network_watcher_id}.
        :param test_configuration: test_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_configuration NetworkConnectionMonitor#test_configuration}
        :param test_group: test_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_group NetworkConnectionMonitor#test_group}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#id NetworkConnectionMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#notes NetworkConnectionMonitor#notes}.
        :param output_workspace_resource_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#output_workspace_resource_ids NetworkConnectionMonitor#output_workspace_resource_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#tags NetworkConnectionMonitor#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#timeouts NetworkConnectionMonitor#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = NetworkConnectionMonitorTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_watcher_id", value=network_watcher_id, expected_type=type_hints["network_watcher_id"])
            check_type(argname="argument test_configuration", value=test_configuration, expected_type=type_hints["test_configuration"])
            check_type(argname="argument test_group", value=test_group, expected_type=type_hints["test_group"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notes", value=notes, expected_type=type_hints["notes"])
            check_type(argname="argument output_workspace_resource_ids", value=output_workspace_resource_ids, expected_type=type_hints["output_workspace_resource_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
            "location": location,
            "name": name,
            "network_watcher_id": network_watcher_id,
            "test_configuration": test_configuration,
            "test_group": test_group,
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
        if notes is not None:
            self._values["notes"] = notes
        if output_workspace_resource_ids is not None:
            self._values["output_workspace_resource_ids"] = output_workspace_resource_ids
        if tags is not None:
            self._values["tags"] = tags
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
    def endpoint(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorEndpoint"]]:
        '''endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#endpoint NetworkConnectionMonitor#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorEndpoint"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#location NetworkConnectionMonitor#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_watcher_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#network_watcher_id NetworkConnectionMonitor#network_watcher_id}.'''
        result = self._values.get("network_watcher_id")
        assert result is not None, "Required property 'network_watcher_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def test_configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestConfiguration"]]:
        '''test_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_configuration NetworkConnectionMonitor#test_configuration}
        '''
        result = self._values.get("test_configuration")
        assert result is not None, "Required property 'test_configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestConfiguration"]], result)

    @builtins.property
    def test_group(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestGroup"]]:
        '''test_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_group NetworkConnectionMonitor#test_group}
        '''
        result = self._values.get("test_group")
        assert result is not None, "Required property 'test_group' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestGroup"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#id NetworkConnectionMonitor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#notes NetworkConnectionMonitor#notes}.'''
        result = self._values.get("notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_workspace_resource_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#output_workspace_resource_ids NetworkConnectionMonitor#output_workspace_resource_ids}.'''
        result = self._values.get("output_workspace_resource_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#tags NetworkConnectionMonitor#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetworkConnectionMonitorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#timeouts NetworkConnectionMonitor#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetworkConnectionMonitorTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "address": "address",
        "coverage_level": "coverageLevel",
        "excluded_ip_addresses": "excludedIpAddresses",
        "filter": "filter",
        "included_ip_addresses": "includedIpAddresses",
        "target_resource_id": "targetResourceId",
        "target_resource_type": "targetResourceType",
    },
)
class NetworkConnectionMonitorEndpoint:
    def __init__(
        self,
        *,
        name: builtins.str,
        address: typing.Optional[builtins.str] = None,
        coverage_level: typing.Optional[builtins.str] = None,
        excluded_ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        filter: typing.Optional[typing.Union["NetworkConnectionMonitorEndpointFilter", typing.Dict[str, typing.Any]]] = None,
        included_ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_resource_id: typing.Optional[builtins.str] = None,
        target_resource_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#address NetworkConnectionMonitor#address}.
        :param coverage_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#coverage_level NetworkConnectionMonitor#coverage_level}.
        :param excluded_ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#excluded_ip_addresses NetworkConnectionMonitor#excluded_ip_addresses}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#filter NetworkConnectionMonitor#filter}
        :param included_ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#included_ip_addresses NetworkConnectionMonitor#included_ip_addresses}.
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#target_resource_id NetworkConnectionMonitor#target_resource_id}.
        :param target_resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#target_resource_type NetworkConnectionMonitor#target_resource_type}.
        '''
        if isinstance(filter, dict):
            filter = NetworkConnectionMonitorEndpointFilter(**filter)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpoint.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument coverage_level", value=coverage_level, expected_type=type_hints["coverage_level"])
            check_type(argname="argument excluded_ip_addresses", value=excluded_ip_addresses, expected_type=type_hints["excluded_ip_addresses"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument included_ip_addresses", value=included_ip_addresses, expected_type=type_hints["included_ip_addresses"])
            check_type(argname="argument target_resource_id", value=target_resource_id, expected_type=type_hints["target_resource_id"])
            check_type(argname="argument target_resource_type", value=target_resource_type, expected_type=type_hints["target_resource_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if address is not None:
            self._values["address"] = address
        if coverage_level is not None:
            self._values["coverage_level"] = coverage_level
        if excluded_ip_addresses is not None:
            self._values["excluded_ip_addresses"] = excluded_ip_addresses
        if filter is not None:
            self._values["filter"] = filter
        if included_ip_addresses is not None:
            self._values["included_ip_addresses"] = included_ip_addresses
        if target_resource_id is not None:
            self._values["target_resource_id"] = target_resource_id
        if target_resource_type is not None:
            self._values["target_resource_type"] = target_resource_type

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#address NetworkConnectionMonitor#address}.'''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def coverage_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#coverage_level NetworkConnectionMonitor#coverage_level}.'''
        result = self._values.get("coverage_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def excluded_ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#excluded_ip_addresses NetworkConnectionMonitor#excluded_ip_addresses}.'''
        result = self._values.get("excluded_ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def filter(self) -> typing.Optional["NetworkConnectionMonitorEndpointFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#filter NetworkConnectionMonitor#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["NetworkConnectionMonitorEndpointFilter"], result)

    @builtins.property
    def included_ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#included_ip_addresses NetworkConnectionMonitor#included_ip_addresses}.'''
        result = self._values.get("included_ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#target_resource_id NetworkConnectionMonitor#target_resource_id}.'''
        result = self._values.get("target_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_resource_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#target_resource_type NetworkConnectionMonitor#target_resource_type}.'''
        result = self._values.get("target_resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorEndpointFilter",
    jsii_struct_bases=[],
    name_mapping={"item": "item", "type": "type"},
)
class NetworkConnectionMonitorEndpointFilter:
    def __init__(
        self,
        *,
        item: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorEndpointFilterItem", typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param item: item block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#item NetworkConnectionMonitor#item}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#type NetworkConnectionMonitor#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointFilter.__init__)
            check_type(argname="argument item", value=item, expected_type=type_hints["item"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if item is not None:
            self._values["item"] = item
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def item(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorEndpointFilterItem"]]]:
        '''item block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#item NetworkConnectionMonitor#item}
        '''
        result = self._values.get("item")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorEndpointFilterItem"]]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#type NetworkConnectionMonitor#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorEndpointFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorEndpointFilterItem",
    jsii_struct_bases=[],
    name_mapping={"address": "address", "type": "type"},
)
class NetworkConnectionMonitorEndpointFilterItem:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#address NetworkConnectionMonitor#address}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#type NetworkConnectionMonitor#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointFilterItem.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#address NetworkConnectionMonitor#address}.'''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#type NetworkConnectionMonitor#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorEndpointFilterItem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectionMonitorEndpointFilterItemList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorEndpointFilterItemList",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointFilterItemList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkConnectionMonitorEndpointFilterItemOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointFilterItemList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkConnectionMonitorEndpointFilterItemOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterItemList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterItemList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterItemList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorEndpointFilterItem]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorEndpointFilterItem]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorEndpointFilterItem]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterItemList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectionMonitorEndpointFilterItemOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorEndpointFilterItemOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointFilterItemOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterItemOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterItemOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkConnectionMonitorEndpointFilterItem, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkConnectionMonitorEndpointFilterItem, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkConnectionMonitorEndpointFilterItem, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterItemOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectionMonitorEndpointFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorEndpointFilterOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putItem")
    def put_item(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[NetworkConnectionMonitorEndpointFilterItem, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointFilterOutputReference.put_item)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItem", [value]))

    @jsii.member(jsii_name="resetItem")
    def reset_item(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItem", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="item")
    def item(self) -> NetworkConnectionMonitorEndpointFilterItemList:
        return typing.cast(NetworkConnectionMonitorEndpointFilterItemList, jsii.get(self, "item"))

    @builtins.property
    @jsii.member(jsii_name="itemInput")
    def item_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorEndpointFilterItem]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorEndpointFilterItem]]], jsii.get(self, "itemInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkConnectionMonitorEndpointFilter]:
        return typing.cast(typing.Optional[NetworkConnectionMonitorEndpointFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkConnectionMonitorEndpointFilter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectionMonitorEndpointList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorEndpointList",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkConnectionMonitorEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkConnectionMonitorEndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorEndpoint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorEndpoint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorEndpoint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectionMonitorEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorEndpointOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        item: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[NetworkConnectionMonitorEndpointFilterItem, typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param item: item block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#item NetworkConnectionMonitor#item}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#type NetworkConnectionMonitor#type}.
        '''
        value = NetworkConnectionMonitorEndpointFilter(item=item, type=type)

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetCoverageLevel")
    def reset_coverage_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoverageLevel", []))

    @jsii.member(jsii_name="resetExcludedIpAddresses")
    def reset_excluded_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedIpAddresses", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetIncludedIpAddresses")
    def reset_included_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedIpAddresses", []))

    @jsii.member(jsii_name="resetTargetResourceId")
    def reset_target_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResourceId", []))

    @jsii.member(jsii_name="resetTargetResourceType")
    def reset_target_resource_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResourceType", []))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> NetworkConnectionMonitorEndpointFilterOutputReference:
        return typing.cast(NetworkConnectionMonitorEndpointFilterOutputReference, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="coverageLevelInput")
    def coverage_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coverageLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedIpAddressesInput")
    def excluded_ip_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedIpAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[NetworkConnectionMonitorEndpointFilter]:
        return typing.cast(typing.Optional[NetworkConnectionMonitorEndpointFilter], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="includedIpAddressesInput")
    def included_ip_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedIpAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceIdInput")
    def target_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceTypeInput")
    def target_resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetResourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="coverageLevel")
    def coverage_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coverageLevel"))

    @coverage_level.setter
    def coverage_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointOutputReference, "coverage_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coverageLevel", value)

    @builtins.property
    @jsii.member(jsii_name="excludedIpAddresses")
    def excluded_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedIpAddresses"))

    @excluded_ip_addresses.setter
    def excluded_ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointOutputReference, "excluded_ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedIpAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="includedIpAddresses")
    def included_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedIpAddresses"))

    @included_ip_addresses.setter
    def included_ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointOutputReference, "included_ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedIpAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceId")
    def target_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetResourceId"))

    @target_resource_id.setter
    def target_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointOutputReference, "target_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceType")
    def target_resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetResourceType"))

    @target_resource_type.setter
    def target_resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointOutputReference, "target_resource_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkConnectionMonitorEndpoint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkConnectionMonitorEndpoint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkConnectionMonitorEndpoint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "protocol": "protocol",
        "http_configuration": "httpConfiguration",
        "icmp_configuration": "icmpConfiguration",
        "preferred_ip_version": "preferredIpVersion",
        "success_threshold": "successThreshold",
        "tcp_configuration": "tcpConfiguration",
        "test_frequency_in_seconds": "testFrequencyInSeconds",
    },
)
class NetworkConnectionMonitorTestConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        protocol: builtins.str,
        http_configuration: typing.Optional[typing.Union["NetworkConnectionMonitorTestConfigurationHttpConfiguration", typing.Dict[str, typing.Any]]] = None,
        icmp_configuration: typing.Optional[typing.Union["NetworkConnectionMonitorTestConfigurationIcmpConfiguration", typing.Dict[str, typing.Any]]] = None,
        preferred_ip_version: typing.Optional[builtins.str] = None,
        success_threshold: typing.Optional[typing.Union["NetworkConnectionMonitorTestConfigurationSuccessThreshold", typing.Dict[str, typing.Any]]] = None,
        tcp_configuration: typing.Optional[typing.Union["NetworkConnectionMonitorTestConfigurationTcpConfiguration", typing.Dict[str, typing.Any]]] = None,
        test_frequency_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#protocol NetworkConnectionMonitor#protocol}.
        :param http_configuration: http_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#http_configuration NetworkConnectionMonitor#http_configuration}
        :param icmp_configuration: icmp_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#icmp_configuration NetworkConnectionMonitor#icmp_configuration}
        :param preferred_ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#preferred_ip_version NetworkConnectionMonitor#preferred_ip_version}.
        :param success_threshold: success_threshold block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#success_threshold NetworkConnectionMonitor#success_threshold}
        :param tcp_configuration: tcp_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#tcp_configuration NetworkConnectionMonitor#tcp_configuration}
        :param test_frequency_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_frequency_in_seconds NetworkConnectionMonitor#test_frequency_in_seconds}.
        '''
        if isinstance(http_configuration, dict):
            http_configuration = NetworkConnectionMonitorTestConfigurationHttpConfiguration(**http_configuration)
        if isinstance(icmp_configuration, dict):
            icmp_configuration = NetworkConnectionMonitorTestConfigurationIcmpConfiguration(**icmp_configuration)
        if isinstance(success_threshold, dict):
            success_threshold = NetworkConnectionMonitorTestConfigurationSuccessThreshold(**success_threshold)
        if isinstance(tcp_configuration, dict):
            tcp_configuration = NetworkConnectionMonitorTestConfigurationTcpConfiguration(**tcp_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument http_configuration", value=http_configuration, expected_type=type_hints["http_configuration"])
            check_type(argname="argument icmp_configuration", value=icmp_configuration, expected_type=type_hints["icmp_configuration"])
            check_type(argname="argument preferred_ip_version", value=preferred_ip_version, expected_type=type_hints["preferred_ip_version"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument tcp_configuration", value=tcp_configuration, expected_type=type_hints["tcp_configuration"])
            check_type(argname="argument test_frequency_in_seconds", value=test_frequency_in_seconds, expected_type=type_hints["test_frequency_in_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "protocol": protocol,
        }
        if http_configuration is not None:
            self._values["http_configuration"] = http_configuration
        if icmp_configuration is not None:
            self._values["icmp_configuration"] = icmp_configuration
        if preferred_ip_version is not None:
            self._values["preferred_ip_version"] = preferred_ip_version
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if tcp_configuration is not None:
            self._values["tcp_configuration"] = tcp_configuration
        if test_frequency_in_seconds is not None:
            self._values["test_frequency_in_seconds"] = test_frequency_in_seconds

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#protocol NetworkConnectionMonitor#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_configuration(
        self,
    ) -> typing.Optional["NetworkConnectionMonitorTestConfigurationHttpConfiguration"]:
        '''http_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#http_configuration NetworkConnectionMonitor#http_configuration}
        '''
        result = self._values.get("http_configuration")
        return typing.cast(typing.Optional["NetworkConnectionMonitorTestConfigurationHttpConfiguration"], result)

    @builtins.property
    def icmp_configuration(
        self,
    ) -> typing.Optional["NetworkConnectionMonitorTestConfigurationIcmpConfiguration"]:
        '''icmp_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#icmp_configuration NetworkConnectionMonitor#icmp_configuration}
        '''
        result = self._values.get("icmp_configuration")
        return typing.cast(typing.Optional["NetworkConnectionMonitorTestConfigurationIcmpConfiguration"], result)

    @builtins.property
    def preferred_ip_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#preferred_ip_version NetworkConnectionMonitor#preferred_ip_version}.'''
        result = self._values.get("preferred_ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_threshold(
        self,
    ) -> typing.Optional["NetworkConnectionMonitorTestConfigurationSuccessThreshold"]:
        '''success_threshold block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#success_threshold NetworkConnectionMonitor#success_threshold}
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional["NetworkConnectionMonitorTestConfigurationSuccessThreshold"], result)

    @builtins.property
    def tcp_configuration(
        self,
    ) -> typing.Optional["NetworkConnectionMonitorTestConfigurationTcpConfiguration"]:
        '''tcp_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#tcp_configuration NetworkConnectionMonitor#tcp_configuration}
        '''
        result = self._values.get("tcp_configuration")
        return typing.cast(typing.Optional["NetworkConnectionMonitorTestConfigurationTcpConfiguration"], result)

    @builtins.property
    def test_frequency_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_frequency_in_seconds NetworkConnectionMonitor#test_frequency_in_seconds}.'''
        result = self._values.get("test_frequency_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorTestConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationHttpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "method": "method",
        "path": "path",
        "port": "port",
        "prefer_https": "preferHttps",
        "request_header": "requestHeader",
        "valid_status_code_ranges": "validStatusCodeRanges",
    },
)
class NetworkConnectionMonitorTestConfigurationHttpConfiguration:
    def __init__(
        self,
        *,
        method: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        prefer_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        request_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader", typing.Dict[str, typing.Any]]]]] = None,
        valid_status_code_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#method NetworkConnectionMonitor#method}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#path NetworkConnectionMonitor#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#port NetworkConnectionMonitor#port}.
        :param prefer_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#prefer_https NetworkConnectionMonitor#prefer_https}.
        :param request_header: request_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#request_header NetworkConnectionMonitor#request_header}
        :param valid_status_code_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#valid_status_code_ranges NetworkConnectionMonitor#valid_status_code_ranges}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationHttpConfiguration.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument prefer_https", value=prefer_https, expected_type=type_hints["prefer_https"])
            check_type(argname="argument request_header", value=request_header, expected_type=type_hints["request_header"])
            check_type(argname="argument valid_status_code_ranges", value=valid_status_code_ranges, expected_type=type_hints["valid_status_code_ranges"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if prefer_https is not None:
            self._values["prefer_https"] = prefer_https
        if request_header is not None:
            self._values["request_header"] = request_header
        if valid_status_code_ranges is not None:
            self._values["valid_status_code_ranges"] = valid_status_code_ranges

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#method NetworkConnectionMonitor#method}.'''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#path NetworkConnectionMonitor#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#port NetworkConnectionMonitor#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def prefer_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#prefer_https NetworkConnectionMonitor#prefer_https}.'''
        result = self._values.get("prefer_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def request_header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader"]]]:
        '''request_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#request_header NetworkConnectionMonitor#request_header}
        '''
        result = self._values.get("request_header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader"]]], result)

    @builtins.property
    def valid_status_code_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#valid_status_code_ranges NetworkConnectionMonitor#valid_status_code_ranges}.'''
        result = self._values.get("valid_status_code_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorTestConfigurationHttpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestHeader")
    def put_request_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference.put_request_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeader", [value]))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPreferHttps")
    def reset_prefer_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferHttps", []))

    @jsii.member(jsii_name="resetRequestHeader")
    def reset_request_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeader", []))

    @jsii.member(jsii_name="resetValidStatusCodeRanges")
    def reset_valid_status_code_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidStatusCodeRanges", []))

    @builtins.property
    @jsii.member(jsii_name="requestHeader")
    def request_header(
        self,
    ) -> "NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList":
        return typing.cast("NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList", jsii.get(self, "requestHeader"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="preferHttpsInput")
    def prefer_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preferHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderInput")
    def request_header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader"]]], jsii.get(self, "requestHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="validStatusCodeRangesInput")
    def valid_status_code_ranges_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "validStatusCodeRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferHttps")
    def prefer_https(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preferHttps"))

    @prefer_https.setter
    def prefer_https(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference, "prefer_https").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferHttps", value)

    @builtins.property
    @jsii.member(jsii_name="validStatusCodeRanges")
    def valid_status_code_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "validStatusCodeRanges"))

    @valid_status_code_ranges.setter
    def valid_status_code_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference, "valid_status_code_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validStatusCodeRanges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkConnectionMonitorTestConfigurationHttpConfiguration]:
        return typing.cast(typing.Optional[NetworkConnectionMonitorTestConfigurationHttpConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkConnectionMonitorTestConfigurationHttpConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#value NetworkConnectionMonitor#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#value NetworkConnectionMonitor#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationIcmpConfiguration",
    jsii_struct_bases=[],
    name_mapping={"trace_route_enabled": "traceRouteEnabled"},
)
class NetworkConnectionMonitorTestConfigurationIcmpConfiguration:
    def __init__(
        self,
        *,
        trace_route_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param trace_route_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#trace_route_enabled NetworkConnectionMonitor#trace_route_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationIcmpConfiguration.__init__)
            check_type(argname="argument trace_route_enabled", value=trace_route_enabled, expected_type=type_hints["trace_route_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if trace_route_enabled is not None:
            self._values["trace_route_enabled"] = trace_route_enabled

    @builtins.property
    def trace_route_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#trace_route_enabled NetworkConnectionMonitor#trace_route_enabled}.'''
        result = self._values.get("trace_route_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorTestConfigurationIcmpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectionMonitorTestConfigurationIcmpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationIcmpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationIcmpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTraceRouteEnabled")
    def reset_trace_route_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTraceRouteEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="traceRouteEnabledInput")
    def trace_route_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "traceRouteEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="traceRouteEnabled")
    def trace_route_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "traceRouteEnabled"))

    @trace_route_enabled.setter
    def trace_route_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationIcmpConfigurationOutputReference, "trace_route_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "traceRouteEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkConnectionMonitorTestConfigurationIcmpConfiguration]:
        return typing.cast(typing.Optional[NetworkConnectionMonitorTestConfigurationIcmpConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkConnectionMonitorTestConfigurationIcmpConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationIcmpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectionMonitorTestConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationList",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkConnectionMonitorTestConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkConnectionMonitorTestConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectionMonitorTestConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttpConfiguration")
    def put_http_configuration(
        self,
        *,
        method: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        prefer_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        request_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader, typing.Dict[str, typing.Any]]]]] = None,
        valid_status_code_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#method NetworkConnectionMonitor#method}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#path NetworkConnectionMonitor#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#port NetworkConnectionMonitor#port}.
        :param prefer_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#prefer_https NetworkConnectionMonitor#prefer_https}.
        :param request_header: request_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#request_header NetworkConnectionMonitor#request_header}
        :param valid_status_code_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#valid_status_code_ranges NetworkConnectionMonitor#valid_status_code_ranges}.
        '''
        value = NetworkConnectionMonitorTestConfigurationHttpConfiguration(
            method=method,
            path=path,
            port=port,
            prefer_https=prefer_https,
            request_header=request_header,
            valid_status_code_ranges=valid_status_code_ranges,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpConfiguration", [value]))

    @jsii.member(jsii_name="putIcmpConfiguration")
    def put_icmp_configuration(
        self,
        *,
        trace_route_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param trace_route_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#trace_route_enabled NetworkConnectionMonitor#trace_route_enabled}.
        '''
        value = NetworkConnectionMonitorTestConfigurationIcmpConfiguration(
            trace_route_enabled=trace_route_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putIcmpConfiguration", [value]))

    @jsii.member(jsii_name="putSuccessThreshold")
    def put_success_threshold(
        self,
        *,
        checks_failed_percent: typing.Optional[jsii.Number] = None,
        round_trip_time_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param checks_failed_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#checks_failed_percent NetworkConnectionMonitor#checks_failed_percent}.
        :param round_trip_time_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#round_trip_time_ms NetworkConnectionMonitor#round_trip_time_ms}.
        '''
        value = NetworkConnectionMonitorTestConfigurationSuccessThreshold(
            checks_failed_percent=checks_failed_percent,
            round_trip_time_ms=round_trip_time_ms,
        )

        return typing.cast(None, jsii.invoke(self, "putSuccessThreshold", [value]))

    @jsii.member(jsii_name="putTcpConfiguration")
    def put_tcp_configuration(
        self,
        *,
        port: jsii.Number,
        destination_port_behavior: typing.Optional[builtins.str] = None,
        trace_route_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#port NetworkConnectionMonitor#port}.
        :param destination_port_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#destination_port_behavior NetworkConnectionMonitor#destination_port_behavior}.
        :param trace_route_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#trace_route_enabled NetworkConnectionMonitor#trace_route_enabled}.
        '''
        value = NetworkConnectionMonitorTestConfigurationTcpConfiguration(
            port=port,
            destination_port_behavior=destination_port_behavior,
            trace_route_enabled=trace_route_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putTcpConfiguration", [value]))

    @jsii.member(jsii_name="resetHttpConfiguration")
    def reset_http_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpConfiguration", []))

    @jsii.member(jsii_name="resetIcmpConfiguration")
    def reset_icmp_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpConfiguration", []))

    @jsii.member(jsii_name="resetPreferredIpVersion")
    def reset_preferred_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredIpVersion", []))

    @jsii.member(jsii_name="resetSuccessThreshold")
    def reset_success_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessThreshold", []))

    @jsii.member(jsii_name="resetTcpConfiguration")
    def reset_tcp_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcpConfiguration", []))

    @jsii.member(jsii_name="resetTestFrequencyInSeconds")
    def reset_test_frequency_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestFrequencyInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="httpConfiguration")
    def http_configuration(
        self,
    ) -> NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference:
        return typing.cast(NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference, jsii.get(self, "httpConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="icmpConfiguration")
    def icmp_configuration(
        self,
    ) -> NetworkConnectionMonitorTestConfigurationIcmpConfigurationOutputReference:
        return typing.cast(NetworkConnectionMonitorTestConfigurationIcmpConfigurationOutputReference, jsii.get(self, "icmpConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="successThreshold")
    def success_threshold(
        self,
    ) -> "NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference":
        return typing.cast("NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference", jsii.get(self, "successThreshold"))

    @builtins.property
    @jsii.member(jsii_name="tcpConfiguration")
    def tcp_configuration(
        self,
    ) -> "NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference":
        return typing.cast("NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference", jsii.get(self, "tcpConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="httpConfigurationInput")
    def http_configuration_input(
        self,
    ) -> typing.Optional[NetworkConnectionMonitorTestConfigurationHttpConfiguration]:
        return typing.cast(typing.Optional[NetworkConnectionMonitorTestConfigurationHttpConfiguration], jsii.get(self, "httpConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpConfigurationInput")
    def icmp_configuration_input(
        self,
    ) -> typing.Optional[NetworkConnectionMonitorTestConfigurationIcmpConfiguration]:
        return typing.cast(typing.Optional[NetworkConnectionMonitorTestConfigurationIcmpConfiguration], jsii.get(self, "icmpConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredIpVersionInput")
    def preferred_ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredIpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="successThresholdInput")
    def success_threshold_input(
        self,
    ) -> typing.Optional["NetworkConnectionMonitorTestConfigurationSuccessThreshold"]:
        return typing.cast(typing.Optional["NetworkConnectionMonitorTestConfigurationSuccessThreshold"], jsii.get(self, "successThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpConfigurationInput")
    def tcp_configuration_input(
        self,
    ) -> typing.Optional["NetworkConnectionMonitorTestConfigurationTcpConfiguration"]:
        return typing.cast(typing.Optional["NetworkConnectionMonitorTestConfigurationTcpConfiguration"], jsii.get(self, "tcpConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="testFrequencyInSecondsInput")
    def test_frequency_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "testFrequencyInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="preferredIpVersion")
    def preferred_ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredIpVersion"))

    @preferred_ip_version.setter
    def preferred_ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationOutputReference, "preferred_ip_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredIpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="testFrequencyInSeconds")
    def test_frequency_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "testFrequencyInSeconds"))

    @test_frequency_in_seconds.setter
    def test_frequency_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationOutputReference, "test_frequency_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testFrequencyInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkConnectionMonitorTestConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkConnectionMonitorTestConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkConnectionMonitorTestConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationSuccessThreshold",
    jsii_struct_bases=[],
    name_mapping={
        "checks_failed_percent": "checksFailedPercent",
        "round_trip_time_ms": "roundTripTimeMs",
    },
)
class NetworkConnectionMonitorTestConfigurationSuccessThreshold:
    def __init__(
        self,
        *,
        checks_failed_percent: typing.Optional[jsii.Number] = None,
        round_trip_time_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param checks_failed_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#checks_failed_percent NetworkConnectionMonitor#checks_failed_percent}.
        :param round_trip_time_ms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#round_trip_time_ms NetworkConnectionMonitor#round_trip_time_ms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationSuccessThreshold.__init__)
            check_type(argname="argument checks_failed_percent", value=checks_failed_percent, expected_type=type_hints["checks_failed_percent"])
            check_type(argname="argument round_trip_time_ms", value=round_trip_time_ms, expected_type=type_hints["round_trip_time_ms"])
        self._values: typing.Dict[str, typing.Any] = {}
        if checks_failed_percent is not None:
            self._values["checks_failed_percent"] = checks_failed_percent
        if round_trip_time_ms is not None:
            self._values["round_trip_time_ms"] = round_trip_time_ms

    @builtins.property
    def checks_failed_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#checks_failed_percent NetworkConnectionMonitor#checks_failed_percent}.'''
        result = self._values.get("checks_failed_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def round_trip_time_ms(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#round_trip_time_ms NetworkConnectionMonitor#round_trip_time_ms}.'''
        result = self._values.get("round_trip_time_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorTestConfigurationSuccessThreshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetChecksFailedPercent")
    def reset_checks_failed_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChecksFailedPercent", []))

    @jsii.member(jsii_name="resetRoundTripTimeMs")
    def reset_round_trip_time_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoundTripTimeMs", []))

    @builtins.property
    @jsii.member(jsii_name="checksFailedPercentInput")
    def checks_failed_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "checksFailedPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="roundTripTimeMsInput")
    def round_trip_time_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "roundTripTimeMsInput"))

    @builtins.property
    @jsii.member(jsii_name="checksFailedPercent")
    def checks_failed_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "checksFailedPercent"))

    @checks_failed_percent.setter
    def checks_failed_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference, "checks_failed_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checksFailedPercent", value)

    @builtins.property
    @jsii.member(jsii_name="roundTripTimeMs")
    def round_trip_time_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "roundTripTimeMs"))

    @round_trip_time_ms.setter
    def round_trip_time_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference, "round_trip_time_ms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roundTripTimeMs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkConnectionMonitorTestConfigurationSuccessThreshold]:
        return typing.cast(typing.Optional[NetworkConnectionMonitorTestConfigurationSuccessThreshold], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkConnectionMonitorTestConfigurationSuccessThreshold],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationTcpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "destination_port_behavior": "destinationPortBehavior",
        "trace_route_enabled": "traceRouteEnabled",
    },
)
class NetworkConnectionMonitorTestConfigurationTcpConfiguration:
    def __init__(
        self,
        *,
        port: jsii.Number,
        destination_port_behavior: typing.Optional[builtins.str] = None,
        trace_route_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#port NetworkConnectionMonitor#port}.
        :param destination_port_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#destination_port_behavior NetworkConnectionMonitor#destination_port_behavior}.
        :param trace_route_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#trace_route_enabled NetworkConnectionMonitor#trace_route_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationTcpConfiguration.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument destination_port_behavior", value=destination_port_behavior, expected_type=type_hints["destination_port_behavior"])
            check_type(argname="argument trace_route_enabled", value=trace_route_enabled, expected_type=type_hints["trace_route_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
        }
        if destination_port_behavior is not None:
            self._values["destination_port_behavior"] = destination_port_behavior
        if trace_route_enabled is not None:
            self._values["trace_route_enabled"] = trace_route_enabled

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#port NetworkConnectionMonitor#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def destination_port_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#destination_port_behavior NetworkConnectionMonitor#destination_port_behavior}.'''
        result = self._values.get("destination_port_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trace_route_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#trace_route_enabled NetworkConnectionMonitor#trace_route_enabled}.'''
        result = self._values.get("trace_route_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorTestConfigurationTcpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestinationPortBehavior")
    def reset_destination_port_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPortBehavior", []))

    @jsii.member(jsii_name="resetTraceRouteEnabled")
    def reset_trace_route_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTraceRouteEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="destinationPortBehaviorInput")
    def destination_port_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationPortBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="traceRouteEnabledInput")
    def trace_route_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "traceRouteEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortBehavior")
    def destination_port_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPortBehavior"))

    @destination_port_behavior.setter
    def destination_port_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference, "destination_port_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPortBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="traceRouteEnabled")
    def trace_route_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "traceRouteEnabled"))

    @trace_route_enabled.setter
    def trace_route_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference, "trace_route_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "traceRouteEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkConnectionMonitorTestConfigurationTcpConfiguration]:
        return typing.cast(typing.Optional[NetworkConnectionMonitorTestConfigurationTcpConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkConnectionMonitorTestConfigurationTcpConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestGroup",
    jsii_struct_bases=[],
    name_mapping={
        "destination_endpoints": "destinationEndpoints",
        "name": "name",
        "source_endpoints": "sourceEndpoints",
        "test_configuration_names": "testConfigurationNames",
        "enabled": "enabled",
    },
)
class NetworkConnectionMonitorTestGroup:
    def __init__(
        self,
        *,
        destination_endpoints: typing.Sequence[builtins.str],
        name: builtins.str,
        source_endpoints: typing.Sequence[builtins.str],
        test_configuration_names: typing.Sequence[builtins.str],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#destination_endpoints NetworkConnectionMonitor#destination_endpoints}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.
        :param source_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#source_endpoints NetworkConnectionMonitor#source_endpoints}.
        :param test_configuration_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_configuration_names NetworkConnectionMonitor#test_configuration_names}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#enabled NetworkConnectionMonitor#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestGroup.__init__)
            check_type(argname="argument destination_endpoints", value=destination_endpoints, expected_type=type_hints["destination_endpoints"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_endpoints", value=source_endpoints, expected_type=type_hints["source_endpoints"])
            check_type(argname="argument test_configuration_names", value=test_configuration_names, expected_type=type_hints["test_configuration_names"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination_endpoints": destination_endpoints,
            "name": name,
            "source_endpoints": source_endpoints,
            "test_configuration_names": test_configuration_names,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def destination_endpoints(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#destination_endpoints NetworkConnectionMonitor#destination_endpoints}.'''
        result = self._values.get("destination_endpoints")
        assert result is not None, "Required property 'destination_endpoints' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#name NetworkConnectionMonitor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_endpoints(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#source_endpoints NetworkConnectionMonitor#source_endpoints}.'''
        result = self._values.get("source_endpoints")
        assert result is not None, "Required property 'source_endpoints' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def test_configuration_names(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#test_configuration_names NetworkConnectionMonitor#test_configuration_names}.'''
        result = self._values.get("test_configuration_names")
        assert result is not None, "Required property 'test_configuration_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#enabled NetworkConnectionMonitor#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorTestGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectionMonitorTestGroupList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestGroupList",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestGroupList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkConnectionMonitorTestGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestGroupList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkConnectionMonitorTestGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkConnectionMonitorTestGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkConnectionMonitorTestGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTestGroupOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTestGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="destinationEndpointsInput")
    def destination_endpoints_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceEndpointsInput")
    def source_endpoints_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="testConfigurationNamesInput")
    def test_configuration_names_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "testConfigurationNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationEndpoints")
    def destination_endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationEndpoints"))

    @destination_endpoints.setter
    def destination_endpoints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupOutputReference, "destination_endpoints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEndpoints")
    def source_endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceEndpoints"))

    @source_endpoints.setter
    def source_endpoints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupOutputReference, "source_endpoints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="testConfigurationNames")
    def test_configuration_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "testConfigurationNames"))

    @test_configuration_names.setter
    def test_configuration_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupOutputReference, "test_configuration_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testConfigurationNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkConnectionMonitorTestGroup, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkConnectionMonitorTestGroup, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkConnectionMonitorTestGroup, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTestGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class NetworkConnectionMonitorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#create NetworkConnectionMonitor#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#delete NetworkConnectionMonitor#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#read NetworkConnectionMonitor#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#update NetworkConnectionMonitor#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#create NetworkConnectionMonitor#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#delete NetworkConnectionMonitor#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#read NetworkConnectionMonitor#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_connection_monitor#update NetworkConnectionMonitor#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectionMonitorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkConnectionMonitorTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkConnectionMonitor.NetworkConnectionMonitorTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkConnectionMonitorTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkConnectionMonitorTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkConnectionMonitorTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkConnectionMonitorTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkConnectionMonitorTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkConnectionMonitor",
    "NetworkConnectionMonitorConfig",
    "NetworkConnectionMonitorEndpoint",
    "NetworkConnectionMonitorEndpointFilter",
    "NetworkConnectionMonitorEndpointFilterItem",
    "NetworkConnectionMonitorEndpointFilterItemList",
    "NetworkConnectionMonitorEndpointFilterItemOutputReference",
    "NetworkConnectionMonitorEndpointFilterOutputReference",
    "NetworkConnectionMonitorEndpointList",
    "NetworkConnectionMonitorEndpointOutputReference",
    "NetworkConnectionMonitorTestConfiguration",
    "NetworkConnectionMonitorTestConfigurationHttpConfiguration",
    "NetworkConnectionMonitorTestConfigurationHttpConfigurationOutputReference",
    "NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeader",
    "NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderList",
    "NetworkConnectionMonitorTestConfigurationHttpConfigurationRequestHeaderOutputReference",
    "NetworkConnectionMonitorTestConfigurationIcmpConfiguration",
    "NetworkConnectionMonitorTestConfigurationIcmpConfigurationOutputReference",
    "NetworkConnectionMonitorTestConfigurationList",
    "NetworkConnectionMonitorTestConfigurationOutputReference",
    "NetworkConnectionMonitorTestConfigurationSuccessThreshold",
    "NetworkConnectionMonitorTestConfigurationSuccessThresholdOutputReference",
    "NetworkConnectionMonitorTestConfigurationTcpConfiguration",
    "NetworkConnectionMonitorTestConfigurationTcpConfigurationOutputReference",
    "NetworkConnectionMonitorTestGroup",
    "NetworkConnectionMonitorTestGroupList",
    "NetworkConnectionMonitorTestGroupOutputReference",
    "NetworkConnectionMonitorTimeouts",
    "NetworkConnectionMonitorTimeoutsOutputReference",
]

publication.publish()
