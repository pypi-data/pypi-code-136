'''
# `azurerm_machine_learning_workspace`

Refer to the Terraform Registory for docs: [`azurerm_machine_learning_workspace`](https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace).
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


class MachineLearningWorkspace(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningWorkspace.MachineLearningWorkspace",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace azurerm_machine_learning_workspace}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        application_insights_id: builtins.str,
        identity: typing.Union["MachineLearningWorkspaceIdentity", typing.Dict[str, typing.Any]],
        key_vault_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        storage_account_id: builtins.str,
        container_registry_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union["MachineLearningWorkspaceEncryption", typing.Dict[str, typing.Any]]] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        high_business_impact: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        image_build_compute_name: typing.Optional[builtins.str] = None,
        primary_user_assigned_identity: typing.Optional[builtins.str] = None,
        public_access_behind_virtual_network_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sku_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MachineLearningWorkspaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        v1_legacy_mode_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace azurerm_machine_learning_workspace} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param application_insights_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#application_insights_id MachineLearningWorkspace#application_insights_id}.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#identity MachineLearningWorkspace#identity}
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_vault_id MachineLearningWorkspace#key_vault_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#location MachineLearningWorkspace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#name MachineLearningWorkspace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#resource_group_name MachineLearningWorkspace#resource_group_name}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#storage_account_id MachineLearningWorkspace#storage_account_id}.
        :param container_registry_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#container_registry_id MachineLearningWorkspace#container_registry_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#description MachineLearningWorkspace#description}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#encryption MachineLearningWorkspace#encryption}
        :param friendly_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#friendly_name MachineLearningWorkspace#friendly_name}.
        :param high_business_impact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#high_business_impact MachineLearningWorkspace#high_business_impact}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#id MachineLearningWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_build_compute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#image_build_compute_name MachineLearningWorkspace#image_build_compute_name}.
        :param primary_user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#primary_user_assigned_identity MachineLearningWorkspace#primary_user_assigned_identity}.
        :param public_access_behind_virtual_network_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#public_access_behind_virtual_network_enabled MachineLearningWorkspace#public_access_behind_virtual_network_enabled}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#public_network_access_enabled MachineLearningWorkspace#public_network_access_enabled}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#sku_name MachineLearningWorkspace#sku_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#tags MachineLearningWorkspace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#timeouts MachineLearningWorkspace#timeouts}
        :param v1_legacy_mode_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#v1_legacy_mode_enabled MachineLearningWorkspace#v1_legacy_mode_enabled}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningWorkspace.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MachineLearningWorkspaceConfig(
            application_insights_id=application_insights_id,
            identity=identity,
            key_vault_id=key_vault_id,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            storage_account_id=storage_account_id,
            container_registry_id=container_registry_id,
            description=description,
            encryption=encryption,
            friendly_name=friendly_name,
            high_business_impact=high_business_impact,
            id=id,
            image_build_compute_name=image_build_compute_name,
            primary_user_assigned_identity=primary_user_assigned_identity,
            public_access_behind_virtual_network_enabled=public_access_behind_virtual_network_enabled,
            public_network_access_enabled=public_network_access_enabled,
            sku_name=sku_name,
            tags=tags,
            timeouts=timeouts,
            v1_legacy_mode_enabled=v1_legacy_mode_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEncryption")
    def put_encryption(
        self,
        *,
        key_id: builtins.str,
        key_vault_id: builtins.str,
        user_assigned_identity_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_id MachineLearningWorkspace#key_id}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_vault_id MachineLearningWorkspace#key_vault_id}.
        :param user_assigned_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#user_assigned_identity_id MachineLearningWorkspace#user_assigned_identity_id}.
        '''
        value = MachineLearningWorkspaceEncryption(
            key_id=key_id,
            key_vault_id=key_vault_id,
            user_assigned_identity_id=user_assigned_identity_id,
        )

        return typing.cast(None, jsii.invoke(self, "putEncryption", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#type MachineLearningWorkspace#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#identity_ids MachineLearningWorkspace#identity_ids}.
        '''
        value = MachineLearningWorkspaceIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#create MachineLearningWorkspace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#delete MachineLearningWorkspace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#read MachineLearningWorkspace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#update MachineLearningWorkspace#update}.
        '''
        value = MachineLearningWorkspaceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetContainerRegistryId")
    def reset_container_registry_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerRegistryId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetFriendlyName")
    def reset_friendly_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFriendlyName", []))

    @jsii.member(jsii_name="resetHighBusinessImpact")
    def reset_high_business_impact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHighBusinessImpact", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageBuildComputeName")
    def reset_image_build_compute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageBuildComputeName", []))

    @jsii.member(jsii_name="resetPrimaryUserAssignedIdentity")
    def reset_primary_user_assigned_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryUserAssignedIdentity", []))

    @jsii.member(jsii_name="resetPublicAccessBehindVirtualNetworkEnabled")
    def reset_public_access_behind_virtual_network_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicAccessBehindVirtualNetworkEnabled", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetSkuName")
    def reset_sku_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkuName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetV1LegacyModeEnabled")
    def reset_v1_legacy_mode_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetV1LegacyModeEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="discoveryUrl")
    def discovery_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "discoveryUrl"))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> "MachineLearningWorkspaceEncryptionOutputReference":
        return typing.cast("MachineLearningWorkspaceEncryptionOutputReference", jsii.get(self, "encryption"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "MachineLearningWorkspaceIdentityOutputReference":
        return typing.cast("MachineLearningWorkspaceIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MachineLearningWorkspaceTimeoutsOutputReference":
        return typing.cast("MachineLearningWorkspaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="applicationInsightsIdInput")
    def application_insights_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationInsightsIdInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryIdInput")
    def container_registry_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(self) -> typing.Optional["MachineLearningWorkspaceEncryption"]:
        return typing.cast(typing.Optional["MachineLearningWorkspaceEncryption"], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="friendlyNameInput")
    def friendly_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "friendlyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="highBusinessImpactInput")
    def high_business_impact_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "highBusinessImpactInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["MachineLearningWorkspaceIdentity"]:
        return typing.cast(typing.Optional["MachineLearningWorkspaceIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageBuildComputeNameInput")
    def image_build_compute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageBuildComputeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryUserAssignedIdentityInput")
    def primary_user_assigned_identity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryUserAssignedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="publicAccessBehindVirtualNetworkEnabledInput")
    def public_access_behind_virtual_network_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicAccessBehindVirtualNetworkEnabledInput"))

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
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MachineLearningWorkspaceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MachineLearningWorkspaceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="v1LegacyModeEnabledInput")
    def v1_legacy_mode_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "v1LegacyModeEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationInsightsId")
    def application_insights_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationInsightsId"))

    @application_insights_id.setter
    def application_insights_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "application_insights_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationInsightsId", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryId")
    def container_registry_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerRegistryId"))

    @container_registry_id.setter
    def container_registry_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "container_registry_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="friendlyName")
    def friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "friendlyName"))

    @friendly_name.setter
    def friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "friendly_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "friendlyName", value)

    @builtins.property
    @jsii.member(jsii_name="highBusinessImpact")
    def high_business_impact(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "highBusinessImpact"))

    @high_business_impact.setter
    def high_business_impact(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "high_business_impact").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "highBusinessImpact", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageBuildComputeName")
    def image_build_compute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageBuildComputeName"))

    @image_build_compute_name.setter
    def image_build_compute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "image_build_compute_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageBuildComputeName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primaryUserAssignedIdentity")
    def primary_user_assigned_identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryUserAssignedIdentity"))

    @primary_user_assigned_identity.setter
    def primary_user_assigned_identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "primary_user_assigned_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryUserAssignedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="publicAccessBehindVirtualNetworkEnabled")
    def public_access_behind_virtual_network_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicAccessBehindVirtualNetworkEnabled"))

    @public_access_behind_virtual_network_enabled.setter
    def public_access_behind_virtual_network_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "public_access_behind_virtual_network_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicAccessBehindVirtualNetworkEnabled", value)

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
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="v1LegacyModeEnabled")
    def v1_legacy_mode_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "v1LegacyModeEnabled"))

    @v1_legacy_mode_enabled.setter
    def v1_legacy_mode_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspace, "v1_legacy_mode_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "v1LegacyModeEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningWorkspace.MachineLearningWorkspaceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "application_insights_id": "applicationInsightsId",
        "identity": "identity",
        "key_vault_id": "keyVaultId",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "storage_account_id": "storageAccountId",
        "container_registry_id": "containerRegistryId",
        "description": "description",
        "encryption": "encryption",
        "friendly_name": "friendlyName",
        "high_business_impact": "highBusinessImpact",
        "id": "id",
        "image_build_compute_name": "imageBuildComputeName",
        "primary_user_assigned_identity": "primaryUserAssignedIdentity",
        "public_access_behind_virtual_network_enabled": "publicAccessBehindVirtualNetworkEnabled",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "sku_name": "skuName",
        "tags": "tags",
        "timeouts": "timeouts",
        "v1_legacy_mode_enabled": "v1LegacyModeEnabled",
    },
)
class MachineLearningWorkspaceConfig(cdktf.TerraformMetaArguments):
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
        application_insights_id: builtins.str,
        identity: typing.Union["MachineLearningWorkspaceIdentity", typing.Dict[str, typing.Any]],
        key_vault_id: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        storage_account_id: builtins.str,
        container_registry_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union["MachineLearningWorkspaceEncryption", typing.Dict[str, typing.Any]]] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        high_business_impact: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        image_build_compute_name: typing.Optional[builtins.str] = None,
        primary_user_assigned_identity: typing.Optional[builtins.str] = None,
        public_access_behind_virtual_network_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sku_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MachineLearningWorkspaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        v1_legacy_mode_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param application_insights_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#application_insights_id MachineLearningWorkspace#application_insights_id}.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#identity MachineLearningWorkspace#identity}
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_vault_id MachineLearningWorkspace#key_vault_id}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#location MachineLearningWorkspace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#name MachineLearningWorkspace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#resource_group_name MachineLearningWorkspace#resource_group_name}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#storage_account_id MachineLearningWorkspace#storage_account_id}.
        :param container_registry_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#container_registry_id MachineLearningWorkspace#container_registry_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#description MachineLearningWorkspace#description}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#encryption MachineLearningWorkspace#encryption}
        :param friendly_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#friendly_name MachineLearningWorkspace#friendly_name}.
        :param high_business_impact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#high_business_impact MachineLearningWorkspace#high_business_impact}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#id MachineLearningWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_build_compute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#image_build_compute_name MachineLearningWorkspace#image_build_compute_name}.
        :param primary_user_assigned_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#primary_user_assigned_identity MachineLearningWorkspace#primary_user_assigned_identity}.
        :param public_access_behind_virtual_network_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#public_access_behind_virtual_network_enabled MachineLearningWorkspace#public_access_behind_virtual_network_enabled}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#public_network_access_enabled MachineLearningWorkspace#public_network_access_enabled}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#sku_name MachineLearningWorkspace#sku_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#tags MachineLearningWorkspace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#timeouts MachineLearningWorkspace#timeouts}
        :param v1_legacy_mode_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#v1_legacy_mode_enabled MachineLearningWorkspace#v1_legacy_mode_enabled}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = MachineLearningWorkspaceIdentity(**identity)
        if isinstance(encryption, dict):
            encryption = MachineLearningWorkspaceEncryption(**encryption)
        if isinstance(timeouts, dict):
            timeouts = MachineLearningWorkspaceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningWorkspaceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument application_insights_id", value=application_insights_id, expected_type=type_hints["application_insights_id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument container_registry_id", value=container_registry_id, expected_type=type_hints["container_registry_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument high_business_impact", value=high_business_impact, expected_type=type_hints["high_business_impact"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_build_compute_name", value=image_build_compute_name, expected_type=type_hints["image_build_compute_name"])
            check_type(argname="argument primary_user_assigned_identity", value=primary_user_assigned_identity, expected_type=type_hints["primary_user_assigned_identity"])
            check_type(argname="argument public_access_behind_virtual_network_enabled", value=public_access_behind_virtual_network_enabled, expected_type=type_hints["public_access_behind_virtual_network_enabled"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument v1_legacy_mode_enabled", value=v1_legacy_mode_enabled, expected_type=type_hints["v1_legacy_mode_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_insights_id": application_insights_id,
            "identity": identity,
            "key_vault_id": key_vault_id,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "storage_account_id": storage_account_id,
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
        if container_registry_id is not None:
            self._values["container_registry_id"] = container_registry_id
        if description is not None:
            self._values["description"] = description
        if encryption is not None:
            self._values["encryption"] = encryption
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if high_business_impact is not None:
            self._values["high_business_impact"] = high_business_impact
        if id is not None:
            self._values["id"] = id
        if image_build_compute_name is not None:
            self._values["image_build_compute_name"] = image_build_compute_name
        if primary_user_assigned_identity is not None:
            self._values["primary_user_assigned_identity"] = primary_user_assigned_identity
        if public_access_behind_virtual_network_enabled is not None:
            self._values["public_access_behind_virtual_network_enabled"] = public_access_behind_virtual_network_enabled
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if sku_name is not None:
            self._values["sku_name"] = sku_name
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if v1_legacy_mode_enabled is not None:
            self._values["v1_legacy_mode_enabled"] = v1_legacy_mode_enabled

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
    def application_insights_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#application_insights_id MachineLearningWorkspace#application_insights_id}.'''
        result = self._values.get("application_insights_id")
        assert result is not None, "Required property 'application_insights_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity(self) -> "MachineLearningWorkspaceIdentity":
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#identity MachineLearningWorkspace#identity}
        '''
        result = self._values.get("identity")
        assert result is not None, "Required property 'identity' is missing"
        return typing.cast("MachineLearningWorkspaceIdentity", result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_vault_id MachineLearningWorkspace#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#location MachineLearningWorkspace#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#name MachineLearningWorkspace#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#resource_group_name MachineLearningWorkspace#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#storage_account_id MachineLearningWorkspace#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        assert result is not None, "Required property 'storage_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_registry_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#container_registry_id MachineLearningWorkspace#container_registry_id}.'''
        result = self._values.get("container_registry_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#description MachineLearningWorkspace#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(self) -> typing.Optional["MachineLearningWorkspaceEncryption"]:
        '''encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#encryption MachineLearningWorkspace#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["MachineLearningWorkspaceEncryption"], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#friendly_name MachineLearningWorkspace#friendly_name}.'''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def high_business_impact(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#high_business_impact MachineLearningWorkspace#high_business_impact}.'''
        result = self._values.get("high_business_impact")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#id MachineLearningWorkspace#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_build_compute_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#image_build_compute_name MachineLearningWorkspace#image_build_compute_name}.'''
        result = self._values.get("image_build_compute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_user_assigned_identity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#primary_user_assigned_identity MachineLearningWorkspace#primary_user_assigned_identity}.'''
        result = self._values.get("primary_user_assigned_identity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_access_behind_virtual_network_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#public_access_behind_virtual_network_enabled MachineLearningWorkspace#public_access_behind_virtual_network_enabled}.'''
        result = self._values.get("public_access_behind_virtual_network_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#public_network_access_enabled MachineLearningWorkspace#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sku_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#sku_name MachineLearningWorkspace#sku_name}.'''
        result = self._values.get("sku_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#tags MachineLearningWorkspace#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MachineLearningWorkspaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#timeouts MachineLearningWorkspace#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MachineLearningWorkspaceTimeouts"], result)

    @builtins.property
    def v1_legacy_mode_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#v1_legacy_mode_enabled MachineLearningWorkspace#v1_legacy_mode_enabled}.'''
        result = self._values.get("v1_legacy_mode_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningWorkspaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningWorkspace.MachineLearningWorkspaceEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "key_id": "keyId",
        "key_vault_id": "keyVaultId",
        "user_assigned_identity_id": "userAssignedIdentityId",
    },
)
class MachineLearningWorkspaceEncryption:
    def __init__(
        self,
        *,
        key_id: builtins.str,
        key_vault_id: builtins.str,
        user_assigned_identity_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_id MachineLearningWorkspace#key_id}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_vault_id MachineLearningWorkspace#key_vault_id}.
        :param user_assigned_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#user_assigned_identity_id MachineLearningWorkspace#user_assigned_identity_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningWorkspaceEncryption.__init__)
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument user_assigned_identity_id", value=user_assigned_identity_id, expected_type=type_hints["user_assigned_identity_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_id": key_id,
            "key_vault_id": key_vault_id,
        }
        if user_assigned_identity_id is not None:
            self._values["user_assigned_identity_id"] = user_assigned_identity_id

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_id MachineLearningWorkspace#key_id}.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#key_vault_id MachineLearningWorkspace#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_assigned_identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#user_assigned_identity_id MachineLearningWorkspace#user_assigned_identity_id}.'''
        result = self._values.get("user_assigned_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningWorkspaceEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningWorkspaceEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningWorkspace.MachineLearningWorkspaceEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(MachineLearningWorkspaceEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUserAssignedIdentityId")
    def reset_user_assigned_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAssignedIdentityId", []))

    @builtins.property
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityIdInput")
    def user_assigned_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAssignedIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceEncryptionOutputReference, "key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceEncryptionOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @user_assigned_identity_id.setter
    def user_assigned_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceEncryptionOutputReference, "user_assigned_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MachineLearningWorkspaceEncryption]:
        return typing.cast(typing.Optional[MachineLearningWorkspaceEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MachineLearningWorkspaceEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningWorkspace.MachineLearningWorkspaceIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class MachineLearningWorkspaceIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#type MachineLearningWorkspace#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#identity_ids MachineLearningWorkspace#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningWorkspaceIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#type MachineLearningWorkspace#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#identity_ids MachineLearningWorkspace#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningWorkspaceIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningWorkspaceIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningWorkspace.MachineLearningWorkspaceIdentityOutputReference",
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
            type_hints = typing.get_type_hints(MachineLearningWorkspaceIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MachineLearningWorkspaceIdentity]:
        return typing.cast(typing.Optional[MachineLearningWorkspaceIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MachineLearningWorkspaceIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.machineLearningWorkspace.MachineLearningWorkspaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MachineLearningWorkspaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#create MachineLearningWorkspace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#delete MachineLearningWorkspace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#read MachineLearningWorkspace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#update MachineLearningWorkspace#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MachineLearningWorkspaceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#create MachineLearningWorkspace#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#delete MachineLearningWorkspace#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#read MachineLearningWorkspace#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/machine_learning_workspace#update MachineLearningWorkspace#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningWorkspaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningWorkspaceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.machineLearningWorkspace.MachineLearningWorkspaceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MachineLearningWorkspaceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MachineLearningWorkspaceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MachineLearningWorkspaceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MachineLearningWorkspaceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MachineLearningWorkspaceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MachineLearningWorkspace",
    "MachineLearningWorkspaceConfig",
    "MachineLearningWorkspaceEncryption",
    "MachineLearningWorkspaceEncryptionOutputReference",
    "MachineLearningWorkspaceIdentity",
    "MachineLearningWorkspaceIdentityOutputReference",
    "MachineLearningWorkspaceTimeouts",
    "MachineLearningWorkspaceTimeoutsOutputReference",
]

publication.publish()
