'''
# `azurerm_databricks_workspace`

Refer to the Terraform Registory for docs: [`azurerm_databricks_workspace`](https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace).
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


class DatabricksWorkspace(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspace",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace azurerm_databricks_workspace}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: builtins.str,
        customer_managed_key_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_parameters: typing.Optional[typing.Union["DatabricksWorkspaceCustomParameters", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        infrastructure_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        load_balancer_backend_address_pool_id: typing.Optional[builtins.str] = None,
        managed_resource_group_name: typing.Optional[builtins.str] = None,
        managed_services_cmk_key_vault_key_id: typing.Optional[builtins.str] = None,
        network_security_group_rules_required: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DatabricksWorkspaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace azurerm_databricks_workspace} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#location DatabricksWorkspace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#name DatabricksWorkspace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#resource_group_name DatabricksWorkspace#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#sku DatabricksWorkspace#sku}.
        :param customer_managed_key_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#customer_managed_key_enabled DatabricksWorkspace#customer_managed_key_enabled}.
        :param custom_parameters: custom_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#custom_parameters DatabricksWorkspace#custom_parameters}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#id DatabricksWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param infrastructure_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#infrastructure_encryption_enabled DatabricksWorkspace#infrastructure_encryption_enabled}.
        :param load_balancer_backend_address_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#load_balancer_backend_address_pool_id DatabricksWorkspace#load_balancer_backend_address_pool_id}.
        :param managed_resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#managed_resource_group_name DatabricksWorkspace#managed_resource_group_name}.
        :param managed_services_cmk_key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#managed_services_cmk_key_vault_key_id DatabricksWorkspace#managed_services_cmk_key_vault_key_id}.
        :param network_security_group_rules_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#network_security_group_rules_required DatabricksWorkspace#network_security_group_rules_required}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_network_access_enabled DatabricksWorkspace#public_network_access_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#tags DatabricksWorkspace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#timeouts DatabricksWorkspace#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabricksWorkspace.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatabricksWorkspaceConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku=sku,
            customer_managed_key_enabled=customer_managed_key_enabled,
            custom_parameters=custom_parameters,
            id=id,
            infrastructure_encryption_enabled=infrastructure_encryption_enabled,
            load_balancer_backend_address_pool_id=load_balancer_backend_address_pool_id,
            managed_resource_group_name=managed_resource_group_name,
            managed_services_cmk_key_vault_key_id=managed_services_cmk_key_vault_key_id,
            network_security_group_rules_required=network_security_group_rules_required,
            public_network_access_enabled=public_network_access_enabled,
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

    @jsii.member(jsii_name="putCustomParameters")
    def put_custom_parameters(
        self,
        *,
        machine_learning_workspace_id: typing.Optional[builtins.str] = None,
        nat_gateway_name: typing.Optional[builtins.str] = None,
        no_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_subnet_name: typing.Optional[builtins.str] = None,
        private_subnet_network_security_group_association_id: typing.Optional[builtins.str] = None,
        public_ip_name: typing.Optional[builtins.str] = None,
        public_subnet_name: typing.Optional[builtins.str] = None,
        public_subnet_network_security_group_association_id: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
        storage_account_sku_name: typing.Optional[builtins.str] = None,
        virtual_network_id: typing.Optional[builtins.str] = None,
        vnet_address_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param machine_learning_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#machine_learning_workspace_id DatabricksWorkspace#machine_learning_workspace_id}.
        :param nat_gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#nat_gateway_name DatabricksWorkspace#nat_gateway_name}.
        :param no_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#no_public_ip DatabricksWorkspace#no_public_ip}.
        :param private_subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#private_subnet_name DatabricksWorkspace#private_subnet_name}.
        :param private_subnet_network_security_group_association_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#private_subnet_network_security_group_association_id DatabricksWorkspace#private_subnet_network_security_group_association_id}.
        :param public_ip_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_ip_name DatabricksWorkspace#public_ip_name}.
        :param public_subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_subnet_name DatabricksWorkspace#public_subnet_name}.
        :param public_subnet_network_security_group_association_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_subnet_network_security_group_association_id DatabricksWorkspace#public_subnet_network_security_group_association_id}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#storage_account_name DatabricksWorkspace#storage_account_name}.
        :param storage_account_sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#storage_account_sku_name DatabricksWorkspace#storage_account_sku_name}.
        :param virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#virtual_network_id DatabricksWorkspace#virtual_network_id}.
        :param vnet_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#vnet_address_prefix DatabricksWorkspace#vnet_address_prefix}.
        '''
        value = DatabricksWorkspaceCustomParameters(
            machine_learning_workspace_id=machine_learning_workspace_id,
            nat_gateway_name=nat_gateway_name,
            no_public_ip=no_public_ip,
            private_subnet_name=private_subnet_name,
            private_subnet_network_security_group_association_id=private_subnet_network_security_group_association_id,
            public_ip_name=public_ip_name,
            public_subnet_name=public_subnet_name,
            public_subnet_network_security_group_association_id=public_subnet_network_security_group_association_id,
            storage_account_name=storage_account_name,
            storage_account_sku_name=storage_account_sku_name,
            virtual_network_id=virtual_network_id,
            vnet_address_prefix=vnet_address_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomParameters", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#create DatabricksWorkspace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#delete DatabricksWorkspace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#read DatabricksWorkspace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#update DatabricksWorkspace#update}.
        '''
        value = DatabricksWorkspaceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCustomerManagedKeyEnabled")
    def reset_customer_managed_key_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedKeyEnabled", []))

    @jsii.member(jsii_name="resetCustomParameters")
    def reset_custom_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomParameters", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInfrastructureEncryptionEnabled")
    def reset_infrastructure_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInfrastructureEncryptionEnabled", []))

    @jsii.member(jsii_name="resetLoadBalancerBackendAddressPoolId")
    def reset_load_balancer_backend_address_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerBackendAddressPoolId", []))

    @jsii.member(jsii_name="resetManagedResourceGroupName")
    def reset_managed_resource_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedResourceGroupName", []))

    @jsii.member(jsii_name="resetManagedServicesCmkKeyVaultKeyId")
    def reset_managed_services_cmk_key_vault_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedServicesCmkKeyVaultKeyId", []))

    @jsii.member(jsii_name="resetNetworkSecurityGroupRulesRequired")
    def reset_network_security_group_rules_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkSecurityGroupRulesRequired", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

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
    @jsii.member(jsii_name="customParameters")
    def custom_parameters(self) -> "DatabricksWorkspaceCustomParametersOutputReference":
        return typing.cast("DatabricksWorkspaceCustomParametersOutputReference", jsii.get(self, "customParameters"))

    @builtins.property
    @jsii.member(jsii_name="managedResourceGroupId")
    def managed_resource_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedResourceGroupId"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdentity")
    def storage_account_identity(
        self,
    ) -> "DatabricksWorkspaceStorageAccountIdentityList":
        return typing.cast("DatabricksWorkspaceStorageAccountIdentityList", jsii.get(self, "storageAccountIdentity"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DatabricksWorkspaceTimeoutsOutputReference":
        return typing.cast("DatabricksWorkspaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceId"))

    @builtins.property
    @jsii.member(jsii_name="workspaceUrl")
    def workspace_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceUrl"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyEnabledInput")
    def customer_managed_key_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "customerManagedKeyEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="customParametersInput")
    def custom_parameters_input(
        self,
    ) -> typing.Optional["DatabricksWorkspaceCustomParameters"]:
        return typing.cast(typing.Optional["DatabricksWorkspaceCustomParameters"], jsii.get(self, "customParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="infrastructureEncryptionEnabledInput")
    def infrastructure_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "infrastructureEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerBackendAddressPoolIdInput")
    def load_balancer_backend_address_pool_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerBackendAddressPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managedResourceGroupNameInput")
    def managed_resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedResourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="managedServicesCmkKeyVaultKeyIdInput")
    def managed_services_cmk_key_vault_key_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedServicesCmkKeyVaultKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupRulesRequiredInput")
    def network_security_group_rules_required_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkSecurityGroupRulesRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DatabricksWorkspaceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DatabricksWorkspaceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyEnabled")
    def customer_managed_key_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "customerManagedKeyEnabled"))

    @customer_managed_key_enabled.setter
    def customer_managed_key_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "customer_managed_key_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKeyEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="infrastructureEncryptionEnabled")
    def infrastructure_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "infrastructureEncryptionEnabled"))

    @infrastructure_encryption_enabled.setter
    def infrastructure_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "infrastructure_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "infrastructureEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerBackendAddressPoolId")
    def load_balancer_backend_address_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerBackendAddressPoolId"))

    @load_balancer_backend_address_pool_id.setter
    def load_balancer_backend_address_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "load_balancer_backend_address_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerBackendAddressPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="managedResourceGroupName")
    def managed_resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedResourceGroupName"))

    @managed_resource_group_name.setter
    def managed_resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "managed_resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedResourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="managedServicesCmkKeyVaultKeyId")
    def managed_services_cmk_key_vault_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedServicesCmkKeyVaultKeyId"))

    @managed_services_cmk_key_vault_key_id.setter
    def managed_services_cmk_key_vault_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "managed_services_cmk_key_vault_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedServicesCmkKeyVaultKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupRulesRequired")
    def network_security_group_rules_required(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkSecurityGroupRulesRequired"))

    @network_security_group_rules_required.setter
    def network_security_group_rules_required(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "network_security_group_rules_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSecurityGroupRulesRequired", value)

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabled")
    def public_network_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicNetworkAccessEnabled"))

    @public_network_access_enabled.setter
    def public_network_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspace, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspaceConfig",
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
        "sku": "sku",
        "customer_managed_key_enabled": "customerManagedKeyEnabled",
        "custom_parameters": "customParameters",
        "id": "id",
        "infrastructure_encryption_enabled": "infrastructureEncryptionEnabled",
        "load_balancer_backend_address_pool_id": "loadBalancerBackendAddressPoolId",
        "managed_resource_group_name": "managedResourceGroupName",
        "managed_services_cmk_key_vault_key_id": "managedServicesCmkKeyVaultKeyId",
        "network_security_group_rules_required": "networkSecurityGroupRulesRequired",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class DatabricksWorkspaceConfig(cdktf.TerraformMetaArguments):
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
        sku: builtins.str,
        customer_managed_key_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_parameters: typing.Optional[typing.Union["DatabricksWorkspaceCustomParameters", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        infrastructure_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        load_balancer_backend_address_pool_id: typing.Optional[builtins.str] = None,
        managed_resource_group_name: typing.Optional[builtins.str] = None,
        managed_services_cmk_key_vault_key_id: typing.Optional[builtins.str] = None,
        network_security_group_rules_required: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DatabricksWorkspaceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#location DatabricksWorkspace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#name DatabricksWorkspace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#resource_group_name DatabricksWorkspace#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#sku DatabricksWorkspace#sku}.
        :param customer_managed_key_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#customer_managed_key_enabled DatabricksWorkspace#customer_managed_key_enabled}.
        :param custom_parameters: custom_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#custom_parameters DatabricksWorkspace#custom_parameters}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#id DatabricksWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param infrastructure_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#infrastructure_encryption_enabled DatabricksWorkspace#infrastructure_encryption_enabled}.
        :param load_balancer_backend_address_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#load_balancer_backend_address_pool_id DatabricksWorkspace#load_balancer_backend_address_pool_id}.
        :param managed_resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#managed_resource_group_name DatabricksWorkspace#managed_resource_group_name}.
        :param managed_services_cmk_key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#managed_services_cmk_key_vault_key_id DatabricksWorkspace#managed_services_cmk_key_vault_key_id}.
        :param network_security_group_rules_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#network_security_group_rules_required DatabricksWorkspace#network_security_group_rules_required}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_network_access_enabled DatabricksWorkspace#public_network_access_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#tags DatabricksWorkspace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#timeouts DatabricksWorkspace#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(custom_parameters, dict):
            custom_parameters = DatabricksWorkspaceCustomParameters(**custom_parameters)
        if isinstance(timeouts, dict):
            timeouts = DatabricksWorkspaceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DatabricksWorkspaceConfig.__init__)
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
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument customer_managed_key_enabled", value=customer_managed_key_enabled, expected_type=type_hints["customer_managed_key_enabled"])
            check_type(argname="argument custom_parameters", value=custom_parameters, expected_type=type_hints["custom_parameters"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument infrastructure_encryption_enabled", value=infrastructure_encryption_enabled, expected_type=type_hints["infrastructure_encryption_enabled"])
            check_type(argname="argument load_balancer_backend_address_pool_id", value=load_balancer_backend_address_pool_id, expected_type=type_hints["load_balancer_backend_address_pool_id"])
            check_type(argname="argument managed_resource_group_name", value=managed_resource_group_name, expected_type=type_hints["managed_resource_group_name"])
            check_type(argname="argument managed_services_cmk_key_vault_key_id", value=managed_services_cmk_key_vault_key_id, expected_type=type_hints["managed_services_cmk_key_vault_key_id"])
            check_type(argname="argument network_security_group_rules_required", value=network_security_group_rules_required, expected_type=type_hints["network_security_group_rules_required"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if customer_managed_key_enabled is not None:
            self._values["customer_managed_key_enabled"] = customer_managed_key_enabled
        if custom_parameters is not None:
            self._values["custom_parameters"] = custom_parameters
        if id is not None:
            self._values["id"] = id
        if infrastructure_encryption_enabled is not None:
            self._values["infrastructure_encryption_enabled"] = infrastructure_encryption_enabled
        if load_balancer_backend_address_pool_id is not None:
            self._values["load_balancer_backend_address_pool_id"] = load_balancer_backend_address_pool_id
        if managed_resource_group_name is not None:
            self._values["managed_resource_group_name"] = managed_resource_group_name
        if managed_services_cmk_key_vault_key_id is not None:
            self._values["managed_services_cmk_key_vault_key_id"] = managed_services_cmk_key_vault_key_id
        if network_security_group_rules_required is not None:
            self._values["network_security_group_rules_required"] = network_security_group_rules_required
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#location DatabricksWorkspace#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#name DatabricksWorkspace#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#resource_group_name DatabricksWorkspace#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#sku DatabricksWorkspace#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def customer_managed_key_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#customer_managed_key_enabled DatabricksWorkspace#customer_managed_key_enabled}.'''
        result = self._values.get("customer_managed_key_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_parameters(
        self,
    ) -> typing.Optional["DatabricksWorkspaceCustomParameters"]:
        '''custom_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#custom_parameters DatabricksWorkspace#custom_parameters}
        '''
        result = self._values.get("custom_parameters")
        return typing.cast(typing.Optional["DatabricksWorkspaceCustomParameters"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#id DatabricksWorkspace#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def infrastructure_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#infrastructure_encryption_enabled DatabricksWorkspace#infrastructure_encryption_enabled}.'''
        result = self._values.get("infrastructure_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def load_balancer_backend_address_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#load_balancer_backend_address_pool_id DatabricksWorkspace#load_balancer_backend_address_pool_id}.'''
        result = self._values.get("load_balancer_backend_address_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_resource_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#managed_resource_group_name DatabricksWorkspace#managed_resource_group_name}.'''
        result = self._values.get("managed_resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_services_cmk_key_vault_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#managed_services_cmk_key_vault_key_id DatabricksWorkspace#managed_services_cmk_key_vault_key_id}.'''
        result = self._values.get("managed_services_cmk_key_vault_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_security_group_rules_required(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#network_security_group_rules_required DatabricksWorkspace#network_security_group_rules_required}.'''
        result = self._values.get("network_security_group_rules_required")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_network_access_enabled DatabricksWorkspace#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#tags DatabricksWorkspace#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DatabricksWorkspaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#timeouts DatabricksWorkspace#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DatabricksWorkspaceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabricksWorkspaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspaceCustomParameters",
    jsii_struct_bases=[],
    name_mapping={
        "machine_learning_workspace_id": "machineLearningWorkspaceId",
        "nat_gateway_name": "natGatewayName",
        "no_public_ip": "noPublicIp",
        "private_subnet_name": "privateSubnetName",
        "private_subnet_network_security_group_association_id": "privateSubnetNetworkSecurityGroupAssociationId",
        "public_ip_name": "publicIpName",
        "public_subnet_name": "publicSubnetName",
        "public_subnet_network_security_group_association_id": "publicSubnetNetworkSecurityGroupAssociationId",
        "storage_account_name": "storageAccountName",
        "storage_account_sku_name": "storageAccountSkuName",
        "virtual_network_id": "virtualNetworkId",
        "vnet_address_prefix": "vnetAddressPrefix",
    },
)
class DatabricksWorkspaceCustomParameters:
    def __init__(
        self,
        *,
        machine_learning_workspace_id: typing.Optional[builtins.str] = None,
        nat_gateway_name: typing.Optional[builtins.str] = None,
        no_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_subnet_name: typing.Optional[builtins.str] = None,
        private_subnet_network_security_group_association_id: typing.Optional[builtins.str] = None,
        public_ip_name: typing.Optional[builtins.str] = None,
        public_subnet_name: typing.Optional[builtins.str] = None,
        public_subnet_network_security_group_association_id: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
        storage_account_sku_name: typing.Optional[builtins.str] = None,
        virtual_network_id: typing.Optional[builtins.str] = None,
        vnet_address_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param machine_learning_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#machine_learning_workspace_id DatabricksWorkspace#machine_learning_workspace_id}.
        :param nat_gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#nat_gateway_name DatabricksWorkspace#nat_gateway_name}.
        :param no_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#no_public_ip DatabricksWorkspace#no_public_ip}.
        :param private_subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#private_subnet_name DatabricksWorkspace#private_subnet_name}.
        :param private_subnet_network_security_group_association_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#private_subnet_network_security_group_association_id DatabricksWorkspace#private_subnet_network_security_group_association_id}.
        :param public_ip_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_ip_name DatabricksWorkspace#public_ip_name}.
        :param public_subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_subnet_name DatabricksWorkspace#public_subnet_name}.
        :param public_subnet_network_security_group_association_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_subnet_network_security_group_association_id DatabricksWorkspace#public_subnet_network_security_group_association_id}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#storage_account_name DatabricksWorkspace#storage_account_name}.
        :param storage_account_sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#storage_account_sku_name DatabricksWorkspace#storage_account_sku_name}.
        :param virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#virtual_network_id DatabricksWorkspace#virtual_network_id}.
        :param vnet_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#vnet_address_prefix DatabricksWorkspace#vnet_address_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabricksWorkspaceCustomParameters.__init__)
            check_type(argname="argument machine_learning_workspace_id", value=machine_learning_workspace_id, expected_type=type_hints["machine_learning_workspace_id"])
            check_type(argname="argument nat_gateway_name", value=nat_gateway_name, expected_type=type_hints["nat_gateway_name"])
            check_type(argname="argument no_public_ip", value=no_public_ip, expected_type=type_hints["no_public_ip"])
            check_type(argname="argument private_subnet_name", value=private_subnet_name, expected_type=type_hints["private_subnet_name"])
            check_type(argname="argument private_subnet_network_security_group_association_id", value=private_subnet_network_security_group_association_id, expected_type=type_hints["private_subnet_network_security_group_association_id"])
            check_type(argname="argument public_ip_name", value=public_ip_name, expected_type=type_hints["public_ip_name"])
            check_type(argname="argument public_subnet_name", value=public_subnet_name, expected_type=type_hints["public_subnet_name"])
            check_type(argname="argument public_subnet_network_security_group_association_id", value=public_subnet_network_security_group_association_id, expected_type=type_hints["public_subnet_network_security_group_association_id"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
            check_type(argname="argument storage_account_sku_name", value=storage_account_sku_name, expected_type=type_hints["storage_account_sku_name"])
            check_type(argname="argument virtual_network_id", value=virtual_network_id, expected_type=type_hints["virtual_network_id"])
            check_type(argname="argument vnet_address_prefix", value=vnet_address_prefix, expected_type=type_hints["vnet_address_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if machine_learning_workspace_id is not None:
            self._values["machine_learning_workspace_id"] = machine_learning_workspace_id
        if nat_gateway_name is not None:
            self._values["nat_gateway_name"] = nat_gateway_name
        if no_public_ip is not None:
            self._values["no_public_ip"] = no_public_ip
        if private_subnet_name is not None:
            self._values["private_subnet_name"] = private_subnet_name
        if private_subnet_network_security_group_association_id is not None:
            self._values["private_subnet_network_security_group_association_id"] = private_subnet_network_security_group_association_id
        if public_ip_name is not None:
            self._values["public_ip_name"] = public_ip_name
        if public_subnet_name is not None:
            self._values["public_subnet_name"] = public_subnet_name
        if public_subnet_network_security_group_association_id is not None:
            self._values["public_subnet_network_security_group_association_id"] = public_subnet_network_security_group_association_id
        if storage_account_name is not None:
            self._values["storage_account_name"] = storage_account_name
        if storage_account_sku_name is not None:
            self._values["storage_account_sku_name"] = storage_account_sku_name
        if virtual_network_id is not None:
            self._values["virtual_network_id"] = virtual_network_id
        if vnet_address_prefix is not None:
            self._values["vnet_address_prefix"] = vnet_address_prefix

    @builtins.property
    def machine_learning_workspace_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#machine_learning_workspace_id DatabricksWorkspace#machine_learning_workspace_id}.'''
        result = self._values.get("machine_learning_workspace_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nat_gateway_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#nat_gateway_name DatabricksWorkspace#nat_gateway_name}.'''
        result = self._values.get("nat_gateway_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#no_public_ip DatabricksWorkspace#no_public_ip}.'''
        result = self._values.get("no_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def private_subnet_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#private_subnet_name DatabricksWorkspace#private_subnet_name}.'''
        result = self._values.get("private_subnet_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_subnet_network_security_group_association_id(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#private_subnet_network_security_group_association_id DatabricksWorkspace#private_subnet_network_security_group_association_id}.'''
        result = self._values.get("private_subnet_network_security_group_association_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_ip_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_ip_name DatabricksWorkspace#public_ip_name}.'''
        result = self._values.get("public_ip_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_subnet_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_subnet_name DatabricksWorkspace#public_subnet_name}.'''
        result = self._values.get("public_subnet_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_subnet_network_security_group_association_id(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#public_subnet_network_security_group_association_id DatabricksWorkspace#public_subnet_network_security_group_association_id}.'''
        result = self._values.get("public_subnet_network_security_group_association_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#storage_account_name DatabricksWorkspace#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_sku_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#storage_account_sku_name DatabricksWorkspace#storage_account_sku_name}.'''
        result = self._values.get("storage_account_sku_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#virtual_network_id DatabricksWorkspace#virtual_network_id}.'''
        result = self._values.get("virtual_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vnet_address_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#vnet_address_prefix DatabricksWorkspace#vnet_address_prefix}.'''
        result = self._values.get("vnet_address_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabricksWorkspaceCustomParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabricksWorkspaceCustomParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspaceCustomParametersOutputReference",
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
            type_hints = typing.get_type_hints(DatabricksWorkspaceCustomParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMachineLearningWorkspaceId")
    def reset_machine_learning_workspace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineLearningWorkspaceId", []))

    @jsii.member(jsii_name="resetNatGatewayName")
    def reset_nat_gateway_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNatGatewayName", []))

    @jsii.member(jsii_name="resetNoPublicIp")
    def reset_no_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoPublicIp", []))

    @jsii.member(jsii_name="resetPrivateSubnetName")
    def reset_private_subnet_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateSubnetName", []))

    @jsii.member(jsii_name="resetPrivateSubnetNetworkSecurityGroupAssociationId")
    def reset_private_subnet_network_security_group_association_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateSubnetNetworkSecurityGroupAssociationId", []))

    @jsii.member(jsii_name="resetPublicIpName")
    def reset_public_ip_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpName", []))

    @jsii.member(jsii_name="resetPublicSubnetName")
    def reset_public_subnet_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicSubnetName", []))

    @jsii.member(jsii_name="resetPublicSubnetNetworkSecurityGroupAssociationId")
    def reset_public_subnet_network_security_group_association_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicSubnetNetworkSecurityGroupAssociationId", []))

    @jsii.member(jsii_name="resetStorageAccountName")
    def reset_storage_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountName", []))

    @jsii.member(jsii_name="resetStorageAccountSkuName")
    def reset_storage_account_sku_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountSkuName", []))

    @jsii.member(jsii_name="resetVirtualNetworkId")
    def reset_virtual_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkId", []))

    @jsii.member(jsii_name="resetVnetAddressPrefix")
    def reset_vnet_address_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnetAddressPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="machineLearningWorkspaceIdInput")
    def machine_learning_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineLearningWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="natGatewayNameInput")
    def nat_gateway_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "natGatewayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="noPublicIpInput")
    def no_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="privateSubnetNameInput")
    def private_subnet_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateSubnetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateSubnetNetworkSecurityGroupAssociationIdInput")
    def private_subnet_network_security_group_association_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateSubnetNetworkSecurityGroupAssociationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpNameInput")
    def public_ip_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpNameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicSubnetNameInput")
    def public_subnet_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicSubnetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicSubnetNetworkSecurityGroupAssociationIdInput")
    def public_subnet_network_security_group_association_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicSubnetNetworkSecurityGroupAssociationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountSkuNameInput")
    def storage_account_sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountSkuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkIdInput")
    def virtual_network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vnetAddressPrefixInput")
    def vnet_address_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vnetAddressPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="machineLearningWorkspaceId")
    def machine_learning_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineLearningWorkspaceId"))

    @machine_learning_workspace_id.setter
    def machine_learning_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "machine_learning_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineLearningWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="natGatewayName")
    def nat_gateway_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natGatewayName"))

    @nat_gateway_name.setter
    def nat_gateway_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "nat_gateway_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "natGatewayName", value)

    @builtins.property
    @jsii.member(jsii_name="noPublicIp")
    def no_public_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noPublicIp"))

    @no_public_ip.setter
    def no_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "no_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="privateSubnetName")
    def private_subnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateSubnetName"))

    @private_subnet_name.setter
    def private_subnet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "private_subnet_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetName", value)

    @builtins.property
    @jsii.member(jsii_name="privateSubnetNetworkSecurityGroupAssociationId")
    def private_subnet_network_security_group_association_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateSubnetNetworkSecurityGroupAssociationId"))

    @private_subnet_network_security_group_association_id.setter
    def private_subnet_network_security_group_association_id(
        self,
        value: builtins.str,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "private_subnet_network_security_group_association_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetNetworkSecurityGroupAssociationId", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpName")
    def public_ip_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpName"))

    @public_ip_name.setter
    def public_ip_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "public_ip_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpName", value)

    @builtins.property
    @jsii.member(jsii_name="publicSubnetName")
    def public_subnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicSubnetName"))

    @public_subnet_name.setter
    def public_subnet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "public_subnet_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetName", value)

    @builtins.property
    @jsii.member(jsii_name="publicSubnetNetworkSecurityGroupAssociationId")
    def public_subnet_network_security_group_association_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicSubnetNetworkSecurityGroupAssociationId"))

    @public_subnet_network_security_group_association_id.setter
    def public_subnet_network_security_group_association_id(
        self,
        value: builtins.str,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "public_subnet_network_security_group_association_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetNetworkSecurityGroupAssociationId", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "storage_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountSkuName")
    def storage_account_sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountSkuName"))

    @storage_account_sku_name.setter
    def storage_account_sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "storage_account_sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountSkuName", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkId")
    def virtual_network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkId"))

    @virtual_network_id.setter
    def virtual_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "virtual_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="vnetAddressPrefix")
    def vnet_address_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnetAddressPrefix"))

    @vnet_address_prefix.setter
    def vnet_address_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "vnet_address_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnetAddressPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabricksWorkspaceCustomParameters]:
        return typing.cast(typing.Optional[DatabricksWorkspaceCustomParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabricksWorkspaceCustomParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceCustomParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspaceStorageAccountIdentity",
    jsii_struct_bases=[],
    name_mapping={},
)
class DatabricksWorkspaceStorageAccountIdentity:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabricksWorkspaceStorageAccountIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabricksWorkspaceStorageAccountIdentityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspaceStorageAccountIdentityList",
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
            type_hints = typing.get_type_hints(DatabricksWorkspaceStorageAccountIdentityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatabricksWorkspaceStorageAccountIdentityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabricksWorkspaceStorageAccountIdentityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatabricksWorkspaceStorageAccountIdentityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceStorageAccountIdentityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceStorageAccountIdentityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceStorageAccountIdentityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DatabricksWorkspaceStorageAccountIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspaceStorageAccountIdentityOutputReference",
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
            type_hints = typing.get_type_hints(DatabricksWorkspaceStorageAccountIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabricksWorkspaceStorageAccountIdentity]:
        return typing.cast(typing.Optional[DatabricksWorkspaceStorageAccountIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabricksWorkspaceStorageAccountIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceStorageAccountIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DatabricksWorkspaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#create DatabricksWorkspace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#delete DatabricksWorkspace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#read DatabricksWorkspace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#update DatabricksWorkspace#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabricksWorkspaceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#create DatabricksWorkspace#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#delete DatabricksWorkspace#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#read DatabricksWorkspace#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace#update DatabricksWorkspace#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabricksWorkspaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabricksWorkspaceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.databricksWorkspace.DatabricksWorkspaceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DatabricksWorkspaceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabricksWorkspaceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabricksWorkspaceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabricksWorkspaceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabricksWorkspaceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatabricksWorkspace",
    "DatabricksWorkspaceConfig",
    "DatabricksWorkspaceCustomParameters",
    "DatabricksWorkspaceCustomParametersOutputReference",
    "DatabricksWorkspaceStorageAccountIdentity",
    "DatabricksWorkspaceStorageAccountIdentityList",
    "DatabricksWorkspaceStorageAccountIdentityOutputReference",
    "DatabricksWorkspaceTimeouts",
    "DatabricksWorkspaceTimeoutsOutputReference",
]

publication.publish()
