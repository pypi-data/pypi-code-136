'''
# `azurerm_storage_account`

Refer to the Terraform Registory for docs: [`azurerm_storage_account`](https://www.terraform.io/docs/providers/azurerm/r/storage_account).
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


class StorageAccount(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account azurerm_storage_account}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_replication_type: builtins.str,
        account_tier: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        access_tier: typing.Optional[builtins.str] = None,
        account_kind: typing.Optional[builtins.str] = None,
        allow_nested_items_to_be_public: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        azure_files_authentication: typing.Optional[typing.Union["StorageAccountAzureFilesAuthentication", typing.Dict[str, typing.Any]]] = None,
        blob_properties: typing.Optional[typing.Union["StorageAccountBlobProperties", typing.Dict[str, typing.Any]]] = None,
        cross_tenant_replication_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_domain: typing.Optional[typing.Union["StorageAccountCustomDomain", typing.Dict[str, typing.Any]]] = None,
        customer_managed_key: typing.Optional[typing.Union["StorageAccountCustomerManagedKey", typing.Dict[str, typing.Any]]] = None,
        default_to_oauth_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        enable_https_traffic_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["StorageAccountIdentity", typing.Dict[str, typing.Any]]] = None,
        infrastructure_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_hns_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        large_file_share_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        min_tls_version: typing.Optional[builtins.str] = None,
        network_rules: typing.Optional[typing.Union["StorageAccountNetworkRules", typing.Dict[str, typing.Any]]] = None,
        nfsv3_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        queue_encryption_key_type: typing.Optional[builtins.str] = None,
        queue_properties: typing.Optional[typing.Union["StorageAccountQueueProperties", typing.Dict[str, typing.Any]]] = None,
        routing: typing.Optional[typing.Union["StorageAccountRouting", typing.Dict[str, typing.Any]]] = None,
        shared_access_key_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        share_properties: typing.Optional[typing.Union["StorageAccountShareProperties", typing.Dict[str, typing.Any]]] = None,
        static_website: typing.Optional[typing.Union["StorageAccountStaticWebsite", typing.Dict[str, typing.Any]]] = None,
        table_encryption_key_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StorageAccountTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account azurerm_storage_account} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_replication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_replication_type StorageAccount#account_replication_type}.
        :param account_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_tier StorageAccount#account_tier}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#location StorageAccount#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#name StorageAccount#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#resource_group_name StorageAccount#resource_group_name}.
        :param access_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#access_tier StorageAccount#access_tier}.
        :param account_kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_kind StorageAccount#account_kind}.
        :param allow_nested_items_to_be_public: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allow_nested_items_to_be_public StorageAccount#allow_nested_items_to_be_public}.
        :param azure_files_authentication: azure_files_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#azure_files_authentication StorageAccount#azure_files_authentication}
        :param blob_properties: blob_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#blob_properties StorageAccount#blob_properties}
        :param cross_tenant_replication_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cross_tenant_replication_enabled StorageAccount#cross_tenant_replication_enabled}.
        :param custom_domain: custom_domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#custom_domain StorageAccount#custom_domain}
        :param customer_managed_key: customer_managed_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#customer_managed_key StorageAccount#customer_managed_key}
        :param default_to_oauth_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_to_oauth_authentication StorageAccount#default_to_oauth_authentication}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#edge_zone StorageAccount#edge_zone}.
        :param enable_https_traffic_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enable_https_traffic_only StorageAccount#enable_https_traffic_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#id StorageAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#identity StorageAccount#identity}
        :param infrastructure_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#infrastructure_encryption_enabled StorageAccount#infrastructure_encryption_enabled}.
        :param is_hns_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#is_hns_enabled StorageAccount#is_hns_enabled}.
        :param large_file_share_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#large_file_share_enabled StorageAccount#large_file_share_enabled}.
        :param min_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#min_tls_version StorageAccount#min_tls_version}.
        :param network_rules: network_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#network_rules StorageAccount#network_rules}
        :param nfsv3_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#nfsv3_enabled StorageAccount#nfsv3_enabled}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#public_network_access_enabled StorageAccount#public_network_access_enabled}.
        :param queue_encryption_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#queue_encryption_key_type StorageAccount#queue_encryption_key_type}.
        :param queue_properties: queue_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#queue_properties StorageAccount#queue_properties}
        :param routing: routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#routing StorageAccount#routing}
        :param shared_access_key_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#shared_access_key_enabled StorageAccount#shared_access_key_enabled}.
        :param share_properties: share_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#share_properties StorageAccount#share_properties}
        :param static_website: static_website block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#static_website StorageAccount#static_website}
        :param table_encryption_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#table_encryption_key_type StorageAccount#table_encryption_key_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#tags StorageAccount#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#timeouts StorageAccount#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccount.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageAccountConfig(
            account_replication_type=account_replication_type,
            account_tier=account_tier,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            access_tier=access_tier,
            account_kind=account_kind,
            allow_nested_items_to_be_public=allow_nested_items_to_be_public,
            azure_files_authentication=azure_files_authentication,
            blob_properties=blob_properties,
            cross_tenant_replication_enabled=cross_tenant_replication_enabled,
            custom_domain=custom_domain,
            customer_managed_key=customer_managed_key,
            default_to_oauth_authentication=default_to_oauth_authentication,
            edge_zone=edge_zone,
            enable_https_traffic_only=enable_https_traffic_only,
            id=id,
            identity=identity,
            infrastructure_encryption_enabled=infrastructure_encryption_enabled,
            is_hns_enabled=is_hns_enabled,
            large_file_share_enabled=large_file_share_enabled,
            min_tls_version=min_tls_version,
            network_rules=network_rules,
            nfsv3_enabled=nfsv3_enabled,
            public_network_access_enabled=public_network_access_enabled,
            queue_encryption_key_type=queue_encryption_key_type,
            queue_properties=queue_properties,
            routing=routing,
            shared_access_key_enabled=shared_access_key_enabled,
            share_properties=share_properties,
            static_website=static_website,
            table_encryption_key_type=table_encryption_key_type,
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

    @jsii.member(jsii_name="putAzureFilesAuthentication")
    def put_azure_files_authentication(
        self,
        *,
        directory_type: builtins.str,
        active_directory: typing.Optional[typing.Union["StorageAccountAzureFilesAuthenticationActiveDirectory", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param directory_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#directory_type StorageAccount#directory_type}.
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#active_directory StorageAccount#active_directory}
        '''
        value = StorageAccountAzureFilesAuthentication(
            directory_type=directory_type, active_directory=active_directory
        )

        return typing.cast(None, jsii.invoke(self, "putAzureFilesAuthentication", [value]))

    @jsii.member(jsii_name="putBlobProperties")
    def put_blob_properties(
        self,
        *,
        change_feed_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        change_feed_retention_in_days: typing.Optional[jsii.Number] = None,
        container_delete_retention_policy: typing.Optional[typing.Union["StorageAccountBlobPropertiesContainerDeleteRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        cors_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountBlobPropertiesCorsRule", typing.Dict[str, typing.Any]]]]] = None,
        default_service_version: typing.Optional[builtins.str] = None,
        delete_retention_policy: typing.Optional[typing.Union["StorageAccountBlobPropertiesDeleteRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        last_access_time_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versioning_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param change_feed_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#change_feed_enabled StorageAccount#change_feed_enabled}.
        :param change_feed_retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#change_feed_retention_in_days StorageAccount#change_feed_retention_in_days}.
        :param container_delete_retention_policy: container_delete_retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#container_delete_retention_policy StorageAccount#container_delete_retention_policy}
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        :param default_service_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_service_version StorageAccount#default_service_version}.
        :param delete_retention_policy: delete_retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete_retention_policy StorageAccount#delete_retention_policy}
        :param last_access_time_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#last_access_time_enabled StorageAccount#last_access_time_enabled}.
        :param versioning_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#versioning_enabled StorageAccount#versioning_enabled}.
        '''
        value = StorageAccountBlobProperties(
            change_feed_enabled=change_feed_enabled,
            change_feed_retention_in_days=change_feed_retention_in_days,
            container_delete_retention_policy=container_delete_retention_policy,
            cors_rule=cors_rule,
            default_service_version=default_service_version,
            delete_retention_policy=delete_retention_policy,
            last_access_time_enabled=last_access_time_enabled,
            versioning_enabled=versioning_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putBlobProperties", [value]))

    @jsii.member(jsii_name="putCustomDomain")
    def put_custom_domain(
        self,
        *,
        name: builtins.str,
        use_subdomain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#name StorageAccount#name}.
        :param use_subdomain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#use_subdomain StorageAccount#use_subdomain}.
        '''
        value = StorageAccountCustomDomain(name=name, use_subdomain=use_subdomain)

        return typing.cast(None, jsii.invoke(self, "putCustomDomain", [value]))

    @jsii.member(jsii_name="putCustomerManagedKey")
    def put_customer_managed_key(
        self,
        *,
        key_vault_key_id: builtins.str,
        user_assigned_identity_id: builtins.str,
    ) -> None:
        '''
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#key_vault_key_id StorageAccount#key_vault_key_id}.
        :param user_assigned_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#user_assigned_identity_id StorageAccount#user_assigned_identity_id}.
        '''
        value = StorageAccountCustomerManagedKey(
            key_vault_key_id=key_vault_key_id,
            user_assigned_identity_id=user_assigned_identity_id,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomerManagedKey", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#type StorageAccount#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#identity_ids StorageAccount#identity_ids}.
        '''
        value = StorageAccountIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putNetworkRules")
    def put_network_rules(
        self,
        *,
        default_action: builtins.str,
        bypass: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_link_access: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountNetworkRulesPrivateLinkAccess", typing.Dict[str, typing.Any]]]]] = None,
        virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_action StorageAccount#default_action}.
        :param bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#bypass StorageAccount#bypass}.
        :param ip_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#ip_rules StorageAccount#ip_rules}.
        :param private_link_access: private_link_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#private_link_access StorageAccount#private_link_access}
        :param virtual_network_subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#virtual_network_subnet_ids StorageAccount#virtual_network_subnet_ids}.
        '''
        value = StorageAccountNetworkRules(
            default_action=default_action,
            bypass=bypass,
            ip_rules=ip_rules,
            private_link_access=private_link_access,
            virtual_network_subnet_ids=virtual_network_subnet_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkRules", [value]))

    @jsii.member(jsii_name="putQueueProperties")
    def put_queue_properties(
        self,
        *,
        cors_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountQueuePropertiesCorsRule", typing.Dict[str, typing.Any]]]]] = None,
        hour_metrics: typing.Optional[typing.Union["StorageAccountQueuePropertiesHourMetrics", typing.Dict[str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["StorageAccountQueuePropertiesLogging", typing.Dict[str, typing.Any]]] = None,
        minute_metrics: typing.Optional[typing.Union["StorageAccountQueuePropertiesMinuteMetrics", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        :param hour_metrics: hour_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#hour_metrics StorageAccount#hour_metrics}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#logging StorageAccount#logging}
        :param minute_metrics: minute_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#minute_metrics StorageAccount#minute_metrics}
        '''
        value = StorageAccountQueueProperties(
            cors_rule=cors_rule,
            hour_metrics=hour_metrics,
            logging=logging,
            minute_metrics=minute_metrics,
        )

        return typing.cast(None, jsii.invoke(self, "putQueueProperties", [value]))

    @jsii.member(jsii_name="putRouting")
    def put_routing(
        self,
        *,
        choice: typing.Optional[builtins.str] = None,
        publish_internet_endpoints: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        publish_microsoft_endpoints: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param choice: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#choice StorageAccount#choice}.
        :param publish_internet_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#publish_internet_endpoints StorageAccount#publish_internet_endpoints}.
        :param publish_microsoft_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#publish_microsoft_endpoints StorageAccount#publish_microsoft_endpoints}.
        '''
        value = StorageAccountRouting(
            choice=choice,
            publish_internet_endpoints=publish_internet_endpoints,
            publish_microsoft_endpoints=publish_microsoft_endpoints,
        )

        return typing.cast(None, jsii.invoke(self, "putRouting", [value]))

    @jsii.member(jsii_name="putShareProperties")
    def put_share_properties(
        self,
        *,
        cors_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountSharePropertiesCorsRule", typing.Dict[str, typing.Any]]]]] = None,
        retention_policy: typing.Optional[typing.Union["StorageAccountSharePropertiesRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        smb: typing.Optional[typing.Union["StorageAccountSharePropertiesSmb", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy StorageAccount#retention_policy}
        :param smb: smb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#smb StorageAccount#smb}
        '''
        value = StorageAccountShareProperties(
            cors_rule=cors_rule, retention_policy=retention_policy, smb=smb
        )

        return typing.cast(None, jsii.invoke(self, "putShareProperties", [value]))

    @jsii.member(jsii_name="putStaticWebsite")
    def put_static_website(
        self,
        *,
        error404_document: typing.Optional[builtins.str] = None,
        index_document: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error404_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#error_404_document StorageAccount#error_404_document}.
        :param index_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#index_document StorageAccount#index_document}.
        '''
        value = StorageAccountStaticWebsite(
            error404_document=error404_document, index_document=index_document
        )

        return typing.cast(None, jsii.invoke(self, "putStaticWebsite", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#create StorageAccount#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete StorageAccount#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#read StorageAccount#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#update StorageAccount#update}.
        '''
        value = StorageAccountTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccessTier")
    def reset_access_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessTier", []))

    @jsii.member(jsii_name="resetAccountKind")
    def reset_account_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountKind", []))

    @jsii.member(jsii_name="resetAllowNestedItemsToBePublic")
    def reset_allow_nested_items_to_be_public(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowNestedItemsToBePublic", []))

    @jsii.member(jsii_name="resetAzureFilesAuthentication")
    def reset_azure_files_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureFilesAuthentication", []))

    @jsii.member(jsii_name="resetBlobProperties")
    def reset_blob_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlobProperties", []))

    @jsii.member(jsii_name="resetCrossTenantReplicationEnabled")
    def reset_cross_tenant_replication_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossTenantReplicationEnabled", []))

    @jsii.member(jsii_name="resetCustomDomain")
    def reset_custom_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDomain", []))

    @jsii.member(jsii_name="resetCustomerManagedKey")
    def reset_customer_managed_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedKey", []))

    @jsii.member(jsii_name="resetDefaultToOauthAuthentication")
    def reset_default_to_oauth_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultToOauthAuthentication", []))

    @jsii.member(jsii_name="resetEdgeZone")
    def reset_edge_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeZone", []))

    @jsii.member(jsii_name="resetEnableHttpsTrafficOnly")
    def reset_enable_https_traffic_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHttpsTrafficOnly", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetInfrastructureEncryptionEnabled")
    def reset_infrastructure_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInfrastructureEncryptionEnabled", []))

    @jsii.member(jsii_name="resetIsHnsEnabled")
    def reset_is_hns_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsHnsEnabled", []))

    @jsii.member(jsii_name="resetLargeFileShareEnabled")
    def reset_large_file_share_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLargeFileShareEnabled", []))

    @jsii.member(jsii_name="resetMinTlsVersion")
    def reset_min_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTlsVersion", []))

    @jsii.member(jsii_name="resetNetworkRules")
    def reset_network_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkRules", []))

    @jsii.member(jsii_name="resetNfsv3Enabled")
    def reset_nfsv3_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsv3Enabled", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetQueueEncryptionKeyType")
    def reset_queue_encryption_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueueEncryptionKeyType", []))

    @jsii.member(jsii_name="resetQueueProperties")
    def reset_queue_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueueProperties", []))

    @jsii.member(jsii_name="resetRouting")
    def reset_routing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouting", []))

    @jsii.member(jsii_name="resetSharedAccessKeyEnabled")
    def reset_shared_access_key_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedAccessKeyEnabled", []))

    @jsii.member(jsii_name="resetShareProperties")
    def reset_share_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareProperties", []))

    @jsii.member(jsii_name="resetStaticWebsite")
    def reset_static_website(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticWebsite", []))

    @jsii.member(jsii_name="resetTableEncryptionKeyType")
    def reset_table_encryption_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableEncryptionKeyType", []))

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
    @jsii.member(jsii_name="azureFilesAuthentication")
    def azure_files_authentication(
        self,
    ) -> "StorageAccountAzureFilesAuthenticationOutputReference":
        return typing.cast("StorageAccountAzureFilesAuthenticationOutputReference", jsii.get(self, "azureFilesAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="blobProperties")
    def blob_properties(self) -> "StorageAccountBlobPropertiesOutputReference":
        return typing.cast("StorageAccountBlobPropertiesOutputReference", jsii.get(self, "blobProperties"))

    @builtins.property
    @jsii.member(jsii_name="customDomain")
    def custom_domain(self) -> "StorageAccountCustomDomainOutputReference":
        return typing.cast("StorageAccountCustomDomainOutputReference", jsii.get(self, "customDomain"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKey")
    def customer_managed_key(self) -> "StorageAccountCustomerManagedKeyOutputReference":
        return typing.cast("StorageAccountCustomerManagedKeyOutputReference", jsii.get(self, "customerManagedKey"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "StorageAccountIdentityOutputReference":
        return typing.cast("StorageAccountIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="networkRules")
    def network_rules(self) -> "StorageAccountNetworkRulesOutputReference":
        return typing.cast("StorageAccountNetworkRulesOutputReference", jsii.get(self, "networkRules"))

    @builtins.property
    @jsii.member(jsii_name="primaryAccessKey")
    def primary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="primaryBlobConnectionString")
    def primary_blob_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryBlobConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="primaryBlobEndpoint")
    def primary_blob_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryBlobEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryBlobHost")
    def primary_blob_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryBlobHost"))

    @builtins.property
    @jsii.member(jsii_name="primaryConnectionString")
    def primary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="primaryDfsEndpoint")
    def primary_dfs_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryDfsEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryDfsHost")
    def primary_dfs_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryDfsHost"))

    @builtins.property
    @jsii.member(jsii_name="primaryFileEndpoint")
    def primary_file_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryFileEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryFileHost")
    def primary_file_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryFileHost"))

    @builtins.property
    @jsii.member(jsii_name="primaryLocation")
    def primary_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryLocation"))

    @builtins.property
    @jsii.member(jsii_name="primaryQueueEndpoint")
    def primary_queue_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryQueueEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryQueueHost")
    def primary_queue_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryQueueHost"))

    @builtins.property
    @jsii.member(jsii_name="primaryTableEndpoint")
    def primary_table_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryTableEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryTableHost")
    def primary_table_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryTableHost"))

    @builtins.property
    @jsii.member(jsii_name="primaryWebEndpoint")
    def primary_web_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryWebEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryWebHost")
    def primary_web_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryWebHost"))

    @builtins.property
    @jsii.member(jsii_name="queueProperties")
    def queue_properties(self) -> "StorageAccountQueuePropertiesOutputReference":
        return typing.cast("StorageAccountQueuePropertiesOutputReference", jsii.get(self, "queueProperties"))

    @builtins.property
    @jsii.member(jsii_name="routing")
    def routing(self) -> "StorageAccountRoutingOutputReference":
        return typing.cast("StorageAccountRoutingOutputReference", jsii.get(self, "routing"))

    @builtins.property
    @jsii.member(jsii_name="secondaryAccessKey")
    def secondary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="secondaryBlobConnectionString")
    def secondary_blob_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryBlobConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="secondaryBlobEndpoint")
    def secondary_blob_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryBlobEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryBlobHost")
    def secondary_blob_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryBlobHost"))

    @builtins.property
    @jsii.member(jsii_name="secondaryConnectionString")
    def secondary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="secondaryDfsEndpoint")
    def secondary_dfs_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryDfsEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryDfsHost")
    def secondary_dfs_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryDfsHost"))

    @builtins.property
    @jsii.member(jsii_name="secondaryFileEndpoint")
    def secondary_file_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryFileEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryFileHost")
    def secondary_file_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryFileHost"))

    @builtins.property
    @jsii.member(jsii_name="secondaryLocation")
    def secondary_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryLocation"))

    @builtins.property
    @jsii.member(jsii_name="secondaryQueueEndpoint")
    def secondary_queue_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryQueueEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryQueueHost")
    def secondary_queue_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryQueueHost"))

    @builtins.property
    @jsii.member(jsii_name="secondaryTableEndpoint")
    def secondary_table_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryTableEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryTableHost")
    def secondary_table_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryTableHost"))

    @builtins.property
    @jsii.member(jsii_name="secondaryWebEndpoint")
    def secondary_web_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryWebEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryWebHost")
    def secondary_web_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryWebHost"))

    @builtins.property
    @jsii.member(jsii_name="shareProperties")
    def share_properties(self) -> "StorageAccountSharePropertiesOutputReference":
        return typing.cast("StorageAccountSharePropertiesOutputReference", jsii.get(self, "shareProperties"))

    @builtins.property
    @jsii.member(jsii_name="staticWebsite")
    def static_website(self) -> "StorageAccountStaticWebsiteOutputReference":
        return typing.cast("StorageAccountStaticWebsiteOutputReference", jsii.get(self, "staticWebsite"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StorageAccountTimeoutsOutputReference":
        return typing.cast("StorageAccountTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accessTierInput")
    def access_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTierInput"))

    @builtins.property
    @jsii.member(jsii_name="accountKindInput")
    def account_kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountKindInput"))

    @builtins.property
    @jsii.member(jsii_name="accountReplicationTypeInput")
    def account_replication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountReplicationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="accountTierInput")
    def account_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountTierInput"))

    @builtins.property
    @jsii.member(jsii_name="allowNestedItemsToBePublicInput")
    def allow_nested_items_to_be_public_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowNestedItemsToBePublicInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFilesAuthenticationInput")
    def azure_files_authentication_input(
        self,
    ) -> typing.Optional["StorageAccountAzureFilesAuthentication"]:
        return typing.cast(typing.Optional["StorageAccountAzureFilesAuthentication"], jsii.get(self, "azureFilesAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="blobPropertiesInput")
    def blob_properties_input(self) -> typing.Optional["StorageAccountBlobProperties"]:
        return typing.cast(typing.Optional["StorageAccountBlobProperties"], jsii.get(self, "blobPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="crossTenantReplicationEnabledInput")
    def cross_tenant_replication_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "crossTenantReplicationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="customDomainInput")
    def custom_domain_input(self) -> typing.Optional["StorageAccountCustomDomain"]:
        return typing.cast(typing.Optional["StorageAccountCustomDomain"], jsii.get(self, "customDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyInput")
    def customer_managed_key_input(
        self,
    ) -> typing.Optional["StorageAccountCustomerManagedKey"]:
        return typing.cast(typing.Optional["StorageAccountCustomerManagedKey"], jsii.get(self, "customerManagedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultToOauthAuthenticationInput")
    def default_to_oauth_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "defaultToOauthAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeZoneInput")
    def edge_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpsTrafficOnlyInput")
    def enable_https_traffic_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHttpsTrafficOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["StorageAccountIdentity"]:
        return typing.cast(typing.Optional["StorageAccountIdentity"], jsii.get(self, "identityInput"))

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
    @jsii.member(jsii_name="isHnsEnabledInput")
    def is_hns_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isHnsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="largeFileShareEnabledInput")
    def large_file_share_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "largeFileShareEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="minTlsVersionInput")
    def min_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkRulesInput")
    def network_rules_input(self) -> typing.Optional["StorageAccountNetworkRules"]:
        return typing.cast(typing.Optional["StorageAccountNetworkRules"], jsii.get(self, "networkRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsv3EnabledInput")
    def nfsv3_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "nfsv3EnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="queueEncryptionKeyTypeInput")
    def queue_encryption_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queueEncryptionKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="queuePropertiesInput")
    def queue_properties_input(
        self,
    ) -> typing.Optional["StorageAccountQueueProperties"]:
        return typing.cast(typing.Optional["StorageAccountQueueProperties"], jsii.get(self, "queuePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="routingInput")
    def routing_input(self) -> typing.Optional["StorageAccountRouting"]:
        return typing.cast(typing.Optional["StorageAccountRouting"], jsii.get(self, "routingInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedAccessKeyEnabledInput")
    def shared_access_key_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sharedAccessKeyEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sharePropertiesInput")
    def share_properties_input(
        self,
    ) -> typing.Optional["StorageAccountShareProperties"]:
        return typing.cast(typing.Optional["StorageAccountShareProperties"], jsii.get(self, "sharePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="staticWebsiteInput")
    def static_website_input(self) -> typing.Optional["StorageAccountStaticWebsite"]:
        return typing.cast(typing.Optional["StorageAccountStaticWebsite"], jsii.get(self, "staticWebsiteInput"))

    @builtins.property
    @jsii.member(jsii_name="tableEncryptionKeyTypeInput")
    def table_encryption_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableEncryptionKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StorageAccountTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StorageAccountTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="accessTier")
    def access_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessTier"))

    @access_tier.setter
    def access_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "access_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessTier", value)

    @builtins.property
    @jsii.member(jsii_name="accountKind")
    def account_kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountKind"))

    @account_kind.setter
    def account_kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "account_kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountKind", value)

    @builtins.property
    @jsii.member(jsii_name="accountReplicationType")
    def account_replication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountReplicationType"))

    @account_replication_type.setter
    def account_replication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "account_replication_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountReplicationType", value)

    @builtins.property
    @jsii.member(jsii_name="accountTier")
    def account_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountTier"))

    @account_tier.setter
    def account_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "account_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountTier", value)

    @builtins.property
    @jsii.member(jsii_name="allowNestedItemsToBePublic")
    def allow_nested_items_to_be_public(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowNestedItemsToBePublic"))

    @allow_nested_items_to_be_public.setter
    def allow_nested_items_to_be_public(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "allow_nested_items_to_be_public").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowNestedItemsToBePublic", value)

    @builtins.property
    @jsii.member(jsii_name="crossTenantReplicationEnabled")
    def cross_tenant_replication_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "crossTenantReplicationEnabled"))

    @cross_tenant_replication_enabled.setter
    def cross_tenant_replication_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "cross_tenant_replication_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossTenantReplicationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="defaultToOauthAuthentication")
    def default_to_oauth_authentication(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "defaultToOauthAuthentication"))

    @default_to_oauth_authentication.setter
    def default_to_oauth_authentication(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "default_to_oauth_authentication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultToOauthAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="edgeZone")
    def edge_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeZone"))

    @edge_zone.setter
    def edge_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "edge_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeZone", value)

    @builtins.property
    @jsii.member(jsii_name="enableHttpsTrafficOnly")
    def enable_https_traffic_only(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHttpsTrafficOnly"))

    @enable_https_traffic_only.setter
    def enable_https_traffic_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "enable_https_traffic_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttpsTrafficOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "id").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccount, "infrastructure_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "infrastructureEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isHnsEnabled")
    def is_hns_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isHnsEnabled"))

    @is_hns_enabled.setter
    def is_hns_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "is_hns_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isHnsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="largeFileShareEnabled")
    def large_file_share_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "largeFileShareEnabled"))

    @large_file_share_enabled.setter
    def large_file_share_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "large_file_share_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "largeFileShareEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="minTlsVersion")
    def min_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minTlsVersion"))

    @min_tls_version.setter
    def min_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "min_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nfsv3Enabled")
    def nfsv3_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "nfsv3Enabled"))

    @nfsv3_enabled.setter
    def nfsv3_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "nfsv3_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nfsv3Enabled", value)

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
            type_hints = typing.get_type_hints(getattr(StorageAccount, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="queueEncryptionKeyType")
    def queue_encryption_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueEncryptionKeyType"))

    @queue_encryption_key_type.setter
    def queue_encryption_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "queue_encryption_key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueEncryptionKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAccessKeyEnabled")
    def shared_access_key_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sharedAccessKeyEnabled"))

    @shared_access_key_enabled.setter
    def shared_access_key_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "shared_access_key_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAccessKeyEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tableEncryptionKeyType")
    def table_encryption_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableEncryptionKeyType"))

    @table_encryption_key_type.setter
    def table_encryption_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "table_encryption_key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableEncryptionKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccount, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountAzureFilesAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "directory_type": "directoryType",
        "active_directory": "activeDirectory",
    },
)
class StorageAccountAzureFilesAuthentication:
    def __init__(
        self,
        *,
        directory_type: builtins.str,
        active_directory: typing.Optional[typing.Union["StorageAccountAzureFilesAuthenticationActiveDirectory", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param directory_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#directory_type StorageAccount#directory_type}.
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#active_directory StorageAccount#active_directory}
        '''
        if isinstance(active_directory, dict):
            active_directory = StorageAccountAzureFilesAuthenticationActiveDirectory(**active_directory)
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountAzureFilesAuthentication.__init__)
            check_type(argname="argument directory_type", value=directory_type, expected_type=type_hints["directory_type"])
            check_type(argname="argument active_directory", value=active_directory, expected_type=type_hints["active_directory"])
        self._values: typing.Dict[str, typing.Any] = {
            "directory_type": directory_type,
        }
        if active_directory is not None:
            self._values["active_directory"] = active_directory

    @builtins.property
    def directory_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#directory_type StorageAccount#directory_type}.'''
        result = self._values.get("directory_type")
        assert result is not None, "Required property 'directory_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_directory(
        self,
    ) -> typing.Optional["StorageAccountAzureFilesAuthenticationActiveDirectory"]:
        '''active_directory block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#active_directory StorageAccount#active_directory}
        '''
        result = self._values.get("active_directory")
        return typing.cast(typing.Optional["StorageAccountAzureFilesAuthenticationActiveDirectory"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountAzureFilesAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountAzureFilesAuthenticationActiveDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "domain_guid": "domainGuid",
        "domain_name": "domainName",
        "domain_sid": "domainSid",
        "forest_name": "forestName",
        "netbios_domain_name": "netbiosDomainName",
        "storage_sid": "storageSid",
    },
)
class StorageAccountAzureFilesAuthenticationActiveDirectory:
    def __init__(
        self,
        *,
        domain_guid: builtins.str,
        domain_name: builtins.str,
        domain_sid: builtins.str,
        forest_name: builtins.str,
        netbios_domain_name: builtins.str,
        storage_sid: builtins.str,
    ) -> None:
        '''
        :param domain_guid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_guid StorageAccount#domain_guid}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_name StorageAccount#domain_name}.
        :param domain_sid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_sid StorageAccount#domain_sid}.
        :param forest_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#forest_name StorageAccount#forest_name}.
        :param netbios_domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#netbios_domain_name StorageAccount#netbios_domain_name}.
        :param storage_sid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#storage_sid StorageAccount#storage_sid}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountAzureFilesAuthenticationActiveDirectory.__init__)
            check_type(argname="argument domain_guid", value=domain_guid, expected_type=type_hints["domain_guid"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument domain_sid", value=domain_sid, expected_type=type_hints["domain_sid"])
            check_type(argname="argument forest_name", value=forest_name, expected_type=type_hints["forest_name"])
            check_type(argname="argument netbios_domain_name", value=netbios_domain_name, expected_type=type_hints["netbios_domain_name"])
            check_type(argname="argument storage_sid", value=storage_sid, expected_type=type_hints["storage_sid"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_guid": domain_guid,
            "domain_name": domain_name,
            "domain_sid": domain_sid,
            "forest_name": forest_name,
            "netbios_domain_name": netbios_domain_name,
            "storage_sid": storage_sid,
        }

    @builtins.property
    def domain_guid(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_guid StorageAccount#domain_guid}.'''
        result = self._values.get("domain_guid")
        assert result is not None, "Required property 'domain_guid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_name StorageAccount#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_sid(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_sid StorageAccount#domain_sid}.'''
        result = self._values.get("domain_sid")
        assert result is not None, "Required property 'domain_sid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def forest_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#forest_name StorageAccount#forest_name}.'''
        result = self._values.get("forest_name")
        assert result is not None, "Required property 'forest_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def netbios_domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#netbios_domain_name StorageAccount#netbios_domain_name}.'''
        result = self._values.get("netbios_domain_name")
        assert result is not None, "Required property 'netbios_domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_sid(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#storage_sid StorageAccount#storage_sid}.'''
        result = self._values.get("storage_sid")
        assert result is not None, "Required property 'storage_sid' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountAzureFilesAuthenticationActiveDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="domainGuidInput")
    def domain_guid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainGuidInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainSidInput")
    def domain_sid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainSidInput"))

    @builtins.property
    @jsii.member(jsii_name="forestNameInput")
    def forest_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forestNameInput"))

    @builtins.property
    @jsii.member(jsii_name="netbiosDomainNameInput")
    def netbios_domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "netbiosDomainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageSidInput")
    def storage_sid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageSidInput"))

    @builtins.property
    @jsii.member(jsii_name="domainGuid")
    def domain_guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainGuid"))

    @domain_guid.setter
    def domain_guid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference, "domain_guid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainGuid", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="domainSid")
    def domain_sid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainSid"))

    @domain_sid.setter
    def domain_sid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference, "domain_sid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainSid", value)

    @builtins.property
    @jsii.member(jsii_name="forestName")
    def forest_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forestName"))

    @forest_name.setter
    def forest_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference, "forest_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forestName", value)

    @builtins.property
    @jsii.member(jsii_name="netbiosDomainName")
    def netbios_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "netbiosDomainName"))

    @netbios_domain_name.setter
    def netbios_domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference, "netbios_domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netbiosDomainName", value)

    @builtins.property
    @jsii.member(jsii_name="storageSid")
    def storage_sid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageSid"))

    @storage_sid.setter
    def storage_sid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference, "storage_sid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageSid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageAccountAzureFilesAuthenticationActiveDirectory]:
        return typing.cast(typing.Optional[StorageAccountAzureFilesAuthenticationActiveDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountAzureFilesAuthenticationActiveDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountAzureFilesAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountAzureFilesAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountAzureFilesAuthenticationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActiveDirectory")
    def put_active_directory(
        self,
        *,
        domain_guid: builtins.str,
        domain_name: builtins.str,
        domain_sid: builtins.str,
        forest_name: builtins.str,
        netbios_domain_name: builtins.str,
        storage_sid: builtins.str,
    ) -> None:
        '''
        :param domain_guid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_guid StorageAccount#domain_guid}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_name StorageAccount#domain_name}.
        :param domain_sid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#domain_sid StorageAccount#domain_sid}.
        :param forest_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#forest_name StorageAccount#forest_name}.
        :param netbios_domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#netbios_domain_name StorageAccount#netbios_domain_name}.
        :param storage_sid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#storage_sid StorageAccount#storage_sid}.
        '''
        value = StorageAccountAzureFilesAuthenticationActiveDirectory(
            domain_guid=domain_guid,
            domain_name=domain_name,
            domain_sid=domain_sid,
            forest_name=forest_name,
            netbios_domain_name=netbios_domain_name,
            storage_sid=storage_sid,
        )

        return typing.cast(None, jsii.invoke(self, "putActiveDirectory", [value]))

    @jsii.member(jsii_name="resetActiveDirectory")
    def reset_active_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectory", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectory")
    def active_directory(
        self,
    ) -> StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference:
        return typing.cast(StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference, jsii.get(self, "activeDirectory"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryInput")
    def active_directory_input(
        self,
    ) -> typing.Optional[StorageAccountAzureFilesAuthenticationActiveDirectory]:
        return typing.cast(typing.Optional[StorageAccountAzureFilesAuthenticationActiveDirectory], jsii.get(self, "activeDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryTypeInput")
    def directory_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryType")
    def directory_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryType"))

    @directory_type.setter
    def directory_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationOutputReference, "directory_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountAzureFilesAuthentication]:
        return typing.cast(typing.Optional[StorageAccountAzureFilesAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountAzureFilesAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountAzureFilesAuthenticationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobProperties",
    jsii_struct_bases=[],
    name_mapping={
        "change_feed_enabled": "changeFeedEnabled",
        "change_feed_retention_in_days": "changeFeedRetentionInDays",
        "container_delete_retention_policy": "containerDeleteRetentionPolicy",
        "cors_rule": "corsRule",
        "default_service_version": "defaultServiceVersion",
        "delete_retention_policy": "deleteRetentionPolicy",
        "last_access_time_enabled": "lastAccessTimeEnabled",
        "versioning_enabled": "versioningEnabled",
    },
)
class StorageAccountBlobProperties:
    def __init__(
        self,
        *,
        change_feed_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        change_feed_retention_in_days: typing.Optional[jsii.Number] = None,
        container_delete_retention_policy: typing.Optional[typing.Union["StorageAccountBlobPropertiesContainerDeleteRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        cors_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountBlobPropertiesCorsRule", typing.Dict[str, typing.Any]]]]] = None,
        default_service_version: typing.Optional[builtins.str] = None,
        delete_retention_policy: typing.Optional[typing.Union["StorageAccountBlobPropertiesDeleteRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        last_access_time_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versioning_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param change_feed_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#change_feed_enabled StorageAccount#change_feed_enabled}.
        :param change_feed_retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#change_feed_retention_in_days StorageAccount#change_feed_retention_in_days}.
        :param container_delete_retention_policy: container_delete_retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#container_delete_retention_policy StorageAccount#container_delete_retention_policy}
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        :param default_service_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_service_version StorageAccount#default_service_version}.
        :param delete_retention_policy: delete_retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete_retention_policy StorageAccount#delete_retention_policy}
        :param last_access_time_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#last_access_time_enabled StorageAccount#last_access_time_enabled}.
        :param versioning_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#versioning_enabled StorageAccount#versioning_enabled}.
        '''
        if isinstance(container_delete_retention_policy, dict):
            container_delete_retention_policy = StorageAccountBlobPropertiesContainerDeleteRetentionPolicy(**container_delete_retention_policy)
        if isinstance(delete_retention_policy, dict):
            delete_retention_policy = StorageAccountBlobPropertiesDeleteRetentionPolicy(**delete_retention_policy)
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountBlobProperties.__init__)
            check_type(argname="argument change_feed_enabled", value=change_feed_enabled, expected_type=type_hints["change_feed_enabled"])
            check_type(argname="argument change_feed_retention_in_days", value=change_feed_retention_in_days, expected_type=type_hints["change_feed_retention_in_days"])
            check_type(argname="argument container_delete_retention_policy", value=container_delete_retention_policy, expected_type=type_hints["container_delete_retention_policy"])
            check_type(argname="argument cors_rule", value=cors_rule, expected_type=type_hints["cors_rule"])
            check_type(argname="argument default_service_version", value=default_service_version, expected_type=type_hints["default_service_version"])
            check_type(argname="argument delete_retention_policy", value=delete_retention_policy, expected_type=type_hints["delete_retention_policy"])
            check_type(argname="argument last_access_time_enabled", value=last_access_time_enabled, expected_type=type_hints["last_access_time_enabled"])
            check_type(argname="argument versioning_enabled", value=versioning_enabled, expected_type=type_hints["versioning_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if change_feed_enabled is not None:
            self._values["change_feed_enabled"] = change_feed_enabled
        if change_feed_retention_in_days is not None:
            self._values["change_feed_retention_in_days"] = change_feed_retention_in_days
        if container_delete_retention_policy is not None:
            self._values["container_delete_retention_policy"] = container_delete_retention_policy
        if cors_rule is not None:
            self._values["cors_rule"] = cors_rule
        if default_service_version is not None:
            self._values["default_service_version"] = default_service_version
        if delete_retention_policy is not None:
            self._values["delete_retention_policy"] = delete_retention_policy
        if last_access_time_enabled is not None:
            self._values["last_access_time_enabled"] = last_access_time_enabled
        if versioning_enabled is not None:
            self._values["versioning_enabled"] = versioning_enabled

    @builtins.property
    def change_feed_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#change_feed_enabled StorageAccount#change_feed_enabled}.'''
        result = self._values.get("change_feed_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def change_feed_retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#change_feed_retention_in_days StorageAccount#change_feed_retention_in_days}.'''
        result = self._values.get("change_feed_retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def container_delete_retention_policy(
        self,
    ) -> typing.Optional["StorageAccountBlobPropertiesContainerDeleteRetentionPolicy"]:
        '''container_delete_retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#container_delete_retention_policy StorageAccount#container_delete_retention_policy}
        '''
        result = self._values.get("container_delete_retention_policy")
        return typing.cast(typing.Optional["StorageAccountBlobPropertiesContainerDeleteRetentionPolicy"], result)

    @builtins.property
    def cors_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountBlobPropertiesCorsRule"]]]:
        '''cors_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        '''
        result = self._values.get("cors_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountBlobPropertiesCorsRule"]]], result)

    @builtins.property
    def default_service_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_service_version StorageAccount#default_service_version}.'''
        result = self._values.get("default_service_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_retention_policy(
        self,
    ) -> typing.Optional["StorageAccountBlobPropertiesDeleteRetentionPolicy"]:
        '''delete_retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete_retention_policy StorageAccount#delete_retention_policy}
        '''
        result = self._values.get("delete_retention_policy")
        return typing.cast(typing.Optional["StorageAccountBlobPropertiesDeleteRetentionPolicy"], result)

    @builtins.property
    def last_access_time_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#last_access_time_enabled StorageAccount#last_access_time_enabled}.'''
        result = self._values.get("last_access_time_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def versioning_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#versioning_enabled StorageAccount#versioning_enabled}.'''
        result = self._values.get("versioning_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountBlobProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobPropertiesContainerDeleteRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={"days": "days"},
)
class StorageAccountBlobPropertiesContainerDeleteRetentionPolicy:
    def __init__(self, *, days: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesContainerDeleteRetentionPolicy.__init__)
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[str, typing.Any] = {}
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountBlobPropertiesContainerDeleteRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountBlobPropertiesContainerDeleteRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobPropertiesContainerDeleteRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesContainerDeleteRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesContainerDeleteRetentionPolicyOutputReference, "days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageAccountBlobPropertiesContainerDeleteRetentionPolicy]:
        return typing.cast(typing.Optional[StorageAccountBlobPropertiesContainerDeleteRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountBlobPropertiesContainerDeleteRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesContainerDeleteRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobPropertiesCorsRule",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_headers": "allowedHeaders",
        "allowed_methods": "allowedMethods",
        "allowed_origins": "allowedOrigins",
        "exposed_headers": "exposedHeaders",
        "max_age_in_seconds": "maxAgeInSeconds",
    },
)
class StorageAccountBlobPropertiesCorsRule:
    def __init__(
        self,
        *,
        allowed_headers: typing.Sequence[builtins.str],
        allowed_methods: typing.Sequence[builtins.str],
        allowed_origins: typing.Sequence[builtins.str],
        exposed_headers: typing.Sequence[builtins.str],
        max_age_in_seconds: jsii.Number,
    ) -> None:
        '''
        :param allowed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_headers StorageAccount#allowed_headers}.
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_methods StorageAccount#allowed_methods}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_origins StorageAccount#allowed_origins}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#exposed_headers StorageAccount#exposed_headers}.
        :param max_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#max_age_in_seconds StorageAccount#max_age_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesCorsRule.__init__)
            check_type(argname="argument allowed_headers", value=allowed_headers, expected_type=type_hints["allowed_headers"])
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument exposed_headers", value=exposed_headers, expected_type=type_hints["exposed_headers"])
            check_type(argname="argument max_age_in_seconds", value=max_age_in_seconds, expected_type=type_hints["max_age_in_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_headers": allowed_headers,
            "allowed_methods": allowed_methods,
            "allowed_origins": allowed_origins,
            "exposed_headers": exposed_headers,
            "max_age_in_seconds": max_age_in_seconds,
        }

    @builtins.property
    def allowed_headers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_headers StorageAccount#allowed_headers}.'''
        result = self._values.get("allowed_headers")
        assert result is not None, "Required property 'allowed_headers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_methods StorageAccount#allowed_methods}.'''
        result = self._values.get("allowed_methods")
        assert result is not None, "Required property 'allowed_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_origins StorageAccount#allowed_origins}.'''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def exposed_headers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#exposed_headers StorageAccount#exposed_headers}.'''
        result = self._values.get("exposed_headers")
        assert result is not None, "Required property 'exposed_headers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def max_age_in_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#max_age_in_seconds StorageAccount#max_age_in_seconds}.'''
        result = self._values.get("max_age_in_seconds")
        assert result is not None, "Required property 'max_age_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountBlobPropertiesCorsRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountBlobPropertiesCorsRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobPropertiesCorsRuleList",
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
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesCorsRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageAccountBlobPropertiesCorsRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesCorsRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageAccountBlobPropertiesCorsRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountBlobPropertiesCorsRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountBlobPropertiesCorsRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountBlobPropertiesCorsRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountBlobPropertiesCorsRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobPropertiesCorsRuleOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesCorsRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="allowedHeadersInput")
    def allowed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethodsInput")
    def allowed_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="exposedHeadersInput")
    def exposed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInSecondsInput")
    def max_age_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHeaders")
    def allowed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedHeaders"))

    @allowed_headers.setter
    def allowed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleOutputReference, "allowed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleOutputReference, "allowed_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleOutputReference, "allowed_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="exposedHeaders")
    def exposed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposedHeaders"))

    @exposed_headers.setter
    def exposed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleOutputReference, "exposed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAgeInSeconds"))

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleOutputReference, "max_age_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageAccountBlobPropertiesCorsRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageAccountBlobPropertiesCorsRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageAccountBlobPropertiesCorsRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesCorsRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobPropertiesDeleteRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={"days": "days"},
)
class StorageAccountBlobPropertiesDeleteRetentionPolicy:
    def __init__(self, *, days: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesDeleteRetentionPolicy.__init__)
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[str, typing.Any] = {}
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountBlobPropertiesDeleteRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountBlobPropertiesDeleteRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobPropertiesDeleteRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesDeleteRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesDeleteRetentionPolicyOutputReference, "days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageAccountBlobPropertiesDeleteRetentionPolicy]:
        return typing.cast(typing.Optional[StorageAccountBlobPropertiesDeleteRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountBlobPropertiesDeleteRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesDeleteRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountBlobPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountBlobPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putContainerDeleteRetentionPolicy")
    def put_container_delete_retention_policy(
        self,
        *,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.
        '''
        value = StorageAccountBlobPropertiesContainerDeleteRetentionPolicy(days=days)

        return typing.cast(None, jsii.invoke(self, "putContainerDeleteRetentionPolicy", [value]))

    @jsii.member(jsii_name="putCorsRule")
    def put_cors_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[StorageAccountBlobPropertiesCorsRule, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountBlobPropertiesOutputReference.put_cors_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCorsRule", [value]))

    @jsii.member(jsii_name="putDeleteRetentionPolicy")
    def put_delete_retention_policy(
        self,
        *,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.
        '''
        value = StorageAccountBlobPropertiesDeleteRetentionPolicy(days=days)

        return typing.cast(None, jsii.invoke(self, "putDeleteRetentionPolicy", [value]))

    @jsii.member(jsii_name="resetChangeFeedEnabled")
    def reset_change_feed_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeFeedEnabled", []))

    @jsii.member(jsii_name="resetChangeFeedRetentionInDays")
    def reset_change_feed_retention_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeFeedRetentionInDays", []))

    @jsii.member(jsii_name="resetContainerDeleteRetentionPolicy")
    def reset_container_delete_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerDeleteRetentionPolicy", []))

    @jsii.member(jsii_name="resetCorsRule")
    def reset_cors_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsRule", []))

    @jsii.member(jsii_name="resetDefaultServiceVersion")
    def reset_default_service_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultServiceVersion", []))

    @jsii.member(jsii_name="resetDeleteRetentionPolicy")
    def reset_delete_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteRetentionPolicy", []))

    @jsii.member(jsii_name="resetLastAccessTimeEnabled")
    def reset_last_access_time_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastAccessTimeEnabled", []))

    @jsii.member(jsii_name="resetVersioningEnabled")
    def reset_versioning_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersioningEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="containerDeleteRetentionPolicy")
    def container_delete_retention_policy(
        self,
    ) -> StorageAccountBlobPropertiesContainerDeleteRetentionPolicyOutputReference:
        return typing.cast(StorageAccountBlobPropertiesContainerDeleteRetentionPolicyOutputReference, jsii.get(self, "containerDeleteRetentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="corsRule")
    def cors_rule(self) -> StorageAccountBlobPropertiesCorsRuleList:
        return typing.cast(StorageAccountBlobPropertiesCorsRuleList, jsii.get(self, "corsRule"))

    @builtins.property
    @jsii.member(jsii_name="deleteRetentionPolicy")
    def delete_retention_policy(
        self,
    ) -> StorageAccountBlobPropertiesDeleteRetentionPolicyOutputReference:
        return typing.cast(StorageAccountBlobPropertiesDeleteRetentionPolicyOutputReference, jsii.get(self, "deleteRetentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="changeFeedEnabledInput")
    def change_feed_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "changeFeedEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="changeFeedRetentionInDaysInput")
    def change_feed_retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "changeFeedRetentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="containerDeleteRetentionPolicyInput")
    def container_delete_retention_policy_input(
        self,
    ) -> typing.Optional[StorageAccountBlobPropertiesContainerDeleteRetentionPolicy]:
        return typing.cast(typing.Optional[StorageAccountBlobPropertiesContainerDeleteRetentionPolicy], jsii.get(self, "containerDeleteRetentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="corsRuleInput")
    def cors_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountBlobPropertiesCorsRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountBlobPropertiesCorsRule]]], jsii.get(self, "corsRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultServiceVersionInput")
    def default_service_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultServiceVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteRetentionPolicyInput")
    def delete_retention_policy_input(
        self,
    ) -> typing.Optional[StorageAccountBlobPropertiesDeleteRetentionPolicy]:
        return typing.cast(typing.Optional[StorageAccountBlobPropertiesDeleteRetentionPolicy], jsii.get(self, "deleteRetentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="lastAccessTimeEnabledInput")
    def last_access_time_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "lastAccessTimeEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="versioningEnabledInput")
    def versioning_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "versioningEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="changeFeedEnabled")
    def change_feed_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "changeFeedEnabled"))

    @change_feed_enabled.setter
    def change_feed_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesOutputReference, "change_feed_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeFeedEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="changeFeedRetentionInDays")
    def change_feed_retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "changeFeedRetentionInDays"))

    @change_feed_retention_in_days.setter
    def change_feed_retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesOutputReference, "change_feed_retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeFeedRetentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="defaultServiceVersion")
    def default_service_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultServiceVersion"))

    @default_service_version.setter
    def default_service_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesOutputReference, "default_service_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultServiceVersion", value)

    @builtins.property
    @jsii.member(jsii_name="lastAccessTimeEnabled")
    def last_access_time_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "lastAccessTimeEnabled"))

    @last_access_time_enabled.setter
    def last_access_time_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesOutputReference, "last_access_time_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastAccessTimeEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="versioningEnabled")
    def versioning_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "versioningEnabled"))

    @versioning_enabled.setter
    def versioning_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesOutputReference, "versioning_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versioningEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountBlobProperties]:
        return typing.cast(typing.Optional[StorageAccountBlobProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountBlobProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountBlobPropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_replication_type": "accountReplicationType",
        "account_tier": "accountTier",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "access_tier": "accessTier",
        "account_kind": "accountKind",
        "allow_nested_items_to_be_public": "allowNestedItemsToBePublic",
        "azure_files_authentication": "azureFilesAuthentication",
        "blob_properties": "blobProperties",
        "cross_tenant_replication_enabled": "crossTenantReplicationEnabled",
        "custom_domain": "customDomain",
        "customer_managed_key": "customerManagedKey",
        "default_to_oauth_authentication": "defaultToOauthAuthentication",
        "edge_zone": "edgeZone",
        "enable_https_traffic_only": "enableHttpsTrafficOnly",
        "id": "id",
        "identity": "identity",
        "infrastructure_encryption_enabled": "infrastructureEncryptionEnabled",
        "is_hns_enabled": "isHnsEnabled",
        "large_file_share_enabled": "largeFileShareEnabled",
        "min_tls_version": "minTlsVersion",
        "network_rules": "networkRules",
        "nfsv3_enabled": "nfsv3Enabled",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "queue_encryption_key_type": "queueEncryptionKeyType",
        "queue_properties": "queueProperties",
        "routing": "routing",
        "shared_access_key_enabled": "sharedAccessKeyEnabled",
        "share_properties": "shareProperties",
        "static_website": "staticWebsite",
        "table_encryption_key_type": "tableEncryptionKeyType",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class StorageAccountConfig(cdktf.TerraformMetaArguments):
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
        account_replication_type: builtins.str,
        account_tier: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        access_tier: typing.Optional[builtins.str] = None,
        account_kind: typing.Optional[builtins.str] = None,
        allow_nested_items_to_be_public: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        azure_files_authentication: typing.Optional[typing.Union[StorageAccountAzureFilesAuthentication, typing.Dict[str, typing.Any]]] = None,
        blob_properties: typing.Optional[typing.Union[StorageAccountBlobProperties, typing.Dict[str, typing.Any]]] = None,
        cross_tenant_replication_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_domain: typing.Optional[typing.Union["StorageAccountCustomDomain", typing.Dict[str, typing.Any]]] = None,
        customer_managed_key: typing.Optional[typing.Union["StorageAccountCustomerManagedKey", typing.Dict[str, typing.Any]]] = None,
        default_to_oauth_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        enable_https_traffic_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["StorageAccountIdentity", typing.Dict[str, typing.Any]]] = None,
        infrastructure_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_hns_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        large_file_share_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        min_tls_version: typing.Optional[builtins.str] = None,
        network_rules: typing.Optional[typing.Union["StorageAccountNetworkRules", typing.Dict[str, typing.Any]]] = None,
        nfsv3_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        queue_encryption_key_type: typing.Optional[builtins.str] = None,
        queue_properties: typing.Optional[typing.Union["StorageAccountQueueProperties", typing.Dict[str, typing.Any]]] = None,
        routing: typing.Optional[typing.Union["StorageAccountRouting", typing.Dict[str, typing.Any]]] = None,
        shared_access_key_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        share_properties: typing.Optional[typing.Union["StorageAccountShareProperties", typing.Dict[str, typing.Any]]] = None,
        static_website: typing.Optional[typing.Union["StorageAccountStaticWebsite", typing.Dict[str, typing.Any]]] = None,
        table_encryption_key_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StorageAccountTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_replication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_replication_type StorageAccount#account_replication_type}.
        :param account_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_tier StorageAccount#account_tier}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#location StorageAccount#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#name StorageAccount#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#resource_group_name StorageAccount#resource_group_name}.
        :param access_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#access_tier StorageAccount#access_tier}.
        :param account_kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_kind StorageAccount#account_kind}.
        :param allow_nested_items_to_be_public: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allow_nested_items_to_be_public StorageAccount#allow_nested_items_to_be_public}.
        :param azure_files_authentication: azure_files_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#azure_files_authentication StorageAccount#azure_files_authentication}
        :param blob_properties: blob_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#blob_properties StorageAccount#blob_properties}
        :param cross_tenant_replication_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cross_tenant_replication_enabled StorageAccount#cross_tenant_replication_enabled}.
        :param custom_domain: custom_domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#custom_domain StorageAccount#custom_domain}
        :param customer_managed_key: customer_managed_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#customer_managed_key StorageAccount#customer_managed_key}
        :param default_to_oauth_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_to_oauth_authentication StorageAccount#default_to_oauth_authentication}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#edge_zone StorageAccount#edge_zone}.
        :param enable_https_traffic_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enable_https_traffic_only StorageAccount#enable_https_traffic_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#id StorageAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#identity StorageAccount#identity}
        :param infrastructure_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#infrastructure_encryption_enabled StorageAccount#infrastructure_encryption_enabled}.
        :param is_hns_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#is_hns_enabled StorageAccount#is_hns_enabled}.
        :param large_file_share_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#large_file_share_enabled StorageAccount#large_file_share_enabled}.
        :param min_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#min_tls_version StorageAccount#min_tls_version}.
        :param network_rules: network_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#network_rules StorageAccount#network_rules}
        :param nfsv3_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#nfsv3_enabled StorageAccount#nfsv3_enabled}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#public_network_access_enabled StorageAccount#public_network_access_enabled}.
        :param queue_encryption_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#queue_encryption_key_type StorageAccount#queue_encryption_key_type}.
        :param queue_properties: queue_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#queue_properties StorageAccount#queue_properties}
        :param routing: routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#routing StorageAccount#routing}
        :param shared_access_key_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#shared_access_key_enabled StorageAccount#shared_access_key_enabled}.
        :param share_properties: share_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#share_properties StorageAccount#share_properties}
        :param static_website: static_website block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#static_website StorageAccount#static_website}
        :param table_encryption_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#table_encryption_key_type StorageAccount#table_encryption_key_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#tags StorageAccount#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#timeouts StorageAccount#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(azure_files_authentication, dict):
            azure_files_authentication = StorageAccountAzureFilesAuthentication(**azure_files_authentication)
        if isinstance(blob_properties, dict):
            blob_properties = StorageAccountBlobProperties(**blob_properties)
        if isinstance(custom_domain, dict):
            custom_domain = StorageAccountCustomDomain(**custom_domain)
        if isinstance(customer_managed_key, dict):
            customer_managed_key = StorageAccountCustomerManagedKey(**customer_managed_key)
        if isinstance(identity, dict):
            identity = StorageAccountIdentity(**identity)
        if isinstance(network_rules, dict):
            network_rules = StorageAccountNetworkRules(**network_rules)
        if isinstance(queue_properties, dict):
            queue_properties = StorageAccountQueueProperties(**queue_properties)
        if isinstance(routing, dict):
            routing = StorageAccountRouting(**routing)
        if isinstance(share_properties, dict):
            share_properties = StorageAccountShareProperties(**share_properties)
        if isinstance(static_website, dict):
            static_website = StorageAccountStaticWebsite(**static_website)
        if isinstance(timeouts, dict):
            timeouts = StorageAccountTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_replication_type", value=account_replication_type, expected_type=type_hints["account_replication_type"])
            check_type(argname="argument account_tier", value=account_tier, expected_type=type_hints["account_tier"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument access_tier", value=access_tier, expected_type=type_hints["access_tier"])
            check_type(argname="argument account_kind", value=account_kind, expected_type=type_hints["account_kind"])
            check_type(argname="argument allow_nested_items_to_be_public", value=allow_nested_items_to_be_public, expected_type=type_hints["allow_nested_items_to_be_public"])
            check_type(argname="argument azure_files_authentication", value=azure_files_authentication, expected_type=type_hints["azure_files_authentication"])
            check_type(argname="argument blob_properties", value=blob_properties, expected_type=type_hints["blob_properties"])
            check_type(argname="argument cross_tenant_replication_enabled", value=cross_tenant_replication_enabled, expected_type=type_hints["cross_tenant_replication_enabled"])
            check_type(argname="argument custom_domain", value=custom_domain, expected_type=type_hints["custom_domain"])
            check_type(argname="argument customer_managed_key", value=customer_managed_key, expected_type=type_hints["customer_managed_key"])
            check_type(argname="argument default_to_oauth_authentication", value=default_to_oauth_authentication, expected_type=type_hints["default_to_oauth_authentication"])
            check_type(argname="argument edge_zone", value=edge_zone, expected_type=type_hints["edge_zone"])
            check_type(argname="argument enable_https_traffic_only", value=enable_https_traffic_only, expected_type=type_hints["enable_https_traffic_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument infrastructure_encryption_enabled", value=infrastructure_encryption_enabled, expected_type=type_hints["infrastructure_encryption_enabled"])
            check_type(argname="argument is_hns_enabled", value=is_hns_enabled, expected_type=type_hints["is_hns_enabled"])
            check_type(argname="argument large_file_share_enabled", value=large_file_share_enabled, expected_type=type_hints["large_file_share_enabled"])
            check_type(argname="argument min_tls_version", value=min_tls_version, expected_type=type_hints["min_tls_version"])
            check_type(argname="argument network_rules", value=network_rules, expected_type=type_hints["network_rules"])
            check_type(argname="argument nfsv3_enabled", value=nfsv3_enabled, expected_type=type_hints["nfsv3_enabled"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument queue_encryption_key_type", value=queue_encryption_key_type, expected_type=type_hints["queue_encryption_key_type"])
            check_type(argname="argument queue_properties", value=queue_properties, expected_type=type_hints["queue_properties"])
            check_type(argname="argument routing", value=routing, expected_type=type_hints["routing"])
            check_type(argname="argument shared_access_key_enabled", value=shared_access_key_enabled, expected_type=type_hints["shared_access_key_enabled"])
            check_type(argname="argument share_properties", value=share_properties, expected_type=type_hints["share_properties"])
            check_type(argname="argument static_website", value=static_website, expected_type=type_hints["static_website"])
            check_type(argname="argument table_encryption_key_type", value=table_encryption_key_type, expected_type=type_hints["table_encryption_key_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_replication_type": account_replication_type,
            "account_tier": account_tier,
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
        if access_tier is not None:
            self._values["access_tier"] = access_tier
        if account_kind is not None:
            self._values["account_kind"] = account_kind
        if allow_nested_items_to_be_public is not None:
            self._values["allow_nested_items_to_be_public"] = allow_nested_items_to_be_public
        if azure_files_authentication is not None:
            self._values["azure_files_authentication"] = azure_files_authentication
        if blob_properties is not None:
            self._values["blob_properties"] = blob_properties
        if cross_tenant_replication_enabled is not None:
            self._values["cross_tenant_replication_enabled"] = cross_tenant_replication_enabled
        if custom_domain is not None:
            self._values["custom_domain"] = custom_domain
        if customer_managed_key is not None:
            self._values["customer_managed_key"] = customer_managed_key
        if default_to_oauth_authentication is not None:
            self._values["default_to_oauth_authentication"] = default_to_oauth_authentication
        if edge_zone is not None:
            self._values["edge_zone"] = edge_zone
        if enable_https_traffic_only is not None:
            self._values["enable_https_traffic_only"] = enable_https_traffic_only
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if infrastructure_encryption_enabled is not None:
            self._values["infrastructure_encryption_enabled"] = infrastructure_encryption_enabled
        if is_hns_enabled is not None:
            self._values["is_hns_enabled"] = is_hns_enabled
        if large_file_share_enabled is not None:
            self._values["large_file_share_enabled"] = large_file_share_enabled
        if min_tls_version is not None:
            self._values["min_tls_version"] = min_tls_version
        if network_rules is not None:
            self._values["network_rules"] = network_rules
        if nfsv3_enabled is not None:
            self._values["nfsv3_enabled"] = nfsv3_enabled
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if queue_encryption_key_type is not None:
            self._values["queue_encryption_key_type"] = queue_encryption_key_type
        if queue_properties is not None:
            self._values["queue_properties"] = queue_properties
        if routing is not None:
            self._values["routing"] = routing
        if shared_access_key_enabled is not None:
            self._values["shared_access_key_enabled"] = shared_access_key_enabled
        if share_properties is not None:
            self._values["share_properties"] = share_properties
        if static_website is not None:
            self._values["static_website"] = static_website
        if table_encryption_key_type is not None:
            self._values["table_encryption_key_type"] = table_encryption_key_type
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
    def account_replication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_replication_type StorageAccount#account_replication_type}.'''
        result = self._values.get("account_replication_type")
        assert result is not None, "Required property 'account_replication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_tier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_tier StorageAccount#account_tier}.'''
        result = self._values.get("account_tier")
        assert result is not None, "Required property 'account_tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#location StorageAccount#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#name StorageAccount#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#resource_group_name StorageAccount#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_tier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#access_tier StorageAccount#access_tier}.'''
        result = self._values.get("access_tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_kind(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#account_kind StorageAccount#account_kind}.'''
        result = self._values.get("account_kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allow_nested_items_to_be_public(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allow_nested_items_to_be_public StorageAccount#allow_nested_items_to_be_public}.'''
        result = self._values.get("allow_nested_items_to_be_public")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def azure_files_authentication(
        self,
    ) -> typing.Optional[StorageAccountAzureFilesAuthentication]:
        '''azure_files_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#azure_files_authentication StorageAccount#azure_files_authentication}
        '''
        result = self._values.get("azure_files_authentication")
        return typing.cast(typing.Optional[StorageAccountAzureFilesAuthentication], result)

    @builtins.property
    def blob_properties(self) -> typing.Optional[StorageAccountBlobProperties]:
        '''blob_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#blob_properties StorageAccount#blob_properties}
        '''
        result = self._values.get("blob_properties")
        return typing.cast(typing.Optional[StorageAccountBlobProperties], result)

    @builtins.property
    def cross_tenant_replication_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cross_tenant_replication_enabled StorageAccount#cross_tenant_replication_enabled}.'''
        result = self._values.get("cross_tenant_replication_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_domain(self) -> typing.Optional["StorageAccountCustomDomain"]:
        '''custom_domain block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#custom_domain StorageAccount#custom_domain}
        '''
        result = self._values.get("custom_domain")
        return typing.cast(typing.Optional["StorageAccountCustomDomain"], result)

    @builtins.property
    def customer_managed_key(
        self,
    ) -> typing.Optional["StorageAccountCustomerManagedKey"]:
        '''customer_managed_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#customer_managed_key StorageAccount#customer_managed_key}
        '''
        result = self._values.get("customer_managed_key")
        return typing.cast(typing.Optional["StorageAccountCustomerManagedKey"], result)

    @builtins.property
    def default_to_oauth_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_to_oauth_authentication StorageAccount#default_to_oauth_authentication}.'''
        result = self._values.get("default_to_oauth_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def edge_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#edge_zone StorageAccount#edge_zone}.'''
        result = self._values.get("edge_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_https_traffic_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enable_https_traffic_only StorageAccount#enable_https_traffic_only}.'''
        result = self._values.get("enable_https_traffic_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#id StorageAccount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["StorageAccountIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#identity StorageAccount#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["StorageAccountIdentity"], result)

    @builtins.property
    def infrastructure_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#infrastructure_encryption_enabled StorageAccount#infrastructure_encryption_enabled}.'''
        result = self._values.get("infrastructure_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_hns_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#is_hns_enabled StorageAccount#is_hns_enabled}.'''
        result = self._values.get("is_hns_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def large_file_share_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#large_file_share_enabled StorageAccount#large_file_share_enabled}.'''
        result = self._values.get("large_file_share_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def min_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#min_tls_version StorageAccount#min_tls_version}.'''
        result = self._values.get("min_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_rules(self) -> typing.Optional["StorageAccountNetworkRules"]:
        '''network_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#network_rules StorageAccount#network_rules}
        '''
        result = self._values.get("network_rules")
        return typing.cast(typing.Optional["StorageAccountNetworkRules"], result)

    @builtins.property
    def nfsv3_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#nfsv3_enabled StorageAccount#nfsv3_enabled}.'''
        result = self._values.get("nfsv3_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#public_network_access_enabled StorageAccount#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def queue_encryption_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#queue_encryption_key_type StorageAccount#queue_encryption_key_type}.'''
        result = self._values.get("queue_encryption_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queue_properties(self) -> typing.Optional["StorageAccountQueueProperties"]:
        '''queue_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#queue_properties StorageAccount#queue_properties}
        '''
        result = self._values.get("queue_properties")
        return typing.cast(typing.Optional["StorageAccountQueueProperties"], result)

    @builtins.property
    def routing(self) -> typing.Optional["StorageAccountRouting"]:
        '''routing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#routing StorageAccount#routing}
        '''
        result = self._values.get("routing")
        return typing.cast(typing.Optional["StorageAccountRouting"], result)

    @builtins.property
    def shared_access_key_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#shared_access_key_enabled StorageAccount#shared_access_key_enabled}.'''
        result = self._values.get("shared_access_key_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def share_properties(self) -> typing.Optional["StorageAccountShareProperties"]:
        '''share_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#share_properties StorageAccount#share_properties}
        '''
        result = self._values.get("share_properties")
        return typing.cast(typing.Optional["StorageAccountShareProperties"], result)

    @builtins.property
    def static_website(self) -> typing.Optional["StorageAccountStaticWebsite"]:
        '''static_website block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#static_website StorageAccount#static_website}
        '''
        result = self._values.get("static_website")
        return typing.cast(typing.Optional["StorageAccountStaticWebsite"], result)

    @builtins.property
    def table_encryption_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#table_encryption_key_type StorageAccount#table_encryption_key_type}.'''
        result = self._values.get("table_encryption_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#tags StorageAccount#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StorageAccountTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#timeouts StorageAccount#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StorageAccountTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountCustomDomain",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "use_subdomain": "useSubdomain"},
)
class StorageAccountCustomDomain:
    def __init__(
        self,
        *,
        name: builtins.str,
        use_subdomain: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#name StorageAccount#name}.
        :param use_subdomain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#use_subdomain StorageAccount#use_subdomain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountCustomDomain.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument use_subdomain", value=use_subdomain, expected_type=type_hints["use_subdomain"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if use_subdomain is not None:
            self._values["use_subdomain"] = use_subdomain

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#name StorageAccount#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_subdomain(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#use_subdomain StorageAccount#use_subdomain}.'''
        result = self._values.get("use_subdomain")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountCustomDomain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountCustomDomainOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountCustomDomainOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountCustomDomainOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUseSubdomain")
    def reset_use_subdomain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseSubdomain", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="useSubdomainInput")
    def use_subdomain_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useSubdomainInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountCustomDomainOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="useSubdomain")
    def use_subdomain(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useSubdomain"))

    @use_subdomain.setter
    def use_subdomain(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountCustomDomainOutputReference, "use_subdomain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useSubdomain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountCustomDomain]:
        return typing.cast(typing.Optional[StorageAccountCustomDomain], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountCustomDomain],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountCustomDomainOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountCustomerManagedKey",
    jsii_struct_bases=[],
    name_mapping={
        "key_vault_key_id": "keyVaultKeyId",
        "user_assigned_identity_id": "userAssignedIdentityId",
    },
)
class StorageAccountCustomerManagedKey:
    def __init__(
        self,
        *,
        key_vault_key_id: builtins.str,
        user_assigned_identity_id: builtins.str,
    ) -> None:
        '''
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#key_vault_key_id StorageAccount#key_vault_key_id}.
        :param user_assigned_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#user_assigned_identity_id StorageAccount#user_assigned_identity_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountCustomerManagedKey.__init__)
            check_type(argname="argument key_vault_key_id", value=key_vault_key_id, expected_type=type_hints["key_vault_key_id"])
            check_type(argname="argument user_assigned_identity_id", value=user_assigned_identity_id, expected_type=type_hints["user_assigned_identity_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_vault_key_id": key_vault_key_id,
            "user_assigned_identity_id": user_assigned_identity_id,
        }

    @builtins.property
    def key_vault_key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#key_vault_key_id StorageAccount#key_vault_key_id}.'''
        result = self._values.get("key_vault_key_id")
        assert result is not None, "Required property 'key_vault_key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_assigned_identity_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#user_assigned_identity_id StorageAccount#user_assigned_identity_id}.'''
        result = self._values.get("user_assigned_identity_id")
        assert result is not None, "Required property 'user_assigned_identity_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountCustomerManagedKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountCustomerManagedKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountCustomerManagedKeyOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountCustomerManagedKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyIdInput")
    def key_vault_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityIdInput")
    def user_assigned_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAssignedIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyId")
    def key_vault_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultKeyId"))

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountCustomerManagedKeyOutputReference, "key_vault_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @user_assigned_identity_id.setter
    def user_assigned_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountCustomerManagedKeyOutputReference, "user_assigned_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountCustomerManagedKey]:
        return typing.cast(typing.Optional[StorageAccountCustomerManagedKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountCustomerManagedKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountCustomerManagedKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class StorageAccountIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#type StorageAccount#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#identity_ids StorageAccount#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#type StorageAccount#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#identity_ids StorageAccount#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountIdentityOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountIdentity]:
        return typing.cast(typing.Optional[StorageAccountIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[StorageAccountIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountNetworkRules",
    jsii_struct_bases=[],
    name_mapping={
        "default_action": "defaultAction",
        "bypass": "bypass",
        "ip_rules": "ipRules",
        "private_link_access": "privateLinkAccess",
        "virtual_network_subnet_ids": "virtualNetworkSubnetIds",
    },
)
class StorageAccountNetworkRules:
    def __init__(
        self,
        *,
        default_action: builtins.str,
        bypass: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_link_access: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountNetworkRulesPrivateLinkAccess", typing.Dict[str, typing.Any]]]]] = None,
        virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_action StorageAccount#default_action}.
        :param bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#bypass StorageAccount#bypass}.
        :param ip_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#ip_rules StorageAccount#ip_rules}.
        :param private_link_access: private_link_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#private_link_access StorageAccount#private_link_access}
        :param virtual_network_subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#virtual_network_subnet_ids StorageAccount#virtual_network_subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRules.__init__)
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument bypass", value=bypass, expected_type=type_hints["bypass"])
            check_type(argname="argument ip_rules", value=ip_rules, expected_type=type_hints["ip_rules"])
            check_type(argname="argument private_link_access", value=private_link_access, expected_type=type_hints["private_link_access"])
            check_type(argname="argument virtual_network_subnet_ids", value=virtual_network_subnet_ids, expected_type=type_hints["virtual_network_subnet_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_action": default_action,
        }
        if bypass is not None:
            self._values["bypass"] = bypass
        if ip_rules is not None:
            self._values["ip_rules"] = ip_rules
        if private_link_access is not None:
            self._values["private_link_access"] = private_link_access
        if virtual_network_subnet_ids is not None:
            self._values["virtual_network_subnet_ids"] = virtual_network_subnet_ids

    @builtins.property
    def default_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#default_action StorageAccount#default_action}.'''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bypass(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#bypass StorageAccount#bypass}.'''
        result = self._values.get("bypass")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_rules(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#ip_rules StorageAccount#ip_rules}.'''
        result = self._values.get("ip_rules")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_link_access(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountNetworkRulesPrivateLinkAccess"]]]:
        '''private_link_access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#private_link_access StorageAccount#private_link_access}
        '''
        result = self._values.get("private_link_access")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountNetworkRulesPrivateLinkAccess"]]], result)

    @builtins.property
    def virtual_network_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#virtual_network_subnet_ids StorageAccount#virtual_network_subnet_ids}.'''
        result = self._values.get("virtual_network_subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountNetworkRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountNetworkRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountNetworkRulesOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPrivateLinkAccess")
    def put_private_link_access(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountNetworkRulesPrivateLinkAccess", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesOutputReference.put_private_link_access)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPrivateLinkAccess", [value]))

    @jsii.member(jsii_name="resetBypass")
    def reset_bypass(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBypass", []))

    @jsii.member(jsii_name="resetIpRules")
    def reset_ip_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRules", []))

    @jsii.member(jsii_name="resetPrivateLinkAccess")
    def reset_private_link_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkAccess", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetIds")
    def reset_virtual_network_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetIds", []))

    @builtins.property
    @jsii.member(jsii_name="privateLinkAccess")
    def private_link_access(self) -> "StorageAccountNetworkRulesPrivateLinkAccessList":
        return typing.cast("StorageAccountNetworkRulesPrivateLinkAccessList", jsii.get(self, "privateLinkAccess"))

    @builtins.property
    @jsii.member(jsii_name="bypassInput")
    def bypass_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bypassInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRulesInput")
    def ip_rules_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkAccessInput")
    def private_link_access_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountNetworkRulesPrivateLinkAccess"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountNetworkRulesPrivateLinkAccess"]]], jsii.get(self, "privateLinkAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdsInput")
    def virtual_network_subnet_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "virtualNetworkSubnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bypass")
    def bypass(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "bypass"))

    @bypass.setter
    def bypass(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesOutputReference, "bypass").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypass", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesOutputReference, "default_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="ipRules")
    def ip_rules(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipRules"))

    @ip_rules.setter
    def ip_rules(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesOutputReference, "ip_rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRules", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIds")
    def virtual_network_subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "virtualNetworkSubnetIds"))

    @virtual_network_subnet_ids.setter
    def virtual_network_subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesOutputReference, "virtual_network_subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountNetworkRules]:
        return typing.cast(typing.Optional[StorageAccountNetworkRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountNetworkRules],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountNetworkRulesPrivateLinkAccess",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_resource_id": "endpointResourceId",
        "endpoint_tenant_id": "endpointTenantId",
    },
)
class StorageAccountNetworkRulesPrivateLinkAccess:
    def __init__(
        self,
        *,
        endpoint_resource_id: builtins.str,
        endpoint_tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#endpoint_resource_id StorageAccount#endpoint_resource_id}.
        :param endpoint_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#endpoint_tenant_id StorageAccount#endpoint_tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesPrivateLinkAccess.__init__)
            check_type(argname="argument endpoint_resource_id", value=endpoint_resource_id, expected_type=type_hints["endpoint_resource_id"])
            check_type(argname="argument endpoint_tenant_id", value=endpoint_tenant_id, expected_type=type_hints["endpoint_tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_resource_id": endpoint_resource_id,
        }
        if endpoint_tenant_id is not None:
            self._values["endpoint_tenant_id"] = endpoint_tenant_id

    @builtins.property
    def endpoint_resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#endpoint_resource_id StorageAccount#endpoint_resource_id}.'''
        result = self._values.get("endpoint_resource_id")
        assert result is not None, "Required property 'endpoint_resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#endpoint_tenant_id StorageAccount#endpoint_tenant_id}.'''
        result = self._values.get("endpoint_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountNetworkRulesPrivateLinkAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountNetworkRulesPrivateLinkAccessList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountNetworkRulesPrivateLinkAccessList",
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
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesPrivateLinkAccessList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageAccountNetworkRulesPrivateLinkAccessOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesPrivateLinkAccessList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageAccountNetworkRulesPrivateLinkAccessOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountNetworkRulesPrivateLinkAccess]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountNetworkRulesPrivateLinkAccess]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountNetworkRulesPrivateLinkAccess]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountNetworkRulesPrivateLinkAccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountNetworkRulesPrivateLinkAccessOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountNetworkRulesPrivateLinkAccessOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEndpointTenantId")
    def reset_endpoint_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="endpointResourceIdInput")
    def endpoint_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointTenantIdInput")
    def endpoint_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointResourceId")
    def endpoint_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointResourceId"))

    @endpoint_resource_id.setter
    def endpoint_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessOutputReference, "endpoint_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="endpointTenantId")
    def endpoint_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointTenantId"))

    @endpoint_tenant_id.setter
    def endpoint_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessOutputReference, "endpoint_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageAccountNetworkRulesPrivateLinkAccess, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageAccountNetworkRulesPrivateLinkAccess, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageAccountNetworkRulesPrivateLinkAccess, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountNetworkRulesPrivateLinkAccessOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueueProperties",
    jsii_struct_bases=[],
    name_mapping={
        "cors_rule": "corsRule",
        "hour_metrics": "hourMetrics",
        "logging": "logging",
        "minute_metrics": "minuteMetrics",
    },
)
class StorageAccountQueueProperties:
    def __init__(
        self,
        *,
        cors_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountQueuePropertiesCorsRule", typing.Dict[str, typing.Any]]]]] = None,
        hour_metrics: typing.Optional[typing.Union["StorageAccountQueuePropertiesHourMetrics", typing.Dict[str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["StorageAccountQueuePropertiesLogging", typing.Dict[str, typing.Any]]] = None,
        minute_metrics: typing.Optional[typing.Union["StorageAccountQueuePropertiesMinuteMetrics", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        :param hour_metrics: hour_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#hour_metrics StorageAccount#hour_metrics}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#logging StorageAccount#logging}
        :param minute_metrics: minute_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#minute_metrics StorageAccount#minute_metrics}
        '''
        if isinstance(hour_metrics, dict):
            hour_metrics = StorageAccountQueuePropertiesHourMetrics(**hour_metrics)
        if isinstance(logging, dict):
            logging = StorageAccountQueuePropertiesLogging(**logging)
        if isinstance(minute_metrics, dict):
            minute_metrics = StorageAccountQueuePropertiesMinuteMetrics(**minute_metrics)
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountQueueProperties.__init__)
            check_type(argname="argument cors_rule", value=cors_rule, expected_type=type_hints["cors_rule"])
            check_type(argname="argument hour_metrics", value=hour_metrics, expected_type=type_hints["hour_metrics"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument minute_metrics", value=minute_metrics, expected_type=type_hints["minute_metrics"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cors_rule is not None:
            self._values["cors_rule"] = cors_rule
        if hour_metrics is not None:
            self._values["hour_metrics"] = hour_metrics
        if logging is not None:
            self._values["logging"] = logging
        if minute_metrics is not None:
            self._values["minute_metrics"] = minute_metrics

    @builtins.property
    def cors_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountQueuePropertiesCorsRule"]]]:
        '''cors_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        '''
        result = self._values.get("cors_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountQueuePropertiesCorsRule"]]], result)

    @builtins.property
    def hour_metrics(
        self,
    ) -> typing.Optional["StorageAccountQueuePropertiesHourMetrics"]:
        '''hour_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#hour_metrics StorageAccount#hour_metrics}
        '''
        result = self._values.get("hour_metrics")
        return typing.cast(typing.Optional["StorageAccountQueuePropertiesHourMetrics"], result)

    @builtins.property
    def logging(self) -> typing.Optional["StorageAccountQueuePropertiesLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#logging StorageAccount#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["StorageAccountQueuePropertiesLogging"], result)

    @builtins.property
    def minute_metrics(
        self,
    ) -> typing.Optional["StorageAccountQueuePropertiesMinuteMetrics"]:
        '''minute_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#minute_metrics StorageAccount#minute_metrics}
        '''
        result = self._values.get("minute_metrics")
        return typing.cast(typing.Optional["StorageAccountQueuePropertiesMinuteMetrics"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountQueueProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesCorsRule",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_headers": "allowedHeaders",
        "allowed_methods": "allowedMethods",
        "allowed_origins": "allowedOrigins",
        "exposed_headers": "exposedHeaders",
        "max_age_in_seconds": "maxAgeInSeconds",
    },
)
class StorageAccountQueuePropertiesCorsRule:
    def __init__(
        self,
        *,
        allowed_headers: typing.Sequence[builtins.str],
        allowed_methods: typing.Sequence[builtins.str],
        allowed_origins: typing.Sequence[builtins.str],
        exposed_headers: typing.Sequence[builtins.str],
        max_age_in_seconds: jsii.Number,
    ) -> None:
        '''
        :param allowed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_headers StorageAccount#allowed_headers}.
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_methods StorageAccount#allowed_methods}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_origins StorageAccount#allowed_origins}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#exposed_headers StorageAccount#exposed_headers}.
        :param max_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#max_age_in_seconds StorageAccount#max_age_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesCorsRule.__init__)
            check_type(argname="argument allowed_headers", value=allowed_headers, expected_type=type_hints["allowed_headers"])
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument exposed_headers", value=exposed_headers, expected_type=type_hints["exposed_headers"])
            check_type(argname="argument max_age_in_seconds", value=max_age_in_seconds, expected_type=type_hints["max_age_in_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_headers": allowed_headers,
            "allowed_methods": allowed_methods,
            "allowed_origins": allowed_origins,
            "exposed_headers": exposed_headers,
            "max_age_in_seconds": max_age_in_seconds,
        }

    @builtins.property
    def allowed_headers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_headers StorageAccount#allowed_headers}.'''
        result = self._values.get("allowed_headers")
        assert result is not None, "Required property 'allowed_headers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_methods StorageAccount#allowed_methods}.'''
        result = self._values.get("allowed_methods")
        assert result is not None, "Required property 'allowed_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_origins StorageAccount#allowed_origins}.'''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def exposed_headers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#exposed_headers StorageAccount#exposed_headers}.'''
        result = self._values.get("exposed_headers")
        assert result is not None, "Required property 'exposed_headers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def max_age_in_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#max_age_in_seconds StorageAccount#max_age_in_seconds}.'''
        result = self._values.get("max_age_in_seconds")
        assert result is not None, "Required property 'max_age_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountQueuePropertiesCorsRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountQueuePropertiesCorsRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesCorsRuleList",
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
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesCorsRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageAccountQueuePropertiesCorsRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesCorsRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageAccountQueuePropertiesCorsRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountQueuePropertiesCorsRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountQueuePropertiesCorsRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountQueuePropertiesCorsRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountQueuePropertiesCorsRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesCorsRuleOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesCorsRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="allowedHeadersInput")
    def allowed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethodsInput")
    def allowed_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="exposedHeadersInput")
    def exposed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInSecondsInput")
    def max_age_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHeaders")
    def allowed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedHeaders"))

    @allowed_headers.setter
    def allowed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleOutputReference, "allowed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleOutputReference, "allowed_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleOutputReference, "allowed_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="exposedHeaders")
    def exposed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposedHeaders"))

    @exposed_headers.setter
    def exposed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleOutputReference, "exposed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAgeInSeconds"))

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleOutputReference, "max_age_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageAccountQueuePropertiesCorsRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageAccountQueuePropertiesCorsRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageAccountQueuePropertiesCorsRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesCorsRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesHourMetrics",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "version": "version",
        "include_apis": "includeApis",
        "retention_policy_days": "retentionPolicyDays",
    },
)
class StorageAccountQueuePropertiesHourMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        version: builtins.str,
        include_apis: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_policy_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enabled StorageAccount#enabled}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.
        :param include_apis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#include_apis StorageAccount#include_apis}.
        :param retention_policy_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesHourMetrics.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument include_apis", value=include_apis, expected_type=type_hints["include_apis"])
            check_type(argname="argument retention_policy_days", value=retention_policy_days, expected_type=type_hints["retention_policy_days"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
            "version": version,
        }
        if include_apis is not None:
            self._values["include_apis"] = include_apis
        if retention_policy_days is not None:
            self._values["retention_policy_days"] = retention_policy_days

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enabled StorageAccount#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_apis(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#include_apis StorageAccount#include_apis}.'''
        result = self._values.get("include_apis")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_policy_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.'''
        result = self._values.get("retention_policy_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountQueuePropertiesHourMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountQueuePropertiesHourMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesHourMetricsOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesHourMetricsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeApis")
    def reset_include_apis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeApis", []))

    @jsii.member(jsii_name="resetRetentionPolicyDays")
    def reset_retention_policy_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicyDays", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="includeApisInput")
    def include_apis_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeApisInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyDaysInput")
    def retention_policy_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPolicyDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesHourMetricsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="includeApis")
    def include_apis(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeApis"))

    @include_apis.setter
    def include_apis(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesHourMetricsOutputReference, "include_apis").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeApis", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyDays")
    def retention_policy_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPolicyDays"))

    @retention_policy_days.setter
    def retention_policy_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesHourMetricsOutputReference, "retention_policy_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPolicyDays", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesHourMetricsOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageAccountQueuePropertiesHourMetrics]:
        return typing.cast(typing.Optional[StorageAccountQueuePropertiesHourMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountQueuePropertiesHourMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesHourMetricsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesLogging",
    jsii_struct_bases=[],
    name_mapping={
        "delete": "delete",
        "read": "read",
        "version": "version",
        "write": "write",
        "retention_policy_days": "retentionPolicyDays",
    },
)
class StorageAccountQueuePropertiesLogging:
    def __init__(
        self,
        *,
        delete: typing.Union[builtins.bool, cdktf.IResolvable],
        read: typing.Union[builtins.bool, cdktf.IResolvable],
        version: builtins.str,
        write: typing.Union[builtins.bool, cdktf.IResolvable],
        retention_policy_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete StorageAccount#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#read StorageAccount#read}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.
        :param write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#write StorageAccount#write}.
        :param retention_policy_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesLogging.__init__)
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument write", value=write, expected_type=type_hints["write"])
            check_type(argname="argument retention_policy_days", value=retention_policy_days, expected_type=type_hints["retention_policy_days"])
        self._values: typing.Dict[str, typing.Any] = {
            "delete": delete,
            "read": read,
            "version": version,
            "write": write,
        }
        if retention_policy_days is not None:
            self._values["retention_policy_days"] = retention_policy_days

    @builtins.property
    def delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete StorageAccount#delete}.'''
        result = self._values.get("delete")
        assert result is not None, "Required property 'delete' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def read(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#read StorageAccount#read}.'''
        result = self._values.get("read")
        assert result is not None, "Required property 'read' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def write(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#write StorageAccount#write}.'''
        result = self._values.get("write")
        assert result is not None, "Required property 'write' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def retention_policy_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.'''
        result = self._values.get("retention_policy_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountQueuePropertiesLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountQueuePropertiesLoggingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesLoggingOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesLoggingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRetentionPolicyDays")
    def reset_retention_policy_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicyDays", []))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyDaysInput")
    def retention_policy_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPolicyDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="writeInput")
    def write_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "writeInput"))

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesLoggingOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "read"))

    @read.setter
    def read(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesLoggingOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyDays")
    def retention_policy_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPolicyDays"))

    @retention_policy_days.setter
    def retention_policy_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesLoggingOutputReference, "retention_policy_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPolicyDays", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesLoggingOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="write")
    def write(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "write"))

    @write.setter
    def write(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesLoggingOutputReference, "write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "write", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountQueuePropertiesLogging]:
        return typing.cast(typing.Optional[StorageAccountQueuePropertiesLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountQueuePropertiesLogging],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesLoggingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesMinuteMetrics",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "version": "version",
        "include_apis": "includeApis",
        "retention_policy_days": "retentionPolicyDays",
    },
)
class StorageAccountQueuePropertiesMinuteMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        version: builtins.str,
        include_apis: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_policy_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enabled StorageAccount#enabled}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.
        :param include_apis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#include_apis StorageAccount#include_apis}.
        :param retention_policy_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesMinuteMetrics.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument include_apis", value=include_apis, expected_type=type_hints["include_apis"])
            check_type(argname="argument retention_policy_days", value=retention_policy_days, expected_type=type_hints["retention_policy_days"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
            "version": version,
        }
        if include_apis is not None:
            self._values["include_apis"] = include_apis
        if retention_policy_days is not None:
            self._values["retention_policy_days"] = retention_policy_days

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enabled StorageAccount#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_apis(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#include_apis StorageAccount#include_apis}.'''
        result = self._values.get("include_apis")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_policy_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.'''
        result = self._values.get("retention_policy_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountQueuePropertiesMinuteMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountQueuePropertiesMinuteMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesMinuteMetricsOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesMinuteMetricsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeApis")
    def reset_include_apis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeApis", []))

    @jsii.member(jsii_name="resetRetentionPolicyDays")
    def reset_retention_policy_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicyDays", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="includeApisInput")
    def include_apis_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeApisInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyDaysInput")
    def retention_policy_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPolicyDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesMinuteMetricsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="includeApis")
    def include_apis(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeApis"))

    @include_apis.setter
    def include_apis(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesMinuteMetricsOutputReference, "include_apis").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeApis", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyDays")
    def retention_policy_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPolicyDays"))

    @retention_policy_days.setter
    def retention_policy_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesMinuteMetricsOutputReference, "retention_policy_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPolicyDays", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesMinuteMetricsOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageAccountQueuePropertiesMinuteMetrics]:
        return typing.cast(typing.Optional[StorageAccountQueuePropertiesMinuteMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountQueuePropertiesMinuteMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesMinuteMetricsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountQueuePropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountQueuePropertiesOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCorsRule")
    def put_cors_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[StorageAccountQueuePropertiesCorsRule, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountQueuePropertiesOutputReference.put_cors_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCorsRule", [value]))

    @jsii.member(jsii_name="putHourMetrics")
    def put_hour_metrics(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        version: builtins.str,
        include_apis: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_policy_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enabled StorageAccount#enabled}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.
        :param include_apis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#include_apis StorageAccount#include_apis}.
        :param retention_policy_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.
        '''
        value = StorageAccountQueuePropertiesHourMetrics(
            enabled=enabled,
            version=version,
            include_apis=include_apis,
            retention_policy_days=retention_policy_days,
        )

        return typing.cast(None, jsii.invoke(self, "putHourMetrics", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        delete: typing.Union[builtins.bool, cdktf.IResolvable],
        read: typing.Union[builtins.bool, cdktf.IResolvable],
        version: builtins.str,
        write: typing.Union[builtins.bool, cdktf.IResolvable],
        retention_policy_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete StorageAccount#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#read StorageAccount#read}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.
        :param write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#write StorageAccount#write}.
        :param retention_policy_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.
        '''
        value = StorageAccountQueuePropertiesLogging(
            delete=delete,
            read=read,
            version=version,
            write=write,
            retention_policy_days=retention_policy_days,
        )

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putMinuteMetrics")
    def put_minute_metrics(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        version: builtins.str,
        include_apis: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_policy_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#enabled StorageAccount#enabled}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#version StorageAccount#version}.
        :param include_apis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#include_apis StorageAccount#include_apis}.
        :param retention_policy_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy_days StorageAccount#retention_policy_days}.
        '''
        value = StorageAccountQueuePropertiesMinuteMetrics(
            enabled=enabled,
            version=version,
            include_apis=include_apis,
            retention_policy_days=retention_policy_days,
        )

        return typing.cast(None, jsii.invoke(self, "putMinuteMetrics", [value]))

    @jsii.member(jsii_name="resetCorsRule")
    def reset_cors_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsRule", []))

    @jsii.member(jsii_name="resetHourMetrics")
    def reset_hour_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHourMetrics", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetMinuteMetrics")
    def reset_minute_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinuteMetrics", []))

    @builtins.property
    @jsii.member(jsii_name="corsRule")
    def cors_rule(self) -> StorageAccountQueuePropertiesCorsRuleList:
        return typing.cast(StorageAccountQueuePropertiesCorsRuleList, jsii.get(self, "corsRule"))

    @builtins.property
    @jsii.member(jsii_name="hourMetrics")
    def hour_metrics(self) -> StorageAccountQueuePropertiesHourMetricsOutputReference:
        return typing.cast(StorageAccountQueuePropertiesHourMetricsOutputReference, jsii.get(self, "hourMetrics"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> StorageAccountQueuePropertiesLoggingOutputReference:
        return typing.cast(StorageAccountQueuePropertiesLoggingOutputReference, jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="minuteMetrics")
    def minute_metrics(
        self,
    ) -> StorageAccountQueuePropertiesMinuteMetricsOutputReference:
        return typing.cast(StorageAccountQueuePropertiesMinuteMetricsOutputReference, jsii.get(self, "minuteMetrics"))

    @builtins.property
    @jsii.member(jsii_name="corsRuleInput")
    def cors_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountQueuePropertiesCorsRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountQueuePropertiesCorsRule]]], jsii.get(self, "corsRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="hourMetricsInput")
    def hour_metrics_input(
        self,
    ) -> typing.Optional[StorageAccountQueuePropertiesHourMetrics]:
        return typing.cast(typing.Optional[StorageAccountQueuePropertiesHourMetrics], jsii.get(self, "hourMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional[StorageAccountQueuePropertiesLogging]:
        return typing.cast(typing.Optional[StorageAccountQueuePropertiesLogging], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="minuteMetricsInput")
    def minute_metrics_input(
        self,
    ) -> typing.Optional[StorageAccountQueuePropertiesMinuteMetrics]:
        return typing.cast(typing.Optional[StorageAccountQueuePropertiesMinuteMetrics], jsii.get(self, "minuteMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountQueueProperties]:
        return typing.cast(typing.Optional[StorageAccountQueueProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountQueueProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountQueuePropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountRouting",
    jsii_struct_bases=[],
    name_mapping={
        "choice": "choice",
        "publish_internet_endpoints": "publishInternetEndpoints",
        "publish_microsoft_endpoints": "publishMicrosoftEndpoints",
    },
)
class StorageAccountRouting:
    def __init__(
        self,
        *,
        choice: typing.Optional[builtins.str] = None,
        publish_internet_endpoints: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        publish_microsoft_endpoints: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param choice: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#choice StorageAccount#choice}.
        :param publish_internet_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#publish_internet_endpoints StorageAccount#publish_internet_endpoints}.
        :param publish_microsoft_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#publish_microsoft_endpoints StorageAccount#publish_microsoft_endpoints}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountRouting.__init__)
            check_type(argname="argument choice", value=choice, expected_type=type_hints["choice"])
            check_type(argname="argument publish_internet_endpoints", value=publish_internet_endpoints, expected_type=type_hints["publish_internet_endpoints"])
            check_type(argname="argument publish_microsoft_endpoints", value=publish_microsoft_endpoints, expected_type=type_hints["publish_microsoft_endpoints"])
        self._values: typing.Dict[str, typing.Any] = {}
        if choice is not None:
            self._values["choice"] = choice
        if publish_internet_endpoints is not None:
            self._values["publish_internet_endpoints"] = publish_internet_endpoints
        if publish_microsoft_endpoints is not None:
            self._values["publish_microsoft_endpoints"] = publish_microsoft_endpoints

    @builtins.property
    def choice(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#choice StorageAccount#choice}.'''
        result = self._values.get("choice")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publish_internet_endpoints(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#publish_internet_endpoints StorageAccount#publish_internet_endpoints}.'''
        result = self._values.get("publish_internet_endpoints")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def publish_microsoft_endpoints(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#publish_microsoft_endpoints StorageAccount#publish_microsoft_endpoints}.'''
        result = self._values.get("publish_microsoft_endpoints")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountRouting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountRoutingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountRoutingOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountRoutingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetChoice")
    def reset_choice(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChoice", []))

    @jsii.member(jsii_name="resetPublishInternetEndpoints")
    def reset_publish_internet_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishInternetEndpoints", []))

    @jsii.member(jsii_name="resetPublishMicrosoftEndpoints")
    def reset_publish_microsoft_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishMicrosoftEndpoints", []))

    @builtins.property
    @jsii.member(jsii_name="choiceInput")
    def choice_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "choiceInput"))

    @builtins.property
    @jsii.member(jsii_name="publishInternetEndpointsInput")
    def publish_internet_endpoints_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publishInternetEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="publishMicrosoftEndpointsInput")
    def publish_microsoft_endpoints_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publishMicrosoftEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="choice")
    def choice(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "choice"))

    @choice.setter
    def choice(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountRoutingOutputReference, "choice").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "choice", value)

    @builtins.property
    @jsii.member(jsii_name="publishInternetEndpoints")
    def publish_internet_endpoints(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publishInternetEndpoints"))

    @publish_internet_endpoints.setter
    def publish_internet_endpoints(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountRoutingOutputReference, "publish_internet_endpoints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishInternetEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="publishMicrosoftEndpoints")
    def publish_microsoft_endpoints(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publishMicrosoftEndpoints"))

    @publish_microsoft_endpoints.setter
    def publish_microsoft_endpoints(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountRoutingOutputReference, "publish_microsoft_endpoints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishMicrosoftEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountRouting]:
        return typing.cast(typing.Optional[StorageAccountRouting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[StorageAccountRouting]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountRoutingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountShareProperties",
    jsii_struct_bases=[],
    name_mapping={
        "cors_rule": "corsRule",
        "retention_policy": "retentionPolicy",
        "smb": "smb",
    },
)
class StorageAccountShareProperties:
    def __init__(
        self,
        *,
        cors_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["StorageAccountSharePropertiesCorsRule", typing.Dict[str, typing.Any]]]]] = None,
        retention_policy: typing.Optional[typing.Union["StorageAccountSharePropertiesRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        smb: typing.Optional[typing.Union["StorageAccountSharePropertiesSmb", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy StorageAccount#retention_policy}
        :param smb: smb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#smb StorageAccount#smb}
        '''
        if isinstance(retention_policy, dict):
            retention_policy = StorageAccountSharePropertiesRetentionPolicy(**retention_policy)
        if isinstance(smb, dict):
            smb = StorageAccountSharePropertiesSmb(**smb)
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountShareProperties.__init__)
            check_type(argname="argument cors_rule", value=cors_rule, expected_type=type_hints["cors_rule"])
            check_type(argname="argument retention_policy", value=retention_policy, expected_type=type_hints["retention_policy"])
            check_type(argname="argument smb", value=smb, expected_type=type_hints["smb"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cors_rule is not None:
            self._values["cors_rule"] = cors_rule
        if retention_policy is not None:
            self._values["retention_policy"] = retention_policy
        if smb is not None:
            self._values["smb"] = smb

    @builtins.property
    def cors_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountSharePropertiesCorsRule"]]]:
        '''cors_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#cors_rule StorageAccount#cors_rule}
        '''
        result = self._values.get("cors_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["StorageAccountSharePropertiesCorsRule"]]], result)

    @builtins.property
    def retention_policy(
        self,
    ) -> typing.Optional["StorageAccountSharePropertiesRetentionPolicy"]:
        '''retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#retention_policy StorageAccount#retention_policy}
        '''
        result = self._values.get("retention_policy")
        return typing.cast(typing.Optional["StorageAccountSharePropertiesRetentionPolicy"], result)

    @builtins.property
    def smb(self) -> typing.Optional["StorageAccountSharePropertiesSmb"]:
        '''smb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#smb StorageAccount#smb}
        '''
        result = self._values.get("smb")
        return typing.cast(typing.Optional["StorageAccountSharePropertiesSmb"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountShareProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountSharePropertiesCorsRule",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_headers": "allowedHeaders",
        "allowed_methods": "allowedMethods",
        "allowed_origins": "allowedOrigins",
        "exposed_headers": "exposedHeaders",
        "max_age_in_seconds": "maxAgeInSeconds",
    },
)
class StorageAccountSharePropertiesCorsRule:
    def __init__(
        self,
        *,
        allowed_headers: typing.Sequence[builtins.str],
        allowed_methods: typing.Sequence[builtins.str],
        allowed_origins: typing.Sequence[builtins.str],
        exposed_headers: typing.Sequence[builtins.str],
        max_age_in_seconds: jsii.Number,
    ) -> None:
        '''
        :param allowed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_headers StorageAccount#allowed_headers}.
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_methods StorageAccount#allowed_methods}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_origins StorageAccount#allowed_origins}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#exposed_headers StorageAccount#exposed_headers}.
        :param max_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#max_age_in_seconds StorageAccount#max_age_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesCorsRule.__init__)
            check_type(argname="argument allowed_headers", value=allowed_headers, expected_type=type_hints["allowed_headers"])
            check_type(argname="argument allowed_methods", value=allowed_methods, expected_type=type_hints["allowed_methods"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument exposed_headers", value=exposed_headers, expected_type=type_hints["exposed_headers"])
            check_type(argname="argument max_age_in_seconds", value=max_age_in_seconds, expected_type=type_hints["max_age_in_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_headers": allowed_headers,
            "allowed_methods": allowed_methods,
            "allowed_origins": allowed_origins,
            "exposed_headers": exposed_headers,
            "max_age_in_seconds": max_age_in_seconds,
        }

    @builtins.property
    def allowed_headers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_headers StorageAccount#allowed_headers}.'''
        result = self._values.get("allowed_headers")
        assert result is not None, "Required property 'allowed_headers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_methods StorageAccount#allowed_methods}.'''
        result = self._values.get("allowed_methods")
        assert result is not None, "Required property 'allowed_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#allowed_origins StorageAccount#allowed_origins}.'''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def exposed_headers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#exposed_headers StorageAccount#exposed_headers}.'''
        result = self._values.get("exposed_headers")
        assert result is not None, "Required property 'exposed_headers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def max_age_in_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#max_age_in_seconds StorageAccount#max_age_in_seconds}.'''
        result = self._values.get("max_age_in_seconds")
        assert result is not None, "Required property 'max_age_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountSharePropertiesCorsRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountSharePropertiesCorsRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountSharePropertiesCorsRuleList",
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
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesCorsRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageAccountSharePropertiesCorsRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesCorsRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageAccountSharePropertiesCorsRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountSharePropertiesCorsRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountSharePropertiesCorsRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountSharePropertiesCorsRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountSharePropertiesCorsRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountSharePropertiesCorsRuleOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesCorsRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="allowedHeadersInput")
    def allowed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedMethodsInput")
    def allowed_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="exposedHeadersInput")
    def exposed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInSecondsInput")
    def max_age_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHeaders")
    def allowed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedHeaders"))

    @allowed_headers.setter
    def allowed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleOutputReference, "allowed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleOutputReference, "allowed_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleOutputReference, "allowed_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="exposedHeaders")
    def exposed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposedHeaders"))

    @exposed_headers.setter
    def exposed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleOutputReference, "exposed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAgeInSeconds"))

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleOutputReference, "max_age_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageAccountSharePropertiesCorsRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageAccountSharePropertiesCorsRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageAccountSharePropertiesCorsRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesCorsRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageAccountSharePropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountSharePropertiesOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCorsRule")
    def put_cors_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[StorageAccountSharePropertiesCorsRule, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesOutputReference.put_cors_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCorsRule", [value]))

    @jsii.member(jsii_name="putRetentionPolicy")
    def put_retention_policy(
        self,
        *,
        days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.
        '''
        value = StorageAccountSharePropertiesRetentionPolicy(days=days)

        return typing.cast(None, jsii.invoke(self, "putRetentionPolicy", [value]))

    @jsii.member(jsii_name="putSmb")
    def put_smb(
        self,
        *,
        authentication_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        channel_encryption_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        kerberos_ticket_encryption_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        multichannel_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param authentication_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#authentication_types StorageAccount#authentication_types}.
        :param channel_encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#channel_encryption_type StorageAccount#channel_encryption_type}.
        :param kerberos_ticket_encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#kerberos_ticket_encryption_type StorageAccount#kerberos_ticket_encryption_type}.
        :param multichannel_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#multichannel_enabled StorageAccount#multichannel_enabled}.
        :param versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#versions StorageAccount#versions}.
        '''
        value = StorageAccountSharePropertiesSmb(
            authentication_types=authentication_types,
            channel_encryption_type=channel_encryption_type,
            kerberos_ticket_encryption_type=kerberos_ticket_encryption_type,
            multichannel_enabled=multichannel_enabled,
            versions=versions,
        )

        return typing.cast(None, jsii.invoke(self, "putSmb", [value]))

    @jsii.member(jsii_name="resetCorsRule")
    def reset_cors_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsRule", []))

    @jsii.member(jsii_name="resetRetentionPolicy")
    def reset_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicy", []))

    @jsii.member(jsii_name="resetSmb")
    def reset_smb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmb", []))

    @builtins.property
    @jsii.member(jsii_name="corsRule")
    def cors_rule(self) -> StorageAccountSharePropertiesCorsRuleList:
        return typing.cast(StorageAccountSharePropertiesCorsRuleList, jsii.get(self, "corsRule"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicy")
    def retention_policy(
        self,
    ) -> "StorageAccountSharePropertiesRetentionPolicyOutputReference":
        return typing.cast("StorageAccountSharePropertiesRetentionPolicyOutputReference", jsii.get(self, "retentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="smb")
    def smb(self) -> "StorageAccountSharePropertiesSmbOutputReference":
        return typing.cast("StorageAccountSharePropertiesSmbOutputReference", jsii.get(self, "smb"))

    @builtins.property
    @jsii.member(jsii_name="corsRuleInput")
    def cors_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountSharePropertiesCorsRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[StorageAccountSharePropertiesCorsRule]]], jsii.get(self, "corsRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyInput")
    def retention_policy_input(
        self,
    ) -> typing.Optional["StorageAccountSharePropertiesRetentionPolicy"]:
        return typing.cast(typing.Optional["StorageAccountSharePropertiesRetentionPolicy"], jsii.get(self, "retentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="smbInput")
    def smb_input(self) -> typing.Optional["StorageAccountSharePropertiesSmb"]:
        return typing.cast(typing.Optional["StorageAccountSharePropertiesSmb"], jsii.get(self, "smbInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountShareProperties]:
        return typing.cast(typing.Optional[StorageAccountShareProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountShareProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountSharePropertiesRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={"days": "days"},
)
class StorageAccountSharePropertiesRetentionPolicy:
    def __init__(self, *, days: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesRetentionPolicy.__init__)
            check_type(argname="argument days", value=days, expected_type=type_hints["days"])
        self._values: typing.Dict[str, typing.Any] = {}
        if days is not None:
            self._values["days"] = days

    @builtins.property
    def days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#days StorageAccount#days}.'''
        result = self._values.get("days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountSharePropertiesRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountSharePropertiesRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountSharePropertiesRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDays")
    def reset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDays", []))

    @builtins.property
    @jsii.member(jsii_name="daysInput")
    def days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysInput"))

    @builtins.property
    @jsii.member(jsii_name="days")
    def days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "days"))

    @days.setter
    def days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesRetentionPolicyOutputReference, "days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "days", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageAccountSharePropertiesRetentionPolicy]:
        return typing.cast(typing.Optional[StorageAccountSharePropertiesRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountSharePropertiesRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountSharePropertiesSmb",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_types": "authenticationTypes",
        "channel_encryption_type": "channelEncryptionType",
        "kerberos_ticket_encryption_type": "kerberosTicketEncryptionType",
        "multichannel_enabled": "multichannelEnabled",
        "versions": "versions",
    },
)
class StorageAccountSharePropertiesSmb:
    def __init__(
        self,
        *,
        authentication_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        channel_encryption_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        kerberos_ticket_encryption_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        multichannel_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param authentication_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#authentication_types StorageAccount#authentication_types}.
        :param channel_encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#channel_encryption_type StorageAccount#channel_encryption_type}.
        :param kerberos_ticket_encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#kerberos_ticket_encryption_type StorageAccount#kerberos_ticket_encryption_type}.
        :param multichannel_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#multichannel_enabled StorageAccount#multichannel_enabled}.
        :param versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#versions StorageAccount#versions}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesSmb.__init__)
            check_type(argname="argument authentication_types", value=authentication_types, expected_type=type_hints["authentication_types"])
            check_type(argname="argument channel_encryption_type", value=channel_encryption_type, expected_type=type_hints["channel_encryption_type"])
            check_type(argname="argument kerberos_ticket_encryption_type", value=kerberos_ticket_encryption_type, expected_type=type_hints["kerberos_ticket_encryption_type"])
            check_type(argname="argument multichannel_enabled", value=multichannel_enabled, expected_type=type_hints["multichannel_enabled"])
            check_type(argname="argument versions", value=versions, expected_type=type_hints["versions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authentication_types is not None:
            self._values["authentication_types"] = authentication_types
        if channel_encryption_type is not None:
            self._values["channel_encryption_type"] = channel_encryption_type
        if kerberos_ticket_encryption_type is not None:
            self._values["kerberos_ticket_encryption_type"] = kerberos_ticket_encryption_type
        if multichannel_enabled is not None:
            self._values["multichannel_enabled"] = multichannel_enabled
        if versions is not None:
            self._values["versions"] = versions

    @builtins.property
    def authentication_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#authentication_types StorageAccount#authentication_types}.'''
        result = self._values.get("authentication_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def channel_encryption_type(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#channel_encryption_type StorageAccount#channel_encryption_type}.'''
        result = self._values.get("channel_encryption_type")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def kerberos_ticket_encryption_type(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#kerberos_ticket_encryption_type StorageAccount#kerberos_ticket_encryption_type}.'''
        result = self._values.get("kerberos_ticket_encryption_type")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def multichannel_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#multichannel_enabled StorageAccount#multichannel_enabled}.'''
        result = self._values.get("multichannel_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#versions StorageAccount#versions}.'''
        result = self._values.get("versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountSharePropertiesSmb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountSharePropertiesSmbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountSharePropertiesSmbOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountSharePropertiesSmbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthenticationTypes")
    def reset_authentication_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationTypes", []))

    @jsii.member(jsii_name="resetChannelEncryptionType")
    def reset_channel_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannelEncryptionType", []))

    @jsii.member(jsii_name="resetKerberosTicketEncryptionType")
    def reset_kerberos_ticket_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberosTicketEncryptionType", []))

    @jsii.member(jsii_name="resetMultichannelEnabled")
    def reset_multichannel_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultichannelEnabled", []))

    @jsii.member(jsii_name="resetVersions")
    def reset_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersions", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypesInput")
    def authentication_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authenticationTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="channelEncryptionTypeInput")
    def channel_encryption_type_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "channelEncryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kerberosTicketEncryptionTypeInput")
    def kerberos_ticket_encryption_type_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "kerberosTicketEncryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="multichannelEnabledInput")
    def multichannel_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "multichannelEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="versionsInput")
    def versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "versionsInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypes")
    def authentication_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authenticationTypes"))

    @authentication_types.setter
    def authentication_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesSmbOutputReference, "authentication_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationTypes", value)

    @builtins.property
    @jsii.member(jsii_name="channelEncryptionType")
    def channel_encryption_type(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "channelEncryptionType"))

    @channel_encryption_type.setter
    def channel_encryption_type(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesSmbOutputReference, "channel_encryption_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelEncryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="kerberosTicketEncryptionType")
    def kerberos_ticket_encryption_type(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "kerberosTicketEncryptionType"))

    @kerberos_ticket_encryption_type.setter
    def kerberos_ticket_encryption_type(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesSmbOutputReference, "kerberos_ticket_encryption_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kerberosTicketEncryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="multichannelEnabled")
    def multichannel_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "multichannelEnabled"))

    @multichannel_enabled.setter
    def multichannel_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesSmbOutputReference, "multichannel_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multichannelEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="versions")
    def versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "versions"))

    @versions.setter
    def versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesSmbOutputReference, "versions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountSharePropertiesSmb]:
        return typing.cast(typing.Optional[StorageAccountSharePropertiesSmb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountSharePropertiesSmb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountSharePropertiesSmbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountStaticWebsite",
    jsii_struct_bases=[],
    name_mapping={
        "error404_document": "error404Document",
        "index_document": "indexDocument",
    },
)
class StorageAccountStaticWebsite:
    def __init__(
        self,
        *,
        error404_document: typing.Optional[builtins.str] = None,
        index_document: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error404_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#error_404_document StorageAccount#error_404_document}.
        :param index_document: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#index_document StorageAccount#index_document}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountStaticWebsite.__init__)
            check_type(argname="argument error404_document", value=error404_document, expected_type=type_hints["error404_document"])
            check_type(argname="argument index_document", value=index_document, expected_type=type_hints["index_document"])
        self._values: typing.Dict[str, typing.Any] = {}
        if error404_document is not None:
            self._values["error404_document"] = error404_document
        if index_document is not None:
            self._values["index_document"] = index_document

    @builtins.property
    def error404_document(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#error_404_document StorageAccount#error_404_document}.'''
        result = self._values.get("error404_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_document(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#index_document StorageAccount#index_document}.'''
        result = self._values.get("index_document")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountStaticWebsite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountStaticWebsiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountStaticWebsiteOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountStaticWebsiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetError404Document")
    def reset_error404_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetError404Document", []))

    @jsii.member(jsii_name="resetIndexDocument")
    def reset_index_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexDocument", []))

    @builtins.property
    @jsii.member(jsii_name="error404DocumentInput")
    def error404_document_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "error404DocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="indexDocumentInput")
    def index_document_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="error404Document")
    def error404_document(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "error404Document"))

    @error404_document.setter
    def error404_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountStaticWebsiteOutputReference, "error404_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "error404Document", value)

    @builtins.property
    @jsii.member(jsii_name="indexDocument")
    def index_document(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexDocument"))

    @index_document.setter
    def index_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountStaticWebsiteOutputReference, "index_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexDocument", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountStaticWebsite]:
        return typing.cast(typing.Optional[StorageAccountStaticWebsite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountStaticWebsite],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountStaticWebsiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StorageAccountTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#create StorageAccount#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete StorageAccount#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#read StorageAccount#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#update StorageAccount#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageAccountTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#create StorageAccount#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#delete StorageAccount#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#read StorageAccount#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/storage_account#update StorageAccount#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.storageAccount.StorageAccountTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(StorageAccountTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(StorageAccountTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageAccountTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageAccountTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageAccountTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageAccountTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageAccount",
    "StorageAccountAzureFilesAuthentication",
    "StorageAccountAzureFilesAuthenticationActiveDirectory",
    "StorageAccountAzureFilesAuthenticationActiveDirectoryOutputReference",
    "StorageAccountAzureFilesAuthenticationOutputReference",
    "StorageAccountBlobProperties",
    "StorageAccountBlobPropertiesContainerDeleteRetentionPolicy",
    "StorageAccountBlobPropertiesContainerDeleteRetentionPolicyOutputReference",
    "StorageAccountBlobPropertiesCorsRule",
    "StorageAccountBlobPropertiesCorsRuleList",
    "StorageAccountBlobPropertiesCorsRuleOutputReference",
    "StorageAccountBlobPropertiesDeleteRetentionPolicy",
    "StorageAccountBlobPropertiesDeleteRetentionPolicyOutputReference",
    "StorageAccountBlobPropertiesOutputReference",
    "StorageAccountConfig",
    "StorageAccountCustomDomain",
    "StorageAccountCustomDomainOutputReference",
    "StorageAccountCustomerManagedKey",
    "StorageAccountCustomerManagedKeyOutputReference",
    "StorageAccountIdentity",
    "StorageAccountIdentityOutputReference",
    "StorageAccountNetworkRules",
    "StorageAccountNetworkRulesOutputReference",
    "StorageAccountNetworkRulesPrivateLinkAccess",
    "StorageAccountNetworkRulesPrivateLinkAccessList",
    "StorageAccountNetworkRulesPrivateLinkAccessOutputReference",
    "StorageAccountQueueProperties",
    "StorageAccountQueuePropertiesCorsRule",
    "StorageAccountQueuePropertiesCorsRuleList",
    "StorageAccountQueuePropertiesCorsRuleOutputReference",
    "StorageAccountQueuePropertiesHourMetrics",
    "StorageAccountQueuePropertiesHourMetricsOutputReference",
    "StorageAccountQueuePropertiesLogging",
    "StorageAccountQueuePropertiesLoggingOutputReference",
    "StorageAccountQueuePropertiesMinuteMetrics",
    "StorageAccountQueuePropertiesMinuteMetricsOutputReference",
    "StorageAccountQueuePropertiesOutputReference",
    "StorageAccountRouting",
    "StorageAccountRoutingOutputReference",
    "StorageAccountShareProperties",
    "StorageAccountSharePropertiesCorsRule",
    "StorageAccountSharePropertiesCorsRuleList",
    "StorageAccountSharePropertiesCorsRuleOutputReference",
    "StorageAccountSharePropertiesOutputReference",
    "StorageAccountSharePropertiesRetentionPolicy",
    "StorageAccountSharePropertiesRetentionPolicyOutputReference",
    "StorageAccountSharePropertiesSmb",
    "StorageAccountSharePropertiesSmbOutputReference",
    "StorageAccountStaticWebsite",
    "StorageAccountStaticWebsiteOutputReference",
    "StorageAccountTimeouts",
    "StorageAccountTimeoutsOutputReference",
]

publication.publish()
