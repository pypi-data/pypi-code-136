'''
# `azurerm_monitor_data_collection_rule`

Refer to the Terraform Registory for docs: [`azurerm_monitor_data_collection_rule`](https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule).
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


class MonitorDataCollectionRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule azurerm_monitor_data_collection_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_flow: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataFlow", typing.Dict[str, typing.Any]]]],
        destinations: typing.Union["MonitorDataCollectionRuleDestinations", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        data_sources: typing.Optional[typing.Union["MonitorDataCollectionRuleDataSources", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MonitorDataCollectionRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule azurerm_monitor_data_collection_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_flow: data_flow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#data_flow MonitorDataCollectionRule#data_flow}
        :param destinations: destinations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#destinations MonitorDataCollectionRule#destinations}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#location MonitorDataCollectionRule#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#resource_group_name MonitorDataCollectionRule#resource_group_name}.
        :param data_sources: data_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#data_sources MonitorDataCollectionRule#data_sources}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#description MonitorDataCollectionRule#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#id MonitorDataCollectionRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#kind MonitorDataCollectionRule#kind}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#tags MonitorDataCollectionRule#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#timeouts MonitorDataCollectionRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorDataCollectionRuleConfig(
            data_flow=data_flow,
            destinations=destinations,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            data_sources=data_sources,
            description=description,
            id=id,
            kind=kind,
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

    @jsii.member(jsii_name="putDataFlow")
    def put_data_flow(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataFlow", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRule.put_data_flow)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataFlow", [value]))

    @jsii.member(jsii_name="putDataSources")
    def put_data_sources(
        self,
        *,
        extension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesExtension", typing.Dict[str, typing.Any]]]]] = None,
        performance_counter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesPerformanceCounter", typing.Dict[str, typing.Any]]]]] = None,
        syslog: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesSyslog", typing.Dict[str, typing.Any]]]]] = None,
        windows_event_log: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesWindowsEventLog", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#extension MonitorDataCollectionRule#extension}
        :param performance_counter: performance_counter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#performance_counter MonitorDataCollectionRule#performance_counter}
        :param syslog: syslog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#syslog MonitorDataCollectionRule#syslog}
        :param windows_event_log: windows_event_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#windows_event_log MonitorDataCollectionRule#windows_event_log}
        '''
        value = MonitorDataCollectionRuleDataSources(
            extension=extension,
            performance_counter=performance_counter,
            syslog=syslog,
            windows_event_log=windows_event_log,
        )

        return typing.cast(None, jsii.invoke(self, "putDataSources", [value]))

    @jsii.member(jsii_name="putDestinations")
    def put_destinations(
        self,
        *,
        azure_monitor_metrics: typing.Optional[typing.Union["MonitorDataCollectionRuleDestinationsAzureMonitorMetrics", typing.Dict[str, typing.Any]]] = None,
        log_analytics: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDestinationsLogAnalytics", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param azure_monitor_metrics: azure_monitor_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#azure_monitor_metrics MonitorDataCollectionRule#azure_monitor_metrics}
        :param log_analytics: log_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#log_analytics MonitorDataCollectionRule#log_analytics}
        '''
        value = MonitorDataCollectionRuleDestinations(
            azure_monitor_metrics=azure_monitor_metrics, log_analytics=log_analytics
        )

        return typing.cast(None, jsii.invoke(self, "putDestinations", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#create MonitorDataCollectionRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#delete MonitorDataCollectionRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#read MonitorDataCollectionRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#update MonitorDataCollectionRule#update}.
        '''
        value = MonitorDataCollectionRuleTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDataSources")
    def reset_data_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSources", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

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
    @jsii.member(jsii_name="dataFlow")
    def data_flow(self) -> "MonitorDataCollectionRuleDataFlowList":
        return typing.cast("MonitorDataCollectionRuleDataFlowList", jsii.get(self, "dataFlow"))

    @builtins.property
    @jsii.member(jsii_name="dataSources")
    def data_sources(self) -> "MonitorDataCollectionRuleDataSourcesOutputReference":
        return typing.cast("MonitorDataCollectionRuleDataSourcesOutputReference", jsii.get(self, "dataSources"))

    @builtins.property
    @jsii.member(jsii_name="destinations")
    def destinations(self) -> "MonitorDataCollectionRuleDestinationsOutputReference":
        return typing.cast("MonitorDataCollectionRuleDestinationsOutputReference", jsii.get(self, "destinations"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MonitorDataCollectionRuleTimeoutsOutputReference":
        return typing.cast("MonitorDataCollectionRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="dataFlowInput")
    def data_flow_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataFlow"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataFlow"]]], jsii.get(self, "dataFlowInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourcesInput")
    def data_sources_input(
        self,
    ) -> typing.Optional["MonitorDataCollectionRuleDataSources"]:
        return typing.cast(typing.Optional["MonitorDataCollectionRuleDataSources"], jsii.get(self, "dataSourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationsInput")
    def destinations_input(
        self,
    ) -> typing.Optional["MonitorDataCollectionRuleDestinations"]:
        return typing.cast(typing.Optional["MonitorDataCollectionRuleDestinations"], jsii.get(self, "destinationsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MonitorDataCollectionRuleTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MonitorDataCollectionRuleTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRule, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRule, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRule, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRule, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_flow": "dataFlow",
        "destinations": "destinations",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "data_sources": "dataSources",
        "description": "description",
        "id": "id",
        "kind": "kind",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class MonitorDataCollectionRuleConfig(cdktf.TerraformMetaArguments):
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
        data_flow: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataFlow", typing.Dict[str, typing.Any]]]],
        destinations: typing.Union["MonitorDataCollectionRuleDestinations", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        data_sources: typing.Optional[typing.Union["MonitorDataCollectionRuleDataSources", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MonitorDataCollectionRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_flow: data_flow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#data_flow MonitorDataCollectionRule#data_flow}
        :param destinations: destinations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#destinations MonitorDataCollectionRule#destinations}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#location MonitorDataCollectionRule#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#resource_group_name MonitorDataCollectionRule#resource_group_name}.
        :param data_sources: data_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#data_sources MonitorDataCollectionRule#data_sources}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#description MonitorDataCollectionRule#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#id MonitorDataCollectionRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#kind MonitorDataCollectionRule#kind}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#tags MonitorDataCollectionRule#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#timeouts MonitorDataCollectionRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destinations, dict):
            destinations = MonitorDataCollectionRuleDestinations(**destinations)
        if isinstance(data_sources, dict):
            data_sources = MonitorDataCollectionRuleDataSources(**data_sources)
        if isinstance(timeouts, dict):
            timeouts = MonitorDataCollectionRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_flow", value=data_flow, expected_type=type_hints["data_flow"])
            check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument data_sources", value=data_sources, expected_type=type_hints["data_sources"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_flow": data_flow,
            "destinations": destinations,
            "location": location,
            "name": name,
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
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if kind is not None:
            self._values["kind"] = kind
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
    def data_flow(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataFlow"]]:
        '''data_flow block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#data_flow MonitorDataCollectionRule#data_flow}
        '''
        result = self._values.get("data_flow")
        assert result is not None, "Required property 'data_flow' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataFlow"]], result)

    @builtins.property
    def destinations(self) -> "MonitorDataCollectionRuleDestinations":
        '''destinations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#destinations MonitorDataCollectionRule#destinations}
        '''
        result = self._values.get("destinations")
        assert result is not None, "Required property 'destinations' is missing"
        return typing.cast("MonitorDataCollectionRuleDestinations", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#location MonitorDataCollectionRule#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#resource_group_name MonitorDataCollectionRule#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_sources(self) -> typing.Optional["MonitorDataCollectionRuleDataSources"]:
        '''data_sources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#data_sources MonitorDataCollectionRule#data_sources}
        '''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional["MonitorDataCollectionRuleDataSources"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#description MonitorDataCollectionRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#id MonitorDataCollectionRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#kind MonitorDataCollectionRule#kind}.'''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#tags MonitorDataCollectionRule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MonitorDataCollectionRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#timeouts MonitorDataCollectionRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MonitorDataCollectionRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataFlow",
    jsii_struct_bases=[],
    name_mapping={"destinations": "destinations", "streams": "streams"},
)
class MonitorDataCollectionRuleDataFlow:
    def __init__(
        self,
        *,
        destinations: typing.Sequence[builtins.str],
        streams: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param destinations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#destinations MonitorDataCollectionRule#destinations}.
        :param streams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#streams MonitorDataCollectionRule#streams}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataFlow.__init__)
            check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            check_type(argname="argument streams", value=streams, expected_type=type_hints["streams"])
        self._values: typing.Dict[str, typing.Any] = {
            "destinations": destinations,
            "streams": streams,
        }

    @builtins.property
    def destinations(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#destinations MonitorDataCollectionRule#destinations}.'''
        result = self._values.get("destinations")
        assert result is not None, "Required property 'destinations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def streams(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#streams MonitorDataCollectionRule#streams}.'''
        result = self._values.get("streams")
        assert result is not None, "Required property 'streams' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDataFlow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDataCollectionRuleDataFlowList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataFlowList",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataFlowList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorDataCollectionRuleDataFlowOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataFlowList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorDataCollectionRuleDataFlowOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataFlowList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataFlowList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataFlowList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataFlow]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataFlow]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataFlow]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataFlowList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDataCollectionRuleDataFlowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataFlowOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataFlowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationsInput")
    def destinations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationsInput"))

    @builtins.property
    @jsii.member(jsii_name="streamsInput")
    def streams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "streamsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinations")
    def destinations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinations"))

    @destinations.setter
    def destinations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataFlowOutputReference, "destinations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinations", value)

    @builtins.property
    @jsii.member(jsii_name="streams")
    def streams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "streams"))

    @streams.setter
    def streams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataFlowOutputReference, "streams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDataCollectionRuleDataFlow, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDataCollectionRuleDataFlow, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDataCollectionRuleDataFlow, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataFlowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSources",
    jsii_struct_bases=[],
    name_mapping={
        "extension": "extension",
        "performance_counter": "performanceCounter",
        "syslog": "syslog",
        "windows_event_log": "windowsEventLog",
    },
)
class MonitorDataCollectionRuleDataSources:
    def __init__(
        self,
        *,
        extension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesExtension", typing.Dict[str, typing.Any]]]]] = None,
        performance_counter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesPerformanceCounter", typing.Dict[str, typing.Any]]]]] = None,
        syslog: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesSyslog", typing.Dict[str, typing.Any]]]]] = None,
        windows_event_log: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesWindowsEventLog", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#extension MonitorDataCollectionRule#extension}
        :param performance_counter: performance_counter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#performance_counter MonitorDataCollectionRule#performance_counter}
        :param syslog: syslog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#syslog MonitorDataCollectionRule#syslog}
        :param windows_event_log: windows_event_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#windows_event_log MonitorDataCollectionRule#windows_event_log}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSources.__init__)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
            check_type(argname="argument performance_counter", value=performance_counter, expected_type=type_hints["performance_counter"])
            check_type(argname="argument syslog", value=syslog, expected_type=type_hints["syslog"])
            check_type(argname="argument windows_event_log", value=windows_event_log, expected_type=type_hints["windows_event_log"])
        self._values: typing.Dict[str, typing.Any] = {}
        if extension is not None:
            self._values["extension"] = extension
        if performance_counter is not None:
            self._values["performance_counter"] = performance_counter
        if syslog is not None:
            self._values["syslog"] = syslog
        if windows_event_log is not None:
            self._values["windows_event_log"] = windows_event_log

    @builtins.property
    def extension(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesExtension"]]]:
        '''extension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#extension MonitorDataCollectionRule#extension}
        '''
        result = self._values.get("extension")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesExtension"]]], result)

    @builtins.property
    def performance_counter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesPerformanceCounter"]]]:
        '''performance_counter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#performance_counter MonitorDataCollectionRule#performance_counter}
        '''
        result = self._values.get("performance_counter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesPerformanceCounter"]]], result)

    @builtins.property
    def syslog(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesSyslog"]]]:
        '''syslog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#syslog MonitorDataCollectionRule#syslog}
        '''
        result = self._values.get("syslog")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesSyslog"]]], result)

    @builtins.property
    def windows_event_log(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesWindowsEventLog"]]]:
        '''windows_event_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#windows_event_log MonitorDataCollectionRule#windows_event_log}
        '''
        result = self._values.get("windows_event_log")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesWindowsEventLog"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDataSources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesExtension",
    jsii_struct_bases=[],
    name_mapping={
        "extension_name": "extensionName",
        "name": "name",
        "streams": "streams",
        "extension_json": "extensionJson",
        "input_data_sources": "inputDataSources",
    },
)
class MonitorDataCollectionRuleDataSourcesExtension:
    def __init__(
        self,
        *,
        extension_name: builtins.str,
        name: builtins.str,
        streams: typing.Sequence[builtins.str],
        extension_json: typing.Optional[builtins.str] = None,
        input_data_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param extension_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#extension_name MonitorDataCollectionRule#extension_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        :param streams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#streams MonitorDataCollectionRule#streams}.
        :param extension_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#extension_json MonitorDataCollectionRule#extension_json}.
        :param input_data_sources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#input_data_sources MonitorDataCollectionRule#input_data_sources}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesExtension.__init__)
            check_type(argname="argument extension_name", value=extension_name, expected_type=type_hints["extension_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument streams", value=streams, expected_type=type_hints["streams"])
            check_type(argname="argument extension_json", value=extension_json, expected_type=type_hints["extension_json"])
            check_type(argname="argument input_data_sources", value=input_data_sources, expected_type=type_hints["input_data_sources"])
        self._values: typing.Dict[str, typing.Any] = {
            "extension_name": extension_name,
            "name": name,
            "streams": streams,
        }
        if extension_json is not None:
            self._values["extension_json"] = extension_json
        if input_data_sources is not None:
            self._values["input_data_sources"] = input_data_sources

    @builtins.property
    def extension_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#extension_name MonitorDataCollectionRule#extension_name}.'''
        result = self._values.get("extension_name")
        assert result is not None, "Required property 'extension_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def streams(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#streams MonitorDataCollectionRule#streams}.'''
        result = self._values.get("streams")
        assert result is not None, "Required property 'streams' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def extension_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#extension_json MonitorDataCollectionRule#extension_json}.'''
        result = self._values.get("extension_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_data_sources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#input_data_sources MonitorDataCollectionRule#input_data_sources}.'''
        result = self._values.get("input_data_sources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDataSourcesExtension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDataCollectionRuleDataSourcesExtensionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesExtensionList",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesExtensionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorDataCollectionRuleDataSourcesExtensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesExtensionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorDataCollectionRuleDataSourcesExtensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesExtension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesExtension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesExtension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDataCollectionRuleDataSourcesExtensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesExtensionOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesExtensionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExtensionJson")
    def reset_extension_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtensionJson", []))

    @jsii.member(jsii_name="resetInputDataSources")
    def reset_input_data_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputDataSources", []))

    @builtins.property
    @jsii.member(jsii_name="extensionJsonInput")
    def extension_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extensionJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionNameInput")
    def extension_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extensionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="inputDataSourcesInput")
    def input_data_sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inputDataSourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="streamsInput")
    def streams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "streamsInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionJson")
    def extension_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extensionJson"))

    @extension_json.setter
    def extension_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionOutputReference, "extension_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionJson", value)

    @builtins.property
    @jsii.member(jsii_name="extensionName")
    def extension_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extensionName"))

    @extension_name.setter
    def extension_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionOutputReference, "extension_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionName", value)

    @builtins.property
    @jsii.member(jsii_name="inputDataSources")
    def input_data_sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inputDataSources"))

    @input_data_sources.setter
    def input_data_sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionOutputReference, "input_data_sources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputDataSources", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="streams")
    def streams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "streams"))

    @streams.setter
    def streams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionOutputReference, "streams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesExtension, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesExtension, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesExtension, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesExtensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDataCollectionRuleDataSourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExtension")
    def put_extension(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorDataCollectionRuleDataSourcesExtension, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesOutputReference.put_extension)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtension", [value]))

    @jsii.member(jsii_name="putPerformanceCounter")
    def put_performance_counter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesPerformanceCounter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesOutputReference.put_performance_counter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPerformanceCounter", [value]))

    @jsii.member(jsii_name="putSyslog")
    def put_syslog(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesSyslog", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesOutputReference.put_syslog)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSyslog", [value]))

    @jsii.member(jsii_name="putWindowsEventLog")
    def put_windows_event_log(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDataSourcesWindowsEventLog", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesOutputReference.put_windows_event_log)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWindowsEventLog", [value]))

    @jsii.member(jsii_name="resetExtension")
    def reset_extension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtension", []))

    @jsii.member(jsii_name="resetPerformanceCounter")
    def reset_performance_counter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformanceCounter", []))

    @jsii.member(jsii_name="resetSyslog")
    def reset_syslog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyslog", []))

    @jsii.member(jsii_name="resetWindowsEventLog")
    def reset_windows_event_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsEventLog", []))

    @builtins.property
    @jsii.member(jsii_name="extension")
    def extension(self) -> MonitorDataCollectionRuleDataSourcesExtensionList:
        return typing.cast(MonitorDataCollectionRuleDataSourcesExtensionList, jsii.get(self, "extension"))

    @builtins.property
    @jsii.member(jsii_name="performanceCounter")
    def performance_counter(
        self,
    ) -> "MonitorDataCollectionRuleDataSourcesPerformanceCounterList":
        return typing.cast("MonitorDataCollectionRuleDataSourcesPerformanceCounterList", jsii.get(self, "performanceCounter"))

    @builtins.property
    @jsii.member(jsii_name="syslog")
    def syslog(self) -> "MonitorDataCollectionRuleDataSourcesSyslogList":
        return typing.cast("MonitorDataCollectionRuleDataSourcesSyslogList", jsii.get(self, "syslog"))

    @builtins.property
    @jsii.member(jsii_name="windowsEventLog")
    def windows_event_log(
        self,
    ) -> "MonitorDataCollectionRuleDataSourcesWindowsEventLogList":
        return typing.cast("MonitorDataCollectionRuleDataSourcesWindowsEventLogList", jsii.get(self, "windowsEventLog"))

    @builtins.property
    @jsii.member(jsii_name="extensionInput")
    def extension_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesExtension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesExtension]]], jsii.get(self, "extensionInput"))

    @builtins.property
    @jsii.member(jsii_name="performanceCounterInput")
    def performance_counter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesPerformanceCounter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesPerformanceCounter"]]], jsii.get(self, "performanceCounterInput"))

    @builtins.property
    @jsii.member(jsii_name="syslogInput")
    def syslog_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesSyslog"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesSyslog"]]], jsii.get(self, "syslogInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsEventLogInput")
    def windows_event_log_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesWindowsEventLog"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDataSourcesWindowsEventLog"]]], jsii.get(self, "windowsEventLogInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorDataCollectionRuleDataSources]:
        return typing.cast(typing.Optional[MonitorDataCollectionRuleDataSources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorDataCollectionRuleDataSources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesPerformanceCounter",
    jsii_struct_bases=[],
    name_mapping={
        "counter_specifiers": "counterSpecifiers",
        "name": "name",
        "sampling_frequency_in_seconds": "samplingFrequencyInSeconds",
        "streams": "streams",
    },
)
class MonitorDataCollectionRuleDataSourcesPerformanceCounter:
    def __init__(
        self,
        *,
        counter_specifiers: typing.Sequence[builtins.str],
        name: builtins.str,
        sampling_frequency_in_seconds: jsii.Number,
        streams: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param counter_specifiers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#counter_specifiers MonitorDataCollectionRule#counter_specifiers}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        :param sampling_frequency_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#sampling_frequency_in_seconds MonitorDataCollectionRule#sampling_frequency_in_seconds}.
        :param streams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#streams MonitorDataCollectionRule#streams}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesPerformanceCounter.__init__)
            check_type(argname="argument counter_specifiers", value=counter_specifiers, expected_type=type_hints["counter_specifiers"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sampling_frequency_in_seconds", value=sampling_frequency_in_seconds, expected_type=type_hints["sampling_frequency_in_seconds"])
            check_type(argname="argument streams", value=streams, expected_type=type_hints["streams"])
        self._values: typing.Dict[str, typing.Any] = {
            "counter_specifiers": counter_specifiers,
            "name": name,
            "sampling_frequency_in_seconds": sampling_frequency_in_seconds,
            "streams": streams,
        }

    @builtins.property
    def counter_specifiers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#counter_specifiers MonitorDataCollectionRule#counter_specifiers}.'''
        result = self._values.get("counter_specifiers")
        assert result is not None, "Required property 'counter_specifiers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sampling_frequency_in_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#sampling_frequency_in_seconds MonitorDataCollectionRule#sampling_frequency_in_seconds}.'''
        result = self._values.get("sampling_frequency_in_seconds")
        assert result is not None, "Required property 'sampling_frequency_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def streams(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#streams MonitorDataCollectionRule#streams}.'''
        result = self._values.get("streams")
        assert result is not None, "Required property 'streams' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDataSourcesPerformanceCounter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDataCollectionRuleDataSourcesPerformanceCounterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesPerformanceCounterList",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesPerformanceCounterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesPerformanceCounterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesPerformanceCounter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesPerformanceCounter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesPerformanceCounter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="counterSpecifiersInput")
    def counter_specifiers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "counterSpecifiersInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="samplingFrequencyInSecondsInput")
    def sampling_frequency_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingFrequencyInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="streamsInput")
    def streams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "streamsInput"))

    @builtins.property
    @jsii.member(jsii_name="counterSpecifiers")
    def counter_specifiers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "counterSpecifiers"))

    @counter_specifiers.setter
    def counter_specifiers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference, "counter_specifiers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "counterSpecifiers", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="samplingFrequencyInSeconds")
    def sampling_frequency_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingFrequencyInSeconds"))

    @sampling_frequency_in_seconds.setter
    def sampling_frequency_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference, "sampling_frequency_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingFrequencyInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="streams")
    def streams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "streams"))

    @streams.setter
    def streams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference, "streams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streams", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesPerformanceCounter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesPerformanceCounter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesPerformanceCounter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesSyslog",
    jsii_struct_bases=[],
    name_mapping={
        "facility_names": "facilityNames",
        "log_levels": "logLevels",
        "name": "name",
    },
)
class MonitorDataCollectionRuleDataSourcesSyslog:
    def __init__(
        self,
        *,
        facility_names: typing.Sequence[builtins.str],
        log_levels: typing.Sequence[builtins.str],
        name: builtins.str,
    ) -> None:
        '''
        :param facility_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#facility_names MonitorDataCollectionRule#facility_names}.
        :param log_levels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#log_levels MonitorDataCollectionRule#log_levels}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesSyslog.__init__)
            check_type(argname="argument facility_names", value=facility_names, expected_type=type_hints["facility_names"])
            check_type(argname="argument log_levels", value=log_levels, expected_type=type_hints["log_levels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "facility_names": facility_names,
            "log_levels": log_levels,
            "name": name,
        }

    @builtins.property
    def facility_names(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#facility_names MonitorDataCollectionRule#facility_names}.'''
        result = self._values.get("facility_names")
        assert result is not None, "Required property 'facility_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def log_levels(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#log_levels MonitorDataCollectionRule#log_levels}.'''
        result = self._values.get("log_levels")
        assert result is not None, "Required property 'log_levels' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDataSourcesSyslog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDataCollectionRuleDataSourcesSyslogList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesSyslogList",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesSyslogList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorDataCollectionRuleDataSourcesSyslogOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesSyslogList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorDataCollectionRuleDataSourcesSyslogOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesSyslogList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesSyslogList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesSyslogList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesSyslog]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesSyslog]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesSyslog]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesSyslogList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDataCollectionRuleDataSourcesSyslogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesSyslogOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesSyslogOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="facilityNamesInput")
    def facility_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "facilityNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelsInput")
    def log_levels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="facilityNames")
    def facility_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "facilityNames"))

    @facility_names.setter
    def facility_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesSyslogOutputReference, "facility_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "facilityNames", value)

    @builtins.property
    @jsii.member(jsii_name="logLevels")
    def log_levels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "logLevels"))

    @log_levels.setter
    def log_levels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesSyslogOutputReference, "log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesSyslogOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesSyslog, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesSyslog, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesSyslog, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesSyslogOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesWindowsEventLog",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "streams": "streams",
        "x_path_queries": "xPathQueries",
    },
)
class MonitorDataCollectionRuleDataSourcesWindowsEventLog:
    def __init__(
        self,
        *,
        name: builtins.str,
        streams: typing.Sequence[builtins.str],
        x_path_queries: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        :param streams: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#streams MonitorDataCollectionRule#streams}.
        :param x_path_queries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#x_path_queries MonitorDataCollectionRule#x_path_queries}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesWindowsEventLog.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument streams", value=streams, expected_type=type_hints["streams"])
            check_type(argname="argument x_path_queries", value=x_path_queries, expected_type=type_hints["x_path_queries"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "streams": streams,
            "x_path_queries": x_path_queries,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def streams(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#streams MonitorDataCollectionRule#streams}.'''
        result = self._values.get("streams")
        assert result is not None, "Required property 'streams' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def x_path_queries(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#x_path_queries MonitorDataCollectionRule#x_path_queries}.'''
        result = self._values.get("x_path_queries")
        assert result is not None, "Required property 'x_path_queries' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDataSourcesWindowsEventLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDataCollectionRuleDataSourcesWindowsEventLogList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesWindowsEventLogList",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesWindowsEventLogList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesWindowsEventLogList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesWindowsEventLogList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesWindowsEventLogList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesWindowsEventLogList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesWindowsEventLog]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesWindowsEventLog]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDataSourcesWindowsEventLog]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesWindowsEventLogList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference.__init__)
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
    @jsii.member(jsii_name="streamsInput")
    def streams_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "streamsInput"))

    @builtins.property
    @jsii.member(jsii_name="xPathQueriesInput")
    def x_path_queries_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xPathQueriesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="streams")
    def streams(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "streams"))

    @streams.setter
    def streams(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference, "streams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streams", value)

    @builtins.property
    @jsii.member(jsii_name="xPathQueries")
    def x_path_queries(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xPathQueries"))

    @x_path_queries.setter
    def x_path_queries(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference, "x_path_queries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xPathQueries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesWindowsEventLog, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesWindowsEventLog, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDataCollectionRuleDataSourcesWindowsEventLog, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDestinations",
    jsii_struct_bases=[],
    name_mapping={
        "azure_monitor_metrics": "azureMonitorMetrics",
        "log_analytics": "logAnalytics",
    },
)
class MonitorDataCollectionRuleDestinations:
    def __init__(
        self,
        *,
        azure_monitor_metrics: typing.Optional[typing.Union["MonitorDataCollectionRuleDestinationsAzureMonitorMetrics", typing.Dict[str, typing.Any]]] = None,
        log_analytics: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorDataCollectionRuleDestinationsLogAnalytics", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param azure_monitor_metrics: azure_monitor_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#azure_monitor_metrics MonitorDataCollectionRule#azure_monitor_metrics}
        :param log_analytics: log_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#log_analytics MonitorDataCollectionRule#log_analytics}
        '''
        if isinstance(azure_monitor_metrics, dict):
            azure_monitor_metrics = MonitorDataCollectionRuleDestinationsAzureMonitorMetrics(**azure_monitor_metrics)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinations.__init__)
            check_type(argname="argument azure_monitor_metrics", value=azure_monitor_metrics, expected_type=type_hints["azure_monitor_metrics"])
            check_type(argname="argument log_analytics", value=log_analytics, expected_type=type_hints["log_analytics"])
        self._values: typing.Dict[str, typing.Any] = {}
        if azure_monitor_metrics is not None:
            self._values["azure_monitor_metrics"] = azure_monitor_metrics
        if log_analytics is not None:
            self._values["log_analytics"] = log_analytics

    @builtins.property
    def azure_monitor_metrics(
        self,
    ) -> typing.Optional["MonitorDataCollectionRuleDestinationsAzureMonitorMetrics"]:
        '''azure_monitor_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#azure_monitor_metrics MonitorDataCollectionRule#azure_monitor_metrics}
        '''
        result = self._values.get("azure_monitor_metrics")
        return typing.cast(typing.Optional["MonitorDataCollectionRuleDestinationsAzureMonitorMetrics"], result)

    @builtins.property
    def log_analytics(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDestinationsLogAnalytics"]]]:
        '''log_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#log_analytics MonitorDataCollectionRule#log_analytics}
        '''
        result = self._values.get("log_analytics")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorDataCollectionRuleDestinationsLogAnalytics"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDestinations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDestinationsAzureMonitorMetrics",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class MonitorDataCollectionRuleDestinationsAzureMonitorMetrics:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinationsAzureMonitorMetrics.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDestinationsAzureMonitorMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDataCollectionRuleDestinationsAzureMonitorMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDestinationsAzureMonitorMetricsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinationsAzureMonitorMetricsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsAzureMonitorMetricsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorDataCollectionRuleDestinationsAzureMonitorMetrics]:
        return typing.cast(typing.Optional[MonitorDataCollectionRuleDestinationsAzureMonitorMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorDataCollectionRuleDestinationsAzureMonitorMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsAzureMonitorMetricsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDestinationsLogAnalytics",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "workspace_resource_id": "workspaceResourceId"},
)
class MonitorDataCollectionRuleDestinationsLogAnalytics:
    def __init__(
        self,
        *,
        name: builtins.str,
        workspace_resource_id: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        :param workspace_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#workspace_resource_id MonitorDataCollectionRule#workspace_resource_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinationsLogAnalytics.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument workspace_resource_id", value=workspace_resource_id, expected_type=type_hints["workspace_resource_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "workspace_resource_id": workspace_resource_id,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#workspace_resource_id MonitorDataCollectionRule#workspace_resource_id}.'''
        result = self._values.get("workspace_resource_id")
        assert result is not None, "Required property 'workspace_resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleDestinationsLogAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDataCollectionRuleDestinationsLogAnalyticsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDestinationsLogAnalyticsList",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinationsLogAnalyticsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinationsLogAnalyticsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsLogAnalyticsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsLogAnalyticsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsLogAnalyticsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDestinationsLogAnalytics]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDestinationsLogAnalytics]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDestinationsLogAnalytics]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsLogAnalyticsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference.__init__)
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
    @jsii.member(jsii_name="workspaceResourceIdInput")
    def workspace_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceResourceId")
    def workspace_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceResourceId"))

    @workspace_resource_id.setter
    def workspace_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference, "workspace_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDataCollectionRuleDestinationsLogAnalytics, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDataCollectionRuleDestinationsLogAnalytics, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDataCollectionRuleDestinationsLogAnalytics, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorDataCollectionRuleDestinationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleDestinationsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAzureMonitorMetrics")
    def put_azure_monitor_metrics(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#name MonitorDataCollectionRule#name}.
        '''
        value = MonitorDataCollectionRuleDestinationsAzureMonitorMetrics(name=name)

        return typing.cast(None, jsii.invoke(self, "putAzureMonitorMetrics", [value]))

    @jsii.member(jsii_name="putLogAnalytics")
    def put_log_analytics(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorDataCollectionRuleDestinationsLogAnalytics, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleDestinationsOutputReference.put_log_analytics)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogAnalytics", [value]))

    @jsii.member(jsii_name="resetAzureMonitorMetrics")
    def reset_azure_monitor_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureMonitorMetrics", []))

    @jsii.member(jsii_name="resetLogAnalytics")
    def reset_log_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogAnalytics", []))

    @builtins.property
    @jsii.member(jsii_name="azureMonitorMetrics")
    def azure_monitor_metrics(
        self,
    ) -> MonitorDataCollectionRuleDestinationsAzureMonitorMetricsOutputReference:
        return typing.cast(MonitorDataCollectionRuleDestinationsAzureMonitorMetricsOutputReference, jsii.get(self, "azureMonitorMetrics"))

    @builtins.property
    @jsii.member(jsii_name="logAnalytics")
    def log_analytics(self) -> MonitorDataCollectionRuleDestinationsLogAnalyticsList:
        return typing.cast(MonitorDataCollectionRuleDestinationsLogAnalyticsList, jsii.get(self, "logAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="azureMonitorMetricsInput")
    def azure_monitor_metrics_input(
        self,
    ) -> typing.Optional[MonitorDataCollectionRuleDestinationsAzureMonitorMetrics]:
        return typing.cast(typing.Optional[MonitorDataCollectionRuleDestinationsAzureMonitorMetrics], jsii.get(self, "azureMonitorMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsInput")
    def log_analytics_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDestinationsLogAnalytics]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorDataCollectionRuleDestinationsLogAnalytics]]], jsii.get(self, "logAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorDataCollectionRuleDestinations]:
        return typing.cast(typing.Optional[MonitorDataCollectionRuleDestinations], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorDataCollectionRuleDestinations],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleDestinationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MonitorDataCollectionRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#create MonitorDataCollectionRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#delete MonitorDataCollectionRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#read MonitorDataCollectionRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#update MonitorDataCollectionRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#create MonitorDataCollectionRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#delete MonitorDataCollectionRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#read MonitorDataCollectionRule#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_data_collection_rule#update MonitorDataCollectionRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorDataCollectionRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorDataCollectionRuleTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorDataCollectionRule.MonitorDataCollectionRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorDataCollectionRuleTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorDataCollectionRuleTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorDataCollectionRuleTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorDataCollectionRuleTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorDataCollectionRuleTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MonitorDataCollectionRule",
    "MonitorDataCollectionRuleConfig",
    "MonitorDataCollectionRuleDataFlow",
    "MonitorDataCollectionRuleDataFlowList",
    "MonitorDataCollectionRuleDataFlowOutputReference",
    "MonitorDataCollectionRuleDataSources",
    "MonitorDataCollectionRuleDataSourcesExtension",
    "MonitorDataCollectionRuleDataSourcesExtensionList",
    "MonitorDataCollectionRuleDataSourcesExtensionOutputReference",
    "MonitorDataCollectionRuleDataSourcesOutputReference",
    "MonitorDataCollectionRuleDataSourcesPerformanceCounter",
    "MonitorDataCollectionRuleDataSourcesPerformanceCounterList",
    "MonitorDataCollectionRuleDataSourcesPerformanceCounterOutputReference",
    "MonitorDataCollectionRuleDataSourcesSyslog",
    "MonitorDataCollectionRuleDataSourcesSyslogList",
    "MonitorDataCollectionRuleDataSourcesSyslogOutputReference",
    "MonitorDataCollectionRuleDataSourcesWindowsEventLog",
    "MonitorDataCollectionRuleDataSourcesWindowsEventLogList",
    "MonitorDataCollectionRuleDataSourcesWindowsEventLogOutputReference",
    "MonitorDataCollectionRuleDestinations",
    "MonitorDataCollectionRuleDestinationsAzureMonitorMetrics",
    "MonitorDataCollectionRuleDestinationsAzureMonitorMetricsOutputReference",
    "MonitorDataCollectionRuleDestinationsLogAnalytics",
    "MonitorDataCollectionRuleDestinationsLogAnalyticsList",
    "MonitorDataCollectionRuleDestinationsLogAnalyticsOutputReference",
    "MonitorDataCollectionRuleDestinationsOutputReference",
    "MonitorDataCollectionRuleTimeouts",
    "MonitorDataCollectionRuleTimeoutsOutputReference",
]

publication.publish()
