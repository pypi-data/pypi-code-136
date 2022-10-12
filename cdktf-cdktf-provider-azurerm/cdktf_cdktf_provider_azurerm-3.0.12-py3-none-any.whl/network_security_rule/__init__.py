'''
# `azurerm_network_security_rule`

Refer to the Terraform Registory for docs: [`azurerm_network_security_rule`](https://www.terraform.io/docs/providers/azurerm/r/network_security_rule).
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


class NetworkSecurityRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkSecurityRule.NetworkSecurityRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule azurerm_network_security_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        access: builtins.str,
        direction: builtins.str,
        name: builtins.str,
        network_security_group_name: builtins.str,
        priority: jsii.Number,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        destination_address_prefix: typing.Optional[builtins.str] = None,
        destination_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_application_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_port_range: typing.Optional[builtins.str] = None,
        destination_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        source_address_prefix: typing.Optional[builtins.str] = None,
        source_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_application_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_port_range: typing.Optional[builtins.str] = None,
        source_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetworkSecurityRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule azurerm_network_security_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#access NetworkSecurityRule#access}.
        :param direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#direction NetworkSecurityRule#direction}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#name NetworkSecurityRule#name}.
        :param network_security_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#network_security_group_name NetworkSecurityRule#network_security_group_name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#priority NetworkSecurityRule#priority}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#protocol NetworkSecurityRule#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#resource_group_name NetworkSecurityRule#resource_group_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#description NetworkSecurityRule#description}.
        :param destination_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_address_prefix NetworkSecurityRule#destination_address_prefix}.
        :param destination_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_address_prefixes NetworkSecurityRule#destination_address_prefixes}.
        :param destination_application_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_application_security_group_ids NetworkSecurityRule#destination_application_security_group_ids}.
        :param destination_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_port_range NetworkSecurityRule#destination_port_range}.
        :param destination_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_port_ranges NetworkSecurityRule#destination_port_ranges}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#id NetworkSecurityRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_address_prefix NetworkSecurityRule#source_address_prefix}.
        :param source_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_address_prefixes NetworkSecurityRule#source_address_prefixes}.
        :param source_application_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_application_security_group_ids NetworkSecurityRule#source_application_security_group_ids}.
        :param source_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_port_range NetworkSecurityRule#source_port_range}.
        :param source_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_port_ranges NetworkSecurityRule#source_port_ranges}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#timeouts NetworkSecurityRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkSecurityRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkSecurityRuleConfig(
            access=access,
            direction=direction,
            name=name,
            network_security_group_name=network_security_group_name,
            priority=priority,
            protocol=protocol,
            resource_group_name=resource_group_name,
            description=description,
            destination_address_prefix=destination_address_prefix,
            destination_address_prefixes=destination_address_prefixes,
            destination_application_security_group_ids=destination_application_security_group_ids,
            destination_port_range=destination_port_range,
            destination_port_ranges=destination_port_ranges,
            id=id,
            source_address_prefix=source_address_prefix,
            source_address_prefixes=source_address_prefixes,
            source_application_security_group_ids=source_application_security_group_ids,
            source_port_range=source_port_range,
            source_port_ranges=source_port_ranges,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#create NetworkSecurityRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#delete NetworkSecurityRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#read NetworkSecurityRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#update NetworkSecurityRule#update}.
        '''
        value = NetworkSecurityRuleTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDestinationAddressPrefix")
    def reset_destination_address_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddressPrefix", []))

    @jsii.member(jsii_name="resetDestinationAddressPrefixes")
    def reset_destination_address_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddressPrefixes", []))

    @jsii.member(jsii_name="resetDestinationApplicationSecurityGroupIds")
    def reset_destination_application_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationApplicationSecurityGroupIds", []))

    @jsii.member(jsii_name="resetDestinationPortRange")
    def reset_destination_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPortRange", []))

    @jsii.member(jsii_name="resetDestinationPortRanges")
    def reset_destination_port_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPortRanges", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSourceAddressPrefix")
    def reset_source_address_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddressPrefix", []))

    @jsii.member(jsii_name="resetSourceAddressPrefixes")
    def reset_source_address_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddressPrefixes", []))

    @jsii.member(jsii_name="resetSourceApplicationSecurityGroupIds")
    def reset_source_application_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceApplicationSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSourcePortRange")
    def reset_source_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcePortRange", []))

    @jsii.member(jsii_name="resetSourcePortRanges")
    def reset_source_port_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcePortRanges", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "NetworkSecurityRuleTimeoutsOutputReference":
        return typing.cast("NetworkSecurityRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressPrefixesInput")
    def destination_address_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationAddressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressPrefixInput")
    def destination_address_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationAddressPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationApplicationSecurityGroupIdsInput")
    def destination_application_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationApplicationSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortRangeInput")
    def destination_port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationPortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortRangesInput")
    def destination_port_ranges_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationPortRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="directionInput")
    def direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupNameInput")
    def network_security_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkSecurityGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefixesInput")
    def source_address_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceAddressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefixInput")
    def source_address_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceAddressPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceApplicationSecurityGroupIdsInput")
    def source_application_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceApplicationSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRangeInput")
    def source_port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRangesInput")
    def source_port_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcePortRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["NetworkSecurityRuleTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetworkSecurityRuleTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "access"))

    @access.setter
    def access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destinationAddressPrefix")
    def destination_address_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationAddressPrefix"))

    @destination_address_prefix.setter
    def destination_address_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "destination_address_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddressPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="destinationAddressPrefixes")
    def destination_address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddressPrefixes"))

    @destination_address_prefixes.setter
    def destination_address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "destination_address_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="destinationApplicationSecurityGroupIds")
    def destination_application_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationApplicationSecurityGroupIds"))

    @destination_application_security_group_ids.setter
    def destination_application_security_group_ids(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "destination_application_security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationApplicationSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPortRange")
    def destination_port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPortRange"))

    @destination_port_range.setter
    def destination_port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "destination_port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPortRange", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPortRanges")
    def destination_port_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationPortRanges"))

    @destination_port_ranges.setter
    def destination_port_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "destination_port_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPortRanges", value)

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupName")
    def network_security_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkSecurityGroupName"))

    @network_security_group_name.setter
    def network_security_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "network_security_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSecurityGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefix")
    def source_address_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceAddressPrefix"))

    @source_address_prefix.setter
    def source_address_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "source_address_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddressPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefixes")
    def source_address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddressPrefixes"))

    @source_address_prefixes.setter
    def source_address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "source_address_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="sourceApplicationSecurityGroupIds")
    def source_application_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceApplicationSecurityGroupIds"))

    @source_application_security_group_ids.setter
    def source_application_security_group_ids(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "source_application_security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceApplicationSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePortRange")
    def source_port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourcePortRange"))

    @source_port_range.setter
    def source_port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "source_port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePortRange", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePortRanges")
    def source_port_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourcePortRanges"))

    @source_port_ranges.setter
    def source_port_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRule, "source_port_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePortRanges", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkSecurityRule.NetworkSecurityRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "access": "access",
        "direction": "direction",
        "name": "name",
        "network_security_group_name": "networkSecurityGroupName",
        "priority": "priority",
        "protocol": "protocol",
        "resource_group_name": "resourceGroupName",
        "description": "description",
        "destination_address_prefix": "destinationAddressPrefix",
        "destination_address_prefixes": "destinationAddressPrefixes",
        "destination_application_security_group_ids": "destinationApplicationSecurityGroupIds",
        "destination_port_range": "destinationPortRange",
        "destination_port_ranges": "destinationPortRanges",
        "id": "id",
        "source_address_prefix": "sourceAddressPrefix",
        "source_address_prefixes": "sourceAddressPrefixes",
        "source_application_security_group_ids": "sourceApplicationSecurityGroupIds",
        "source_port_range": "sourcePortRange",
        "source_port_ranges": "sourcePortRanges",
        "timeouts": "timeouts",
    },
)
class NetworkSecurityRuleConfig(cdktf.TerraformMetaArguments):
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
        access: builtins.str,
        direction: builtins.str,
        name: builtins.str,
        network_security_group_name: builtins.str,
        priority: jsii.Number,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        destination_address_prefix: typing.Optional[builtins.str] = None,
        destination_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_application_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_port_range: typing.Optional[builtins.str] = None,
        destination_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        source_address_prefix: typing.Optional[builtins.str] = None,
        source_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_application_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_port_range: typing.Optional[builtins.str] = None,
        source_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetworkSecurityRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#access NetworkSecurityRule#access}.
        :param direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#direction NetworkSecurityRule#direction}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#name NetworkSecurityRule#name}.
        :param network_security_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#network_security_group_name NetworkSecurityRule#network_security_group_name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#priority NetworkSecurityRule#priority}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#protocol NetworkSecurityRule#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#resource_group_name NetworkSecurityRule#resource_group_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#description NetworkSecurityRule#description}.
        :param destination_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_address_prefix NetworkSecurityRule#destination_address_prefix}.
        :param destination_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_address_prefixes NetworkSecurityRule#destination_address_prefixes}.
        :param destination_application_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_application_security_group_ids NetworkSecurityRule#destination_application_security_group_ids}.
        :param destination_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_port_range NetworkSecurityRule#destination_port_range}.
        :param destination_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_port_ranges NetworkSecurityRule#destination_port_ranges}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#id NetworkSecurityRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_address_prefix NetworkSecurityRule#source_address_prefix}.
        :param source_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_address_prefixes NetworkSecurityRule#source_address_prefixes}.
        :param source_application_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_application_security_group_ids NetworkSecurityRule#source_application_security_group_ids}.
        :param source_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_port_range NetworkSecurityRule#source_port_range}.
        :param source_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_port_ranges NetworkSecurityRule#source_port_ranges}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#timeouts NetworkSecurityRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = NetworkSecurityRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkSecurityRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_security_group_name", value=network_security_group_name, expected_type=type_hints["network_security_group_name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument destination_address_prefix", value=destination_address_prefix, expected_type=type_hints["destination_address_prefix"])
            check_type(argname="argument destination_address_prefixes", value=destination_address_prefixes, expected_type=type_hints["destination_address_prefixes"])
            check_type(argname="argument destination_application_security_group_ids", value=destination_application_security_group_ids, expected_type=type_hints["destination_application_security_group_ids"])
            check_type(argname="argument destination_port_range", value=destination_port_range, expected_type=type_hints["destination_port_range"])
            check_type(argname="argument destination_port_ranges", value=destination_port_ranges, expected_type=type_hints["destination_port_ranges"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument source_address_prefix", value=source_address_prefix, expected_type=type_hints["source_address_prefix"])
            check_type(argname="argument source_address_prefixes", value=source_address_prefixes, expected_type=type_hints["source_address_prefixes"])
            check_type(argname="argument source_application_security_group_ids", value=source_application_security_group_ids, expected_type=type_hints["source_application_security_group_ids"])
            check_type(argname="argument source_port_range", value=source_port_range, expected_type=type_hints["source_port_range"])
            check_type(argname="argument source_port_ranges", value=source_port_ranges, expected_type=type_hints["source_port_ranges"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "access": access,
            "direction": direction,
            "name": name,
            "network_security_group_name": network_security_group_name,
            "priority": priority,
            "protocol": protocol,
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
        if description is not None:
            self._values["description"] = description
        if destination_address_prefix is not None:
            self._values["destination_address_prefix"] = destination_address_prefix
        if destination_address_prefixes is not None:
            self._values["destination_address_prefixes"] = destination_address_prefixes
        if destination_application_security_group_ids is not None:
            self._values["destination_application_security_group_ids"] = destination_application_security_group_ids
        if destination_port_range is not None:
            self._values["destination_port_range"] = destination_port_range
        if destination_port_ranges is not None:
            self._values["destination_port_ranges"] = destination_port_ranges
        if id is not None:
            self._values["id"] = id
        if source_address_prefix is not None:
            self._values["source_address_prefix"] = source_address_prefix
        if source_address_prefixes is not None:
            self._values["source_address_prefixes"] = source_address_prefixes
        if source_application_security_group_ids is not None:
            self._values["source_application_security_group_ids"] = source_application_security_group_ids
        if source_port_range is not None:
            self._values["source_port_range"] = source_port_range
        if source_port_ranges is not None:
            self._values["source_port_ranges"] = source_port_ranges
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
    def access(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#access NetworkSecurityRule#access}.'''
        result = self._values.get("access")
        assert result is not None, "Required property 'access' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def direction(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#direction NetworkSecurityRule#direction}.'''
        result = self._values.get("direction")
        assert result is not None, "Required property 'direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#name NetworkSecurityRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_security_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#network_security_group_name NetworkSecurityRule#network_security_group_name}.'''
        result = self._values.get("network_security_group_name")
        assert result is not None, "Required property 'network_security_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#priority NetworkSecurityRule#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#protocol NetworkSecurityRule#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#resource_group_name NetworkSecurityRule#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#description NetworkSecurityRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_address_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_address_prefix NetworkSecurityRule#destination_address_prefix}.'''
        result = self._values.get("destination_address_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_address_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_address_prefixes NetworkSecurityRule#destination_address_prefixes}.'''
        result = self._values.get("destination_address_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_application_security_group_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_application_security_group_ids NetworkSecurityRule#destination_application_security_group_ids}.'''
        result = self._values.get("destination_application_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_port_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_port_range NetworkSecurityRule#destination_port_range}.'''
        result = self._values.get("destination_port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_port_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#destination_port_ranges NetworkSecurityRule#destination_port_ranges}.'''
        result = self._values.get("destination_port_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#id NetworkSecurityRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_address_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_address_prefix NetworkSecurityRule#source_address_prefix}.'''
        result = self._values.get("source_address_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_address_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_address_prefixes NetworkSecurityRule#source_address_prefixes}.'''
        result = self._values.get("source_address_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_application_security_group_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_application_security_group_ids NetworkSecurityRule#source_application_security_group_ids}.'''
        result = self._values.get("source_application_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_port_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_port_range NetworkSecurityRule#source_port_range}.'''
        result = self._values.get("source_port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_port_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#source_port_ranges NetworkSecurityRule#source_port_ranges}.'''
        result = self._values.get("source_port_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetworkSecurityRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#timeouts NetworkSecurityRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetworkSecurityRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkSecurityRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.networkSecurityRule.NetworkSecurityRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class NetworkSecurityRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#create NetworkSecurityRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#delete NetworkSecurityRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#read NetworkSecurityRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#update NetworkSecurityRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkSecurityRuleTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#create NetworkSecurityRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#delete NetworkSecurityRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#read NetworkSecurityRule#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/network_security_rule#update NetworkSecurityRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkSecurityRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkSecurityRuleTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.networkSecurityRule.NetworkSecurityRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkSecurityRuleTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRuleTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRuleTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRuleTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRuleTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkSecurityRuleTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkSecurityRule",
    "NetworkSecurityRuleConfig",
    "NetworkSecurityRuleTimeouts",
    "NetworkSecurityRuleTimeoutsOutputReference",
]

publication.publish()
