'''
# `azurerm_synapse_workspace`

Refer to the Terraform Registory for docs: [`azurerm_synapse_workspace`](https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace).
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


class SynapseWorkspace(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspace",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace azurerm_synapse_workspace}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        identity: typing.Union["SynapseWorkspaceIdentity", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sql_administrator_login: builtins.str,
        sql_administrator_login_password: builtins.str,
        storage_data_lake_gen2_filesystem_id: builtins.str,
        aad_admin: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SynapseWorkspaceAadAdmin", typing.Dict[str, typing.Any]]]]] = None,
        azure_devops_repo: typing.Optional[typing.Union["SynapseWorkspaceAzureDevopsRepo", typing.Dict[str, typing.Any]]] = None,
        compute_subnet_id: typing.Optional[builtins.str] = None,
        customer_managed_key: typing.Optional[typing.Union["SynapseWorkspaceCustomerManagedKey", typing.Dict[str, typing.Any]]] = None,
        data_exfiltration_protection_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        github_repo: typing.Optional[typing.Union["SynapseWorkspaceGithubRepo", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        linking_allowed_for_aad_tenant_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        managed_resource_group_name: typing.Optional[builtins.str] = None,
        managed_virtual_network_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        purview_id: typing.Optional[builtins.str] = None,
        sql_aad_admin: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SynapseWorkspaceSqlAadAdmin", typing.Dict[str, typing.Any]]]]] = None,
        sql_identity_control_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SynapseWorkspaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace azurerm_synapse_workspace} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#identity SynapseWorkspace#identity}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#location SynapseWorkspace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#name SynapseWorkspace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#resource_group_name SynapseWorkspace#resource_group_name}.
        :param sql_administrator_login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_administrator_login SynapseWorkspace#sql_administrator_login}.
        :param sql_administrator_login_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_administrator_login_password SynapseWorkspace#sql_administrator_login_password}.
        :param storage_data_lake_gen2_filesystem_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#storage_data_lake_gen2_filesystem_id SynapseWorkspace#storage_data_lake_gen2_filesystem_id}.
        :param aad_admin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#aad_admin SynapseWorkspace#aad_admin}.
        :param azure_devops_repo: azure_devops_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#azure_devops_repo SynapseWorkspace#azure_devops_repo}
        :param compute_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#compute_subnet_id SynapseWorkspace#compute_subnet_id}.
        :param customer_managed_key: customer_managed_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#customer_managed_key SynapseWorkspace#customer_managed_key}
        :param data_exfiltration_protection_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#data_exfiltration_protection_enabled SynapseWorkspace#data_exfiltration_protection_enabled}.
        :param github_repo: github_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#github_repo SynapseWorkspace#github_repo}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#id SynapseWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param linking_allowed_for_aad_tenant_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#linking_allowed_for_aad_tenant_ids SynapseWorkspace#linking_allowed_for_aad_tenant_ids}.
        :param managed_resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#managed_resource_group_name SynapseWorkspace#managed_resource_group_name}.
        :param managed_virtual_network_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#managed_virtual_network_enabled SynapseWorkspace#managed_virtual_network_enabled}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#public_network_access_enabled SynapseWorkspace#public_network_access_enabled}.
        :param purview_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#purview_id SynapseWorkspace#purview_id}.
        :param sql_aad_admin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_aad_admin SynapseWorkspace#sql_aad_admin}.
        :param sql_identity_control_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_identity_control_enabled SynapseWorkspace#sql_identity_control_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tags SynapseWorkspace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#timeouts SynapseWorkspace#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspace.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SynapseWorkspaceConfig(
            identity=identity,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sql_administrator_login=sql_administrator_login,
            sql_administrator_login_password=sql_administrator_login_password,
            storage_data_lake_gen2_filesystem_id=storage_data_lake_gen2_filesystem_id,
            aad_admin=aad_admin,
            azure_devops_repo=azure_devops_repo,
            compute_subnet_id=compute_subnet_id,
            customer_managed_key=customer_managed_key,
            data_exfiltration_protection_enabled=data_exfiltration_protection_enabled,
            github_repo=github_repo,
            id=id,
            linking_allowed_for_aad_tenant_ids=linking_allowed_for_aad_tenant_ids,
            managed_resource_group_name=managed_resource_group_name,
            managed_virtual_network_enabled=managed_virtual_network_enabled,
            public_network_access_enabled=public_network_access_enabled,
            purview_id=purview_id,
            sql_aad_admin=sql_aad_admin,
            sql_identity_control_enabled=sql_identity_control_enabled,
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

    @jsii.member(jsii_name="putAadAdmin")
    def put_aad_admin(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SynapseWorkspaceAadAdmin", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspace.put_aad_admin)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAadAdmin", [value]))

    @jsii.member(jsii_name="putAzureDevopsRepo")
    def put_azure_devops_repo(
        self,
        *,
        account_name: builtins.str,
        branch_name: builtins.str,
        project_name: builtins.str,
        repository_name: builtins.str,
        root_folder: builtins.str,
        last_commit_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#account_name SynapseWorkspace#account_name}.
        :param branch_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#branch_name SynapseWorkspace#branch_name}.
        :param project_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#project_name SynapseWorkspace#project_name}.
        :param repository_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#repository_name SynapseWorkspace#repository_name}.
        :param root_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#root_folder SynapseWorkspace#root_folder}.
        :param last_commit_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#last_commit_id SynapseWorkspace#last_commit_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tenant_id SynapseWorkspace#tenant_id}.
        '''
        value = SynapseWorkspaceAzureDevopsRepo(
            account_name=account_name,
            branch_name=branch_name,
            project_name=project_name,
            repository_name=repository_name,
            root_folder=root_folder,
            last_commit_id=last_commit_id,
            tenant_id=tenant_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureDevopsRepo", [value]))

    @jsii.member(jsii_name="putCustomerManagedKey")
    def put_customer_managed_key(
        self,
        *,
        key_versionless_id: builtins.str,
        key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_versionless_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#key_versionless_id SynapseWorkspace#key_versionless_id}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#key_name SynapseWorkspace#key_name}.
        '''
        value = SynapseWorkspaceCustomerManagedKey(
            key_versionless_id=key_versionless_id, key_name=key_name
        )

        return typing.cast(None, jsii.invoke(self, "putCustomerManagedKey", [value]))

    @jsii.member(jsii_name="putGithubRepo")
    def put_github_repo(
        self,
        *,
        account_name: builtins.str,
        branch_name: builtins.str,
        repository_name: builtins.str,
        root_folder: builtins.str,
        git_url: typing.Optional[builtins.str] = None,
        last_commit_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#account_name SynapseWorkspace#account_name}.
        :param branch_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#branch_name SynapseWorkspace#branch_name}.
        :param repository_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#repository_name SynapseWorkspace#repository_name}.
        :param root_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#root_folder SynapseWorkspace#root_folder}.
        :param git_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#git_url SynapseWorkspace#git_url}.
        :param last_commit_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#last_commit_id SynapseWorkspace#last_commit_id}.
        '''
        value = SynapseWorkspaceGithubRepo(
            account_name=account_name,
            branch_name=branch_name,
            repository_name=repository_name,
            root_folder=root_folder,
            git_url=git_url,
            last_commit_id=last_commit_id,
        )

        return typing.cast(None, jsii.invoke(self, "putGithubRepo", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#type SynapseWorkspace#type}.
        '''
        value = SynapseWorkspaceIdentity(type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putSqlAadAdmin")
    def put_sql_aad_admin(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SynapseWorkspaceSqlAadAdmin", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspace.put_sql_aad_admin)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSqlAadAdmin", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#create SynapseWorkspace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#delete SynapseWorkspace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#read SynapseWorkspace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#update SynapseWorkspace#update}.
        '''
        value = SynapseWorkspaceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAadAdmin")
    def reset_aad_admin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAadAdmin", []))

    @jsii.member(jsii_name="resetAzureDevopsRepo")
    def reset_azure_devops_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureDevopsRepo", []))

    @jsii.member(jsii_name="resetComputeSubnetId")
    def reset_compute_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputeSubnetId", []))

    @jsii.member(jsii_name="resetCustomerManagedKey")
    def reset_customer_managed_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedKey", []))

    @jsii.member(jsii_name="resetDataExfiltrationProtectionEnabled")
    def reset_data_exfiltration_protection_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataExfiltrationProtectionEnabled", []))

    @jsii.member(jsii_name="resetGithubRepo")
    def reset_github_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithubRepo", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLinkingAllowedForAadTenantIds")
    def reset_linking_allowed_for_aad_tenant_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkingAllowedForAadTenantIds", []))

    @jsii.member(jsii_name="resetManagedResourceGroupName")
    def reset_managed_resource_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedResourceGroupName", []))

    @jsii.member(jsii_name="resetManagedVirtualNetworkEnabled")
    def reset_managed_virtual_network_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedVirtualNetworkEnabled", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetPurviewId")
    def reset_purview_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurviewId", []))

    @jsii.member(jsii_name="resetSqlAadAdmin")
    def reset_sql_aad_admin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlAadAdmin", []))

    @jsii.member(jsii_name="resetSqlIdentityControlEnabled")
    def reset_sql_identity_control_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlIdentityControlEnabled", []))

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
    @jsii.member(jsii_name="aadAdmin")
    def aad_admin(self) -> "SynapseWorkspaceAadAdminList":
        return typing.cast("SynapseWorkspaceAadAdminList", jsii.get(self, "aadAdmin"))

    @builtins.property
    @jsii.member(jsii_name="azureDevopsRepo")
    def azure_devops_repo(self) -> "SynapseWorkspaceAzureDevopsRepoOutputReference":
        return typing.cast("SynapseWorkspaceAzureDevopsRepoOutputReference", jsii.get(self, "azureDevopsRepo"))

    @builtins.property
    @jsii.member(jsii_name="connectivityEndpoints")
    def connectivity_endpoints(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "connectivityEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKey")
    def customer_managed_key(
        self,
    ) -> "SynapseWorkspaceCustomerManagedKeyOutputReference":
        return typing.cast("SynapseWorkspaceCustomerManagedKeyOutputReference", jsii.get(self, "customerManagedKey"))

    @builtins.property
    @jsii.member(jsii_name="githubRepo")
    def github_repo(self) -> "SynapseWorkspaceGithubRepoOutputReference":
        return typing.cast("SynapseWorkspaceGithubRepoOutputReference", jsii.get(self, "githubRepo"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "SynapseWorkspaceIdentityOutputReference":
        return typing.cast("SynapseWorkspaceIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="sqlAadAdmin")
    def sql_aad_admin(self) -> "SynapseWorkspaceSqlAadAdminList":
        return typing.cast("SynapseWorkspaceSqlAadAdminList", jsii.get(self, "sqlAadAdmin"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SynapseWorkspaceTimeoutsOutputReference":
        return typing.cast("SynapseWorkspaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="aadAdminInput")
    def aad_admin_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SynapseWorkspaceAadAdmin"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SynapseWorkspaceAadAdmin"]]], jsii.get(self, "aadAdminInput"))

    @builtins.property
    @jsii.member(jsii_name="azureDevopsRepoInput")
    def azure_devops_repo_input(
        self,
    ) -> typing.Optional["SynapseWorkspaceAzureDevopsRepo"]:
        return typing.cast(typing.Optional["SynapseWorkspaceAzureDevopsRepo"], jsii.get(self, "azureDevopsRepoInput"))

    @builtins.property
    @jsii.member(jsii_name="computeSubnetIdInput")
    def compute_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyInput")
    def customer_managed_key_input(
        self,
    ) -> typing.Optional["SynapseWorkspaceCustomerManagedKey"]:
        return typing.cast(typing.Optional["SynapseWorkspaceCustomerManagedKey"], jsii.get(self, "customerManagedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="dataExfiltrationProtectionEnabledInput")
    def data_exfiltration_protection_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dataExfiltrationProtectionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="githubRepoInput")
    def github_repo_input(self) -> typing.Optional["SynapseWorkspaceGithubRepo"]:
        return typing.cast(typing.Optional["SynapseWorkspaceGithubRepo"], jsii.get(self, "githubRepoInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["SynapseWorkspaceIdentity"]:
        return typing.cast(typing.Optional["SynapseWorkspaceIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="linkingAllowedForAadTenantIdsInput")
    def linking_allowed_for_aad_tenant_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "linkingAllowedForAadTenantIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managedResourceGroupNameInput")
    def managed_resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedResourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="managedVirtualNetworkEnabledInput")
    def managed_virtual_network_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "managedVirtualNetworkEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="purviewIdInput")
    def purview_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "purviewIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlAadAdminInput")
    def sql_aad_admin_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SynapseWorkspaceSqlAadAdmin"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SynapseWorkspaceSqlAadAdmin"]]], jsii.get(self, "sqlAadAdminInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlAdministratorLoginInput")
    def sql_administrator_login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlAdministratorLoginInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlAdministratorLoginPasswordInput")
    def sql_administrator_login_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlAdministratorLoginPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlIdentityControlEnabledInput")
    def sql_identity_control_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sqlIdentityControlEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="storageDataLakeGen2FilesystemIdInput")
    def storage_data_lake_gen2_filesystem_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageDataLakeGen2FilesystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SynapseWorkspaceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SynapseWorkspaceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="computeSubnetId")
    def compute_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computeSubnetId"))

    @compute_subnet_id.setter
    def compute_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "compute_subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="dataExfiltrationProtectionEnabled")
    def data_exfiltration_protection_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dataExfiltrationProtectionEnabled"))

    @data_exfiltration_protection_enabled.setter
    def data_exfiltration_protection_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "data_exfiltration_protection_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataExfiltrationProtectionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="linkingAllowedForAadTenantIds")
    def linking_allowed_for_aad_tenant_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "linkingAllowedForAadTenantIds"))

    @linking_allowed_for_aad_tenant_ids.setter
    def linking_allowed_for_aad_tenant_ids(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "linking_allowed_for_aad_tenant_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkingAllowedForAadTenantIds", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="managedResourceGroupName")
    def managed_resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedResourceGroupName"))

    @managed_resource_group_name.setter
    def managed_resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "managed_resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedResourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="managedVirtualNetworkEnabled")
    def managed_virtual_network_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "managedVirtualNetworkEnabled"))

    @managed_virtual_network_enabled.setter
    def managed_virtual_network_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "managed_virtual_network_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedVirtualNetworkEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "name").fset)
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
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="purviewId")
    def purview_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "purviewId"))

    @purview_id.setter
    def purview_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "purview_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purviewId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sqlAdministratorLogin")
    def sql_administrator_login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlAdministratorLogin"))

    @sql_administrator_login.setter
    def sql_administrator_login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "sql_administrator_login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlAdministratorLogin", value)

    @builtins.property
    @jsii.member(jsii_name="sqlAdministratorLoginPassword")
    def sql_administrator_login_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlAdministratorLoginPassword"))

    @sql_administrator_login_password.setter
    def sql_administrator_login_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "sql_administrator_login_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlAdministratorLoginPassword", value)

    @builtins.property
    @jsii.member(jsii_name="sqlIdentityControlEnabled")
    def sql_identity_control_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sqlIdentityControlEnabled"))

    @sql_identity_control_enabled.setter
    def sql_identity_control_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "sql_identity_control_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlIdentityControlEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="storageDataLakeGen2FilesystemId")
    def storage_data_lake_gen2_filesystem_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageDataLakeGen2FilesystemId"))

    @storage_data_lake_gen2_filesystem_id.setter
    def storage_data_lake_gen2_filesystem_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "storage_data_lake_gen2_filesystem_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageDataLakeGen2FilesystemId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspace, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceAadAdmin",
    jsii_struct_bases=[],
    name_mapping={"login": "login", "object_id": "objectId", "tenant_id": "tenantId"},
)
class SynapseWorkspaceAadAdmin:
    def __init__(
        self,
        *,
        login: typing.Optional[builtins.str] = None,
        object_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#login SynapseWorkspace#login}.
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#object_id SynapseWorkspace#object_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tenant_id SynapseWorkspace#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceAadAdmin.__init__)
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if login is not None:
            self._values["login"] = login
        if object_id is not None:
            self._values["object_id"] = object_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def login(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#login SynapseWorkspace#login}.'''
        result = self._values.get("login")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#object_id SynapseWorkspace#object_id}.'''
        result = self._values.get("object_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tenant_id SynapseWorkspace#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceAadAdmin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseWorkspaceAadAdminList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceAadAdminList",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceAadAdminList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SynapseWorkspaceAadAdminOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceAadAdminList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SynapseWorkspaceAadAdminOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAadAdminList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAadAdminList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAadAdminList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SynapseWorkspaceAadAdmin]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SynapseWorkspaceAadAdmin]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SynapseWorkspaceAadAdmin]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAadAdminList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SynapseWorkspaceAadAdminOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceAadAdminOutputReference",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceAadAdminOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetLogin")
    def reset_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogin", []))

    @jsii.member(jsii_name="resetObjectId")
    def reset_object_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectId", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdInput")
    def object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "login"))

    @login.setter
    def login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAadAdminOutputReference, "login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "login", value)

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @object_id.setter
    def object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAadAdminOutputReference, "object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAadAdminOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SynapseWorkspaceAadAdmin, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SynapseWorkspaceAadAdmin, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SynapseWorkspaceAadAdmin, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAadAdminOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceAzureDevopsRepo",
    jsii_struct_bases=[],
    name_mapping={
        "account_name": "accountName",
        "branch_name": "branchName",
        "project_name": "projectName",
        "repository_name": "repositoryName",
        "root_folder": "rootFolder",
        "last_commit_id": "lastCommitId",
        "tenant_id": "tenantId",
    },
)
class SynapseWorkspaceAzureDevopsRepo:
    def __init__(
        self,
        *,
        account_name: builtins.str,
        branch_name: builtins.str,
        project_name: builtins.str,
        repository_name: builtins.str,
        root_folder: builtins.str,
        last_commit_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#account_name SynapseWorkspace#account_name}.
        :param branch_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#branch_name SynapseWorkspace#branch_name}.
        :param project_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#project_name SynapseWorkspace#project_name}.
        :param repository_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#repository_name SynapseWorkspace#repository_name}.
        :param root_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#root_folder SynapseWorkspace#root_folder}.
        :param last_commit_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#last_commit_id SynapseWorkspace#last_commit_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tenant_id SynapseWorkspace#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceAzureDevopsRepo.__init__)
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument branch_name", value=branch_name, expected_type=type_hints["branch_name"])
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument root_folder", value=root_folder, expected_type=type_hints["root_folder"])
            check_type(argname="argument last_commit_id", value=last_commit_id, expected_type=type_hints["last_commit_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_name": account_name,
            "branch_name": branch_name,
            "project_name": project_name,
            "repository_name": repository_name,
            "root_folder": root_folder,
        }
        if last_commit_id is not None:
            self._values["last_commit_id"] = last_commit_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#account_name SynapseWorkspace#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#branch_name SynapseWorkspace#branch_name}.'''
        result = self._values.get("branch_name")
        assert result is not None, "Required property 'branch_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#project_name SynapseWorkspace#project_name}.'''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#repository_name SynapseWorkspace#repository_name}.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_folder(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#root_folder SynapseWorkspace#root_folder}.'''
        result = self._values.get("root_folder")
        assert result is not None, "Required property 'root_folder' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last_commit_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#last_commit_id SynapseWorkspace#last_commit_id}.'''
        result = self._values.get("last_commit_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tenant_id SynapseWorkspace#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceAzureDevopsRepo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseWorkspaceAzureDevopsRepoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceAzureDevopsRepoOutputReference",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceAzureDevopsRepoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLastCommitId")
    def reset_last_commit_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastCommitId", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="branchNameInput")
    def branch_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchNameInput"))

    @builtins.property
    @jsii.member(jsii_name="lastCommitIdInput")
    def last_commit_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastCommitIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectNameInput")
    def project_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectNameInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryNameInput")
    def repository_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootFolderInput")
    def root_folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootFolderInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAzureDevopsRepoOutputReference, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="branchName")
    def branch_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branchName"))

    @branch_name.setter
    def branch_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAzureDevopsRepoOutputReference, "branch_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branchName", value)

    @builtins.property
    @jsii.member(jsii_name="lastCommitId")
    def last_commit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastCommitId"))

    @last_commit_id.setter
    def last_commit_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAzureDevopsRepoOutputReference, "last_commit_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastCommitId", value)

    @builtins.property
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAzureDevopsRepoOutputReference, "project_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectName", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAzureDevopsRepoOutputReference, "repository_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryName", value)

    @builtins.property
    @jsii.member(jsii_name="rootFolder")
    def root_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootFolder"))

    @root_folder.setter
    def root_folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAzureDevopsRepoOutputReference, "root_folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootFolder", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAzureDevopsRepoOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SynapseWorkspaceAzureDevopsRepo]:
        return typing.cast(typing.Optional[SynapseWorkspaceAzureDevopsRepo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SynapseWorkspaceAzureDevopsRepo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceAzureDevopsRepoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "identity": "identity",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sql_administrator_login": "sqlAdministratorLogin",
        "sql_administrator_login_password": "sqlAdministratorLoginPassword",
        "storage_data_lake_gen2_filesystem_id": "storageDataLakeGen2FilesystemId",
        "aad_admin": "aadAdmin",
        "azure_devops_repo": "azureDevopsRepo",
        "compute_subnet_id": "computeSubnetId",
        "customer_managed_key": "customerManagedKey",
        "data_exfiltration_protection_enabled": "dataExfiltrationProtectionEnabled",
        "github_repo": "githubRepo",
        "id": "id",
        "linking_allowed_for_aad_tenant_ids": "linkingAllowedForAadTenantIds",
        "managed_resource_group_name": "managedResourceGroupName",
        "managed_virtual_network_enabled": "managedVirtualNetworkEnabled",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "purview_id": "purviewId",
        "sql_aad_admin": "sqlAadAdmin",
        "sql_identity_control_enabled": "sqlIdentityControlEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class SynapseWorkspaceConfig(cdktf.TerraformMetaArguments):
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
        identity: typing.Union["SynapseWorkspaceIdentity", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sql_administrator_login: builtins.str,
        sql_administrator_login_password: builtins.str,
        storage_data_lake_gen2_filesystem_id: builtins.str,
        aad_admin: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SynapseWorkspaceAadAdmin, typing.Dict[str, typing.Any]]]]] = None,
        azure_devops_repo: typing.Optional[typing.Union[SynapseWorkspaceAzureDevopsRepo, typing.Dict[str, typing.Any]]] = None,
        compute_subnet_id: typing.Optional[builtins.str] = None,
        customer_managed_key: typing.Optional[typing.Union["SynapseWorkspaceCustomerManagedKey", typing.Dict[str, typing.Any]]] = None,
        data_exfiltration_protection_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        github_repo: typing.Optional[typing.Union["SynapseWorkspaceGithubRepo", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        linking_allowed_for_aad_tenant_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        managed_resource_group_name: typing.Optional[builtins.str] = None,
        managed_virtual_network_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        purview_id: typing.Optional[builtins.str] = None,
        sql_aad_admin: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SynapseWorkspaceSqlAadAdmin", typing.Dict[str, typing.Any]]]]] = None,
        sql_identity_control_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SynapseWorkspaceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#identity SynapseWorkspace#identity}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#location SynapseWorkspace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#name SynapseWorkspace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#resource_group_name SynapseWorkspace#resource_group_name}.
        :param sql_administrator_login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_administrator_login SynapseWorkspace#sql_administrator_login}.
        :param sql_administrator_login_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_administrator_login_password SynapseWorkspace#sql_administrator_login_password}.
        :param storage_data_lake_gen2_filesystem_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#storage_data_lake_gen2_filesystem_id SynapseWorkspace#storage_data_lake_gen2_filesystem_id}.
        :param aad_admin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#aad_admin SynapseWorkspace#aad_admin}.
        :param azure_devops_repo: azure_devops_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#azure_devops_repo SynapseWorkspace#azure_devops_repo}
        :param compute_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#compute_subnet_id SynapseWorkspace#compute_subnet_id}.
        :param customer_managed_key: customer_managed_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#customer_managed_key SynapseWorkspace#customer_managed_key}
        :param data_exfiltration_protection_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#data_exfiltration_protection_enabled SynapseWorkspace#data_exfiltration_protection_enabled}.
        :param github_repo: github_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#github_repo SynapseWorkspace#github_repo}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#id SynapseWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param linking_allowed_for_aad_tenant_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#linking_allowed_for_aad_tenant_ids SynapseWorkspace#linking_allowed_for_aad_tenant_ids}.
        :param managed_resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#managed_resource_group_name SynapseWorkspace#managed_resource_group_name}.
        :param managed_virtual_network_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#managed_virtual_network_enabled SynapseWorkspace#managed_virtual_network_enabled}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#public_network_access_enabled SynapseWorkspace#public_network_access_enabled}.
        :param purview_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#purview_id SynapseWorkspace#purview_id}.
        :param sql_aad_admin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_aad_admin SynapseWorkspace#sql_aad_admin}.
        :param sql_identity_control_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_identity_control_enabled SynapseWorkspace#sql_identity_control_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tags SynapseWorkspace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#timeouts SynapseWorkspace#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity, dict):
            identity = SynapseWorkspaceIdentity(**identity)
        if isinstance(azure_devops_repo, dict):
            azure_devops_repo = SynapseWorkspaceAzureDevopsRepo(**azure_devops_repo)
        if isinstance(customer_managed_key, dict):
            customer_managed_key = SynapseWorkspaceCustomerManagedKey(**customer_managed_key)
        if isinstance(github_repo, dict):
            github_repo = SynapseWorkspaceGithubRepo(**github_repo)
        if isinstance(timeouts, dict):
            timeouts = SynapseWorkspaceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sql_administrator_login", value=sql_administrator_login, expected_type=type_hints["sql_administrator_login"])
            check_type(argname="argument sql_administrator_login_password", value=sql_administrator_login_password, expected_type=type_hints["sql_administrator_login_password"])
            check_type(argname="argument storage_data_lake_gen2_filesystem_id", value=storage_data_lake_gen2_filesystem_id, expected_type=type_hints["storage_data_lake_gen2_filesystem_id"])
            check_type(argname="argument aad_admin", value=aad_admin, expected_type=type_hints["aad_admin"])
            check_type(argname="argument azure_devops_repo", value=azure_devops_repo, expected_type=type_hints["azure_devops_repo"])
            check_type(argname="argument compute_subnet_id", value=compute_subnet_id, expected_type=type_hints["compute_subnet_id"])
            check_type(argname="argument customer_managed_key", value=customer_managed_key, expected_type=type_hints["customer_managed_key"])
            check_type(argname="argument data_exfiltration_protection_enabled", value=data_exfiltration_protection_enabled, expected_type=type_hints["data_exfiltration_protection_enabled"])
            check_type(argname="argument github_repo", value=github_repo, expected_type=type_hints["github_repo"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument linking_allowed_for_aad_tenant_ids", value=linking_allowed_for_aad_tenant_ids, expected_type=type_hints["linking_allowed_for_aad_tenant_ids"])
            check_type(argname="argument managed_resource_group_name", value=managed_resource_group_name, expected_type=type_hints["managed_resource_group_name"])
            check_type(argname="argument managed_virtual_network_enabled", value=managed_virtual_network_enabled, expected_type=type_hints["managed_virtual_network_enabled"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument purview_id", value=purview_id, expected_type=type_hints["purview_id"])
            check_type(argname="argument sql_aad_admin", value=sql_aad_admin, expected_type=type_hints["sql_aad_admin"])
            check_type(argname="argument sql_identity_control_enabled", value=sql_identity_control_enabled, expected_type=type_hints["sql_identity_control_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity": identity,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sql_administrator_login": sql_administrator_login,
            "sql_administrator_login_password": sql_administrator_login_password,
            "storage_data_lake_gen2_filesystem_id": storage_data_lake_gen2_filesystem_id,
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
        if aad_admin is not None:
            self._values["aad_admin"] = aad_admin
        if azure_devops_repo is not None:
            self._values["azure_devops_repo"] = azure_devops_repo
        if compute_subnet_id is not None:
            self._values["compute_subnet_id"] = compute_subnet_id
        if customer_managed_key is not None:
            self._values["customer_managed_key"] = customer_managed_key
        if data_exfiltration_protection_enabled is not None:
            self._values["data_exfiltration_protection_enabled"] = data_exfiltration_protection_enabled
        if github_repo is not None:
            self._values["github_repo"] = github_repo
        if id is not None:
            self._values["id"] = id
        if linking_allowed_for_aad_tenant_ids is not None:
            self._values["linking_allowed_for_aad_tenant_ids"] = linking_allowed_for_aad_tenant_ids
        if managed_resource_group_name is not None:
            self._values["managed_resource_group_name"] = managed_resource_group_name
        if managed_virtual_network_enabled is not None:
            self._values["managed_virtual_network_enabled"] = managed_virtual_network_enabled
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if purview_id is not None:
            self._values["purview_id"] = purview_id
        if sql_aad_admin is not None:
            self._values["sql_aad_admin"] = sql_aad_admin
        if sql_identity_control_enabled is not None:
            self._values["sql_identity_control_enabled"] = sql_identity_control_enabled
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
    def identity(self) -> "SynapseWorkspaceIdentity":
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#identity SynapseWorkspace#identity}
        '''
        result = self._values.get("identity")
        assert result is not None, "Required property 'identity' is missing"
        return typing.cast("SynapseWorkspaceIdentity", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#location SynapseWorkspace#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#name SynapseWorkspace#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#resource_group_name SynapseWorkspace#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_administrator_login(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_administrator_login SynapseWorkspace#sql_administrator_login}.'''
        result = self._values.get("sql_administrator_login")
        assert result is not None, "Required property 'sql_administrator_login' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_administrator_login_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_administrator_login_password SynapseWorkspace#sql_administrator_login_password}.'''
        result = self._values.get("sql_administrator_login_password")
        assert result is not None, "Required property 'sql_administrator_login_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_data_lake_gen2_filesystem_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#storage_data_lake_gen2_filesystem_id SynapseWorkspace#storage_data_lake_gen2_filesystem_id}.'''
        result = self._values.get("storage_data_lake_gen2_filesystem_id")
        assert result is not None, "Required property 'storage_data_lake_gen2_filesystem_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aad_admin(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SynapseWorkspaceAadAdmin]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#aad_admin SynapseWorkspace#aad_admin}.'''
        result = self._values.get("aad_admin")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SynapseWorkspaceAadAdmin]]], result)

    @builtins.property
    def azure_devops_repo(self) -> typing.Optional[SynapseWorkspaceAzureDevopsRepo]:
        '''azure_devops_repo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#azure_devops_repo SynapseWorkspace#azure_devops_repo}
        '''
        result = self._values.get("azure_devops_repo")
        return typing.cast(typing.Optional[SynapseWorkspaceAzureDevopsRepo], result)

    @builtins.property
    def compute_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#compute_subnet_id SynapseWorkspace#compute_subnet_id}.'''
        result = self._values.get("compute_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_managed_key(
        self,
    ) -> typing.Optional["SynapseWorkspaceCustomerManagedKey"]:
        '''customer_managed_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#customer_managed_key SynapseWorkspace#customer_managed_key}
        '''
        result = self._values.get("customer_managed_key")
        return typing.cast(typing.Optional["SynapseWorkspaceCustomerManagedKey"], result)

    @builtins.property
    def data_exfiltration_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#data_exfiltration_protection_enabled SynapseWorkspace#data_exfiltration_protection_enabled}.'''
        result = self._values.get("data_exfiltration_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def github_repo(self) -> typing.Optional["SynapseWorkspaceGithubRepo"]:
        '''github_repo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#github_repo SynapseWorkspace#github_repo}
        '''
        result = self._values.get("github_repo")
        return typing.cast(typing.Optional["SynapseWorkspaceGithubRepo"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#id SynapseWorkspace#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def linking_allowed_for_aad_tenant_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#linking_allowed_for_aad_tenant_ids SynapseWorkspace#linking_allowed_for_aad_tenant_ids}.'''
        result = self._values.get("linking_allowed_for_aad_tenant_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def managed_resource_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#managed_resource_group_name SynapseWorkspace#managed_resource_group_name}.'''
        result = self._values.get("managed_resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_virtual_network_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#managed_virtual_network_enabled SynapseWorkspace#managed_virtual_network_enabled}.'''
        result = self._values.get("managed_virtual_network_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#public_network_access_enabled SynapseWorkspace#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def purview_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#purview_id SynapseWorkspace#purview_id}.'''
        result = self._values.get("purview_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_aad_admin(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SynapseWorkspaceSqlAadAdmin"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_aad_admin SynapseWorkspace#sql_aad_admin}.'''
        result = self._values.get("sql_aad_admin")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SynapseWorkspaceSqlAadAdmin"]]], result)

    @builtins.property
    def sql_identity_control_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#sql_identity_control_enabled SynapseWorkspace#sql_identity_control_enabled}.'''
        result = self._values.get("sql_identity_control_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tags SynapseWorkspace#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SynapseWorkspaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#timeouts SynapseWorkspace#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SynapseWorkspaceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceCustomerManagedKey",
    jsii_struct_bases=[],
    name_mapping={"key_versionless_id": "keyVersionlessId", "key_name": "keyName"},
)
class SynapseWorkspaceCustomerManagedKey:
    def __init__(
        self,
        *,
        key_versionless_id: builtins.str,
        key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_versionless_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#key_versionless_id SynapseWorkspace#key_versionless_id}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#key_name SynapseWorkspace#key_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceCustomerManagedKey.__init__)
            check_type(argname="argument key_versionless_id", value=key_versionless_id, expected_type=type_hints["key_versionless_id"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_versionless_id": key_versionless_id,
        }
        if key_name is not None:
            self._values["key_name"] = key_name

    @builtins.property
    def key_versionless_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#key_versionless_id SynapseWorkspace#key_versionless_id}.'''
        result = self._values.get("key_versionless_id")
        assert result is not None, "Required property 'key_versionless_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#key_name SynapseWorkspace#key_name}.'''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceCustomerManagedKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseWorkspaceCustomerManagedKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceCustomerManagedKeyOutputReference",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceCustomerManagedKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeyName")
    def reset_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyName", []))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVersionlessIdInput")
    def key_versionless_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVersionlessIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceCustomerManagedKeyOutputReference, "key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVersionlessId")
    def key_versionless_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVersionlessId"))

    @key_versionless_id.setter
    def key_versionless_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceCustomerManagedKeyOutputReference, "key_versionless_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVersionlessId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SynapseWorkspaceCustomerManagedKey]:
        return typing.cast(typing.Optional[SynapseWorkspaceCustomerManagedKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SynapseWorkspaceCustomerManagedKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceCustomerManagedKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceGithubRepo",
    jsii_struct_bases=[],
    name_mapping={
        "account_name": "accountName",
        "branch_name": "branchName",
        "repository_name": "repositoryName",
        "root_folder": "rootFolder",
        "git_url": "gitUrl",
        "last_commit_id": "lastCommitId",
    },
)
class SynapseWorkspaceGithubRepo:
    def __init__(
        self,
        *,
        account_name: builtins.str,
        branch_name: builtins.str,
        repository_name: builtins.str,
        root_folder: builtins.str,
        git_url: typing.Optional[builtins.str] = None,
        last_commit_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#account_name SynapseWorkspace#account_name}.
        :param branch_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#branch_name SynapseWorkspace#branch_name}.
        :param repository_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#repository_name SynapseWorkspace#repository_name}.
        :param root_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#root_folder SynapseWorkspace#root_folder}.
        :param git_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#git_url SynapseWorkspace#git_url}.
        :param last_commit_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#last_commit_id SynapseWorkspace#last_commit_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceGithubRepo.__init__)
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument branch_name", value=branch_name, expected_type=type_hints["branch_name"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument root_folder", value=root_folder, expected_type=type_hints["root_folder"])
            check_type(argname="argument git_url", value=git_url, expected_type=type_hints["git_url"])
            check_type(argname="argument last_commit_id", value=last_commit_id, expected_type=type_hints["last_commit_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_name": account_name,
            "branch_name": branch_name,
            "repository_name": repository_name,
            "root_folder": root_folder,
        }
        if git_url is not None:
            self._values["git_url"] = git_url
        if last_commit_id is not None:
            self._values["last_commit_id"] = last_commit_id

    @builtins.property
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#account_name SynapseWorkspace#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#branch_name SynapseWorkspace#branch_name}.'''
        result = self._values.get("branch_name")
        assert result is not None, "Required property 'branch_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#repository_name SynapseWorkspace#repository_name}.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_folder(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#root_folder SynapseWorkspace#root_folder}.'''
        result = self._values.get("root_folder")
        assert result is not None, "Required property 'root_folder' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def git_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#git_url SynapseWorkspace#git_url}.'''
        result = self._values.get("git_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_commit_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#last_commit_id SynapseWorkspace#last_commit_id}.'''
        result = self._values.get("last_commit_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceGithubRepo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseWorkspaceGithubRepoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceGithubRepoOutputReference",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceGithubRepoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGitUrl")
    def reset_git_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitUrl", []))

    @jsii.member(jsii_name="resetLastCommitId")
    def reset_last_commit_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastCommitId", []))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="branchNameInput")
    def branch_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchNameInput"))

    @builtins.property
    @jsii.member(jsii_name="gitUrlInput")
    def git_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gitUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="lastCommitIdInput")
    def last_commit_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastCommitIdInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryNameInput")
    def repository_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rootFolderInput")
    def root_folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootFolderInput"))

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceGithubRepoOutputReference, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="branchName")
    def branch_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branchName"))

    @branch_name.setter
    def branch_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceGithubRepoOutputReference, "branch_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branchName", value)

    @builtins.property
    @jsii.member(jsii_name="gitUrl")
    def git_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gitUrl"))

    @git_url.setter
    def git_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceGithubRepoOutputReference, "git_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitUrl", value)

    @builtins.property
    @jsii.member(jsii_name="lastCommitId")
    def last_commit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastCommitId"))

    @last_commit_id.setter
    def last_commit_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceGithubRepoOutputReference, "last_commit_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastCommitId", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceGithubRepoOutputReference, "repository_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryName", value)

    @builtins.property
    @jsii.member(jsii_name="rootFolder")
    def root_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootFolder"))

    @root_folder.setter
    def root_folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceGithubRepoOutputReference, "root_folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootFolder", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SynapseWorkspaceGithubRepo]:
        return typing.cast(typing.Optional[SynapseWorkspaceGithubRepo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SynapseWorkspaceGithubRepo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceGithubRepoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class SynapseWorkspaceIdentity:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#type SynapseWorkspace#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#type SynapseWorkspace#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseWorkspaceIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceIdentityOutputReference",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SynapseWorkspaceIdentity]:
        return typing.cast(typing.Optional[SynapseWorkspaceIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SynapseWorkspaceIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceSqlAadAdmin",
    jsii_struct_bases=[],
    name_mapping={"login": "login", "object_id": "objectId", "tenant_id": "tenantId"},
)
class SynapseWorkspaceSqlAadAdmin:
    def __init__(
        self,
        *,
        login: typing.Optional[builtins.str] = None,
        object_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param login: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#login SynapseWorkspace#login}.
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#object_id SynapseWorkspace#object_id}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tenant_id SynapseWorkspace#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceSqlAadAdmin.__init__)
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if login is not None:
            self._values["login"] = login
        if object_id is not None:
            self._values["object_id"] = object_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def login(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#login SynapseWorkspace#login}.'''
        result = self._values.get("login")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#object_id SynapseWorkspace#object_id}.'''
        result = self._values.get("object_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#tenant_id SynapseWorkspace#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceSqlAadAdmin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseWorkspaceSqlAadAdminList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceSqlAadAdminList",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceSqlAadAdminList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SynapseWorkspaceSqlAadAdminOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceSqlAadAdminList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SynapseWorkspaceSqlAadAdminOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSqlAadAdminList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSqlAadAdminList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSqlAadAdminList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SynapseWorkspaceSqlAadAdmin]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SynapseWorkspaceSqlAadAdmin]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SynapseWorkspaceSqlAadAdmin]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSqlAadAdminList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SynapseWorkspaceSqlAadAdminOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceSqlAadAdminOutputReference",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceSqlAadAdminOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetLogin")
    def reset_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogin", []))

    @jsii.member(jsii_name="resetObjectId")
    def reset_object_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectId", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdInput")
    def object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "login"))

    @login.setter
    def login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSqlAadAdminOutputReference, "login").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "login", value)

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @object_id.setter
    def object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSqlAadAdminOutputReference, "object_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSqlAadAdminOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SynapseWorkspaceSqlAadAdmin, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SynapseWorkspaceSqlAadAdmin, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SynapseWorkspaceSqlAadAdmin, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceSqlAadAdminOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SynapseWorkspaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#create SynapseWorkspace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#delete SynapseWorkspace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#read SynapseWorkspace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#update SynapseWorkspace#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SynapseWorkspaceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#create SynapseWorkspace#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#delete SynapseWorkspace#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#read SynapseWorkspace#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/synapse_workspace#update SynapseWorkspace#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynapseWorkspaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SynapseWorkspaceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.synapseWorkspace.SynapseWorkspaceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SynapseWorkspaceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SynapseWorkspaceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SynapseWorkspaceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SynapseWorkspaceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SynapseWorkspaceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SynapseWorkspace",
    "SynapseWorkspaceAadAdmin",
    "SynapseWorkspaceAadAdminList",
    "SynapseWorkspaceAadAdminOutputReference",
    "SynapseWorkspaceAzureDevopsRepo",
    "SynapseWorkspaceAzureDevopsRepoOutputReference",
    "SynapseWorkspaceConfig",
    "SynapseWorkspaceCustomerManagedKey",
    "SynapseWorkspaceCustomerManagedKeyOutputReference",
    "SynapseWorkspaceGithubRepo",
    "SynapseWorkspaceGithubRepoOutputReference",
    "SynapseWorkspaceIdentity",
    "SynapseWorkspaceIdentityOutputReference",
    "SynapseWorkspaceSqlAadAdmin",
    "SynapseWorkspaceSqlAadAdminList",
    "SynapseWorkspaceSqlAadAdminOutputReference",
    "SynapseWorkspaceTimeouts",
    "SynapseWorkspaceTimeoutsOutputReference",
]

publication.publish()
