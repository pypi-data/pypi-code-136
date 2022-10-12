'''
# `google_sql_database_instance`

Refer to the Terraform Registory for docs: [`google_sql_database_instance`](https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance).
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


class GoogleSqlDatabaseInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance google_sql_database_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        database_version: builtins.str,
        clone: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceClone", typing.Dict[str, typing.Any]]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_key_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_version: typing.Optional[builtins.str] = None,
        master_instance_name: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        replica_configuration: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceReplicaConfiguration", typing.Dict[str, typing.Any]]] = None,
        restore_backup_context: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceRestoreBackupContext", typing.Dict[str, typing.Any]]] = None,
        root_password: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettings", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance google_sql_database_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_version: The MySQL, PostgreSQL or SQL Server (beta) version to use. Supported values include MYSQL_5_6, MYSQL_5_7, MYSQL_8_0, POSTGRES_9_6, POSTGRES_10, POSTGRES_11, POSTGRES_12, POSTGRES_13, POSTGRES_14, SQLSERVER_2017_STANDARD, SQLSERVER_2017_ENTERPRISE, SQLSERVER_2017_EXPRESS, SQLSERVER_2017_WEB. Database Version Policies includes an up-to-date reference of supported versions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#database_version GoogleSqlDatabaseInstance#database_version}
        :param clone: clone block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#clone GoogleSqlDatabaseInstance#clone}
        :param deletion_protection: Used to block Terraform from deleting a SQL Instance. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#deletion_protection GoogleSqlDatabaseInstance#deletion_protection}
        :param encryption_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#encryption_key_name GoogleSqlDatabaseInstance#encryption_key_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#id GoogleSqlDatabaseInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_version: Maintenance version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#maintenance_version GoogleSqlDatabaseInstance#maintenance_version}
        :param master_instance_name: The name of the instance that will act as the master in the replication setup. Note, this requires the master to have binary_log_enabled set, as well as existing backups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#master_instance_name GoogleSqlDatabaseInstance#master_instance_name}
        :param name: The name of the instance. If the name is left blank, Terraform will randomly generate one when the instance is first created. This is done because after a name is used, it cannot be reused for up to one week. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#name GoogleSqlDatabaseInstance#name}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#project GoogleSqlDatabaseInstance#project}
        :param region: The region the instance will sit in. Note, Cloud SQL is not available in all regions. A valid region must be provided to use this resource. If a region is not provided in the resource definition, the provider region will be used instead, but this will be an apply-time error for instances if the provider region is not supported with Cloud SQL. If you choose not to provide the region argument for this resource, make sure you understand this. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#region GoogleSqlDatabaseInstance#region}
        :param replica_configuration: replica_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#replica_configuration GoogleSqlDatabaseInstance#replica_configuration}
        :param restore_backup_context: restore_backup_context block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#restore_backup_context GoogleSqlDatabaseInstance#restore_backup_context}
        :param root_password: Initial root password. Required for MS SQL Server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#root_password GoogleSqlDatabaseInstance#root_password}
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#settings GoogleSqlDatabaseInstance#settings}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#timeouts GoogleSqlDatabaseInstance#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleSqlDatabaseInstanceConfig(
            database_version=database_version,
            clone=clone,
            deletion_protection=deletion_protection,
            encryption_key_name=encryption_key_name,
            id=id,
            maintenance_version=maintenance_version,
            master_instance_name=master_instance_name,
            name=name,
            project=project,
            region=region,
            replica_configuration=replica_configuration,
            restore_backup_context=restore_backup_context,
            root_password=root_password,
            settings=settings,
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

    @jsii.member(jsii_name="putClone")
    def put_clone(
        self,
        *,
        source_instance_name: builtins.str,
        allocated_ip_range: typing.Optional[builtins.str] = None,
        point_in_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_instance_name: The name of the instance from which the point in time should be restored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#source_instance_name GoogleSqlDatabaseInstance#source_instance_name}
        :param allocated_ip_range: The name of the allocated ip range for the private ip CloudSQL instance. For example: "google-managed-services-default". If set, the cloned instance ip will be created in the allocated range. The range name must comply with `RFC 1035 <https://tools.ietf.org/html/rfc1035>`_. Specifically, the name must be 1-63 characters long and match the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#allocated_ip_range GoogleSqlDatabaseInstance#allocated_ip_range}
        :param point_in_time: The timestamp of the point in time that should be restored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#point_in_time GoogleSqlDatabaseInstance#point_in_time}
        '''
        value = GoogleSqlDatabaseInstanceClone(
            source_instance_name=source_instance_name,
            allocated_ip_range=allocated_ip_range,
            point_in_time=point_in_time,
        )

        return typing.cast(None, jsii.invoke(self, "putClone", [value]))

    @jsii.member(jsii_name="putReplicaConfiguration")
    def put_replica_configuration(
        self,
        *,
        ca_certificate: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        connect_retry_interval: typing.Optional[jsii.Number] = None,
        dump_file_path: typing.Optional[builtins.str] = None,
        failover_target: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_heartbeat_period: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        ssl_cipher: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        verify_server_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param ca_certificate: PEM representation of the trusted CA's x509 certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ca_certificate GoogleSqlDatabaseInstance#ca_certificate}
        :param client_certificate: PEM representation of the replica's x509 certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#client_certificate GoogleSqlDatabaseInstance#client_certificate}
        :param client_key: PEM representation of the replica's private key. The corresponding public key in encoded in the client_certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#client_key GoogleSqlDatabaseInstance#client_key}
        :param connect_retry_interval: The number of seconds between connect retries. MySQL's default is 60 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#connect_retry_interval GoogleSqlDatabaseInstance#connect_retry_interval}
        :param dump_file_path: Path to a SQL file in Google Cloud Storage from which replica instances are created. Format is gs://bucket/filename. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#dump_file_path GoogleSqlDatabaseInstance#dump_file_path}
        :param failover_target: Specifies if the replica is the failover target. If the field is set to true the replica will be designated as a failover replica. If the master instance fails, the replica instance will be promoted as the new master instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#failover_target GoogleSqlDatabaseInstance#failover_target}
        :param master_heartbeat_period: Time in ms between replication heartbeats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#master_heartbeat_period GoogleSqlDatabaseInstance#master_heartbeat_period}
        :param password: Password for the replication connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password GoogleSqlDatabaseInstance#password}
        :param ssl_cipher: Permissible ciphers for use in SSL encryption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ssl_cipher GoogleSqlDatabaseInstance#ssl_cipher}
        :param username: Username for replication connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#username GoogleSqlDatabaseInstance#username}
        :param verify_server_certificate: True if the master's common name value is checked during the SSL handshake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#verify_server_certificate GoogleSqlDatabaseInstance#verify_server_certificate}
        '''
        value = GoogleSqlDatabaseInstanceReplicaConfiguration(
            ca_certificate=ca_certificate,
            client_certificate=client_certificate,
            client_key=client_key,
            connect_retry_interval=connect_retry_interval,
            dump_file_path=dump_file_path,
            failover_target=failover_target,
            master_heartbeat_period=master_heartbeat_period,
            password=password,
            ssl_cipher=ssl_cipher,
            username=username,
            verify_server_certificate=verify_server_certificate,
        )

        return typing.cast(None, jsii.invoke(self, "putReplicaConfiguration", [value]))

    @jsii.member(jsii_name="putRestoreBackupContext")
    def put_restore_backup_context(
        self,
        *,
        backup_run_id: jsii.Number,
        instance_id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backup_run_id: The ID of the backup run to restore from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_run_id GoogleSqlDatabaseInstance#backup_run_id}
        :param instance_id: The ID of the instance that the backup was taken from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#instance_id GoogleSqlDatabaseInstance#instance_id}
        :param project: The full project ID of the source instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#project GoogleSqlDatabaseInstance#project}
        '''
        value = GoogleSqlDatabaseInstanceRestoreBackupContext(
            backup_run_id=backup_run_id, instance_id=instance_id, project=project
        )

        return typing.cast(None, jsii.invoke(self, "putRestoreBackupContext", [value]))

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        *,
        tier: builtins.str,
        activation_policy: typing.Optional[builtins.str] = None,
        active_directory_config: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig", typing.Dict[str, typing.Any]]] = None,
        availability_type: typing.Optional[builtins.str] = None,
        backup_configuration: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsBackupConfiguration", typing.Dict[str, typing.Any]]] = None,
        collation: typing.Optional[builtins.str] = None,
        database_flags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSqlDatabaseInstanceSettingsDatabaseFlags", typing.Dict[str, typing.Any]]]]] = None,
        disk_autoresize: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disk_autoresize_limit: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        insights_config: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsInsightsConfig", typing.Dict[str, typing.Any]]] = None,
        ip_configuration: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsIpConfiguration", typing.Dict[str, typing.Any]]] = None,
        location_preference: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsLocationPreference", typing.Dict[str, typing.Any]]] = None,
        maintenance_window: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        password_validation_policy: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy", typing.Dict[str, typing.Any]]] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        sql_server_audit_config: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig", typing.Dict[str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param tier: The machine type to use. See tiers for more details and supported versions. Postgres supports only shared-core machine types, and custom machine types such as db-custom-2-13312. See the Custom Machine Type Documentation to learn about specifying custom machine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#tier GoogleSqlDatabaseInstance#tier}
        :param activation_policy: This specifies when the instance should be active. Can be either ALWAYS, NEVER or ON_DEMAND. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#activation_policy GoogleSqlDatabaseInstance#activation_policy}
        :param active_directory_config: active_directory_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#active_directory_config GoogleSqlDatabaseInstance#active_directory_config}
        :param availability_type: The availability type of the Cloud SQL instance, high availability (REGIONAL) or single zone (ZONAL). For all instances, ensure that settings.backup_configuration.enabled is set to true. For MySQL instances, ensure that settings.backup_configuration.binary_log_enabled is set to true. For Postgres instances, ensure that settings.backup_configuration.point_in_time_recovery_enabled is set to true. Defaults to ZONAL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#availability_type GoogleSqlDatabaseInstance#availability_type}
        :param backup_configuration: backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_configuration GoogleSqlDatabaseInstance#backup_configuration}
        :param collation: The name of server instance collation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#collation GoogleSqlDatabaseInstance#collation}
        :param database_flags: database_flags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#database_flags GoogleSqlDatabaseInstance#database_flags}
        :param disk_autoresize: Enables auto-resizing of the storage size. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_autoresize GoogleSqlDatabaseInstance#disk_autoresize}
        :param disk_autoresize_limit: The maximum size, in GB, to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_autoresize_limit GoogleSqlDatabaseInstance#disk_autoresize_limit}
        :param disk_size: The size of data disk, in GB. Size of a running instance cannot be reduced but can be increased. The minimum value is 10GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_size GoogleSqlDatabaseInstance#disk_size}
        :param disk_type: The type of data disk: PD_SSD or PD_HDD. Defaults to PD_SSD. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_type GoogleSqlDatabaseInstance#disk_type}
        :param insights_config: insights_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#insights_config GoogleSqlDatabaseInstance#insights_config}
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ip_configuration GoogleSqlDatabaseInstance#ip_configuration}
        :param location_preference: location_preference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#location_preference GoogleSqlDatabaseInstance#location_preference}
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#maintenance_window GoogleSqlDatabaseInstance#maintenance_window}
        :param password_validation_policy: password_validation_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password_validation_policy GoogleSqlDatabaseInstance#password_validation_policy}
        :param pricing_plan: Pricing plan for this instance, can only be PER_USE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#pricing_plan GoogleSqlDatabaseInstance#pricing_plan}
        :param sql_server_audit_config: sql_server_audit_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#sql_server_audit_config GoogleSqlDatabaseInstance#sql_server_audit_config}
        :param user_labels: A set of key/value user label pairs to assign to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#user_labels GoogleSqlDatabaseInstance#user_labels}
        '''
        value = GoogleSqlDatabaseInstanceSettings(
            tier=tier,
            activation_policy=activation_policy,
            active_directory_config=active_directory_config,
            availability_type=availability_type,
            backup_configuration=backup_configuration,
            collation=collation,
            database_flags=database_flags,
            disk_autoresize=disk_autoresize,
            disk_autoresize_limit=disk_autoresize_limit,
            disk_size=disk_size,
            disk_type=disk_type,
            insights_config=insights_config,
            ip_configuration=ip_configuration,
            location_preference=location_preference,
            maintenance_window=maintenance_window,
            password_validation_policy=password_validation_policy,
            pricing_plan=pricing_plan,
            sql_server_audit_config=sql_server_audit_config,
            user_labels=user_labels,
        )

        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#create GoogleSqlDatabaseInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#delete GoogleSqlDatabaseInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#update GoogleSqlDatabaseInstance#update}.
        '''
        value = GoogleSqlDatabaseInstanceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetClone")
    def reset_clone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClone", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetEncryptionKeyName")
    def reset_encryption_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionKeyName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenanceVersion")
    def reset_maintenance_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceVersion", []))

    @jsii.member(jsii_name="resetMasterInstanceName")
    def reset_master_instance_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterInstanceName", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetReplicaConfiguration")
    def reset_replica_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicaConfiguration", []))

    @jsii.member(jsii_name="resetRestoreBackupContext")
    def reset_restore_backup_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreBackupContext", []))

    @jsii.member(jsii_name="resetRootPassword")
    def reset_root_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootPassword", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

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
    @jsii.member(jsii_name="availableMaintenanceVersions")
    def available_maintenance_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availableMaintenanceVersions"))

    @builtins.property
    @jsii.member(jsii_name="clone")
    def clone(self) -> "GoogleSqlDatabaseInstanceCloneOutputReference":
        return typing.cast("GoogleSqlDatabaseInstanceCloneOutputReference", jsii.get(self, "clone"))

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @builtins.property
    @jsii.member(jsii_name="firstIpAddress")
    def first_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> "GoogleSqlDatabaseInstanceIpAddressList":
        return typing.cast("GoogleSqlDatabaseInstanceIpAddressList", jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddress")
    def public_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="replicaConfiguration")
    def replica_configuration(
        self,
    ) -> "GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference":
        return typing.cast("GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference", jsii.get(self, "replicaConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="restoreBackupContext")
    def restore_backup_context(
        self,
    ) -> "GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference":
        return typing.cast("GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference", jsii.get(self, "restoreBackupContext"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="serverCaCert")
    def server_ca_cert(self) -> "GoogleSqlDatabaseInstanceServerCaCertList":
        return typing.cast("GoogleSqlDatabaseInstanceServerCaCertList", jsii.get(self, "serverCaCert"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountEmailAddress"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "GoogleSqlDatabaseInstanceSettingsOutputReference":
        return typing.cast("GoogleSqlDatabaseInstanceSettingsOutputReference", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleSqlDatabaseInstanceTimeoutsOutputReference":
        return typing.cast("GoogleSqlDatabaseInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="cloneInput")
    def clone_input(self) -> typing.Optional["GoogleSqlDatabaseInstanceClone"]:
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceClone"], jsii.get(self, "cloneInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseVersionInput")
    def database_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyNameInput")
    def encryption_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceVersionInput")
    def maintenance_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceNameInput")
    def master_instance_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterInstanceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="replicaConfigurationInput")
    def replica_configuration_input(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceReplicaConfiguration"]:
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceReplicaConfiguration"], jsii.get(self, "replicaConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreBackupContextInput")
    def restore_backup_context_input(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceRestoreBackupContext"]:
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceRestoreBackupContext"], jsii.get(self, "restoreBackupContextInput"))

    @builtins.property
    @jsii.member(jsii_name="rootPasswordInput")
    def root_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional["GoogleSqlDatabaseInstanceSettings"]:
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettings"], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleSqlDatabaseInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleSqlDatabaseInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseVersion")
    def database_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseVersion"))

    @database_version.setter
    def database_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "database_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseVersion", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "deletion_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyName")
    def encryption_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionKeyName"))

    @encryption_key_name.setter
    def encryption_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "encryption_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceVersion")
    def maintenance_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceVersion"))

    @maintenance_version.setter
    def maintenance_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "maintenance_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceVersion", value)

    @builtins.property
    @jsii.member(jsii_name="masterInstanceName")
    def master_instance_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterInstanceName"))

    @master_instance_name.setter
    def master_instance_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "master_instance_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterInstanceName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="rootPassword")
    def root_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootPassword"))

    @root_password.setter
    def root_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstance, "root_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootPassword", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceClone",
    jsii_struct_bases=[],
    name_mapping={
        "source_instance_name": "sourceInstanceName",
        "allocated_ip_range": "allocatedIpRange",
        "point_in_time": "pointInTime",
    },
)
class GoogleSqlDatabaseInstanceClone:
    def __init__(
        self,
        *,
        source_instance_name: builtins.str,
        allocated_ip_range: typing.Optional[builtins.str] = None,
        point_in_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_instance_name: The name of the instance from which the point in time should be restored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#source_instance_name GoogleSqlDatabaseInstance#source_instance_name}
        :param allocated_ip_range: The name of the allocated ip range for the private ip CloudSQL instance. For example: "google-managed-services-default". If set, the cloned instance ip will be created in the allocated range. The range name must comply with `RFC 1035 <https://tools.ietf.org/html/rfc1035>`_. Specifically, the name must be 1-63 characters long and match the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#allocated_ip_range GoogleSqlDatabaseInstance#allocated_ip_range}
        :param point_in_time: The timestamp of the point in time that should be restored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#point_in_time GoogleSqlDatabaseInstance#point_in_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceClone.__init__)
            check_type(argname="argument source_instance_name", value=source_instance_name, expected_type=type_hints["source_instance_name"])
            check_type(argname="argument allocated_ip_range", value=allocated_ip_range, expected_type=type_hints["allocated_ip_range"])
            check_type(argname="argument point_in_time", value=point_in_time, expected_type=type_hints["point_in_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_instance_name": source_instance_name,
        }
        if allocated_ip_range is not None:
            self._values["allocated_ip_range"] = allocated_ip_range
        if point_in_time is not None:
            self._values["point_in_time"] = point_in_time

    @builtins.property
    def source_instance_name(self) -> builtins.str:
        '''The name of the instance from which the point in time should be restored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#source_instance_name GoogleSqlDatabaseInstance#source_instance_name}
        '''
        result = self._values.get("source_instance_name")
        assert result is not None, "Required property 'source_instance_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocated_ip_range(self) -> typing.Optional[builtins.str]:
        '''The name of the allocated ip range for the private ip CloudSQL instance.

        For example: "google-managed-services-default". If set, the cloned instance ip will be created in the allocated range. The range name must comply with `RFC 1035 <https://tools.ietf.org/html/rfc1035>`_. Specifically, the name must be 1-63 characters long and match the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#allocated_ip_range GoogleSqlDatabaseInstance#allocated_ip_range}
        '''
        result = self._values.get("allocated_ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def point_in_time(self) -> typing.Optional[builtins.str]:
        '''The timestamp of the point in time that should be restored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#point_in_time GoogleSqlDatabaseInstance#point_in_time}
        '''
        result = self._values.get("point_in_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceClone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceCloneOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceCloneOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceCloneOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllocatedIpRange")
    def reset_allocated_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocatedIpRange", []))

    @jsii.member(jsii_name="resetPointInTime")
    def reset_point_in_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTime", []))

    @builtins.property
    @jsii.member(jsii_name="allocatedIpRangeInput")
    def allocated_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocatedIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeInput")
    def point_in_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pointInTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInstanceNameInput")
    def source_instance_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInstanceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="allocatedIpRange")
    def allocated_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocatedIpRange"))

    @allocated_ip_range.setter
    def allocated_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceCloneOutputReference, "allocated_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatedIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="pointInTime")
    def point_in_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pointInTime"))

    @point_in_time.setter
    def point_in_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceCloneOutputReference, "point_in_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pointInTime", value)

    @builtins.property
    @jsii.member(jsii_name="sourceInstanceName")
    def source_instance_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceInstanceName"))

    @source_instance_name.setter
    def source_instance_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceCloneOutputReference, "source_instance_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceInstanceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSqlDatabaseInstanceClone]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceClone], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceClone],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceCloneOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_version": "databaseVersion",
        "clone": "clone",
        "deletion_protection": "deletionProtection",
        "encryption_key_name": "encryptionKeyName",
        "id": "id",
        "maintenance_version": "maintenanceVersion",
        "master_instance_name": "masterInstanceName",
        "name": "name",
        "project": "project",
        "region": "region",
        "replica_configuration": "replicaConfiguration",
        "restore_backup_context": "restoreBackupContext",
        "root_password": "rootPassword",
        "settings": "settings",
        "timeouts": "timeouts",
    },
)
class GoogleSqlDatabaseInstanceConfig(cdktf.TerraformMetaArguments):
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
        database_version: builtins.str,
        clone: typing.Optional[typing.Union[GoogleSqlDatabaseInstanceClone, typing.Dict[str, typing.Any]]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_key_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_version: typing.Optional[builtins.str] = None,
        master_instance_name: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        replica_configuration: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceReplicaConfiguration", typing.Dict[str, typing.Any]]] = None,
        restore_backup_context: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceRestoreBackupContext", typing.Dict[str, typing.Any]]] = None,
        root_password: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettings", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database_version: The MySQL, PostgreSQL or SQL Server (beta) version to use. Supported values include MYSQL_5_6, MYSQL_5_7, MYSQL_8_0, POSTGRES_9_6, POSTGRES_10, POSTGRES_11, POSTGRES_12, POSTGRES_13, POSTGRES_14, SQLSERVER_2017_STANDARD, SQLSERVER_2017_ENTERPRISE, SQLSERVER_2017_EXPRESS, SQLSERVER_2017_WEB. Database Version Policies includes an up-to-date reference of supported versions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#database_version GoogleSqlDatabaseInstance#database_version}
        :param clone: clone block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#clone GoogleSqlDatabaseInstance#clone}
        :param deletion_protection: Used to block Terraform from deleting a SQL Instance. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#deletion_protection GoogleSqlDatabaseInstance#deletion_protection}
        :param encryption_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#encryption_key_name GoogleSqlDatabaseInstance#encryption_key_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#id GoogleSqlDatabaseInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_version: Maintenance version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#maintenance_version GoogleSqlDatabaseInstance#maintenance_version}
        :param master_instance_name: The name of the instance that will act as the master in the replication setup. Note, this requires the master to have binary_log_enabled set, as well as existing backups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#master_instance_name GoogleSqlDatabaseInstance#master_instance_name}
        :param name: The name of the instance. If the name is left blank, Terraform will randomly generate one when the instance is first created. This is done because after a name is used, it cannot be reused for up to one week. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#name GoogleSqlDatabaseInstance#name}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#project GoogleSqlDatabaseInstance#project}
        :param region: The region the instance will sit in. Note, Cloud SQL is not available in all regions. A valid region must be provided to use this resource. If a region is not provided in the resource definition, the provider region will be used instead, but this will be an apply-time error for instances if the provider region is not supported with Cloud SQL. If you choose not to provide the region argument for this resource, make sure you understand this. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#region GoogleSqlDatabaseInstance#region}
        :param replica_configuration: replica_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#replica_configuration GoogleSqlDatabaseInstance#replica_configuration}
        :param restore_backup_context: restore_backup_context block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#restore_backup_context GoogleSqlDatabaseInstance#restore_backup_context}
        :param root_password: Initial root password. Required for MS SQL Server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#root_password GoogleSqlDatabaseInstance#root_password}
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#settings GoogleSqlDatabaseInstance#settings}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#timeouts GoogleSqlDatabaseInstance#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(clone, dict):
            clone = GoogleSqlDatabaseInstanceClone(**clone)
        if isinstance(replica_configuration, dict):
            replica_configuration = GoogleSqlDatabaseInstanceReplicaConfiguration(**replica_configuration)
        if isinstance(restore_backup_context, dict):
            restore_backup_context = GoogleSqlDatabaseInstanceRestoreBackupContext(**restore_backup_context)
        if isinstance(settings, dict):
            settings = GoogleSqlDatabaseInstanceSettings(**settings)
        if isinstance(timeouts, dict):
            timeouts = GoogleSqlDatabaseInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_version", value=database_version, expected_type=type_hints["database_version"])
            check_type(argname="argument clone", value=clone, expected_type=type_hints["clone"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument encryption_key_name", value=encryption_key_name, expected_type=type_hints["encryption_key_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance_version", value=maintenance_version, expected_type=type_hints["maintenance_version"])
            check_type(argname="argument master_instance_name", value=master_instance_name, expected_type=type_hints["master_instance_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument replica_configuration", value=replica_configuration, expected_type=type_hints["replica_configuration"])
            check_type(argname="argument restore_backup_context", value=restore_backup_context, expected_type=type_hints["restore_backup_context"])
            check_type(argname="argument root_password", value=root_password, expected_type=type_hints["root_password"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_version": database_version,
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
        if clone is not None:
            self._values["clone"] = clone
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if encryption_key_name is not None:
            self._values["encryption_key_name"] = encryption_key_name
        if id is not None:
            self._values["id"] = id
        if maintenance_version is not None:
            self._values["maintenance_version"] = maintenance_version
        if master_instance_name is not None:
            self._values["master_instance_name"] = master_instance_name
        if name is not None:
            self._values["name"] = name
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if replica_configuration is not None:
            self._values["replica_configuration"] = replica_configuration
        if restore_backup_context is not None:
            self._values["restore_backup_context"] = restore_backup_context
        if root_password is not None:
            self._values["root_password"] = root_password
        if settings is not None:
            self._values["settings"] = settings
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
    def database_version(self) -> builtins.str:
        '''The MySQL, PostgreSQL or SQL Server (beta) version to use.

        Supported values include MYSQL_5_6, MYSQL_5_7, MYSQL_8_0, POSTGRES_9_6, POSTGRES_10, POSTGRES_11, POSTGRES_12, POSTGRES_13, POSTGRES_14, SQLSERVER_2017_STANDARD, SQLSERVER_2017_ENTERPRISE, SQLSERVER_2017_EXPRESS, SQLSERVER_2017_WEB. Database Version Policies includes an up-to-date reference of supported versions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#database_version GoogleSqlDatabaseInstance#database_version}
        '''
        result = self._values.get("database_version")
        assert result is not None, "Required property 'database_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def clone(self) -> typing.Optional[GoogleSqlDatabaseInstanceClone]:
        '''clone block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#clone GoogleSqlDatabaseInstance#clone}
        '''
        result = self._values.get("clone")
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceClone], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Used to block Terraform from deleting a SQL Instance. Defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#deletion_protection GoogleSqlDatabaseInstance#deletion_protection}
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption_key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#encryption_key_name GoogleSqlDatabaseInstance#encryption_key_name}.'''
        result = self._values.get("encryption_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#id GoogleSqlDatabaseInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_version(self) -> typing.Optional[builtins.str]:
        '''Maintenance version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#maintenance_version GoogleSqlDatabaseInstance#maintenance_version}
        '''
        result = self._values.get("maintenance_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_instance_name(self) -> typing.Optional[builtins.str]:
        '''The name of the instance that will act as the master in the replication setup.

        Note, this requires the master to have binary_log_enabled set, as well as existing backups.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#master_instance_name GoogleSqlDatabaseInstance#master_instance_name}
        '''
        result = self._values.get("master_instance_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the instance.

        If the name is left blank, Terraform will randomly generate one when the instance is first created. This is done because after a name is used, it cannot be reused for up to one week.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#name GoogleSqlDatabaseInstance#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#project GoogleSqlDatabaseInstance#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the instance will sit in.

        Note, Cloud SQL is not available in all regions. A valid region must be provided to use this resource. If a region is not provided in the resource definition, the provider region will be used instead, but this will be an apply-time error for instances if the provider region is not supported with Cloud SQL. If you choose not to provide the region argument for this resource, make sure you understand this.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#region GoogleSqlDatabaseInstance#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replica_configuration(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceReplicaConfiguration"]:
        '''replica_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#replica_configuration GoogleSqlDatabaseInstance#replica_configuration}
        '''
        result = self._values.get("replica_configuration")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceReplicaConfiguration"], result)

    @builtins.property
    def restore_backup_context(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceRestoreBackupContext"]:
        '''restore_backup_context block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#restore_backup_context GoogleSqlDatabaseInstance#restore_backup_context}
        '''
        result = self._values.get("restore_backup_context")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceRestoreBackupContext"], result)

    @builtins.property
    def root_password(self) -> typing.Optional[builtins.str]:
        '''Initial root password. Required for MS SQL Server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#root_password GoogleSqlDatabaseInstance#root_password}
        '''
        result = self._values.get("root_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional["GoogleSqlDatabaseInstanceSettings"]:
        '''settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#settings GoogleSqlDatabaseInstance#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettings"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleSqlDatabaseInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#timeouts GoogleSqlDatabaseInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceIpAddress",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleSqlDatabaseInstanceIpAddress:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceIpAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceIpAddressList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceIpAddressList",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceIpAddressList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleSqlDatabaseInstanceIpAddressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceIpAddressList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleSqlDatabaseInstanceIpAddressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceIpAddressList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceIpAddressList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceIpAddressList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleSqlDatabaseInstanceIpAddressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceIpAddressOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceIpAddressOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="timeToRetire")
    def time_to_retire(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeToRetire"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSqlDatabaseInstanceIpAddress]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceIpAddress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceIpAddress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceIpAddressOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceReplicaConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificate": "caCertificate",
        "client_certificate": "clientCertificate",
        "client_key": "clientKey",
        "connect_retry_interval": "connectRetryInterval",
        "dump_file_path": "dumpFilePath",
        "failover_target": "failoverTarget",
        "master_heartbeat_period": "masterHeartbeatPeriod",
        "password": "password",
        "ssl_cipher": "sslCipher",
        "username": "username",
        "verify_server_certificate": "verifyServerCertificate",
    },
)
class GoogleSqlDatabaseInstanceReplicaConfiguration:
    def __init__(
        self,
        *,
        ca_certificate: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        connect_retry_interval: typing.Optional[jsii.Number] = None,
        dump_file_path: typing.Optional[builtins.str] = None,
        failover_target: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        master_heartbeat_period: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        ssl_cipher: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        verify_server_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param ca_certificate: PEM representation of the trusted CA's x509 certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ca_certificate GoogleSqlDatabaseInstance#ca_certificate}
        :param client_certificate: PEM representation of the replica's x509 certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#client_certificate GoogleSqlDatabaseInstance#client_certificate}
        :param client_key: PEM representation of the replica's private key. The corresponding public key in encoded in the client_certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#client_key GoogleSqlDatabaseInstance#client_key}
        :param connect_retry_interval: The number of seconds between connect retries. MySQL's default is 60 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#connect_retry_interval GoogleSqlDatabaseInstance#connect_retry_interval}
        :param dump_file_path: Path to a SQL file in Google Cloud Storage from which replica instances are created. Format is gs://bucket/filename. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#dump_file_path GoogleSqlDatabaseInstance#dump_file_path}
        :param failover_target: Specifies if the replica is the failover target. If the field is set to true the replica will be designated as a failover replica. If the master instance fails, the replica instance will be promoted as the new master instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#failover_target GoogleSqlDatabaseInstance#failover_target}
        :param master_heartbeat_period: Time in ms between replication heartbeats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#master_heartbeat_period GoogleSqlDatabaseInstance#master_heartbeat_period}
        :param password: Password for the replication connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password GoogleSqlDatabaseInstance#password}
        :param ssl_cipher: Permissible ciphers for use in SSL encryption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ssl_cipher GoogleSqlDatabaseInstance#ssl_cipher}
        :param username: Username for replication connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#username GoogleSqlDatabaseInstance#username}
        :param verify_server_certificate: True if the master's common name value is checked during the SSL handshake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#verify_server_certificate GoogleSqlDatabaseInstance#verify_server_certificate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceReplicaConfiguration.__init__)
            check_type(argname="argument ca_certificate", value=ca_certificate, expected_type=type_hints["ca_certificate"])
            check_type(argname="argument client_certificate", value=client_certificate, expected_type=type_hints["client_certificate"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument connect_retry_interval", value=connect_retry_interval, expected_type=type_hints["connect_retry_interval"])
            check_type(argname="argument dump_file_path", value=dump_file_path, expected_type=type_hints["dump_file_path"])
            check_type(argname="argument failover_target", value=failover_target, expected_type=type_hints["failover_target"])
            check_type(argname="argument master_heartbeat_period", value=master_heartbeat_period, expected_type=type_hints["master_heartbeat_period"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument ssl_cipher", value=ssl_cipher, expected_type=type_hints["ssl_cipher"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument verify_server_certificate", value=verify_server_certificate, expected_type=type_hints["verify_server_certificate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificate is not None:
            self._values["ca_certificate"] = ca_certificate
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if client_key is not None:
            self._values["client_key"] = client_key
        if connect_retry_interval is not None:
            self._values["connect_retry_interval"] = connect_retry_interval
        if dump_file_path is not None:
            self._values["dump_file_path"] = dump_file_path
        if failover_target is not None:
            self._values["failover_target"] = failover_target
        if master_heartbeat_period is not None:
            self._values["master_heartbeat_period"] = master_heartbeat_period
        if password is not None:
            self._values["password"] = password
        if ssl_cipher is not None:
            self._values["ssl_cipher"] = ssl_cipher
        if username is not None:
            self._values["username"] = username
        if verify_server_certificate is not None:
            self._values["verify_server_certificate"] = verify_server_certificate

    @builtins.property
    def ca_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM representation of the trusted CA's x509 certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ca_certificate GoogleSqlDatabaseInstance#ca_certificate}
        '''
        result = self._values.get("ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM representation of the replica's x509 certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#client_certificate GoogleSqlDatabaseInstance#client_certificate}
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''PEM representation of the replica's private key. The corresponding public key in encoded in the client_certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#client_key GoogleSqlDatabaseInstance#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connect_retry_interval(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds between connect retries. MySQL's default is 60 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#connect_retry_interval GoogleSqlDatabaseInstance#connect_retry_interval}
        '''
        result = self._values.get("connect_retry_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dump_file_path(self) -> typing.Optional[builtins.str]:
        '''Path to a SQL file in Google Cloud Storage from which replica instances are created. Format is gs://bucket/filename.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#dump_file_path GoogleSqlDatabaseInstance#dump_file_path}
        '''
        result = self._values.get("dump_file_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failover_target(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the replica is the failover target.

        If the field is set to true the replica will be designated as a failover replica. If the master instance fails, the replica instance will be promoted as the new master instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#failover_target GoogleSqlDatabaseInstance#failover_target}
        '''
        result = self._values.get("failover_target")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def master_heartbeat_period(self) -> typing.Optional[jsii.Number]:
        '''Time in ms between replication heartbeats.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#master_heartbeat_period GoogleSqlDatabaseInstance#master_heartbeat_period}
        '''
        result = self._values.get("master_heartbeat_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for the replication connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password GoogleSqlDatabaseInstance#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_cipher(self) -> typing.Optional[builtins.str]:
        '''Permissible ciphers for use in SSL encryption.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ssl_cipher GoogleSqlDatabaseInstance#ssl_cipher}
        '''
        result = self._values.get("ssl_cipher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for replication connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#username GoogleSqlDatabaseInstance#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_server_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if the master's common name value is checked during the SSL handshake.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#verify_server_certificate GoogleSqlDatabaseInstance#verify_server_certificate}
        '''
        result = self._values.get("verify_server_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceReplicaConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaCertificate")
    def reset_ca_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCertificate", []))

    @jsii.member(jsii_name="resetClientCertificate")
    def reset_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificate", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetConnectRetryInterval")
    def reset_connect_retry_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectRetryInterval", []))

    @jsii.member(jsii_name="resetDumpFilePath")
    def reset_dump_file_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDumpFilePath", []))

    @jsii.member(jsii_name="resetFailoverTarget")
    def reset_failover_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailoverTarget", []))

    @jsii.member(jsii_name="resetMasterHeartbeatPeriod")
    def reset_master_heartbeat_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterHeartbeatPeriod", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSslCipher")
    def reset_ssl_cipher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslCipher", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetVerifyServerCertificate")
    def reset_verify_server_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyServerCertificate", []))

    @builtins.property
    @jsii.member(jsii_name="caCertificateInput")
    def ca_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateInput")
    def client_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="connectRetryIntervalInput")
    def connect_retry_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectRetryIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="dumpFilePathInput")
    def dump_file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dumpFilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverTargetInput")
    def failover_target_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failoverTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="masterHeartbeatPeriodInput")
    def master_heartbeat_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "masterHeartbeatPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="sslCipherInput")
    def ssl_cipher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslCipherInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyServerCertificateInput")
    def verify_server_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifyServerCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertificate")
    def ca_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCertificate"))

    @ca_certificate.setter
    def ca_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "ca_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificate"))

    @client_certificate.setter
    def client_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "client_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="connectRetryInterval")
    def connect_retry_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectRetryInterval"))

    @connect_retry_interval.setter
    def connect_retry_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "connect_retry_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectRetryInterval", value)

    @builtins.property
    @jsii.member(jsii_name="dumpFilePath")
    def dump_file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dumpFilePath"))

    @dump_file_path.setter
    def dump_file_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "dump_file_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dumpFilePath", value)

    @builtins.property
    @jsii.member(jsii_name="failoverTarget")
    def failover_target(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failoverTarget"))

    @failover_target.setter
    def failover_target(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "failover_target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failoverTarget", value)

    @builtins.property
    @jsii.member(jsii_name="masterHeartbeatPeriod")
    def master_heartbeat_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "masterHeartbeatPeriod"))

    @master_heartbeat_period.setter
    def master_heartbeat_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "master_heartbeat_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterHeartbeatPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="sslCipher")
    def ssl_cipher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCipher"))

    @ssl_cipher.setter
    def ssl_cipher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "ssl_cipher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslCipher", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="verifyServerCertificate")
    def verify_server_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifyServerCertificate"))

    @verify_server_certificate.setter
    def verify_server_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "verify_server_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyServerCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceReplicaConfiguration]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceReplicaConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceReplicaConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceRestoreBackupContext",
    jsii_struct_bases=[],
    name_mapping={
        "backup_run_id": "backupRunId",
        "instance_id": "instanceId",
        "project": "project",
    },
)
class GoogleSqlDatabaseInstanceRestoreBackupContext:
    def __init__(
        self,
        *,
        backup_run_id: jsii.Number,
        instance_id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backup_run_id: The ID of the backup run to restore from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_run_id GoogleSqlDatabaseInstance#backup_run_id}
        :param instance_id: The ID of the instance that the backup was taken from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#instance_id GoogleSqlDatabaseInstance#instance_id}
        :param project: The full project ID of the source instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#project GoogleSqlDatabaseInstance#project}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceRestoreBackupContext.__init__)
            check_type(argname="argument backup_run_id", value=backup_run_id, expected_type=type_hints["backup_run_id"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        self._values: typing.Dict[str, typing.Any] = {
            "backup_run_id": backup_run_id,
        }
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if project is not None:
            self._values["project"] = project

    @builtins.property
    def backup_run_id(self) -> jsii.Number:
        '''The ID of the backup run to restore from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_run_id GoogleSqlDatabaseInstance#backup_run_id}
        '''
        result = self._values.get("backup_run_id")
        assert result is not None, "Required property 'backup_run_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the instance that the backup was taken from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#instance_id GoogleSqlDatabaseInstance#instance_id}
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The full project ID of the source instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#project GoogleSqlDatabaseInstance#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceRestoreBackupContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceId")
    def reset_instance_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @builtins.property
    @jsii.member(jsii_name="backupRunIdInput")
    def backup_run_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupRunIdInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="backupRunId")
    def backup_run_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupRunId"))

    @backup_run_id.setter
    def backup_run_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference, "backup_run_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRunId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference, "instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceRestoreBackupContext]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceRestoreBackupContext], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceRestoreBackupContext],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceServerCaCert",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleSqlDatabaseInstanceServerCaCert:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceServerCaCert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceServerCaCertList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceServerCaCertList",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceServerCaCertList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleSqlDatabaseInstanceServerCaCertOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceServerCaCertList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleSqlDatabaseInstanceServerCaCertOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceServerCaCertList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceServerCaCertList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceServerCaCertList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleSqlDatabaseInstanceServerCaCertOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceServerCaCertOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceServerCaCertOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cert")
    def cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cert"))

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="expirationTime")
    def expiration_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationTime"))

    @builtins.property
    @jsii.member(jsii_name="sha1Fingerprint")
    def sha1_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha1Fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSqlDatabaseInstanceServerCaCert]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceServerCaCert], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceServerCaCert],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceServerCaCertOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettings",
    jsii_struct_bases=[],
    name_mapping={
        "tier": "tier",
        "activation_policy": "activationPolicy",
        "active_directory_config": "activeDirectoryConfig",
        "availability_type": "availabilityType",
        "backup_configuration": "backupConfiguration",
        "collation": "collation",
        "database_flags": "databaseFlags",
        "disk_autoresize": "diskAutoresize",
        "disk_autoresize_limit": "diskAutoresizeLimit",
        "disk_size": "diskSize",
        "disk_type": "diskType",
        "insights_config": "insightsConfig",
        "ip_configuration": "ipConfiguration",
        "location_preference": "locationPreference",
        "maintenance_window": "maintenanceWindow",
        "password_validation_policy": "passwordValidationPolicy",
        "pricing_plan": "pricingPlan",
        "sql_server_audit_config": "sqlServerAuditConfig",
        "user_labels": "userLabels",
    },
)
class GoogleSqlDatabaseInstanceSettings:
    def __init__(
        self,
        *,
        tier: builtins.str,
        activation_policy: typing.Optional[builtins.str] = None,
        active_directory_config: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig", typing.Dict[str, typing.Any]]] = None,
        availability_type: typing.Optional[builtins.str] = None,
        backup_configuration: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsBackupConfiguration", typing.Dict[str, typing.Any]]] = None,
        collation: typing.Optional[builtins.str] = None,
        database_flags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSqlDatabaseInstanceSettingsDatabaseFlags", typing.Dict[str, typing.Any]]]]] = None,
        disk_autoresize: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disk_autoresize_limit: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[builtins.str] = None,
        insights_config: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsInsightsConfig", typing.Dict[str, typing.Any]]] = None,
        ip_configuration: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsIpConfiguration", typing.Dict[str, typing.Any]]] = None,
        location_preference: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsLocationPreference", typing.Dict[str, typing.Any]]] = None,
        maintenance_window: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        password_validation_policy: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy", typing.Dict[str, typing.Any]]] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        sql_server_audit_config: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig", typing.Dict[str, typing.Any]]] = None,
        user_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param tier: The machine type to use. See tiers for more details and supported versions. Postgres supports only shared-core machine types, and custom machine types such as db-custom-2-13312. See the Custom Machine Type Documentation to learn about specifying custom machine types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#tier GoogleSqlDatabaseInstance#tier}
        :param activation_policy: This specifies when the instance should be active. Can be either ALWAYS, NEVER or ON_DEMAND. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#activation_policy GoogleSqlDatabaseInstance#activation_policy}
        :param active_directory_config: active_directory_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#active_directory_config GoogleSqlDatabaseInstance#active_directory_config}
        :param availability_type: The availability type of the Cloud SQL instance, high availability (REGIONAL) or single zone (ZONAL). For all instances, ensure that settings.backup_configuration.enabled is set to true. For MySQL instances, ensure that settings.backup_configuration.binary_log_enabled is set to true. For Postgres instances, ensure that settings.backup_configuration.point_in_time_recovery_enabled is set to true. Defaults to ZONAL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#availability_type GoogleSqlDatabaseInstance#availability_type}
        :param backup_configuration: backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_configuration GoogleSqlDatabaseInstance#backup_configuration}
        :param collation: The name of server instance collation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#collation GoogleSqlDatabaseInstance#collation}
        :param database_flags: database_flags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#database_flags GoogleSqlDatabaseInstance#database_flags}
        :param disk_autoresize: Enables auto-resizing of the storage size. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_autoresize GoogleSqlDatabaseInstance#disk_autoresize}
        :param disk_autoresize_limit: The maximum size, in GB, to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_autoresize_limit GoogleSqlDatabaseInstance#disk_autoresize_limit}
        :param disk_size: The size of data disk, in GB. Size of a running instance cannot be reduced but can be increased. The minimum value is 10GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_size GoogleSqlDatabaseInstance#disk_size}
        :param disk_type: The type of data disk: PD_SSD or PD_HDD. Defaults to PD_SSD. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_type GoogleSqlDatabaseInstance#disk_type}
        :param insights_config: insights_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#insights_config GoogleSqlDatabaseInstance#insights_config}
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ip_configuration GoogleSqlDatabaseInstance#ip_configuration}
        :param location_preference: location_preference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#location_preference GoogleSqlDatabaseInstance#location_preference}
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#maintenance_window GoogleSqlDatabaseInstance#maintenance_window}
        :param password_validation_policy: password_validation_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password_validation_policy GoogleSqlDatabaseInstance#password_validation_policy}
        :param pricing_plan: Pricing plan for this instance, can only be PER_USE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#pricing_plan GoogleSqlDatabaseInstance#pricing_plan}
        :param sql_server_audit_config: sql_server_audit_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#sql_server_audit_config GoogleSqlDatabaseInstance#sql_server_audit_config}
        :param user_labels: A set of key/value user label pairs to assign to the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#user_labels GoogleSqlDatabaseInstance#user_labels}
        '''
        if isinstance(active_directory_config, dict):
            active_directory_config = GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig(**active_directory_config)
        if isinstance(backup_configuration, dict):
            backup_configuration = GoogleSqlDatabaseInstanceSettingsBackupConfiguration(**backup_configuration)
        if isinstance(insights_config, dict):
            insights_config = GoogleSqlDatabaseInstanceSettingsInsightsConfig(**insights_config)
        if isinstance(ip_configuration, dict):
            ip_configuration = GoogleSqlDatabaseInstanceSettingsIpConfiguration(**ip_configuration)
        if isinstance(location_preference, dict):
            location_preference = GoogleSqlDatabaseInstanceSettingsLocationPreference(**location_preference)
        if isinstance(maintenance_window, dict):
            maintenance_window = GoogleSqlDatabaseInstanceSettingsMaintenanceWindow(**maintenance_window)
        if isinstance(password_validation_policy, dict):
            password_validation_policy = GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy(**password_validation_policy)
        if isinstance(sql_server_audit_config, dict):
            sql_server_audit_config = GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig(**sql_server_audit_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettings.__init__)
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument activation_policy", value=activation_policy, expected_type=type_hints["activation_policy"])
            check_type(argname="argument active_directory_config", value=active_directory_config, expected_type=type_hints["active_directory_config"])
            check_type(argname="argument availability_type", value=availability_type, expected_type=type_hints["availability_type"])
            check_type(argname="argument backup_configuration", value=backup_configuration, expected_type=type_hints["backup_configuration"])
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument database_flags", value=database_flags, expected_type=type_hints["database_flags"])
            check_type(argname="argument disk_autoresize", value=disk_autoresize, expected_type=type_hints["disk_autoresize"])
            check_type(argname="argument disk_autoresize_limit", value=disk_autoresize_limit, expected_type=type_hints["disk_autoresize_limit"])
            check_type(argname="argument disk_size", value=disk_size, expected_type=type_hints["disk_size"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
            check_type(argname="argument insights_config", value=insights_config, expected_type=type_hints["insights_config"])
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument location_preference", value=location_preference, expected_type=type_hints["location_preference"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument password_validation_policy", value=password_validation_policy, expected_type=type_hints["password_validation_policy"])
            check_type(argname="argument pricing_plan", value=pricing_plan, expected_type=type_hints["pricing_plan"])
            check_type(argname="argument sql_server_audit_config", value=sql_server_audit_config, expected_type=type_hints["sql_server_audit_config"])
            check_type(argname="argument user_labels", value=user_labels, expected_type=type_hints["user_labels"])
        self._values: typing.Dict[str, typing.Any] = {
            "tier": tier,
        }
        if activation_policy is not None:
            self._values["activation_policy"] = activation_policy
        if active_directory_config is not None:
            self._values["active_directory_config"] = active_directory_config
        if availability_type is not None:
            self._values["availability_type"] = availability_type
        if backup_configuration is not None:
            self._values["backup_configuration"] = backup_configuration
        if collation is not None:
            self._values["collation"] = collation
        if database_flags is not None:
            self._values["database_flags"] = database_flags
        if disk_autoresize is not None:
            self._values["disk_autoresize"] = disk_autoresize
        if disk_autoresize_limit is not None:
            self._values["disk_autoresize_limit"] = disk_autoresize_limit
        if disk_size is not None:
            self._values["disk_size"] = disk_size
        if disk_type is not None:
            self._values["disk_type"] = disk_type
        if insights_config is not None:
            self._values["insights_config"] = insights_config
        if ip_configuration is not None:
            self._values["ip_configuration"] = ip_configuration
        if location_preference is not None:
            self._values["location_preference"] = location_preference
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if password_validation_policy is not None:
            self._values["password_validation_policy"] = password_validation_policy
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if sql_server_audit_config is not None:
            self._values["sql_server_audit_config"] = sql_server_audit_config
        if user_labels is not None:
            self._values["user_labels"] = user_labels

    @builtins.property
    def tier(self) -> builtins.str:
        '''The machine type to use.

        See tiers for more details and supported versions. Postgres supports only shared-core machine types, and custom machine types such as db-custom-2-13312. See the Custom Machine Type Documentation to learn about specifying custom machine types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#tier GoogleSqlDatabaseInstance#tier}
        '''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def activation_policy(self) -> typing.Optional[builtins.str]:
        '''This specifies when the instance should be active. Can be either ALWAYS, NEVER or ON_DEMAND.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#activation_policy GoogleSqlDatabaseInstance#activation_policy}
        '''
        result = self._values.get("activation_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def active_directory_config(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig"]:
        '''active_directory_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#active_directory_config GoogleSqlDatabaseInstance#active_directory_config}
        '''
        result = self._values.get("active_directory_config")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig"], result)

    @builtins.property
    def availability_type(self) -> typing.Optional[builtins.str]:
        '''The availability type of the Cloud SQL instance, high availability (REGIONAL) or single zone (ZONAL).

        For all instances, ensure that
        settings.backup_configuration.enabled is set to true.
        For MySQL instances, ensure that settings.backup_configuration.binary_log_enabled is set to true.
        For Postgres instances, ensure that settings.backup_configuration.point_in_time_recovery_enabled
        is set to true. Defaults to ZONAL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#availability_type GoogleSqlDatabaseInstance#availability_type}
        '''
        result = self._values.get("availability_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_configuration(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsBackupConfiguration"]:
        '''backup_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_configuration GoogleSqlDatabaseInstance#backup_configuration}
        '''
        result = self._values.get("backup_configuration")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsBackupConfiguration"], result)

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''The name of server instance collation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#collation GoogleSqlDatabaseInstance#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_flags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSqlDatabaseInstanceSettingsDatabaseFlags"]]]:
        '''database_flags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#database_flags GoogleSqlDatabaseInstance#database_flags}
        '''
        result = self._values.get("database_flags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSqlDatabaseInstanceSettingsDatabaseFlags"]]], result)

    @builtins.property
    def disk_autoresize(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables auto-resizing of the storage size. Defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_autoresize GoogleSqlDatabaseInstance#disk_autoresize}
        '''
        result = self._values.get("disk_autoresize")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disk_autoresize_limit(self) -> typing.Optional[jsii.Number]:
        '''The maximum size, in GB, to which storage capacity can be automatically increased.

        The default value is 0, which specifies that there is no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_autoresize_limit GoogleSqlDatabaseInstance#disk_autoresize_limit}
        '''
        result = self._values.get("disk_autoresize_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_size(self) -> typing.Optional[jsii.Number]:
        '''The size of data disk, in GB.

        Size of a running instance cannot be reduced but can be increased. The minimum value is 10GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_size GoogleSqlDatabaseInstance#disk_size}
        '''
        result = self._values.get("disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_type(self) -> typing.Optional[builtins.str]:
        '''The type of data disk: PD_SSD or PD_HDD. Defaults to PD_SSD.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disk_type GoogleSqlDatabaseInstance#disk_type}
        '''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insights_config(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsInsightsConfig"]:
        '''insights_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#insights_config GoogleSqlDatabaseInstance#insights_config}
        '''
        result = self._values.get("insights_config")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsInsightsConfig"], result)

    @builtins.property
    def ip_configuration(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsIpConfiguration"]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ip_configuration GoogleSqlDatabaseInstance#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsIpConfiguration"], result)

    @builtins.property
    def location_preference(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsLocationPreference"]:
        '''location_preference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#location_preference GoogleSqlDatabaseInstance#location_preference}
        '''
        result = self._values.get("location_preference")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsLocationPreference"], result)

    @builtins.property
    def maintenance_window(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsMaintenanceWindow"]:
        '''maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#maintenance_window GoogleSqlDatabaseInstance#maintenance_window}
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsMaintenanceWindow"], result)

    @builtins.property
    def password_validation_policy(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy"]:
        '''password_validation_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password_validation_policy GoogleSqlDatabaseInstance#password_validation_policy}
        '''
        result = self._values.get("password_validation_policy")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy"], result)

    @builtins.property
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''Pricing plan for this instance, can only be PER_USE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#pricing_plan GoogleSqlDatabaseInstance#pricing_plan}
        '''
        result = self._values.get("pricing_plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_server_audit_config(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig"]:
        '''sql_server_audit_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#sql_server_audit_config GoogleSqlDatabaseInstance#sql_server_audit_config}
        '''
        result = self._values.get("sql_server_audit_config")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig"], result)

    @builtins.property
    def user_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value user label pairs to assign to the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#user_labels GoogleSqlDatabaseInstance#user_labels}
        '''
        result = self._values.get("user_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig",
    jsii_struct_bases=[],
    name_mapping={"domain": "domain"},
)
class GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig:
    def __init__(self, *, domain: builtins.str) -> None:
        '''
        :param domain: Domain name of the Active Directory for SQL Server (e.g., mydomain.com). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#domain GoogleSqlDatabaseInstance#domain}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig.__init__)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain": domain,
        }

    @builtins.property
    def domain(self) -> builtins.str:
        '''Domain name of the Active Directory for SQL Server (e.g., mydomain.com).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#domain GoogleSqlDatabaseInstance#domain}
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfigOutputReference, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsBackupConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "backup_retention_settings": "backupRetentionSettings",
        "binary_log_enabled": "binaryLogEnabled",
        "enabled": "enabled",
        "location": "location",
        "point_in_time_recovery_enabled": "pointInTimeRecoveryEnabled",
        "start_time": "startTime",
        "transaction_log_retention_days": "transactionLogRetentionDays",
    },
)
class GoogleSqlDatabaseInstanceSettingsBackupConfiguration:
    def __init__(
        self,
        *,
        backup_retention_settings: typing.Optional[typing.Union["GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings", typing.Dict[str, typing.Any]]] = None,
        binary_log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        start_time: typing.Optional[builtins.str] = None,
        transaction_log_retention_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param backup_retention_settings: backup_retention_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_retention_settings GoogleSqlDatabaseInstance#backup_retention_settings}
        :param binary_log_enabled: True if binary logging is enabled. If settings.backup_configuration.enabled is false, this must be as well. Can only be used with MySQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#binary_log_enabled GoogleSqlDatabaseInstance#binary_log_enabled}
        :param enabled: True if backup configuration is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#enabled GoogleSqlDatabaseInstance#enabled}
        :param location: Location of the backup configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#location GoogleSqlDatabaseInstance#location}
        :param point_in_time_recovery_enabled: True if Point-in-time recovery is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#point_in_time_recovery_enabled GoogleSqlDatabaseInstance#point_in_time_recovery_enabled}
        :param start_time: HH:MM format time indicating when backup configuration starts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#start_time GoogleSqlDatabaseInstance#start_time}
        :param transaction_log_retention_days: The number of days of transaction logs we retain for point in time restore, from 1-7. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#transaction_log_retention_days GoogleSqlDatabaseInstance#transaction_log_retention_days}
        '''
        if isinstance(backup_retention_settings, dict):
            backup_retention_settings = GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings(**backup_retention_settings)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsBackupConfiguration.__init__)
            check_type(argname="argument backup_retention_settings", value=backup_retention_settings, expected_type=type_hints["backup_retention_settings"])
            check_type(argname="argument binary_log_enabled", value=binary_log_enabled, expected_type=type_hints["binary_log_enabled"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument point_in_time_recovery_enabled", value=point_in_time_recovery_enabled, expected_type=type_hints["point_in_time_recovery_enabled"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument transaction_log_retention_days", value=transaction_log_retention_days, expected_type=type_hints["transaction_log_retention_days"])
        self._values: typing.Dict[str, typing.Any] = {}
        if backup_retention_settings is not None:
            self._values["backup_retention_settings"] = backup_retention_settings
        if binary_log_enabled is not None:
            self._values["binary_log_enabled"] = binary_log_enabled
        if enabled is not None:
            self._values["enabled"] = enabled
        if location is not None:
            self._values["location"] = location
        if point_in_time_recovery_enabled is not None:
            self._values["point_in_time_recovery_enabled"] = point_in_time_recovery_enabled
        if start_time is not None:
            self._values["start_time"] = start_time
        if transaction_log_retention_days is not None:
            self._values["transaction_log_retention_days"] = transaction_log_retention_days

    @builtins.property
    def backup_retention_settings(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings"]:
        '''backup_retention_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_retention_settings GoogleSqlDatabaseInstance#backup_retention_settings}
        '''
        result = self._values.get("backup_retention_settings")
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings"], result)

    @builtins.property
    def binary_log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if binary logging is enabled.

        If settings.backup_configuration.enabled is false, this must be as well. Can only be used with MySQL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#binary_log_enabled GoogleSqlDatabaseInstance#binary_log_enabled}
        '''
        result = self._values.get("binary_log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if backup configuration is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#enabled GoogleSqlDatabaseInstance#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Location of the backup configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#location GoogleSqlDatabaseInstance#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def point_in_time_recovery_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if Point-in-time recovery is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#point_in_time_recovery_enabled GoogleSqlDatabaseInstance#point_in_time_recovery_enabled}
        '''
        result = self._values.get("point_in_time_recovery_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''HH:MM format time indicating when backup configuration starts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#start_time GoogleSqlDatabaseInstance#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transaction_log_retention_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days of transaction logs we retain for point in time restore, from 1-7.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#transaction_log_retention_days GoogleSqlDatabaseInstance#transaction_log_retention_days}
        '''
        result = self._values.get("transaction_log_retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsBackupConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings",
    jsii_struct_bases=[],
    name_mapping={
        "retained_backups": "retainedBackups",
        "retention_unit": "retentionUnit",
    },
)
class GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings:
    def __init__(
        self,
        *,
        retained_backups: jsii.Number,
        retention_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param retained_backups: Number of backups to retain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retained_backups GoogleSqlDatabaseInstance#retained_backups}
        :param retention_unit: The unit that 'retainedBackups' represents. Defaults to COUNT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retention_unit GoogleSqlDatabaseInstance#retention_unit}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings.__init__)
            check_type(argname="argument retained_backups", value=retained_backups, expected_type=type_hints["retained_backups"])
            check_type(argname="argument retention_unit", value=retention_unit, expected_type=type_hints["retention_unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "retained_backups": retained_backups,
        }
        if retention_unit is not None:
            self._values["retention_unit"] = retention_unit

    @builtins.property
    def retained_backups(self) -> jsii.Number:
        '''Number of backups to retain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retained_backups GoogleSqlDatabaseInstance#retained_backups}
        '''
        result = self._values.get("retained_backups")
        assert result is not None, "Required property 'retained_backups' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def retention_unit(self) -> typing.Optional[builtins.str]:
        '''The unit that 'retainedBackups' represents. Defaults to COUNT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retention_unit GoogleSqlDatabaseInstance#retention_unit}
        '''
        result = self._values.get("retention_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRetentionUnit")
    def reset_retention_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionUnit", []))

    @builtins.property
    @jsii.member(jsii_name="retainedBackupsInput")
    def retained_backups_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retainedBackupsInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionUnitInput")
    def retention_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retentionUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="retainedBackups")
    def retained_backups(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retainedBackups"))

    @retained_backups.setter
    def retained_backups(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference, "retained_backups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retainedBackups", value)

    @builtins.property
    @jsii.member(jsii_name="retentionUnit")
    def retention_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retentionUnit"))

    @retention_unit.setter
    def retention_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference, "retention_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionUnit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackupRetentionSettings")
    def put_backup_retention_settings(
        self,
        *,
        retained_backups: jsii.Number,
        retention_unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param retained_backups: Number of backups to retain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retained_backups GoogleSqlDatabaseInstance#retained_backups}
        :param retention_unit: The unit that 'retainedBackups' represents. Defaults to COUNT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retention_unit GoogleSqlDatabaseInstance#retention_unit}
        '''
        value = GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings(
            retained_backups=retained_backups, retention_unit=retention_unit
        )

        return typing.cast(None, jsii.invoke(self, "putBackupRetentionSettings", [value]))

    @jsii.member(jsii_name="resetBackupRetentionSettings")
    def reset_backup_retention_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupRetentionSettings", []))

    @jsii.member(jsii_name="resetBinaryLogEnabled")
    def reset_binary_log_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBinaryLogEnabled", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetPointInTimeRecoveryEnabled")
    def reset_point_in_time_recovery_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTimeRecoveryEnabled", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetTransactionLogRetentionDays")
    def reset_transaction_log_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransactionLogRetentionDays", []))

    @builtins.property
    @jsii.member(jsii_name="backupRetentionSettings")
    def backup_retention_settings(
        self,
    ) -> GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference, jsii.get(self, "backupRetentionSettings"))

    @builtins.property
    @jsii.member(jsii_name="backupRetentionSettingsInput")
    def backup_retention_settings_input(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings], jsii.get(self, "backupRetentionSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="binaryLogEnabledInput")
    def binary_log_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "binaryLogEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryEnabledInput")
    def point_in_time_recovery_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pointInTimeRecoveryEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="transactionLogRetentionDaysInput")
    def transaction_log_retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "transactionLogRetentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="binaryLogEnabled")
    def binary_log_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "binaryLogEnabled"))

    @binary_log_enabled.setter
    def binary_log_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference, "binary_log_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "binaryLogEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pointInTimeRecoveryEnabled"))

    @point_in_time_recovery_enabled.setter
    def point_in_time_recovery_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference, "point_in_time_recovery_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pointInTimeRecoveryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="transactionLogRetentionDays")
    def transaction_log_retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "transactionLogRetentionDays"))

    @transaction_log_retention_days.setter
    def transaction_log_retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference, "transaction_log_retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transactionLogRetentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfiguration]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsDatabaseFlags",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class GoogleSqlDatabaseInstanceSettingsDatabaseFlags:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Name of the flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#name GoogleSqlDatabaseInstance#name}
        :param value: Value of the flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#value GoogleSqlDatabaseInstance#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsDatabaseFlags.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the flag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#name GoogleSqlDatabaseInstance#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the flag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#value GoogleSqlDatabaseInstance#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsDatabaseFlags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsDatabaseFlags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsDatabaseFlags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsDatabaseFlags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference.__init__)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSqlDatabaseInstanceSettingsDatabaseFlags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSqlDatabaseInstanceSettingsDatabaseFlags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSqlDatabaseInstanceSettingsDatabaseFlags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsInsightsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "query_insights_enabled": "queryInsightsEnabled",
        "query_string_length": "queryStringLength",
        "record_application_tags": "recordApplicationTags",
        "record_client_address": "recordClientAddress",
    },
)
class GoogleSqlDatabaseInstanceSettingsInsightsConfig:
    def __init__(
        self,
        *,
        query_insights_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        query_string_length: typing.Optional[jsii.Number] = None,
        record_application_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        record_client_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param query_insights_enabled: True if Query Insights feature is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#query_insights_enabled GoogleSqlDatabaseInstance#query_insights_enabled}
        :param query_string_length: Maximum query length stored in bytes. Between 256 and 4500. Default to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#query_string_length GoogleSqlDatabaseInstance#query_string_length}
        :param record_application_tags: True if Query Insights will record application tags from query when enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#record_application_tags GoogleSqlDatabaseInstance#record_application_tags}
        :param record_client_address: True if Query Insights will record client address when enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#record_client_address GoogleSqlDatabaseInstance#record_client_address}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsInsightsConfig.__init__)
            check_type(argname="argument query_insights_enabled", value=query_insights_enabled, expected_type=type_hints["query_insights_enabled"])
            check_type(argname="argument query_string_length", value=query_string_length, expected_type=type_hints["query_string_length"])
            check_type(argname="argument record_application_tags", value=record_application_tags, expected_type=type_hints["record_application_tags"])
            check_type(argname="argument record_client_address", value=record_client_address, expected_type=type_hints["record_client_address"])
        self._values: typing.Dict[str, typing.Any] = {}
        if query_insights_enabled is not None:
            self._values["query_insights_enabled"] = query_insights_enabled
        if query_string_length is not None:
            self._values["query_string_length"] = query_string_length
        if record_application_tags is not None:
            self._values["record_application_tags"] = record_application_tags
        if record_client_address is not None:
            self._values["record_client_address"] = record_client_address

    @builtins.property
    def query_insights_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if Query Insights feature is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#query_insights_enabled GoogleSqlDatabaseInstance#query_insights_enabled}
        '''
        result = self._values.get("query_insights_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def query_string_length(self) -> typing.Optional[jsii.Number]:
        '''Maximum query length stored in bytes. Between 256 and 4500. Default to 1024.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#query_string_length GoogleSqlDatabaseInstance#query_string_length}
        '''
        result = self._values.get("query_string_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def record_application_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if Query Insights will record application tags from query when enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#record_application_tags GoogleSqlDatabaseInstance#record_application_tags}
        '''
        result = self._values.get("record_application_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def record_client_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if Query Insights will record client address when enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#record_client_address GoogleSqlDatabaseInstance#record_client_address}
        '''
        result = self._values.get("record_client_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsInsightsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetQueryInsightsEnabled")
    def reset_query_insights_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryInsightsEnabled", []))

    @jsii.member(jsii_name="resetQueryStringLength")
    def reset_query_string_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringLength", []))

    @jsii.member(jsii_name="resetRecordApplicationTags")
    def reset_record_application_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordApplicationTags", []))

    @jsii.member(jsii_name="resetRecordClientAddress")
    def reset_record_client_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordClientAddress", []))

    @builtins.property
    @jsii.member(jsii_name="queryInsightsEnabledInput")
    def query_insights_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "queryInsightsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringLengthInput")
    def query_string_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queryStringLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="recordApplicationTagsInput")
    def record_application_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "recordApplicationTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="recordClientAddressInput")
    def record_client_address_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "recordClientAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInsightsEnabled")
    def query_insights_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "queryInsightsEnabled"))

    @query_insights_enabled.setter
    def query_insights_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference, "query_insights_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryInsightsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringLength")
    def query_string_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queryStringLength"))

    @query_string_length.setter
    def query_string_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference, "query_string_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringLength", value)

    @builtins.property
    @jsii.member(jsii_name="recordApplicationTags")
    def record_application_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "recordApplicationTags"))

    @record_application_tags.setter
    def record_application_tags(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference, "record_application_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordApplicationTags", value)

    @builtins.property
    @jsii.member(jsii_name="recordClientAddress")
    def record_client_address(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "recordClientAddress"))

    @record_client_address.setter
    def record_client_address(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference, "record_client_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordClientAddress", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsInsightsConfig]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsInsightsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsInsightsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "allocated_ip_range": "allocatedIpRange",
        "authorized_networks": "authorizedNetworks",
        "ipv4_enabled": "ipv4Enabled",
        "private_network": "privateNetwork",
        "require_ssl": "requireSsl",
    },
)
class GoogleSqlDatabaseInstanceSettingsIpConfiguration:
    def __init__(
        self,
        *,
        allocated_ip_range: typing.Optional[builtins.str] = None,
        authorized_networks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks", typing.Dict[str, typing.Any]]]]] = None,
        ipv4_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_network: typing.Optional[builtins.str] = None,
        require_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allocated_ip_range: The name of the allocated ip range for the private ip CloudSQL instance. For example: "google-managed-services-default". If set, the instance ip will be created in the allocated range. The range name must comply with RFC 1035. Specifically, the name must be 1-63 characters long and match the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#allocated_ip_range GoogleSqlDatabaseInstance#allocated_ip_range}
        :param authorized_networks: authorized_networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#authorized_networks GoogleSqlDatabaseInstance#authorized_networks}
        :param ipv4_enabled: Whether this Cloud SQL instance should be assigned a public IPV4 address. At least ipv4_enabled must be enabled or a private_network must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ipv4_enabled GoogleSqlDatabaseInstance#ipv4_enabled}
        :param private_network: The VPC network from which the Cloud SQL instance is accessible for private IP. For example, projects/myProject/global/networks/default. Specifying a network enables private IP. At least ipv4_enabled must be enabled or a private_network must be configured. This setting can be updated, but it cannot be removed after it is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#private_network GoogleSqlDatabaseInstance#private_network}
        :param require_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#require_ssl GoogleSqlDatabaseInstance#require_ssl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsIpConfiguration.__init__)
            check_type(argname="argument allocated_ip_range", value=allocated_ip_range, expected_type=type_hints["allocated_ip_range"])
            check_type(argname="argument authorized_networks", value=authorized_networks, expected_type=type_hints["authorized_networks"])
            check_type(argname="argument ipv4_enabled", value=ipv4_enabled, expected_type=type_hints["ipv4_enabled"])
            check_type(argname="argument private_network", value=private_network, expected_type=type_hints["private_network"])
            check_type(argname="argument require_ssl", value=require_ssl, expected_type=type_hints["require_ssl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allocated_ip_range is not None:
            self._values["allocated_ip_range"] = allocated_ip_range
        if authorized_networks is not None:
            self._values["authorized_networks"] = authorized_networks
        if ipv4_enabled is not None:
            self._values["ipv4_enabled"] = ipv4_enabled
        if private_network is not None:
            self._values["private_network"] = private_network
        if require_ssl is not None:
            self._values["require_ssl"] = require_ssl

    @builtins.property
    def allocated_ip_range(self) -> typing.Optional[builtins.str]:
        '''The name of the allocated ip range for the private ip CloudSQL instance.

        For example: "google-managed-services-default". If set, the instance ip will be created in the allocated range. The range name must comply with RFC 1035. Specifically, the name must be 1-63 characters long and match the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#allocated_ip_range GoogleSqlDatabaseInstance#allocated_ip_range}
        '''
        result = self._values.get("allocated_ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorized_networks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks"]]]:
        '''authorized_networks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#authorized_networks GoogleSqlDatabaseInstance#authorized_networks}
        '''
        result = self._values.get("authorized_networks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks"]]], result)

    @builtins.property
    def ipv4_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this Cloud SQL instance should be assigned a public IPV4 address.

        At least ipv4_enabled must be enabled or a private_network must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ipv4_enabled GoogleSqlDatabaseInstance#ipv4_enabled}
        '''
        result = self._values.get("ipv4_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def private_network(self) -> typing.Optional[builtins.str]:
        '''The VPC network from which the Cloud SQL instance is accessible for private IP.

        For example, projects/myProject/global/networks/default. Specifying a network enables private IP. At least ipv4_enabled must be enabled or a private_network must be configured. This setting can be updated, but it cannot be removed after it is set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#private_network GoogleSqlDatabaseInstance#private_network}
        '''
        result = self._values.get("private_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#require_ssl GoogleSqlDatabaseInstance#require_ssl}.'''
        result = self._values.get("require_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "expiration_time": "expirationTime",
        "name": "name",
    },
)
class GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks:
    def __init__(
        self,
        *,
        value: builtins.str,
        expiration_time: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#value GoogleSqlDatabaseInstance#value}.
        :param expiration_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#expiration_time GoogleSqlDatabaseInstance#expiration_time}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#name GoogleSqlDatabaseInstance#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument expiration_time", value=expiration_time, expected_type=type_hints["expiration_time"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if expiration_time is not None:
            self._values["expiration_time"] = expiration_time
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#value GoogleSqlDatabaseInstance#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expiration_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#expiration_time GoogleSqlDatabaseInstance#expiration_time}.'''
        result = self._values.get("expiration_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#name GoogleSqlDatabaseInstance#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpirationTime")
    def reset_expiration_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationTime", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeInput")
    def expiration_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTime")
    def expiration_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationTime"))

    @expiration_time.setter
    def expiration_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference, "expiration_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTime", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthorizedNetworks")
    def put_authorized_networks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference.put_authorized_networks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuthorizedNetworks", [value]))

    @jsii.member(jsii_name="resetAllocatedIpRange")
    def reset_allocated_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocatedIpRange", []))

    @jsii.member(jsii_name="resetAuthorizedNetworks")
    def reset_authorized_networks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizedNetworks", []))

    @jsii.member(jsii_name="resetIpv4Enabled")
    def reset_ipv4_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4Enabled", []))

    @jsii.member(jsii_name="resetPrivateNetwork")
    def reset_private_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateNetwork", []))

    @jsii.member(jsii_name="resetRequireSsl")
    def reset_require_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireSsl", []))

    @builtins.property
    @jsii.member(jsii_name="authorizedNetworks")
    def authorized_networks(
        self,
    ) -> GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList, jsii.get(self, "authorizedNetworks"))

    @builtins.property
    @jsii.member(jsii_name="allocatedIpRangeInput")
    def allocated_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocatedIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizedNetworksInput")
    def authorized_networks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks]]], jsii.get(self, "authorizedNetworksInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4EnabledInput")
    def ipv4_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ipv4EnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="privateNetworkInput")
    def private_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="requireSslInput")
    def require_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireSslInput"))

    @builtins.property
    @jsii.member(jsii_name="allocatedIpRange")
    def allocated_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocatedIpRange"))

    @allocated_ip_range.setter
    def allocated_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference, "allocated_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatedIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Enabled")
    def ipv4_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ipv4Enabled"))

    @ipv4_enabled.setter
    def ipv4_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference, "ipv4_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Enabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateNetwork")
    def private_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateNetwork"))

    @private_network.setter
    def private_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference, "private_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="requireSsl")
    def require_ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireSsl"))

    @require_ssl.setter
    def require_ssl(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference, "require_ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireSsl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsIpConfiguration]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsIpConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsIpConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsLocationPreference",
    jsii_struct_bases=[],
    name_mapping={
        "follow_gae_application": "followGaeApplication",
        "secondary_zone": "secondaryZone",
        "zone": "zone",
    },
)
class GoogleSqlDatabaseInstanceSettingsLocationPreference:
    def __init__(
        self,
        *,
        follow_gae_application: typing.Optional[builtins.str] = None,
        secondary_zone: typing.Optional[builtins.str] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param follow_gae_application: A Google App Engine application whose zone to remain in. Must be in the same region as this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#follow_gae_application GoogleSqlDatabaseInstance#follow_gae_application}
        :param secondary_zone: The preferred Compute Engine zone for the secondary/failover. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#secondary_zone GoogleSqlDatabaseInstance#secondary_zone}
        :param zone: The preferred compute engine zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#zone GoogleSqlDatabaseInstance#zone}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsLocationPreference.__init__)
            check_type(argname="argument follow_gae_application", value=follow_gae_application, expected_type=type_hints["follow_gae_application"])
            check_type(argname="argument secondary_zone", value=secondary_zone, expected_type=type_hints["secondary_zone"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {}
        if follow_gae_application is not None:
            self._values["follow_gae_application"] = follow_gae_application
        if secondary_zone is not None:
            self._values["secondary_zone"] = secondary_zone
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def follow_gae_application(self) -> typing.Optional[builtins.str]:
        '''A Google App Engine application whose zone to remain in. Must be in the same region as this instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#follow_gae_application GoogleSqlDatabaseInstance#follow_gae_application}
        '''
        result = self._values.get("follow_gae_application")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_zone(self) -> typing.Optional[builtins.str]:
        '''The preferred Compute Engine zone for the secondary/failover.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#secondary_zone GoogleSqlDatabaseInstance#secondary_zone}
        '''
        result = self._values.get("secondary_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''The preferred compute engine zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#zone GoogleSqlDatabaseInstance#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsLocationPreference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFollowGaeApplication")
    def reset_follow_gae_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFollowGaeApplication", []))

    @jsii.member(jsii_name="resetSecondaryZone")
    def reset_secondary_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryZone", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @builtins.property
    @jsii.member(jsii_name="followGaeApplicationInput")
    def follow_gae_application_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "followGaeApplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryZoneInput")
    def secondary_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondaryZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="followGaeApplication")
    def follow_gae_application(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "followGaeApplication"))

    @follow_gae_application.setter
    def follow_gae_application(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference, "follow_gae_application").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "followGaeApplication", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryZone")
    def secondary_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryZone"))

    @secondary_zone.setter
    def secondary_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference, "secondary_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryZone", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsLocationPreference]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsLocationPreference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsLocationPreference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={"day": "day", "hour": "hour", "update_track": "updateTrack"},
)
class GoogleSqlDatabaseInstanceSettingsMaintenanceWindow:
    def __init__(
        self,
        *,
        day: typing.Optional[jsii.Number] = None,
        hour: typing.Optional[jsii.Number] = None,
        update_track: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param day: Day of week (1-7), starting on Monday. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#day GoogleSqlDatabaseInstance#day}
        :param hour: Hour of day (0-23), ignored if day not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#hour GoogleSqlDatabaseInstance#hour}
        :param update_track: Receive updates earlier (canary) or later (stable). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#update_track GoogleSqlDatabaseInstance#update_track}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsMaintenanceWindow.__init__)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument update_track", value=update_track, expected_type=type_hints["update_track"])
        self._values: typing.Dict[str, typing.Any] = {}
        if day is not None:
            self._values["day"] = day
        if hour is not None:
            self._values["hour"] = hour
        if update_track is not None:
            self._values["update_track"] = update_track

    @builtins.property
    def day(self) -> typing.Optional[jsii.Number]:
        '''Day of week (1-7), starting on Monday.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#day GoogleSqlDatabaseInstance#day}
        '''
        result = self._values.get("day")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def hour(self) -> typing.Optional[jsii.Number]:
        '''Hour of day (0-23), ignored if day not set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#hour GoogleSqlDatabaseInstance#hour}
        '''
        result = self._values.get("hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def update_track(self) -> typing.Optional[builtins.str]:
        '''Receive updates earlier (canary) or later (stable).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#update_track GoogleSqlDatabaseInstance#update_track}
        '''
        result = self._values.get("update_track")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDay")
    def reset_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDay", []))

    @jsii.member(jsii_name="resetHour")
    def reset_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHour", []))

    @jsii.member(jsii_name="resetUpdateTrack")
    def reset_update_track(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateTrack", []))

    @builtins.property
    @jsii.member(jsii_name="dayInput")
    def day_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dayInput"))

    @builtins.property
    @jsii.member(jsii_name="hourInput")
    def hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hourInput"))

    @builtins.property
    @jsii.member(jsii_name="updateTrackInput")
    def update_track_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateTrackInput"))

    @builtins.property
    @jsii.member(jsii_name="day")
    def day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "day"))

    @day.setter
    def day(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference, "day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "day", value)

    @builtins.property
    @jsii.member(jsii_name="hour")
    def hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hour"))

    @hour.setter
    def hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference, "hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hour", value)

    @builtins.property
    @jsii.member(jsii_name="updateTrack")
    def update_track(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTrack"))

    @update_track.setter
    def update_track(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference, "update_track").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateTrack", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsMaintenanceWindow]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleSqlDatabaseInstanceSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActiveDirectoryConfig")
    def put_active_directory_config(self, *, domain: builtins.str) -> None:
        '''
        :param domain: Domain name of the Active Directory for SQL Server (e.g., mydomain.com). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#domain GoogleSqlDatabaseInstance#domain}
        '''
        value = GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig(domain=domain)

        return typing.cast(None, jsii.invoke(self, "putActiveDirectoryConfig", [value]))

    @jsii.member(jsii_name="putBackupConfiguration")
    def put_backup_configuration(
        self,
        *,
        backup_retention_settings: typing.Optional[typing.Union[GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings, typing.Dict[str, typing.Any]]] = None,
        binary_log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        start_time: typing.Optional[builtins.str] = None,
        transaction_log_retention_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param backup_retention_settings: backup_retention_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#backup_retention_settings GoogleSqlDatabaseInstance#backup_retention_settings}
        :param binary_log_enabled: True if binary logging is enabled. If settings.backup_configuration.enabled is false, this must be as well. Can only be used with MySQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#binary_log_enabled GoogleSqlDatabaseInstance#binary_log_enabled}
        :param enabled: True if backup configuration is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#enabled GoogleSqlDatabaseInstance#enabled}
        :param location: Location of the backup configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#location GoogleSqlDatabaseInstance#location}
        :param point_in_time_recovery_enabled: True if Point-in-time recovery is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#point_in_time_recovery_enabled GoogleSqlDatabaseInstance#point_in_time_recovery_enabled}
        :param start_time: HH:MM format time indicating when backup configuration starts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#start_time GoogleSqlDatabaseInstance#start_time}
        :param transaction_log_retention_days: The number of days of transaction logs we retain for point in time restore, from 1-7. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#transaction_log_retention_days GoogleSqlDatabaseInstance#transaction_log_retention_days}
        '''
        value = GoogleSqlDatabaseInstanceSettingsBackupConfiguration(
            backup_retention_settings=backup_retention_settings,
            binary_log_enabled=binary_log_enabled,
            enabled=enabled,
            location=location,
            point_in_time_recovery_enabled=point_in_time_recovery_enabled,
            start_time=start_time,
            transaction_log_retention_days=transaction_log_retention_days,
        )

        return typing.cast(None, jsii.invoke(self, "putBackupConfiguration", [value]))

    @jsii.member(jsii_name="putDatabaseFlags")
    def put_database_flags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleSqlDatabaseInstanceSettingsDatabaseFlags, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsOutputReference.put_database_flags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDatabaseFlags", [value]))

    @jsii.member(jsii_name="putInsightsConfig")
    def put_insights_config(
        self,
        *,
        query_insights_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        query_string_length: typing.Optional[jsii.Number] = None,
        record_application_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        record_client_address: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param query_insights_enabled: True if Query Insights feature is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#query_insights_enabled GoogleSqlDatabaseInstance#query_insights_enabled}
        :param query_string_length: Maximum query length stored in bytes. Between 256 and 4500. Default to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#query_string_length GoogleSqlDatabaseInstance#query_string_length}
        :param record_application_tags: True if Query Insights will record application tags from query when enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#record_application_tags GoogleSqlDatabaseInstance#record_application_tags}
        :param record_client_address: True if Query Insights will record client address when enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#record_client_address GoogleSqlDatabaseInstance#record_client_address}
        '''
        value = GoogleSqlDatabaseInstanceSettingsInsightsConfig(
            query_insights_enabled=query_insights_enabled,
            query_string_length=query_string_length,
            record_application_tags=record_application_tags,
            record_client_address=record_client_address,
        )

        return typing.cast(None, jsii.invoke(self, "putInsightsConfig", [value]))

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        *,
        allocated_ip_range: typing.Optional[builtins.str] = None,
        authorized_networks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks, typing.Dict[str, typing.Any]]]]] = None,
        ipv4_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_network: typing.Optional[builtins.str] = None,
        require_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allocated_ip_range: The name of the allocated ip range for the private ip CloudSQL instance. For example: "google-managed-services-default". If set, the instance ip will be created in the allocated range. The range name must comply with RFC 1035. Specifically, the name must be 1-63 characters long and match the regular expression `a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#allocated_ip_range GoogleSqlDatabaseInstance#allocated_ip_range}
        :param authorized_networks: authorized_networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#authorized_networks GoogleSqlDatabaseInstance#authorized_networks}
        :param ipv4_enabled: Whether this Cloud SQL instance should be assigned a public IPV4 address. At least ipv4_enabled must be enabled or a private_network must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#ipv4_enabled GoogleSqlDatabaseInstance#ipv4_enabled}
        :param private_network: The VPC network from which the Cloud SQL instance is accessible for private IP. For example, projects/myProject/global/networks/default. Specifying a network enables private IP. At least ipv4_enabled must be enabled or a private_network must be configured. This setting can be updated, but it cannot be removed after it is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#private_network GoogleSqlDatabaseInstance#private_network}
        :param require_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#require_ssl GoogleSqlDatabaseInstance#require_ssl}.
        '''
        value = GoogleSqlDatabaseInstanceSettingsIpConfiguration(
            allocated_ip_range=allocated_ip_range,
            authorized_networks=authorized_networks,
            ipv4_enabled=ipv4_enabled,
            private_network=private_network,
            require_ssl=require_ssl,
        )

        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

    @jsii.member(jsii_name="putLocationPreference")
    def put_location_preference(
        self,
        *,
        follow_gae_application: typing.Optional[builtins.str] = None,
        secondary_zone: typing.Optional[builtins.str] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param follow_gae_application: A Google App Engine application whose zone to remain in. Must be in the same region as this instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#follow_gae_application GoogleSqlDatabaseInstance#follow_gae_application}
        :param secondary_zone: The preferred Compute Engine zone for the secondary/failover. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#secondary_zone GoogleSqlDatabaseInstance#secondary_zone}
        :param zone: The preferred compute engine zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#zone GoogleSqlDatabaseInstance#zone}
        '''
        value = GoogleSqlDatabaseInstanceSettingsLocationPreference(
            follow_gae_application=follow_gae_application,
            secondary_zone=secondary_zone,
            zone=zone,
        )

        return typing.cast(None, jsii.invoke(self, "putLocationPreference", [value]))

    @jsii.member(jsii_name="putMaintenanceWindow")
    def put_maintenance_window(
        self,
        *,
        day: typing.Optional[jsii.Number] = None,
        hour: typing.Optional[jsii.Number] = None,
        update_track: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param day: Day of week (1-7), starting on Monday. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#day GoogleSqlDatabaseInstance#day}
        :param hour: Hour of day (0-23), ignored if day not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#hour GoogleSqlDatabaseInstance#hour}
        :param update_track: Receive updates earlier (canary) or later (stable). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#update_track GoogleSqlDatabaseInstance#update_track}
        '''
        value = GoogleSqlDatabaseInstanceSettingsMaintenanceWindow(
            day=day, hour=hour, update_track=update_track
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindow", [value]))

    @jsii.member(jsii_name="putPasswordValidationPolicy")
    def put_password_validation_policy(
        self,
        *,
        enable_password_policy: typing.Union[builtins.bool, cdktf.IResolvable],
        complexity: typing.Optional[builtins.str] = None,
        disallow_username_substring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        min_length: typing.Optional[jsii.Number] = None,
        password_change_interval: typing.Optional[builtins.str] = None,
        reuse_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable_password_policy: Whether the password policy is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#enable_password_policy GoogleSqlDatabaseInstance#enable_password_policy}
        :param complexity: Password complexity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#complexity GoogleSqlDatabaseInstance#complexity}
        :param disallow_username_substring: Disallow username as a part of the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disallow_username_substring GoogleSqlDatabaseInstance#disallow_username_substring}
        :param min_length: Minimum number of characters allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#min_length GoogleSqlDatabaseInstance#min_length}
        :param password_change_interval: Minimum interval after which the password can be changed. This flag is only supported for PostgresSQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password_change_interval GoogleSqlDatabaseInstance#password_change_interval}
        :param reuse_interval: Number of previous passwords that cannot be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#reuse_interval GoogleSqlDatabaseInstance#reuse_interval}
        '''
        value = GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy(
            enable_password_policy=enable_password_policy,
            complexity=complexity,
            disallow_username_substring=disallow_username_substring,
            min_length=min_length,
            password_change_interval=password_change_interval,
            reuse_interval=reuse_interval,
        )

        return typing.cast(None, jsii.invoke(self, "putPasswordValidationPolicy", [value]))

    @jsii.member(jsii_name="putSqlServerAuditConfig")
    def put_sql_server_audit_config(
        self,
        *,
        bucket: builtins.str,
        retention_interval: typing.Optional[builtins.str] = None,
        upload_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: The name of the destination bucket (e.g., gs://mybucket). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#bucket GoogleSqlDatabaseInstance#bucket}
        :param retention_interval: How long to keep generated audit files. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retention_interval GoogleSqlDatabaseInstance#retention_interval}
        :param upload_interval: How often to upload generated audit files. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#upload_interval GoogleSqlDatabaseInstance#upload_interval}
        '''
        value = GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig(
            bucket=bucket,
            retention_interval=retention_interval,
            upload_interval=upload_interval,
        )

        return typing.cast(None, jsii.invoke(self, "putSqlServerAuditConfig", [value]))

    @jsii.member(jsii_name="resetActivationPolicy")
    def reset_activation_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivationPolicy", []))

    @jsii.member(jsii_name="resetActiveDirectoryConfig")
    def reset_active_directory_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectoryConfig", []))

    @jsii.member(jsii_name="resetAvailabilityType")
    def reset_availability_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityType", []))

    @jsii.member(jsii_name="resetBackupConfiguration")
    def reset_backup_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupConfiguration", []))

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetDatabaseFlags")
    def reset_database_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseFlags", []))

    @jsii.member(jsii_name="resetDiskAutoresize")
    def reset_disk_autoresize(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskAutoresize", []))

    @jsii.member(jsii_name="resetDiskAutoresizeLimit")
    def reset_disk_autoresize_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskAutoresizeLimit", []))

    @jsii.member(jsii_name="resetDiskSize")
    def reset_disk_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSize", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @jsii.member(jsii_name="resetInsightsConfig")
    def reset_insights_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsightsConfig", []))

    @jsii.member(jsii_name="resetIpConfiguration")
    def reset_ip_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpConfiguration", []))

    @jsii.member(jsii_name="resetLocationPreference")
    def reset_location_preference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationPreference", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetPasswordValidationPolicy")
    def reset_password_validation_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordValidationPolicy", []))

    @jsii.member(jsii_name="resetPricingPlan")
    def reset_pricing_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPricingPlan", []))

    @jsii.member(jsii_name="resetSqlServerAuditConfig")
    def reset_sql_server_audit_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlServerAuditConfig", []))

    @jsii.member(jsii_name="resetUserLabels")
    def reset_user_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserLabels", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryConfig")
    def active_directory_config(
        self,
    ) -> GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfigOutputReference:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfigOutputReference, jsii.get(self, "activeDirectoryConfig"))

    @builtins.property
    @jsii.member(jsii_name="backupConfiguration")
    def backup_configuration(
        self,
    ) -> GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference, jsii.get(self, "backupConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="databaseFlags")
    def database_flags(self) -> GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList, jsii.get(self, "databaseFlags"))

    @builtins.property
    @jsii.member(jsii_name="insightsConfig")
    def insights_config(
        self,
    ) -> GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference, jsii.get(self, "insightsConfig"))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(
        self,
    ) -> GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference, jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="locationPreference")
    def location_preference(
        self,
    ) -> GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference, jsii.get(self, "locationPreference"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference:
        return typing.cast(GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference, jsii.get(self, "maintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="passwordValidationPolicy")
    def password_validation_policy(
        self,
    ) -> "GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference":
        return typing.cast("GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference", jsii.get(self, "passwordValidationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="sqlServerAuditConfig")
    def sql_server_audit_config(
        self,
    ) -> "GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference":
        return typing.cast("GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference", jsii.get(self, "sqlServerAuditConfig"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="activationPolicyInput")
    def activation_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryConfigInput")
    def active_directory_config_input(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig], jsii.get(self, "activeDirectoryConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityTypeInput")
    def availability_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="backupConfigurationInput")
    def backup_configuration_input(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfiguration]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsBackupConfiguration], jsii.get(self, "backupConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseFlagsInput")
    def database_flags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsDatabaseFlags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleSqlDatabaseInstanceSettingsDatabaseFlags]]], jsii.get(self, "databaseFlagsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskAutoresizeInput")
    def disk_autoresize_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "diskAutoresizeInput"))

    @builtins.property
    @jsii.member(jsii_name="diskAutoresizeLimitInput")
    def disk_autoresize_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskAutoresizeLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeInput")
    def disk_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="insightsConfigInput")
    def insights_config_input(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsInsightsConfig]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsInsightsConfig], jsii.get(self, "insightsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsIpConfiguration]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsIpConfiguration], jsii.get(self, "ipConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="locationPreferenceInput")
    def location_preference_input(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsLocationPreference]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsLocationPreference], jsii.get(self, "locationPreferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsMaintenanceWindow]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsMaintenanceWindow], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordValidationPolicyInput")
    def password_validation_policy_input(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy"]:
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy"], jsii.get(self, "passwordValidationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="pricingPlanInput")
    def pricing_plan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlanInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlServerAuditConfigInput")
    def sql_server_audit_config_input(
        self,
    ) -> typing.Optional["GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig"]:
        return typing.cast(typing.Optional["GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig"], jsii.get(self, "sqlServerAuditConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="userLabelsInput")
    def user_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "userLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="activationPolicy")
    def activation_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activationPolicy"))

    @activation_policy.setter
    def activation_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "activation_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activationPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityType")
    def availability_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityType"))

    @availability_type.setter
    def availability_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "availability_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityType", value)

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "collation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="diskAutoresize")
    def disk_autoresize(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "diskAutoresize"))

    @disk_autoresize.setter
    def disk_autoresize(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "disk_autoresize").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskAutoresize", value)

    @builtins.property
    @jsii.member(jsii_name="diskAutoresizeLimit")
    def disk_autoresize_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskAutoresizeLimit"))

    @disk_autoresize_limit.setter
    def disk_autoresize_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "disk_autoresize_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskAutoresizeLimit", value)

    @builtins.property
    @jsii.member(jsii_name="diskSize")
    def disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSize"))

    @disk_size.setter
    def disk_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "disk_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSize", value)

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "pricing_plan").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlan", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="userLabels")
    def user_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "userLabels"))

    @user_labels.setter
    def user_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "user_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleSqlDatabaseInstanceSettings]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "enable_password_policy": "enablePasswordPolicy",
        "complexity": "complexity",
        "disallow_username_substring": "disallowUsernameSubstring",
        "min_length": "minLength",
        "password_change_interval": "passwordChangeInterval",
        "reuse_interval": "reuseInterval",
    },
)
class GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy:
    def __init__(
        self,
        *,
        enable_password_policy: typing.Union[builtins.bool, cdktf.IResolvable],
        complexity: typing.Optional[builtins.str] = None,
        disallow_username_substring: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        min_length: typing.Optional[jsii.Number] = None,
        password_change_interval: typing.Optional[builtins.str] = None,
        reuse_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable_password_policy: Whether the password policy is enabled or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#enable_password_policy GoogleSqlDatabaseInstance#enable_password_policy}
        :param complexity: Password complexity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#complexity GoogleSqlDatabaseInstance#complexity}
        :param disallow_username_substring: Disallow username as a part of the password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disallow_username_substring GoogleSqlDatabaseInstance#disallow_username_substring}
        :param min_length: Minimum number of characters allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#min_length GoogleSqlDatabaseInstance#min_length}
        :param password_change_interval: Minimum interval after which the password can be changed. This flag is only supported for PostgresSQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password_change_interval GoogleSqlDatabaseInstance#password_change_interval}
        :param reuse_interval: Number of previous passwords that cannot be reused. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#reuse_interval GoogleSqlDatabaseInstance#reuse_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy.__init__)
            check_type(argname="argument enable_password_policy", value=enable_password_policy, expected_type=type_hints["enable_password_policy"])
            check_type(argname="argument complexity", value=complexity, expected_type=type_hints["complexity"])
            check_type(argname="argument disallow_username_substring", value=disallow_username_substring, expected_type=type_hints["disallow_username_substring"])
            check_type(argname="argument min_length", value=min_length, expected_type=type_hints["min_length"])
            check_type(argname="argument password_change_interval", value=password_change_interval, expected_type=type_hints["password_change_interval"])
            check_type(argname="argument reuse_interval", value=reuse_interval, expected_type=type_hints["reuse_interval"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_password_policy": enable_password_policy,
        }
        if complexity is not None:
            self._values["complexity"] = complexity
        if disallow_username_substring is not None:
            self._values["disallow_username_substring"] = disallow_username_substring
        if min_length is not None:
            self._values["min_length"] = min_length
        if password_change_interval is not None:
            self._values["password_change_interval"] = password_change_interval
        if reuse_interval is not None:
            self._values["reuse_interval"] = reuse_interval

    @builtins.property
    def enable_password_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether the password policy is enabled or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#enable_password_policy GoogleSqlDatabaseInstance#enable_password_policy}
        '''
        result = self._values.get("enable_password_policy")
        assert result is not None, "Required property 'enable_password_policy' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def complexity(self) -> typing.Optional[builtins.str]:
        '''Password complexity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#complexity GoogleSqlDatabaseInstance#complexity}
        '''
        result = self._values.get("complexity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disallow_username_substring(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disallow username as a part of the password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#disallow_username_substring GoogleSqlDatabaseInstance#disallow_username_substring}
        '''
        result = self._values.get("disallow_username_substring")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def min_length(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of characters allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#min_length GoogleSqlDatabaseInstance#min_length}
        '''
        result = self._values.get("min_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_change_interval(self) -> typing.Optional[builtins.str]:
        '''Minimum interval after which the password can be changed. This flag is only supported for PostgresSQL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#password_change_interval GoogleSqlDatabaseInstance#password_change_interval}
        '''
        result = self._values.get("password_change_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reuse_interval(self) -> typing.Optional[jsii.Number]:
        '''Number of previous passwords that cannot be reused.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#reuse_interval GoogleSqlDatabaseInstance#reuse_interval}
        '''
        result = self._values.get("reuse_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComplexity")
    def reset_complexity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComplexity", []))

    @jsii.member(jsii_name="resetDisallowUsernameSubstring")
    def reset_disallow_username_substring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisallowUsernameSubstring", []))

    @jsii.member(jsii_name="resetMinLength")
    def reset_min_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinLength", []))

    @jsii.member(jsii_name="resetPasswordChangeInterval")
    def reset_password_change_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordChangeInterval", []))

    @jsii.member(jsii_name="resetReuseInterval")
    def reset_reuse_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReuseInterval", []))

    @builtins.property
    @jsii.member(jsii_name="complexityInput")
    def complexity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complexityInput"))

    @builtins.property
    @jsii.member(jsii_name="disallowUsernameSubstringInput")
    def disallow_username_substring_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disallowUsernameSubstringInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePasswordPolicyInput")
    def enable_password_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePasswordPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="minLengthInput")
    def min_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordChangeIntervalInput")
    def password_change_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordChangeIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="reuseIntervalInput")
    def reuse_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "reuseIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="complexity")
    def complexity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "complexity"))

    @complexity.setter
    def complexity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference, "complexity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "complexity", value)

    @builtins.property
    @jsii.member(jsii_name="disallowUsernameSubstring")
    def disallow_username_substring(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disallowUsernameSubstring"))

    @disallow_username_substring.setter
    def disallow_username_substring(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference, "disallow_username_substring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disallowUsernameSubstring", value)

    @builtins.property
    @jsii.member(jsii_name="enablePasswordPolicy")
    def enable_password_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enablePasswordPolicy"))

    @enable_password_policy.setter
    def enable_password_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference, "enable_password_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePasswordPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="minLength")
    def min_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minLength"))

    @min_length.setter
    def min_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference, "min_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLength", value)

    @builtins.property
    @jsii.member(jsii_name="passwordChangeInterval")
    def password_change_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordChangeInterval"))

    @password_change_interval.setter
    def password_change_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference, "password_change_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordChangeInterval", value)

    @builtins.property
    @jsii.member(jsii_name="reuseInterval")
    def reuse_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "reuseInterval"))

    @reuse_interval.setter
    def reuse_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference, "reuse_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reuseInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "retention_interval": "retentionInterval",
        "upload_interval": "uploadInterval",
    },
)
class GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        retention_interval: typing.Optional[builtins.str] = None,
        upload_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: The name of the destination bucket (e.g., gs://mybucket). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#bucket GoogleSqlDatabaseInstance#bucket}
        :param retention_interval: How long to keep generated audit files. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retention_interval GoogleSqlDatabaseInstance#retention_interval}
        :param upload_interval: How often to upload generated audit files. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#upload_interval GoogleSqlDatabaseInstance#upload_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument retention_interval", value=retention_interval, expected_type=type_hints["retention_interval"])
            check_type(argname="argument upload_interval", value=upload_interval, expected_type=type_hints["upload_interval"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if retention_interval is not None:
            self._values["retention_interval"] = retention_interval
        if upload_interval is not None:
            self._values["upload_interval"] = upload_interval

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The name of the destination bucket (e.g., gs://mybucket).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#bucket GoogleSqlDatabaseInstance#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_interval(self) -> typing.Optional[builtins.str]:
        '''How long to keep generated audit files.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"..

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#retention_interval GoogleSqlDatabaseInstance#retention_interval}
        '''
        result = self._values.get("retention_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upload_interval(self) -> typing.Optional[builtins.str]:
        '''How often to upload generated audit files.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#upload_interval GoogleSqlDatabaseInstance#upload_interval}
        '''
        result = self._values.get("upload_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRetentionInterval")
    def reset_retention_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionInterval", []))

    @jsii.member(jsii_name="resetUploadInterval")
    def reset_upload_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUploadInterval", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionIntervalInput")
    def retention_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retentionIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="uploadIntervalInput")
    def upload_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uploadIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInterval")
    def retention_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retentionInterval"))

    @retention_interval.setter
    def retention_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference, "retention_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInterval", value)

    @builtins.property
    @jsii.member(jsii_name="uploadInterval")
    def upload_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uploadInterval"))

    @upload_interval.setter
    def upload_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference, "upload_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uploadInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig]:
        return typing.cast(typing.Optional[GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleSqlDatabaseInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#create GoogleSqlDatabaseInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#delete GoogleSqlDatabaseInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#update GoogleSqlDatabaseInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#create GoogleSqlDatabaseInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#delete GoogleSqlDatabaseInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_sql_database_instance#update GoogleSqlDatabaseInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleSqlDatabaseInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleSqlDatabaseInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleSqlDatabaseInstance.GoogleSqlDatabaseInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleSqlDatabaseInstanceTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleSqlDatabaseInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleSqlDatabaseInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleSqlDatabaseInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleSqlDatabaseInstanceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleSqlDatabaseInstance",
    "GoogleSqlDatabaseInstanceClone",
    "GoogleSqlDatabaseInstanceCloneOutputReference",
    "GoogleSqlDatabaseInstanceConfig",
    "GoogleSqlDatabaseInstanceIpAddress",
    "GoogleSqlDatabaseInstanceIpAddressList",
    "GoogleSqlDatabaseInstanceIpAddressOutputReference",
    "GoogleSqlDatabaseInstanceReplicaConfiguration",
    "GoogleSqlDatabaseInstanceReplicaConfigurationOutputReference",
    "GoogleSqlDatabaseInstanceRestoreBackupContext",
    "GoogleSqlDatabaseInstanceRestoreBackupContextOutputReference",
    "GoogleSqlDatabaseInstanceServerCaCert",
    "GoogleSqlDatabaseInstanceServerCaCertList",
    "GoogleSqlDatabaseInstanceServerCaCertOutputReference",
    "GoogleSqlDatabaseInstanceSettings",
    "GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfig",
    "GoogleSqlDatabaseInstanceSettingsActiveDirectoryConfigOutputReference",
    "GoogleSqlDatabaseInstanceSettingsBackupConfiguration",
    "GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings",
    "GoogleSqlDatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsOutputReference",
    "GoogleSqlDatabaseInstanceSettingsBackupConfigurationOutputReference",
    "GoogleSqlDatabaseInstanceSettingsDatabaseFlags",
    "GoogleSqlDatabaseInstanceSettingsDatabaseFlagsList",
    "GoogleSqlDatabaseInstanceSettingsDatabaseFlagsOutputReference",
    "GoogleSqlDatabaseInstanceSettingsInsightsConfig",
    "GoogleSqlDatabaseInstanceSettingsInsightsConfigOutputReference",
    "GoogleSqlDatabaseInstanceSettingsIpConfiguration",
    "GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworks",
    "GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksList",
    "GoogleSqlDatabaseInstanceSettingsIpConfigurationAuthorizedNetworksOutputReference",
    "GoogleSqlDatabaseInstanceSettingsIpConfigurationOutputReference",
    "GoogleSqlDatabaseInstanceSettingsLocationPreference",
    "GoogleSqlDatabaseInstanceSettingsLocationPreferenceOutputReference",
    "GoogleSqlDatabaseInstanceSettingsMaintenanceWindow",
    "GoogleSqlDatabaseInstanceSettingsMaintenanceWindowOutputReference",
    "GoogleSqlDatabaseInstanceSettingsOutputReference",
    "GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicy",
    "GoogleSqlDatabaseInstanceSettingsPasswordValidationPolicyOutputReference",
    "GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfig",
    "GoogleSqlDatabaseInstanceSettingsSqlServerAuditConfigOutputReference",
    "GoogleSqlDatabaseInstanceTimeouts",
    "GoogleSqlDatabaseInstanceTimeoutsOutputReference",
]

publication.publish()
