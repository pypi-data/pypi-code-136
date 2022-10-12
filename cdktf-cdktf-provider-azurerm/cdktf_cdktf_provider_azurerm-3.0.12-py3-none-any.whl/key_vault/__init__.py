'''
# `azurerm_key_vault`

Refer to the Terraform Registory for docs: [`azurerm_key_vault`](https://www.terraform.io/docs/providers/azurerm/r/key_vault).
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


class KeyVault(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVault",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault azurerm_key_vault}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        tenant_id: builtins.str,
        access_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyVaultAccessPolicy", typing.Dict[str, typing.Any]]]]] = None,
        contact: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyVaultContact", typing.Dict[str, typing.Any]]]]] = None,
        enabled_for_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled_for_disk_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled_for_template_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_rbac_authorization: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        network_acls: typing.Optional[typing.Union["KeyVaultNetworkAcls", typing.Dict[str, typing.Any]]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        purge_protection_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        soft_delete_retention_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyVaultTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault azurerm_key_vault} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#location KeyVault#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#name KeyVault#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#resource_group_name KeyVault#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#sku_name KeyVault#sku_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#tenant_id KeyVault#tenant_id}.
        :param access_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#access_policy KeyVault#access_policy}.
        :param contact: contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#contact KeyVault#contact}
        :param enabled_for_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_deployment KeyVault#enabled_for_deployment}.
        :param enabled_for_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_disk_encryption KeyVault#enabled_for_disk_encryption}.
        :param enabled_for_template_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_template_deployment KeyVault#enabled_for_template_deployment}.
        :param enable_rbac_authorization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enable_rbac_authorization KeyVault#enable_rbac_authorization}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#id KeyVault#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network_acls: network_acls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#network_acls KeyVault#network_acls}
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#public_network_access_enabled KeyVault#public_network_access_enabled}.
        :param purge_protection_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#purge_protection_enabled KeyVault#purge_protection_enabled}.
        :param soft_delete_retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#soft_delete_retention_days KeyVault#soft_delete_retention_days}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#tags KeyVault#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#timeouts KeyVault#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVault.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KeyVaultConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            tenant_id=tenant_id,
            access_policy=access_policy,
            contact=contact,
            enabled_for_deployment=enabled_for_deployment,
            enabled_for_disk_encryption=enabled_for_disk_encryption,
            enabled_for_template_deployment=enabled_for_template_deployment,
            enable_rbac_authorization=enable_rbac_authorization,
            id=id,
            network_acls=network_acls,
            public_network_access_enabled=public_network_access_enabled,
            purge_protection_enabled=purge_protection_enabled,
            soft_delete_retention_days=soft_delete_retention_days,
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

    @jsii.member(jsii_name="putAccessPolicy")
    def put_access_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyVaultAccessPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVault.put_access_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessPolicy", [value]))

    @jsii.member(jsii_name="putContact")
    def put_contact(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyVaultContact", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVault.put_contact)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContact", [value]))

    @jsii.member(jsii_name="putNetworkAcls")
    def put_network_acls(
        self,
        *,
        bypass: builtins.str,
        default_action: builtins.str,
        ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#bypass KeyVault#bypass}.
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#default_action KeyVault#default_action}.
        :param ip_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#ip_rules KeyVault#ip_rules}.
        :param virtual_network_subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#virtual_network_subnet_ids KeyVault#virtual_network_subnet_ids}.
        '''
        value = KeyVaultNetworkAcls(
            bypass=bypass,
            default_action=default_action,
            ip_rules=ip_rules,
            virtual_network_subnet_ids=virtual_network_subnet_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkAcls", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#create KeyVault#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#delete KeyVault#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#read KeyVault#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#update KeyVault#update}.
        '''
        value = KeyVaultTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccessPolicy")
    def reset_access_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessPolicy", []))

    @jsii.member(jsii_name="resetContact")
    def reset_contact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContact", []))

    @jsii.member(jsii_name="resetEnabledForDeployment")
    def reset_enabled_for_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledForDeployment", []))

    @jsii.member(jsii_name="resetEnabledForDiskEncryption")
    def reset_enabled_for_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledForDiskEncryption", []))

    @jsii.member(jsii_name="resetEnabledForTemplateDeployment")
    def reset_enabled_for_template_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledForTemplateDeployment", []))

    @jsii.member(jsii_name="resetEnableRbacAuthorization")
    def reset_enable_rbac_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableRbacAuthorization", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNetworkAcls")
    def reset_network_acls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkAcls", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetPurgeProtectionEnabled")
    def reset_purge_protection_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurgeProtectionEnabled", []))

    @jsii.member(jsii_name="resetSoftDeleteRetentionDays")
    def reset_soft_delete_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoftDeleteRetentionDays", []))

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
    @jsii.member(jsii_name="accessPolicy")
    def access_policy(self) -> "KeyVaultAccessPolicyList":
        return typing.cast("KeyVaultAccessPolicyList", jsii.get(self, "accessPolicy"))

    @builtins.property
    @jsii.member(jsii_name="contact")
    def contact(self) -> "KeyVaultContactList":
        return typing.cast("KeyVaultContactList", jsii.get(self, "contact"))

    @builtins.property
    @jsii.member(jsii_name="networkAcls")
    def network_acls(self) -> "KeyVaultNetworkAclsOutputReference":
        return typing.cast("KeyVaultNetworkAclsOutputReference", jsii.get(self, "networkAcls"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KeyVaultTimeoutsOutputReference":
        return typing.cast("KeyVaultTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vaultUri")
    def vault_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultUri"))

    @builtins.property
    @jsii.member(jsii_name="accessPolicyInput")
    def access_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyVaultAccessPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyVaultAccessPolicy"]]], jsii.get(self, "accessPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="contactInput")
    def contact_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyVaultContact"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyVaultContact"]]], jsii.get(self, "contactInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledForDeploymentInput")
    def enabled_for_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledForDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledForDiskEncryptionInput")
    def enabled_for_disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledForDiskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledForTemplateDeploymentInput")
    def enabled_for_template_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledForTemplateDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="enableRbacAuthorizationInput")
    def enable_rbac_authorization_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableRbacAuthorizationInput"))

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
    @jsii.member(jsii_name="networkAclsInput")
    def network_acls_input(self) -> typing.Optional["KeyVaultNetworkAcls"]:
        return typing.cast(typing.Optional["KeyVaultNetworkAcls"], jsii.get(self, "networkAclsInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="purgeProtectionEnabledInput")
    def purge_protection_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "purgeProtectionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="softDeleteRetentionDaysInput")
    def soft_delete_retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "softDeleteRetentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KeyVaultTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KeyVaultTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledForDeployment")
    def enabled_for_deployment(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabledForDeployment"))

    @enabled_for_deployment.setter
    def enabled_for_deployment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "enabled_for_deployment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledForDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="enabledForDiskEncryption")
    def enabled_for_disk_encryption(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabledForDiskEncryption"))

    @enabled_for_disk_encryption.setter
    def enabled_for_disk_encryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "enabled_for_disk_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledForDiskEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="enabledForTemplateDeployment")
    def enabled_for_template_deployment(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabledForTemplateDeployment"))

    @enabled_for_template_deployment.setter
    def enabled_for_template_deployment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "enabled_for_template_deployment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledForTemplateDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="enableRbacAuthorization")
    def enable_rbac_authorization(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableRbacAuthorization"))

    @enable_rbac_authorization.setter
    def enable_rbac_authorization(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "enable_rbac_authorization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableRbacAuthorization", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

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
            type_hints = typing.get_type_hints(getattr(KeyVault, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="purgeProtectionEnabled")
    def purge_protection_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "purgeProtectionEnabled"))

    @purge_protection_enabled.setter
    def purge_protection_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "purge_protection_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purgeProtectionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="softDeleteRetentionDays")
    def soft_delete_retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "softDeleteRetentionDays"))

    @soft_delete_retention_days.setter
    def soft_delete_retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "soft_delete_retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "softDeleteRetentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVault, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultAccessPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "certificate_permissions": "certificatePermissions",
        "key_permissions": "keyPermissions",
        "object_id": "objectId",
        "secret_permissions": "secretPermissions",
        "storage_permissions": "storagePermissions",
        "tenant_id": "tenantId",
    },
)
class KeyVaultAccessPolicy:
    def __init__(
        self,
        *,
        application_id: typing.Optional[builtins.str] = None,
        certificate_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        object_id: typing.Optional[builtins.str] = None,
        secret_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#application_id KeyVault#application_id}.
        :param certificate_permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#certificate_permissions KeyVault#certificate_permissions}.
        :param key_permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#key_permissions KeyVault#key_permissions}.
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#object_id KeyVault#object_id}.
        :param secret_permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#secret_permissions KeyVault#secret_permissions}.
        :param storage_permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#storage_permissions KeyVault#storage_permissions}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#tenant_id KeyVault#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultAccessPolicy.__init__)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument certificate_permissions", value=certificate_permissions, expected_type=type_hints["certificate_permissions"])
            check_type(argname="argument key_permissions", value=key_permissions, expected_type=type_hints["key_permissions"])
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument secret_permissions", value=secret_permissions, expected_type=type_hints["secret_permissions"])
            check_type(argname="argument storage_permissions", value=storage_permissions, expected_type=type_hints["storage_permissions"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if application_id is not None:
            self._values["application_id"] = application_id
        if certificate_permissions is not None:
            self._values["certificate_permissions"] = certificate_permissions
        if key_permissions is not None:
            self._values["key_permissions"] = key_permissions
        if object_id is not None:
            self._values["object_id"] = object_id
        if secret_permissions is not None:
            self._values["secret_permissions"] = secret_permissions
        if storage_permissions is not None:
            self._values["storage_permissions"] = storage_permissions
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def application_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#application_id KeyVault#application_id}.'''
        result = self._values.get("application_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#certificate_permissions KeyVault#certificate_permissions}.'''
        result = self._values.get("certificate_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#key_permissions KeyVault#key_permissions}.'''
        result = self._values.get("key_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def object_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#object_id KeyVault#object_id}.'''
        result = self._values.get("object_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#secret_permissions KeyVault#secret_permissions}.'''
        result = self._values.get("secret_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#storage_permissions KeyVault#storage_permissions}.'''
        result = self._values.get("storage_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#tenant_id KeyVault#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultAccessPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultAccessPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultAccessPolicyList",
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
            type_hints = typing.get_type_hints(KeyVaultAccessPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KeyVaultAccessPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultAccessPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyVaultAccessPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultAccessPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultAccessPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultAccessPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyVaultAccessPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultAccessPolicyOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultAccessPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetApplicationId")
    def reset_application_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationId", []))

    @jsii.member(jsii_name="resetCertificatePermissions")
    def reset_certificate_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePermissions", []))

    @jsii.member(jsii_name="resetKeyPermissions")
    def reset_key_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPermissions", []))

    @jsii.member(jsii_name="resetObjectId")
    def reset_object_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectId", []))

    @jsii.member(jsii_name="resetSecretPermissions")
    def reset_secret_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretPermissions", []))

    @jsii.member(jsii_name="resetStoragePermissions")
    def reset_storage_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoragePermissions", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePermissionsInput")
    def certificate_permissions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificatePermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPermissionsInput")
    def key_permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keyPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdInput")
    def object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretPermissionsInput")
    def secret_permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secretPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="storagePermissionsInput")
    def storage_permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "storagePermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyOutputReference, "application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePermissions")
    def certificate_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificatePermissions"))

    @certificate_permissions.setter
    def certificate_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyOutputReference, "certificate_permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePermissions", value)

    @builtins.property
    @jsii.member(jsii_name="keyPermissions")
    def key_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keyPermissions"))

    @key_permissions.setter
    def key_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyOutputReference, "key_permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @object_id.setter
    def object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyOutputReference, "object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectId", value)

    @builtins.property
    @jsii.member(jsii_name="secretPermissions")
    def secret_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secretPermissions"))

    @secret_permissions.setter
    def secret_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyOutputReference, "secret_permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="storagePermissions")
    def storage_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "storagePermissions"))

    @storage_permissions.setter
    def storage_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyOutputReference, "storage_permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storagePermissions", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyVaultAccessPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyVaultAccessPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyVaultAccessPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultAccessPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultConfig",
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
        "sku_name": "skuName",
        "tenant_id": "tenantId",
        "access_policy": "accessPolicy",
        "contact": "contact",
        "enabled_for_deployment": "enabledForDeployment",
        "enabled_for_disk_encryption": "enabledForDiskEncryption",
        "enabled_for_template_deployment": "enabledForTemplateDeployment",
        "enable_rbac_authorization": "enableRbacAuthorization",
        "id": "id",
        "network_acls": "networkAcls",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "purge_protection_enabled": "purgeProtectionEnabled",
        "soft_delete_retention_days": "softDeleteRetentionDays",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class KeyVaultConfig(cdktf.TerraformMetaArguments):
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
        sku_name: builtins.str,
        tenant_id: builtins.str,
        access_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyVaultAccessPolicy, typing.Dict[str, typing.Any]]]]] = None,
        contact: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyVaultContact", typing.Dict[str, typing.Any]]]]] = None,
        enabled_for_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled_for_disk_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled_for_template_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_rbac_authorization: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        network_acls: typing.Optional[typing.Union["KeyVaultNetworkAcls", typing.Dict[str, typing.Any]]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        purge_protection_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        soft_delete_retention_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyVaultTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#location KeyVault#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#name KeyVault#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#resource_group_name KeyVault#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#sku_name KeyVault#sku_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#tenant_id KeyVault#tenant_id}.
        :param access_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#access_policy KeyVault#access_policy}.
        :param contact: contact block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#contact KeyVault#contact}
        :param enabled_for_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_deployment KeyVault#enabled_for_deployment}.
        :param enabled_for_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_disk_encryption KeyVault#enabled_for_disk_encryption}.
        :param enabled_for_template_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_template_deployment KeyVault#enabled_for_template_deployment}.
        :param enable_rbac_authorization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enable_rbac_authorization KeyVault#enable_rbac_authorization}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#id KeyVault#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network_acls: network_acls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#network_acls KeyVault#network_acls}
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#public_network_access_enabled KeyVault#public_network_access_enabled}.
        :param purge_protection_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#purge_protection_enabled KeyVault#purge_protection_enabled}.
        :param soft_delete_retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#soft_delete_retention_days KeyVault#soft_delete_retention_days}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#tags KeyVault#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#timeouts KeyVault#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(network_acls, dict):
            network_acls = KeyVaultNetworkAcls(**network_acls)
        if isinstance(timeouts, dict):
            timeouts = KeyVaultTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultConfig.__init__)
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
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument access_policy", value=access_policy, expected_type=type_hints["access_policy"])
            check_type(argname="argument contact", value=contact, expected_type=type_hints["contact"])
            check_type(argname="argument enabled_for_deployment", value=enabled_for_deployment, expected_type=type_hints["enabled_for_deployment"])
            check_type(argname="argument enabled_for_disk_encryption", value=enabled_for_disk_encryption, expected_type=type_hints["enabled_for_disk_encryption"])
            check_type(argname="argument enabled_for_template_deployment", value=enabled_for_template_deployment, expected_type=type_hints["enabled_for_template_deployment"])
            check_type(argname="argument enable_rbac_authorization", value=enable_rbac_authorization, expected_type=type_hints["enable_rbac_authorization"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument network_acls", value=network_acls, expected_type=type_hints["network_acls"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument purge_protection_enabled", value=purge_protection_enabled, expected_type=type_hints["purge_protection_enabled"])
            check_type(argname="argument soft_delete_retention_days", value=soft_delete_retention_days, expected_type=type_hints["soft_delete_retention_days"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
            "tenant_id": tenant_id,
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
        if access_policy is not None:
            self._values["access_policy"] = access_policy
        if contact is not None:
            self._values["contact"] = contact
        if enabled_for_deployment is not None:
            self._values["enabled_for_deployment"] = enabled_for_deployment
        if enabled_for_disk_encryption is not None:
            self._values["enabled_for_disk_encryption"] = enabled_for_disk_encryption
        if enabled_for_template_deployment is not None:
            self._values["enabled_for_template_deployment"] = enabled_for_template_deployment
        if enable_rbac_authorization is not None:
            self._values["enable_rbac_authorization"] = enable_rbac_authorization
        if id is not None:
            self._values["id"] = id
        if network_acls is not None:
            self._values["network_acls"] = network_acls
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if purge_protection_enabled is not None:
            self._values["purge_protection_enabled"] = purge_protection_enabled
        if soft_delete_retention_days is not None:
            self._values["soft_delete_retention_days"] = soft_delete_retention_days
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#location KeyVault#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#name KeyVault#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#resource_group_name KeyVault#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#sku_name KeyVault#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#tenant_id KeyVault#tenant_id}.'''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultAccessPolicy]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#access_policy KeyVault#access_policy}.'''
        result = self._values.get("access_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultAccessPolicy]]], result)

    @builtins.property
    def contact(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyVaultContact"]]]:
        '''contact block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#contact KeyVault#contact}
        '''
        result = self._values.get("contact")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyVaultContact"]]], result)

    @builtins.property
    def enabled_for_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_deployment KeyVault#enabled_for_deployment}.'''
        result = self._values.get("enabled_for_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enabled_for_disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_disk_encryption KeyVault#enabled_for_disk_encryption}.'''
        result = self._values.get("enabled_for_disk_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enabled_for_template_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enabled_for_template_deployment KeyVault#enabled_for_template_deployment}.'''
        result = self._values.get("enabled_for_template_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_rbac_authorization(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#enable_rbac_authorization KeyVault#enable_rbac_authorization}.'''
        result = self._values.get("enable_rbac_authorization")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#id KeyVault#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_acls(self) -> typing.Optional["KeyVaultNetworkAcls"]:
        '''network_acls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#network_acls KeyVault#network_acls}
        '''
        result = self._values.get("network_acls")
        return typing.cast(typing.Optional["KeyVaultNetworkAcls"], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#public_network_access_enabled KeyVault#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def purge_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#purge_protection_enabled KeyVault#purge_protection_enabled}.'''
        result = self._values.get("purge_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def soft_delete_retention_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#soft_delete_retention_days KeyVault#soft_delete_retention_days}.'''
        result = self._values.get("soft_delete_retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#tags KeyVault#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KeyVaultTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#timeouts KeyVault#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KeyVaultTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultContact",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "name": "name", "phone": "phone"},
)
class KeyVaultContact:
    def __init__(
        self,
        *,
        email: builtins.str,
        name: typing.Optional[builtins.str] = None,
        phone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#email KeyVault#email}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#name KeyVault#name}.
        :param phone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#phone KeyVault#phone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultContact.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
        self._values: typing.Dict[str, typing.Any] = {
            "email": email,
        }
        if name is not None:
            self._values["name"] = name
        if phone is not None:
            self._values["phone"] = phone

    @builtins.property
    def email(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#email KeyVault#email}.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#name KeyVault#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#phone KeyVault#phone}.'''
        result = self._values.get("phone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultContactList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultContactList",
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
            type_hints = typing.get_type_hints(KeyVaultContactList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KeyVaultContactOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultContactList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyVaultContactOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultContactList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(KeyVaultContactList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(KeyVaultContactList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultContact]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultContact]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyVaultContact]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultContactList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyVaultContactOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultContactOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultContactOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPhone")
    def reset_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhone", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneInput")
    def phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultContactOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultContactOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultContactOutputReference, "phone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyVaultContact, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyVaultContact, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyVaultContact, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultContactOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultNetworkAcls",
    jsii_struct_bases=[],
    name_mapping={
        "bypass": "bypass",
        "default_action": "defaultAction",
        "ip_rules": "ipRules",
        "virtual_network_subnet_ids": "virtualNetworkSubnetIds",
    },
)
class KeyVaultNetworkAcls:
    def __init__(
        self,
        *,
        bypass: builtins.str,
        default_action: builtins.str,
        ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#bypass KeyVault#bypass}.
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#default_action KeyVault#default_action}.
        :param ip_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#ip_rules KeyVault#ip_rules}.
        :param virtual_network_subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#virtual_network_subnet_ids KeyVault#virtual_network_subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultNetworkAcls.__init__)
            check_type(argname="argument bypass", value=bypass, expected_type=type_hints["bypass"])
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument ip_rules", value=ip_rules, expected_type=type_hints["ip_rules"])
            check_type(argname="argument virtual_network_subnet_ids", value=virtual_network_subnet_ids, expected_type=type_hints["virtual_network_subnet_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "bypass": bypass,
            "default_action": default_action,
        }
        if ip_rules is not None:
            self._values["ip_rules"] = ip_rules
        if virtual_network_subnet_ids is not None:
            self._values["virtual_network_subnet_ids"] = virtual_network_subnet_ids

    @builtins.property
    def bypass(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#bypass KeyVault#bypass}.'''
        result = self._values.get("bypass")
        assert result is not None, "Required property 'bypass' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#default_action KeyVault#default_action}.'''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_rules(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#ip_rules KeyVault#ip_rules}.'''
        result = self._values.get("ip_rules")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def virtual_network_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#virtual_network_subnet_ids KeyVault#virtual_network_subnet_ids}.'''
        result = self._values.get("virtual_network_subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultNetworkAcls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultNetworkAclsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultNetworkAclsOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultNetworkAclsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIpRules")
    def reset_ip_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRules", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetIds")
    def reset_virtual_network_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetIds", []))

    @builtins.property
    @jsii.member(jsii_name="bypassInput")
    def bypass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bypassInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRulesInput")
    def ip_rules_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdsInput")
    def virtual_network_subnet_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "virtualNetworkSubnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bypass")
    def bypass(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bypass"))

    @bypass.setter
    def bypass(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultNetworkAclsOutputReference, "bypass").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypass", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultNetworkAclsOutputReference, "default_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="ipRules")
    def ip_rules(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipRules"))

    @ip_rules.setter
    def ip_rules(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultNetworkAclsOutputReference, "ip_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRules", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIds")
    def virtual_network_subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "virtualNetworkSubnetIds"))

    @virtual_network_subnet_ids.setter
    def virtual_network_subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultNetworkAclsOutputReference, "virtual_network_subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyVaultNetworkAcls]:
        return typing.cast(typing.Optional[KeyVaultNetworkAcls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KeyVaultNetworkAcls]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultNetworkAclsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class KeyVaultTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#create KeyVault#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#delete KeyVault#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#read KeyVault#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#update KeyVault#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KeyVaultTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#create KeyVault#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#delete KeyVault#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#read KeyVault#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/key_vault#update KeyVault#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.keyVault.KeyVaultTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(KeyVaultTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(KeyVaultTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyVaultTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyVaultTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyVaultTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KeyVaultTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KeyVault",
    "KeyVaultAccessPolicy",
    "KeyVaultAccessPolicyList",
    "KeyVaultAccessPolicyOutputReference",
    "KeyVaultConfig",
    "KeyVaultContact",
    "KeyVaultContactList",
    "KeyVaultContactOutputReference",
    "KeyVaultNetworkAcls",
    "KeyVaultNetworkAclsOutputReference",
    "KeyVaultTimeouts",
    "KeyVaultTimeoutsOutputReference",
]

publication.publish()
