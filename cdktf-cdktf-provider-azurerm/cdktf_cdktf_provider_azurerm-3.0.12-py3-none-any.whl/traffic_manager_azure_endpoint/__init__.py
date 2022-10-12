'''
# `azurerm_traffic_manager_azure_endpoint`

Refer to the Terraform Registory for docs: [`azurerm_traffic_manager_azure_endpoint`](https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint).
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


class TrafficManagerAzureEndpoint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint azurerm_traffic_manager_azure_endpoint}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        profile_id: builtins.str,
        target_resource_id: builtins.str,
        custom_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TrafficManagerAzureEndpointCustomHeader", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        geo_mappings: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        subnet: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TrafficManagerAzureEndpointSubnet", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["TrafficManagerAzureEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
        weight: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint azurerm_traffic_manager_azure_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#name TrafficManagerAzureEndpoint#name}.
        :param profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#profile_id TrafficManagerAzureEndpoint#profile_id}.
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#target_resource_id TrafficManagerAzureEndpoint#target_resource_id}.
        :param custom_header: custom_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#custom_header TrafficManagerAzureEndpoint#custom_header}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#enabled TrafficManagerAzureEndpoint#enabled}.
        :param geo_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#geo_mappings TrafficManagerAzureEndpoint#geo_mappings}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#id TrafficManagerAzureEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#priority TrafficManagerAzureEndpoint#priority}.
        :param subnet: subnet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#subnet TrafficManagerAzureEndpoint#subnet}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#timeouts TrafficManagerAzureEndpoint#timeouts}
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#weight TrafficManagerAzureEndpoint#weight}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpoint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TrafficManagerAzureEndpointConfig(
            name=name,
            profile_id=profile_id,
            target_resource_id=target_resource_id,
            custom_header=custom_header,
            enabled=enabled,
            geo_mappings=geo_mappings,
            id=id,
            priority=priority,
            subnet=subnet,
            timeouts=timeouts,
            weight=weight,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCustomHeader")
    def put_custom_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TrafficManagerAzureEndpointCustomHeader", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpoint.put_custom_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomHeader", [value]))

    @jsii.member(jsii_name="putSubnet")
    def put_subnet(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TrafficManagerAzureEndpointSubnet", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpoint.put_subnet)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSubnet", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#create TrafficManagerAzureEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#delete TrafficManagerAzureEndpoint#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#read TrafficManagerAzureEndpoint#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#update TrafficManagerAzureEndpoint#update}.
        '''
        value = TrafficManagerAzureEndpointTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCustomHeader")
    def reset_custom_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeader", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetGeoMappings")
    def reset_geo_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoMappings", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customHeader")
    def custom_header(self) -> "TrafficManagerAzureEndpointCustomHeaderList":
        return typing.cast("TrafficManagerAzureEndpointCustomHeaderList", jsii.get(self, "customHeader"))

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> "TrafficManagerAzureEndpointSubnetList":
        return typing.cast("TrafficManagerAzureEndpointSubnetList", jsii.get(self, "subnet"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "TrafficManagerAzureEndpointTimeoutsOutputReference":
        return typing.cast("TrafficManagerAzureEndpointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderInput")
    def custom_header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TrafficManagerAzureEndpointCustomHeader"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TrafficManagerAzureEndpointCustomHeader"]]], jsii.get(self, "customHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="geoMappingsInput")
    def geo_mappings_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "geoMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="profileIdInput")
    def profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TrafficManagerAzureEndpointSubnet"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TrafficManagerAzureEndpointSubnet"]]], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceIdInput")
    def target_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["TrafficManagerAzureEndpointTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["TrafficManagerAzureEndpointTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpoint, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="geoMappings")
    def geo_mappings(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "geoMappings"))

    @geo_mappings.setter
    def geo_mappings(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpoint, "geo_mappings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoMappings", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpoint, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpoint, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpoint, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpoint, "profile_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceId")
    def target_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetResourceId"))

    @target_resource_id.setter
    def target_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpoint, "target_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpoint, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointConfig",
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
        "profile_id": "profileId",
        "target_resource_id": "targetResourceId",
        "custom_header": "customHeader",
        "enabled": "enabled",
        "geo_mappings": "geoMappings",
        "id": "id",
        "priority": "priority",
        "subnet": "subnet",
        "timeouts": "timeouts",
        "weight": "weight",
    },
)
class TrafficManagerAzureEndpointConfig(cdktf.TerraformMetaArguments):
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
        profile_id: builtins.str,
        target_resource_id: builtins.str,
        custom_header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TrafficManagerAzureEndpointCustomHeader", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        geo_mappings: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        subnet: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TrafficManagerAzureEndpointSubnet", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["TrafficManagerAzureEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#name TrafficManagerAzureEndpoint#name}.
        :param profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#profile_id TrafficManagerAzureEndpoint#profile_id}.
        :param target_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#target_resource_id TrafficManagerAzureEndpoint#target_resource_id}.
        :param custom_header: custom_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#custom_header TrafficManagerAzureEndpoint#custom_header}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#enabled TrafficManagerAzureEndpoint#enabled}.
        :param geo_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#geo_mappings TrafficManagerAzureEndpoint#geo_mappings}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#id TrafficManagerAzureEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#priority TrafficManagerAzureEndpoint#priority}.
        :param subnet: subnet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#subnet TrafficManagerAzureEndpoint#subnet}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#timeouts TrafficManagerAzureEndpoint#timeouts}
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#weight TrafficManagerAzureEndpoint#weight}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = TrafficManagerAzureEndpointTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
            check_type(argname="argument target_resource_id", value=target_resource_id, expected_type=type_hints["target_resource_id"])
            check_type(argname="argument custom_header", value=custom_header, expected_type=type_hints["custom_header"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument geo_mappings", value=geo_mappings, expected_type=type_hints["geo_mappings"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "profile_id": profile_id,
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
        if custom_header is not None:
            self._values["custom_header"] = custom_header
        if enabled is not None:
            self._values["enabled"] = enabled
        if geo_mappings is not None:
            self._values["geo_mappings"] = geo_mappings
        if id is not None:
            self._values["id"] = id
        if priority is not None:
            self._values["priority"] = priority
        if subnet is not None:
            self._values["subnet"] = subnet
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if weight is not None:
            self._values["weight"] = weight

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#name TrafficManagerAzureEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#profile_id TrafficManagerAzureEndpoint#profile_id}.'''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#target_resource_id TrafficManagerAzureEndpoint#target_resource_id}.'''
        result = self._values.get("target_resource_id")
        assert result is not None, "Required property 'target_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TrafficManagerAzureEndpointCustomHeader"]]]:
        '''custom_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#custom_header TrafficManagerAzureEndpoint#custom_header}
        '''
        result = self._values.get("custom_header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TrafficManagerAzureEndpointCustomHeader"]]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#enabled TrafficManagerAzureEndpoint#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def geo_mappings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#geo_mappings TrafficManagerAzureEndpoint#geo_mappings}.'''
        result = self._values.get("geo_mappings")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#id TrafficManagerAzureEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#priority TrafficManagerAzureEndpoint#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subnet(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TrafficManagerAzureEndpointSubnet"]]]:
        '''subnet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#subnet TrafficManagerAzureEndpoint#subnet}
        '''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TrafficManagerAzureEndpointSubnet"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["TrafficManagerAzureEndpointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#timeouts TrafficManagerAzureEndpoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["TrafficManagerAzureEndpointTimeouts"], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#weight TrafficManagerAzureEndpoint#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficManagerAzureEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointCustomHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class TrafficManagerAzureEndpointCustomHeader:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#name TrafficManagerAzureEndpoint#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#value TrafficManagerAzureEndpoint#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointCustomHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#name TrafficManagerAzureEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#value TrafficManagerAzureEndpoint#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficManagerAzureEndpointCustomHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TrafficManagerAzureEndpointCustomHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointCustomHeaderList",
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
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointCustomHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "TrafficManagerAzureEndpointCustomHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointCustomHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TrafficManagerAzureEndpointCustomHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointCustomHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointCustomHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointCustomHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TrafficManagerAzureEndpointCustomHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TrafficManagerAzureEndpointCustomHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TrafficManagerAzureEndpointCustomHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointCustomHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TrafficManagerAzureEndpointCustomHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointCustomHeaderOutputReference",
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
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointCustomHeaderOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointCustomHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointCustomHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TrafficManagerAzureEndpointCustomHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TrafficManagerAzureEndpointCustomHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TrafficManagerAzureEndpointCustomHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointCustomHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointSubnet",
    jsii_struct_bases=[],
    name_mapping={"first": "first", "last": "last", "scope": "scope"},
)
class TrafficManagerAzureEndpointSubnet:
    def __init__(
        self,
        *,
        first: builtins.str,
        last: typing.Optional[builtins.str] = None,
        scope: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param first: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#first TrafficManagerAzureEndpoint#first}.
        :param last: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#last TrafficManagerAzureEndpoint#last}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#scope TrafficManagerAzureEndpoint#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointSubnet.__init__)
            check_type(argname="argument first", value=first, expected_type=type_hints["first"])
            check_type(argname="argument last", value=last, expected_type=type_hints["last"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {
            "first": first,
        }
        if last is not None:
            self._values["last"] = last
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def first(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#first TrafficManagerAzureEndpoint#first}.'''
        result = self._values.get("first")
        assert result is not None, "Required property 'first' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#last TrafficManagerAzureEndpoint#last}.'''
        result = self._values.get("last")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#scope TrafficManagerAzureEndpoint#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficManagerAzureEndpointSubnet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TrafficManagerAzureEndpointSubnetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointSubnetList",
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
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointSubnetList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "TrafficManagerAzureEndpointSubnetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointSubnetList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TrafficManagerAzureEndpointSubnetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointSubnetList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointSubnetList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointSubnetList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TrafficManagerAzureEndpointSubnet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TrafficManagerAzureEndpointSubnet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TrafficManagerAzureEndpointSubnet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointSubnetList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TrafficManagerAzureEndpointSubnetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointSubnetOutputReference",
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
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointSubnetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetLast")
    def reset_last(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLast", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="firstInput")
    def first_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstInput"))

    @builtins.property
    @jsii.member(jsii_name="lastInput")
    def last_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="first")
    def first(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "first"))

    @first.setter
    def first(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointSubnetOutputReference, "first").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "first", value)

    @builtins.property
    @jsii.member(jsii_name="last")
    def last(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "last"))

    @last.setter
    def last(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointSubnetOutputReference, "last").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "last", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointSubnetOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TrafficManagerAzureEndpointSubnet, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TrafficManagerAzureEndpointSubnet, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TrafficManagerAzureEndpointSubnet, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointSubnetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class TrafficManagerAzureEndpointTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#create TrafficManagerAzureEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#delete TrafficManagerAzureEndpoint#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#read TrafficManagerAzureEndpoint#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#update TrafficManagerAzureEndpoint#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#create TrafficManagerAzureEndpoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#delete TrafficManagerAzureEndpoint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#read TrafficManagerAzureEndpoint#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_azure_endpoint#update TrafficManagerAzureEndpoint#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficManagerAzureEndpointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TrafficManagerAzureEndpointTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.trafficManagerAzureEndpoint.TrafficManagerAzureEndpointTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(TrafficManagerAzureEndpointTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TrafficManagerAzureEndpointTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TrafficManagerAzureEndpointTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TrafficManagerAzureEndpointTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TrafficManagerAzureEndpointTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TrafficManagerAzureEndpoint",
    "TrafficManagerAzureEndpointConfig",
    "TrafficManagerAzureEndpointCustomHeader",
    "TrafficManagerAzureEndpointCustomHeaderList",
    "TrafficManagerAzureEndpointCustomHeaderOutputReference",
    "TrafficManagerAzureEndpointSubnet",
    "TrafficManagerAzureEndpointSubnetList",
    "TrafficManagerAzureEndpointSubnetOutputReference",
    "TrafficManagerAzureEndpointTimeouts",
    "TrafficManagerAzureEndpointTimeoutsOutputReference",
]

publication.publish()
