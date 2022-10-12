'''
# `azurerm_cosmosdb_account`

Refer to the Terraform Registory for docs: [`azurerm_cosmosdb_account`](https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account).
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


class CosmosdbAccount(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account azurerm_cosmosdb_account}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        consistency_policy: typing.Union["CosmosdbAccountConsistencyPolicy", typing.Dict[str, typing.Any]],
        geo_location: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountGeoLocation", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        offer_type: builtins.str,
        resource_group_name: builtins.str,
        access_key_metadata_writes_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        analytical_storage: typing.Optional[typing.Union["CosmosdbAccountAnalyticalStorage", typing.Dict[str, typing.Any]]] = None,
        analytical_storage_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backup: typing.Optional[typing.Union["CosmosdbAccountBackup", typing.Dict[str, typing.Any]]] = None,
        capabilities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountCapabilities", typing.Dict[str, typing.Any]]]]] = None,
        capacity: typing.Optional[typing.Union["CosmosdbAccountCapacity", typing.Dict[str, typing.Any]]] = None,
        cors_rule: typing.Optional[typing.Union["CosmosdbAccountCorsRule", typing.Dict[str, typing.Any]]] = None,
        create_mode: typing.Optional[builtins.str] = None,
        default_identity_type: typing.Optional[builtins.str] = None,
        enable_automatic_failover: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_free_tier: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_multiple_write_locations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["CosmosdbAccountIdentity", typing.Dict[str, typing.Any]]] = None,
        ip_range_filter: typing.Optional[builtins.str] = None,
        is_virtual_network_filter_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_vault_key_id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        local_authentication_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mongo_server_version: typing.Optional[builtins.str] = None,
        network_acl_bypass_for_azure_services: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_acl_bypass_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restore: typing.Optional[typing.Union["CosmosdbAccountRestore", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CosmosdbAccountTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountVirtualNetworkRule", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account azurerm_cosmosdb_account} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param consistency_policy: consistency_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#consistency_policy CosmosdbAccount#consistency_policy}
        :param geo_location: geo_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#geo_location CosmosdbAccount#geo_location}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#location CosmosdbAccount#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#name CosmosdbAccount#name}.
        :param offer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#offer_type CosmosdbAccount#offer_type}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#resource_group_name CosmosdbAccount#resource_group_name}.
        :param access_key_metadata_writes_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#access_key_metadata_writes_enabled CosmosdbAccount#access_key_metadata_writes_enabled}.
        :param analytical_storage: analytical_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#analytical_storage CosmosdbAccount#analytical_storage}
        :param analytical_storage_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#analytical_storage_enabled CosmosdbAccount#analytical_storage_enabled}.
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#backup CosmosdbAccount#backup}
        :param capabilities: capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#capabilities CosmosdbAccount#capabilities}
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#capacity CosmosdbAccount#capacity}
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#cors_rule CosmosdbAccount#cors_rule}
        :param create_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#create_mode CosmosdbAccount#create_mode}.
        :param default_identity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#default_identity_type CosmosdbAccount#default_identity_type}.
        :param enable_automatic_failover: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_automatic_failover CosmosdbAccount#enable_automatic_failover}.
        :param enable_free_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_free_tier CosmosdbAccount#enable_free_tier}.
        :param enable_multiple_write_locations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_multiple_write_locations CosmosdbAccount#enable_multiple_write_locations}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#id CosmosdbAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#identity CosmosdbAccount#identity}
        :param ip_range_filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#ip_range_filter CosmosdbAccount#ip_range_filter}.
        :param is_virtual_network_filter_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#is_virtual_network_filter_enabled CosmosdbAccount#is_virtual_network_filter_enabled}.
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#key_vault_key_id CosmosdbAccount#key_vault_key_id}.
        :param kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#kind CosmosdbAccount#kind}.
        :param local_authentication_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#local_authentication_disabled CosmosdbAccount#local_authentication_disabled}.
        :param mongo_server_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#mongo_server_version CosmosdbAccount#mongo_server_version}.
        :param network_acl_bypass_for_azure_services: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#network_acl_bypass_for_azure_services CosmosdbAccount#network_acl_bypass_for_azure_services}.
        :param network_acl_bypass_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#network_acl_bypass_ids CosmosdbAccount#network_acl_bypass_ids}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#public_network_access_enabled CosmosdbAccount#public_network_access_enabled}.
        :param restore: restore block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#restore CosmosdbAccount#restore}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#tags CosmosdbAccount#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#timeouts CosmosdbAccount#timeouts}
        :param virtual_network_rule: virtual_network_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#virtual_network_rule CosmosdbAccount#virtual_network_rule}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccount.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CosmosdbAccountConfig(
            consistency_policy=consistency_policy,
            geo_location=geo_location,
            location=location,
            name=name,
            offer_type=offer_type,
            resource_group_name=resource_group_name,
            access_key_metadata_writes_enabled=access_key_metadata_writes_enabled,
            analytical_storage=analytical_storage,
            analytical_storage_enabled=analytical_storage_enabled,
            backup=backup,
            capabilities=capabilities,
            capacity=capacity,
            cors_rule=cors_rule,
            create_mode=create_mode,
            default_identity_type=default_identity_type,
            enable_automatic_failover=enable_automatic_failover,
            enable_free_tier=enable_free_tier,
            enable_multiple_write_locations=enable_multiple_write_locations,
            id=id,
            identity=identity,
            ip_range_filter=ip_range_filter,
            is_virtual_network_filter_enabled=is_virtual_network_filter_enabled,
            key_vault_key_id=key_vault_key_id,
            kind=kind,
            local_authentication_disabled=local_authentication_disabled,
            mongo_server_version=mongo_server_version,
            network_acl_bypass_for_azure_services=network_acl_bypass_for_azure_services,
            network_acl_bypass_ids=network_acl_bypass_ids,
            public_network_access_enabled=public_network_access_enabled,
            restore=restore,
            tags=tags,
            timeouts=timeouts,
            virtual_network_rule=virtual_network_rule,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAnalyticalStorage")
    def put_analytical_storage(self, *, schema_type: builtins.str) -> None:
        '''
        :param schema_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#schema_type CosmosdbAccount#schema_type}.
        '''
        value = CosmosdbAccountAnalyticalStorage(schema_type=schema_type)

        return typing.cast(None, jsii.invoke(self, "putAnalyticalStorage", [value]))

    @jsii.member(jsii_name="putBackup")
    def put_backup(
        self,
        *,
        type: builtins.str,
        interval_in_minutes: typing.Optional[jsii.Number] = None,
        retention_in_hours: typing.Optional[jsii.Number] = None,
        storage_redundancy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#type CosmosdbAccount#type}.
        :param interval_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#interval_in_minutes CosmosdbAccount#interval_in_minutes}.
        :param retention_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#retention_in_hours CosmosdbAccount#retention_in_hours}.
        :param storage_redundancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#storage_redundancy CosmosdbAccount#storage_redundancy}.
        '''
        value = CosmosdbAccountBackup(
            type=type,
            interval_in_minutes=interval_in_minutes,
            retention_in_hours=retention_in_hours,
            storage_redundancy=storage_redundancy,
        )

        return typing.cast(None, jsii.invoke(self, "putBackup", [value]))

    @jsii.member(jsii_name="putCapabilities")
    def put_capabilities(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountCapabilities", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccount.put_capabilities)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapabilities", [value]))

    @jsii.member(jsii_name="putCapacity")
    def put_capacity(self, *, total_throughput_limit: jsii.Number) -> None:
        '''
        :param total_throughput_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#total_throughput_limit CosmosdbAccount#total_throughput_limit}.
        '''
        value = CosmosdbAccountCapacity(total_throughput_limit=total_throughput_limit)

        return typing.cast(None, jsii.invoke(self, "putCapacity", [value]))

    @jsii.member(jsii_name="putConsistencyPolicy")
    def put_consistency_policy(
        self,
        *,
        consistency_level: builtins.str,
        max_interval_in_seconds: typing.Optional[jsii.Number] = None,
        max_staleness_prefix: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param consistency_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#consistency_level CosmosdbAccount#consistency_level}.
        :param max_interval_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_interval_in_seconds CosmosdbAccount#max_interval_in_seconds}.
        :param max_staleness_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_staleness_prefix CosmosdbAccount#max_staleness_prefix}.
        '''
        value = CosmosdbAccountConsistencyPolicy(
            consistency_level=consistency_level,
            max_interval_in_seconds=max_interval_in_seconds,
            max_staleness_prefix=max_staleness_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putConsistencyPolicy", [value]))

    @jsii.member(jsii_name="putCorsRule")
    def put_cors_rule(
        self,
        *,
        allowed_headers: typing.Sequence[builtins.str],
        allowed_methods: typing.Sequence[builtins.str],
        allowed_origins: typing.Sequence[builtins.str],
        exposed_headers: typing.Sequence[builtins.str],
        max_age_in_seconds: jsii.Number,
    ) -> None:
        '''
        :param allowed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_headers CosmosdbAccount#allowed_headers}.
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_methods CosmosdbAccount#allowed_methods}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_origins CosmosdbAccount#allowed_origins}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#exposed_headers CosmosdbAccount#exposed_headers}.
        :param max_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_age_in_seconds CosmosdbAccount#max_age_in_seconds}.
        '''
        value = CosmosdbAccountCorsRule(
            allowed_headers=allowed_headers,
            allowed_methods=allowed_methods,
            allowed_origins=allowed_origins,
            exposed_headers=exposed_headers,
            max_age_in_seconds=max_age_in_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putCorsRule", [value]))

    @jsii.member(jsii_name="putGeoLocation")
    def put_geo_location(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountGeoLocation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccount.put_geo_location)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGeoLocation", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#type CosmosdbAccount#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#identity_ids CosmosdbAccount#identity_ids}.
        '''
        value = CosmosdbAccountIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putRestore")
    def put_restore(
        self,
        *,
        restore_timestamp_in_utc: builtins.str,
        source_cosmosdb_account_id: builtins.str,
        database: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountRestoreDatabase", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param restore_timestamp_in_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#restore_timestamp_in_utc CosmosdbAccount#restore_timestamp_in_utc}.
        :param source_cosmosdb_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#source_cosmosdb_account_id CosmosdbAccount#source_cosmosdb_account_id}.
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#database CosmosdbAccount#database}
        '''
        value = CosmosdbAccountRestore(
            restore_timestamp_in_utc=restore_timestamp_in_utc,
            source_cosmosdb_account_id=source_cosmosdb_account_id,
            database=database,
        )

        return typing.cast(None, jsii.invoke(self, "putRestore", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#create CosmosdbAccount#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#delete CosmosdbAccount#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#read CosmosdbAccount#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#update CosmosdbAccount#update}.
        '''
        value = CosmosdbAccountTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVirtualNetworkRule")
    def put_virtual_network_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountVirtualNetworkRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccount.put_virtual_network_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVirtualNetworkRule", [value]))

    @jsii.member(jsii_name="resetAccessKeyMetadataWritesEnabled")
    def reset_access_key_metadata_writes_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKeyMetadataWritesEnabled", []))

    @jsii.member(jsii_name="resetAnalyticalStorage")
    def reset_analytical_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnalyticalStorage", []))

    @jsii.member(jsii_name="resetAnalyticalStorageEnabled")
    def reset_analytical_storage_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnalyticalStorageEnabled", []))

    @jsii.member(jsii_name="resetBackup")
    def reset_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackup", []))

    @jsii.member(jsii_name="resetCapabilities")
    def reset_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapabilities", []))

    @jsii.member(jsii_name="resetCapacity")
    def reset_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacity", []))

    @jsii.member(jsii_name="resetCorsRule")
    def reset_cors_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsRule", []))

    @jsii.member(jsii_name="resetCreateMode")
    def reset_create_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateMode", []))

    @jsii.member(jsii_name="resetDefaultIdentityType")
    def reset_default_identity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultIdentityType", []))

    @jsii.member(jsii_name="resetEnableAutomaticFailover")
    def reset_enable_automatic_failover(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutomaticFailover", []))

    @jsii.member(jsii_name="resetEnableFreeTier")
    def reset_enable_free_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableFreeTier", []))

    @jsii.member(jsii_name="resetEnableMultipleWriteLocations")
    def reset_enable_multiple_write_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMultipleWriteLocations", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetIpRangeFilter")
    def reset_ip_range_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRangeFilter", []))

    @jsii.member(jsii_name="resetIsVirtualNetworkFilterEnabled")
    def reset_is_virtual_network_filter_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsVirtualNetworkFilterEnabled", []))

    @jsii.member(jsii_name="resetKeyVaultKeyId")
    def reset_key_vault_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultKeyId", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetLocalAuthenticationDisabled")
    def reset_local_authentication_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalAuthenticationDisabled", []))

    @jsii.member(jsii_name="resetMongoServerVersion")
    def reset_mongo_server_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMongoServerVersion", []))

    @jsii.member(jsii_name="resetNetworkAclBypassForAzureServices")
    def reset_network_acl_bypass_for_azure_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkAclBypassForAzureServices", []))

    @jsii.member(jsii_name="resetNetworkAclBypassIds")
    def reset_network_acl_bypass_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkAclBypassIds", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetRestore")
    def reset_restore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestore", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVirtualNetworkRule")
    def reset_virtual_network_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkRule", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="analyticalStorage")
    def analytical_storage(self) -> "CosmosdbAccountAnalyticalStorageOutputReference":
        return typing.cast("CosmosdbAccountAnalyticalStorageOutputReference", jsii.get(self, "analyticalStorage"))

    @builtins.property
    @jsii.member(jsii_name="backup")
    def backup(self) -> "CosmosdbAccountBackupOutputReference":
        return typing.cast("CosmosdbAccountBackupOutputReference", jsii.get(self, "backup"))

    @builtins.property
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> "CosmosdbAccountCapabilitiesList":
        return typing.cast("CosmosdbAccountCapabilitiesList", jsii.get(self, "capabilities"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> "CosmosdbAccountCapacityOutputReference":
        return typing.cast("CosmosdbAccountCapacityOutputReference", jsii.get(self, "capacity"))

    @builtins.property
    @jsii.member(jsii_name="connectionStrings")
    def connection_strings(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "connectionStrings"))

    @builtins.property
    @jsii.member(jsii_name="consistencyPolicy")
    def consistency_policy(self) -> "CosmosdbAccountConsistencyPolicyOutputReference":
        return typing.cast("CosmosdbAccountConsistencyPolicyOutputReference", jsii.get(self, "consistencyPolicy"))

    @builtins.property
    @jsii.member(jsii_name="corsRule")
    def cors_rule(self) -> "CosmosdbAccountCorsRuleOutputReference":
        return typing.cast("CosmosdbAccountCorsRuleOutputReference", jsii.get(self, "corsRule"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="geoLocation")
    def geo_location(self) -> "CosmosdbAccountGeoLocationList":
        return typing.cast("CosmosdbAccountGeoLocationList", jsii.get(self, "geoLocation"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "CosmosdbAccountIdentityOutputReference":
        return typing.cast("CosmosdbAccountIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryKey"))

    @builtins.property
    @jsii.member(jsii_name="primaryReadonlyKey")
    def primary_readonly_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryReadonlyKey"))

    @builtins.property
    @jsii.member(jsii_name="readEndpoints")
    def read_endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "readEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="restore")
    def restore(self) -> "CosmosdbAccountRestoreOutputReference":
        return typing.cast("CosmosdbAccountRestoreOutputReference", jsii.get(self, "restore"))

    @builtins.property
    @jsii.member(jsii_name="secondaryKey")
    def secondary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryKey"))

    @builtins.property
    @jsii.member(jsii_name="secondaryReadonlyKey")
    def secondary_readonly_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryReadonlyKey"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CosmosdbAccountTimeoutsOutputReference":
        return typing.cast("CosmosdbAccountTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkRule")
    def virtual_network_rule(self) -> "CosmosdbAccountVirtualNetworkRuleList":
        return typing.cast("CosmosdbAccountVirtualNetworkRuleList", jsii.get(self, "virtualNetworkRule"))

    @builtins.property
    @jsii.member(jsii_name="writeEndpoints")
    def write_endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "writeEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyMetadataWritesEnabledInput")
    def access_key_metadata_writes_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "accessKeyMetadataWritesEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="analyticalStorageEnabledInput")
    def analytical_storage_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "analyticalStorageEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="analyticalStorageInput")
    def analytical_storage_input(
        self,
    ) -> typing.Optional["CosmosdbAccountAnalyticalStorage"]:
        return typing.cast(typing.Optional["CosmosdbAccountAnalyticalStorage"], jsii.get(self, "analyticalStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="backupInput")
    def backup_input(self) -> typing.Optional["CosmosdbAccountBackup"]:
        return typing.cast(typing.Optional["CosmosdbAccountBackup"], jsii.get(self, "backupInput"))

    @builtins.property
    @jsii.member(jsii_name="capabilitiesInput")
    def capabilities_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountCapabilities"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountCapabilities"]]], jsii.get(self, "capabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional["CosmosdbAccountCapacity"]:
        return typing.cast(typing.Optional["CosmosdbAccountCapacity"], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="consistencyPolicyInput")
    def consistency_policy_input(
        self,
    ) -> typing.Optional["CosmosdbAccountConsistencyPolicy"]:
        return typing.cast(typing.Optional["CosmosdbAccountConsistencyPolicy"], jsii.get(self, "consistencyPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="corsRuleInput")
    def cors_rule_input(self) -> typing.Optional["CosmosdbAccountCorsRule"]:
        return typing.cast(typing.Optional["CosmosdbAccountCorsRule"], jsii.get(self, "corsRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="createModeInput")
    def create_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createModeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultIdentityTypeInput")
    def default_identity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultIdentityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticFailoverInput")
    def enable_automatic_failover_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutomaticFailoverInput"))

    @builtins.property
    @jsii.member(jsii_name="enableFreeTierInput")
    def enable_free_tier_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableFreeTierInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMultipleWriteLocationsInput")
    def enable_multiple_write_locations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableMultipleWriteLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="geoLocationInput")
    def geo_location_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountGeoLocation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountGeoLocation"]]], jsii.get(self, "geoLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["CosmosdbAccountIdentity"]:
        return typing.cast(typing.Optional["CosmosdbAccountIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRangeFilterInput")
    def ip_range_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipRangeFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="isVirtualNetworkFilterEnabledInput")
    def is_virtual_network_filter_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isVirtualNetworkFilterEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyIdInput")
    def key_vault_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="localAuthenticationDisabledInput")
    def local_authentication_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localAuthenticationDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="mongoServerVersionInput")
    def mongo_server_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mongoServerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkAclBypassForAzureServicesInput")
    def network_acl_bypass_for_azure_services_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "networkAclBypassForAzureServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="networkAclBypassIdsInput")
    def network_acl_bypass_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networkAclBypassIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="offerTypeInput")
    def offer_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offerTypeInput"))

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
    @jsii.member(jsii_name="restoreInput")
    def restore_input(self) -> typing.Optional["CosmosdbAccountRestore"]:
        return typing.cast(typing.Optional["CosmosdbAccountRestore"], jsii.get(self, "restoreInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CosmosdbAccountTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CosmosdbAccountTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkRuleInput")
    def virtual_network_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountVirtualNetworkRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountVirtualNetworkRule"]]], jsii.get(self, "virtualNetworkRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyMetadataWritesEnabled")
    def access_key_metadata_writes_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "accessKeyMetadataWritesEnabled"))

    @access_key_metadata_writes_enabled.setter
    def access_key_metadata_writes_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "access_key_metadata_writes_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKeyMetadataWritesEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="analyticalStorageEnabled")
    def analytical_storage_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "analyticalStorageEnabled"))

    @analytical_storage_enabled.setter
    def analytical_storage_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "analytical_storage_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analyticalStorageEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="createMode")
    def create_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createMode"))

    @create_mode.setter
    def create_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "create_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createMode", value)

    @builtins.property
    @jsii.member(jsii_name="defaultIdentityType")
    def default_identity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultIdentityType"))

    @default_identity_type.setter
    def default_identity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "default_identity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultIdentityType", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticFailover")
    def enable_automatic_failover(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutomaticFailover"))

    @enable_automatic_failover.setter
    def enable_automatic_failover(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "enable_automatic_failover").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticFailover", value)

    @builtins.property
    @jsii.member(jsii_name="enableFreeTier")
    def enable_free_tier(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableFreeTier"))

    @enable_free_tier.setter
    def enable_free_tier(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "enable_free_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFreeTier", value)

    @builtins.property
    @jsii.member(jsii_name="enableMultipleWriteLocations")
    def enable_multiple_write_locations(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableMultipleWriteLocations"))

    @enable_multiple_write_locations.setter
    def enable_multiple_write_locations(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "enable_multiple_write_locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMultipleWriteLocations", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipRangeFilter")
    def ip_range_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipRangeFilter"))

    @ip_range_filter.setter
    def ip_range_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "ip_range_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRangeFilter", value)

    @builtins.property
    @jsii.member(jsii_name="isVirtualNetworkFilterEnabled")
    def is_virtual_network_filter_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isVirtualNetworkFilterEnabled"))

    @is_virtual_network_filter_enabled.setter
    def is_virtual_network_filter_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "is_virtual_network_filter_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isVirtualNetworkFilterEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultKeyId")
    def key_vault_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultKeyId"))

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "key_vault_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="localAuthenticationDisabled")
    def local_authentication_disabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localAuthenticationDisabled"))

    @local_authentication_disabled.setter
    def local_authentication_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "local_authentication_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAuthenticationDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="mongoServerVersion")
    def mongo_server_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mongoServerVersion"))

    @mongo_server_version.setter
    def mongo_server_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "mongo_server_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mongoServerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkAclBypassForAzureServices")
    def network_acl_bypass_for_azure_services(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "networkAclBypassForAzureServices"))

    @network_acl_bypass_for_azure_services.setter
    def network_acl_bypass_for_azure_services(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "network_acl_bypass_for_azure_services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkAclBypassForAzureServices", value)

    @builtins.property
    @jsii.member(jsii_name="networkAclBypassIds")
    def network_acl_bypass_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkAclBypassIds"))

    @network_acl_bypass_ids.setter
    def network_acl_bypass_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "network_acl_bypass_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkAclBypassIds", value)

    @builtins.property
    @jsii.member(jsii_name="offerType")
    def offer_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offerType"))

    @offer_type.setter
    def offer_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "offer_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offerType", value)

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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccount, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountAnalyticalStorage",
    jsii_struct_bases=[],
    name_mapping={"schema_type": "schemaType"},
)
class CosmosdbAccountAnalyticalStorage:
    def __init__(self, *, schema_type: builtins.str) -> None:
        '''
        :param schema_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#schema_type CosmosdbAccount#schema_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountAnalyticalStorage.__init__)
            check_type(argname="argument schema_type", value=schema_type, expected_type=type_hints["schema_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "schema_type": schema_type,
        }

    @builtins.property
    def schema_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#schema_type CosmosdbAccount#schema_type}.'''
        result = self._values.get("schema_type")
        assert result is not None, "Required property 'schema_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountAnalyticalStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountAnalyticalStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountAnalyticalStorageOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountAnalyticalStorageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="schemaTypeInput")
    def schema_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaType")
    def schema_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaType"))

    @schema_type.setter
    def schema_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountAnalyticalStorageOutputReference, "schema_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbAccountAnalyticalStorage]:
        return typing.cast(typing.Optional[CosmosdbAccountAnalyticalStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CosmosdbAccountAnalyticalStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountAnalyticalStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountBackup",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "interval_in_minutes": "intervalInMinutes",
        "retention_in_hours": "retentionInHours",
        "storage_redundancy": "storageRedundancy",
    },
)
class CosmosdbAccountBackup:
    def __init__(
        self,
        *,
        type: builtins.str,
        interval_in_minutes: typing.Optional[jsii.Number] = None,
        retention_in_hours: typing.Optional[jsii.Number] = None,
        storage_redundancy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#type CosmosdbAccount#type}.
        :param interval_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#interval_in_minutes CosmosdbAccount#interval_in_minutes}.
        :param retention_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#retention_in_hours CosmosdbAccount#retention_in_hours}.
        :param storage_redundancy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#storage_redundancy CosmosdbAccount#storage_redundancy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountBackup.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument interval_in_minutes", value=interval_in_minutes, expected_type=type_hints["interval_in_minutes"])
            check_type(argname="argument retention_in_hours", value=retention_in_hours, expected_type=type_hints["retention_in_hours"])
            check_type(argname="argument storage_redundancy", value=storage_redundancy, expected_type=type_hints["storage_redundancy"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if interval_in_minutes is not None:
            self._values["interval_in_minutes"] = interval_in_minutes
        if retention_in_hours is not None:
            self._values["retention_in_hours"] = retention_in_hours
        if storage_redundancy is not None:
            self._values["storage_redundancy"] = storage_redundancy

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#type CosmosdbAccount#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def interval_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#interval_in_minutes CosmosdbAccount#interval_in_minutes}.'''
        result = self._values.get("interval_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retention_in_hours(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#retention_in_hours CosmosdbAccount#retention_in_hours}.'''
        result = self._values.get("retention_in_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_redundancy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#storage_redundancy CosmosdbAccount#storage_redundancy}.'''
        result = self._values.get("storage_redundancy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountBackupOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountBackupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIntervalInMinutes")
    def reset_interval_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntervalInMinutes", []))

    @jsii.member(jsii_name="resetRetentionInHours")
    def reset_retention_in_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionInHours", []))

    @jsii.member(jsii_name="resetStorageRedundancy")
    def reset_storage_redundancy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageRedundancy", []))

    @builtins.property
    @jsii.member(jsii_name="intervalInMinutesInput")
    def interval_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInHoursInput")
    def retention_in_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="storageRedundancyInput")
    def storage_redundancy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageRedundancyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInMinutes")
    def interval_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalInMinutes"))

    @interval_in_minutes.setter
    def interval_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountBackupOutputReference, "interval_in_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInHours")
    def retention_in_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInHours"))

    @retention_in_hours.setter
    def retention_in_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountBackupOutputReference, "retention_in_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInHours", value)

    @builtins.property
    @jsii.member(jsii_name="storageRedundancy")
    def storage_redundancy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageRedundancy"))

    @storage_redundancy.setter
    def storage_redundancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountBackupOutputReference, "storage_redundancy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageRedundancy", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountBackupOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbAccountBackup]:
        return typing.cast(typing.Optional[CosmosdbAccountBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CosmosdbAccountBackup]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountBackupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountCapabilities",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CosmosdbAccountCapabilities:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#name CosmosdbAccount#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountCapabilities.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#name CosmosdbAccount#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountCapabilitiesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountCapabilitiesList",
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
            type_hints = typing.get_type_hints(CosmosdbAccountCapabilitiesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CosmosdbAccountCapabilitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountCapabilitiesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbAccountCapabilitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCapabilitiesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCapabilitiesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCapabilitiesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountCapabilities]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountCapabilities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountCapabilities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCapabilitiesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbAccountCapabilitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountCapabilitiesOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountCapabilitiesOutputReference.__init__)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCapabilitiesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbAccountCapabilities, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbAccountCapabilities, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbAccountCapabilities, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCapabilitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountCapacity",
    jsii_struct_bases=[],
    name_mapping={"total_throughput_limit": "totalThroughputLimit"},
)
class CosmosdbAccountCapacity:
    def __init__(self, *, total_throughput_limit: jsii.Number) -> None:
        '''
        :param total_throughput_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#total_throughput_limit CosmosdbAccount#total_throughput_limit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountCapacity.__init__)
            check_type(argname="argument total_throughput_limit", value=total_throughput_limit, expected_type=type_hints["total_throughput_limit"])
        self._values: typing.Dict[str, typing.Any] = {
            "total_throughput_limit": total_throughput_limit,
        }

    @builtins.property
    def total_throughput_limit(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#total_throughput_limit CosmosdbAccount#total_throughput_limit}.'''
        result = self._values.get("total_throughput_limit")
        assert result is not None, "Required property 'total_throughput_limit' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountCapacityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountCapacityOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountCapacityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="totalThroughputLimitInput")
    def total_throughput_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "totalThroughputLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="totalThroughputLimit")
    def total_throughput_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "totalThroughputLimit"))

    @total_throughput_limit.setter
    def total_throughput_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCapacityOutputReference, "total_throughput_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalThroughputLimit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbAccountCapacity]:
        return typing.cast(typing.Optional[CosmosdbAccountCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CosmosdbAccountCapacity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCapacityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "consistency_policy": "consistencyPolicy",
        "geo_location": "geoLocation",
        "location": "location",
        "name": "name",
        "offer_type": "offerType",
        "resource_group_name": "resourceGroupName",
        "access_key_metadata_writes_enabled": "accessKeyMetadataWritesEnabled",
        "analytical_storage": "analyticalStorage",
        "analytical_storage_enabled": "analyticalStorageEnabled",
        "backup": "backup",
        "capabilities": "capabilities",
        "capacity": "capacity",
        "cors_rule": "corsRule",
        "create_mode": "createMode",
        "default_identity_type": "defaultIdentityType",
        "enable_automatic_failover": "enableAutomaticFailover",
        "enable_free_tier": "enableFreeTier",
        "enable_multiple_write_locations": "enableMultipleWriteLocations",
        "id": "id",
        "identity": "identity",
        "ip_range_filter": "ipRangeFilter",
        "is_virtual_network_filter_enabled": "isVirtualNetworkFilterEnabled",
        "key_vault_key_id": "keyVaultKeyId",
        "kind": "kind",
        "local_authentication_disabled": "localAuthenticationDisabled",
        "mongo_server_version": "mongoServerVersion",
        "network_acl_bypass_for_azure_services": "networkAclBypassForAzureServices",
        "network_acl_bypass_ids": "networkAclBypassIds",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "restore": "restore",
        "tags": "tags",
        "timeouts": "timeouts",
        "virtual_network_rule": "virtualNetworkRule",
    },
)
class CosmosdbAccountConfig(cdktf.TerraformMetaArguments):
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
        consistency_policy: typing.Union["CosmosdbAccountConsistencyPolicy", typing.Dict[str, typing.Any]],
        geo_location: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountGeoLocation", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        offer_type: builtins.str,
        resource_group_name: builtins.str,
        access_key_metadata_writes_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        analytical_storage: typing.Optional[typing.Union[CosmosdbAccountAnalyticalStorage, typing.Dict[str, typing.Any]]] = None,
        analytical_storage_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backup: typing.Optional[typing.Union[CosmosdbAccountBackup, typing.Dict[str, typing.Any]]] = None,
        capabilities: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CosmosdbAccountCapabilities, typing.Dict[str, typing.Any]]]]] = None,
        capacity: typing.Optional[typing.Union[CosmosdbAccountCapacity, typing.Dict[str, typing.Any]]] = None,
        cors_rule: typing.Optional[typing.Union["CosmosdbAccountCorsRule", typing.Dict[str, typing.Any]]] = None,
        create_mode: typing.Optional[builtins.str] = None,
        default_identity_type: typing.Optional[builtins.str] = None,
        enable_automatic_failover: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_free_tier: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_multiple_write_locations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["CosmosdbAccountIdentity", typing.Dict[str, typing.Any]]] = None,
        ip_range_filter: typing.Optional[builtins.str] = None,
        is_virtual_network_filter_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_vault_key_id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        local_authentication_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mongo_server_version: typing.Optional[builtins.str] = None,
        network_acl_bypass_for_azure_services: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_acl_bypass_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restore: typing.Optional[typing.Union["CosmosdbAccountRestore", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CosmosdbAccountTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountVirtualNetworkRule", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param consistency_policy: consistency_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#consistency_policy CosmosdbAccount#consistency_policy}
        :param geo_location: geo_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#geo_location CosmosdbAccount#geo_location}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#location CosmosdbAccount#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#name CosmosdbAccount#name}.
        :param offer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#offer_type CosmosdbAccount#offer_type}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#resource_group_name CosmosdbAccount#resource_group_name}.
        :param access_key_metadata_writes_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#access_key_metadata_writes_enabled CosmosdbAccount#access_key_metadata_writes_enabled}.
        :param analytical_storage: analytical_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#analytical_storage CosmosdbAccount#analytical_storage}
        :param analytical_storage_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#analytical_storage_enabled CosmosdbAccount#analytical_storage_enabled}.
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#backup CosmosdbAccount#backup}
        :param capabilities: capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#capabilities CosmosdbAccount#capabilities}
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#capacity CosmosdbAccount#capacity}
        :param cors_rule: cors_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#cors_rule CosmosdbAccount#cors_rule}
        :param create_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#create_mode CosmosdbAccount#create_mode}.
        :param default_identity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#default_identity_type CosmosdbAccount#default_identity_type}.
        :param enable_automatic_failover: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_automatic_failover CosmosdbAccount#enable_automatic_failover}.
        :param enable_free_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_free_tier CosmosdbAccount#enable_free_tier}.
        :param enable_multiple_write_locations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_multiple_write_locations CosmosdbAccount#enable_multiple_write_locations}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#id CosmosdbAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#identity CosmosdbAccount#identity}
        :param ip_range_filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#ip_range_filter CosmosdbAccount#ip_range_filter}.
        :param is_virtual_network_filter_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#is_virtual_network_filter_enabled CosmosdbAccount#is_virtual_network_filter_enabled}.
        :param key_vault_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#key_vault_key_id CosmosdbAccount#key_vault_key_id}.
        :param kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#kind CosmosdbAccount#kind}.
        :param local_authentication_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#local_authentication_disabled CosmosdbAccount#local_authentication_disabled}.
        :param mongo_server_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#mongo_server_version CosmosdbAccount#mongo_server_version}.
        :param network_acl_bypass_for_azure_services: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#network_acl_bypass_for_azure_services CosmosdbAccount#network_acl_bypass_for_azure_services}.
        :param network_acl_bypass_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#network_acl_bypass_ids CosmosdbAccount#network_acl_bypass_ids}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#public_network_access_enabled CosmosdbAccount#public_network_access_enabled}.
        :param restore: restore block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#restore CosmosdbAccount#restore}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#tags CosmosdbAccount#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#timeouts CosmosdbAccount#timeouts}
        :param virtual_network_rule: virtual_network_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#virtual_network_rule CosmosdbAccount#virtual_network_rule}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(consistency_policy, dict):
            consistency_policy = CosmosdbAccountConsistencyPolicy(**consistency_policy)
        if isinstance(analytical_storage, dict):
            analytical_storage = CosmosdbAccountAnalyticalStorage(**analytical_storage)
        if isinstance(backup, dict):
            backup = CosmosdbAccountBackup(**backup)
        if isinstance(capacity, dict):
            capacity = CosmosdbAccountCapacity(**capacity)
        if isinstance(cors_rule, dict):
            cors_rule = CosmosdbAccountCorsRule(**cors_rule)
        if isinstance(identity, dict):
            identity = CosmosdbAccountIdentity(**identity)
        if isinstance(restore, dict):
            restore = CosmosdbAccountRestore(**restore)
        if isinstance(timeouts, dict):
            timeouts = CosmosdbAccountTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument consistency_policy", value=consistency_policy, expected_type=type_hints["consistency_policy"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument offer_type", value=offer_type, expected_type=type_hints["offer_type"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument access_key_metadata_writes_enabled", value=access_key_metadata_writes_enabled, expected_type=type_hints["access_key_metadata_writes_enabled"])
            check_type(argname="argument analytical_storage", value=analytical_storage, expected_type=type_hints["analytical_storage"])
            check_type(argname="argument analytical_storage_enabled", value=analytical_storage_enabled, expected_type=type_hints["analytical_storage_enabled"])
            check_type(argname="argument backup", value=backup, expected_type=type_hints["backup"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument cors_rule", value=cors_rule, expected_type=type_hints["cors_rule"])
            check_type(argname="argument create_mode", value=create_mode, expected_type=type_hints["create_mode"])
            check_type(argname="argument default_identity_type", value=default_identity_type, expected_type=type_hints["default_identity_type"])
            check_type(argname="argument enable_automatic_failover", value=enable_automatic_failover, expected_type=type_hints["enable_automatic_failover"])
            check_type(argname="argument enable_free_tier", value=enable_free_tier, expected_type=type_hints["enable_free_tier"])
            check_type(argname="argument enable_multiple_write_locations", value=enable_multiple_write_locations, expected_type=type_hints["enable_multiple_write_locations"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument ip_range_filter", value=ip_range_filter, expected_type=type_hints["ip_range_filter"])
            check_type(argname="argument is_virtual_network_filter_enabled", value=is_virtual_network_filter_enabled, expected_type=type_hints["is_virtual_network_filter_enabled"])
            check_type(argname="argument key_vault_key_id", value=key_vault_key_id, expected_type=type_hints["key_vault_key_id"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument local_authentication_disabled", value=local_authentication_disabled, expected_type=type_hints["local_authentication_disabled"])
            check_type(argname="argument mongo_server_version", value=mongo_server_version, expected_type=type_hints["mongo_server_version"])
            check_type(argname="argument network_acl_bypass_for_azure_services", value=network_acl_bypass_for_azure_services, expected_type=type_hints["network_acl_bypass_for_azure_services"])
            check_type(argname="argument network_acl_bypass_ids", value=network_acl_bypass_ids, expected_type=type_hints["network_acl_bypass_ids"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument restore", value=restore, expected_type=type_hints["restore"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_network_rule", value=virtual_network_rule, expected_type=type_hints["virtual_network_rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "consistency_policy": consistency_policy,
            "geo_location": geo_location,
            "location": location,
            "name": name,
            "offer_type": offer_type,
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
        if access_key_metadata_writes_enabled is not None:
            self._values["access_key_metadata_writes_enabled"] = access_key_metadata_writes_enabled
        if analytical_storage is not None:
            self._values["analytical_storage"] = analytical_storage
        if analytical_storage_enabled is not None:
            self._values["analytical_storage_enabled"] = analytical_storage_enabled
        if backup is not None:
            self._values["backup"] = backup
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if capacity is not None:
            self._values["capacity"] = capacity
        if cors_rule is not None:
            self._values["cors_rule"] = cors_rule
        if create_mode is not None:
            self._values["create_mode"] = create_mode
        if default_identity_type is not None:
            self._values["default_identity_type"] = default_identity_type
        if enable_automatic_failover is not None:
            self._values["enable_automatic_failover"] = enable_automatic_failover
        if enable_free_tier is not None:
            self._values["enable_free_tier"] = enable_free_tier
        if enable_multiple_write_locations is not None:
            self._values["enable_multiple_write_locations"] = enable_multiple_write_locations
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if ip_range_filter is not None:
            self._values["ip_range_filter"] = ip_range_filter
        if is_virtual_network_filter_enabled is not None:
            self._values["is_virtual_network_filter_enabled"] = is_virtual_network_filter_enabled
        if key_vault_key_id is not None:
            self._values["key_vault_key_id"] = key_vault_key_id
        if kind is not None:
            self._values["kind"] = kind
        if local_authentication_disabled is not None:
            self._values["local_authentication_disabled"] = local_authentication_disabled
        if mongo_server_version is not None:
            self._values["mongo_server_version"] = mongo_server_version
        if network_acl_bypass_for_azure_services is not None:
            self._values["network_acl_bypass_for_azure_services"] = network_acl_bypass_for_azure_services
        if network_acl_bypass_ids is not None:
            self._values["network_acl_bypass_ids"] = network_acl_bypass_ids
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if restore is not None:
            self._values["restore"] = restore
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if virtual_network_rule is not None:
            self._values["virtual_network_rule"] = virtual_network_rule

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
    def consistency_policy(self) -> "CosmosdbAccountConsistencyPolicy":
        '''consistency_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#consistency_policy CosmosdbAccount#consistency_policy}
        '''
        result = self._values.get("consistency_policy")
        assert result is not None, "Required property 'consistency_policy' is missing"
        return typing.cast("CosmosdbAccountConsistencyPolicy", result)

    @builtins.property
    def geo_location(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountGeoLocation"]]:
        '''geo_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#geo_location CosmosdbAccount#geo_location}
        '''
        result = self._values.get("geo_location")
        assert result is not None, "Required property 'geo_location' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountGeoLocation"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#location CosmosdbAccount#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#name CosmosdbAccount#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def offer_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#offer_type CosmosdbAccount#offer_type}.'''
        result = self._values.get("offer_type")
        assert result is not None, "Required property 'offer_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#resource_group_name CosmosdbAccount#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key_metadata_writes_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#access_key_metadata_writes_enabled CosmosdbAccount#access_key_metadata_writes_enabled}.'''
        result = self._values.get("access_key_metadata_writes_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def analytical_storage(self) -> typing.Optional[CosmosdbAccountAnalyticalStorage]:
        '''analytical_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#analytical_storage CosmosdbAccount#analytical_storage}
        '''
        result = self._values.get("analytical_storage")
        return typing.cast(typing.Optional[CosmosdbAccountAnalyticalStorage], result)

    @builtins.property
    def analytical_storage_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#analytical_storage_enabled CosmosdbAccount#analytical_storage_enabled}.'''
        result = self._values.get("analytical_storage_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def backup(self) -> typing.Optional[CosmosdbAccountBackup]:
        '''backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#backup CosmosdbAccount#backup}
        '''
        result = self._values.get("backup")
        return typing.cast(typing.Optional[CosmosdbAccountBackup], result)

    @builtins.property
    def capabilities(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountCapabilities]]]:
        '''capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#capabilities CosmosdbAccount#capabilities}
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountCapabilities]]], result)

    @builtins.property
    def capacity(self) -> typing.Optional[CosmosdbAccountCapacity]:
        '''capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#capacity CosmosdbAccount#capacity}
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[CosmosdbAccountCapacity], result)

    @builtins.property
    def cors_rule(self) -> typing.Optional["CosmosdbAccountCorsRule"]:
        '''cors_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#cors_rule CosmosdbAccount#cors_rule}
        '''
        result = self._values.get("cors_rule")
        return typing.cast(typing.Optional["CosmosdbAccountCorsRule"], result)

    @builtins.property
    def create_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#create_mode CosmosdbAccount#create_mode}.'''
        result = self._values.get("create_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_identity_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#default_identity_type CosmosdbAccount#default_identity_type}.'''
        result = self._values.get("default_identity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_automatic_failover(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_automatic_failover CosmosdbAccount#enable_automatic_failover}.'''
        result = self._values.get("enable_automatic_failover")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_free_tier(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_free_tier CosmosdbAccount#enable_free_tier}.'''
        result = self._values.get("enable_free_tier")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_multiple_write_locations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#enable_multiple_write_locations CosmosdbAccount#enable_multiple_write_locations}.'''
        result = self._values.get("enable_multiple_write_locations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#id CosmosdbAccount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["CosmosdbAccountIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#identity CosmosdbAccount#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["CosmosdbAccountIdentity"], result)

    @builtins.property
    def ip_range_filter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#ip_range_filter CosmosdbAccount#ip_range_filter}.'''
        result = self._values.get("ip_range_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_virtual_network_filter_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#is_virtual_network_filter_enabled CosmosdbAccount#is_virtual_network_filter_enabled}.'''
        result = self._values.get("is_virtual_network_filter_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_vault_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#key_vault_key_id CosmosdbAccount#key_vault_key_id}.'''
        result = self._values.get("key_vault_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#kind CosmosdbAccount#kind}.'''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_authentication_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#local_authentication_disabled CosmosdbAccount#local_authentication_disabled}.'''
        result = self._values.get("local_authentication_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def mongo_server_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#mongo_server_version CosmosdbAccount#mongo_server_version}.'''
        result = self._values.get("mongo_server_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_acl_bypass_for_azure_services(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#network_acl_bypass_for_azure_services CosmosdbAccount#network_acl_bypass_for_azure_services}.'''
        result = self._values.get("network_acl_bypass_for_azure_services")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def network_acl_bypass_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#network_acl_bypass_ids CosmosdbAccount#network_acl_bypass_ids}.'''
        result = self._values.get("network_acl_bypass_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#public_network_access_enabled CosmosdbAccount#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def restore(self) -> typing.Optional["CosmosdbAccountRestore"]:
        '''restore block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#restore CosmosdbAccount#restore}
        '''
        result = self._values.get("restore")
        return typing.cast(typing.Optional["CosmosdbAccountRestore"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#tags CosmosdbAccount#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CosmosdbAccountTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#timeouts CosmosdbAccount#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CosmosdbAccountTimeouts"], result)

    @builtins.property
    def virtual_network_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountVirtualNetworkRule"]]]:
        '''virtual_network_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#virtual_network_rule CosmosdbAccount#virtual_network_rule}
        '''
        result = self._values.get("virtual_network_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountVirtualNetworkRule"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountConsistencyPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "consistency_level": "consistencyLevel",
        "max_interval_in_seconds": "maxIntervalInSeconds",
        "max_staleness_prefix": "maxStalenessPrefix",
    },
)
class CosmosdbAccountConsistencyPolicy:
    def __init__(
        self,
        *,
        consistency_level: builtins.str,
        max_interval_in_seconds: typing.Optional[jsii.Number] = None,
        max_staleness_prefix: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param consistency_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#consistency_level CosmosdbAccount#consistency_level}.
        :param max_interval_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_interval_in_seconds CosmosdbAccount#max_interval_in_seconds}.
        :param max_staleness_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_staleness_prefix CosmosdbAccount#max_staleness_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountConsistencyPolicy.__init__)
            check_type(argname="argument consistency_level", value=consistency_level, expected_type=type_hints["consistency_level"])
            check_type(argname="argument max_interval_in_seconds", value=max_interval_in_seconds, expected_type=type_hints["max_interval_in_seconds"])
            check_type(argname="argument max_staleness_prefix", value=max_staleness_prefix, expected_type=type_hints["max_staleness_prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "consistency_level": consistency_level,
        }
        if max_interval_in_seconds is not None:
            self._values["max_interval_in_seconds"] = max_interval_in_seconds
        if max_staleness_prefix is not None:
            self._values["max_staleness_prefix"] = max_staleness_prefix

    @builtins.property
    def consistency_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#consistency_level CosmosdbAccount#consistency_level}.'''
        result = self._values.get("consistency_level")
        assert result is not None, "Required property 'consistency_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_interval_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_interval_in_seconds CosmosdbAccount#max_interval_in_seconds}.'''
        result = self._values.get("max_interval_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_staleness_prefix(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_staleness_prefix CosmosdbAccount#max_staleness_prefix}.'''
        result = self._values.get("max_staleness_prefix")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountConsistencyPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountConsistencyPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountConsistencyPolicyOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountConsistencyPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxIntervalInSeconds")
    def reset_max_interval_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIntervalInSeconds", []))

    @jsii.member(jsii_name="resetMaxStalenessPrefix")
    def reset_max_staleness_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxStalenessPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="consistencyLevelInput")
    def consistency_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consistencyLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIntervalInSecondsInput")
    def max_interval_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIntervalInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxStalenessPrefixInput")
    def max_staleness_prefix_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxStalenessPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="consistencyLevel")
    def consistency_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consistencyLevel"))

    @consistency_level.setter
    def consistency_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountConsistencyPolicyOutputReference, "consistency_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consistencyLevel", value)

    @builtins.property
    @jsii.member(jsii_name="maxIntervalInSeconds")
    def max_interval_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIntervalInSeconds"))

    @max_interval_in_seconds.setter
    def max_interval_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountConsistencyPolicyOutputReference, "max_interval_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIntervalInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maxStalenessPrefix")
    def max_staleness_prefix(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxStalenessPrefix"))

    @max_staleness_prefix.setter
    def max_staleness_prefix(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountConsistencyPolicyOutputReference, "max_staleness_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxStalenessPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbAccountConsistencyPolicy]:
        return typing.cast(typing.Optional[CosmosdbAccountConsistencyPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CosmosdbAccountConsistencyPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountConsistencyPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountCorsRule",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_headers": "allowedHeaders",
        "allowed_methods": "allowedMethods",
        "allowed_origins": "allowedOrigins",
        "exposed_headers": "exposedHeaders",
        "max_age_in_seconds": "maxAgeInSeconds",
    },
)
class CosmosdbAccountCorsRule:
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
        :param allowed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_headers CosmosdbAccount#allowed_headers}.
        :param allowed_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_methods CosmosdbAccount#allowed_methods}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_origins CosmosdbAccount#allowed_origins}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#exposed_headers CosmosdbAccount#exposed_headers}.
        :param max_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_age_in_seconds CosmosdbAccount#max_age_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountCorsRule.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_headers CosmosdbAccount#allowed_headers}.'''
        result = self._values.get("allowed_headers")
        assert result is not None, "Required property 'allowed_headers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_methods(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_methods CosmosdbAccount#allowed_methods}.'''
        result = self._values.get("allowed_methods")
        assert result is not None, "Required property 'allowed_methods' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#allowed_origins CosmosdbAccount#allowed_origins}.'''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def exposed_headers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#exposed_headers CosmosdbAccount#exposed_headers}.'''
        result = self._values.get("exposed_headers")
        assert result is not None, "Required property 'exposed_headers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def max_age_in_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#max_age_in_seconds CosmosdbAccount#max_age_in_seconds}.'''
        result = self._values.get("max_age_in_seconds")
        assert result is not None, "Required property 'max_age_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountCorsRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountCorsRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountCorsRuleOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountCorsRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCorsRuleOutputReference, "allowed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowedMethods")
    def allowed_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedMethods"))

    @allowed_methods.setter
    def allowed_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCorsRuleOutputReference, "allowed_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCorsRuleOutputReference, "allowed_origins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="exposedHeaders")
    def exposed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposedHeaders"))

    @exposed_headers.setter
    def exposed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCorsRuleOutputReference, "exposed_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAgeInSeconds")
    def max_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAgeInSeconds"))

    @max_age_in_seconds.setter
    def max_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCorsRuleOutputReference, "max_age_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbAccountCorsRule]:
        return typing.cast(typing.Optional[CosmosdbAccountCorsRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CosmosdbAccountCorsRule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountCorsRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountGeoLocation",
    jsii_struct_bases=[],
    name_mapping={
        "failover_priority": "failoverPriority",
        "location": "location",
        "zone_redundant": "zoneRedundant",
    },
)
class CosmosdbAccountGeoLocation:
    def __init__(
        self,
        *,
        failover_priority: jsii.Number,
        location: builtins.str,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param failover_priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#failover_priority CosmosdbAccount#failover_priority}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#location CosmosdbAccount#location}.
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#zone_redundant CosmosdbAccount#zone_redundant}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountGeoLocation.__init__)
            check_type(argname="argument failover_priority", value=failover_priority, expected_type=type_hints["failover_priority"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument zone_redundant", value=zone_redundant, expected_type=type_hints["zone_redundant"])
        self._values: typing.Dict[str, typing.Any] = {
            "failover_priority": failover_priority,
            "location": location,
        }
        if zone_redundant is not None:
            self._values["zone_redundant"] = zone_redundant

    @builtins.property
    def failover_priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#failover_priority CosmosdbAccount#failover_priority}.'''
        result = self._values.get("failover_priority")
        assert result is not None, "Required property 'failover_priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#location CosmosdbAccount#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_redundant(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#zone_redundant CosmosdbAccount#zone_redundant}.'''
        result = self._values.get("zone_redundant")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountGeoLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountGeoLocationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountGeoLocationList",
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
            type_hints = typing.get_type_hints(CosmosdbAccountGeoLocationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CosmosdbAccountGeoLocationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountGeoLocationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbAccountGeoLocationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountGeoLocationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountGeoLocationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountGeoLocationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountGeoLocation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountGeoLocation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountGeoLocation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountGeoLocationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbAccountGeoLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountGeoLocationOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountGeoLocationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetZoneRedundant")
    def reset_zone_redundant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneRedundant", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="failoverPriorityInput")
    def failover_priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failoverPriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneRedundantInput")
    def zone_redundant_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "zoneRedundantInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverPriority")
    def failover_priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failoverPriority"))

    @failover_priority.setter
    def failover_priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountGeoLocationOutputReference, "failover_priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failoverPriority", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountGeoLocationOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="zoneRedundant")
    def zone_redundant(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "zoneRedundant"))

    @zone_redundant.setter
    def zone_redundant(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountGeoLocationOutputReference, "zone_redundant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneRedundant", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbAccountGeoLocation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbAccountGeoLocation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbAccountGeoLocation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountGeoLocationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class CosmosdbAccountIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#type CosmosdbAccount#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#identity_ids CosmosdbAccount#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#type CosmosdbAccount#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#identity_ids CosmosdbAccount#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountIdentityOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountIdentityOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbAccountIdentity]:
        return typing.cast(typing.Optional[CosmosdbAccountIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CosmosdbAccountIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountRestore",
    jsii_struct_bases=[],
    name_mapping={
        "restore_timestamp_in_utc": "restoreTimestampInUtc",
        "source_cosmosdb_account_id": "sourceCosmosdbAccountId",
        "database": "database",
    },
)
class CosmosdbAccountRestore:
    def __init__(
        self,
        *,
        restore_timestamp_in_utc: builtins.str,
        source_cosmosdb_account_id: builtins.str,
        database: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CosmosdbAccountRestoreDatabase", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param restore_timestamp_in_utc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#restore_timestamp_in_utc CosmosdbAccount#restore_timestamp_in_utc}.
        :param source_cosmosdb_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#source_cosmosdb_account_id CosmosdbAccount#source_cosmosdb_account_id}.
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#database CosmosdbAccount#database}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountRestore.__init__)
            check_type(argname="argument restore_timestamp_in_utc", value=restore_timestamp_in_utc, expected_type=type_hints["restore_timestamp_in_utc"])
            check_type(argname="argument source_cosmosdb_account_id", value=source_cosmosdb_account_id, expected_type=type_hints["source_cosmosdb_account_id"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
        self._values: typing.Dict[str, typing.Any] = {
            "restore_timestamp_in_utc": restore_timestamp_in_utc,
            "source_cosmosdb_account_id": source_cosmosdb_account_id,
        }
        if database is not None:
            self._values["database"] = database

    @builtins.property
    def restore_timestamp_in_utc(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#restore_timestamp_in_utc CosmosdbAccount#restore_timestamp_in_utc}.'''
        result = self._values.get("restore_timestamp_in_utc")
        assert result is not None, "Required property 'restore_timestamp_in_utc' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_cosmosdb_account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#source_cosmosdb_account_id CosmosdbAccount#source_cosmosdb_account_id}.'''
        result = self._values.get("source_cosmosdb_account_id")
        assert result is not None, "Required property 'source_cosmosdb_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountRestoreDatabase"]]]:
        '''database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#database CosmosdbAccount#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CosmosdbAccountRestoreDatabase"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountRestore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountRestoreDatabase",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "collection_names": "collectionNames"},
)
class CosmosdbAccountRestoreDatabase:
    def __init__(
        self,
        *,
        name: builtins.str,
        collection_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#name CosmosdbAccount#name}.
        :param collection_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#collection_names CosmosdbAccount#collection_names}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountRestoreDatabase.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument collection_names", value=collection_names, expected_type=type_hints["collection_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if collection_names is not None:
            self._values["collection_names"] = collection_names

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#name CosmosdbAccount#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collection_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#collection_names CosmosdbAccount#collection_names}.'''
        result = self._values.get("collection_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountRestoreDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountRestoreDatabaseList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountRestoreDatabaseList",
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
            type_hints = typing.get_type_hints(CosmosdbAccountRestoreDatabaseList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CosmosdbAccountRestoreDatabaseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountRestoreDatabaseList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbAccountRestoreDatabaseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreDatabaseList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreDatabaseList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreDatabaseList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountRestoreDatabase]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountRestoreDatabase]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountRestoreDatabase]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreDatabaseList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbAccountRestoreDatabaseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountRestoreDatabaseOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountRestoreDatabaseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCollectionNames")
    def reset_collection_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollectionNames", []))

    @builtins.property
    @jsii.member(jsii_name="collectionNamesInput")
    def collection_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "collectionNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="collectionNames")
    def collection_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "collectionNames"))

    @collection_names.setter
    def collection_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreDatabaseOutputReference, "collection_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionNames", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreDatabaseOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbAccountRestoreDatabase, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbAccountRestoreDatabase, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbAccountRestoreDatabase, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreDatabaseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbAccountRestoreOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountRestoreOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountRestoreOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDatabase")
    def put_database(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CosmosdbAccountRestoreDatabase, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountRestoreOutputReference.put_database)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDatabase", [value]))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> CosmosdbAccountRestoreDatabaseList:
        return typing.cast(CosmosdbAccountRestoreDatabaseList, jsii.get(self, "database"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountRestoreDatabase]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountRestoreDatabase]]], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreTimestampInUtcInput")
    def restore_timestamp_in_utc_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreTimestampInUtcInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceCosmosdbAccountIdInput")
    def source_cosmosdb_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceCosmosdbAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreTimestampInUtc")
    def restore_timestamp_in_utc(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreTimestampInUtc"))

    @restore_timestamp_in_utc.setter
    def restore_timestamp_in_utc(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreOutputReference, "restore_timestamp_in_utc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreTimestampInUtc", value)

    @builtins.property
    @jsii.member(jsii_name="sourceCosmosdbAccountId")
    def source_cosmosdb_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceCosmosdbAccountId"))

    @source_cosmosdb_account_id.setter
    def source_cosmosdb_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreOutputReference, "source_cosmosdb_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceCosmosdbAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CosmosdbAccountRestore]:
        return typing.cast(typing.Optional[CosmosdbAccountRestore], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CosmosdbAccountRestore]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountRestoreOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CosmosdbAccountTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#create CosmosdbAccount#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#delete CosmosdbAccount#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#read CosmosdbAccount#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#update CosmosdbAccount#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#create CosmosdbAccount#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#delete CosmosdbAccount#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#read CosmosdbAccount#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#update CosmosdbAccount#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbAccountTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbAccountTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbAccountTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountVirtualNetworkRule",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "ignore_missing_vnet_service_endpoint": "ignoreMissingVnetServiceEndpoint",
    },
)
class CosmosdbAccountVirtualNetworkRule:
    def __init__(
        self,
        *,
        id: builtins.str,
        ignore_missing_vnet_service_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#id CosmosdbAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_missing_vnet_service_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#ignore_missing_vnet_service_endpoint CosmosdbAccount#ignore_missing_vnet_service_endpoint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountVirtualNetworkRule.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignore_missing_vnet_service_endpoint", value=ignore_missing_vnet_service_endpoint, expected_type=type_hints["ignore_missing_vnet_service_endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if ignore_missing_vnet_service_endpoint is not None:
            self._values["ignore_missing_vnet_service_endpoint"] = ignore_missing_vnet_service_endpoint

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#id CosmosdbAccount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ignore_missing_vnet_service_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cosmosdb_account#ignore_missing_vnet_service_endpoint CosmosdbAccount#ignore_missing_vnet_service_endpoint}.'''
        result = self._values.get("ignore_missing_vnet_service_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CosmosdbAccountVirtualNetworkRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CosmosdbAccountVirtualNetworkRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountVirtualNetworkRuleList",
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
            type_hints = typing.get_type_hints(CosmosdbAccountVirtualNetworkRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CosmosdbAccountVirtualNetworkRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CosmosdbAccountVirtualNetworkRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CosmosdbAccountVirtualNetworkRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountVirtualNetworkRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountVirtualNetworkRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountVirtualNetworkRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountVirtualNetworkRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountVirtualNetworkRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CosmosdbAccountVirtualNetworkRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountVirtualNetworkRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CosmosdbAccountVirtualNetworkRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cosmosdbAccount.CosmosdbAccountVirtualNetworkRuleOutputReference",
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
            type_hints = typing.get_type_hints(CosmosdbAccountVirtualNetworkRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreMissingVnetServiceEndpoint")
    def reset_ignore_missing_vnet_service_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreMissingVnetServiceEndpoint", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingVnetServiceEndpointInput")
    def ignore_missing_vnet_service_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreMissingVnetServiceEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountVirtualNetworkRuleOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreMissingVnetServiceEndpoint"))

    @ignore_missing_vnet_service_endpoint.setter
    def ignore_missing_vnet_service_endpoint(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountVirtualNetworkRuleOutputReference, "ignore_missing_vnet_service_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreMissingVnetServiceEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CosmosdbAccountVirtualNetworkRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CosmosdbAccountVirtualNetworkRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CosmosdbAccountVirtualNetworkRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CosmosdbAccountVirtualNetworkRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CosmosdbAccount",
    "CosmosdbAccountAnalyticalStorage",
    "CosmosdbAccountAnalyticalStorageOutputReference",
    "CosmosdbAccountBackup",
    "CosmosdbAccountBackupOutputReference",
    "CosmosdbAccountCapabilities",
    "CosmosdbAccountCapabilitiesList",
    "CosmosdbAccountCapabilitiesOutputReference",
    "CosmosdbAccountCapacity",
    "CosmosdbAccountCapacityOutputReference",
    "CosmosdbAccountConfig",
    "CosmosdbAccountConsistencyPolicy",
    "CosmosdbAccountConsistencyPolicyOutputReference",
    "CosmosdbAccountCorsRule",
    "CosmosdbAccountCorsRuleOutputReference",
    "CosmosdbAccountGeoLocation",
    "CosmosdbAccountGeoLocationList",
    "CosmosdbAccountGeoLocationOutputReference",
    "CosmosdbAccountIdentity",
    "CosmosdbAccountIdentityOutputReference",
    "CosmosdbAccountRestore",
    "CosmosdbAccountRestoreDatabase",
    "CosmosdbAccountRestoreDatabaseList",
    "CosmosdbAccountRestoreDatabaseOutputReference",
    "CosmosdbAccountRestoreOutputReference",
    "CosmosdbAccountTimeouts",
    "CosmosdbAccountTimeoutsOutputReference",
    "CosmosdbAccountVirtualNetworkRule",
    "CosmosdbAccountVirtualNetworkRuleList",
    "CosmosdbAccountVirtualNetworkRuleOutputReference",
]

publication.publish()
