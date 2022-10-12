'''
# `azurerm_mssql_database`

Refer to the Terraform Registory for docs: [`azurerm_mssql_database`](https://www.terraform.io/docs/providers/azurerm/r/mssql_database).
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


class MssqlDatabase(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabase",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database azurerm_mssql_database}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        server_id: builtins.str,
        auto_pause_delay_in_minutes: typing.Optional[jsii.Number] = None,
        collation: typing.Optional[builtins.str] = None,
        create_mode: typing.Optional[builtins.str] = None,
        creation_source_database_id: typing.Optional[builtins.str] = None,
        elastic_pool_id: typing.Optional[builtins.str] = None,
        geo_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ledger_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        license_type: typing.Optional[builtins.str] = None,
        long_term_retention_policy: typing.Optional[typing.Union["MssqlDatabaseLongTermRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        maintenance_configuration_name: typing.Optional[builtins.str] = None,
        max_size_gb: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        read_replica_count: typing.Optional[jsii.Number] = None,
        read_scale: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        recover_database_id: typing.Optional[builtins.str] = None,
        restore_dropped_database_id: typing.Optional[builtins.str] = None,
        restore_point_in_time: typing.Optional[builtins.str] = None,
        sample_name: typing.Optional[builtins.str] = None,
        short_term_retention_policy: typing.Optional[typing.Union["MssqlDatabaseShortTermRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        sku_name: typing.Optional[builtins.str] = None,
        storage_account_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        threat_detection_policy: typing.Optional[typing.Union["MssqlDatabaseThreatDetectionPolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MssqlDatabaseTimeouts", typing.Dict[str, typing.Any]]] = None,
        transparent_data_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database azurerm_mssql_database} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#name MssqlDatabase#name}.
        :param server_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#server_id MssqlDatabase#server_id}.
        :param auto_pause_delay_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#auto_pause_delay_in_minutes MssqlDatabase#auto_pause_delay_in_minutes}.
        :param collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#collation MssqlDatabase#collation}.
        :param create_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#create_mode MssqlDatabase#create_mode}.
        :param creation_source_database_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#creation_source_database_id MssqlDatabase#creation_source_database_id}.
        :param elastic_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#elastic_pool_id MssqlDatabase#elastic_pool_id}.
        :param geo_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#geo_backup_enabled MssqlDatabase#geo_backup_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#id MssqlDatabase#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ledger_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#ledger_enabled MssqlDatabase#ledger_enabled}.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#license_type MssqlDatabase#license_type}.
        :param long_term_retention_policy: long_term_retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#long_term_retention_policy MssqlDatabase#long_term_retention_policy}
        :param maintenance_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#maintenance_configuration_name MssqlDatabase#maintenance_configuration_name}.
        :param max_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#max_size_gb MssqlDatabase#max_size_gb}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#min_capacity MssqlDatabase#min_capacity}.
        :param read_replica_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read_replica_count MssqlDatabase#read_replica_count}.
        :param read_scale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read_scale MssqlDatabase#read_scale}.
        :param recover_database_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#recover_database_id MssqlDatabase#recover_database_id}.
        :param restore_dropped_database_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#restore_dropped_database_id MssqlDatabase#restore_dropped_database_id}.
        :param restore_point_in_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#restore_point_in_time MssqlDatabase#restore_point_in_time}.
        :param sample_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#sample_name MssqlDatabase#sample_name}.
        :param short_term_retention_policy: short_term_retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#short_term_retention_policy MssqlDatabase#short_term_retention_policy}
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#sku_name MssqlDatabase#sku_name}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_account_type MssqlDatabase#storage_account_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#tags MssqlDatabase#tags}.
        :param threat_detection_policy: threat_detection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#threat_detection_policy MssqlDatabase#threat_detection_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#timeouts MssqlDatabase#timeouts}
        :param transparent_data_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#transparent_data_encryption_enabled MssqlDatabase#transparent_data_encryption_enabled}.
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#zone_redundant MssqlDatabase#zone_redundant}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlDatabase.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MssqlDatabaseConfig(
            name=name,
            server_id=server_id,
            auto_pause_delay_in_minutes=auto_pause_delay_in_minutes,
            collation=collation,
            create_mode=create_mode,
            creation_source_database_id=creation_source_database_id,
            elastic_pool_id=elastic_pool_id,
            geo_backup_enabled=geo_backup_enabled,
            id=id,
            ledger_enabled=ledger_enabled,
            license_type=license_type,
            long_term_retention_policy=long_term_retention_policy,
            maintenance_configuration_name=maintenance_configuration_name,
            max_size_gb=max_size_gb,
            min_capacity=min_capacity,
            read_replica_count=read_replica_count,
            read_scale=read_scale,
            recover_database_id=recover_database_id,
            restore_dropped_database_id=restore_dropped_database_id,
            restore_point_in_time=restore_point_in_time,
            sample_name=sample_name,
            short_term_retention_policy=short_term_retention_policy,
            sku_name=sku_name,
            storage_account_type=storage_account_type,
            tags=tags,
            threat_detection_policy=threat_detection_policy,
            timeouts=timeouts,
            transparent_data_encryption_enabled=transparent_data_encryption_enabled,
            zone_redundant=zone_redundant,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLongTermRetentionPolicy")
    def put_long_term_retention_policy(
        self,
        *,
        monthly_retention: typing.Optional[builtins.str] = None,
        weekly_retention: typing.Optional[builtins.str] = None,
        week_of_year: typing.Optional[jsii.Number] = None,
        yearly_retention: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monthly_retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#monthly_retention MssqlDatabase#monthly_retention}.
        :param weekly_retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#weekly_retention MssqlDatabase#weekly_retention}.
        :param week_of_year: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#week_of_year MssqlDatabase#week_of_year}.
        :param yearly_retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#yearly_retention MssqlDatabase#yearly_retention}.
        '''
        value = MssqlDatabaseLongTermRetentionPolicy(
            monthly_retention=monthly_retention,
            weekly_retention=weekly_retention,
            week_of_year=week_of_year,
            yearly_retention=yearly_retention,
        )

        return typing.cast(None, jsii.invoke(self, "putLongTermRetentionPolicy", [value]))

    @jsii.member(jsii_name="putShortTermRetentionPolicy")
    def put_short_term_retention_policy(
        self,
        *,
        retention_days: jsii.Number,
        backup_interval_in_hours: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#retention_days MssqlDatabase#retention_days}.
        :param backup_interval_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#backup_interval_in_hours MssqlDatabase#backup_interval_in_hours}.
        '''
        value = MssqlDatabaseShortTermRetentionPolicy(
            retention_days=retention_days,
            backup_interval_in_hours=backup_interval_in_hours,
        )

        return typing.cast(None, jsii.invoke(self, "putShortTermRetentionPolicy", [value]))

    @jsii.member(jsii_name="putThreatDetectionPolicy")
    def put_threat_detection_policy(
        self,
        *,
        disabled_alerts: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_account_admins: typing.Optional[builtins.str] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        retention_days: typing.Optional[jsii.Number] = None,
        state: typing.Optional[builtins.str] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disabled_alerts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#disabled_alerts MssqlDatabase#disabled_alerts}.
        :param email_account_admins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#email_account_admins MssqlDatabase#email_account_admins}.
        :param email_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#email_addresses MssqlDatabase#email_addresses}.
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#retention_days MssqlDatabase#retention_days}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#state MssqlDatabase#state}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_account_access_key MssqlDatabase#storage_account_access_key}.
        :param storage_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_endpoint MssqlDatabase#storage_endpoint}.
        '''
        value = MssqlDatabaseThreatDetectionPolicy(
            disabled_alerts=disabled_alerts,
            email_account_admins=email_account_admins,
            email_addresses=email_addresses,
            retention_days=retention_days,
            state=state,
            storage_account_access_key=storage_account_access_key,
            storage_endpoint=storage_endpoint,
        )

        return typing.cast(None, jsii.invoke(self, "putThreatDetectionPolicy", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#create MssqlDatabase#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#delete MssqlDatabase#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read MssqlDatabase#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#update MssqlDatabase#update}.
        '''
        value = MssqlDatabaseTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoPauseDelayInMinutes")
    def reset_auto_pause_delay_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoPauseDelayInMinutes", []))

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetCreateMode")
    def reset_create_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateMode", []))

    @jsii.member(jsii_name="resetCreationSourceDatabaseId")
    def reset_creation_source_database_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreationSourceDatabaseId", []))

    @jsii.member(jsii_name="resetElasticPoolId")
    def reset_elastic_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticPoolId", []))

    @jsii.member(jsii_name="resetGeoBackupEnabled")
    def reset_geo_backup_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoBackupEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLedgerEnabled")
    def reset_ledger_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLedgerEnabled", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetLongTermRetentionPolicy")
    def reset_long_term_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongTermRetentionPolicy", []))

    @jsii.member(jsii_name="resetMaintenanceConfigurationName")
    def reset_maintenance_configuration_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceConfigurationName", []))

    @jsii.member(jsii_name="resetMaxSizeGb")
    def reset_max_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxSizeGb", []))

    @jsii.member(jsii_name="resetMinCapacity")
    def reset_min_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCapacity", []))

    @jsii.member(jsii_name="resetReadReplicaCount")
    def reset_read_replica_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadReplicaCount", []))

    @jsii.member(jsii_name="resetReadScale")
    def reset_read_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadScale", []))

    @jsii.member(jsii_name="resetRecoverDatabaseId")
    def reset_recover_database_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoverDatabaseId", []))

    @jsii.member(jsii_name="resetRestoreDroppedDatabaseId")
    def reset_restore_dropped_database_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreDroppedDatabaseId", []))

    @jsii.member(jsii_name="resetRestorePointInTime")
    def reset_restore_point_in_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestorePointInTime", []))

    @jsii.member(jsii_name="resetSampleName")
    def reset_sample_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleName", []))

    @jsii.member(jsii_name="resetShortTermRetentionPolicy")
    def reset_short_term_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShortTermRetentionPolicy", []))

    @jsii.member(jsii_name="resetSkuName")
    def reset_sku_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkuName", []))

    @jsii.member(jsii_name="resetStorageAccountType")
    def reset_storage_account_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetThreatDetectionPolicy")
    def reset_threat_detection_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreatDetectionPolicy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTransparentDataEncryptionEnabled")
    def reset_transparent_data_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransparentDataEncryptionEnabled", []))

    @jsii.member(jsii_name="resetZoneRedundant")
    def reset_zone_redundant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneRedundant", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="longTermRetentionPolicy")
    def long_term_retention_policy(
        self,
    ) -> "MssqlDatabaseLongTermRetentionPolicyOutputReference":
        return typing.cast("MssqlDatabaseLongTermRetentionPolicyOutputReference", jsii.get(self, "longTermRetentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="shortTermRetentionPolicy")
    def short_term_retention_policy(
        self,
    ) -> "MssqlDatabaseShortTermRetentionPolicyOutputReference":
        return typing.cast("MssqlDatabaseShortTermRetentionPolicyOutputReference", jsii.get(self, "shortTermRetentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="threatDetectionPolicy")
    def threat_detection_policy(
        self,
    ) -> "MssqlDatabaseThreatDetectionPolicyOutputReference":
        return typing.cast("MssqlDatabaseThreatDetectionPolicyOutputReference", jsii.get(self, "threatDetectionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MssqlDatabaseTimeoutsOutputReference":
        return typing.cast("MssqlDatabaseTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoPauseDelayInMinutesInput")
    def auto_pause_delay_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoPauseDelayInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="createModeInput")
    def create_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createModeInput"))

    @builtins.property
    @jsii.member(jsii_name="creationSourceDatabaseIdInput")
    def creation_source_database_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "creationSourceDatabaseIdInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticPoolIdInput")
    def elastic_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="geoBackupEnabledInput")
    def geo_backup_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "geoBackupEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ledgerEnabledInput")
    def ledger_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ledgerEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseTypeInput")
    def license_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="longTermRetentionPolicyInput")
    def long_term_retention_policy_input(
        self,
    ) -> typing.Optional["MssqlDatabaseLongTermRetentionPolicy"]:
        return typing.cast(typing.Optional["MssqlDatabaseLongTermRetentionPolicy"], jsii.get(self, "longTermRetentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceConfigurationNameInput")
    def maintenance_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeGbInput")
    def max_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="minCapacityInput")
    def min_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="readReplicaCountInput")
    def read_replica_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readReplicaCountInput"))

    @builtins.property
    @jsii.member(jsii_name="readScaleInput")
    def read_scale_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readScaleInput"))

    @builtins.property
    @jsii.member(jsii_name="recoverDatabaseIdInput")
    def recover_database_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoverDatabaseIdInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreDroppedDatabaseIdInput")
    def restore_dropped_database_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreDroppedDatabaseIdInput"))

    @builtins.property
    @jsii.member(jsii_name="restorePointInTimeInput")
    def restore_point_in_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restorePointInTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleNameInput")
    def sample_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serverIdInput")
    def server_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverIdInput"))

    @builtins.property
    @jsii.member(jsii_name="shortTermRetentionPolicyInput")
    def short_term_retention_policy_input(
        self,
    ) -> typing.Optional["MssqlDatabaseShortTermRetentionPolicy"]:
        return typing.cast(typing.Optional["MssqlDatabaseShortTermRetentionPolicy"], jsii.get(self, "shortTermRetentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="threatDetectionPolicyInput")
    def threat_detection_policy_input(
        self,
    ) -> typing.Optional["MssqlDatabaseThreatDetectionPolicy"]:
        return typing.cast(typing.Optional["MssqlDatabaseThreatDetectionPolicy"], jsii.get(self, "threatDetectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MssqlDatabaseTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MssqlDatabaseTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transparentDataEncryptionEnabledInput")
    def transparent_data_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "transparentDataEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneRedundantInput")
    def zone_redundant_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "zoneRedundantInput"))

    @builtins.property
    @jsii.member(jsii_name="autoPauseDelayInMinutes")
    def auto_pause_delay_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoPauseDelayInMinutes"))

    @auto_pause_delay_in_minutes.setter
    def auto_pause_delay_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "auto_pause_delay_in_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoPauseDelayInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "collation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="createMode")
    def create_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createMode"))

    @create_mode.setter
    def create_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "create_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createMode", value)

    @builtins.property
    @jsii.member(jsii_name="creationSourceDatabaseId")
    def creation_source_database_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationSourceDatabaseId"))

    @creation_source_database_id.setter
    def creation_source_database_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "creation_source_database_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationSourceDatabaseId", value)

    @builtins.property
    @jsii.member(jsii_name="elasticPoolId")
    def elastic_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticPoolId"))

    @elastic_pool_id.setter
    def elastic_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "elastic_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="geoBackupEnabled")
    def geo_backup_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "geoBackupEnabled"))

    @geo_backup_enabled.setter
    def geo_backup_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "geo_backup_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoBackupEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ledgerEnabled")
    def ledger_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ledgerEnabled"))

    @ledger_enabled.setter
    def ledger_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "ledger_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ledgerEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "license_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceConfigurationName")
    def maintenance_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceConfigurationName"))

    @maintenance_configuration_name.setter
    def maintenance_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "maintenance_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="maxSizeGb")
    def max_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSizeGb"))

    @max_size_gb.setter
    def max_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "max_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "min_capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="readReplicaCount")
    def read_replica_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readReplicaCount"))

    @read_replica_count.setter
    def read_replica_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "read_replica_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readReplicaCount", value)

    @builtins.property
    @jsii.member(jsii_name="readScale")
    def read_scale(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readScale"))

    @read_scale.setter
    def read_scale(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "read_scale").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readScale", value)

    @builtins.property
    @jsii.member(jsii_name="recoverDatabaseId")
    def recover_database_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoverDatabaseId"))

    @recover_database_id.setter
    def recover_database_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "recover_database_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoverDatabaseId", value)

    @builtins.property
    @jsii.member(jsii_name="restoreDroppedDatabaseId")
    def restore_dropped_database_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreDroppedDatabaseId"))

    @restore_dropped_database_id.setter
    def restore_dropped_database_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "restore_dropped_database_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreDroppedDatabaseId", value)

    @builtins.property
    @jsii.member(jsii_name="restorePointInTime")
    def restore_point_in_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restorePointInTime"))

    @restore_point_in_time.setter
    def restore_point_in_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "restore_point_in_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restorePointInTime", value)

    @builtins.property
    @jsii.member(jsii_name="sampleName")
    def sample_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sampleName"))

    @sample_name.setter
    def sample_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "sample_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleName", value)

    @builtins.property
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverId"))

    @server_id.setter
    def server_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "server_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverId", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "storage_account_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="transparentDataEncryptionEnabled")
    def transparent_data_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "transparentDataEncryptionEnabled"))

    @transparent_data_encryption_enabled.setter
    def transparent_data_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "transparent_data_encryption_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transparentDataEncryptionEnabled", value)

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
            type_hints = typing.get_type_hints(getattr(MssqlDatabase, "zone_redundant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneRedundant", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "server_id": "serverId",
        "auto_pause_delay_in_minutes": "autoPauseDelayInMinutes",
        "collation": "collation",
        "create_mode": "createMode",
        "creation_source_database_id": "creationSourceDatabaseId",
        "elastic_pool_id": "elasticPoolId",
        "geo_backup_enabled": "geoBackupEnabled",
        "id": "id",
        "ledger_enabled": "ledgerEnabled",
        "license_type": "licenseType",
        "long_term_retention_policy": "longTermRetentionPolicy",
        "maintenance_configuration_name": "maintenanceConfigurationName",
        "max_size_gb": "maxSizeGb",
        "min_capacity": "minCapacity",
        "read_replica_count": "readReplicaCount",
        "read_scale": "readScale",
        "recover_database_id": "recoverDatabaseId",
        "restore_dropped_database_id": "restoreDroppedDatabaseId",
        "restore_point_in_time": "restorePointInTime",
        "sample_name": "sampleName",
        "short_term_retention_policy": "shortTermRetentionPolicy",
        "sku_name": "skuName",
        "storage_account_type": "storageAccountType",
        "tags": "tags",
        "threat_detection_policy": "threatDetectionPolicy",
        "timeouts": "timeouts",
        "transparent_data_encryption_enabled": "transparentDataEncryptionEnabled",
        "zone_redundant": "zoneRedundant",
    },
)
class MssqlDatabaseConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        server_id: builtins.str,
        auto_pause_delay_in_minutes: typing.Optional[jsii.Number] = None,
        collation: typing.Optional[builtins.str] = None,
        create_mode: typing.Optional[builtins.str] = None,
        creation_source_database_id: typing.Optional[builtins.str] = None,
        elastic_pool_id: typing.Optional[builtins.str] = None,
        geo_backup_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ledger_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        license_type: typing.Optional[builtins.str] = None,
        long_term_retention_policy: typing.Optional[typing.Union["MssqlDatabaseLongTermRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        maintenance_configuration_name: typing.Optional[builtins.str] = None,
        max_size_gb: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        read_replica_count: typing.Optional[jsii.Number] = None,
        read_scale: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        recover_database_id: typing.Optional[builtins.str] = None,
        restore_dropped_database_id: typing.Optional[builtins.str] = None,
        restore_point_in_time: typing.Optional[builtins.str] = None,
        sample_name: typing.Optional[builtins.str] = None,
        short_term_retention_policy: typing.Optional[typing.Union["MssqlDatabaseShortTermRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        sku_name: typing.Optional[builtins.str] = None,
        storage_account_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        threat_detection_policy: typing.Optional[typing.Union["MssqlDatabaseThreatDetectionPolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MssqlDatabaseTimeouts", typing.Dict[str, typing.Any]]] = None,
        transparent_data_encryption_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zone_redundant: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#name MssqlDatabase#name}.
        :param server_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#server_id MssqlDatabase#server_id}.
        :param auto_pause_delay_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#auto_pause_delay_in_minutes MssqlDatabase#auto_pause_delay_in_minutes}.
        :param collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#collation MssqlDatabase#collation}.
        :param create_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#create_mode MssqlDatabase#create_mode}.
        :param creation_source_database_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#creation_source_database_id MssqlDatabase#creation_source_database_id}.
        :param elastic_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#elastic_pool_id MssqlDatabase#elastic_pool_id}.
        :param geo_backup_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#geo_backup_enabled MssqlDatabase#geo_backup_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#id MssqlDatabase#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ledger_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#ledger_enabled MssqlDatabase#ledger_enabled}.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#license_type MssqlDatabase#license_type}.
        :param long_term_retention_policy: long_term_retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#long_term_retention_policy MssqlDatabase#long_term_retention_policy}
        :param maintenance_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#maintenance_configuration_name MssqlDatabase#maintenance_configuration_name}.
        :param max_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#max_size_gb MssqlDatabase#max_size_gb}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#min_capacity MssqlDatabase#min_capacity}.
        :param read_replica_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read_replica_count MssqlDatabase#read_replica_count}.
        :param read_scale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read_scale MssqlDatabase#read_scale}.
        :param recover_database_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#recover_database_id MssqlDatabase#recover_database_id}.
        :param restore_dropped_database_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#restore_dropped_database_id MssqlDatabase#restore_dropped_database_id}.
        :param restore_point_in_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#restore_point_in_time MssqlDatabase#restore_point_in_time}.
        :param sample_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#sample_name MssqlDatabase#sample_name}.
        :param short_term_retention_policy: short_term_retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#short_term_retention_policy MssqlDatabase#short_term_retention_policy}
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#sku_name MssqlDatabase#sku_name}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_account_type MssqlDatabase#storage_account_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#tags MssqlDatabase#tags}.
        :param threat_detection_policy: threat_detection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#threat_detection_policy MssqlDatabase#threat_detection_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#timeouts MssqlDatabase#timeouts}
        :param transparent_data_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#transparent_data_encryption_enabled MssqlDatabase#transparent_data_encryption_enabled}.
        :param zone_redundant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#zone_redundant MssqlDatabase#zone_redundant}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(long_term_retention_policy, dict):
            long_term_retention_policy = MssqlDatabaseLongTermRetentionPolicy(**long_term_retention_policy)
        if isinstance(short_term_retention_policy, dict):
            short_term_retention_policy = MssqlDatabaseShortTermRetentionPolicy(**short_term_retention_policy)
        if isinstance(threat_detection_policy, dict):
            threat_detection_policy = MssqlDatabaseThreatDetectionPolicy(**threat_detection_policy)
        if isinstance(timeouts, dict):
            timeouts = MssqlDatabaseTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MssqlDatabaseConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument server_id", value=server_id, expected_type=type_hints["server_id"])
            check_type(argname="argument auto_pause_delay_in_minutes", value=auto_pause_delay_in_minutes, expected_type=type_hints["auto_pause_delay_in_minutes"])
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument create_mode", value=create_mode, expected_type=type_hints["create_mode"])
            check_type(argname="argument creation_source_database_id", value=creation_source_database_id, expected_type=type_hints["creation_source_database_id"])
            check_type(argname="argument elastic_pool_id", value=elastic_pool_id, expected_type=type_hints["elastic_pool_id"])
            check_type(argname="argument geo_backup_enabled", value=geo_backup_enabled, expected_type=type_hints["geo_backup_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ledger_enabled", value=ledger_enabled, expected_type=type_hints["ledger_enabled"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument long_term_retention_policy", value=long_term_retention_policy, expected_type=type_hints["long_term_retention_policy"])
            check_type(argname="argument maintenance_configuration_name", value=maintenance_configuration_name, expected_type=type_hints["maintenance_configuration_name"])
            check_type(argname="argument max_size_gb", value=max_size_gb, expected_type=type_hints["max_size_gb"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument read_replica_count", value=read_replica_count, expected_type=type_hints["read_replica_count"])
            check_type(argname="argument read_scale", value=read_scale, expected_type=type_hints["read_scale"])
            check_type(argname="argument recover_database_id", value=recover_database_id, expected_type=type_hints["recover_database_id"])
            check_type(argname="argument restore_dropped_database_id", value=restore_dropped_database_id, expected_type=type_hints["restore_dropped_database_id"])
            check_type(argname="argument restore_point_in_time", value=restore_point_in_time, expected_type=type_hints["restore_point_in_time"])
            check_type(argname="argument sample_name", value=sample_name, expected_type=type_hints["sample_name"])
            check_type(argname="argument short_term_retention_policy", value=short_term_retention_policy, expected_type=type_hints["short_term_retention_policy"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument threat_detection_policy", value=threat_detection_policy, expected_type=type_hints["threat_detection_policy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transparent_data_encryption_enabled", value=transparent_data_encryption_enabled, expected_type=type_hints["transparent_data_encryption_enabled"])
            check_type(argname="argument zone_redundant", value=zone_redundant, expected_type=type_hints["zone_redundant"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "server_id": server_id,
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
        if auto_pause_delay_in_minutes is not None:
            self._values["auto_pause_delay_in_minutes"] = auto_pause_delay_in_minutes
        if collation is not None:
            self._values["collation"] = collation
        if create_mode is not None:
            self._values["create_mode"] = create_mode
        if creation_source_database_id is not None:
            self._values["creation_source_database_id"] = creation_source_database_id
        if elastic_pool_id is not None:
            self._values["elastic_pool_id"] = elastic_pool_id
        if geo_backup_enabled is not None:
            self._values["geo_backup_enabled"] = geo_backup_enabled
        if id is not None:
            self._values["id"] = id
        if ledger_enabled is not None:
            self._values["ledger_enabled"] = ledger_enabled
        if license_type is not None:
            self._values["license_type"] = license_type
        if long_term_retention_policy is not None:
            self._values["long_term_retention_policy"] = long_term_retention_policy
        if maintenance_configuration_name is not None:
            self._values["maintenance_configuration_name"] = maintenance_configuration_name
        if max_size_gb is not None:
            self._values["max_size_gb"] = max_size_gb
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if read_replica_count is not None:
            self._values["read_replica_count"] = read_replica_count
        if read_scale is not None:
            self._values["read_scale"] = read_scale
        if recover_database_id is not None:
            self._values["recover_database_id"] = recover_database_id
        if restore_dropped_database_id is not None:
            self._values["restore_dropped_database_id"] = restore_dropped_database_id
        if restore_point_in_time is not None:
            self._values["restore_point_in_time"] = restore_point_in_time
        if sample_name is not None:
            self._values["sample_name"] = sample_name
        if short_term_retention_policy is not None:
            self._values["short_term_retention_policy"] = short_term_retention_policy
        if sku_name is not None:
            self._values["sku_name"] = sku_name
        if storage_account_type is not None:
            self._values["storage_account_type"] = storage_account_type
        if tags is not None:
            self._values["tags"] = tags
        if threat_detection_policy is not None:
            self._values["threat_detection_policy"] = threat_detection_policy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transparent_data_encryption_enabled is not None:
            self._values["transparent_data_encryption_enabled"] = transparent_data_encryption_enabled
        if zone_redundant is not None:
            self._values["zone_redundant"] = zone_redundant

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#name MssqlDatabase#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#server_id MssqlDatabase#server_id}.'''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_pause_delay_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#auto_pause_delay_in_minutes MssqlDatabase#auto_pause_delay_in_minutes}.'''
        result = self._values.get("auto_pause_delay_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#collation MssqlDatabase#collation}.'''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#create_mode MssqlDatabase#create_mode}.'''
        result = self._values.get("create_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_source_database_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#creation_source_database_id MssqlDatabase#creation_source_database_id}.'''
        result = self._values.get("creation_source_database_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elastic_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#elastic_pool_id MssqlDatabase#elastic_pool_id}.'''
        result = self._values.get("elastic_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def geo_backup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#geo_backup_enabled MssqlDatabase#geo_backup_enabled}.'''
        result = self._values.get("geo_backup_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#id MssqlDatabase#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ledger_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#ledger_enabled MssqlDatabase#ledger_enabled}.'''
        result = self._values.get("ledger_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#license_type MssqlDatabase#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_term_retention_policy(
        self,
    ) -> typing.Optional["MssqlDatabaseLongTermRetentionPolicy"]:
        '''long_term_retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#long_term_retention_policy MssqlDatabase#long_term_retention_policy}
        '''
        result = self._values.get("long_term_retention_policy")
        return typing.cast(typing.Optional["MssqlDatabaseLongTermRetentionPolicy"], result)

    @builtins.property
    def maintenance_configuration_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#maintenance_configuration_name MssqlDatabase#maintenance_configuration_name}.'''
        result = self._values.get("maintenance_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#max_size_gb MssqlDatabase#max_size_gb}.'''
        result = self._values.get("max_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#min_capacity MssqlDatabase#min_capacity}.'''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_replica_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read_replica_count MssqlDatabase#read_replica_count}.'''
        result = self._values.get("read_replica_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_scale(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read_scale MssqlDatabase#read_scale}.'''
        result = self._values.get("read_scale")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def recover_database_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#recover_database_id MssqlDatabase#recover_database_id}.'''
        result = self._values.get("recover_database_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_dropped_database_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#restore_dropped_database_id MssqlDatabase#restore_dropped_database_id}.'''
        result = self._values.get("restore_dropped_database_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_point_in_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#restore_point_in_time MssqlDatabase#restore_point_in_time}.'''
        result = self._values.get("restore_point_in_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#sample_name MssqlDatabase#sample_name}.'''
        result = self._values.get("sample_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def short_term_retention_policy(
        self,
    ) -> typing.Optional["MssqlDatabaseShortTermRetentionPolicy"]:
        '''short_term_retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#short_term_retention_policy MssqlDatabase#short_term_retention_policy}
        '''
        result = self._values.get("short_term_retention_policy")
        return typing.cast(typing.Optional["MssqlDatabaseShortTermRetentionPolicy"], result)

    @builtins.property
    def sku_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#sku_name MssqlDatabase#sku_name}.'''
        result = self._values.get("sku_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_account_type MssqlDatabase#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#tags MssqlDatabase#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def threat_detection_policy(
        self,
    ) -> typing.Optional["MssqlDatabaseThreatDetectionPolicy"]:
        '''threat_detection_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#threat_detection_policy MssqlDatabase#threat_detection_policy}
        '''
        result = self._values.get("threat_detection_policy")
        return typing.cast(typing.Optional["MssqlDatabaseThreatDetectionPolicy"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MssqlDatabaseTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#timeouts MssqlDatabase#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MssqlDatabaseTimeouts"], result)

    @builtins.property
    def transparent_data_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#transparent_data_encryption_enabled MssqlDatabase#transparent_data_encryption_enabled}.'''
        result = self._values.get("transparent_data_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def zone_redundant(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#zone_redundant MssqlDatabase#zone_redundant}.'''
        result = self._values.get("zone_redundant")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlDatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseLongTermRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "monthly_retention": "monthlyRetention",
        "weekly_retention": "weeklyRetention",
        "week_of_year": "weekOfYear",
        "yearly_retention": "yearlyRetention",
    },
)
class MssqlDatabaseLongTermRetentionPolicy:
    def __init__(
        self,
        *,
        monthly_retention: typing.Optional[builtins.str] = None,
        weekly_retention: typing.Optional[builtins.str] = None,
        week_of_year: typing.Optional[jsii.Number] = None,
        yearly_retention: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monthly_retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#monthly_retention MssqlDatabase#monthly_retention}.
        :param weekly_retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#weekly_retention MssqlDatabase#weekly_retention}.
        :param week_of_year: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#week_of_year MssqlDatabase#week_of_year}.
        :param yearly_retention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#yearly_retention MssqlDatabase#yearly_retention}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlDatabaseLongTermRetentionPolicy.__init__)
            check_type(argname="argument monthly_retention", value=monthly_retention, expected_type=type_hints["monthly_retention"])
            check_type(argname="argument weekly_retention", value=weekly_retention, expected_type=type_hints["weekly_retention"])
            check_type(argname="argument week_of_year", value=week_of_year, expected_type=type_hints["week_of_year"])
            check_type(argname="argument yearly_retention", value=yearly_retention, expected_type=type_hints["yearly_retention"])
        self._values: typing.Dict[str, typing.Any] = {}
        if monthly_retention is not None:
            self._values["monthly_retention"] = monthly_retention
        if weekly_retention is not None:
            self._values["weekly_retention"] = weekly_retention
        if week_of_year is not None:
            self._values["week_of_year"] = week_of_year
        if yearly_retention is not None:
            self._values["yearly_retention"] = yearly_retention

    @builtins.property
    def monthly_retention(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#monthly_retention MssqlDatabase#monthly_retention}.'''
        result = self._values.get("monthly_retention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekly_retention(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#weekly_retention MssqlDatabase#weekly_retention}.'''
        result = self._values.get("weekly_retention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def week_of_year(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#week_of_year MssqlDatabase#week_of_year}.'''
        result = self._values.get("week_of_year")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def yearly_retention(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#yearly_retention MssqlDatabase#yearly_retention}.'''
        result = self._values.get("yearly_retention")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlDatabaseLongTermRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlDatabaseLongTermRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseLongTermRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MssqlDatabaseLongTermRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMonthlyRetention")
    def reset_monthly_retention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthlyRetention", []))

    @jsii.member(jsii_name="resetWeeklyRetention")
    def reset_weekly_retention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklyRetention", []))

    @jsii.member(jsii_name="resetWeekOfYear")
    def reset_week_of_year(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekOfYear", []))

    @jsii.member(jsii_name="resetYearlyRetention")
    def reset_yearly_retention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetYearlyRetention", []))

    @builtins.property
    @jsii.member(jsii_name="monthlyRetentionInput")
    def monthly_retention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monthlyRetentionInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyRetentionInput")
    def weekly_retention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyRetentionInput"))

    @builtins.property
    @jsii.member(jsii_name="weekOfYearInput")
    def week_of_year_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weekOfYearInput"))

    @builtins.property
    @jsii.member(jsii_name="yearlyRetentionInput")
    def yearly_retention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "yearlyRetentionInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlyRetention")
    def monthly_retention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monthlyRetention"))

    @monthly_retention.setter
    def monthly_retention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseLongTermRetentionPolicyOutputReference, "monthly_retention").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthlyRetention", value)

    @builtins.property
    @jsii.member(jsii_name="weeklyRetention")
    def weekly_retention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weeklyRetention"))

    @weekly_retention.setter
    def weekly_retention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseLongTermRetentionPolicyOutputReference, "weekly_retention").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklyRetention", value)

    @builtins.property
    @jsii.member(jsii_name="weekOfYear")
    def week_of_year(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weekOfYear"))

    @week_of_year.setter
    def week_of_year(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseLongTermRetentionPolicyOutputReference, "week_of_year").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekOfYear", value)

    @builtins.property
    @jsii.member(jsii_name="yearlyRetention")
    def yearly_retention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "yearlyRetention"))

    @yearly_retention.setter
    def yearly_retention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseLongTermRetentionPolicyOutputReference, "yearly_retention").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "yearlyRetention", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlDatabaseLongTermRetentionPolicy]:
        return typing.cast(typing.Optional[MssqlDatabaseLongTermRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlDatabaseLongTermRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseLongTermRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseShortTermRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "retention_days": "retentionDays",
        "backup_interval_in_hours": "backupIntervalInHours",
    },
)
class MssqlDatabaseShortTermRetentionPolicy:
    def __init__(
        self,
        *,
        retention_days: jsii.Number,
        backup_interval_in_hours: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#retention_days MssqlDatabase#retention_days}.
        :param backup_interval_in_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#backup_interval_in_hours MssqlDatabase#backup_interval_in_hours}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlDatabaseShortTermRetentionPolicy.__init__)
            check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
            check_type(argname="argument backup_interval_in_hours", value=backup_interval_in_hours, expected_type=type_hints["backup_interval_in_hours"])
        self._values: typing.Dict[str, typing.Any] = {
            "retention_days": retention_days,
        }
        if backup_interval_in_hours is not None:
            self._values["backup_interval_in_hours"] = backup_interval_in_hours

    @builtins.property
    def retention_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#retention_days MssqlDatabase#retention_days}.'''
        result = self._values.get("retention_days")
        assert result is not None, "Required property 'retention_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def backup_interval_in_hours(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#backup_interval_in_hours MssqlDatabase#backup_interval_in_hours}.'''
        result = self._values.get("backup_interval_in_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlDatabaseShortTermRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlDatabaseShortTermRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseShortTermRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MssqlDatabaseShortTermRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBackupIntervalInHours")
    def reset_backup_interval_in_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupIntervalInHours", []))

    @builtins.property
    @jsii.member(jsii_name="backupIntervalInHoursInput")
    def backup_interval_in_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupIntervalInHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaysInput")
    def retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="backupIntervalInHours")
    def backup_interval_in_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupIntervalInHours"))

    @backup_interval_in_hours.setter
    def backup_interval_in_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseShortTermRetentionPolicyOutputReference, "backup_interval_in_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupIntervalInHours", value)

    @builtins.property
    @jsii.member(jsii_name="retentionDays")
    def retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionDays"))

    @retention_days.setter
    def retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseShortTermRetentionPolicyOutputReference, "retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlDatabaseShortTermRetentionPolicy]:
        return typing.cast(typing.Optional[MssqlDatabaseShortTermRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlDatabaseShortTermRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseShortTermRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseThreatDetectionPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "disabled_alerts": "disabledAlerts",
        "email_account_admins": "emailAccountAdmins",
        "email_addresses": "emailAddresses",
        "retention_days": "retentionDays",
        "state": "state",
        "storage_account_access_key": "storageAccountAccessKey",
        "storage_endpoint": "storageEndpoint",
    },
)
class MssqlDatabaseThreatDetectionPolicy:
    def __init__(
        self,
        *,
        disabled_alerts: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_account_admins: typing.Optional[builtins.str] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        retention_days: typing.Optional[jsii.Number] = None,
        state: typing.Optional[builtins.str] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disabled_alerts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#disabled_alerts MssqlDatabase#disabled_alerts}.
        :param email_account_admins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#email_account_admins MssqlDatabase#email_account_admins}.
        :param email_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#email_addresses MssqlDatabase#email_addresses}.
        :param retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#retention_days MssqlDatabase#retention_days}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#state MssqlDatabase#state}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_account_access_key MssqlDatabase#storage_account_access_key}.
        :param storage_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_endpoint MssqlDatabase#storage_endpoint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlDatabaseThreatDetectionPolicy.__init__)
            check_type(argname="argument disabled_alerts", value=disabled_alerts, expected_type=type_hints["disabled_alerts"])
            check_type(argname="argument email_account_admins", value=email_account_admins, expected_type=type_hints["email_account_admins"])
            check_type(argname="argument email_addresses", value=email_addresses, expected_type=type_hints["email_addresses"])
            check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument storage_account_access_key", value=storage_account_access_key, expected_type=type_hints["storage_account_access_key"])
            check_type(argname="argument storage_endpoint", value=storage_endpoint, expected_type=type_hints["storage_endpoint"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disabled_alerts is not None:
            self._values["disabled_alerts"] = disabled_alerts
        if email_account_admins is not None:
            self._values["email_account_admins"] = email_account_admins
        if email_addresses is not None:
            self._values["email_addresses"] = email_addresses
        if retention_days is not None:
            self._values["retention_days"] = retention_days
        if state is not None:
            self._values["state"] = state
        if storage_account_access_key is not None:
            self._values["storage_account_access_key"] = storage_account_access_key
        if storage_endpoint is not None:
            self._values["storage_endpoint"] = storage_endpoint

    @builtins.property
    def disabled_alerts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#disabled_alerts MssqlDatabase#disabled_alerts}.'''
        result = self._values.get("disabled_alerts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_account_admins(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#email_account_admins MssqlDatabase#email_account_admins}.'''
        result = self._values.get("email_account_admins")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#email_addresses MssqlDatabase#email_addresses}.'''
        result = self._values.get("email_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def retention_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#retention_days MssqlDatabase#retention_days}.'''
        result = self._values.get("retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#state MssqlDatabase#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_access_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_account_access_key MssqlDatabase#storage_account_access_key}.'''
        result = self._values.get("storage_account_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#storage_endpoint MssqlDatabase#storage_endpoint}.'''
        result = self._values.get("storage_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlDatabaseThreatDetectionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlDatabaseThreatDetectionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseThreatDetectionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(MssqlDatabaseThreatDetectionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisabledAlerts")
    def reset_disabled_alerts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabledAlerts", []))

    @jsii.member(jsii_name="resetEmailAccountAdmins")
    def reset_email_account_admins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAccountAdmins", []))

    @jsii.member(jsii_name="resetEmailAddresses")
    def reset_email_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAddresses", []))

    @jsii.member(jsii_name="resetRetentionDays")
    def reset_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionDays", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetStorageAccountAccessKey")
    def reset_storage_account_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountAccessKey", []))

    @jsii.member(jsii_name="resetStorageEndpoint")
    def reset_storage_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageEndpoint", []))

    @builtins.property
    @jsii.member(jsii_name="disabledAlertsInput")
    def disabled_alerts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disabledAlertsInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAccountAdminsInput")
    def email_account_admins_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAccountAdminsInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressesInput")
    def email_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaysInput")
    def retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKeyInput")
    def storage_account_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageEndpointInput")
    def storage_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledAlerts")
    def disabled_alerts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disabledAlerts"))

    @disabled_alerts.setter
    def disabled_alerts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseThreatDetectionPolicyOutputReference, "disabled_alerts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabledAlerts", value)

    @builtins.property
    @jsii.member(jsii_name="emailAccountAdmins")
    def email_account_admins(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAccountAdmins"))

    @email_account_admins.setter
    def email_account_admins(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseThreatDetectionPolicyOutputReference, "email_account_admins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAccountAdmins", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddresses")
    def email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailAddresses"))

    @email_addresses.setter
    def email_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseThreatDetectionPolicyOutputReference, "email_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="retentionDays")
    def retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionDays"))

    @retention_days.setter
    def retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseThreatDetectionPolicyOutputReference, "retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseThreatDetectionPolicyOutputReference, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKey")
    def storage_account_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountAccessKey"))

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseThreatDetectionPolicyOutputReference, "storage_account_access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageEndpoint")
    def storage_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageEndpoint"))

    @storage_endpoint.setter
    def storage_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseThreatDetectionPolicyOutputReference, "storage_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MssqlDatabaseThreatDetectionPolicy]:
        return typing.cast(typing.Optional[MssqlDatabaseThreatDetectionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MssqlDatabaseThreatDetectionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseThreatDetectionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MssqlDatabaseTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#create MssqlDatabase#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#delete MssqlDatabase#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read MssqlDatabase#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#update MssqlDatabase#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MssqlDatabaseTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#create MssqlDatabase#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#delete MssqlDatabase#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#read MssqlDatabase#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_database#update MssqlDatabase#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlDatabaseTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlDatabaseTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlDatabase.MssqlDatabaseTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MssqlDatabaseTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MssqlDatabaseTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MssqlDatabaseTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MssqlDatabaseTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MssqlDatabaseTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MssqlDatabase",
    "MssqlDatabaseConfig",
    "MssqlDatabaseLongTermRetentionPolicy",
    "MssqlDatabaseLongTermRetentionPolicyOutputReference",
    "MssqlDatabaseShortTermRetentionPolicy",
    "MssqlDatabaseShortTermRetentionPolicyOutputReference",
    "MssqlDatabaseThreatDetectionPolicy",
    "MssqlDatabaseThreatDetectionPolicyOutputReference",
    "MssqlDatabaseTimeouts",
    "MssqlDatabaseTimeoutsOutputReference",
]

publication.publish()
