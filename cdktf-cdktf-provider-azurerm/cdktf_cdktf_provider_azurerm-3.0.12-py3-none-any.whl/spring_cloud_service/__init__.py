'''
# `azurerm_spring_cloud_service`

Refer to the Terraform Registory for docs: [`azurerm_spring_cloud_service`](https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service).
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


class SpringCloudService(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service azurerm_spring_cloud_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        build_agent_pool_size: typing.Optional[builtins.str] = None,
        config_server_git_setting: typing.Optional[typing.Union["SpringCloudServiceConfigServerGitSetting", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        log_stream_public_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network: typing.Optional[typing.Union["SpringCloudServiceNetwork", typing.Dict[str, typing.Any]]] = None,
        service_registry_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sku_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        trace: typing.Optional[typing.Union["SpringCloudServiceTrace", typing.Dict[str, typing.Any]]] = None,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service azurerm_spring_cloud_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#location SpringCloudService#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#name SpringCloudService#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#resource_group_name SpringCloudService#resource_group_name}.
        :param build_agent_pool_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#build_agent_pool_size SpringCloudService#build_agent_pool_size}.
        :param config_server_git_setting: config_server_git_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#config_server_git_setting SpringCloudService#config_server_git_setting}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#id SpringCloudService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_stream_public_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#log_stream_public_endpoint_enabled SpringCloudService#log_stream_public_endpoint_enabled}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#network SpringCloudService#network}
        :param service_registry_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_registry_enabled SpringCloudService#service_registry_enabled}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#sku_name SpringCloudService#sku_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#tags SpringCloudService#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#timeouts SpringCloudService#timeouts}
        :param trace: trace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#trace SpringCloudService#trace}
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#zone_redundant SpringCloudService#zone_redundant}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SpringCloudServiceConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            build_agent_pool_size=build_agent_pool_size,
            config_server_git_setting=config_server_git_setting,
            id=id,
            log_stream_public_endpoint_enabled=log_stream_public_endpoint_enabled,
            network=network,
            service_registry_enabled=service_registry_enabled,
            sku_name=sku_name,
            tags=tags,
            timeouts=timeouts,
            trace=trace,
            zone_redundant=zone_redundant,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConfigServerGitSetting")
    def put_config_server_git_setting(
        self,
        *,
        uri: builtins.str,
        http_basic_auth: typing.Optional[typing.Union["SpringCloudServiceConfigServerGitSettingHttpBasicAuth", typing.Dict[str, typing.Any]]] = None,
        label: typing.Optional[builtins.str] = None,
        repository: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SpringCloudServiceConfigServerGitSettingRepository", typing.Dict[str, typing.Any]]]]] = None,
        search_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        ssh_auth: typing.Optional[typing.Union["SpringCloudServiceConfigServerGitSettingSshAuth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#uri SpringCloudService#uri}.
        :param http_basic_auth: http_basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#http_basic_auth SpringCloudService#http_basic_auth}
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#label SpringCloudService#label}.
        :param repository: repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#repository SpringCloudService#repository}
        :param search_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#search_paths SpringCloudService#search_paths}.
        :param ssh_auth: ssh_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#ssh_auth SpringCloudService#ssh_auth}
        '''
        value = SpringCloudServiceConfigServerGitSetting(
            uri=uri,
            http_basic_auth=http_basic_auth,
            label=label,
            repository=repository,
            search_paths=search_paths,
            ssh_auth=ssh_auth,
        )

        return typing.cast(None, jsii.invoke(self, "putConfigServerGitSetting", [value]))

    @jsii.member(jsii_name="putNetwork")
    def put_network(
        self,
        *,
        app_subnet_id: builtins.str,
        cidr_ranges: typing.Sequence[builtins.str],
        service_runtime_subnet_id: builtins.str,
        app_network_resource_group: typing.Optional[builtins.str] = None,
        read_timeout_seconds: typing.Optional[jsii.Number] = None,
        service_runtime_network_resource_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param app_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#app_subnet_id SpringCloudService#app_subnet_id}.
        :param cidr_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#cidr_ranges SpringCloudService#cidr_ranges}.
        :param service_runtime_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_runtime_subnet_id SpringCloudService#service_runtime_subnet_id}.
        :param app_network_resource_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#app_network_resource_group SpringCloudService#app_network_resource_group}.
        :param read_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#read_timeout_seconds SpringCloudService#read_timeout_seconds}.
        :param service_runtime_network_resource_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_runtime_network_resource_group SpringCloudService#service_runtime_network_resource_group}.
        '''
        value = SpringCloudServiceNetwork(
            app_subnet_id=app_subnet_id,
            cidr_ranges=cidr_ranges,
            service_runtime_subnet_id=service_runtime_subnet_id,
            app_network_resource_group=app_network_resource_group,
            read_timeout_seconds=read_timeout_seconds,
            service_runtime_network_resource_group=service_runtime_network_resource_group,
        )

        return typing.cast(None, jsii.invoke(self, "putNetwork", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#create SpringCloudService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#delete SpringCloudService#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#read SpringCloudService#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#update SpringCloudService#update}.
        '''
        value = SpringCloudServiceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTrace")
    def put_trace(
        self,
        *,
        connection_string: typing.Optional[builtins.str] = None,
        sample_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#connection_string SpringCloudService#connection_string}.
        :param sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#sample_rate SpringCloudService#sample_rate}.
        '''
        value = SpringCloudServiceTrace(
            connection_string=connection_string, sample_rate=sample_rate
        )

        return typing.cast(None, jsii.invoke(self, "putTrace", [value]))

    @jsii.member(jsii_name="resetBuildAgentPoolSize")
    def reset_build_agent_pool_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildAgentPoolSize", []))

    @jsii.member(jsii_name="resetConfigServerGitSetting")
    def reset_config_server_git_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigServerGitSetting", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogStreamPublicEndpointEnabled")
    def reset_log_stream_public_endpoint_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamPublicEndpointEnabled", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetServiceRegistryEnabled")
    def reset_service_registry_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRegistryEnabled", []))

    @jsii.member(jsii_name="resetSkuName")
    def reset_sku_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkuName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTrace")
    def reset_trace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrace", []))

    @jsii.member(jsii_name="resetZoneRedundant")
    def reset_zone_redundant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneRedundant", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="configServerGitSetting")
    def config_server_git_setting(
        self,
    ) -> "SpringCloudServiceConfigServerGitSettingOutputReference":
        return typing.cast("SpringCloudServiceConfigServerGitSettingOutputReference", jsii.get(self, "configServerGitSetting"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> "SpringCloudServiceNetworkOutputReference":
        return typing.cast("SpringCloudServiceNetworkOutputReference", jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="outboundPublicIpAddresses")
    def outbound_public_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "outboundPublicIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="requiredNetworkTrafficRules")
    def required_network_traffic_rules(
        self,
    ) -> "SpringCloudServiceRequiredNetworkTrafficRulesList":
        return typing.cast("SpringCloudServiceRequiredNetworkTrafficRulesList", jsii.get(self, "requiredNetworkTrafficRules"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistryId")
    def service_registry_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRegistryId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SpringCloudServiceTimeoutsOutputReference":
        return typing.cast("SpringCloudServiceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="trace")
    def trace(self) -> "SpringCloudServiceTraceOutputReference":
        return typing.cast("SpringCloudServiceTraceOutputReference", jsii.get(self, "trace"))

    @builtins.property
    @jsii.member(jsii_name="buildAgentPoolSizeInput")
    def build_agent_pool_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildAgentPoolSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="configServerGitSettingInput")
    def config_server_git_setting_input(
        self,
    ) -> typing.Optional["SpringCloudServiceConfigServerGitSetting"]:
        return typing.cast(typing.Optional["SpringCloudServiceConfigServerGitSetting"], jsii.get(self, "configServerGitSettingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamPublicEndpointEnabledInput")
    def log_stream_public_endpoint_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logStreamPublicEndpointEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional["SpringCloudServiceNetwork"]:
        return typing.cast(typing.Optional["SpringCloudServiceNetwork"], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistryEnabledInput")
    def service_registry_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "serviceRegistryEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SpringCloudServiceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SpringCloudServiceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="traceInput")
    def trace_input(self) -> typing.Optional["SpringCloudServiceTrace"]:
        return typing.cast(typing.Optional["SpringCloudServiceTrace"], jsii.get(self, "traceInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneRedundantInput")
    def zone_redundant_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "zoneRedundantInput"))

    @builtins.property
    @jsii.member(jsii_name="buildAgentPoolSize")
    def build_agent_pool_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildAgentPoolSize"))

    @build_agent_pool_size.setter
    def build_agent_pool_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "build_agent_pool_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildAgentPoolSize", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamPublicEndpointEnabled")
    def log_stream_public_endpoint_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logStreamPublicEndpointEnabled"))

    @log_stream_public_endpoint_enabled.setter
    def log_stream_public_endpoint_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "log_stream_public_endpoint_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamPublicEndpointEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRegistryEnabled")
    def service_registry_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "serviceRegistryEnabled"))

    @service_registry_enabled.setter
    def service_registry_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "service_registry_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRegistryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="zoneRedundant")
    def zone_redundant(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "zoneRedundant"))

    @zone_redundant.setter
    def zone_redundant(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudService, "zone_redundant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneRedundant", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "build_agent_pool_size": "buildAgentPoolSize",
        "config_server_git_setting": "configServerGitSetting",
        "id": "id",
        "log_stream_public_endpoint_enabled": "logStreamPublicEndpointEnabled",
        "network": "network",
        "service_registry_enabled": "serviceRegistryEnabled",
        "sku_name": "skuName",
        "tags": "tags",
        "timeouts": "timeouts",
        "trace": "trace",
        "zone_redundant": "zoneRedundant",
    },
)
class SpringCloudServiceConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        build_agent_pool_size: typing.Optional[builtins.str] = None,
        config_server_git_setting: typing.Optional[typing.Union["SpringCloudServiceConfigServerGitSetting", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        log_stream_public_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network: typing.Optional[typing.Union["SpringCloudServiceNetwork", typing.Dict[str, typing.Any]]] = None,
        service_registry_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sku_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SpringCloudServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        trace: typing.Optional[typing.Union["SpringCloudServiceTrace", typing.Dict[str, typing.Any]]] = None,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#location SpringCloudService#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#name SpringCloudService#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#resource_group_name SpringCloudService#resource_group_name}.
        :param build_agent_pool_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#build_agent_pool_size SpringCloudService#build_agent_pool_size}.
        :param config_server_git_setting: config_server_git_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#config_server_git_setting SpringCloudService#config_server_git_setting}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#id SpringCloudService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_stream_public_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#log_stream_public_endpoint_enabled SpringCloudService#log_stream_public_endpoint_enabled}.
        :param network: network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#network SpringCloudService#network}
        :param service_registry_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_registry_enabled SpringCloudService#service_registry_enabled}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#sku_name SpringCloudService#sku_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#tags SpringCloudService#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#timeouts SpringCloudService#timeouts}
        :param trace: trace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#trace SpringCloudService#trace}
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#zone_redundant SpringCloudService#zone_redundant}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(config_server_git_setting, dict):
            config_server_git_setting = SpringCloudServiceConfigServerGitSetting(**config_server_git_setting)
        if isinstance(network, dict):
            network = SpringCloudServiceNetwork(**network)
        if isinstance(timeouts, dict):
            timeouts = SpringCloudServiceTimeouts(**timeouts)
        if isinstance(trace, dict):
            trace = SpringCloudServiceTrace(**trace)
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument build_agent_pool_size", value=build_agent_pool_size, expected_type=type_hints["build_agent_pool_size"])
            check_type(argname="argument config_server_git_setting", value=config_server_git_setting, expected_type=type_hints["config_server_git_setting"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_stream_public_endpoint_enabled", value=log_stream_public_endpoint_enabled, expected_type=type_hints["log_stream_public_endpoint_enabled"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument service_registry_enabled", value=service_registry_enabled, expected_type=type_hints["service_registry_enabled"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument trace", value=trace, expected_type=type_hints["trace"])
            check_type(argname="argument zone_redundant", value=zone_redundant, expected_type=type_hints["zone_redundant"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if build_agent_pool_size is not None:
            self._values["build_agent_pool_size"] = build_agent_pool_size
        if config_server_git_setting is not None:
            self._values["config_server_git_setting"] = config_server_git_setting
        if id is not None:
            self._values["id"] = id
        if log_stream_public_endpoint_enabled is not None:
            self._values["log_stream_public_endpoint_enabled"] = log_stream_public_endpoint_enabled
        if network is not None:
            self._values["network"] = network
        if service_registry_enabled is not None:
            self._values["service_registry_enabled"] = service_registry_enabled
        if sku_name is not None:
            self._values["sku_name"] = sku_name
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if trace is not None:
            self._values["trace"] = trace
        if zone_redundant is not None:
            self._values["zone_redundant"] = zone_redundant

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#location SpringCloudService#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#name SpringCloudService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#resource_group_name SpringCloudService#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_agent_pool_size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#build_agent_pool_size SpringCloudService#build_agent_pool_size}.'''
        result = self._values.get("build_agent_pool_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_server_git_setting(
        self,
    ) -> typing.Optional["SpringCloudServiceConfigServerGitSetting"]:
        '''config_server_git_setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#config_server_git_setting SpringCloudService#config_server_git_setting}
        '''
        result = self._values.get("config_server_git_setting")
        return typing.cast(typing.Optional["SpringCloudServiceConfigServerGitSetting"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#id SpringCloudService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_public_endpoint_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#log_stream_public_endpoint_enabled SpringCloudService#log_stream_public_endpoint_enabled}.'''
        result = self._values.get("log_stream_public_endpoint_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def network(self) -> typing.Optional["SpringCloudServiceNetwork"]:
        '''network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#network SpringCloudService#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional["SpringCloudServiceNetwork"], result)

    @builtins.property
    def service_registry_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_registry_enabled SpringCloudService#service_registry_enabled}.'''
        result = self._values.get("service_registry_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sku_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#sku_name SpringCloudService#sku_name}.'''
        result = self._values.get("sku_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#tags SpringCloudService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SpringCloudServiceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#timeouts SpringCloudService#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SpringCloudServiceTimeouts"], result)

    @builtins.property
    def trace(self) -> typing.Optional["SpringCloudServiceTrace"]:
        '''trace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#trace SpringCloudService#trace}
        '''
        result = self._values.get("trace")
        return typing.cast(typing.Optional["SpringCloudServiceTrace"], result)

    @builtins.property
    def zone_redundant(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#zone_redundant SpringCloudService#zone_redundant}.'''
        result = self._values.get("zone_redundant")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSetting",
    jsii_struct_bases=[],
    name_mapping={
        "uri": "uri",
        "http_basic_auth": "httpBasicAuth",
        "label": "label",
        "repository": "repository",
        "search_paths": "searchPaths",
        "ssh_auth": "sshAuth",
    },
)
class SpringCloudServiceConfigServerGitSetting:
    def __init__(
        self,
        *,
        uri: builtins.str,
        http_basic_auth: typing.Optional[typing.Union["SpringCloudServiceConfigServerGitSettingHttpBasicAuth", typing.Dict[str, typing.Any]]] = None,
        label: typing.Optional[builtins.str] = None,
        repository: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SpringCloudServiceConfigServerGitSettingRepository", typing.Dict[str, typing.Any]]]]] = None,
        search_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        ssh_auth: typing.Optional[typing.Union["SpringCloudServiceConfigServerGitSettingSshAuth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#uri SpringCloudService#uri}.
        :param http_basic_auth: http_basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#http_basic_auth SpringCloudService#http_basic_auth}
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#label SpringCloudService#label}.
        :param repository: repository block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#repository SpringCloudService#repository}
        :param search_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#search_paths SpringCloudService#search_paths}.
        :param ssh_auth: ssh_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#ssh_auth SpringCloudService#ssh_auth}
        '''
        if isinstance(http_basic_auth, dict):
            http_basic_auth = SpringCloudServiceConfigServerGitSettingHttpBasicAuth(**http_basic_auth)
        if isinstance(ssh_auth, dict):
            ssh_auth = SpringCloudServiceConfigServerGitSettingSshAuth(**ssh_auth)
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSetting.__init__)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument http_basic_auth", value=http_basic_auth, expected_type=type_hints["http_basic_auth"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument search_paths", value=search_paths, expected_type=type_hints["search_paths"])
            check_type(argname="argument ssh_auth", value=ssh_auth, expected_type=type_hints["ssh_auth"])
        self._values: typing.Dict[str, typing.Any] = {
            "uri": uri,
        }
        if http_basic_auth is not None:
            self._values["http_basic_auth"] = http_basic_auth
        if label is not None:
            self._values["label"] = label
        if repository is not None:
            self._values["repository"] = repository
        if search_paths is not None:
            self._values["search_paths"] = search_paths
        if ssh_auth is not None:
            self._values["ssh_auth"] = ssh_auth

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#uri SpringCloudService#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_basic_auth(
        self,
    ) -> typing.Optional["SpringCloudServiceConfigServerGitSettingHttpBasicAuth"]:
        '''http_basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#http_basic_auth SpringCloudService#http_basic_auth}
        '''
        result = self._values.get("http_basic_auth")
        return typing.cast(typing.Optional["SpringCloudServiceConfigServerGitSettingHttpBasicAuth"], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#label SpringCloudService#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SpringCloudServiceConfigServerGitSettingRepository"]]]:
        '''repository block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#repository SpringCloudService#repository}
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SpringCloudServiceConfigServerGitSettingRepository"]]], result)

    @builtins.property
    def search_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#search_paths SpringCloudService#search_paths}.'''
        result = self._values.get("search_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ssh_auth(
        self,
    ) -> typing.Optional["SpringCloudServiceConfigServerGitSettingSshAuth"]:
        '''ssh_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#ssh_auth SpringCloudService#ssh_auth}
        '''
        result = self._values.get("ssh_auth")
        return typing.cast(typing.Optional["SpringCloudServiceConfigServerGitSettingSshAuth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceConfigServerGitSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingHttpBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class SpringCloudServiceConfigServerGitSettingHttpBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#password SpringCloudService#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#username SpringCloudService#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingHttpBasicAuth.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#password SpringCloudService#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#username SpringCloudService#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceConfigServerGitSettingHttpBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpringCloudServiceConfigServerGitSettingHttpBasicAuth]:
        return typing.cast(typing.Optional[SpringCloudServiceConfigServerGitSettingHttpBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudServiceConfigServerGitSettingHttpBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SpringCloudServiceConfigServerGitSettingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHttpBasicAuth")
    def put_http_basic_auth(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#password SpringCloudService#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#username SpringCloudService#username}.
        '''
        value = SpringCloudServiceConfigServerGitSettingHttpBasicAuth(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putHttpBasicAuth", [value]))

    @jsii.member(jsii_name="putRepository")
    def put_repository(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SpringCloudServiceConfigServerGitSettingRepository", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingOutputReference.put_repository)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRepository", [value]))

    @jsii.member(jsii_name="putSshAuth")
    def put_ssh_auth(
        self,
        *,
        private_key: builtins.str,
        host_key: typing.Optional[builtins.str] = None,
        host_key_algorithm: typing.Optional[builtins.str] = None,
        strict_host_key_checking_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#private_key SpringCloudService#private_key}.
        :param host_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key SpringCloudService#host_key}.
        :param host_key_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key_algorithm SpringCloudService#host_key_algorithm}.
        :param strict_host_key_checking_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#strict_host_key_checking_enabled SpringCloudService#strict_host_key_checking_enabled}.
        '''
        value = SpringCloudServiceConfigServerGitSettingSshAuth(
            private_key=private_key,
            host_key=host_key,
            host_key_algorithm=host_key_algorithm,
            strict_host_key_checking_enabled=strict_host_key_checking_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putSshAuth", [value]))

    @jsii.member(jsii_name="resetHttpBasicAuth")
    def reset_http_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpBasicAuth", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetRepository")
    def reset_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepository", []))

    @jsii.member(jsii_name="resetSearchPaths")
    def reset_search_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchPaths", []))

    @jsii.member(jsii_name="resetSshAuth")
    def reset_ssh_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshAuth", []))

    @builtins.property
    @jsii.member(jsii_name="httpBasicAuth")
    def http_basic_auth(
        self,
    ) -> SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference:
        return typing.cast(SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference, jsii.get(self, "httpBasicAuth"))

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> "SpringCloudServiceConfigServerGitSettingRepositoryList":
        return typing.cast("SpringCloudServiceConfigServerGitSettingRepositoryList", jsii.get(self, "repository"))

    @builtins.property
    @jsii.member(jsii_name="sshAuth")
    def ssh_auth(
        self,
    ) -> "SpringCloudServiceConfigServerGitSettingSshAuthOutputReference":
        return typing.cast("SpringCloudServiceConfigServerGitSettingSshAuthOutputReference", jsii.get(self, "sshAuth"))

    @builtins.property
    @jsii.member(jsii_name="httpBasicAuthInput")
    def http_basic_auth_input(
        self,
    ) -> typing.Optional[SpringCloudServiceConfigServerGitSettingHttpBasicAuth]:
        return typing.cast(typing.Optional[SpringCloudServiceConfigServerGitSettingHttpBasicAuth], jsii.get(self, "httpBasicAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SpringCloudServiceConfigServerGitSettingRepository"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SpringCloudServiceConfigServerGitSettingRepository"]]], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="searchPathsInput")
    def search_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "searchPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="sshAuthInput")
    def ssh_auth_input(
        self,
    ) -> typing.Optional["SpringCloudServiceConfigServerGitSettingSshAuth"]:
        return typing.cast(typing.Optional["SpringCloudServiceConfigServerGitSettingSshAuth"], jsii.get(self, "sshAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="searchPaths")
    def search_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "searchPaths"))

    @search_paths.setter
    def search_paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingOutputReference, "search_paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchPaths", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpringCloudServiceConfigServerGitSetting]:
        return typing.cast(typing.Optional[SpringCloudServiceConfigServerGitSetting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudServiceConfigServerGitSetting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingRepository",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "uri": "uri",
        "http_basic_auth": "httpBasicAuth",
        "label": "label",
        "pattern": "pattern",
        "search_paths": "searchPaths",
        "ssh_auth": "sshAuth",
    },
)
class SpringCloudServiceConfigServerGitSettingRepository:
    def __init__(
        self,
        *,
        name: builtins.str,
        uri: builtins.str,
        http_basic_auth: typing.Optional[typing.Union["SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth", typing.Dict[str, typing.Any]]] = None,
        label: typing.Optional[builtins.str] = None,
        pattern: typing.Optional[typing.Sequence[builtins.str]] = None,
        search_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        ssh_auth: typing.Optional[typing.Union["SpringCloudServiceConfigServerGitSettingRepositorySshAuth", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#name SpringCloudService#name}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#uri SpringCloudService#uri}.
        :param http_basic_auth: http_basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#http_basic_auth SpringCloudService#http_basic_auth}
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#label SpringCloudService#label}.
        :param pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#pattern SpringCloudService#pattern}.
        :param search_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#search_paths SpringCloudService#search_paths}.
        :param ssh_auth: ssh_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#ssh_auth SpringCloudService#ssh_auth}
        '''
        if isinstance(http_basic_auth, dict):
            http_basic_auth = SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth(**http_basic_auth)
        if isinstance(ssh_auth, dict):
            ssh_auth = SpringCloudServiceConfigServerGitSettingRepositorySshAuth(**ssh_auth)
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingRepository.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument http_basic_auth", value=http_basic_auth, expected_type=type_hints["http_basic_auth"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument search_paths", value=search_paths, expected_type=type_hints["search_paths"])
            check_type(argname="argument ssh_auth", value=ssh_auth, expected_type=type_hints["ssh_auth"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "uri": uri,
        }
        if http_basic_auth is not None:
            self._values["http_basic_auth"] = http_basic_auth
        if label is not None:
            self._values["label"] = label
        if pattern is not None:
            self._values["pattern"] = pattern
        if search_paths is not None:
            self._values["search_paths"] = search_paths
        if ssh_auth is not None:
            self._values["ssh_auth"] = ssh_auth

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#name SpringCloudService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#uri SpringCloudService#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_basic_auth(
        self,
    ) -> typing.Optional["SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth"]:
        '''http_basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#http_basic_auth SpringCloudService#http_basic_auth}
        '''
        result = self._values.get("http_basic_auth")
        return typing.cast(typing.Optional["SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth"], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#label SpringCloudService#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pattern(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#pattern SpringCloudService#pattern}.'''
        result = self._values.get("pattern")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def search_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#search_paths SpringCloudService#search_paths}.'''
        result = self._values.get("search_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ssh_auth(
        self,
    ) -> typing.Optional["SpringCloudServiceConfigServerGitSettingRepositorySshAuth"]:
        '''ssh_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#ssh_auth SpringCloudService#ssh_auth}
        '''
        result = self._values.get("ssh_auth")
        return typing.cast(typing.Optional["SpringCloudServiceConfigServerGitSettingRepositorySshAuth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceConfigServerGitSettingRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#password SpringCloudService#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#username SpringCloudService#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#password SpringCloudService#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#username SpringCloudService#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth]:
        return typing.cast(typing.Optional[SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SpringCloudServiceConfigServerGitSettingRepositoryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingRepositoryList",
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
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingRepositoryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SpringCloudServiceConfigServerGitSettingRepositoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingRepositoryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SpringCloudServiceConfigServerGitSettingRepositoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SpringCloudServiceConfigServerGitSettingRepository]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SpringCloudServiceConfigServerGitSettingRepository]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SpringCloudServiceConfigServerGitSettingRepository]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SpringCloudServiceConfigServerGitSettingRepositoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingRepositoryOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingRepositoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttpBasicAuth")
    def put_http_basic_auth(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#password SpringCloudService#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#username SpringCloudService#username}.
        '''
        value = SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putHttpBasicAuth", [value]))

    @jsii.member(jsii_name="putSshAuth")
    def put_ssh_auth(
        self,
        *,
        private_key: builtins.str,
        host_key: typing.Optional[builtins.str] = None,
        host_key_algorithm: typing.Optional[builtins.str] = None,
        strict_host_key_checking_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#private_key SpringCloudService#private_key}.
        :param host_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key SpringCloudService#host_key}.
        :param host_key_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key_algorithm SpringCloudService#host_key_algorithm}.
        :param strict_host_key_checking_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#strict_host_key_checking_enabled SpringCloudService#strict_host_key_checking_enabled}.
        '''
        value = SpringCloudServiceConfigServerGitSettingRepositorySshAuth(
            private_key=private_key,
            host_key=host_key,
            host_key_algorithm=host_key_algorithm,
            strict_host_key_checking_enabled=strict_host_key_checking_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putSshAuth", [value]))

    @jsii.member(jsii_name="resetHttpBasicAuth")
    def reset_http_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpBasicAuth", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetPattern")
    def reset_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPattern", []))

    @jsii.member(jsii_name="resetSearchPaths")
    def reset_search_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchPaths", []))

    @jsii.member(jsii_name="resetSshAuth")
    def reset_ssh_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshAuth", []))

    @builtins.property
    @jsii.member(jsii_name="httpBasicAuth")
    def http_basic_auth(
        self,
    ) -> SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference:
        return typing.cast(SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference, jsii.get(self, "httpBasicAuth"))

    @builtins.property
    @jsii.member(jsii_name="sshAuth")
    def ssh_auth(
        self,
    ) -> "SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference":
        return typing.cast("SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference", jsii.get(self, "sshAuth"))

    @builtins.property
    @jsii.member(jsii_name="httpBasicAuthInput")
    def http_basic_auth_input(
        self,
    ) -> typing.Optional[SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth]:
        return typing.cast(typing.Optional[SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth], jsii.get(self, "httpBasicAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patternInput"))

    @builtins.property
    @jsii.member(jsii_name="searchPathsInput")
    def search_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "searchPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="sshAuthInput")
    def ssh_auth_input(
        self,
    ) -> typing.Optional["SpringCloudServiceConfigServerGitSettingRepositorySshAuth"]:
        return typing.cast(typing.Optional["SpringCloudServiceConfigServerGitSettingRepositorySshAuth"], jsii.get(self, "sshAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryOutputReference, "pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="searchPaths")
    def search_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "searchPaths"))

    @search_paths.setter
    def search_paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryOutputReference, "search_paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchPaths", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpringCloudServiceConfigServerGitSettingRepository, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpringCloudServiceConfigServerGitSettingRepository, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpringCloudServiceConfigServerGitSettingRepository, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingRepositorySshAuth",
    jsii_struct_bases=[],
    name_mapping={
        "private_key": "privateKey",
        "host_key": "hostKey",
        "host_key_algorithm": "hostKeyAlgorithm",
        "strict_host_key_checking_enabled": "strictHostKeyCheckingEnabled",
    },
)
class SpringCloudServiceConfigServerGitSettingRepositorySshAuth:
    def __init__(
        self,
        *,
        private_key: builtins.str,
        host_key: typing.Optional[builtins.str] = None,
        host_key_algorithm: typing.Optional[builtins.str] = None,
        strict_host_key_checking_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#private_key SpringCloudService#private_key}.
        :param host_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key SpringCloudService#host_key}.
        :param host_key_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key_algorithm SpringCloudService#host_key_algorithm}.
        :param strict_host_key_checking_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#strict_host_key_checking_enabled SpringCloudService#strict_host_key_checking_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingRepositorySshAuth.__init__)
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument host_key", value=host_key, expected_type=type_hints["host_key"])
            check_type(argname="argument host_key_algorithm", value=host_key_algorithm, expected_type=type_hints["host_key_algorithm"])
            check_type(argname="argument strict_host_key_checking_enabled", value=strict_host_key_checking_enabled, expected_type=type_hints["strict_host_key_checking_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "private_key": private_key,
        }
        if host_key is not None:
            self._values["host_key"] = host_key
        if host_key_algorithm is not None:
            self._values["host_key_algorithm"] = host_key_algorithm
        if strict_host_key_checking_enabled is not None:
            self._values["strict_host_key_checking_enabled"] = strict_host_key_checking_enabled

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#private_key SpringCloudService#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key SpringCloudService#host_key}.'''
        result = self._values.get("host_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_key_algorithm(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key_algorithm SpringCloudService#host_key_algorithm}.'''
        result = self._values.get("host_key_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def strict_host_key_checking_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#strict_host_key_checking_enabled SpringCloudService#strict_host_key_checking_enabled}.'''
        result = self._values.get("strict_host_key_checking_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceConfigServerGitSettingRepositorySshAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostKey")
    def reset_host_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostKey", []))

    @jsii.member(jsii_name="resetHostKeyAlgorithm")
    def reset_host_key_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostKeyAlgorithm", []))

    @jsii.member(jsii_name="resetStrictHostKeyCheckingEnabled")
    def reset_strict_host_key_checking_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrictHostKeyCheckingEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="hostKeyAlgorithmInput")
    def host_key_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostKeyAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="hostKeyInput")
    def host_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="strictHostKeyCheckingEnabledInput")
    def strict_host_key_checking_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "strictHostKeyCheckingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="hostKey")
    def host_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostKey"))

    @host_key.setter
    def host_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference, "host_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostKey", value)

    @builtins.property
    @jsii.member(jsii_name="hostKeyAlgorithm")
    def host_key_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostKeyAlgorithm"))

    @host_key_algorithm.setter
    def host_key_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference, "host_key_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostKeyAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference, "private_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="strictHostKeyCheckingEnabled")
    def strict_host_key_checking_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "strictHostKeyCheckingEnabled"))

    @strict_host_key_checking_enabled.setter
    def strict_host_key_checking_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference, "strict_host_key_checking_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strictHostKeyCheckingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpringCloudServiceConfigServerGitSettingRepositorySshAuth]:
        return typing.cast(typing.Optional[SpringCloudServiceConfigServerGitSettingRepositorySshAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudServiceConfigServerGitSettingRepositorySshAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingSshAuth",
    jsii_struct_bases=[],
    name_mapping={
        "private_key": "privateKey",
        "host_key": "hostKey",
        "host_key_algorithm": "hostKeyAlgorithm",
        "strict_host_key_checking_enabled": "strictHostKeyCheckingEnabled",
    },
)
class SpringCloudServiceConfigServerGitSettingSshAuth:
    def __init__(
        self,
        *,
        private_key: builtins.str,
        host_key: typing.Optional[builtins.str] = None,
        host_key_algorithm: typing.Optional[builtins.str] = None,
        strict_host_key_checking_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#private_key SpringCloudService#private_key}.
        :param host_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key SpringCloudService#host_key}.
        :param host_key_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key_algorithm SpringCloudService#host_key_algorithm}.
        :param strict_host_key_checking_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#strict_host_key_checking_enabled SpringCloudService#strict_host_key_checking_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingSshAuth.__init__)
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument host_key", value=host_key, expected_type=type_hints["host_key"])
            check_type(argname="argument host_key_algorithm", value=host_key_algorithm, expected_type=type_hints["host_key_algorithm"])
            check_type(argname="argument strict_host_key_checking_enabled", value=strict_host_key_checking_enabled, expected_type=type_hints["strict_host_key_checking_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "private_key": private_key,
        }
        if host_key is not None:
            self._values["host_key"] = host_key
        if host_key_algorithm is not None:
            self._values["host_key_algorithm"] = host_key_algorithm
        if strict_host_key_checking_enabled is not None:
            self._values["strict_host_key_checking_enabled"] = strict_host_key_checking_enabled

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#private_key SpringCloudService#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key SpringCloudService#host_key}.'''
        result = self._values.get("host_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_key_algorithm(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#host_key_algorithm SpringCloudService#host_key_algorithm}.'''
        result = self._values.get("host_key_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def strict_host_key_checking_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#strict_host_key_checking_enabled SpringCloudService#strict_host_key_checking_enabled}.'''
        result = self._values.get("strict_host_key_checking_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceConfigServerGitSettingSshAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudServiceConfigServerGitSettingSshAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceConfigServerGitSettingSshAuthOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceConfigServerGitSettingSshAuthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHostKey")
    def reset_host_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostKey", []))

    @jsii.member(jsii_name="resetHostKeyAlgorithm")
    def reset_host_key_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostKeyAlgorithm", []))

    @jsii.member(jsii_name="resetStrictHostKeyCheckingEnabled")
    def reset_strict_host_key_checking_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrictHostKeyCheckingEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="hostKeyAlgorithmInput")
    def host_key_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostKeyAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="hostKeyInput")
    def host_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="strictHostKeyCheckingEnabledInput")
    def strict_host_key_checking_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "strictHostKeyCheckingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="hostKey")
    def host_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostKey"))

    @host_key.setter
    def host_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingSshAuthOutputReference, "host_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostKey", value)

    @builtins.property
    @jsii.member(jsii_name="hostKeyAlgorithm")
    def host_key_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostKeyAlgorithm"))

    @host_key_algorithm.setter
    def host_key_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingSshAuthOutputReference, "host_key_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostKeyAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingSshAuthOutputReference, "private_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="strictHostKeyCheckingEnabled")
    def strict_host_key_checking_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "strictHostKeyCheckingEnabled"))

    @strict_host_key_checking_enabled.setter
    def strict_host_key_checking_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingSshAuthOutputReference, "strict_host_key_checking_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strictHostKeyCheckingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpringCloudServiceConfigServerGitSettingSshAuth]:
        return typing.cast(typing.Optional[SpringCloudServiceConfigServerGitSettingSshAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudServiceConfigServerGitSettingSshAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceConfigServerGitSettingSshAuthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceNetwork",
    jsii_struct_bases=[],
    name_mapping={
        "app_subnet_id": "appSubnetId",
        "cidr_ranges": "cidrRanges",
        "service_runtime_subnet_id": "serviceRuntimeSubnetId",
        "app_network_resource_group": "appNetworkResourceGroup",
        "read_timeout_seconds": "readTimeoutSeconds",
        "service_runtime_network_resource_group": "serviceRuntimeNetworkResourceGroup",
    },
)
class SpringCloudServiceNetwork:
    def __init__(
        self,
        *,
        app_subnet_id: builtins.str,
        cidr_ranges: typing.Sequence[builtins.str],
        service_runtime_subnet_id: builtins.str,
        app_network_resource_group: typing.Optional[builtins.str] = None,
        read_timeout_seconds: typing.Optional[jsii.Number] = None,
        service_runtime_network_resource_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param app_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#app_subnet_id SpringCloudService#app_subnet_id}.
        :param cidr_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#cidr_ranges SpringCloudService#cidr_ranges}.
        :param service_runtime_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_runtime_subnet_id SpringCloudService#service_runtime_subnet_id}.
        :param app_network_resource_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#app_network_resource_group SpringCloudService#app_network_resource_group}.
        :param read_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#read_timeout_seconds SpringCloudService#read_timeout_seconds}.
        :param service_runtime_network_resource_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_runtime_network_resource_group SpringCloudService#service_runtime_network_resource_group}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceNetwork.__init__)
            check_type(argname="argument app_subnet_id", value=app_subnet_id, expected_type=type_hints["app_subnet_id"])
            check_type(argname="argument cidr_ranges", value=cidr_ranges, expected_type=type_hints["cidr_ranges"])
            check_type(argname="argument service_runtime_subnet_id", value=service_runtime_subnet_id, expected_type=type_hints["service_runtime_subnet_id"])
            check_type(argname="argument app_network_resource_group", value=app_network_resource_group, expected_type=type_hints["app_network_resource_group"])
            check_type(argname="argument read_timeout_seconds", value=read_timeout_seconds, expected_type=type_hints["read_timeout_seconds"])
            check_type(argname="argument service_runtime_network_resource_group", value=service_runtime_network_resource_group, expected_type=type_hints["service_runtime_network_resource_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_subnet_id": app_subnet_id,
            "cidr_ranges": cidr_ranges,
            "service_runtime_subnet_id": service_runtime_subnet_id,
        }
        if app_network_resource_group is not None:
            self._values["app_network_resource_group"] = app_network_resource_group
        if read_timeout_seconds is not None:
            self._values["read_timeout_seconds"] = read_timeout_seconds
        if service_runtime_network_resource_group is not None:
            self._values["service_runtime_network_resource_group"] = service_runtime_network_resource_group

    @builtins.property
    def app_subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#app_subnet_id SpringCloudService#app_subnet_id}.'''
        result = self._values.get("app_subnet_id")
        assert result is not None, "Required property 'app_subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_ranges(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#cidr_ranges SpringCloudService#cidr_ranges}.'''
        result = self._values.get("cidr_ranges")
        assert result is not None, "Required property 'cidr_ranges' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def service_runtime_subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_runtime_subnet_id SpringCloudService#service_runtime_subnet_id}.'''
        result = self._values.get("service_runtime_subnet_id")
        assert result is not None, "Required property 'service_runtime_subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_network_resource_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#app_network_resource_group SpringCloudService#app_network_resource_group}.'''
        result = self._values.get("app_network_resource_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#read_timeout_seconds SpringCloudService#read_timeout_seconds}.'''
        result = self._values.get("read_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_runtime_network_resource_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#service_runtime_network_resource_group SpringCloudService#service_runtime_network_resource_group}.'''
        result = self._values.get("service_runtime_network_resource_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudServiceNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceNetworkOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppNetworkResourceGroup")
    def reset_app_network_resource_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppNetworkResourceGroup", []))

    @jsii.member(jsii_name="resetReadTimeoutSeconds")
    def reset_read_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadTimeoutSeconds", []))

    @jsii.member(jsii_name="resetServiceRuntimeNetworkResourceGroup")
    def reset_service_runtime_network_resource_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRuntimeNetworkResourceGroup", []))

    @builtins.property
    @jsii.member(jsii_name="appNetworkResourceGroupInput")
    def app_network_resource_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appNetworkResourceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="appSubnetIdInput")
    def app_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrRangesInput")
    def cidr_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cidrRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="readTimeoutSecondsInput")
    def read_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRuntimeNetworkResourceGroupInput")
    def service_runtime_network_resource_group_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRuntimeNetworkResourceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRuntimeSubnetIdInput")
    def service_runtime_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRuntimeSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appNetworkResourceGroup")
    def app_network_resource_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appNetworkResourceGroup"))

    @app_network_resource_group.setter
    def app_network_resource_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceNetworkOutputReference, "app_network_resource_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appNetworkResourceGroup", value)

    @builtins.property
    @jsii.member(jsii_name="appSubnetId")
    def app_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSubnetId"))

    @app_subnet_id.setter
    def app_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceNetworkOutputReference, "app_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="cidrRanges")
    def cidr_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cidrRanges"))

    @cidr_ranges.setter
    def cidr_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceNetworkOutputReference, "cidr_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrRanges", value)

    @builtins.property
    @jsii.member(jsii_name="readTimeoutSeconds")
    def read_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readTimeoutSeconds"))

    @read_timeout_seconds.setter
    def read_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceNetworkOutputReference, "read_timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRuntimeNetworkResourceGroup")
    def service_runtime_network_resource_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRuntimeNetworkResourceGroup"))

    @service_runtime_network_resource_group.setter
    def service_runtime_network_resource_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceNetworkOutputReference, "service_runtime_network_resource_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRuntimeNetworkResourceGroup", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRuntimeSubnetId")
    def service_runtime_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRuntimeSubnetId"))

    @service_runtime_subnet_id.setter
    def service_runtime_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceNetworkOutputReference, "service_runtime_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRuntimeSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudServiceNetwork]:
        return typing.cast(typing.Optional[SpringCloudServiceNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SpringCloudServiceNetwork]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceRequiredNetworkTrafficRules",
    jsii_struct_bases=[],
    name_mapping={},
)
class SpringCloudServiceRequiredNetworkTrafficRules:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceRequiredNetworkTrafficRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudServiceRequiredNetworkTrafficRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceRequiredNetworkTrafficRulesList",
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
            type_hints = typing.get_type_hints(SpringCloudServiceRequiredNetworkTrafficRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SpringCloudServiceRequiredNetworkTrafficRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceRequiredNetworkTrafficRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SpringCloudServiceRequiredNetworkTrafficRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceRequiredNetworkTrafficRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceRequiredNetworkTrafficRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceRequiredNetworkTrafficRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class SpringCloudServiceRequiredNetworkTrafficRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceRequiredNetworkTrafficRulesOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceRequiredNetworkTrafficRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @builtins.property
    @jsii.member(jsii_name="fqdns")
    def fqdns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fqdns"))

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SpringCloudServiceRequiredNetworkTrafficRules]:
        return typing.cast(typing.Optional[SpringCloudServiceRequiredNetworkTrafficRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpringCloudServiceRequiredNetworkTrafficRules],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceRequiredNetworkTrafficRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SpringCloudServiceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#create SpringCloudService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#delete SpringCloudService#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#read SpringCloudService#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#update SpringCloudService#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#create SpringCloudService#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#delete SpringCloudService#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#read SpringCloudService#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#update SpringCloudService#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudServiceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SpringCloudServiceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SpringCloudServiceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SpringCloudServiceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceTrace",
    jsii_struct_bases=[],
    name_mapping={
        "connection_string": "connectionString",
        "sample_rate": "sampleRate",
    },
)
class SpringCloudServiceTrace:
    def __init__(
        self,
        *,
        connection_string: typing.Optional[builtins.str] = None,
        sample_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#connection_string SpringCloudService#connection_string}.
        :param sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#sample_rate SpringCloudService#sample_rate}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpringCloudServiceTrace.__init__)
            check_type(argname="argument connection_string", value=connection_string, expected_type=type_hints["connection_string"])
            check_type(argname="argument sample_rate", value=sample_rate, expected_type=type_hints["sample_rate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_string is not None:
            self._values["connection_string"] = connection_string
        if sample_rate is not None:
            self._values["sample_rate"] = sample_rate

    @builtins.property
    def connection_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#connection_string SpringCloudService#connection_string}.'''
        result = self._values.get("connection_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/spring_cloud_service#sample_rate SpringCloudService#sample_rate}.'''
        result = self._values.get("sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpringCloudServiceTrace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpringCloudServiceTraceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.springCloudService.SpringCloudServiceTraceOutputReference",
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
            type_hints = typing.get_type_hints(SpringCloudServiceTraceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectionString")
    def reset_connection_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionString", []))

    @jsii.member(jsii_name="resetSampleRate")
    def reset_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleRate", []))

    @builtins.property
    @jsii.member(jsii_name="connectionStringInput")
    def connection_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleRateInput")
    def sample_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionString"))

    @connection_string.setter
    def connection_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceTraceOutputReference, "connection_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionString", value)

    @builtins.property
    @jsii.member(jsii_name="sampleRate")
    def sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sampleRate"))

    @sample_rate.setter
    def sample_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceTraceOutputReference, "sample_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpringCloudServiceTrace]:
        return typing.cast(typing.Optional[SpringCloudServiceTrace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SpringCloudServiceTrace]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpringCloudServiceTraceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SpringCloudService",
    "SpringCloudServiceConfig",
    "SpringCloudServiceConfigServerGitSetting",
    "SpringCloudServiceConfigServerGitSettingHttpBasicAuth",
    "SpringCloudServiceConfigServerGitSettingHttpBasicAuthOutputReference",
    "SpringCloudServiceConfigServerGitSettingOutputReference",
    "SpringCloudServiceConfigServerGitSettingRepository",
    "SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuth",
    "SpringCloudServiceConfigServerGitSettingRepositoryHttpBasicAuthOutputReference",
    "SpringCloudServiceConfigServerGitSettingRepositoryList",
    "SpringCloudServiceConfigServerGitSettingRepositoryOutputReference",
    "SpringCloudServiceConfigServerGitSettingRepositorySshAuth",
    "SpringCloudServiceConfigServerGitSettingRepositorySshAuthOutputReference",
    "SpringCloudServiceConfigServerGitSettingSshAuth",
    "SpringCloudServiceConfigServerGitSettingSshAuthOutputReference",
    "SpringCloudServiceNetwork",
    "SpringCloudServiceNetworkOutputReference",
    "SpringCloudServiceRequiredNetworkTrafficRules",
    "SpringCloudServiceRequiredNetworkTrafficRulesList",
    "SpringCloudServiceRequiredNetworkTrafficRulesOutputReference",
    "SpringCloudServiceTimeouts",
    "SpringCloudServiceTimeoutsOutputReference",
    "SpringCloudServiceTrace",
    "SpringCloudServiceTraceOutputReference",
]

publication.publish()
