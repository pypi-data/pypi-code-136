'''
# `azurerm_virtual_network_gateway_nat_rule`

Refer to the Terraform Registory for docs: [`azurerm_virtual_network_gateway_nat_rule`](https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule).
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


class VirtualNetworkGatewayNatRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule azurerm_virtual_network_gateway_nat_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        external_mapping: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayNatRuleExternalMapping", typing.Dict[str, typing.Any]]]],
        internal_mapping: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayNatRuleInternalMapping", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        resource_group_name: builtins.str,
        virtual_network_gateway_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        ip_configuration_id: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayNatRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule azurerm_virtual_network_gateway_nat_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param external_mapping: external_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#external_mapping VirtualNetworkGatewayNatRule#external_mapping}
        :param internal_mapping: internal_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#internal_mapping VirtualNetworkGatewayNatRule#internal_mapping}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#name VirtualNetworkGatewayNatRule#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#resource_group_name VirtualNetworkGatewayNatRule#resource_group_name}.
        :param virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#virtual_network_gateway_id VirtualNetworkGatewayNatRule#virtual_network_gateway_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#id VirtualNetworkGatewayNatRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#ip_configuration_id VirtualNetworkGatewayNatRule#ip_configuration_id}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#mode VirtualNetworkGatewayNatRule#mode}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#timeouts VirtualNetworkGatewayNatRule#timeouts}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#type VirtualNetworkGatewayNatRule#type}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualNetworkGatewayNatRuleConfig(
            external_mapping=external_mapping,
            internal_mapping=internal_mapping,
            name=name,
            resource_group_name=resource_group_name,
            virtual_network_gateway_id=virtual_network_gateway_id,
            id=id,
            ip_configuration_id=ip_configuration_id,
            mode=mode,
            timeouts=timeouts,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putExternalMapping")
    def put_external_mapping(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayNatRuleExternalMapping", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRule.put_external_mapping)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExternalMapping", [value]))

    @jsii.member(jsii_name="putInternalMapping")
    def put_internal_mapping(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayNatRuleInternalMapping", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRule.put_internal_mapping)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInternalMapping", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#create VirtualNetworkGatewayNatRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#delete VirtualNetworkGatewayNatRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#read VirtualNetworkGatewayNatRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#update VirtualNetworkGatewayNatRule#update}.
        '''
        value = VirtualNetworkGatewayNatRuleTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpConfigurationId")
    def reset_ip_configuration_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpConfigurationId", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="externalMapping")
    def external_mapping(self) -> "VirtualNetworkGatewayNatRuleExternalMappingList":
        return typing.cast("VirtualNetworkGatewayNatRuleExternalMappingList", jsii.get(self, "externalMapping"))

    @builtins.property
    @jsii.member(jsii_name="internalMapping")
    def internal_mapping(self) -> "VirtualNetworkGatewayNatRuleInternalMappingList":
        return typing.cast("VirtualNetworkGatewayNatRuleInternalMappingList", jsii.get(self, "internalMapping"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualNetworkGatewayNatRuleTimeoutsOutputReference":
        return typing.cast("VirtualNetworkGatewayNatRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="externalMappingInput")
    def external_mapping_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayNatRuleExternalMapping"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayNatRuleExternalMapping"]]], jsii.get(self, "externalMappingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="internalMappingInput")
    def internal_mapping_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayNatRuleInternalMapping"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayNatRuleInternalMapping"]]], jsii.get(self, "internalMappingInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationIdInput")
    def ip_configuration_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipConfigurationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualNetworkGatewayNatRuleTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualNetworkGatewayNatRuleTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkGatewayIdInput")
    def virtual_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationId")
    def ip_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipConfigurationId"))

    @ip_configuration_id.setter
    def ip_configuration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRule, "ip_configuration_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipConfigurationId", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRule, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRule, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRule, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkGatewayId")
    def virtual_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkGatewayId"))

    @virtual_network_gateway_id.setter
    def virtual_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRule, "virtual_network_gateway_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkGatewayId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "external_mapping": "externalMapping",
        "internal_mapping": "internalMapping",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "virtual_network_gateway_id": "virtualNetworkGatewayId",
        "id": "id",
        "ip_configuration_id": "ipConfigurationId",
        "mode": "mode",
        "timeouts": "timeouts",
        "type": "type",
    },
)
class VirtualNetworkGatewayNatRuleConfig(cdktf.TerraformMetaArguments):
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
        external_mapping: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayNatRuleExternalMapping", typing.Dict[str, typing.Any]]]],
        internal_mapping: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayNatRuleInternalMapping", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        resource_group_name: builtins.str,
        virtual_network_gateway_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        ip_configuration_id: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayNatRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param external_mapping: external_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#external_mapping VirtualNetworkGatewayNatRule#external_mapping}
        :param internal_mapping: internal_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#internal_mapping VirtualNetworkGatewayNatRule#internal_mapping}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#name VirtualNetworkGatewayNatRule#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#resource_group_name VirtualNetworkGatewayNatRule#resource_group_name}.
        :param virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#virtual_network_gateway_id VirtualNetworkGatewayNatRule#virtual_network_gateway_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#id VirtualNetworkGatewayNatRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#ip_configuration_id VirtualNetworkGatewayNatRule#ip_configuration_id}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#mode VirtualNetworkGatewayNatRule#mode}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#timeouts VirtualNetworkGatewayNatRule#timeouts}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#type VirtualNetworkGatewayNatRule#type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = VirtualNetworkGatewayNatRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument external_mapping", value=external_mapping, expected_type=type_hints["external_mapping"])
            check_type(argname="argument internal_mapping", value=internal_mapping, expected_type=type_hints["internal_mapping"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument virtual_network_gateway_id", value=virtual_network_gateway_id, expected_type=type_hints["virtual_network_gateway_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_configuration_id", value=ip_configuration_id, expected_type=type_hints["ip_configuration_id"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "external_mapping": external_mapping,
            "internal_mapping": internal_mapping,
            "name": name,
            "resource_group_name": resource_group_name,
            "virtual_network_gateway_id": virtual_network_gateway_id,
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
        if ip_configuration_id is not None:
            self._values["ip_configuration_id"] = ip_configuration_id
        if mode is not None:
            self._values["mode"] = mode
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type

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
    def external_mapping(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayNatRuleExternalMapping"]]:
        '''external_mapping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#external_mapping VirtualNetworkGatewayNatRule#external_mapping}
        '''
        result = self._values.get("external_mapping")
        assert result is not None, "Required property 'external_mapping' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayNatRuleExternalMapping"]], result)

    @builtins.property
    def internal_mapping(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayNatRuleInternalMapping"]]:
        '''internal_mapping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#internal_mapping VirtualNetworkGatewayNatRule#internal_mapping}
        '''
        result = self._values.get("internal_mapping")
        assert result is not None, "Required property 'internal_mapping' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayNatRuleInternalMapping"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#name VirtualNetworkGatewayNatRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#resource_group_name VirtualNetworkGatewayNatRule#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_network_gateway_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#virtual_network_gateway_id VirtualNetworkGatewayNatRule#virtual_network_gateway_id}.'''
        result = self._values.get("virtual_network_gateway_id")
        assert result is not None, "Required property 'virtual_network_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#id VirtualNetworkGatewayNatRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_configuration_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#ip_configuration_id VirtualNetworkGatewayNatRule#ip_configuration_id}.'''
        result = self._values.get("ip_configuration_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#mode VirtualNetworkGatewayNatRule#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualNetworkGatewayNatRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#timeouts VirtualNetworkGatewayNatRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualNetworkGatewayNatRuleTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#type VirtualNetworkGatewayNatRule#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayNatRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleExternalMapping",
    jsii_struct_bases=[],
    name_mapping={"address_space": "addressSpace", "port_range": "portRange"},
)
class VirtualNetworkGatewayNatRuleExternalMapping:
    def __init__(
        self,
        *,
        address_space: builtins.str,
        port_range: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_space: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#address_space VirtualNetworkGatewayNatRule#address_space}.
        :param port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#port_range VirtualNetworkGatewayNatRule#port_range}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleExternalMapping.__init__)
            check_type(argname="argument address_space", value=address_space, expected_type=type_hints["address_space"])
            check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
        self._values: typing.Dict[str, typing.Any] = {
            "address_space": address_space,
        }
        if port_range is not None:
            self._values["port_range"] = port_range

    @builtins.property
    def address_space(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#address_space VirtualNetworkGatewayNatRule#address_space}.'''
        result = self._values.get("address_space")
        assert result is not None, "Required property 'address_space' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#port_range VirtualNetworkGatewayNatRule#port_range}.'''
        result = self._values.get("port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayNatRuleExternalMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayNatRuleExternalMappingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleExternalMappingList",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleExternalMappingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayNatRuleExternalMappingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleExternalMappingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayNatRuleExternalMappingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleExternalMappingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleExternalMappingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleExternalMappingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayNatRuleExternalMapping]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayNatRuleExternalMapping]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayNatRuleExternalMapping]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleExternalMappingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayNatRuleExternalMappingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleExternalMappingOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleExternalMappingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPortRange")
    def reset_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRange", []))

    @builtins.property
    @jsii.member(jsii_name="addressSpaceInput")
    def address_space_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressSpaceInput"))

    @builtins.property
    @jsii.member(jsii_name="portRangeInput")
    def port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="addressSpace")
    def address_space(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressSpace"))

    @address_space.setter
    def address_space(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleExternalMappingOutputReference, "address_space").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressSpace", value)

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portRange"))

    @port_range.setter
    def port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleExternalMappingOutputReference, "port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portRange", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleExternalMapping, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleExternalMapping, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleExternalMapping, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleExternalMappingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleInternalMapping",
    jsii_struct_bases=[],
    name_mapping={"address_space": "addressSpace", "port_range": "portRange"},
)
class VirtualNetworkGatewayNatRuleInternalMapping:
    def __init__(
        self,
        *,
        address_space: builtins.str,
        port_range: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_space: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#address_space VirtualNetworkGatewayNatRule#address_space}.
        :param port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#port_range VirtualNetworkGatewayNatRule#port_range}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleInternalMapping.__init__)
            check_type(argname="argument address_space", value=address_space, expected_type=type_hints["address_space"])
            check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
        self._values: typing.Dict[str, typing.Any] = {
            "address_space": address_space,
        }
        if port_range is not None:
            self._values["port_range"] = port_range

    @builtins.property
    def address_space(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#address_space VirtualNetworkGatewayNatRule#address_space}.'''
        result = self._values.get("address_space")
        assert result is not None, "Required property 'address_space' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#port_range VirtualNetworkGatewayNatRule#port_range}.'''
        result = self._values.get("port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayNatRuleInternalMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayNatRuleInternalMappingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleInternalMappingList",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleInternalMappingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayNatRuleInternalMappingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleInternalMappingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayNatRuleInternalMappingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleInternalMappingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleInternalMappingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleInternalMappingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayNatRuleInternalMapping]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayNatRuleInternalMapping]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayNatRuleInternalMapping]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleInternalMappingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayNatRuleInternalMappingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleInternalMappingOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleInternalMappingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPortRange")
    def reset_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRange", []))

    @builtins.property
    @jsii.member(jsii_name="addressSpaceInput")
    def address_space_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressSpaceInput"))

    @builtins.property
    @jsii.member(jsii_name="portRangeInput")
    def port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="addressSpace")
    def address_space(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressSpace"))

    @address_space.setter
    def address_space(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleInternalMappingOutputReference, "address_space").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressSpace", value)

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portRange"))

    @port_range.setter
    def port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleInternalMappingOutputReference, "port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portRange", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleInternalMapping, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleInternalMapping, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleInternalMapping, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleInternalMappingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualNetworkGatewayNatRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#create VirtualNetworkGatewayNatRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#delete VirtualNetworkGatewayNatRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#read VirtualNetworkGatewayNatRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#update VirtualNetworkGatewayNatRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#create VirtualNetworkGatewayNatRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#delete VirtualNetworkGatewayNatRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#read VirtualNetworkGatewayNatRule#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_nat_rule#update VirtualNetworkGatewayNatRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayNatRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayNatRuleTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayNatRule.VirtualNetworkGatewayNatRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayNatRuleTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayNatRuleTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayNatRuleTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualNetworkGatewayNatRule",
    "VirtualNetworkGatewayNatRuleConfig",
    "VirtualNetworkGatewayNatRuleExternalMapping",
    "VirtualNetworkGatewayNatRuleExternalMappingList",
    "VirtualNetworkGatewayNatRuleExternalMappingOutputReference",
    "VirtualNetworkGatewayNatRuleInternalMapping",
    "VirtualNetworkGatewayNatRuleInternalMappingList",
    "VirtualNetworkGatewayNatRuleInternalMappingOutputReference",
    "VirtualNetworkGatewayNatRuleTimeouts",
    "VirtualNetworkGatewayNatRuleTimeoutsOutputReference",
]

publication.publish()
