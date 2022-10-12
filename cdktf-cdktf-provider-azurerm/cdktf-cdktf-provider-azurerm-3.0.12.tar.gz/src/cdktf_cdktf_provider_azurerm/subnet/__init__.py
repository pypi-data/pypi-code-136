'''
# `azurerm_subnet`

Refer to the Terraform Registory for docs: [`azurerm_subnet`](https://www.terraform.io/docs/providers/azurerm/r/subnet).
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


class Subnet(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subnet.Subnet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/subnet azurerm_subnet}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        address_prefixes: typing.Sequence[builtins.str],
        name: builtins.str,
        resource_group_name: builtins.str,
        virtual_network_name: builtins.str,
        delegation: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SubnetDelegation", typing.Dict[str, typing.Any]]]]] = None,
        enforce_private_link_endpoint_network_policies: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enforce_private_link_service_network_policies: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        private_endpoint_network_policies_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_link_service_network_policies_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_endpoint_policy_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_endpoints: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SubnetTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/subnet azurerm_subnet} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#address_prefixes Subnet#address_prefixes}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#name Subnet#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#resource_group_name Subnet#resource_group_name}.
        :param virtual_network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#virtual_network_name Subnet#virtual_network_name}.
        :param delegation: delegation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#delegation Subnet#delegation}
        :param enforce_private_link_endpoint_network_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#enforce_private_link_endpoint_network_policies Subnet#enforce_private_link_endpoint_network_policies}.
        :param enforce_private_link_service_network_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#enforce_private_link_service_network_policies Subnet#enforce_private_link_service_network_policies}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#id Subnet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param private_endpoint_network_policies_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#private_endpoint_network_policies_enabled Subnet#private_endpoint_network_policies_enabled}.
        :param private_link_service_network_policies_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#private_link_service_network_policies_enabled Subnet#private_link_service_network_policies_enabled}.
        :param service_endpoint_policy_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#service_endpoint_policy_ids Subnet#service_endpoint_policy_ids}.
        :param service_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#service_endpoints Subnet#service_endpoints}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#timeouts Subnet#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Subnet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SubnetConfig(
            address_prefixes=address_prefixes,
            name=name,
            resource_group_name=resource_group_name,
            virtual_network_name=virtual_network_name,
            delegation=delegation,
            enforce_private_link_endpoint_network_policies=enforce_private_link_endpoint_network_policies,
            enforce_private_link_service_network_policies=enforce_private_link_service_network_policies,
            id=id,
            private_endpoint_network_policies_enabled=private_endpoint_network_policies_enabled,
            private_link_service_network_policies_enabled=private_link_service_network_policies_enabled,
            service_endpoint_policy_ids=service_endpoint_policy_ids,
            service_endpoints=service_endpoints,
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

    @jsii.member(jsii_name="putDelegation")
    def put_delegation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SubnetDelegation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Subnet.put_delegation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDelegation", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#create Subnet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#delete Subnet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#read Subnet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#update Subnet#update}.
        '''
        value = SubnetTimeouts(create=create, delete=delete, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDelegation")
    def reset_delegation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelegation", []))

    @jsii.member(jsii_name="resetEnforcePrivateLinkEndpointNetworkPolicies")
    def reset_enforce_private_link_endpoint_network_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforcePrivateLinkEndpointNetworkPolicies", []))

    @jsii.member(jsii_name="resetEnforcePrivateLinkServiceNetworkPolicies")
    def reset_enforce_private_link_service_network_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforcePrivateLinkServiceNetworkPolicies", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrivateEndpointNetworkPoliciesEnabled")
    def reset_private_endpoint_network_policies_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateEndpointNetworkPoliciesEnabled", []))

    @jsii.member(jsii_name="resetPrivateLinkServiceNetworkPoliciesEnabled")
    def reset_private_link_service_network_policies_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkServiceNetworkPoliciesEnabled", []))

    @jsii.member(jsii_name="resetServiceEndpointPolicyIds")
    def reset_service_endpoint_policy_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceEndpointPolicyIds", []))

    @jsii.member(jsii_name="resetServiceEndpoints")
    def reset_service_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceEndpoints", []))

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
    @jsii.member(jsii_name="delegation")
    def delegation(self) -> "SubnetDelegationList":
        return typing.cast("SubnetDelegationList", jsii.get(self, "delegation"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SubnetTimeoutsOutputReference":
        return typing.cast("SubnetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="addressPrefixesInput")
    def address_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="delegationInput")
    def delegation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SubnetDelegation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SubnetDelegation"]]], jsii.get(self, "delegationInput"))

    @builtins.property
    @jsii.member(jsii_name="enforcePrivateLinkEndpointNetworkPoliciesInput")
    def enforce_private_link_endpoint_network_policies_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforcePrivateLinkEndpointNetworkPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="enforcePrivateLinkServiceNetworkPoliciesInput")
    def enforce_private_link_service_network_policies_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforcePrivateLinkServiceNetworkPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateEndpointNetworkPoliciesEnabledInput")
    def private_endpoint_network_policies_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateEndpointNetworkPoliciesEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceNetworkPoliciesEnabledInput")
    def private_link_service_network_policies_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateLinkServiceNetworkPoliciesEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceEndpointPolicyIdsInput")
    def service_endpoint_policy_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceEndpointPolicyIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceEndpointsInput")
    def service_endpoints_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SubnetTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SubnetTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkNameInput")
    def virtual_network_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkNameInput"))

    @builtins.property
    @jsii.member(jsii_name="addressPrefixes")
    def address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addressPrefixes"))

    @address_prefixes.setter
    def address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "address_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="enforcePrivateLinkEndpointNetworkPolicies")
    def enforce_private_link_endpoint_network_policies(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforcePrivateLinkEndpointNetworkPolicies"))

    @enforce_private_link_endpoint_network_policies.setter
    def enforce_private_link_endpoint_network_policies(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "enforce_private_link_endpoint_network_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforcePrivateLinkEndpointNetworkPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="enforcePrivateLinkServiceNetworkPolicies")
    def enforce_private_link_service_network_policies(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforcePrivateLinkServiceNetworkPolicies"))

    @enforce_private_link_service_network_policies.setter
    def enforce_private_link_service_network_policies(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "enforce_private_link_service_network_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforcePrivateLinkServiceNetworkPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateEndpointNetworkPoliciesEnabled")
    def private_endpoint_network_policies_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privateEndpointNetworkPoliciesEnabled"))

    @private_endpoint_network_policies_enabled.setter
    def private_endpoint_network_policies_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "private_endpoint_network_policies_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateEndpointNetworkPoliciesEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceNetworkPoliciesEnabled")
    def private_link_service_network_policies_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privateLinkServiceNetworkPoliciesEnabled"))

    @private_link_service_network_policies_enabled.setter
    def private_link_service_network_policies_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "private_link_service_network_policies_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateLinkServiceNetworkPoliciesEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceEndpointPolicyIds")
    def service_endpoint_policy_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceEndpointPolicyIds"))

    @service_endpoint_policy_ids.setter
    def service_endpoint_policy_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "service_endpoint_policy_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceEndpointPolicyIds", value)

    @builtins.property
    @jsii.member(jsii_name="serviceEndpoints")
    def service_endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceEndpoints"))

    @service_endpoints.setter
    def service_endpoints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "service_endpoints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkName")
    def virtual_network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkName"))

    @virtual_network_name.setter
    def virtual_network_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Subnet, "virtual_network_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.subnet.SubnetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "address_prefixes": "addressPrefixes",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "virtual_network_name": "virtualNetworkName",
        "delegation": "delegation",
        "enforce_private_link_endpoint_network_policies": "enforcePrivateLinkEndpointNetworkPolicies",
        "enforce_private_link_service_network_policies": "enforcePrivateLinkServiceNetworkPolicies",
        "id": "id",
        "private_endpoint_network_policies_enabled": "privateEndpointNetworkPoliciesEnabled",
        "private_link_service_network_policies_enabled": "privateLinkServiceNetworkPoliciesEnabled",
        "service_endpoint_policy_ids": "serviceEndpointPolicyIds",
        "service_endpoints": "serviceEndpoints",
        "timeouts": "timeouts",
    },
)
class SubnetConfig(cdktf.TerraformMetaArguments):
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
        address_prefixes: typing.Sequence[builtins.str],
        name: builtins.str,
        resource_group_name: builtins.str,
        virtual_network_name: builtins.str,
        delegation: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SubnetDelegation", typing.Dict[str, typing.Any]]]]] = None,
        enforce_private_link_endpoint_network_policies: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enforce_private_link_service_network_policies: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        private_endpoint_network_policies_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_link_service_network_policies_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_endpoint_policy_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_endpoints: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SubnetTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#address_prefixes Subnet#address_prefixes}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#name Subnet#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#resource_group_name Subnet#resource_group_name}.
        :param virtual_network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#virtual_network_name Subnet#virtual_network_name}.
        :param delegation: delegation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#delegation Subnet#delegation}
        :param enforce_private_link_endpoint_network_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#enforce_private_link_endpoint_network_policies Subnet#enforce_private_link_endpoint_network_policies}.
        :param enforce_private_link_service_network_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#enforce_private_link_service_network_policies Subnet#enforce_private_link_service_network_policies}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#id Subnet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param private_endpoint_network_policies_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#private_endpoint_network_policies_enabled Subnet#private_endpoint_network_policies_enabled}.
        :param private_link_service_network_policies_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#private_link_service_network_policies_enabled Subnet#private_link_service_network_policies_enabled}.
        :param service_endpoint_policy_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#service_endpoint_policy_ids Subnet#service_endpoint_policy_ids}.
        :param service_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#service_endpoints Subnet#service_endpoints}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#timeouts Subnet#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SubnetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SubnetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument address_prefixes", value=address_prefixes, expected_type=type_hints["address_prefixes"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument virtual_network_name", value=virtual_network_name, expected_type=type_hints["virtual_network_name"])
            check_type(argname="argument delegation", value=delegation, expected_type=type_hints["delegation"])
            check_type(argname="argument enforce_private_link_endpoint_network_policies", value=enforce_private_link_endpoint_network_policies, expected_type=type_hints["enforce_private_link_endpoint_network_policies"])
            check_type(argname="argument enforce_private_link_service_network_policies", value=enforce_private_link_service_network_policies, expected_type=type_hints["enforce_private_link_service_network_policies"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument private_endpoint_network_policies_enabled", value=private_endpoint_network_policies_enabled, expected_type=type_hints["private_endpoint_network_policies_enabled"])
            check_type(argname="argument private_link_service_network_policies_enabled", value=private_link_service_network_policies_enabled, expected_type=type_hints["private_link_service_network_policies_enabled"])
            check_type(argname="argument service_endpoint_policy_ids", value=service_endpoint_policy_ids, expected_type=type_hints["service_endpoint_policy_ids"])
            check_type(argname="argument service_endpoints", value=service_endpoints, expected_type=type_hints["service_endpoints"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "address_prefixes": address_prefixes,
            "name": name,
            "resource_group_name": resource_group_name,
            "virtual_network_name": virtual_network_name,
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
        if delegation is not None:
            self._values["delegation"] = delegation
        if enforce_private_link_endpoint_network_policies is not None:
            self._values["enforce_private_link_endpoint_network_policies"] = enforce_private_link_endpoint_network_policies
        if enforce_private_link_service_network_policies is not None:
            self._values["enforce_private_link_service_network_policies"] = enforce_private_link_service_network_policies
        if id is not None:
            self._values["id"] = id
        if private_endpoint_network_policies_enabled is not None:
            self._values["private_endpoint_network_policies_enabled"] = private_endpoint_network_policies_enabled
        if private_link_service_network_policies_enabled is not None:
            self._values["private_link_service_network_policies_enabled"] = private_link_service_network_policies_enabled
        if service_endpoint_policy_ids is not None:
            self._values["service_endpoint_policy_ids"] = service_endpoint_policy_ids
        if service_endpoints is not None:
            self._values["service_endpoints"] = service_endpoints
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
    def address_prefixes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#address_prefixes Subnet#address_prefixes}.'''
        result = self._values.get("address_prefixes")
        assert result is not None, "Required property 'address_prefixes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#name Subnet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#resource_group_name Subnet#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_network_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#virtual_network_name Subnet#virtual_network_name}.'''
        result = self._values.get("virtual_network_name")
        assert result is not None, "Required property 'virtual_network_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delegation(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SubnetDelegation"]]]:
        '''delegation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#delegation Subnet#delegation}
        '''
        result = self._values.get("delegation")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SubnetDelegation"]]], result)

    @builtins.property
    def enforce_private_link_endpoint_network_policies(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#enforce_private_link_endpoint_network_policies Subnet#enforce_private_link_endpoint_network_policies}.'''
        result = self._values.get("enforce_private_link_endpoint_network_policies")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enforce_private_link_service_network_policies(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#enforce_private_link_service_network_policies Subnet#enforce_private_link_service_network_policies}.'''
        result = self._values.get("enforce_private_link_service_network_policies")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#id Subnet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_endpoint_network_policies_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#private_endpoint_network_policies_enabled Subnet#private_endpoint_network_policies_enabled}.'''
        result = self._values.get("private_endpoint_network_policies_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def private_link_service_network_policies_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#private_link_service_network_policies_enabled Subnet#private_link_service_network_policies_enabled}.'''
        result = self._values.get("private_link_service_network_policies_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_endpoint_policy_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#service_endpoint_policy_ids Subnet#service_endpoint_policy_ids}.'''
        result = self._values.get("service_endpoint_policy_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_endpoints(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#service_endpoints Subnet#service_endpoints}.'''
        result = self._values.get("service_endpoints")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SubnetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#timeouts Subnet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SubnetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.subnet.SubnetDelegation",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "service_delegation": "serviceDelegation"},
)
class SubnetDelegation:
    def __init__(
        self,
        *,
        name: builtins.str,
        service_delegation: typing.Union["SubnetDelegationServiceDelegation", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#name Subnet#name}.
        :param service_delegation: service_delegation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#service_delegation Subnet#service_delegation}
        '''
        if isinstance(service_delegation, dict):
            service_delegation = SubnetDelegationServiceDelegation(**service_delegation)
        if __debug__:
            type_hints = typing.get_type_hints(SubnetDelegation.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_delegation", value=service_delegation, expected_type=type_hints["service_delegation"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "service_delegation": service_delegation,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#name Subnet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_delegation(self) -> "SubnetDelegationServiceDelegation":
        '''service_delegation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#service_delegation Subnet#service_delegation}
        '''
        result = self._values.get("service_delegation")
        assert result is not None, "Required property 'service_delegation' is missing"
        return typing.cast("SubnetDelegationServiceDelegation", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetDelegation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubnetDelegationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subnet.SubnetDelegationList",
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
            type_hints = typing.get_type_hints(SubnetDelegationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SubnetDelegationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubnetDelegationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SubnetDelegationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetDelegationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SubnetDelegationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SubnetDelegationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SubnetDelegation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SubnetDelegation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SubnetDelegation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetDelegationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SubnetDelegationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subnet.SubnetDelegationOutputReference",
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
            type_hints = typing.get_type_hints(SubnetDelegationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putServiceDelegation")
    def put_service_delegation(
        self,
        *,
        name: builtins.str,
        actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#name Subnet#name}.
        :param actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#actions Subnet#actions}.
        '''
        value = SubnetDelegationServiceDelegation(name=name, actions=actions)

        return typing.cast(None, jsii.invoke(self, "putServiceDelegation", [value]))

    @builtins.property
    @jsii.member(jsii_name="serviceDelegation")
    def service_delegation(self) -> "SubnetDelegationServiceDelegationOutputReference":
        return typing.cast("SubnetDelegationServiceDelegationOutputReference", jsii.get(self, "serviceDelegation"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceDelegationInput")
    def service_delegation_input(
        self,
    ) -> typing.Optional["SubnetDelegationServiceDelegation"]:
        return typing.cast(typing.Optional["SubnetDelegationServiceDelegation"], jsii.get(self, "serviceDelegationInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetDelegationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SubnetDelegation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SubnetDelegation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SubnetDelegation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetDelegationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.subnet.SubnetDelegationServiceDelegation",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "actions": "actions"},
)
class SubnetDelegationServiceDelegation:
    def __init__(
        self,
        *,
        name: builtins.str,
        actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#name Subnet#name}.
        :param actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#actions Subnet#actions}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubnetDelegationServiceDelegation.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if actions is not None:
            self._values["actions"] = actions

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#name Subnet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#actions Subnet#actions}.'''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetDelegationServiceDelegation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubnetDelegationServiceDelegationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subnet.SubnetDelegationServiceDelegationOutputReference",
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
            type_hints = typing.get_type_hints(SubnetDelegationServiceDelegationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetActions")
    def reset_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActions", []))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetDelegationServiceDelegationOutputReference, "actions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetDelegationServiceDelegationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SubnetDelegationServiceDelegation]:
        return typing.cast(typing.Optional[SubnetDelegationServiceDelegation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SubnetDelegationServiceDelegation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetDelegationServiceDelegationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.subnet.SubnetTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SubnetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#create Subnet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#delete Subnet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#read Subnet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#update Subnet#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SubnetTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#create Subnet#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#delete Subnet#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#read Subnet#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/subnet#update Subnet#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubnetTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.subnet.SubnetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SubnetTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SubnetTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SubnetTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SubnetTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SubnetTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SubnetTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Subnet",
    "SubnetConfig",
    "SubnetDelegation",
    "SubnetDelegationList",
    "SubnetDelegationOutputReference",
    "SubnetDelegationServiceDelegation",
    "SubnetDelegationServiceDelegationOutputReference",
    "SubnetTimeouts",
    "SubnetTimeoutsOutputReference",
]

publication.publish()
