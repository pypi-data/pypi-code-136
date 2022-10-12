'''
# `azurerm_private_endpoint`

Refer to the Terraform Registory for docs: [`azurerm_private_endpoint`](https://www.terraform.io/docs/providers/azurerm/r/private_endpoint).
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


class PrivateEndpoint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint azurerm_private_endpoint}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        private_service_connection: typing.Union["PrivateEndpointPrivateServiceConnection", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        subnet_id: builtins.str,
        custom_network_interface_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_configuration: typing.Optional[typing.Union["PrivateEndpointIpConfiguration", typing.Dict[str, typing.Any]]] = None,
        private_dns_zone_group: typing.Optional[typing.Union["PrivateEndpointPrivateDnsZoneGroup", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["PrivateEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint azurerm_private_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#location PrivateEndpoint#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.
        :param private_service_connection: private_service_connection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_service_connection PrivateEndpoint#private_service_connection}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#resource_group_name PrivateEndpoint#resource_group_name}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subnet_id PrivateEndpoint#subnet_id}.
        :param custom_network_interface_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#custom_network_interface_name PrivateEndpoint#custom_network_interface_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#id PrivateEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#ip_configuration PrivateEndpoint#ip_configuration}
        :param private_dns_zone_group: private_dns_zone_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_dns_zone_group PrivateEndpoint#private_dns_zone_group}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#tags PrivateEndpoint#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#timeouts PrivateEndpoint#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpoint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PrivateEndpointConfig(
            location=location,
            name=name,
            private_service_connection=private_service_connection,
            resource_group_name=resource_group_name,
            subnet_id=subnet_id,
            custom_network_interface_name=custom_network_interface_name,
            id=id,
            ip_configuration=ip_configuration,
            private_dns_zone_group=private_dns_zone_group,
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

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        *,
        name: builtins.str,
        private_ip_address: builtins.str,
        subresource_name: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.
        :param private_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_ip_address PrivateEndpoint#private_ip_address}.
        :param subresource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subresource_name PrivateEndpoint#subresource_name}.
        '''
        value = PrivateEndpointIpConfiguration(
            name=name,
            private_ip_address=private_ip_address,
            subresource_name=subresource_name,
        )

        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

    @jsii.member(jsii_name="putPrivateDnsZoneGroup")
    def put_private_dns_zone_group(
        self,
        *,
        name: builtins.str,
        private_dns_zone_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.
        :param private_dns_zone_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_dns_zone_ids PrivateEndpoint#private_dns_zone_ids}.
        '''
        value = PrivateEndpointPrivateDnsZoneGroup(
            name=name, private_dns_zone_ids=private_dns_zone_ids
        )

        return typing.cast(None, jsii.invoke(self, "putPrivateDnsZoneGroup", [value]))

    @jsii.member(jsii_name="putPrivateServiceConnection")
    def put_private_service_connection(
        self,
        *,
        is_manual_connection: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        private_connection_resource_alias: typing.Optional[builtins.str] = None,
        private_connection_resource_id: typing.Optional[builtins.str] = None,
        request_message: typing.Optional[builtins.str] = None,
        subresource_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param is_manual_connection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#is_manual_connection PrivateEndpoint#is_manual_connection}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.
        :param private_connection_resource_alias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_connection_resource_alias PrivateEndpoint#private_connection_resource_alias}.
        :param private_connection_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_connection_resource_id PrivateEndpoint#private_connection_resource_id}.
        :param request_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#request_message PrivateEndpoint#request_message}.
        :param subresource_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subresource_names PrivateEndpoint#subresource_names}.
        '''
        value = PrivateEndpointPrivateServiceConnection(
            is_manual_connection=is_manual_connection,
            name=name,
            private_connection_resource_alias=private_connection_resource_alias,
            private_connection_resource_id=private_connection_resource_id,
            request_message=request_message,
            subresource_names=subresource_names,
        )

        return typing.cast(None, jsii.invoke(self, "putPrivateServiceConnection", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#create PrivateEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#delete PrivateEndpoint#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#read PrivateEndpoint#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#update PrivateEndpoint#update}.
        '''
        value = PrivateEndpointTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCustomNetworkInterfaceName")
    def reset_custom_network_interface_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomNetworkInterfaceName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpConfiguration")
    def reset_ip_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpConfiguration", []))

    @jsii.member(jsii_name="resetPrivateDnsZoneGroup")
    def reset_private_dns_zone_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateDnsZoneGroup", []))

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
    @jsii.member(jsii_name="customDnsConfigs")
    def custom_dns_configs(self) -> "PrivateEndpointCustomDnsConfigsList":
        return typing.cast("PrivateEndpointCustomDnsConfigsList", jsii.get(self, "customDnsConfigs"))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(self) -> "PrivateEndpointIpConfigurationOutputReference":
        return typing.cast("PrivateEndpointIpConfigurationOutputReference", jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "PrivateEndpointNetworkInterfaceList":
        return typing.cast("PrivateEndpointNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneConfigs")
    def private_dns_zone_configs(self) -> "PrivateEndpointPrivateDnsZoneConfigsList":
        return typing.cast("PrivateEndpointPrivateDnsZoneConfigsList", jsii.get(self, "privateDnsZoneConfigs"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneGroup")
    def private_dns_zone_group(
        self,
    ) -> "PrivateEndpointPrivateDnsZoneGroupOutputReference":
        return typing.cast("PrivateEndpointPrivateDnsZoneGroupOutputReference", jsii.get(self, "privateDnsZoneGroup"))

    @builtins.property
    @jsii.member(jsii_name="privateServiceConnection")
    def private_service_connection(
        self,
    ) -> "PrivateEndpointPrivateServiceConnectionOutputReference":
        return typing.cast("PrivateEndpointPrivateServiceConnectionOutputReference", jsii.get(self, "privateServiceConnection"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PrivateEndpointTimeoutsOutputReference":
        return typing.cast("PrivateEndpointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="customNetworkInterfaceNameInput")
    def custom_network_interface_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customNetworkInterfaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional["PrivateEndpointIpConfiguration"]:
        return typing.cast(typing.Optional["PrivateEndpointIpConfiguration"], jsii.get(self, "ipConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneGroupInput")
    def private_dns_zone_group_input(
        self,
    ) -> typing.Optional["PrivateEndpointPrivateDnsZoneGroup"]:
        return typing.cast(typing.Optional["PrivateEndpointPrivateDnsZoneGroup"], jsii.get(self, "privateDnsZoneGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="privateServiceConnectionInput")
    def private_service_connection_input(
        self,
    ) -> typing.Optional["PrivateEndpointPrivateServiceConnection"]:
        return typing.cast(typing.Optional["PrivateEndpointPrivateServiceConnection"], jsii.get(self, "privateServiceConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["PrivateEndpointTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PrivateEndpointTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="customNetworkInterfaceName")
    def custom_network_interface_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customNetworkInterfaceName"))

    @custom_network_interface_name.setter
    def custom_network_interface_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpoint, "custom_network_interface_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customNetworkInterfaceName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpoint, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpoint, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpoint, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpoint, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpoint, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpoint, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointConfig",
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
        "private_service_connection": "privateServiceConnection",
        "resource_group_name": "resourceGroupName",
        "subnet_id": "subnetId",
        "custom_network_interface_name": "customNetworkInterfaceName",
        "id": "id",
        "ip_configuration": "ipConfiguration",
        "private_dns_zone_group": "privateDnsZoneGroup",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class PrivateEndpointConfig(cdktf.TerraformMetaArguments):
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
        private_service_connection: typing.Union["PrivateEndpointPrivateServiceConnection", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        subnet_id: builtins.str,
        custom_network_interface_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_configuration: typing.Optional[typing.Union["PrivateEndpointIpConfiguration", typing.Dict[str, typing.Any]]] = None,
        private_dns_zone_group: typing.Optional[typing.Union["PrivateEndpointPrivateDnsZoneGroup", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["PrivateEndpointTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#location PrivateEndpoint#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.
        :param private_service_connection: private_service_connection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_service_connection PrivateEndpoint#private_service_connection}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#resource_group_name PrivateEndpoint#resource_group_name}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subnet_id PrivateEndpoint#subnet_id}.
        :param custom_network_interface_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#custom_network_interface_name PrivateEndpoint#custom_network_interface_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#id PrivateEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#ip_configuration PrivateEndpoint#ip_configuration}
        :param private_dns_zone_group: private_dns_zone_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_dns_zone_group PrivateEndpoint#private_dns_zone_group}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#tags PrivateEndpoint#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#timeouts PrivateEndpoint#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(private_service_connection, dict):
            private_service_connection = PrivateEndpointPrivateServiceConnection(**private_service_connection)
        if isinstance(ip_configuration, dict):
            ip_configuration = PrivateEndpointIpConfiguration(**ip_configuration)
        if isinstance(private_dns_zone_group, dict):
            private_dns_zone_group = PrivateEndpointPrivateDnsZoneGroup(**private_dns_zone_group)
        if isinstance(timeouts, dict):
            timeouts = PrivateEndpointTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_service_connection", value=private_service_connection, expected_type=type_hints["private_service_connection"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument custom_network_interface_name", value=custom_network_interface_name, expected_type=type_hints["custom_network_interface_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument private_dns_zone_group", value=private_dns_zone_group, expected_type=type_hints["private_dns_zone_group"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "private_service_connection": private_service_connection,
            "resource_group_name": resource_group_name,
            "subnet_id": subnet_id,
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
        if custom_network_interface_name is not None:
            self._values["custom_network_interface_name"] = custom_network_interface_name
        if id is not None:
            self._values["id"] = id
        if ip_configuration is not None:
            self._values["ip_configuration"] = ip_configuration
        if private_dns_zone_group is not None:
            self._values["private_dns_zone_group"] = private_dns_zone_group
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#location PrivateEndpoint#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_service_connection(self) -> "PrivateEndpointPrivateServiceConnection":
        '''private_service_connection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_service_connection PrivateEndpoint#private_service_connection}
        '''
        result = self._values.get("private_service_connection")
        assert result is not None, "Required property 'private_service_connection' is missing"
        return typing.cast("PrivateEndpointPrivateServiceConnection", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#resource_group_name PrivateEndpoint#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subnet_id PrivateEndpoint#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_network_interface_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#custom_network_interface_name PrivateEndpoint#custom_network_interface_name}.'''
        result = self._values.get("custom_network_interface_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#id PrivateEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_configuration(self) -> typing.Optional["PrivateEndpointIpConfiguration"]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#ip_configuration PrivateEndpoint#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        return typing.cast(typing.Optional["PrivateEndpointIpConfiguration"], result)

    @builtins.property
    def private_dns_zone_group(
        self,
    ) -> typing.Optional["PrivateEndpointPrivateDnsZoneGroup"]:
        '''private_dns_zone_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_dns_zone_group PrivateEndpoint#private_dns_zone_group}
        '''
        result = self._values.get("private_dns_zone_group")
        return typing.cast(typing.Optional["PrivateEndpointPrivateDnsZoneGroup"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#tags PrivateEndpoint#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PrivateEndpointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#timeouts PrivateEndpoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PrivateEndpointTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointCustomDnsConfigs",
    jsii_struct_bases=[],
    name_mapping={},
)
class PrivateEndpointCustomDnsConfigs:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointCustomDnsConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrivateEndpointCustomDnsConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointCustomDnsConfigsList",
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
            type_hints = typing.get_type_hints(PrivateEndpointCustomDnsConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PrivateEndpointCustomDnsConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointCustomDnsConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PrivateEndpointCustomDnsConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointCustomDnsConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointCustomDnsConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointCustomDnsConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class PrivateEndpointCustomDnsConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointCustomDnsConfigsOutputReference",
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
            type_hints = typing.get_type_hints(PrivateEndpointCustomDnsConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PrivateEndpointCustomDnsConfigs]:
        return typing.cast(typing.Optional[PrivateEndpointCustomDnsConfigs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PrivateEndpointCustomDnsConfigs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointCustomDnsConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "private_ip_address": "privateIpAddress",
        "subresource_name": "subresourceName",
    },
)
class PrivateEndpointIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        private_ip_address: builtins.str,
        subresource_name: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.
        :param private_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_ip_address PrivateEndpoint#private_ip_address}.
        :param subresource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subresource_name PrivateEndpoint#subresource_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointIpConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
            check_type(argname="argument subresource_name", value=subresource_name, expected_type=type_hints["subresource_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "private_ip_address": private_ip_address,
            "subresource_name": subresource_name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_ip_address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_ip_address PrivateEndpoint#private_ip_address}.'''
        result = self._values.get("private_ip_address")
        assert result is not None, "Required property 'private_ip_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subresource_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subresource_name PrivateEndpoint#subresource_name}.'''
        result = self._values.get("subresource_name")
        assert result is not None, "Required property 'subresource_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrivateEndpointIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(PrivateEndpointIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressInput")
    def private_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="subresourceNameInput")
    def subresource_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subresourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @private_ip_address.setter
    def private_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointIpConfigurationOutputReference, "private_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="subresourceName")
    def subresource_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subresourceName"))

    @subresource_name.setter
    def subresource_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointIpConfigurationOutputReference, "subresource_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subresourceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PrivateEndpointIpConfiguration]:
        return typing.cast(typing.Optional[PrivateEndpointIpConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PrivateEndpointIpConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={},
)
class PrivateEndpointNetworkInterface:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrivateEndpointNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(PrivateEndpointNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PrivateEndpointNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PrivateEndpointNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class PrivateEndpointNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(PrivateEndpointNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PrivateEndpointNetworkInterface]:
        return typing.cast(typing.Optional[PrivateEndpointNetworkInterface], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PrivateEndpointNetworkInterface],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateDnsZoneConfigs",
    jsii_struct_bases=[],
    name_mapping={},
)
class PrivateEndpointPrivateDnsZoneConfigs:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointPrivateDnsZoneConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrivateEndpointPrivateDnsZoneConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateDnsZoneConfigsList",
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
            type_hints = typing.get_type_hints(PrivateEndpointPrivateDnsZoneConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PrivateEndpointPrivateDnsZoneConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointPrivateDnsZoneConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PrivateEndpointPrivateDnsZoneConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class PrivateEndpointPrivateDnsZoneConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateDnsZoneConfigsOutputReference",
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
            type_hints = typing.get_type_hints(PrivateEndpointPrivateDnsZoneConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneId")
    def private_dns_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateDnsZoneId"))

    @builtins.property
    @jsii.member(jsii_name="recordSets")
    def record_sets(self) -> "PrivateEndpointPrivateDnsZoneConfigsRecordSetsList":
        return typing.cast("PrivateEndpointPrivateDnsZoneConfigsRecordSetsList", jsii.get(self, "recordSets"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PrivateEndpointPrivateDnsZoneConfigs]:
        return typing.cast(typing.Optional[PrivateEndpointPrivateDnsZoneConfigs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PrivateEndpointPrivateDnsZoneConfigs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateDnsZoneConfigsRecordSets",
    jsii_struct_bases=[],
    name_mapping={},
)
class PrivateEndpointPrivateDnsZoneConfigsRecordSets:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointPrivateDnsZoneConfigsRecordSets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrivateEndpointPrivateDnsZoneConfigsRecordSetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateDnsZoneConfigsRecordSetsList",
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
            type_hints = typing.get_type_hints(PrivateEndpointPrivateDnsZoneConfigsRecordSetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PrivateEndpointPrivateDnsZoneConfigsRecordSetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointPrivateDnsZoneConfigsRecordSetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PrivateEndpointPrivateDnsZoneConfigsRecordSetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneConfigsRecordSetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneConfigsRecordSetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneConfigsRecordSetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class PrivateEndpointPrivateDnsZoneConfigsRecordSetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateDnsZoneConfigsRecordSetsOutputReference",
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
            type_hints = typing.get_type_hints(PrivateEndpointPrivateDnsZoneConfigsRecordSetsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PrivateEndpointPrivateDnsZoneConfigsRecordSets]:
        return typing.cast(typing.Optional[PrivateEndpointPrivateDnsZoneConfigsRecordSets], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PrivateEndpointPrivateDnsZoneConfigsRecordSets],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneConfigsRecordSetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateDnsZoneGroup",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "private_dns_zone_ids": "privateDnsZoneIds"},
)
class PrivateEndpointPrivateDnsZoneGroup:
    def __init__(
        self,
        *,
        name: builtins.str,
        private_dns_zone_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.
        :param private_dns_zone_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_dns_zone_ids PrivateEndpoint#private_dns_zone_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointPrivateDnsZoneGroup.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_dns_zone_ids", value=private_dns_zone_ids, expected_type=type_hints["private_dns_zone_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "private_dns_zone_ids": private_dns_zone_ids,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_dns_zone_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_dns_zone_ids PrivateEndpoint#private_dns_zone_ids}.'''
        result = self._values.get("private_dns_zone_ids")
        assert result is not None, "Required property 'private_dns_zone_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointPrivateDnsZoneGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrivateEndpointPrivateDnsZoneGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateDnsZoneGroupOutputReference",
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
            type_hints = typing.get_type_hints(PrivateEndpointPrivateDnsZoneGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneIdsInput")
    def private_dns_zone_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privateDnsZoneIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneGroupOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateDnsZoneIds")
    def private_dns_zone_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateDnsZoneIds"))

    @private_dns_zone_ids.setter
    def private_dns_zone_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneGroupOutputReference, "private_dns_zone_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateDnsZoneIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PrivateEndpointPrivateDnsZoneGroup]:
        return typing.cast(typing.Optional[PrivateEndpointPrivateDnsZoneGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PrivateEndpointPrivateDnsZoneGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateDnsZoneGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateServiceConnection",
    jsii_struct_bases=[],
    name_mapping={
        "is_manual_connection": "isManualConnection",
        "name": "name",
        "private_connection_resource_alias": "privateConnectionResourceAlias",
        "private_connection_resource_id": "privateConnectionResourceId",
        "request_message": "requestMessage",
        "subresource_names": "subresourceNames",
    },
)
class PrivateEndpointPrivateServiceConnection:
    def __init__(
        self,
        *,
        is_manual_connection: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        private_connection_resource_alias: typing.Optional[builtins.str] = None,
        private_connection_resource_id: typing.Optional[builtins.str] = None,
        request_message: typing.Optional[builtins.str] = None,
        subresource_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param is_manual_connection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#is_manual_connection PrivateEndpoint#is_manual_connection}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.
        :param private_connection_resource_alias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_connection_resource_alias PrivateEndpoint#private_connection_resource_alias}.
        :param private_connection_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_connection_resource_id PrivateEndpoint#private_connection_resource_id}.
        :param request_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#request_message PrivateEndpoint#request_message}.
        :param subresource_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subresource_names PrivateEndpoint#subresource_names}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointPrivateServiceConnection.__init__)
            check_type(argname="argument is_manual_connection", value=is_manual_connection, expected_type=type_hints["is_manual_connection"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_connection_resource_alias", value=private_connection_resource_alias, expected_type=type_hints["private_connection_resource_alias"])
            check_type(argname="argument private_connection_resource_id", value=private_connection_resource_id, expected_type=type_hints["private_connection_resource_id"])
            check_type(argname="argument request_message", value=request_message, expected_type=type_hints["request_message"])
            check_type(argname="argument subresource_names", value=subresource_names, expected_type=type_hints["subresource_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "is_manual_connection": is_manual_connection,
            "name": name,
        }
        if private_connection_resource_alias is not None:
            self._values["private_connection_resource_alias"] = private_connection_resource_alias
        if private_connection_resource_id is not None:
            self._values["private_connection_resource_id"] = private_connection_resource_id
        if request_message is not None:
            self._values["request_message"] = request_message
        if subresource_names is not None:
            self._values["subresource_names"] = subresource_names

    @builtins.property
    def is_manual_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#is_manual_connection PrivateEndpoint#is_manual_connection}.'''
        result = self._values.get("is_manual_connection")
        assert result is not None, "Required property 'is_manual_connection' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#name PrivateEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_connection_resource_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_connection_resource_alias PrivateEndpoint#private_connection_resource_alias}.'''
        result = self._values.get("private_connection_resource_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_connection_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#private_connection_resource_id PrivateEndpoint#private_connection_resource_id}.'''
        result = self._values.get("private_connection_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#request_message PrivateEndpoint#request_message}.'''
        result = self._values.get("request_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subresource_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#subresource_names PrivateEndpoint#subresource_names}.'''
        result = self._values.get("subresource_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointPrivateServiceConnection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrivateEndpointPrivateServiceConnectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointPrivateServiceConnectionOutputReference",
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
            type_hints = typing.get_type_hints(PrivateEndpointPrivateServiceConnectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPrivateConnectionResourceAlias")
    def reset_private_connection_resource_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateConnectionResourceAlias", []))

    @jsii.member(jsii_name="resetPrivateConnectionResourceId")
    def reset_private_connection_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateConnectionResourceId", []))

    @jsii.member(jsii_name="resetRequestMessage")
    def reset_request_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMessage", []))

    @jsii.member(jsii_name="resetSubresourceNames")
    def reset_subresource_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubresourceNames", []))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="isManualConnectionInput")
    def is_manual_connection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isManualConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateConnectionResourceAliasInput")
    def private_connection_resource_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateConnectionResourceAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="privateConnectionResourceIdInput")
    def private_connection_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateConnectionResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMessageInput")
    def request_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="subresourceNamesInput")
    def subresource_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subresourceNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="isManualConnection")
    def is_manual_connection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isManualConnection"))

    @is_manual_connection.setter
    def is_manual_connection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateServiceConnectionOutputReference, "is_manual_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isManualConnection", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateServiceConnectionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateConnectionResourceAlias")
    def private_connection_resource_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateConnectionResourceAlias"))

    @private_connection_resource_alias.setter
    def private_connection_resource_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateServiceConnectionOutputReference, "private_connection_resource_alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateConnectionResourceAlias", value)

    @builtins.property
    @jsii.member(jsii_name="privateConnectionResourceId")
    def private_connection_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateConnectionResourceId"))

    @private_connection_resource_id.setter
    def private_connection_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateServiceConnectionOutputReference, "private_connection_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateConnectionResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="requestMessage")
    def request_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestMessage"))

    @request_message.setter
    def request_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateServiceConnectionOutputReference, "request_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMessage", value)

    @builtins.property
    @jsii.member(jsii_name="subresourceNames")
    def subresource_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subresourceNames"))

    @subresource_names.setter
    def subresource_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateServiceConnectionOutputReference, "subresource_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subresourceNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PrivateEndpointPrivateServiceConnection]:
        return typing.cast(typing.Optional[PrivateEndpointPrivateServiceConnection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PrivateEndpointPrivateServiceConnection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointPrivateServiceConnectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class PrivateEndpointTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#create PrivateEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#delete PrivateEndpoint#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#read PrivateEndpoint#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#update PrivateEndpoint#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PrivateEndpointTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#create PrivateEndpoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#delete PrivateEndpoint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#read PrivateEndpoint#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/private_endpoint#update PrivateEndpoint#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateEndpointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrivateEndpointTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.privateEndpoint.PrivateEndpointTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(PrivateEndpointTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(PrivateEndpointTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PrivateEndpointTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PrivateEndpointTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PrivateEndpointTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PrivateEndpointTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PrivateEndpoint",
    "PrivateEndpointConfig",
    "PrivateEndpointCustomDnsConfigs",
    "PrivateEndpointCustomDnsConfigsList",
    "PrivateEndpointCustomDnsConfigsOutputReference",
    "PrivateEndpointIpConfiguration",
    "PrivateEndpointIpConfigurationOutputReference",
    "PrivateEndpointNetworkInterface",
    "PrivateEndpointNetworkInterfaceList",
    "PrivateEndpointNetworkInterfaceOutputReference",
    "PrivateEndpointPrivateDnsZoneConfigs",
    "PrivateEndpointPrivateDnsZoneConfigsList",
    "PrivateEndpointPrivateDnsZoneConfigsOutputReference",
    "PrivateEndpointPrivateDnsZoneConfigsRecordSets",
    "PrivateEndpointPrivateDnsZoneConfigsRecordSetsList",
    "PrivateEndpointPrivateDnsZoneConfigsRecordSetsOutputReference",
    "PrivateEndpointPrivateDnsZoneGroup",
    "PrivateEndpointPrivateDnsZoneGroupOutputReference",
    "PrivateEndpointPrivateServiceConnection",
    "PrivateEndpointPrivateServiceConnectionOutputReference",
    "PrivateEndpointTimeouts",
    "PrivateEndpointTimeoutsOutputReference",
]

publication.publish()
